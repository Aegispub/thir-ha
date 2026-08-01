# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-01 |
| **Generated At** | 2026-08-01T19:15:38Z |
| **Shift Time** | 19:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **378** |
| Confirmed Threats | **363** |
| False Positives Filtered | **15** (4.0%) |
| Unique Attacker IPs | **74** |
| Countries of Origin | **23** |
| High Severity Cases | **306** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **72** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **323** |
| Unique Credential Pairs | **291** |
| Unique Usernames | **131** |
| Unique Passwords | **180** |
| Successful Auth Pairs | **311** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 85 |
| `admin` | 18 |
| `user` | 11 |
| `support` | 7 |
| `test` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 21 |
| `1234` | 12 |
| `123` | 12 |
| `1` | 10 |
| `admin` | 10 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 7 |
| `root` | `` | 5 |
| `root` | `159357` | 5 |
| `root` | `smo@@kkklss` | 4 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `root` | `91.92.42.227` | 2026-08-01T16:55:08 |
| `root` | `P@ssw0rd` | `91.92.42.227` | 2026-08-01T16:55:14 |
| `root` | `Aa123321` | `91.92.42.227` | 2026-08-01T16:55:20 |
| `root` | `qwe123!@#` | `91.92.42.227` | 2026-08-01T16:55:26 |
| `root` | `r00t` | `91.92.42.227` | 2026-08-01T16:55:32 |
| `test` | `1` | `91.92.42.227` | 2026-08-01T16:55:38 |
| `csgo` | `csgo` | `91.92.42.227` | 2026-08-01T16:55:44 |
| `kafka` | `kafka` | `91.92.42.227` | 2026-08-01T16:55:50 |
| `milad` | `milad123` | `91.92.42.227` | 2026-08-01T16:55:56 |
| `root` | `00000000` | `91.92.42.227` | 2026-08-01T16:56:02 |
| `pi` | `1` | `91.92.42.227` | 2026-08-01T16:56:08 |
| `system` | `1qaz2wsx` | `91.92.42.227` | 2026-08-01T16:56:14 |
| `vncuser` | `vncuser` | `91.92.42.227` | 2026-08-01T16:56:20 |
| `oscar` | `1234` | `91.92.42.227` | 2026-08-01T16:56:26 |
| `git` | `123` | `91.92.42.227` | 2026-08-01T16:56:32 |
| `hu` | `123456` | `91.92.42.227` | 2026-08-01T16:56:38 |
| `dmdba` | `123456` | `91.92.42.227` | 2026-08-01T16:56:44 |
| `amir` | `amir` | `91.92.42.227` | 2026-08-01T16:56:50 |
| `devops` | `12345` | `91.92.42.227` | 2026-08-01T16:56:56 |
| `rdpuser` | `123` | `91.92.42.227` | 2026-08-01T16:57:02 |
| `root` | `p@ssw0rd` | `91.92.42.227` | 2026-08-01T16:57:08 |
| `root` | `redhat` | `91.92.42.227` | 2026-08-01T16:57:14 |
| `user` | `user` | `91.92.42.227` | 2026-08-01T16:57:20 |
| `admin` | `admin` | `47.88.0.49` | 2026-08-01T16:57:26 |
| `chenxi` | `123456` | `91.92.42.227` | 2026-08-01T16:57:27 |
| `appuser` | `password` | `91.92.42.227` | 2026-08-01T16:57:32 |
| `ai` | `toor` | `91.92.42.227` | 2026-08-01T16:57:39 |
| `root` | `eve` | `91.92.42.227` | 2026-08-01T16:57:45 |
| `root` | `!QAZ2wsx` | `91.92.42.227` | 2026-08-01T16:57:51 |
| `root` | `1Q2w3e4r` | `91.92.42.227` | 2026-08-01T16:57:58 |
| `root` | `1qaz@WSX` | `91.92.42.227` | 2026-08-01T16:58:04 |
| `debian` | `qwerty` | `91.92.42.227` | 2026-08-01T16:58:10 |
| `alex` | `alex` | `91.92.42.227` | 2026-08-01T16:58:17 |
| `ubuntu` | `admin@123` | `91.92.42.227` | 2026-08-01T16:58:23 |
| `root` | `aA123456` | `91.92.42.227` | 2026-08-01T16:58:29 |
| `root` | `root@123` | `91.92.42.227` | 2026-08-01T16:58:35 |
| `root` | `12345qwert` | `91.92.42.227` | 2026-08-01T16:58:41 |
| `root` | `19901017` | `91.92.42.227` | 2026-08-01T16:58:48 |
| `myuser` | `123456` | `91.92.42.227` | 2026-08-01T16:58:53 |
| `root` | `baidu123` | `91.92.42.227` | 2026-08-01T16:59:00 |
| `nobody` | `nobody` | `91.92.42.227` | 2026-08-01T16:59:06 |
| `runner` | `1` | `91.92.42.227` | 2026-08-01T16:59:12 |
| `test` | `test1234` | `91.92.42.227` | 2026-08-01T16:59:18 |
| `user1` | `root@123` | `91.92.42.227` | 2026-08-01T16:59:24 |
| `support` | `Passw0rd` | `91.92.42.227` | 2026-08-01T16:59:30 |
| `admin` | `123123` | `91.92.42.227` | 2026-08-01T16:59:35 |
| `config` | `config` | `91.92.42.227` | 2026-08-01T16:59:42 |
| `root` | `P@55w0rd` | `91.92.42.227` | 2026-08-01T16:59:48 |
| `sam` | `abc123` | `91.92.42.227` | 2026-08-01T16:59:54 |
| `solana` | `1234` | `91.92.42.227` | 2026-08-01T17:00:00 |
| `t1` | `123` | `91.92.42.227` | 2026-08-01T17:00:06 |
| `kingbase` | `kingbase` | `91.92.42.227` | 2026-08-01T17:00:12 |
| `test` | `passwd` | `91.92.42.227` | 2026-08-01T17:00:18 |
| `jack` | `1234` | `91.92.42.227` | 2026-08-01T17:00:24 |
| `pi` | `toor` | `91.92.42.227` | 2026-08-01T17:00:30 |
| `tester` | `password` | `91.92.42.227` | 2026-08-01T17:00:36 |
| `rdpuser` | `123456789` | `91.92.42.227` | 2026-08-01T17:00:42 |
| `gitlab` | `git` | `91.92.42.227` | 2026-08-01T17:00:48 |
| `debian` | `Aa123456.` | `91.92.42.227` | 2026-08-01T17:00:54 |
| `alex` | `12345678` | `91.92.42.227` | 2026-08-01T17:01:01 |
| `user` | `123456` | `91.92.42.227` | 2026-08-01T17:01:07 |
| `minecraft` | `1` | `91.92.42.227` | 2026-08-01T17:01:13 |
| `nexus` | `nexus` | `91.92.42.227` | 2026-08-01T17:01:19 |
| `azureuser` | `12345` | `91.92.42.227` | 2026-08-01T17:01:25 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-01T17:01:29 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-01T17:01:29 |
| `root` | `147258` | `91.92.42.227` | 2026-08-01T17:01:31 |
| `minecraft` | `123` | `91.92.42.227` | 2026-08-01T17:01:37 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-01T17:01:39 |
| `user` | `password` | `91.92.42.227` | 2026-08-01T17:01:43 |
| `root` | `admin@123` | `91.92.42.227` | 2026-08-01T17:01:49 |
| `admin` | `123456` | `91.92.42.227` | 2026-08-01T17:01:55 |
| `ali` | `ali` | `91.92.42.227` | 2026-08-01T17:02:01 |
| `odoo16` | `odoo16` | `91.92.42.227` | 2026-08-01T17:02:08 |
| `deploy` | `deploy` | `91.92.42.227` | 2026-08-01T17:02:13 |
| `core` | `P@ssw0rd` | `91.92.42.227` | 2026-08-01T17:02:19 |
| `main` | `12345` | `91.92.42.227` | 2026-08-01T17:02:25 |
| `root` | `P@ssword1` | `91.92.42.227` | 2026-08-01T17:02:31 |
| `root` | `welcome1` | `91.92.42.227` | 2026-08-01T17:02:37 |
| `hadoop` | `123` | `91.92.42.227` | 2026-08-01T17:02:43 |
| `ducc0x` | `phuvanduc` | `91.92.42.227` | 2026-08-01T17:02:49 |
| `root` | `zaq12wsx` | `91.92.42.227` | 2026-08-01T17:02:55 |
| `mysql` | `123456` | `91.92.42.227` | 2026-08-01T17:03:01 |
| `deployer` | `user` | `91.92.42.227` | 2026-08-01T17:03:07 |
| `fastuser` | `1234567890` | `91.92.42.227` | 2026-08-01T17:03:14 |
| `rock` | `rock` | `91.92.42.227` | 2026-08-01T17:03:20 |
| `testuser` | `testuser` | `91.92.42.227` | 2026-08-01T17:03:26 |
| `deploy` | `qwerty` | `91.92.42.227` | 2026-08-01T17:03:32 |
| `uploader` | `uploader` | `91.92.42.227` | 2026-08-01T17:03:38 |
| `user` | `123` | `91.92.42.227` | 2026-08-01T17:03:45 |
| `root` | `Aaaa1111` | `91.92.42.227` | 2026-08-01T17:03:51 |
| `dspace` | `dspace` | `91.92.42.227` | 2026-08-01T17:03:57 |
| `admin` | `Admin@123` | `91.92.42.227` | 2026-08-01T17:04:03 |
| `dev` | `dev` | `91.92.42.227` | 2026-08-01T17:04:09 |
| `kim` | `kim123` | `91.92.42.227` | 2026-08-01T17:04:15 |
| `root` | `momo123` | `91.92.42.227` | 2026-08-01T17:04:21 |
| `nobody` | `1234` | `91.92.42.227` | 2026-08-01T17:04:27 |
| `support` | `support8` | `10.0.0.73` | 2026-08-01T17:04:28 |
| `john` | `123456` | `91.92.42.227` | 2026-08-01T17:04:33 |
| `nagios` | `nagios` | `91.92.42.227` | 2026-08-01T17:04:39 |
| `ts` | `ts` | `91.92.42.227` | 2026-08-01T17:04:45 |
| `cloud` | `1234` | `91.92.42.227` | 2026-08-01T17:04:51 |
| `test` | `abc123` | `91.92.42.227` | 2026-08-01T17:04:57 |
| `ftp` | `123456` | `91.92.42.227` | 2026-08-01T17:05:03 |
| `root` | `qwe123!@` | `91.92.42.227` | 2026-08-01T17:05:09 |
| `root` | `q1w2e3r4` | `91.92.42.227` | 2026-08-01T17:05:15 |
| `user4` | `user4` | `91.92.42.227` | 2026-08-01T17:05:21 |
| `kipt` | `kipt` | `91.92.42.227` | 2026-08-01T17:05:27 |
| `frappe` | `admin` | `91.92.42.227` | 2026-08-01T17:05:33 |
| `git` | `git` | `91.92.42.227` | 2026-08-01T17:05:39 |
| `mc` | `mc` | `91.92.42.227` | 2026-08-01T17:05:46 |
| `cloud` | `cloud` | `91.92.42.227` | 2026-08-01T17:05:52 |
| `user` | `1111` | `91.92.42.227` | 2026-08-01T17:05:58 |
| `user` | `user123456` | `91.92.42.227` | 2026-08-01T17:06:04 |
| `teamspeak` | `1` | `91.92.42.227` | 2026-08-01T17:06:10 |
| `root` | `Welcome@123` | `91.92.42.227` | 2026-08-01T17:06:16 |
| `root` | `nimda` | `91.92.42.227` | 2026-08-01T17:06:22 |
| `support` | `support` | `176.53.159.196` | 2026-08-01T17:06:26 |
| `tom` | `111111` | `91.92.42.227` | 2026-08-01T17:06:28 |
| `myuser` | `root` | `91.92.42.227` | 2026-08-01T17:06:34 |
| `pi` | `p@ssw0rd` | `91.92.42.227` | 2026-08-01T17:06:41 |
| `admin` | `admin` | `91.92.42.227` | 2026-08-01T17:06:47 |
| `root` | `Pass1234` | `91.92.42.227` | 2026-08-01T17:06:53 |
| `user1` | `123` | `91.92.42.227` | 2026-08-01T17:06:59 |
| `developer` | `dev` | `91.92.42.227` | 2026-08-01T17:07:05 |
| `coder` | `123456` | `91.92.42.227` | 2026-08-01T17:07:11 |
| `deploy` | `123456789` | `91.92.42.227` | 2026-08-01T17:07:17 |
| `bernard` | `bernard` | `91.92.42.227` | 2026-08-01T17:07:23 |
| `nginx` | `toor` | `91.92.42.227` | 2026-08-01T17:07:29 |
| `claude` | `123` | `91.92.42.227` | 2026-08-01T17:07:35 |
| `runner` | `test` | `91.92.42.227` | 2026-08-01T17:07:41 |
| `deploy` | `123456` | `91.92.42.227` | 2026-08-01T17:07:47 |
| `user` | `passw0rd` | `91.92.42.227` | 2026-08-01T17:07:54 |
| `master` | `qwerty` | `91.92.42.227` | 2026-08-01T17:08:06 |
| `server` | `1234` | `91.92.42.227` | 2026-08-01T17:08:12 |
| `student` | `redhat` | `91.92.42.227` | 2026-08-01T17:08:19 |
| `rajvir` | `rajvir123` | `91.92.42.227` | 2026-08-01T17:08:25 |
| `deploy` | `password` | `91.92.42.227` | 2026-08-01T17:08:31 |
| `debian` | `123456789` | `91.92.42.227` | 2026-08-01T17:08:38 |
| `tactical` | `123456` | `91.92.42.227` | 2026-08-01T17:08:44 |
| `administrator` | `administrator` | `91.92.42.227` | 2026-08-01T17:08:49 |
| `huawei` | `Huawei12#$` | `77.90.185.20` | 2026-08-01T17:08:54 |
| `teamspeak` | `raspberry` | `91.92.42.227` | 2026-08-01T17:08:55 |
| `root` | `999` | `91.92.42.227` | 2026-08-01T17:09:01 |
| `data` | `test` | `91.92.42.227` | 2026-08-01T17:09:07 |
| `web` | `web123` | `91.92.42.227` | 2026-08-01T17:09:13 |
| `root` | `1029384756` | `91.92.42.227` | 2026-08-01T17:09:18 |
| `runner` | `1234` | `91.92.42.227` | 2026-08-01T17:09:24 |
| `oscar` | `oscar` | `91.92.42.227` | 2026-08-01T17:09:30 |
| `user` | `Aa123456` | `91.92.42.227` | 2026-08-01T17:09:36 |
| `opc` | `opc` | `91.92.42.227` | 2026-08-01T17:09:43 |
| `openvpn` | `openvpn` | `91.92.42.227` | 2026-08-01T17:09:49 |
| `ubuntu` | `12345678` | `91.92.42.227` | 2026-08-01T17:09:54 |
| `debian` | `debian` | `91.92.42.227` | 2026-08-01T17:10:01 |
| `ftp` | `ftp123` | `91.92.42.227` | 2026-08-01T17:10:06 |
| `openclaw` | `12345` | `91.92.42.227` | 2026-08-01T17:10:12 |
| `rocky` | `1` | `91.92.42.227` | 2026-08-01T17:10:18 |
| `test` | `12345678` | `91.92.42.227` | 2026-08-01T17:10:24 |
| `gd` | `gd` | `91.92.42.227` | 2026-08-01T17:10:30 |
| `security` | `security` | `91.92.42.227` | 2026-08-01T17:10:36 |
| `linuxuser` | `1` | `91.92.42.227` | 2026-08-01T17:10:42 |
| `manoj` | `manoj123` | `91.92.42.227` | 2026-08-01T17:10:48 |
| `teamspeak` | `root` | `91.92.42.227` | 2026-08-01T17:10:54 |
| `gpadmin` | `gpadmin` | `91.92.42.227` | 2026-08-01T17:11:00 |
| `ftp` | `ftp` | `91.92.42.227` | 2026-08-01T17:11:06 |
| `root` | `P@ssw0rd2026` | `91.92.42.227` | 2026-08-01T17:11:12 |
| `claude` | `12345678` | `91.92.42.227` | 2026-08-01T17:11:19 |
| `ubuntu` | `Aa123456` | `91.92.42.227` | 2026-08-01T17:11:25 |
| `onkar` | `onkar123` | `91.92.42.227` | 2026-08-01T17:11:31 |
| `root` | `AA123456` | `91.92.42.227` | 2026-08-01T17:11:37 |
| `student` | `123456` | `91.92.42.227` | 2026-08-01T17:11:43 |
| `hamed` | `hamed` | `91.92.42.227` | 2026-08-01T17:11:49 |
| `potok` | `potok` | `91.92.42.227` | 2026-08-01T17:11:55 |
| `daniel` | `daniel` | `91.92.42.227` | 2026-08-01T17:12:01 |
| `myuser` | `123` | `91.92.42.227` | 2026-08-01T17:12:07 |
| `root` | `1234567890` | `91.92.42.227` | 2026-08-01T17:12:13 |
| `ai` | `ai` | `91.92.42.227` | 2026-08-01T17:12:19 |
| `app` | `123` | `91.92.42.227` | 2026-08-01T17:12:25 |
| `a` | `a` | `91.92.42.227` | 2026-08-01T17:12:31 |
| `vagrant` | `vagrant` | `91.92.42.227` | 2026-08-01T17:12:37 |
| `ansible` | `passwd` | `91.92.42.227` | 2026-08-01T17:12:43 |
| `odoo` | `odoo` | `91.92.42.227` | 2026-08-01T17:12:49 |
| `root` | `nD6ffS9msOngs` | `91.92.42.227` | 2026-08-01T17:12:54 |
| `liyang` | `123456` | `91.92.42.227` | 2026-08-01T17:13:00 |
| `odoo14` | `odoo14` | `91.92.42.227` | 2026-08-01T17:13:06 |
| `mysql` | `mysql@1234` | `91.92.42.227` | 2026-08-01T17:13:11 |
| `root` | `qwe123` | `91.92.42.227` | 2026-08-01T17:13:17 |
| `root` | `dottie` | `59.46.182.10` | 2026-08-01T17:13:19 |
| `webuser` | `123456` | `91.92.42.227` | 2026-08-01T17:13:23 |
| `root` | `123qwe!@` | `91.92.42.227` | 2026-08-01T17:13:29 |
| `root` | `dottie` | `58.34.174.90` | 2026-08-01T17:13:30 |
| `pi` | `123456` | `91.92.42.227` | 2026-08-01T17:13:35 |
| `z` | `qwe123` | `91.92.42.227` | 2026-08-01T17:13:41 |
| `admin` | `root` | `91.92.42.227` | 2026-08-01T17:13:46 |
| `test1` | `123456789` | `91.92.42.227` | 2026-08-01T17:13:52 |
| `bot` | `root` | `91.92.42.227` | 2026-08-01T17:13:57 |
| `root` | `741852963` | `91.92.42.227` | 2026-08-01T17:14:03 |
| `ubuntu` | `1qaz@WSX` | `91.92.42.227` | 2026-08-01T17:16:35 |
| `master` | `123` | `91.92.42.227` | 2026-08-01T17:16:40 |
| `minecraft` | `123123` | `91.92.42.227` | 2026-08-01T17:16:42 |
| `admin` | `051178` | `91.92.42.227` | 2026-08-01T17:16:42 |
| `admin` | `111` | `91.92.42.227` | 2026-08-01T17:16:45 |
| `guest` | `guest` | `91.92.42.227` | 2026-08-01T17:16:50 |
| `root` | `admin` | `91.92.42.227` | 2026-08-01T17:16:56 |
| `root` | `Aa123456+` | `91.92.42.227` | 2026-08-01T17:17:02 |
| `john` | `john` | `91.92.42.227` | 2026-08-01T17:17:07 |
| `frappe` | `frappe` | `91.92.42.227` | 2026-08-01T17:17:13 |
| `debian` | `toor` | `91.92.42.227` | 2026-08-01T17:17:19 |
| `root` | `12345qwe` | `91.92.42.227` | 2026-08-01T17:17:25 |
| `mysql` | `mysql` | `91.92.42.227` | 2026-08-01T17:17:31 |
| `root` | `passw0rd` | `91.92.42.227` | 2026-08-01T17:17:37 |
| `root` | `rootrootroot` | `91.92.42.227` | 2026-08-01T17:17:43 |
| `pi` | `raspberry` | `91.92.42.227` | 2026-08-01T17:17:49 |
| `root` | `P@ssword` | `91.92.42.227` | 2026-08-01T17:17:54 |
| `root` | `hello123` | `91.92.42.227` | 2026-08-01T17:18:00 |
| `admin` | `0000` | `91.92.42.227` | 2026-08-01T17:18:07 |
| `kevin` | `kevin` | `91.92.42.227` | 2026-08-01T17:18:12 |
| `root` | `Aa123456.` | `91.92.42.227` | 2026-08-01T17:18:19 |
| `openclaw` | `user` | `91.92.42.227` | 2026-08-01T17:18:25 |
| `root` | `Test1234` | `91.92.42.227` | 2026-08-01T17:18:31 |
| `user1` | `123456789` | `91.92.42.227` | 2026-08-01T17:18:37 |
| `dev` | `123456` | `91.92.42.227` | 2026-08-01T17:18:44 |
| `root` | `Huawei123` | `91.92.42.227` | 2026-08-01T17:18:50 |
| `sdadmin` | `51nGleD` | `91.92.42.227` | 2026-08-01T17:18:56 |
| `user2` | `1` | `91.92.42.227` | 2026-08-01T17:19:03 |
| `amit` | `amit` | `91.92.42.227` | 2026-08-01T17:19:09 |
| `root` | `qwertyuiop` | `91.92.42.227` | 2026-08-01T17:19:15 |
| `admin` | `admin123!` | `91.92.42.227` | 2026-08-01T17:19:21 |
| `stack` | `stack` | `91.92.42.227` | 2026-08-01T17:19:27 |
| `crafty` | `12345678` | `91.92.42.227` | 2026-08-01T17:19:33 |
| `trade` | `123456` | `91.92.42.227` | 2026-08-01T17:19:40 |
| `root` | `1q2w3e4r5t6y` | `91.92.42.227` | 2026-08-01T17:19:46 |
| `test` | `123456` | `91.92.42.227` | 2026-08-01T17:19:52 |
| `root` | `t0talc0ntr0l4!` | `91.92.42.227` | 2026-08-01T17:19:58 |
| `root` | `huawei@123` | `91.92.42.227` | 2026-08-01T17:20:04 |
| `toto` | `toto` | `91.92.42.227` | 2026-08-01T17:20:10 |
| `user1` | `modzmodz` | `91.92.42.227` | 2026-08-01T17:20:16 |
| `user2` | `user2` | `91.92.42.227` | 2026-08-01T17:20:22 |
| `alex` | `1234` | `91.92.42.227` | 2026-08-01T17:20:28 |
| `admin` | `password` | `91.92.42.227` | 2026-08-01T17:20:34 |
| `postgres` | `postgres` | `91.92.42.227` | 2026-08-01T17:20:40 |
| `admin` | `1` | `91.92.42.227` | 2026-08-01T17:20:46 |
| `sam` | `1234` | `91.92.42.227` | 2026-08-01T17:20:52 |
| `bob` | `bob` | `91.92.42.227` | 2026-08-01T17:20:58 |
| `root` | `Admin@123` | `91.92.42.227` | 2026-08-01T17:21:04 |
| `ansible` | `ansible` | `91.92.42.227` | 2026-08-01T17:21:11 |
| `erp` | `erp` | `91.92.42.227` | 2026-08-01T17:21:17 |
| `frappe` | `12345678` | `91.92.42.227` | 2026-08-01T17:21:23 |
| `root` | `Password@123` | `91.92.42.227` | 2026-08-01T17:21:30 |
| `jay` | `jay` | `91.92.42.227` | 2026-08-01T17:21:35 |
| `fastuser` | `12345678` | `91.92.42.227` | 2026-08-01T17:21:42 |
| `guest` | `111111` | `91.92.42.227` | 2026-08-01T17:21:48 |
| `jack` | `jack` | `91.92.42.227` | 2026-08-01T17:21:54 |
| `odoo` | `123` | `91.92.42.227` | 2026-08-01T17:22:01 |
| `claude` | `1234` | `91.92.42.227` | 2026-08-01T17:22:07 |
| `root` | `Admin123!` | `91.92.42.227` | 2026-08-01T17:22:13 |
| `root` | `159357` | `182.76.71.82` | 2026-08-01T17:22:16 |
| `root` | `1234` | `163.192.48.255` | 2026-08-01T17:22:18 |
| `monitor` | `monitor` | `91.92.42.227` | 2026-08-01T17:22:20 |
| `dev` | `password` | `91.92.42.227` | 2026-08-01T17:22:25 |
| `gateway` | `gateway` | `91.92.42.227` | 2026-08-01T17:22:32 |
| `root` | `adminadmin` | `20.227.140.178` | 2026-08-01T17:22:32 |
| `www` | `user` | `91.92.42.227` | 2026-08-01T17:22:37 |
| `user` | `12345` | `91.92.42.227` | 2026-08-01T17:22:44 |
| `root` | `root123` | `91.92.42.227` | 2026-08-01T17:22:50 |
| `ghost` | `ghost` | `91.92.42.227` | 2026-08-01T17:22:56 |
| `guest` | `123456` | `91.92.42.227` | 2026-08-01T17:23:02 |
| `GET /..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd HTTP/1.1` | `Host: 129.80.119.236:2323` | `192.161.49.2` | 2026-08-01T17:23:06 |
| `newuser` | `qwerty` | `91.92.42.227` | 2026-08-01T17:23:08 |
| `support` | `support8` | `91.144.158.62` | 2026-08-01T17:23:14 |
| `deploy` | `admin` | `91.92.42.227` | 2026-08-01T17:23:15 |
| `user` | `qwe123456` | `91.92.42.227` | 2026-08-01T17:23:20 |
| `admin` | `!QAZ2wsx` | `91.92.42.227` | 2026-08-01T17:23:27 |
| `jenkins` | `1234` | `91.92.42.227` | 2026-08-01T17:23:34 |
| `postgres` | `1` | `91.92.42.227` | 2026-08-01T17:23:39 |
| `user1` | `12345` | `91.92.42.227` | 2026-08-01T17:23:45 |
| `lighthouse` | `lighthouse` | `91.92.42.227` | 2026-08-01T17:23:51 |
| `ubnt` | `ubnt66` | `201.63.52.54` | 2026-08-01T17:31:32 |
| `support` | `support` | `10.0.0.73` | 2026-08-01T17:31:42 |
| `ubnt` | `ubnt66` | `68.7.114.69` | 2026-08-01T17:31:44 |
| `root` | `159357` | `10.0.0.73` | 2026-08-01T17:34:11 |
| `Root` | `444444444` | `10.0.0.73` | 2026-08-01T17:38:58 |
| `root` | `` | `176.65.132.8` | 2026-08-01T17:44:31 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-01T17:45:37 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-01T17:45:37 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-01T17:45:46 |
| `ubnt` | `ubnt66` | `220.80.223.144` | 2026-08-01T17:48:12 |
| `ubnt` | `ubnt66` | `83.166.50.15` | 2026-08-01T17:48:24 |
| `root` | `159357` | `201.28.237.90` | 2026-08-01T17:51:51 |
| `root` | `159357` | `211.223.41.90` | 2026-08-01T17:52:04 |
| `Root` | `444444444` | `217.24.185.98` | 2026-08-01T17:57:55 |
| `admin` | `admin` | `45.43.37.254` | 2026-08-01T17:59:51 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-01T18:01:40 |
| `caja01` | `123456` | `107.150.100.146` | 2026-08-01T18:02:45 |
| `345gs5662d34` | `345gs5662d34` | `107.150.100.146` | 2026-08-01T18:02:47 |
| `caja01` | `3245gs5662d34` | `107.150.100.146` | 2026-08-01T18:02:47 |
| `root` | `administrator` | `20.227.140.178` | 2026-08-01T18:03:10 |
| `root` | `00001111` | `138.124.30.187` | 2026-08-01T18:05:17 |
| `345gs5662d34` | `345gs5662d34` | `138.124.30.187` | 2026-08-01T18:05:20 |
| `root` | `3245gs5662d34` | `138.124.30.187` | 2026-08-01T18:05:20 |
| `guest` | `guest11` | `10.0.0.73` | 2026-08-01T18:08:59 |
| `ubnt` | `ubnt77` | `10.0.0.73` | 2026-08-01T18:13:45 |
| `supervisor` | `99` | `60.174.35.18` | 2026-08-01T18:23:02 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-01T18:24:34 |
| `guest` | `guest11` | `203.252.10.3` | 2026-08-01T18:26:35 |
| `root` | `222222` | `194.31.8.12` | 2026-08-01T18:31:46 |
| `default` | `default10` | `10.0.0.73` | 2026-08-01T18:39:33 |
| `root` | `Administrator` | `20.227.140.178` | 2026-08-01T18:45:47 |
| `admin` | `admin` | `198.98.53.110` | 2026-08-01T18:48:59 |
| `admin` | `admin` | `121.40.20.65` | 2026-08-01T18:49:53 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-01T18:49:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **378** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 283 |
| OpenSSH | 14 |
| Paramiko (Python) | 8 |
| libssh | 7 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 265 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 14 | 14 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `16443846184e...` | Generic scanner | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 265 | 2 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 14 | 14 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 5 | 5 | — |
| `16443846184e...` | Go SSH scanner | 4 | 2 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 3 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `176.65.132.8`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `138.124.30.187`, `107.150.100.146`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **74** |
| Unique ASNs | **48** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS51396` | Pfcloud UG | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (306)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8d6900d725c1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:55 |
| **Last Seen** | 2026-08-01 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:55:07` | `cowrie.session.connect` |
| `2026-08-01 16:55:07` | `cowrie.client.version` |
| `2026-08-01 16:55:07` | `cowrie.client.kex` |
| `2026-08-01 16:55:08` | `cowrie.login.success` |
| `2026-08-01 16:55:09` | `cowrie.session.params` |
| `2026-08-01 16:55:09` | `cowrie.command.input` |
| `2026-08-01 16:55:09` | `cowrie.log.closed` |
| `2026-08-01 16:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08d0e098df17

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:55 |
| **Last Seen** | 2026-08-01 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:55:13` | `cowrie.session.connect` |
| `2026-08-01 16:55:13` | `cowrie.client.version` |
| `2026-08-01 16:55:13` | `cowrie.client.kex` |
| `2026-08-01 16:55:14` | `cowrie.login.success` |
| `2026-08-01 16:55:15` | `cowrie.session.params` |
| `2026-08-01 16:55:15` | `cowrie.command.input` |
| `2026-08-01 16:55:15` | `cowrie.log.closed` |
| `2026-08-01 16:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81b61e3e8395

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:55 |
| **Last Seen** | 2026-08-01 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:55:19` | `cowrie.session.connect` |
| `2026-08-01 16:55:19` | `cowrie.client.version` |
| `2026-08-01 16:55:19` | `cowrie.client.kex` |
| `2026-08-01 16:55:20` | `cowrie.login.success` |
| `2026-08-01 16:55:21` | `cowrie.session.params` |
| `2026-08-01 16:55:21` | `cowrie.command.input` |
| `2026-08-01 16:55:21` | `cowrie.log.closed` |
| `2026-08-01 16:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e1e7bcedca6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:55 |
| **Last Seen** | 2026-08-01 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:55:25` | `cowrie.session.connect` |
| `2026-08-01 16:55:25` | `cowrie.client.version` |
| `2026-08-01 16:55:25` | `cowrie.client.kex` |
| `2026-08-01 16:55:26` | `cowrie.login.success` |
| `2026-08-01 16:55:27` | `cowrie.session.params` |
| `2026-08-01 16:55:27` | `cowrie.command.input` |
| `2026-08-01 16:55:27` | `cowrie.log.closed` |
| `2026-08-01 16:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858198964811

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:55 |
| **Last Seen** | 2026-08-01 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:55:31` | `cowrie.session.connect` |
| `2026-08-01 16:55:31` | `cowrie.client.version` |
| `2026-08-01 16:55:31` | `cowrie.client.kex` |
| `2026-08-01 16:55:32` | `cowrie.login.success` |
| `2026-08-01 16:55:33` | `cowrie.session.params` |
| `2026-08-01 16:55:33` | `cowrie.command.input` |
| `2026-08-01 16:55:33` | `cowrie.log.closed` |
| `2026-08-01 16:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b2e8a4013dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:55 |
| **Last Seen** | 2026-08-01 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:55:37` | `cowrie.session.connect` |
| `2026-08-01 16:55:37` | `cowrie.client.version` |
| `2026-08-01 16:55:37` | `cowrie.client.kex` |
| `2026-08-01 16:55:38` | `cowrie.login.success` |
| `2026-08-01 16:55:39` | `cowrie.session.params` |
| `2026-08-01 16:55:39` | `cowrie.command.input` |
| `2026-08-01 16:55:39` | `cowrie.log.closed` |
| `2026-08-01 16:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df22a3e5f4a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:55 |
| **Last Seen** | 2026-08-01 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:55:43` | `cowrie.session.connect` |
| `2026-08-01 16:55:43` | `cowrie.client.version` |
| `2026-08-01 16:55:43` | `cowrie.client.kex` |
| `2026-08-01 16:55:44` | `cowrie.login.success` |
| `2026-08-01 16:55:45` | `cowrie.session.params` |
| `2026-08-01 16:55:45` | `cowrie.command.input` |
| `2026-08-01 16:55:45` | `cowrie.log.closed` |
| `2026-08-01 16:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e5b0e35643

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:55 |
| **Last Seen** | 2026-08-01 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:55:49` | `cowrie.session.connect` |
| `2026-08-01 16:55:49` | `cowrie.client.version` |
| `2026-08-01 16:55:49` | `cowrie.client.kex` |
| `2026-08-01 16:55:50` | `cowrie.login.success` |
| `2026-08-01 16:55:51` | `cowrie.session.params` |
| `2026-08-01 16:55:51` | `cowrie.command.input` |
| `2026-08-01 16:55:51` | `cowrie.log.closed` |
| `2026-08-01 16:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da0581ea8438

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:55 |
| **Last Seen** | 2026-08-01 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:55:55` | `cowrie.session.connect` |
| `2026-08-01 16:55:55` | `cowrie.client.version` |
| `2026-08-01 16:55:55` | `cowrie.client.kex` |
| `2026-08-01 16:55:56` | `cowrie.login.success` |
| `2026-08-01 16:55:57` | `cowrie.session.params` |
| `2026-08-01 16:55:57` | `cowrie.command.input` |
| `2026-08-01 16:55:57` | `cowrie.log.closed` |
| `2026-08-01 16:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8203f9e8a08

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:56 |
| **Last Seen** | 2026-08-01 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:56:01` | `cowrie.session.connect` |
| `2026-08-01 16:56:01` | `cowrie.client.version` |
| `2026-08-01 16:56:01` | `cowrie.client.kex` |
| `2026-08-01 16:56:02` | `cowrie.login.success` |
| `2026-08-01 16:56:03` | `cowrie.session.params` |
| `2026-08-01 16:56:03` | `cowrie.command.input` |
| `2026-08-01 16:56:03` | `cowrie.log.closed` |
| `2026-08-01 16:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74aa438eda5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:56 |
| **Last Seen** | 2026-08-01 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:56:07` | `cowrie.session.connect` |
| `2026-08-01 16:56:07` | `cowrie.client.version` |
| `2026-08-01 16:56:07` | `cowrie.client.kex` |
| `2026-08-01 16:56:08` | `cowrie.login.success` |
| `2026-08-01 16:56:09` | `cowrie.session.params` |
| `2026-08-01 16:56:09` | `cowrie.command.input` |
| `2026-08-01 16:56:09` | `cowrie.log.closed` |
| `2026-08-01 16:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6bbf942921

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:56 |
| **Last Seen** | 2026-08-01 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:56:13` | `cowrie.session.connect` |
| `2026-08-01 16:56:13` | `cowrie.client.version` |
| `2026-08-01 16:56:13` | `cowrie.client.kex` |
| `2026-08-01 16:56:14` | `cowrie.login.success` |
| `2026-08-01 16:56:15` | `cowrie.session.params` |
| `2026-08-01 16:56:15` | `cowrie.command.input` |
| `2026-08-01 16:56:15` | `cowrie.log.closed` |
| `2026-08-01 16:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5157bb6c2e20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:56 |
| **Last Seen** | 2026-08-01 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:56:19` | `cowrie.session.connect` |
| `2026-08-01 16:56:19` | `cowrie.client.version` |
| `2026-08-01 16:56:20` | `cowrie.client.kex` |
| `2026-08-01 16:56:20` | `cowrie.login.success` |
| `2026-08-01 16:56:21` | `cowrie.session.params` |
| `2026-08-01 16:56:21` | `cowrie.command.input` |
| `2026-08-01 16:56:21` | `cowrie.log.closed` |
| `2026-08-01 16:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-562e061e2730

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:56 |
| **Last Seen** | 2026-08-01 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:56:25` | `cowrie.session.connect` |
| `2026-08-01 16:56:26` | `cowrie.client.version` |
| `2026-08-01 16:56:26` | `cowrie.client.kex` |
| `2026-08-01 16:56:26` | `cowrie.login.success` |
| `2026-08-01 16:56:27` | `cowrie.session.params` |
| `2026-08-01 16:56:27` | `cowrie.command.input` |
| `2026-08-01 16:56:27` | `cowrie.log.closed` |
| `2026-08-01 16:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0397e8c2c97f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:56 |
| **Last Seen** | 2026-08-01 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:56:31` | `cowrie.session.connect` |
| `2026-08-01 16:56:31` | `cowrie.client.version` |
| `2026-08-01 16:56:31` | `cowrie.client.kex` |
| `2026-08-01 16:56:32` | `cowrie.login.success` |
| `2026-08-01 16:56:33` | `cowrie.session.params` |
| `2026-08-01 16:56:33` | `cowrie.command.input` |
| `2026-08-01 16:56:33` | `cowrie.log.closed` |
| `2026-08-01 16:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e0287d9b100

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:56 |
| **Last Seen** | 2026-08-01 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:56:37` | `cowrie.session.connect` |
| `2026-08-01 16:56:37` | `cowrie.client.version` |
| `2026-08-01 16:56:37` | `cowrie.client.kex` |
| `2026-08-01 16:56:38` | `cowrie.login.success` |
| `2026-08-01 16:56:39` | `cowrie.session.params` |
| `2026-08-01 16:56:39` | `cowrie.command.input` |
| `2026-08-01 16:56:39` | `cowrie.log.closed` |
| `2026-08-01 16:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-134039d7c4d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:56 |
| **Last Seen** | 2026-08-01 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:56:43` | `cowrie.session.connect` |
| `2026-08-01 16:56:44` | `cowrie.client.version` |
| `2026-08-01 16:56:44` | `cowrie.client.kex` |
| `2026-08-01 16:56:44` | `cowrie.login.success` |
| `2026-08-01 16:56:45` | `cowrie.session.params` |
| `2026-08-01 16:56:45` | `cowrie.command.input` |
| `2026-08-01 16:56:45` | `cowrie.log.closed` |
| `2026-08-01 16:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef20d32990b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:56 |
| **Last Seen** | 2026-08-01 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:56:50` | `cowrie.session.connect` |
| `2026-08-01 16:56:50` | `cowrie.client.version` |
| `2026-08-01 16:56:50` | `cowrie.client.kex` |
| `2026-08-01 16:56:50` | `cowrie.login.success` |
| `2026-08-01 16:56:51` | `cowrie.session.params` |
| `2026-08-01 16:56:51` | `cowrie.command.input` |
| `2026-08-01 16:56:51` | `cowrie.log.closed` |
| `2026-08-01 16:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7689c09548cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:56 |
| **Last Seen** | 2026-08-01 16:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:56:56` | `cowrie.session.connect` |
| `2026-08-01 16:56:56` | `cowrie.client.version` |
| `2026-08-01 16:56:56` | `cowrie.client.kex` |
| `2026-08-01 16:56:56` | `cowrie.login.success` |
| `2026-08-01 16:56:58` | `cowrie.session.params` |
| `2026-08-01 16:56:58` | `cowrie.command.input` |
| `2026-08-01 16:56:58` | `cowrie.log.closed` |
| `2026-08-01 16:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0061a18f44

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:01` | `cowrie.session.connect` |
| `2026-08-01 16:57:01` | `cowrie.client.version` |
| `2026-08-01 16:57:02` | `cowrie.client.kex` |
| `2026-08-01 16:57:02` | `cowrie.login.success` |
| `2026-08-01 16:57:03` | `cowrie.session.params` |
| `2026-08-01 16:57:03` | `cowrie.command.input` |
| `2026-08-01 16:57:03` | `cowrie.log.closed` |
| `2026-08-01 16:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f76532da11cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:07` | `cowrie.session.connect` |
| `2026-08-01 16:57:07` | `cowrie.client.version` |
| `2026-08-01 16:57:08` | `cowrie.client.kex` |
| `2026-08-01 16:57:08` | `cowrie.login.success` |
| `2026-08-01 16:57:09` | `cowrie.session.params` |
| `2026-08-01 16:57:09` | `cowrie.command.input` |
| `2026-08-01 16:57:09` | `cowrie.log.closed` |
| `2026-08-01 16:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd7322463ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:14` | `cowrie.session.connect` |
| `2026-08-01 16:57:14` | `cowrie.client.version` |
| `2026-08-01 16:57:14` | `cowrie.client.kex` |
| `2026-08-01 16:57:14` | `cowrie.login.success` |
| `2026-08-01 16:57:15` | `cowrie.session.params` |
| `2026-08-01 16:57:15` | `cowrie.command.input` |
| `2026-08-01 16:57:16` | `cowrie.log.closed` |
| `2026-08-01 16:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85ab3e51a6db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:20` | `cowrie.session.connect` |
| `2026-08-01 16:57:20` | `cowrie.client.version` |
| `2026-08-01 16:57:20` | `cowrie.client.kex` |
| `2026-08-01 16:57:20` | `cowrie.login.success` |
| `2026-08-01 16:57:21` | `cowrie.session.params` |
| `2026-08-01 16:57:21` | `cowrie.command.input` |
| `2026-08-01 16:57:21` | `cowrie.log.closed` |
| `2026-08-01 16:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d30cd09ef8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:26` | `cowrie.session.connect` |
| `2026-08-01 16:57:26` | `cowrie.client.version` |
| `2026-08-01 16:57:26` | `cowrie.client.kex` |
| `2026-08-01 16:57:27` | `cowrie.login.success` |
| `2026-08-01 16:57:28` | `cowrie.session.params` |
| `2026-08-01 16:57:28` | `cowrie.command.input` |
| `2026-08-01 16:57:28` | `cowrie.log.closed` |
| `2026-08-01 16:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cadc354fe104

| Field | Detail |
|---|---|
| **Source IP** | `47.88.0[.]49` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:26` | `cowrie.session.connect` |
| `2026-08-01 16:57:26` | `cowrie.telnet.option` |
| `2026-08-01 16:57:26` | `cowrie.telnet.option` |
| `2026-08-01 16:57:26` | `cowrie.login.success` |
| `2026-08-01 16:57:27` | `cowrie.session.params` |
| `2026-08-01 16:57:27` | `cowrie.telnet.option` |
| `2026-08-01 16:57:27` | `cowrie.telnet.option` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.failed` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.failed` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.failed` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.command.input` |
| `2026-08-01 16:57:27` | `cowrie.log.closed` |
| `2026-08-01 16:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.88.0[.]49` to AbuseIPDB if not already reported
- [ ] Block `47.88.0[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af0d2888aab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:32` | `cowrie.session.connect` |
| `2026-08-01 16:57:32` | `cowrie.client.version` |
| `2026-08-01 16:57:32` | `cowrie.client.kex` |
| `2026-08-01 16:57:32` | `cowrie.login.success` |
| `2026-08-01 16:57:33` | `cowrie.session.params` |
| `2026-08-01 16:57:33` | `cowrie.command.input` |
| `2026-08-01 16:57:33` | `cowrie.log.closed` |
| `2026-08-01 16:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb92bf5e4f38

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:38` | `cowrie.session.connect` |
| `2026-08-01 16:57:38` | `cowrie.client.version` |
| `2026-08-01 16:57:38` | `cowrie.client.kex` |
| `2026-08-01 16:57:39` | `cowrie.login.success` |
| `2026-08-01 16:57:41` | `cowrie.session.params` |
| `2026-08-01 16:57:41` | `cowrie.command.input` |
| `2026-08-01 16:57:41` | `cowrie.log.closed` |
| `2026-08-01 16:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c837ca481518

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:44` | `cowrie.session.connect` |
| `2026-08-01 16:57:44` | `cowrie.client.version` |
| `2026-08-01 16:57:44` | `cowrie.client.kex` |
| `2026-08-01 16:57:45` | `cowrie.login.success` |
| `2026-08-01 16:57:46` | `cowrie.session.params` |
| `2026-08-01 16:57:46` | `cowrie.command.input` |
| `2026-08-01 16:57:46` | `cowrie.log.closed` |
| `2026-08-01 16:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-089182a6eefa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:50` | `cowrie.session.connect` |
| `2026-08-01 16:57:50` | `cowrie.client.version` |
| `2026-08-01 16:57:50` | `cowrie.client.kex` |
| `2026-08-01 16:57:51` | `cowrie.login.success` |
| `2026-08-01 16:57:52` | `cowrie.session.params` |
| `2026-08-01 16:57:52` | `cowrie.command.input` |
| `2026-08-01 16:57:52` | `cowrie.log.closed` |
| `2026-08-01 16:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e231c451f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:57 |
| **Last Seen** | 2026-08-01 16:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:57:57` | `cowrie.session.connect` |
| `2026-08-01 16:57:57` | `cowrie.client.version` |
| `2026-08-01 16:57:57` | `cowrie.client.kex` |
| `2026-08-01 16:57:58` | `cowrie.login.success` |
| `2026-08-01 16:57:59` | `cowrie.session.params` |
| `2026-08-01 16:57:59` | `cowrie.command.input` |
| `2026-08-01 16:57:59` | `cowrie.log.closed` |
| `2026-08-01 16:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d042b91fe1e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:58 |
| **Last Seen** | 2026-08-01 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:58:03` | `cowrie.session.connect` |
| `2026-08-01 16:58:03` | `cowrie.client.version` |
| `2026-08-01 16:58:03` | `cowrie.client.kex` |
| `2026-08-01 16:58:04` | `cowrie.login.success` |
| `2026-08-01 16:58:05` | `cowrie.session.params` |
| `2026-08-01 16:58:05` | `cowrie.command.input` |
| `2026-08-01 16:58:05` | `cowrie.log.closed` |
| `2026-08-01 16:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-586beb17bdb8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:58 |
| **Last Seen** | 2026-08-01 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:58:10` | `cowrie.session.connect` |
| `2026-08-01 16:58:10` | `cowrie.client.version` |
| `2026-08-01 16:58:10` | `cowrie.client.kex` |
| `2026-08-01 16:58:10` | `cowrie.login.success` |
| `2026-08-01 16:58:11` | `cowrie.session.params` |
| `2026-08-01 16:58:11` | `cowrie.command.input` |
| `2026-08-01 16:58:12` | `cowrie.log.closed` |
| `2026-08-01 16:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a3f8ecc8124

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:58 |
| **Last Seen** | 2026-08-01 16:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:58:16` | `cowrie.session.connect` |
| `2026-08-01 16:58:16` | `cowrie.client.version` |
| `2026-08-01 16:58:16` | `cowrie.client.kex` |
| `2026-08-01 16:58:17` | `cowrie.login.success` |
| `2026-08-01 16:58:19` | `cowrie.session.params` |
| `2026-08-01 16:58:19` | `cowrie.command.input` |
| `2026-08-01 16:58:19` | `cowrie.log.closed` |
| `2026-08-01 16:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d46d9a8d68c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:58 |
| **Last Seen** | 2026-08-01 16:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:58:22` | `cowrie.session.connect` |
| `2026-08-01 16:58:22` | `cowrie.client.version` |
| `2026-08-01 16:58:22` | `cowrie.client.kex` |
| `2026-08-01 16:58:23` | `cowrie.login.success` |
| `2026-08-01 16:58:24` | `cowrie.session.params` |
| `2026-08-01 16:58:24` | `cowrie.command.input` |
| `2026-08-01 16:58:24` | `cowrie.log.closed` |
| `2026-08-01 16:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bef696cfda01

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:58 |
| **Last Seen** | 2026-08-01 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:58:28` | `cowrie.session.connect` |
| `2026-08-01 16:58:28` | `cowrie.client.version` |
| `2026-08-01 16:58:28` | `cowrie.client.kex` |
| `2026-08-01 16:58:29` | `cowrie.login.success` |
| `2026-08-01 16:58:30` | `cowrie.session.params` |
| `2026-08-01 16:58:30` | `cowrie.command.input` |
| `2026-08-01 16:58:30` | `cowrie.log.closed` |
| `2026-08-01 16:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad77b80d56c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:58 |
| **Last Seen** | 2026-08-01 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:58:34` | `cowrie.session.connect` |
| `2026-08-01 16:58:34` | `cowrie.client.version` |
| `2026-08-01 16:58:34` | `cowrie.client.kex` |
| `2026-08-01 16:58:35` | `cowrie.login.success` |
| `2026-08-01 16:58:36` | `cowrie.session.params` |
| `2026-08-01 16:58:36` | `cowrie.command.input` |
| `2026-08-01 16:58:36` | `cowrie.log.closed` |
| `2026-08-01 16:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e26d29565fbf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:58 |
| **Last Seen** | 2026-08-01 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:58:41` | `cowrie.session.connect` |
| `2026-08-01 16:58:41` | `cowrie.client.version` |
| `2026-08-01 16:58:41` | `cowrie.client.kex` |
| `2026-08-01 16:58:41` | `cowrie.login.success` |
| `2026-08-01 16:58:42` | `cowrie.session.params` |
| `2026-08-01 16:58:42` | `cowrie.command.input` |
| `2026-08-01 16:58:42` | `cowrie.log.closed` |
| `2026-08-01 16:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a122fe0165ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:58 |
| **Last Seen** | 2026-08-01 16:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:58:47` | `cowrie.session.connect` |
| `2026-08-01 16:58:47` | `cowrie.client.version` |
| `2026-08-01 16:58:47` | `cowrie.client.kex` |
| `2026-08-01 16:58:48` | `cowrie.login.success` |
| `2026-08-01 16:58:49` | `cowrie.session.params` |
| `2026-08-01 16:58:49` | `cowrie.command.input` |
| `2026-08-01 16:58:49` | `cowrie.log.closed` |
| `2026-08-01 16:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a1afe125a9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:58 |
| **Last Seen** | 2026-08-01 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:58:53` | `cowrie.session.connect` |
| `2026-08-01 16:58:53` | `cowrie.client.version` |
| `2026-08-01 16:58:53` | `cowrie.client.kex` |
| `2026-08-01 16:58:53` | `cowrie.login.success` |
| `2026-08-01 16:58:54` | `cowrie.session.params` |
| `2026-08-01 16:58:54` | `cowrie.command.input` |
| `2026-08-01 16:58:54` | `cowrie.log.closed` |
| `2026-08-01 16:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869fc3acf7af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:58 |
| **Last Seen** | 2026-08-01 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:58:59` | `cowrie.session.connect` |
| `2026-08-01 16:58:59` | `cowrie.client.version` |
| `2026-08-01 16:58:59` | `cowrie.client.kex` |
| `2026-08-01 16:59:00` | `cowrie.login.success` |
| `2026-08-01 16:59:00` | `cowrie.session.params` |
| `2026-08-01 16:59:00` | `cowrie.command.input` |
| `2026-08-01 16:59:01` | `cowrie.log.closed` |
| `2026-08-01 16:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7af5dfb87f25

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:59 |
| **Last Seen** | 2026-08-01 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:59:05` | `cowrie.session.connect` |
| `2026-08-01 16:59:05` | `cowrie.client.version` |
| `2026-08-01 16:59:05` | `cowrie.client.kex` |
| `2026-08-01 16:59:06` | `cowrie.login.success` |
| `2026-08-01 16:59:06` | `cowrie.session.params` |
| `2026-08-01 16:59:06` | `cowrie.command.input` |
| `2026-08-01 16:59:07` | `cowrie.log.closed` |
| `2026-08-01 16:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b654e8e70559

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:59 |
| **Last Seen** | 2026-08-01 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:59:11` | `cowrie.session.connect` |
| `2026-08-01 16:59:11` | `cowrie.client.version` |
| `2026-08-01 16:59:11` | `cowrie.client.kex` |
| `2026-08-01 16:59:12` | `cowrie.login.success` |
| `2026-08-01 16:59:12` | `cowrie.session.params` |
| `2026-08-01 16:59:12` | `cowrie.command.input` |
| `2026-08-01 16:59:13` | `cowrie.log.closed` |
| `2026-08-01 16:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91147ffb0c64

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:59 |
| **Last Seen** | 2026-08-01 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:59:17` | `cowrie.session.connect` |
| `2026-08-01 16:59:17` | `cowrie.client.version` |
| `2026-08-01 16:59:17` | `cowrie.client.kex` |
| `2026-08-01 16:59:18` | `cowrie.login.success` |
| `2026-08-01 16:59:19` | `cowrie.session.params` |
| `2026-08-01 16:59:19` | `cowrie.command.input` |
| `2026-08-01 16:59:19` | `cowrie.log.closed` |
| `2026-08-01 16:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f2dddb4066

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:59 |
| **Last Seen** | 2026-08-01 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:59:23` | `cowrie.session.connect` |
| `2026-08-01 16:59:23` | `cowrie.client.version` |
| `2026-08-01 16:59:23` | `cowrie.client.kex` |
| `2026-08-01 16:59:24` | `cowrie.login.success` |
| `2026-08-01 16:59:24` | `cowrie.session.params` |
| `2026-08-01 16:59:24` | `cowrie.command.input` |
| `2026-08-01 16:59:25` | `cowrie.log.closed` |
| `2026-08-01 16:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6915a183e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:59 |
| **Last Seen** | 2026-08-01 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:59:29` | `cowrie.session.connect` |
| `2026-08-01 16:59:29` | `cowrie.client.version` |
| `2026-08-01 16:59:29` | `cowrie.client.kex` |
| `2026-08-01 16:59:30` | `cowrie.login.success` |
| `2026-08-01 16:59:30` | `cowrie.session.params` |
| `2026-08-01 16:59:30` | `cowrie.command.input` |
| `2026-08-01 16:59:30` | `cowrie.log.closed` |
| `2026-08-01 16:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f9711054e3c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:59 |
| **Last Seen** | 2026-08-01 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:59:35` | `cowrie.session.connect` |
| `2026-08-01 16:59:35` | `cowrie.client.version` |
| `2026-08-01 16:59:35` | `cowrie.client.kex` |
| `2026-08-01 16:59:35` | `cowrie.login.success` |
| `2026-08-01 16:59:36` | `cowrie.session.params` |
| `2026-08-01 16:59:36` | `cowrie.command.input` |
| `2026-08-01 16:59:37` | `cowrie.log.closed` |
| `2026-08-01 16:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caeb58074c5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:59 |
| **Last Seen** | 2026-08-01 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:59:41` | `cowrie.session.connect` |
| `2026-08-01 16:59:41` | `cowrie.client.version` |
| `2026-08-01 16:59:41` | `cowrie.client.kex` |
| `2026-08-01 16:59:42` | `cowrie.login.success` |
| `2026-08-01 16:59:43` | `cowrie.session.params` |
| `2026-08-01 16:59:43` | `cowrie.command.input` |
| `2026-08-01 16:59:43` | `cowrie.log.closed` |
| `2026-08-01 16:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab55227ab7a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:59 |
| **Last Seen** | 2026-08-01 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:59:47` | `cowrie.session.connect` |
| `2026-08-01 16:59:47` | `cowrie.client.version` |
| `2026-08-01 16:59:47` | `cowrie.client.kex` |
| `2026-08-01 16:59:48` | `cowrie.login.success` |
| `2026-08-01 16:59:48` | `cowrie.session.params` |
| `2026-08-01 16:59:48` | `cowrie.command.input` |
| `2026-08-01 16:59:48` | `cowrie.log.closed` |
| `2026-08-01 16:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2639e48c0717

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:59 |
| **Last Seen** | 2026-08-01 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:59:53` | `cowrie.session.connect` |
| `2026-08-01 16:59:53` | `cowrie.client.version` |
| `2026-08-01 16:59:53` | `cowrie.client.kex` |
| `2026-08-01 16:59:54` | `cowrie.login.success` |
| `2026-08-01 16:59:55` | `cowrie.session.params` |
| `2026-08-01 16:59:55` | `cowrie.command.input` |
| `2026-08-01 16:59:55` | `cowrie.log.closed` |
| `2026-08-01 16:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fdbba851159

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 16:59 |
| **Last Seen** | 2026-08-01 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 16:59:59` | `cowrie.session.connect` |
| `2026-08-01 16:59:59` | `cowrie.client.version` |
| `2026-08-01 16:59:59` | `cowrie.client.kex` |
| `2026-08-01 17:00:00` | `cowrie.login.success` |
| `2026-08-01 17:00:01` | `cowrie.session.params` |
| `2026-08-01 17:00:01` | `cowrie.command.input` |
| `2026-08-01 17:00:01` | `cowrie.log.closed` |
| `2026-08-01 17:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3447006d5d0b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:00 |
| **Last Seen** | 2026-08-01 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:00:05` | `cowrie.session.connect` |
| `2026-08-01 17:00:05` | `cowrie.client.version` |
| `2026-08-01 17:00:05` | `cowrie.client.kex` |
| `2026-08-01 17:00:06` | `cowrie.login.success` |
| `2026-08-01 17:00:07` | `cowrie.session.params` |
| `2026-08-01 17:00:07` | `cowrie.command.input` |
| `2026-08-01 17:00:07` | `cowrie.log.closed` |
| `2026-08-01 17:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144e6797770c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:00 |
| **Last Seen** | 2026-08-01 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:00:11` | `cowrie.session.connect` |
| `2026-08-01 17:00:11` | `cowrie.client.version` |
| `2026-08-01 17:00:11` | `cowrie.client.kex` |
| `2026-08-01 17:00:12` | `cowrie.login.success` |
| `2026-08-01 17:00:13` | `cowrie.session.params` |
| `2026-08-01 17:00:13` | `cowrie.command.input` |
| `2026-08-01 17:00:13` | `cowrie.log.closed` |
| `2026-08-01 17:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-916ff70b0aba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:00 |
| **Last Seen** | 2026-08-01 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:00:17` | `cowrie.session.connect` |
| `2026-08-01 17:00:17` | `cowrie.client.version` |
| `2026-08-01 17:00:18` | `cowrie.client.kex` |
| `2026-08-01 17:00:18` | `cowrie.login.success` |
| `2026-08-01 17:00:19` | `cowrie.session.params` |
| `2026-08-01 17:00:19` | `cowrie.command.input` |
| `2026-08-01 17:00:19` | `cowrie.log.closed` |
| `2026-08-01 17:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2dc085cb89

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:00 |
| **Last Seen** | 2026-08-01 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:00:24` | `cowrie.session.connect` |
| `2026-08-01 17:00:24` | `cowrie.client.version` |
| `2026-08-01 17:00:24` | `cowrie.client.kex` |
| `2026-08-01 17:00:24` | `cowrie.login.success` |
| `2026-08-01 17:00:25` | `cowrie.session.params` |
| `2026-08-01 17:00:25` | `cowrie.command.input` |
| `2026-08-01 17:00:25` | `cowrie.log.closed` |
| `2026-08-01 17:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58d16a50df8f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:00 |
| **Last Seen** | 2026-08-01 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:00:30` | `cowrie.session.connect` |
| `2026-08-01 17:00:30` | `cowrie.client.version` |
| `2026-08-01 17:00:30` | `cowrie.client.kex` |
| `2026-08-01 17:00:30` | `cowrie.login.success` |
| `2026-08-01 17:00:31` | `cowrie.session.params` |
| `2026-08-01 17:00:31` | `cowrie.command.input` |
| `2026-08-01 17:00:31` | `cowrie.log.closed` |
| `2026-08-01 17:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ac4e8d579ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:00 |
| **Last Seen** | 2026-08-01 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:00:36` | `cowrie.session.connect` |
| `2026-08-01 17:00:36` | `cowrie.client.version` |
| `2026-08-01 17:00:36` | `cowrie.client.kex` |
| `2026-08-01 17:00:36` | `cowrie.login.success` |
| `2026-08-01 17:00:37` | `cowrie.session.params` |
| `2026-08-01 17:00:37` | `cowrie.command.input` |
| `2026-08-01 17:00:38` | `cowrie.log.closed` |
| `2026-08-01 17:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0030667806a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:00 |
| **Last Seen** | 2026-08-01 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:00:42` | `cowrie.session.connect` |
| `2026-08-01 17:00:42` | `cowrie.client.version` |
| `2026-08-01 17:00:42` | `cowrie.client.kex` |
| `2026-08-01 17:00:42` | `cowrie.login.success` |
| `2026-08-01 17:00:43` | `cowrie.session.params` |
| `2026-08-01 17:00:43` | `cowrie.command.input` |
| `2026-08-01 17:00:44` | `cowrie.log.closed` |
| `2026-08-01 17:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3226c5ab0369

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:00 |
| **Last Seen** | 2026-08-01 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:00:48` | `cowrie.session.connect` |
| `2026-08-01 17:00:48` | `cowrie.client.version` |
| `2026-08-01 17:00:48` | `cowrie.client.kex` |
| `2026-08-01 17:00:48` | `cowrie.login.success` |
| `2026-08-01 17:00:49` | `cowrie.session.params` |
| `2026-08-01 17:00:49` | `cowrie.command.input` |
| `2026-08-01 17:00:49` | `cowrie.log.closed` |
| `2026-08-01 17:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3437051dffc0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:00 |
| **Last Seen** | 2026-08-01 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:00:54` | `cowrie.session.connect` |
| `2026-08-01 17:00:54` | `cowrie.client.version` |
| `2026-08-01 17:00:54` | `cowrie.client.kex` |
| `2026-08-01 17:00:54` | `cowrie.login.success` |
| `2026-08-01 17:00:55` | `cowrie.session.params` |
| `2026-08-01 17:00:55` | `cowrie.command.input` |
| `2026-08-01 17:00:55` | `cowrie.log.closed` |
| `2026-08-01 17:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c0e86c65fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:00` | `cowrie.session.connect` |
| `2026-08-01 17:01:00` | `cowrie.client.version` |
| `2026-08-01 17:01:00` | `cowrie.client.kex` |
| `2026-08-01 17:01:01` | `cowrie.login.success` |
| `2026-08-01 17:01:02` | `cowrie.session.params` |
| `2026-08-01 17:01:02` | `cowrie.command.input` |
| `2026-08-01 17:01:02` | `cowrie.log.closed` |
| `2026-08-01 17:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be69c9cc7a73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:06` | `cowrie.session.connect` |
| `2026-08-01 17:01:06` | `cowrie.client.version` |
| `2026-08-01 17:01:06` | `cowrie.client.kex` |
| `2026-08-01 17:01:07` | `cowrie.login.success` |
| `2026-08-01 17:01:07` | `cowrie.session.params` |
| `2026-08-01 17:01:07` | `cowrie.command.input` |
| `2026-08-01 17:01:07` | `cowrie.log.closed` |
| `2026-08-01 17:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81b3db12fc37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:12` | `cowrie.session.connect` |
| `2026-08-01 17:01:12` | `cowrie.client.version` |
| `2026-08-01 17:01:12` | `cowrie.client.kex` |
| `2026-08-01 17:01:13` | `cowrie.login.success` |
| `2026-08-01 17:01:14` | `cowrie.session.params` |
| `2026-08-01 17:01:14` | `cowrie.command.input` |
| `2026-08-01 17:01:14` | `cowrie.log.closed` |
| `2026-08-01 17:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ec6dd98efd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:18` | `cowrie.session.connect` |
| `2026-08-01 17:01:18` | `cowrie.client.version` |
| `2026-08-01 17:01:18` | `cowrie.client.kex` |
| `2026-08-01 17:01:19` | `cowrie.login.success` |
| `2026-08-01 17:01:19` | `cowrie.session.params` |
| `2026-08-01 17:01:19` | `cowrie.command.input` |
| `2026-08-01 17:01:20` | `cowrie.log.closed` |
| `2026-08-01 17:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12b8f86dfc9f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:24` | `cowrie.session.connect` |
| `2026-08-01 17:01:24` | `cowrie.client.version` |
| `2026-08-01 17:01:24` | `cowrie.client.kex` |
| `2026-08-01 17:01:25` | `cowrie.login.success` |
| `2026-08-01 17:01:25` | `cowrie.session.params` |
| `2026-08-01 17:01:25` | `cowrie.command.input` |
| `2026-08-01 17:01:25` | `cowrie.log.closed` |
| `2026-08-01 17:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19fefd1795c9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:28` | `cowrie.session.connect` |
| `2026-08-01 17:01:28` | `cowrie.client.version` |
| `2026-08-01 17:01:28` | `cowrie.client.kex` |
| `2026-08-01 17:01:29` | `cowrie.login.success` |
| `2026-08-01 17:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3704ad831041

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:28` | `cowrie.session.connect` |
| `2026-08-01 17:01:28` | `cowrie.client.version` |
| `2026-08-01 17:01:29` | `cowrie.client.kex` |
| `2026-08-01 17:01:29` | `cowrie.login.success` |
| `2026-08-01 17:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c10764d88c52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:30` | `cowrie.session.connect` |
| `2026-08-01 17:01:30` | `cowrie.client.version` |
| `2026-08-01 17:01:30` | `cowrie.client.kex` |
| `2026-08-01 17:01:31` | `cowrie.login.success` |
| `2026-08-01 17:01:32` | `cowrie.session.params` |
| `2026-08-01 17:01:32` | `cowrie.command.input` |
| `2026-08-01 17:01:32` | `cowrie.log.closed` |
| `2026-08-01 17:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3228d6fc91c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:36` | `cowrie.session.connect` |
| `2026-08-01 17:01:36` | `cowrie.client.version` |
| `2026-08-01 17:01:36` | `cowrie.client.kex` |
| `2026-08-01 17:01:37` | `cowrie.login.success` |
| `2026-08-01 17:01:38` | `cowrie.session.params` |
| `2026-08-01 17:01:38` | `cowrie.command.input` |
| `2026-08-01 17:01:38` | `cowrie.log.closed` |
| `2026-08-01 17:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d00078ea48fa

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:38` | `cowrie.session.connect` |
| `2026-08-01 17:01:38` | `cowrie.client.version` |
| `2026-08-01 17:01:38` | `cowrie.client.kex` |
| `2026-08-01 17:01:39` | `cowrie.login.success` |
| `2026-08-01 17:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c06f543f8a6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:39` | `cowrie.session.connect` |
| `2026-08-01 17:01:39` | `cowrie.client.version` |
| `2026-08-01 17:01:39` | `cowrie.client.kex` |
| `2026-08-01 17:01:39` | `cowrie.login.success` |
| `2026-08-01 17:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcaa7d6bb66c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:42` | `cowrie.session.connect` |
| `2026-08-01 17:01:42` | `cowrie.client.version` |
| `2026-08-01 17:01:43` | `cowrie.client.kex` |
| `2026-08-01 17:01:43` | `cowrie.login.success` |
| `2026-08-01 17:01:44` | `cowrie.session.params` |
| `2026-08-01 17:01:44` | `cowrie.command.input` |
| `2026-08-01 17:01:44` | `cowrie.log.closed` |
| `2026-08-01 17:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463312b12810

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:48` | `cowrie.session.connect` |
| `2026-08-01 17:01:48` | `cowrie.client.version` |
| `2026-08-01 17:01:48` | `cowrie.client.kex` |
| `2026-08-01 17:01:49` | `cowrie.login.success` |
| `2026-08-01 17:01:50` | `cowrie.session.params` |
| `2026-08-01 17:01:50` | `cowrie.command.input` |
| `2026-08-01 17:01:50` | `cowrie.log.closed` |
| `2026-08-01 17:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-088170cdb4c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:01 |
| **Last Seen** | 2026-08-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:01:54` | `cowrie.session.connect` |
| `2026-08-01 17:01:54` | `cowrie.client.version` |
| `2026-08-01 17:01:55` | `cowrie.client.kex` |
| `2026-08-01 17:01:55` | `cowrie.login.success` |
| `2026-08-01 17:01:56` | `cowrie.session.params` |
| `2026-08-01 17:01:56` | `cowrie.command.input` |
| `2026-08-01 17:01:56` | `cowrie.log.closed` |
| `2026-08-01 17:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da90abb446f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:02 |
| **Last Seen** | 2026-08-01 17:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:02:00` | `cowrie.session.connect` |
| `2026-08-01 17:02:00` | `cowrie.client.version` |
| `2026-08-01 17:02:01` | `cowrie.client.kex` |
| `2026-08-01 17:02:01` | `cowrie.login.success` |
| `2026-08-01 17:02:02` | `cowrie.session.params` |
| `2026-08-01 17:02:02` | `cowrie.command.input` |
| `2026-08-01 17:02:02` | `cowrie.log.closed` |
| `2026-08-01 17:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4b5d32f8216

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:02 |
| **Last Seen** | 2026-08-01 17:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:02:07` | `cowrie.session.connect` |
| `2026-08-01 17:02:07` | `cowrie.client.version` |
| `2026-08-01 17:02:07` | `cowrie.client.kex` |
| `2026-08-01 17:02:08` | `cowrie.login.success` |
| `2026-08-01 17:02:09` | `cowrie.session.params` |
| `2026-08-01 17:02:09` | `cowrie.command.input` |
| `2026-08-01 17:02:09` | `cowrie.log.closed` |
| `2026-08-01 17:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a18311d627b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:02 |
| **Last Seen** | 2026-08-01 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:02:13` | `cowrie.session.connect` |
| `2026-08-01 17:02:13` | `cowrie.client.version` |
| `2026-08-01 17:02:13` | `cowrie.client.kex` |
| `2026-08-01 17:02:13` | `cowrie.login.success` |
| `2026-08-01 17:02:14` | `cowrie.session.params` |
| `2026-08-01 17:02:14` | `cowrie.command.input` |
| `2026-08-01 17:02:14` | `cowrie.log.closed` |
| `2026-08-01 17:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6004792a68f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:02 |
| **Last Seen** | 2026-08-01 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:02:19` | `cowrie.session.connect` |
| `2026-08-01 17:02:19` | `cowrie.client.version` |
| `2026-08-01 17:02:19` | `cowrie.client.kex` |
| `2026-08-01 17:02:19` | `cowrie.login.success` |
| `2026-08-01 17:02:20` | `cowrie.session.params` |
| `2026-08-01 17:02:20` | `cowrie.command.input` |
| `2026-08-01 17:02:21` | `cowrie.log.closed` |
| `2026-08-01 17:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892e553525d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:02 |
| **Last Seen** | 2026-08-01 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:02:25` | `cowrie.session.connect` |
| `2026-08-01 17:02:25` | `cowrie.client.version` |
| `2026-08-01 17:02:25` | `cowrie.client.kex` |
| `2026-08-01 17:02:25` | `cowrie.login.success` |
| `2026-08-01 17:02:26` | `cowrie.session.params` |
| `2026-08-01 17:02:26` | `cowrie.command.input` |
| `2026-08-01 17:02:26` | `cowrie.log.closed` |
| `2026-08-01 17:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724277f48581

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:02 |
| **Last Seen** | 2026-08-01 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:02:31` | `cowrie.session.connect` |
| `2026-08-01 17:02:31` | `cowrie.client.version` |
| `2026-08-01 17:02:31` | `cowrie.client.kex` |
| `2026-08-01 17:02:31` | `cowrie.login.success` |
| `2026-08-01 17:02:32` | `cowrie.session.params` |
| `2026-08-01 17:02:32` | `cowrie.command.input` |
| `2026-08-01 17:02:32` | `cowrie.log.closed` |
| `2026-08-01 17:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b23708ec63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:02 |
| **Last Seen** | 2026-08-01 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:02:37` | `cowrie.session.connect` |
| `2026-08-01 17:02:37` | `cowrie.client.version` |
| `2026-08-01 17:02:37` | `cowrie.client.kex` |
| `2026-08-01 17:02:37` | `cowrie.login.success` |
| `2026-08-01 17:02:38` | `cowrie.session.params` |
| `2026-08-01 17:02:38` | `cowrie.command.input` |
| `2026-08-01 17:02:38` | `cowrie.log.closed` |
| `2026-08-01 17:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f1ce80f2f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:02 |
| **Last Seen** | 2026-08-01 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:02:43` | `cowrie.session.connect` |
| `2026-08-01 17:02:43` | `cowrie.client.version` |
| `2026-08-01 17:02:43` | `cowrie.client.kex` |
| `2026-08-01 17:02:43` | `cowrie.login.success` |
| `2026-08-01 17:02:44` | `cowrie.session.params` |
| `2026-08-01 17:02:44` | `cowrie.command.input` |
| `2026-08-01 17:02:44` | `cowrie.log.closed` |
| `2026-08-01 17:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cabd69a350b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:02 |
| **Last Seen** | 2026-08-01 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:02:49` | `cowrie.session.connect` |
| `2026-08-01 17:02:49` | `cowrie.client.version` |
| `2026-08-01 17:02:49` | `cowrie.client.kex` |
| `2026-08-01 17:02:49` | `cowrie.login.success` |
| `2026-08-01 17:02:50` | `cowrie.session.params` |
| `2026-08-01 17:02:50` | `cowrie.command.input` |
| `2026-08-01 17:02:50` | `cowrie.log.closed` |
| `2026-08-01 17:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a4d7cd2c05f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:02 |
| **Last Seen** | 2026-08-01 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:02:55` | `cowrie.session.connect` |
| `2026-08-01 17:02:55` | `cowrie.client.version` |
| `2026-08-01 17:02:55` | `cowrie.client.kex` |
| `2026-08-01 17:02:55` | `cowrie.login.success` |
| `2026-08-01 17:02:56` | `cowrie.session.params` |
| `2026-08-01 17:02:56` | `cowrie.command.input` |
| `2026-08-01 17:02:56` | `cowrie.log.closed` |
| `2026-08-01 17:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a62a938862e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:03 |
| **Last Seen** | 2026-08-01 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:03:01` | `cowrie.session.connect` |
| `2026-08-01 17:03:01` | `cowrie.client.version` |
| `2026-08-01 17:03:01` | `cowrie.client.kex` |
| `2026-08-01 17:03:01` | `cowrie.login.success` |
| `2026-08-01 17:03:02` | `cowrie.session.params` |
| `2026-08-01 17:03:02` | `cowrie.command.input` |
| `2026-08-01 17:03:03` | `cowrie.log.closed` |
| `2026-08-01 17:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cadd938aab55

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:03 |
| **Last Seen** | 2026-08-01 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:03:07` | `cowrie.session.connect` |
| `2026-08-01 17:03:07` | `cowrie.client.version` |
| `2026-08-01 17:03:07` | `cowrie.client.kex` |
| `2026-08-01 17:03:07` | `cowrie.login.success` |
| `2026-08-01 17:03:08` | `cowrie.session.params` |
| `2026-08-01 17:03:08` | `cowrie.command.input` |
| `2026-08-01 17:03:08` | `cowrie.log.closed` |
| `2026-08-01 17:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ae284c8b2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:03 |
| **Last Seen** | 2026-08-01 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:03:13` | `cowrie.session.connect` |
| `2026-08-01 17:03:13` | `cowrie.client.version` |
| `2026-08-01 17:03:13` | `cowrie.client.kex` |
| `2026-08-01 17:03:14` | `cowrie.login.success` |
| `2026-08-01 17:03:14` | `cowrie.session.params` |
| `2026-08-01 17:03:14` | `cowrie.command.input` |
| `2026-08-01 17:03:15` | `cowrie.log.closed` |
| `2026-08-01 17:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d9c5c59aa26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:03 |
| **Last Seen** | 2026-08-01 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:03:19` | `cowrie.session.connect` |
| `2026-08-01 17:03:19` | `cowrie.client.version` |
| `2026-08-01 17:03:20` | `cowrie.client.kex` |
| `2026-08-01 17:03:20` | `cowrie.login.success` |
| `2026-08-01 17:03:21` | `cowrie.session.params` |
| `2026-08-01 17:03:21` | `cowrie.command.input` |
| `2026-08-01 17:03:21` | `cowrie.log.closed` |
| `2026-08-01 17:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb787552486

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:03 |
| **Last Seen** | 2026-08-01 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:03:26` | `cowrie.session.connect` |
| `2026-08-01 17:03:26` | `cowrie.client.version` |
| `2026-08-01 17:03:26` | `cowrie.client.kex` |
| `2026-08-01 17:03:26` | `cowrie.login.success` |
| `2026-08-01 17:03:27` | `cowrie.session.params` |
| `2026-08-01 17:03:27` | `cowrie.command.input` |
| `2026-08-01 17:03:27` | `cowrie.log.closed` |
| `2026-08-01 17:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd9769c37b94

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:03 |
| **Last Seen** | 2026-08-01 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:03:32` | `cowrie.session.connect` |
| `2026-08-01 17:03:32` | `cowrie.client.version` |
| `2026-08-01 17:03:32` | `cowrie.client.kex` |
| `2026-08-01 17:03:32` | `cowrie.login.success` |
| `2026-08-01 17:03:33` | `cowrie.session.params` |
| `2026-08-01 17:03:33` | `cowrie.command.input` |
| `2026-08-01 17:03:33` | `cowrie.log.closed` |
| `2026-08-01 17:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f8658b81e65

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:03 |
| **Last Seen** | 2026-08-01 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:03:38` | `cowrie.session.connect` |
| `2026-08-01 17:03:38` | `cowrie.client.version` |
| `2026-08-01 17:03:38` | `cowrie.client.kex` |
| `2026-08-01 17:03:38` | `cowrie.login.success` |
| `2026-08-01 17:03:39` | `cowrie.session.params` |
| `2026-08-01 17:03:39` | `cowrie.command.input` |
| `2026-08-01 17:03:39` | `cowrie.log.closed` |
| `2026-08-01 17:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11bcf93b47d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:03 |
| **Last Seen** | 2026-08-01 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:03:44` | `cowrie.session.connect` |
| `2026-08-01 17:03:44` | `cowrie.client.version` |
| `2026-08-01 17:03:44` | `cowrie.client.kex` |
| `2026-08-01 17:03:45` | `cowrie.login.success` |
| `2026-08-01 17:03:45` | `cowrie.session.params` |
| `2026-08-01 17:03:45` | `cowrie.command.input` |
| `2026-08-01 17:03:46` | `cowrie.log.closed` |
| `2026-08-01 17:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e6363d5dc29

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:03 |
| **Last Seen** | 2026-08-01 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:03:50` | `cowrie.session.connect` |
| `2026-08-01 17:03:50` | `cowrie.client.version` |
| `2026-08-01 17:03:50` | `cowrie.client.kex` |
| `2026-08-01 17:03:51` | `cowrie.login.success` |
| `2026-08-01 17:03:51` | `cowrie.session.params` |
| `2026-08-01 17:03:51` | `cowrie.command.input` |
| `2026-08-01 17:03:51` | `cowrie.log.closed` |
| `2026-08-01 17:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8553bd2ba601

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:03 |
| **Last Seen** | 2026-08-01 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:03:56` | `cowrie.session.connect` |
| `2026-08-01 17:03:56` | `cowrie.client.version` |
| `2026-08-01 17:03:56` | `cowrie.client.kex` |
| `2026-08-01 17:03:57` | `cowrie.login.success` |
| `2026-08-01 17:03:58` | `cowrie.session.params` |
| `2026-08-01 17:03:58` | `cowrie.command.input` |
| `2026-08-01 17:03:58` | `cowrie.log.closed` |
| `2026-08-01 17:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-847b369af800

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:04 |
| **Last Seen** | 2026-08-01 17:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:04:02` | `cowrie.session.connect` |
| `2026-08-01 17:04:02` | `cowrie.client.version` |
| `2026-08-01 17:04:02` | `cowrie.client.kex` |
| `2026-08-01 17:04:03` | `cowrie.login.success` |
| `2026-08-01 17:04:04` | `cowrie.session.params` |
| `2026-08-01 17:04:04` | `cowrie.command.input` |
| `2026-08-01 17:04:04` | `cowrie.log.closed` |
| `2026-08-01 17:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-086bff9ebdd7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:04 |
| **Last Seen** | 2026-08-01 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:04:08` | `cowrie.session.connect` |
| `2026-08-01 17:04:08` | `cowrie.client.version` |
| `2026-08-01 17:04:08` | `cowrie.client.kex` |
| `2026-08-01 17:04:09` | `cowrie.login.success` |
| `2026-08-01 17:04:10` | `cowrie.session.params` |
| `2026-08-01 17:04:10` | `cowrie.command.input` |
| `2026-08-01 17:04:10` | `cowrie.log.closed` |
| `2026-08-01 17:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-972e1cc593b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:04 |
| **Last Seen** | 2026-08-01 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:04:14` | `cowrie.session.connect` |
| `2026-08-01 17:04:14` | `cowrie.client.version` |
| `2026-08-01 17:04:15` | `cowrie.client.kex` |
| `2026-08-01 17:04:15` | `cowrie.login.success` |
| `2026-08-01 17:04:16` | `cowrie.session.params` |
| `2026-08-01 17:04:16` | `cowrie.command.input` |
| `2026-08-01 17:04:16` | `cowrie.log.closed` |
| `2026-08-01 17:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52bf8ceb5630

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:04 |
| **Last Seen** | 2026-08-01 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:04:20` | `cowrie.session.connect` |
| `2026-08-01 17:04:20` | `cowrie.client.version` |
| `2026-08-01 17:04:20` | `cowrie.client.kex` |
| `2026-08-01 17:04:21` | `cowrie.login.success` |
| `2026-08-01 17:04:22` | `cowrie.session.params` |
| `2026-08-01 17:04:22` | `cowrie.command.input` |
| `2026-08-01 17:04:22` | `cowrie.log.closed` |
| `2026-08-01 17:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7be23a1c191d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:04 |
| **Last Seen** | 2026-08-01 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:04:26` | `cowrie.session.connect` |
| `2026-08-01 17:04:26` | `cowrie.client.version` |
| `2026-08-01 17:04:26` | `cowrie.client.kex` |
| `2026-08-01 17:04:27` | `cowrie.login.success` |
| `2026-08-01 17:04:28` | `cowrie.session.params` |
| `2026-08-01 17:04:28` | `cowrie.command.input` |
| `2026-08-01 17:04:28` | `cowrie.log.closed` |
| `2026-08-01 17:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49dcf6f76961

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:04 |
| **Last Seen** | 2026-08-01 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:04:32` | `cowrie.session.connect` |
| `2026-08-01 17:04:32` | `cowrie.client.version` |
| `2026-08-01 17:04:32` | `cowrie.client.kex` |
| `2026-08-01 17:04:33` | `cowrie.login.success` |
| `2026-08-01 17:04:34` | `cowrie.session.params` |
| `2026-08-01 17:04:34` | `cowrie.command.input` |
| `2026-08-01 17:04:34` | `cowrie.log.closed` |
| `2026-08-01 17:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-210a04c2d719

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:04 |
| **Last Seen** | 2026-08-01 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:04:38` | `cowrie.session.connect` |
| `2026-08-01 17:04:38` | `cowrie.client.version` |
| `2026-08-01 17:04:38` | `cowrie.client.kex` |
| `2026-08-01 17:04:39` | `cowrie.login.success` |
| `2026-08-01 17:04:40` | `cowrie.session.params` |
| `2026-08-01 17:04:40` | `cowrie.command.input` |
| `2026-08-01 17:04:40` | `cowrie.log.closed` |
| `2026-08-01 17:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-458228b1dc46

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:04 |
| **Last Seen** | 2026-08-01 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:04:44` | `cowrie.session.connect` |
| `2026-08-01 17:04:44` | `cowrie.client.version` |
| `2026-08-01 17:04:44` | `cowrie.client.kex` |
| `2026-08-01 17:04:45` | `cowrie.login.success` |
| `2026-08-01 17:04:46` | `cowrie.session.params` |
| `2026-08-01 17:04:46` | `cowrie.command.input` |
| `2026-08-01 17:04:46` | `cowrie.log.closed` |
| `2026-08-01 17:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-529bab9fc24f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:04 |
| **Last Seen** | 2026-08-01 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:04:50` | `cowrie.session.connect` |
| `2026-08-01 17:04:50` | `cowrie.client.version` |
| `2026-08-01 17:04:50` | `cowrie.client.kex` |
| `2026-08-01 17:04:51` | `cowrie.login.success` |
| `2026-08-01 17:04:52` | `cowrie.session.params` |
| `2026-08-01 17:04:52` | `cowrie.command.input` |
| `2026-08-01 17:04:52` | `cowrie.log.closed` |
| `2026-08-01 17:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44f3c5ec8dfa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:04 |
| **Last Seen** | 2026-08-01 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:04:56` | `cowrie.session.connect` |
| `2026-08-01 17:04:56` | `cowrie.client.version` |
| `2026-08-01 17:04:56` | `cowrie.client.kex` |
| `2026-08-01 17:04:57` | `cowrie.login.success` |
| `2026-08-01 17:04:57` | `cowrie.session.params` |
| `2026-08-01 17:04:57` | `cowrie.command.input` |
| `2026-08-01 17:04:57` | `cowrie.log.closed` |
| `2026-08-01 17:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47f97b9ce1c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:05 |
| **Last Seen** | 2026-08-01 17:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:05:02` | `cowrie.session.connect` |
| `2026-08-01 17:05:02` | `cowrie.client.version` |
| `2026-08-01 17:05:02` | `cowrie.client.kex` |
| `2026-08-01 17:05:03` | `cowrie.login.success` |
| `2026-08-01 17:05:04` | `cowrie.session.params` |
| `2026-08-01 17:05:04` | `cowrie.command.input` |
| `2026-08-01 17:05:05` | `cowrie.log.closed` |
| `2026-08-01 17:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad2344b7197

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:05 |
| **Last Seen** | 2026-08-01 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:05:08` | `cowrie.session.connect` |
| `2026-08-01 17:05:08` | `cowrie.client.version` |
| `2026-08-01 17:05:08` | `cowrie.client.kex` |
| `2026-08-01 17:05:09` | `cowrie.login.success` |
| `2026-08-01 17:05:09` | `cowrie.session.params` |
| `2026-08-01 17:05:09` | `cowrie.command.input` |
| `2026-08-01 17:05:10` | `cowrie.log.closed` |
| `2026-08-01 17:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8fa6dfd707

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:05 |
| **Last Seen** | 2026-08-01 17:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:05:14` | `cowrie.session.connect` |
| `2026-08-01 17:05:14` | `cowrie.client.version` |
| `2026-08-01 17:05:14` | `cowrie.client.kex` |
| `2026-08-01 17:05:15` | `cowrie.login.success` |
| `2026-08-01 17:05:16` | `cowrie.session.params` |
| `2026-08-01 17:05:16` | `cowrie.command.input` |
| `2026-08-01 17:05:16` | `cowrie.log.closed` |
| `2026-08-01 17:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33cf21ffa06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:05 |
| **Last Seen** | 2026-08-01 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:05:20` | `cowrie.session.connect` |
| `2026-08-01 17:05:20` | `cowrie.client.version` |
| `2026-08-01 17:05:20` | `cowrie.client.kex` |
| `2026-08-01 17:05:21` | `cowrie.login.success` |
| `2026-08-01 17:05:22` | `cowrie.session.params` |
| `2026-08-01 17:05:22` | `cowrie.command.input` |
| `2026-08-01 17:05:22` | `cowrie.log.closed` |
| `2026-08-01 17:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fa444ae4c41

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:05 |
| **Last Seen** | 2026-08-01 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:05:26` | `cowrie.session.connect` |
| `2026-08-01 17:05:26` | `cowrie.client.version` |
| `2026-08-01 17:05:26` | `cowrie.client.kex` |
| `2026-08-01 17:05:27` | `cowrie.login.success` |
| `2026-08-01 17:05:28` | `cowrie.session.params` |
| `2026-08-01 17:05:28` | `cowrie.command.input` |
| `2026-08-01 17:05:28` | `cowrie.log.closed` |
| `2026-08-01 17:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1729d6a54fa5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:05 |
| **Last Seen** | 2026-08-01 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:05:32` | `cowrie.session.connect` |
| `2026-08-01 17:05:32` | `cowrie.client.version` |
| `2026-08-01 17:05:32` | `cowrie.client.kex` |
| `2026-08-01 17:05:33` | `cowrie.login.success` |
| `2026-08-01 17:05:34` | `cowrie.session.params` |
| `2026-08-01 17:05:34` | `cowrie.command.input` |
| `2026-08-01 17:05:34` | `cowrie.log.closed` |
| `2026-08-01 17:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db86d4e46896

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:05 |
| **Last Seen** | 2026-08-01 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:05:39` | `cowrie.session.connect` |
| `2026-08-01 17:05:39` | `cowrie.client.version` |
| `2026-08-01 17:05:39` | `cowrie.client.kex` |
| `2026-08-01 17:05:39` | `cowrie.login.success` |
| `2026-08-01 17:05:40` | `cowrie.session.params` |
| `2026-08-01 17:05:40` | `cowrie.command.input` |
| `2026-08-01 17:05:40` | `cowrie.log.closed` |
| `2026-08-01 17:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e66307e9b412

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:05 |
| **Last Seen** | 2026-08-01 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:05:45` | `cowrie.session.connect` |
| `2026-08-01 17:05:45` | `cowrie.client.version` |
| `2026-08-01 17:05:45` | `cowrie.client.kex` |
| `2026-08-01 17:05:46` | `cowrie.login.success` |
| `2026-08-01 17:05:46` | `cowrie.session.params` |
| `2026-08-01 17:05:46` | `cowrie.command.input` |
| `2026-08-01 17:05:46` | `cowrie.log.closed` |
| `2026-08-01 17:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f715a8e64e8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:05 |
| **Last Seen** | 2026-08-01 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:05:51` | `cowrie.session.connect` |
| `2026-08-01 17:05:51` | `cowrie.client.version` |
| `2026-08-01 17:05:51` | `cowrie.client.kex` |
| `2026-08-01 17:05:52` | `cowrie.login.success` |
| `2026-08-01 17:05:52` | `cowrie.session.params` |
| `2026-08-01 17:05:52` | `cowrie.command.input` |
| `2026-08-01 17:05:53` | `cowrie.log.closed` |
| `2026-08-01 17:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-886612529afc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:05 |
| **Last Seen** | 2026-08-01 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:05:57` | `cowrie.session.connect` |
| `2026-08-01 17:05:57` | `cowrie.client.version` |
| `2026-08-01 17:05:57` | `cowrie.client.kex` |
| `2026-08-01 17:05:58` | `cowrie.login.success` |
| `2026-08-01 17:05:58` | `cowrie.session.params` |
| `2026-08-01 17:05:58` | `cowrie.command.input` |
| `2026-08-01 17:05:59` | `cowrie.log.closed` |
| `2026-08-01 17:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b865cc010228

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:03` | `cowrie.session.connect` |
| `2026-08-01 17:06:03` | `cowrie.client.version` |
| `2026-08-01 17:06:03` | `cowrie.client.kex` |
| `2026-08-01 17:06:04` | `cowrie.login.success` |
| `2026-08-01 17:06:04` | `cowrie.session.params` |
| `2026-08-01 17:06:04` | `cowrie.command.input` |
| `2026-08-01 17:06:05` | `cowrie.log.closed` |
| `2026-08-01 17:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75c9ac6ad43e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:10` | `cowrie.session.connect` |
| `2026-08-01 17:06:10` | `cowrie.client.version` |
| `2026-08-01 17:06:10` | `cowrie.client.kex` |
| `2026-08-01 17:06:10` | `cowrie.login.success` |
| `2026-08-01 17:06:11` | `cowrie.session.params` |
| `2026-08-01 17:06:11` | `cowrie.command.input` |
| `2026-08-01 17:06:11` | `cowrie.log.closed` |
| `2026-08-01 17:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d567f2cd1098

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:16` | `cowrie.session.connect` |
| `2026-08-01 17:06:16` | `cowrie.client.version` |
| `2026-08-01 17:06:16` | `cowrie.client.kex` |
| `2026-08-01 17:06:16` | `cowrie.login.success` |
| `2026-08-01 17:06:17` | `cowrie.session.params` |
| `2026-08-01 17:06:17` | `cowrie.command.input` |
| `2026-08-01 17:06:17` | `cowrie.log.closed` |
| `2026-08-01 17:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d064ed5127f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:22` | `cowrie.session.connect` |
| `2026-08-01 17:06:22` | `cowrie.client.version` |
| `2026-08-01 17:06:22` | `cowrie.client.kex` |
| `2026-08-01 17:06:22` | `cowrie.login.success` |
| `2026-08-01 17:06:23` | `cowrie.session.params` |
| `2026-08-01 17:06:23` | `cowrie.command.input` |
| `2026-08-01 17:06:23` | `cowrie.log.closed` |
| `2026-08-01 17:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6febed217d02

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:26` | `cowrie.session.connect` |
| `2026-08-01 17:06:26` | `cowrie.client.version` |
| `2026-08-01 17:06:26` | `cowrie.client.kex` |
| `2026-08-01 17:06:26` | `cowrie.login.success` |
| `2026-08-01 17:06:26` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:06:26` | `cowrie.direct-tcpip.data` |
| `2026-08-01 17:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cdb1ea4e928

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:28` | `cowrie.session.connect` |
| `2026-08-01 17:06:28` | `cowrie.client.version` |
| `2026-08-01 17:06:28` | `cowrie.client.kex` |
| `2026-08-01 17:06:28` | `cowrie.login.success` |
| `2026-08-01 17:06:29` | `cowrie.session.params` |
| `2026-08-01 17:06:29` | `cowrie.command.input` |
| `2026-08-01 17:06:29` | `cowrie.log.closed` |
| `2026-08-01 17:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2719f5d1b099

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:34` | `cowrie.session.connect` |
| `2026-08-01 17:06:34` | `cowrie.client.version` |
| `2026-08-01 17:06:34` | `cowrie.client.kex` |
| `2026-08-01 17:06:34` | `cowrie.login.success` |
| `2026-08-01 17:06:35` | `cowrie.session.params` |
| `2026-08-01 17:06:35` | `cowrie.command.input` |
| `2026-08-01 17:06:35` | `cowrie.log.closed` |
| `2026-08-01 17:06:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360ae4681a6c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:40` | `cowrie.session.connect` |
| `2026-08-01 17:06:40` | `cowrie.client.version` |
| `2026-08-01 17:06:40` | `cowrie.client.kex` |
| `2026-08-01 17:06:41` | `cowrie.login.success` |
| `2026-08-01 17:06:42` | `cowrie.session.params` |
| `2026-08-01 17:06:42` | `cowrie.command.input` |
| `2026-08-01 17:06:42` | `cowrie.log.closed` |
| `2026-08-01 17:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-711c3e500ae7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:46` | `cowrie.session.connect` |
| `2026-08-01 17:06:46` | `cowrie.client.version` |
| `2026-08-01 17:06:46` | `cowrie.client.kex` |
| `2026-08-01 17:06:47` | `cowrie.login.success` |
| `2026-08-01 17:06:48` | `cowrie.session.params` |
| `2026-08-01 17:06:48` | `cowrie.command.input` |
| `2026-08-01 17:06:48` | `cowrie.log.closed` |
| `2026-08-01 17:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37eb6db7f75

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:52` | `cowrie.session.connect` |
| `2026-08-01 17:06:52` | `cowrie.client.version` |
| `2026-08-01 17:06:52` | `cowrie.client.kex` |
| `2026-08-01 17:06:53` | `cowrie.login.success` |
| `2026-08-01 17:06:54` | `cowrie.session.params` |
| `2026-08-01 17:06:54` | `cowrie.command.input` |
| `2026-08-01 17:06:54` | `cowrie.log.closed` |
| `2026-08-01 17:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00fed5bc5350

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:06 |
| **Last Seen** | 2026-08-01 17:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:06:58` | `cowrie.session.connect` |
| `2026-08-01 17:06:58` | `cowrie.client.version` |
| `2026-08-01 17:06:58` | `cowrie.client.kex` |
| `2026-08-01 17:06:59` | `cowrie.login.success` |
| `2026-08-01 17:07:00` | `cowrie.session.params` |
| `2026-08-01 17:07:00` | `cowrie.command.input` |
| `2026-08-01 17:07:00` | `cowrie.log.closed` |
| `2026-08-01 17:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7297a32a27b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:07 |
| **Last Seen** | 2026-08-01 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:07:04` | `cowrie.session.connect` |
| `2026-08-01 17:07:04` | `cowrie.client.version` |
| `2026-08-01 17:07:04` | `cowrie.client.kex` |
| `2026-08-01 17:07:05` | `cowrie.login.success` |
| `2026-08-01 17:07:05` | `cowrie.session.params` |
| `2026-08-01 17:07:05` | `cowrie.command.input` |
| `2026-08-01 17:07:05` | `cowrie.log.closed` |
| `2026-08-01 17:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4455103e00f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:07 |
| **Last Seen** | 2026-08-01 17:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:07:10` | `cowrie.session.connect` |
| `2026-08-01 17:07:10` | `cowrie.client.version` |
| `2026-08-01 17:07:10` | `cowrie.client.kex` |
| `2026-08-01 17:07:11` | `cowrie.login.success` |
| `2026-08-01 17:07:12` | `cowrie.session.params` |
| `2026-08-01 17:07:12` | `cowrie.command.input` |
| `2026-08-01 17:07:12` | `cowrie.log.closed` |
| `2026-08-01 17:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19f16da7e3b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:07 |
| **Last Seen** | 2026-08-01 17:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:07:16` | `cowrie.session.connect` |
| `2026-08-01 17:07:16` | `cowrie.client.version` |
| `2026-08-01 17:07:16` | `cowrie.client.kex` |
| `2026-08-01 17:07:17` | `cowrie.login.success` |
| `2026-08-01 17:07:18` | `cowrie.session.params` |
| `2026-08-01 17:07:18` | `cowrie.command.input` |
| `2026-08-01 17:07:18` | `cowrie.log.closed` |
| `2026-08-01 17:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a29484ed85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:07 |
| **Last Seen** | 2026-08-01 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:07:22` | `cowrie.session.connect` |
| `2026-08-01 17:07:22` | `cowrie.client.version` |
| `2026-08-01 17:07:22` | `cowrie.client.kex` |
| `2026-08-01 17:07:23` | `cowrie.login.success` |
| `2026-08-01 17:07:24` | `cowrie.session.params` |
| `2026-08-01 17:07:24` | `cowrie.command.input` |
| `2026-08-01 17:07:24` | `cowrie.log.closed` |
| `2026-08-01 17:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2e072bafb2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:07 |
| **Last Seen** | 2026-08-01 17:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:07:28` | `cowrie.session.connect` |
| `2026-08-01 17:07:28` | `cowrie.client.version` |
| `2026-08-01 17:07:28` | `cowrie.client.kex` |
| `2026-08-01 17:07:29` | `cowrie.login.success` |
| `2026-08-01 17:07:30` | `cowrie.session.params` |
| `2026-08-01 17:07:30` | `cowrie.command.input` |
| `2026-08-01 17:07:30` | `cowrie.log.closed` |
| `2026-08-01 17:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57eb2b540ac4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:07 |
| **Last Seen** | 2026-08-01 17:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:07:34` | `cowrie.session.connect` |
| `2026-08-01 17:07:34` | `cowrie.client.version` |
| `2026-08-01 17:07:34` | `cowrie.client.kex` |
| `2026-08-01 17:07:35` | `cowrie.login.success` |
| `2026-08-01 17:07:36` | `cowrie.session.params` |
| `2026-08-01 17:07:36` | `cowrie.command.input` |
| `2026-08-01 17:07:36` | `cowrie.log.closed` |
| `2026-08-01 17:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b739bbe480

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:07 |
| **Last Seen** | 2026-08-01 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:07:41` | `cowrie.session.connect` |
| `2026-08-01 17:07:41` | `cowrie.client.version` |
| `2026-08-01 17:07:41` | `cowrie.client.kex` |
| `2026-08-01 17:07:41` | `cowrie.login.success` |
| `2026-08-01 17:07:42` | `cowrie.session.params` |
| `2026-08-01 17:07:42` | `cowrie.command.input` |
| `2026-08-01 17:07:42` | `cowrie.log.closed` |
| `2026-08-01 17:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f8a3b69ef1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:07 |
| **Last Seen** | 2026-08-01 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:07:47` | `cowrie.session.connect` |
| `2026-08-01 17:07:47` | `cowrie.client.version` |
| `2026-08-01 17:07:47` | `cowrie.client.kex` |
| `2026-08-01 17:07:47` | `cowrie.login.success` |
| `2026-08-01 17:07:48` | `cowrie.session.params` |
| `2026-08-01 17:07:48` | `cowrie.command.input` |
| `2026-08-01 17:07:48` | `cowrie.log.closed` |
| `2026-08-01 17:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a9e5d04bbb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:07 |
| **Last Seen** | 2026-08-01 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:07:53` | `cowrie.session.connect` |
| `2026-08-01 17:07:53` | `cowrie.client.version` |
| `2026-08-01 17:07:53` | `cowrie.client.kex` |
| `2026-08-01 17:07:54` | `cowrie.login.success` |
| `2026-08-01 17:07:55` | `cowrie.session.params` |
| `2026-08-01 17:07:55` | `cowrie.command.input` |
| `2026-08-01 17:07:55` | `cowrie.log.closed` |
| `2026-08-01 17:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a771f474ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:06` | `cowrie.session.connect` |
| `2026-08-01 17:08:06` | `cowrie.client.version` |
| `2026-08-01 17:08:06` | `cowrie.client.kex` |
| `2026-08-01 17:08:06` | `cowrie.login.success` |
| `2026-08-01 17:08:07` | `cowrie.session.params` |
| `2026-08-01 17:08:07` | `cowrie.command.input` |
| `2026-08-01 17:08:07` | `cowrie.log.closed` |
| `2026-08-01 17:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7d6fb152a74

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:12` | `cowrie.session.connect` |
| `2026-08-01 17:08:12` | `cowrie.client.version` |
| `2026-08-01 17:08:12` | `cowrie.client.kex` |
| `2026-08-01 17:08:12` | `cowrie.login.success` |
| `2026-08-01 17:08:13` | `cowrie.session.params` |
| `2026-08-01 17:08:13` | `cowrie.command.input` |
| `2026-08-01 17:08:14` | `cowrie.log.closed` |
| `2026-08-01 17:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ee1921fcd7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:18` | `cowrie.session.connect` |
| `2026-08-01 17:08:18` | `cowrie.client.version` |
| `2026-08-01 17:08:18` | `cowrie.client.kex` |
| `2026-08-01 17:08:19` | `cowrie.login.success` |
| `2026-08-01 17:08:19` | `cowrie.session.params` |
| `2026-08-01 17:08:19` | `cowrie.command.input` |
| `2026-08-01 17:08:19` | `cowrie.log.closed` |
| `2026-08-01 17:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ded8fbb941

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:24` | `cowrie.session.connect` |
| `2026-08-01 17:08:24` | `cowrie.client.version` |
| `2026-08-01 17:08:24` | `cowrie.client.kex` |
| `2026-08-01 17:08:25` | `cowrie.login.success` |
| `2026-08-01 17:08:26` | `cowrie.session.params` |
| `2026-08-01 17:08:26` | `cowrie.command.input` |
| `2026-08-01 17:08:26` | `cowrie.log.closed` |
| `2026-08-01 17:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb35bf1f7eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:31` | `cowrie.session.connect` |
| `2026-08-01 17:08:31` | `cowrie.client.version` |
| `2026-08-01 17:08:31` | `cowrie.client.kex` |
| `2026-08-01 17:08:31` | `cowrie.login.success` |
| `2026-08-01 17:08:32` | `cowrie.session.params` |
| `2026-08-01 17:08:32` | `cowrie.command.input` |
| `2026-08-01 17:08:32` | `cowrie.log.closed` |
| `2026-08-01 17:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fda02aeb587

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:37` | `cowrie.session.connect` |
| `2026-08-01 17:08:37` | `cowrie.client.version` |
| `2026-08-01 17:08:37` | `cowrie.client.kex` |
| `2026-08-01 17:08:38` | `cowrie.login.success` |
| `2026-08-01 17:08:39` | `cowrie.session.params` |
| `2026-08-01 17:08:39` | `cowrie.command.input` |
| `2026-08-01 17:08:39` | `cowrie.log.closed` |
| `2026-08-01 17:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b18f302fef70

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:08 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:41` | `cowrie.session.connect` |
| `2026-08-01 17:08:43` | `cowrie.client.version` |
| `2026-08-01 17:08:43` | `cowrie.client.kex` |
| `2026-08-01 17:08:54` | `cowrie.login.success` |
| `2026-08-01 17:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4912c533d8d6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:43` | `cowrie.session.connect` |
| `2026-08-01 17:08:43` | `cowrie.client.version` |
| `2026-08-01 17:08:43` | `cowrie.client.kex` |
| `2026-08-01 17:08:44` | `cowrie.login.success` |
| `2026-08-01 17:08:44` | `cowrie.session.params` |
| `2026-08-01 17:08:44` | `cowrie.command.input` |
| `2026-08-01 17:08:45` | `cowrie.log.closed` |
| `2026-08-01 17:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49fff292d7f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:49` | `cowrie.session.connect` |
| `2026-08-01 17:08:49` | `cowrie.client.version` |
| `2026-08-01 17:08:49` | `cowrie.client.kex` |
| `2026-08-01 17:08:49` | `cowrie.login.success` |
| `2026-08-01 17:08:50` | `cowrie.session.params` |
| `2026-08-01 17:08:50` | `cowrie.command.input` |
| `2026-08-01 17:08:50` | `cowrie.log.closed` |
| `2026-08-01 17:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94d27334ed81

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:55` | `cowrie.session.connect` |
| `2026-08-01 17:08:55` | `cowrie.client.version` |
| `2026-08-01 17:08:55` | `cowrie.client.kex` |
| `2026-08-01 17:08:55` | `cowrie.login.success` |
| `2026-08-01 17:08:56` | `cowrie.session.params` |
| `2026-08-01 17:08:56` | `cowrie.command.input` |
| `2026-08-01 17:08:56` | `cowrie.log.closed` |
| `2026-08-01 17:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4180d0baac46

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-01 17:08 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:08:59` | `cowrie.session.connect` |
| `2026-08-01 17:08:59` | `cowrie.client.version` |
| `2026-08-01 17:08:59` | `cowrie.client.kex` |
| `2026-08-01 17:09:00` | `cowrie.login.success` |
| `2026-08-01 17:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e6d93424b38

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:09 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:09:01` | `cowrie.session.connect` |
| `2026-08-01 17:09:01` | `cowrie.client.version` |
| `2026-08-01 17:09:01` | `cowrie.client.kex` |
| `2026-08-01 17:09:01` | `cowrie.login.success` |
| `2026-08-01 17:09:02` | `cowrie.session.params` |
| `2026-08-01 17:09:02` | `cowrie.command.input` |
| `2026-08-01 17:09:02` | `cowrie.log.closed` |
| `2026-08-01 17:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28b3797fdcfb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:09 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:09:06` | `cowrie.session.connect` |
| `2026-08-01 17:09:07` | `cowrie.client.version` |
| `2026-08-01 17:09:07` | `cowrie.client.kex` |
| `2026-08-01 17:09:07` | `cowrie.login.success` |
| `2026-08-01 17:09:08` | `cowrie.session.params` |
| `2026-08-01 17:09:08` | `cowrie.command.input` |
| `2026-08-01 17:09:08` | `cowrie.log.closed` |
| `2026-08-01 17:09:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6bace94bdbd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:09 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:09:12` | `cowrie.session.connect` |
| `2026-08-01 17:09:12` | `cowrie.client.version` |
| `2026-08-01 17:09:12` | `cowrie.client.kex` |
| `2026-08-01 17:09:13` | `cowrie.login.success` |
| `2026-08-01 17:09:14` | `cowrie.session.params` |
| `2026-08-01 17:09:14` | `cowrie.command.input` |
| `2026-08-01 17:09:14` | `cowrie.log.closed` |
| `2026-08-01 17:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106b4a43e23c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:09 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:09:18` | `cowrie.session.connect` |
| `2026-08-01 17:09:18` | `cowrie.client.version` |
| `2026-08-01 17:09:18` | `cowrie.client.kex` |
| `2026-08-01 17:09:18` | `cowrie.login.success` |
| `2026-08-01 17:09:19` | `cowrie.session.params` |
| `2026-08-01 17:09:19` | `cowrie.command.input` |
| `2026-08-01 17:09:20` | `cowrie.log.closed` |
| `2026-08-01 17:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d99a8e2ce4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:09 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:09:24` | `cowrie.session.connect` |
| `2026-08-01 17:09:24` | `cowrie.client.version` |
| `2026-08-01 17:09:24` | `cowrie.client.kex` |
| `2026-08-01 17:09:24` | `cowrie.login.success` |
| `2026-08-01 17:09:25` | `cowrie.session.params` |
| `2026-08-01 17:09:25` | `cowrie.command.input` |
| `2026-08-01 17:09:25` | `cowrie.log.closed` |
| `2026-08-01 17:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c8eea4445a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:09 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:09:30` | `cowrie.session.connect` |
| `2026-08-01 17:09:30` | `cowrie.client.version` |
| `2026-08-01 17:09:30` | `cowrie.client.kex` |
| `2026-08-01 17:09:30` | `cowrie.login.success` |
| `2026-08-01 17:09:31` | `cowrie.session.params` |
| `2026-08-01 17:09:31` | `cowrie.command.input` |
| `2026-08-01 17:09:31` | `cowrie.log.closed` |
| `2026-08-01 17:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f07331ea4ec6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:09 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:09:36` | `cowrie.session.connect` |
| `2026-08-01 17:09:36` | `cowrie.client.version` |
| `2026-08-01 17:09:36` | `cowrie.client.kex` |
| `2026-08-01 17:09:36` | `cowrie.login.success` |
| `2026-08-01 17:09:37` | `cowrie.session.params` |
| `2026-08-01 17:09:37` | `cowrie.command.input` |
| `2026-08-01 17:09:37` | `cowrie.log.closed` |
| `2026-08-01 17:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0636ac34cb9a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:09 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:09:42` | `cowrie.session.connect` |
| `2026-08-01 17:09:42` | `cowrie.client.version` |
| `2026-08-01 17:09:42` | `cowrie.client.kex` |
| `2026-08-01 17:09:43` | `cowrie.login.success` |
| `2026-08-01 17:09:43` | `cowrie.session.params` |
| `2026-08-01 17:09:43` | `cowrie.command.input` |
| `2026-08-01 17:09:44` | `cowrie.log.closed` |
| `2026-08-01 17:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f0d9003890

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:09 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:09:48` | `cowrie.session.connect` |
| `2026-08-01 17:09:48` | `cowrie.client.version` |
| `2026-08-01 17:09:48` | `cowrie.client.kex` |
| `2026-08-01 17:09:49` | `cowrie.login.success` |
| `2026-08-01 17:09:49` | `cowrie.session.params` |
| `2026-08-01 17:09:49` | `cowrie.command.input` |
| `2026-08-01 17:09:49` | `cowrie.log.closed` |
| `2026-08-01 17:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86fb470a7c94

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:09 |
| **Last Seen** | 2026-08-01 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:09:54` | `cowrie.session.connect` |
| `2026-08-01 17:09:54` | `cowrie.client.version` |
| `2026-08-01 17:09:54` | `cowrie.client.kex` |
| `2026-08-01 17:09:54` | `cowrie.login.success` |
| `2026-08-01 17:09:55` | `cowrie.session.params` |
| `2026-08-01 17:09:55` | `cowrie.command.input` |
| `2026-08-01 17:09:55` | `cowrie.log.closed` |
| `2026-08-01 17:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2027faf11b48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:10 |
| **Last Seen** | 2026-08-01 17:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:10:00` | `cowrie.session.connect` |
| `2026-08-01 17:10:00` | `cowrie.client.version` |
| `2026-08-01 17:10:00` | `cowrie.client.kex` |
| `2026-08-01 17:10:01` | `cowrie.login.success` |
| `2026-08-01 17:10:02` | `cowrie.session.params` |
| `2026-08-01 17:10:02` | `cowrie.command.input` |
| `2026-08-01 17:10:02` | `cowrie.log.closed` |
| `2026-08-01 17:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ba8e55150cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:10 |
| **Last Seen** | 2026-08-01 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:10:06` | `cowrie.session.connect` |
| `2026-08-01 17:10:06` | `cowrie.client.version` |
| `2026-08-01 17:10:06` | `cowrie.client.kex` |
| `2026-08-01 17:10:06` | `cowrie.login.success` |
| `2026-08-01 17:10:07` | `cowrie.session.params` |
| `2026-08-01 17:10:07` | `cowrie.command.input` |
| `2026-08-01 17:10:07` | `cowrie.log.closed` |
| `2026-08-01 17:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5dc7c5cb502

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:10 |
| **Last Seen** | 2026-08-01 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:10:12` | `cowrie.session.connect` |
| `2026-08-01 17:10:12` | `cowrie.client.version` |
| `2026-08-01 17:10:12` | `cowrie.client.kex` |
| `2026-08-01 17:10:12` | `cowrie.login.success` |
| `2026-08-01 17:10:13` | `cowrie.session.params` |
| `2026-08-01 17:10:13` | `cowrie.command.input` |
| `2026-08-01 17:10:13` | `cowrie.log.closed` |
| `2026-08-01 17:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf2ade34f39

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:10 |
| **Last Seen** | 2026-08-01 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:10:17` | `cowrie.session.connect` |
| `2026-08-01 17:10:17` | `cowrie.client.version` |
| `2026-08-01 17:10:18` | `cowrie.client.kex` |
| `2026-08-01 17:10:18` | `cowrie.login.success` |
| `2026-08-01 17:10:19` | `cowrie.session.params` |
| `2026-08-01 17:10:19` | `cowrie.command.input` |
| `2026-08-01 17:10:19` | `cowrie.log.closed` |
| `2026-08-01 17:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a32e57e2718

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:10 |
| **Last Seen** | 2026-08-01 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:10:23` | `cowrie.session.connect` |
| `2026-08-01 17:10:23` | `cowrie.client.version` |
| `2026-08-01 17:10:23` | `cowrie.client.kex` |
| `2026-08-01 17:10:24` | `cowrie.login.success` |
| `2026-08-01 17:10:25` | `cowrie.session.params` |
| `2026-08-01 17:10:25` | `cowrie.command.input` |
| `2026-08-01 17:10:25` | `cowrie.log.closed` |
| `2026-08-01 17:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0748b3fcad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:10 |
| **Last Seen** | 2026-08-01 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:10:29` | `cowrie.session.connect` |
| `2026-08-01 17:10:30` | `cowrie.client.version` |
| `2026-08-01 17:10:30` | `cowrie.client.kex` |
| `2026-08-01 17:10:30` | `cowrie.login.success` |
| `2026-08-01 17:10:31` | `cowrie.session.params` |
| `2026-08-01 17:10:31` | `cowrie.command.input` |
| `2026-08-01 17:10:31` | `cowrie.log.closed` |
| `2026-08-01 17:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e7bf9acdf3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:10 |
| **Last Seen** | 2026-08-01 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:10:35` | `cowrie.session.connect` |
| `2026-08-01 17:10:35` | `cowrie.client.version` |
| `2026-08-01 17:10:36` | `cowrie.client.kex` |
| `2026-08-01 17:10:36` | `cowrie.login.success` |
| `2026-08-01 17:10:37` | `cowrie.session.params` |
| `2026-08-01 17:10:37` | `cowrie.command.input` |
| `2026-08-01 17:10:37` | `cowrie.log.closed` |
| `2026-08-01 17:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1990696e7dc1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:10 |
| **Last Seen** | 2026-08-01 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:10:42` | `cowrie.session.connect` |
| `2026-08-01 17:10:42` | `cowrie.client.version` |
| `2026-08-01 17:10:42` | `cowrie.client.kex` |
| `2026-08-01 17:10:42` | `cowrie.login.success` |
| `2026-08-01 17:10:43` | `cowrie.session.params` |
| `2026-08-01 17:10:43` | `cowrie.command.input` |
| `2026-08-01 17:10:43` | `cowrie.log.closed` |
| `2026-08-01 17:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c44b33f7e0e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:10 |
| **Last Seen** | 2026-08-01 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:10:48` | `cowrie.session.connect` |
| `2026-08-01 17:10:48` | `cowrie.client.version` |
| `2026-08-01 17:10:48` | `cowrie.client.kex` |
| `2026-08-01 17:10:48` | `cowrie.login.success` |
| `2026-08-01 17:10:49` | `cowrie.session.params` |
| `2026-08-01 17:10:49` | `cowrie.command.input` |
| `2026-08-01 17:10:49` | `cowrie.log.closed` |
| `2026-08-01 17:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cfa088d63ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:10 |
| **Last Seen** | 2026-08-01 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:10:54` | `cowrie.session.connect` |
| `2026-08-01 17:10:54` | `cowrie.client.version` |
| `2026-08-01 17:10:54` | `cowrie.client.kex` |
| `2026-08-01 17:10:54` | `cowrie.login.success` |
| `2026-08-01 17:10:55` | `cowrie.session.params` |
| `2026-08-01 17:10:55` | `cowrie.command.input` |
| `2026-08-01 17:10:55` | `cowrie.log.closed` |
| `2026-08-01 17:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1754d815898

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:11 |
| **Last Seen** | 2026-08-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:11:00` | `cowrie.session.connect` |
| `2026-08-01 17:11:00` | `cowrie.client.version` |
| `2026-08-01 17:11:00` | `cowrie.client.kex` |
| `2026-08-01 17:11:00` | `cowrie.login.success` |
| `2026-08-01 17:11:01` | `cowrie.session.params` |
| `2026-08-01 17:11:01` | `cowrie.command.input` |
| `2026-08-01 17:11:01` | `cowrie.log.closed` |
| `2026-08-01 17:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0405bdd251e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:11 |
| **Last Seen** | 2026-08-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:11:06` | `cowrie.session.connect` |
| `2026-08-01 17:11:06` | `cowrie.client.version` |
| `2026-08-01 17:11:06` | `cowrie.client.kex` |
| `2026-08-01 17:11:06` | `cowrie.login.success` |
| `2026-08-01 17:11:07` | `cowrie.session.params` |
| `2026-08-01 17:11:07` | `cowrie.command.input` |
| `2026-08-01 17:11:07` | `cowrie.log.closed` |
| `2026-08-01 17:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3b756017aac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:11 |
| **Last Seen** | 2026-08-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:11:12` | `cowrie.session.connect` |
| `2026-08-01 17:11:12` | `cowrie.client.version` |
| `2026-08-01 17:11:12` | `cowrie.client.kex` |
| `2026-08-01 17:11:12` | `cowrie.login.success` |
| `2026-08-01 17:11:13` | `cowrie.session.params` |
| `2026-08-01 17:11:13` | `cowrie.command.input` |
| `2026-08-01 17:11:13` | `cowrie.log.closed` |
| `2026-08-01 17:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34355c75c0cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:11 |
| **Last Seen** | 2026-08-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:11:18` | `cowrie.session.connect` |
| `2026-08-01 17:11:18` | `cowrie.client.version` |
| `2026-08-01 17:11:18` | `cowrie.client.kex` |
| `2026-08-01 17:11:19` | `cowrie.login.success` |
| `2026-08-01 17:11:19` | `cowrie.session.params` |
| `2026-08-01 17:11:19` | `cowrie.command.input` |
| `2026-08-01 17:11:20` | `cowrie.log.closed` |
| `2026-08-01 17:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63a0f17299f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:11 |
| **Last Seen** | 2026-08-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:11:24` | `cowrie.session.connect` |
| `2026-08-01 17:11:24` | `cowrie.client.version` |
| `2026-08-01 17:11:24` | `cowrie.client.kex` |
| `2026-08-01 17:11:25` | `cowrie.login.success` |
| `2026-08-01 17:11:26` | `cowrie.session.params` |
| `2026-08-01 17:11:26` | `cowrie.command.input` |
| `2026-08-01 17:11:26` | `cowrie.log.closed` |
| `2026-08-01 17:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c4e079ee319

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:11 |
| **Last Seen** | 2026-08-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:11:30` | `cowrie.session.connect` |
| `2026-08-01 17:11:30` | `cowrie.client.version` |
| `2026-08-01 17:11:30` | `cowrie.client.kex` |
| `2026-08-01 17:11:31` | `cowrie.login.success` |
| `2026-08-01 17:11:32` | `cowrie.session.params` |
| `2026-08-01 17:11:32` | `cowrie.command.input` |
| `2026-08-01 17:11:32` | `cowrie.log.closed` |
| `2026-08-01 17:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-925614244ac3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:11 |
| **Last Seen** | 2026-08-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:11:36` | `cowrie.session.connect` |
| `2026-08-01 17:11:36` | `cowrie.client.version` |
| `2026-08-01 17:11:36` | `cowrie.client.kex` |
| `2026-08-01 17:11:37` | `cowrie.login.success` |
| `2026-08-01 17:11:38` | `cowrie.session.params` |
| `2026-08-01 17:11:38` | `cowrie.command.input` |
| `2026-08-01 17:11:38` | `cowrie.log.closed` |
| `2026-08-01 17:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7746c41cab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:11 |
| **Last Seen** | 2026-08-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:11:42` | `cowrie.session.connect` |
| `2026-08-01 17:11:42` | `cowrie.client.version` |
| `2026-08-01 17:11:42` | `cowrie.client.kex` |
| `2026-08-01 17:11:43` | `cowrie.login.success` |
| `2026-08-01 17:11:44` | `cowrie.session.params` |
| `2026-08-01 17:11:44` | `cowrie.command.input` |
| `2026-08-01 17:11:44` | `cowrie.log.closed` |
| `2026-08-01 17:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17534e7ad3f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:11 |
| **Last Seen** | 2026-08-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:11:48` | `cowrie.session.connect` |
| `2026-08-01 17:11:48` | `cowrie.client.version` |
| `2026-08-01 17:11:48` | `cowrie.client.kex` |
| `2026-08-01 17:11:49` | `cowrie.login.success` |
| `2026-08-01 17:11:50` | `cowrie.session.params` |
| `2026-08-01 17:11:50` | `cowrie.command.input` |
| `2026-08-01 17:11:50` | `cowrie.log.closed` |
| `2026-08-01 17:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c141db43e7e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:11 |
| **Last Seen** | 2026-08-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:11:54` | `cowrie.session.connect` |
| `2026-08-01 17:11:54` | `cowrie.client.version` |
| `2026-08-01 17:11:54` | `cowrie.client.kex` |
| `2026-08-01 17:11:55` | `cowrie.login.success` |
| `2026-08-01 17:11:56` | `cowrie.session.params` |
| `2026-08-01 17:11:56` | `cowrie.command.input` |
| `2026-08-01 17:11:56` | `cowrie.log.closed` |
| `2026-08-01 17:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74d12da354fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:12 |
| **Last Seen** | 2026-08-01 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:12:01` | `cowrie.session.connect` |
| `2026-08-01 17:12:01` | `cowrie.client.version` |
| `2026-08-01 17:12:01` | `cowrie.client.kex` |
| `2026-08-01 17:12:01` | `cowrie.login.success` |
| `2026-08-01 17:12:02` | `cowrie.session.params` |
| `2026-08-01 17:12:02` | `cowrie.command.input` |
| `2026-08-01 17:12:02` | `cowrie.log.closed` |
| `2026-08-01 17:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36eb9ce31dcf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:12 |
| **Last Seen** | 2026-08-01 17:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:12:06` | `cowrie.session.connect` |
| `2026-08-01 17:12:06` | `cowrie.client.version` |
| `2026-08-01 17:12:06` | `cowrie.client.kex` |
| `2026-08-01 17:12:07` | `cowrie.login.success` |
| `2026-08-01 17:12:08` | `cowrie.session.params` |
| `2026-08-01 17:12:08` | `cowrie.command.input` |
| `2026-08-01 17:12:08` | `cowrie.log.closed` |
| `2026-08-01 17:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373add7c03de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:12 |
| **Last Seen** | 2026-08-01 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:12:12` | `cowrie.session.connect` |
| `2026-08-01 17:12:12` | `cowrie.client.version` |
| `2026-08-01 17:12:12` | `cowrie.client.kex` |
| `2026-08-01 17:12:13` | `cowrie.login.success` |
| `2026-08-01 17:12:14` | `cowrie.session.params` |
| `2026-08-01 17:12:14` | `cowrie.command.input` |
| `2026-08-01 17:12:14` | `cowrie.log.closed` |
| `2026-08-01 17:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f591f9cfae5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:12 |
| **Last Seen** | 2026-08-01 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:12:19` | `cowrie.session.connect` |
| `2026-08-01 17:12:19` | `cowrie.client.version` |
| `2026-08-01 17:12:19` | `cowrie.client.kex` |
| `2026-08-01 17:12:19` | `cowrie.login.success` |
| `2026-08-01 17:12:20` | `cowrie.session.params` |
| `2026-08-01 17:12:20` | `cowrie.command.input` |
| `2026-08-01 17:12:20` | `cowrie.log.closed` |
| `2026-08-01 17:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7de404fc474

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:12 |
| **Last Seen** | 2026-08-01 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:12:24` | `cowrie.session.connect` |
| `2026-08-01 17:12:24` | `cowrie.client.version` |
| `2026-08-01 17:12:24` | `cowrie.client.kex` |
| `2026-08-01 17:12:25` | `cowrie.login.success` |
| `2026-08-01 17:12:26` | `cowrie.session.params` |
| `2026-08-01 17:12:26` | `cowrie.command.input` |
| `2026-08-01 17:12:26` | `cowrie.log.closed` |
| `2026-08-01 17:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128efc64455c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:12 |
| **Last Seen** | 2026-08-01 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:12:30` | `cowrie.session.connect` |
| `2026-08-01 17:12:30` | `cowrie.client.version` |
| `2026-08-01 17:12:30` | `cowrie.client.kex` |
| `2026-08-01 17:12:31` | `cowrie.login.success` |
| `2026-08-01 17:12:32` | `cowrie.session.params` |
| `2026-08-01 17:12:32` | `cowrie.command.input` |
| `2026-08-01 17:12:32` | `cowrie.log.closed` |
| `2026-08-01 17:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d20f8b0f35

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:12 |
| **Last Seen** | 2026-08-01 17:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:12:36` | `cowrie.session.connect` |
| `2026-08-01 17:12:36` | `cowrie.client.version` |
| `2026-08-01 17:12:36` | `cowrie.client.kex` |
| `2026-08-01 17:12:37` | `cowrie.login.success` |
| `2026-08-01 17:12:38` | `cowrie.session.params` |
| `2026-08-01 17:12:38` | `cowrie.command.input` |
| `2026-08-01 17:12:38` | `cowrie.log.closed` |
| `2026-08-01 17:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c6b61fdc8c9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:12 |
| **Last Seen** | 2026-08-01 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:12:42` | `cowrie.session.connect` |
| `2026-08-01 17:12:42` | `cowrie.client.version` |
| `2026-08-01 17:12:42` | `cowrie.client.kex` |
| `2026-08-01 17:12:43` | `cowrie.login.success` |
| `2026-08-01 17:12:44` | `cowrie.session.params` |
| `2026-08-01 17:12:44` | `cowrie.command.input` |
| `2026-08-01 17:12:44` | `cowrie.log.closed` |
| `2026-08-01 17:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70881c626034

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:12 |
| **Last Seen** | 2026-08-01 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:12:48` | `cowrie.session.connect` |
| `2026-08-01 17:12:48` | `cowrie.client.version` |
| `2026-08-01 17:12:48` | `cowrie.client.kex` |
| `2026-08-01 17:12:49` | `cowrie.login.success` |
| `2026-08-01 17:12:50` | `cowrie.session.params` |
| `2026-08-01 17:12:50` | `cowrie.command.input` |
| `2026-08-01 17:12:50` | `cowrie.log.closed` |
| `2026-08-01 17:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eca6c252abb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:12 |
| **Last Seen** | 2026-08-01 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:12:54` | `cowrie.session.connect` |
| `2026-08-01 17:12:54` | `cowrie.client.version` |
| `2026-08-01 17:12:54` | `cowrie.client.kex` |
| `2026-08-01 17:12:54` | `cowrie.login.success` |
| `2026-08-01 17:12:55` | `cowrie.session.params` |
| `2026-08-01 17:12:55` | `cowrie.command.input` |
| `2026-08-01 17:12:55` | `cowrie.log.closed` |
| `2026-08-01 17:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91cb85ec9e5a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:00` | `cowrie.session.connect` |
| `2026-08-01 17:13:00` | `cowrie.client.version` |
| `2026-08-01 17:13:00` | `cowrie.client.kex` |
| `2026-08-01 17:13:00` | `cowrie.login.success` |
| `2026-08-01 17:13:01` | `cowrie.session.params` |
| `2026-08-01 17:13:01` | `cowrie.command.input` |
| `2026-08-01 17:13:01` | `cowrie.log.closed` |
| `2026-08-01 17:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3090011ec723

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:06` | `cowrie.session.connect` |
| `2026-08-01 17:13:06` | `cowrie.client.version` |
| `2026-08-01 17:13:06` | `cowrie.client.kex` |
| `2026-08-01 17:13:06` | `cowrie.login.success` |
| `2026-08-01 17:13:07` | `cowrie.session.params` |
| `2026-08-01 17:13:07` | `cowrie.command.input` |
| `2026-08-01 17:13:07` | `cowrie.log.closed` |
| `2026-08-01 17:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27ba423c1f03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:11` | `cowrie.session.connect` |
| `2026-08-01 17:13:11` | `cowrie.client.version` |
| `2026-08-01 17:13:11` | `cowrie.client.kex` |
| `2026-08-01 17:13:11` | `cowrie.login.success` |
| `2026-08-01 17:13:12` | `cowrie.session.params` |
| `2026-08-01 17:13:12` | `cowrie.command.input` |
| `2026-08-01 17:13:12` | `cowrie.log.closed` |
| `2026-08-01 17:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5330c23e1705

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:16` | `cowrie.session.connect` |
| `2026-08-01 17:13:17` | `cowrie.client.version` |
| `2026-08-01 17:13:17` | `cowrie.client.kex` |
| `2026-08-01 17:13:19` | `cowrie.login.success` |
| `2026-08-01 17:13:20` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6f361acdfc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:17` | `cowrie.session.connect` |
| `2026-08-01 17:13:17` | `cowrie.client.version` |
| `2026-08-01 17:13:17` | `cowrie.client.kex` |
| `2026-08-01 17:13:17` | `cowrie.login.success` |
| `2026-08-01 17:13:18` | `cowrie.session.params` |
| `2026-08-01 17:13:18` | `cowrie.command.input` |
| `2026-08-01 17:13:19` | `cowrie.log.closed` |
| `2026-08-01 17:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88599bad3a99

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:23` | `cowrie.session.connect` |
| `2026-08-01 17:13:23` | `cowrie.client.version` |
| `2026-08-01 17:13:23` | `cowrie.client.kex` |
| `2026-08-01 17:13:23` | `cowrie.login.success` |
| `2026-08-01 17:13:24` | `cowrie.session.params` |
| `2026-08-01 17:13:24` | `cowrie.command.input` |
| `2026-08-01 17:13:24` | `cowrie.log.closed` |
| `2026-08-01 17:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed88685d014

| Field | Detail |
|---|---|
| **Source IP** | `58.34.174[.]90` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:26` | `cowrie.session.connect` |
| `2026-08-01 17:13:27` | `cowrie.client.version` |
| `2026-08-01 17:13:27` | `cowrie.client.kex` |
| `2026-08-01 17:13:30` | `cowrie.login.success` |
| `2026-08-01 17:13:31` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.34.174[.]90` to AbuseIPDB if not already reported
- [ ] Block `58.34.174[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b0c4195b92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:28` | `cowrie.session.connect` |
| `2026-08-01 17:13:28` | `cowrie.client.version` |
| `2026-08-01 17:13:28` | `cowrie.client.kex` |
| `2026-08-01 17:13:29` | `cowrie.login.success` |
| `2026-08-01 17:13:30` | `cowrie.session.params` |
| `2026-08-01 17:13:30` | `cowrie.command.input` |
| `2026-08-01 17:13:30` | `cowrie.log.closed` |
| `2026-08-01 17:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0cc0ace6b6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:34` | `cowrie.session.connect` |
| `2026-08-01 17:13:34` | `cowrie.client.version` |
| `2026-08-01 17:13:34` | `cowrie.client.kex` |
| `2026-08-01 17:13:35` | `cowrie.login.success` |
| `2026-08-01 17:13:35` | `cowrie.session.params` |
| `2026-08-01 17:13:35` | `cowrie.command.input` |
| `2026-08-01 17:13:36` | `cowrie.log.closed` |
| `2026-08-01 17:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3ade3332f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:40` | `cowrie.session.connect` |
| `2026-08-01 17:13:40` | `cowrie.client.version` |
| `2026-08-01 17:13:40` | `cowrie.client.kex` |
| `2026-08-01 17:13:41` | `cowrie.login.success` |
| `2026-08-01 17:13:41` | `cowrie.session.params` |
| `2026-08-01 17:13:41` | `cowrie.command.input` |
| `2026-08-01 17:13:42` | `cowrie.log.closed` |
| `2026-08-01 17:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b996c5cfd179

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:46` | `cowrie.session.connect` |
| `2026-08-01 17:13:46` | `cowrie.client.version` |
| `2026-08-01 17:13:46` | `cowrie.client.kex` |
| `2026-08-01 17:13:46` | `cowrie.login.success` |
| `2026-08-01 17:13:47` | `cowrie.session.params` |
| `2026-08-01 17:13:47` | `cowrie.command.input` |
| `2026-08-01 17:13:47` | `cowrie.log.closed` |
| `2026-08-01 17:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-285c7c8cce28

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:51` | `cowrie.session.connect` |
| `2026-08-01 17:13:51` | `cowrie.client.version` |
| `2026-08-01 17:13:51` | `cowrie.client.kex` |
| `2026-08-01 17:13:52` | `cowrie.login.success` |
| `2026-08-01 17:13:52` | `cowrie.session.params` |
| `2026-08-01 17:13:52` | `cowrie.command.input` |
| `2026-08-01 17:13:53` | `cowrie.log.closed` |
| `2026-08-01 17:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c217f1c2beaf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:13 |
| **Last Seen** | 2026-08-01 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:13:56` | `cowrie.session.connect` |
| `2026-08-01 17:13:57` | `cowrie.client.version` |
| `2026-08-01 17:13:57` | `cowrie.client.kex` |
| `2026-08-01 17:13:57` | `cowrie.login.success` |
| `2026-08-01 17:13:58` | `cowrie.session.params` |
| `2026-08-01 17:13:58` | `cowrie.command.input` |
| `2026-08-01 17:13:58` | `cowrie.log.closed` |
| `2026-08-01 17:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bbbfa720571

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:14 |
| **Last Seen** | 2026-08-01 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:14:02` | `cowrie.session.connect` |
| `2026-08-01 17:14:02` | `cowrie.client.version` |
| `2026-08-01 17:14:02` | `cowrie.client.kex` |
| `2026-08-01 17:14:03` | `cowrie.login.success` |
| `2026-08-01 17:14:04` | `cowrie.session.params` |
| `2026-08-01 17:14:04` | `cowrie.command.input` |
| `2026-08-01 17:14:04` | `cowrie.log.closed` |
| `2026-08-01 17:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d612234a9766

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:16 |
| **Last Seen** | 2026-08-01 17:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:16:35` | `cowrie.session.connect` |
| `2026-08-01 17:16:35` | `cowrie.client.version` |
| `2026-08-01 17:16:35` | `cowrie.client.kex` |
| `2026-08-01 17:16:35` | `cowrie.login.success` |
| `2026-08-01 17:16:41` | `cowrie.session.params` |
| `2026-08-01 17:16:41` | `cowrie.command.input` |
| `2026-08-01 17:16:41` | `cowrie.log.closed` |
| `2026-08-01 17:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc3b54258b2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:16 |
| **Last Seen** | 2026-08-01 17:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:16:39` | `cowrie.session.connect` |
| `2026-08-01 17:16:39` | `cowrie.client.version` |
| `2026-08-01 17:16:39` | `cowrie.client.kex` |
| `2026-08-01 17:16:40` | `cowrie.login.success` |
| `2026-08-01 17:16:41` | `cowrie.session.params` |
| `2026-08-01 17:16:41` | `cowrie.command.input` |
| `2026-08-01 17:16:41` | `cowrie.log.closed` |
| `2026-08-01 17:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba8bdc4bf6f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:16 |
| **Last Seen** | 2026-08-01 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:16:41` | `cowrie.session.connect` |
| `2026-08-01 17:16:41` | `cowrie.client.version` |
| `2026-08-01 17:16:41` | `cowrie.client.kex` |
| `2026-08-01 17:16:42` | `cowrie.login.success` |
| `2026-08-01 17:16:42` | `cowrie.session.params` |
| `2026-08-01 17:16:42` | `cowrie.command.input` |
| `2026-08-01 17:16:43` | `cowrie.log.closed` |
| `2026-08-01 17:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ac903f6757

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:16 |
| **Last Seen** | 2026-08-01 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:16:41` | `cowrie.session.connect` |
| `2026-08-01 17:16:41` | `cowrie.client.version` |
| `2026-08-01 17:16:42` | `cowrie.client.kex` |
| `2026-08-01 17:16:42` | `cowrie.login.success` |
| `2026-08-01 17:16:43` | `cowrie.session.params` |
| `2026-08-01 17:16:43` | `cowrie.command.input` |
| `2026-08-01 17:16:43` | `cowrie.log.closed` |
| `2026-08-01 17:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef128c14c4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:16 |
| **Last Seen** | 2026-08-01 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:16:44` | `cowrie.session.connect` |
| `2026-08-01 17:16:44` | `cowrie.client.version` |
| `2026-08-01 17:16:44` | `cowrie.client.kex` |
| `2026-08-01 17:16:45` | `cowrie.login.success` |
| `2026-08-01 17:16:45` | `cowrie.session.params` |
| `2026-08-01 17:16:45` | `cowrie.command.input` |
| `2026-08-01 17:16:46` | `cowrie.log.closed` |
| `2026-08-01 17:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-279bc5709430

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:16 |
| **Last Seen** | 2026-08-01 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:16:50` | `cowrie.session.connect` |
| `2026-08-01 17:16:50` | `cowrie.client.version` |
| `2026-08-01 17:16:50` | `cowrie.client.kex` |
| `2026-08-01 17:16:50` | `cowrie.login.success` |
| `2026-08-01 17:16:51` | `cowrie.session.params` |
| `2026-08-01 17:16:51` | `cowrie.command.input` |
| `2026-08-01 17:16:51` | `cowrie.log.closed` |
| `2026-08-01 17:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fb2fd950dba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:16 |
| **Last Seen** | 2026-08-01 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:16:56` | `cowrie.session.connect` |
| `2026-08-01 17:16:56` | `cowrie.client.version` |
| `2026-08-01 17:16:56` | `cowrie.client.kex` |
| `2026-08-01 17:16:56` | `cowrie.login.success` |
| `2026-08-01 17:16:57` | `cowrie.session.params` |
| `2026-08-01 17:16:57` | `cowrie.command.input` |
| `2026-08-01 17:16:57` | `cowrie.log.closed` |
| `2026-08-01 17:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3098cec7f6eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:17 |
| **Last Seen** | 2026-08-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:17:01` | `cowrie.session.connect` |
| `2026-08-01 17:17:01` | `cowrie.client.version` |
| `2026-08-01 17:17:01` | `cowrie.client.kex` |
| `2026-08-01 17:17:02` | `cowrie.login.success` |
| `2026-08-01 17:17:03` | `cowrie.session.params` |
| `2026-08-01 17:17:03` | `cowrie.command.input` |
| `2026-08-01 17:17:03` | `cowrie.log.closed` |
| `2026-08-01 17:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc5f697efc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:17 |
| **Last Seen** | 2026-08-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:17:07` | `cowrie.session.connect` |
| `2026-08-01 17:17:07` | `cowrie.client.version` |
| `2026-08-01 17:17:07` | `cowrie.client.kex` |
| `2026-08-01 17:17:07` | `cowrie.login.success` |
| `2026-08-01 17:17:08` | `cowrie.session.params` |
| `2026-08-01 17:17:08` | `cowrie.command.input` |
| `2026-08-01 17:17:08` | `cowrie.log.closed` |
| `2026-08-01 17:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf0bacc7460

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:17 |
| **Last Seen** | 2026-08-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:17:13` | `cowrie.session.connect` |
| `2026-08-01 17:17:13` | `cowrie.client.version` |
| `2026-08-01 17:17:13` | `cowrie.client.kex` |
| `2026-08-01 17:17:13` | `cowrie.login.success` |
| `2026-08-01 17:17:15` | `cowrie.session.params` |
| `2026-08-01 17:17:15` | `cowrie.command.input` |
| `2026-08-01 17:17:15` | `cowrie.log.closed` |
| `2026-08-01 17:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d8fbaef3db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:17 |
| **Last Seen** | 2026-08-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:17:19` | `cowrie.session.connect` |
| `2026-08-01 17:17:19` | `cowrie.client.version` |
| `2026-08-01 17:17:19` | `cowrie.client.kex` |
| `2026-08-01 17:17:19` | `cowrie.login.success` |
| `2026-08-01 17:17:20` | `cowrie.session.params` |
| `2026-08-01 17:17:20` | `cowrie.command.input` |
| `2026-08-01 17:17:20` | `cowrie.log.closed` |
| `2026-08-01 17:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a5ae6fbd6a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:17 |
| **Last Seen** | 2026-08-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:17:25` | `cowrie.session.connect` |
| `2026-08-01 17:17:25` | `cowrie.client.version` |
| `2026-08-01 17:17:25` | `cowrie.client.kex` |
| `2026-08-01 17:17:25` | `cowrie.login.success` |
| `2026-08-01 17:17:26` | `cowrie.session.params` |
| `2026-08-01 17:17:26` | `cowrie.command.input` |
| `2026-08-01 17:17:26` | `cowrie.log.closed` |
| `2026-08-01 17:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ace102cb0ab0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:17 |
| **Last Seen** | 2026-08-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:17:31` | `cowrie.session.connect` |
| `2026-08-01 17:17:31` | `cowrie.client.version` |
| `2026-08-01 17:17:31` | `cowrie.client.kex` |
| `2026-08-01 17:17:31` | `cowrie.login.success` |
| `2026-08-01 17:17:32` | `cowrie.session.params` |
| `2026-08-01 17:17:32` | `cowrie.command.input` |
| `2026-08-01 17:17:32` | `cowrie.log.closed` |
| `2026-08-01 17:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda7f6184295

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:17 |
| **Last Seen** | 2026-08-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:17:37` | `cowrie.session.connect` |
| `2026-08-01 17:17:37` | `cowrie.client.version` |
| `2026-08-01 17:17:37` | `cowrie.client.kex` |
| `2026-08-01 17:17:37` | `cowrie.login.success` |
| `2026-08-01 17:17:38` | `cowrie.session.params` |
| `2026-08-01 17:17:38` | `cowrie.command.input` |
| `2026-08-01 17:17:38` | `cowrie.log.closed` |
| `2026-08-01 17:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe3d92141242

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:17 |
| **Last Seen** | 2026-08-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:17:42` | `cowrie.session.connect` |
| `2026-08-01 17:17:42` | `cowrie.client.version` |
| `2026-08-01 17:17:43` | `cowrie.client.kex` |
| `2026-08-01 17:17:43` | `cowrie.login.success` |
| `2026-08-01 17:17:44` | `cowrie.session.params` |
| `2026-08-01 17:17:44` | `cowrie.command.input` |
| `2026-08-01 17:17:44` | `cowrie.log.closed` |
| `2026-08-01 17:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1fbca88ef1e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:17 |
| **Last Seen** | 2026-08-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:17:48` | `cowrie.session.connect` |
| `2026-08-01 17:17:48` | `cowrie.client.version` |
| `2026-08-01 17:17:48` | `cowrie.client.kex` |
| `2026-08-01 17:17:49` | `cowrie.login.success` |
| `2026-08-01 17:17:49` | `cowrie.session.params` |
| `2026-08-01 17:17:49` | `cowrie.command.input` |
| `2026-08-01 17:17:50` | `cowrie.log.closed` |
| `2026-08-01 17:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-589f06434373

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:17 |
| **Last Seen** | 2026-08-01 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:17:54` | `cowrie.session.connect` |
| `2026-08-01 17:17:54` | `cowrie.client.version` |
| `2026-08-01 17:17:54` | `cowrie.client.kex` |
| `2026-08-01 17:17:54` | `cowrie.login.success` |
| `2026-08-01 17:17:55` | `cowrie.session.params` |
| `2026-08-01 17:17:55` | `cowrie.command.input` |
| `2026-08-01 17:17:55` | `cowrie.log.closed` |
| `2026-08-01 17:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c653019ecb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:18 |
| **Last Seen** | 2026-08-01 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:18:00` | `cowrie.session.connect` |
| `2026-08-01 17:18:00` | `cowrie.client.version` |
| `2026-08-01 17:18:00` | `cowrie.client.kex` |
| `2026-08-01 17:18:00` | `cowrie.login.success` |
| `2026-08-01 17:18:01` | `cowrie.session.params` |
| `2026-08-01 17:18:01` | `cowrie.command.input` |
| `2026-08-01 17:18:01` | `cowrie.log.closed` |
| `2026-08-01 17:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-468e9cc958d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:18 |
| **Last Seen** | 2026-08-01 17:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:18:06` | `cowrie.session.connect` |
| `2026-08-01 17:18:06` | `cowrie.client.version` |
| `2026-08-01 17:18:06` | `cowrie.client.kex` |
| `2026-08-01 17:18:07` | `cowrie.login.success` |
| `2026-08-01 17:18:08` | `cowrie.session.params` |
| `2026-08-01 17:18:08` | `cowrie.command.input` |
| `2026-08-01 17:18:08` | `cowrie.log.closed` |
| `2026-08-01 17:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c53400195d8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:18 |
| **Last Seen** | 2026-08-01 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:18:12` | `cowrie.session.connect` |
| `2026-08-01 17:18:12` | `cowrie.client.version` |
| `2026-08-01 17:18:12` | `cowrie.client.kex` |
| `2026-08-01 17:18:12` | `cowrie.login.success` |
| `2026-08-01 17:18:13` | `cowrie.session.params` |
| `2026-08-01 17:18:13` | `cowrie.command.input` |
| `2026-08-01 17:18:13` | `cowrie.log.closed` |
| `2026-08-01 17:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31f841354d8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:18 |
| **Last Seen** | 2026-08-01 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:18:18` | `cowrie.session.connect` |
| `2026-08-01 17:18:18` | `cowrie.client.version` |
| `2026-08-01 17:18:18` | `cowrie.client.kex` |
| `2026-08-01 17:18:19` | `cowrie.login.success` |
| `2026-08-01 17:18:20` | `cowrie.session.params` |
| `2026-08-01 17:18:20` | `cowrie.command.input` |
| `2026-08-01 17:18:20` | `cowrie.log.closed` |
| `2026-08-01 17:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266907e237c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:18 |
| **Last Seen** | 2026-08-01 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:18:24` | `cowrie.session.connect` |
| `2026-08-01 17:18:24` | `cowrie.client.version` |
| `2026-08-01 17:18:24` | `cowrie.client.kex` |
| `2026-08-01 17:18:25` | `cowrie.login.success` |
| `2026-08-01 17:18:25` | `cowrie.session.params` |
| `2026-08-01 17:18:25` | `cowrie.command.input` |
| `2026-08-01 17:18:26` | `cowrie.log.closed` |
| `2026-08-01 17:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ce47026a850

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:18 |
| **Last Seen** | 2026-08-01 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:18:30` | `cowrie.session.connect` |
| `2026-08-01 17:18:30` | `cowrie.client.version` |
| `2026-08-01 17:18:30` | `cowrie.client.kex` |
| `2026-08-01 17:18:31` | `cowrie.login.success` |
| `2026-08-01 17:18:32` | `cowrie.session.params` |
| `2026-08-01 17:18:32` | `cowrie.command.input` |
| `2026-08-01 17:18:32` | `cowrie.log.closed` |
| `2026-08-01 17:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-651bf1c39076

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:18 |
| **Last Seen** | 2026-08-01 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:18:36` | `cowrie.session.connect` |
| `2026-08-01 17:18:36` | `cowrie.client.version` |
| `2026-08-01 17:18:36` | `cowrie.client.kex` |
| `2026-08-01 17:18:37` | `cowrie.login.success` |
| `2026-08-01 17:18:38` | `cowrie.session.params` |
| `2026-08-01 17:18:38` | `cowrie.command.input` |
| `2026-08-01 17:18:38` | `cowrie.log.closed` |
| `2026-08-01 17:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a1146c51d4c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:18 |
| **Last Seen** | 2026-08-01 17:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:18:43` | `cowrie.session.connect` |
| `2026-08-01 17:18:43` | `cowrie.client.version` |
| `2026-08-01 17:18:43` | `cowrie.client.kex` |
| `2026-08-01 17:18:44` | `cowrie.login.success` |
| `2026-08-01 17:18:45` | `cowrie.session.params` |
| `2026-08-01 17:18:45` | `cowrie.command.input` |
| `2026-08-01 17:18:45` | `cowrie.log.closed` |
| `2026-08-01 17:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8729018fdb2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:18 |
| **Last Seen** | 2026-08-01 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:18:49` | `cowrie.session.connect` |
| `2026-08-01 17:18:49` | `cowrie.client.version` |
| `2026-08-01 17:18:49` | `cowrie.client.kex` |
| `2026-08-01 17:18:50` | `cowrie.login.success` |
| `2026-08-01 17:18:51` | `cowrie.session.params` |
| `2026-08-01 17:18:51` | `cowrie.command.input` |
| `2026-08-01 17:18:51` | `cowrie.log.closed` |
| `2026-08-01 17:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-486de72f1d0d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:18 |
| **Last Seen** | 2026-08-01 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:18:56` | `cowrie.session.connect` |
| `2026-08-01 17:18:56` | `cowrie.client.version` |
| `2026-08-01 17:18:56` | `cowrie.client.kex` |
| `2026-08-01 17:18:56` | `cowrie.login.success` |
| `2026-08-01 17:18:57` | `cowrie.session.params` |
| `2026-08-01 17:18:57` | `cowrie.command.input` |
| `2026-08-01 17:18:57` | `cowrie.log.closed` |
| `2026-08-01 17:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8e99dccc958

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:19 |
| **Last Seen** | 2026-08-01 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:19:01` | `cowrie.session.connect` |
| `2026-08-01 17:19:02` | `cowrie.client.version` |
| `2026-08-01 17:19:02` | `cowrie.client.kex` |
| `2026-08-01 17:19:03` | `cowrie.login.success` |
| `2026-08-01 17:19:04` | `cowrie.session.params` |
| `2026-08-01 17:19:04` | `cowrie.command.input` |
| `2026-08-01 17:19:04` | `cowrie.log.closed` |
| `2026-08-01 17:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13875df7e7f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:19 |
| **Last Seen** | 2026-08-01 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:19:08` | `cowrie.session.connect` |
| `2026-08-01 17:19:08` | `cowrie.client.version` |
| `2026-08-01 17:19:08` | `cowrie.client.kex` |
| `2026-08-01 17:19:09` | `cowrie.login.success` |
| `2026-08-01 17:19:10` | `cowrie.session.params` |
| `2026-08-01 17:19:10` | `cowrie.command.input` |
| `2026-08-01 17:19:10` | `cowrie.log.closed` |
| `2026-08-01 17:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29f8b7b36a8f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:19 |
| **Last Seen** | 2026-08-01 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:19:14` | `cowrie.session.connect` |
| `2026-08-01 17:19:14` | `cowrie.client.version` |
| `2026-08-01 17:19:14` | `cowrie.client.kex` |
| `2026-08-01 17:19:15` | `cowrie.login.success` |
| `2026-08-01 17:19:16` | `cowrie.session.params` |
| `2026-08-01 17:19:16` | `cowrie.command.input` |
| `2026-08-01 17:19:16` | `cowrie.log.closed` |
| `2026-08-01 17:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b9d67f20e36

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:19 |
| **Last Seen** | 2026-08-01 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:19:21` | `cowrie.session.connect` |
| `2026-08-01 17:19:21` | `cowrie.client.version` |
| `2026-08-01 17:19:21` | `cowrie.client.kex` |
| `2026-08-01 17:19:21` | `cowrie.login.success` |
| `2026-08-01 17:19:22` | `cowrie.session.params` |
| `2026-08-01 17:19:22` | `cowrie.command.input` |
| `2026-08-01 17:19:22` | `cowrie.log.closed` |
| `2026-08-01 17:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b218cb4d9d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:19 |
| **Last Seen** | 2026-08-01 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:19:26` | `cowrie.session.connect` |
| `2026-08-01 17:19:27` | `cowrie.client.version` |
| `2026-08-01 17:19:27` | `cowrie.client.kex` |
| `2026-08-01 17:19:27` | `cowrie.login.success` |
| `2026-08-01 17:19:28` | `cowrie.session.params` |
| `2026-08-01 17:19:28` | `cowrie.command.input` |
| `2026-08-01 17:19:29` | `cowrie.log.closed` |
| `2026-08-01 17:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a163d64ce8c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:19 |
| **Last Seen** | 2026-08-01 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:19:33` | `cowrie.session.connect` |
| `2026-08-01 17:19:33` | `cowrie.client.version` |
| `2026-08-01 17:19:33` | `cowrie.client.kex` |
| `2026-08-01 17:19:33` | `cowrie.login.success` |
| `2026-08-01 17:19:34` | `cowrie.session.params` |
| `2026-08-01 17:19:34` | `cowrie.command.input` |
| `2026-08-01 17:19:34` | `cowrie.log.closed` |
| `2026-08-01 17:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27a435787f63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:19 |
| **Last Seen** | 2026-08-01 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:19:39` | `cowrie.session.connect` |
| `2026-08-01 17:19:39` | `cowrie.client.version` |
| `2026-08-01 17:19:39` | `cowrie.client.kex` |
| `2026-08-01 17:19:40` | `cowrie.login.success` |
| `2026-08-01 17:19:41` | `cowrie.session.params` |
| `2026-08-01 17:19:41` | `cowrie.command.input` |
| `2026-08-01 17:19:41` | `cowrie.log.closed` |
| `2026-08-01 17:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335fd189e277

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:19 |
| **Last Seen** | 2026-08-01 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:19:45` | `cowrie.session.connect` |
| `2026-08-01 17:19:45` | `cowrie.client.version` |
| `2026-08-01 17:19:45` | `cowrie.client.kex` |
| `2026-08-01 17:19:46` | `cowrie.login.success` |
| `2026-08-01 17:19:47` | `cowrie.session.params` |
| `2026-08-01 17:19:47` | `cowrie.command.input` |
| `2026-08-01 17:19:47` | `cowrie.log.closed` |
| `2026-08-01 17:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bace9c1c80a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:19 |
| **Last Seen** | 2026-08-01 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:19:51` | `cowrie.session.connect` |
| `2026-08-01 17:19:51` | `cowrie.client.version` |
| `2026-08-01 17:19:51` | `cowrie.client.kex` |
| `2026-08-01 17:19:52` | `cowrie.login.success` |
| `2026-08-01 17:19:53` | `cowrie.session.params` |
| `2026-08-01 17:19:53` | `cowrie.command.input` |
| `2026-08-01 17:19:53` | `cowrie.log.closed` |
| `2026-08-01 17:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01b4549f624d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:19 |
| **Last Seen** | 2026-08-01 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:19:57` | `cowrie.session.connect` |
| `2026-08-01 17:19:57` | `cowrie.client.version` |
| `2026-08-01 17:19:57` | `cowrie.client.kex` |
| `2026-08-01 17:19:58` | `cowrie.login.success` |
| `2026-08-01 17:19:59` | `cowrie.session.params` |
| `2026-08-01 17:19:59` | `cowrie.command.input` |
| `2026-08-01 17:19:59` | `cowrie.log.closed` |
| `2026-08-01 17:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0959022cf284

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:20 |
| **Last Seen** | 2026-08-01 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:20:03` | `cowrie.session.connect` |
| `2026-08-01 17:20:03` | `cowrie.client.version` |
| `2026-08-01 17:20:03` | `cowrie.client.kex` |
| `2026-08-01 17:20:04` | `cowrie.login.success` |
| `2026-08-01 17:20:05` | `cowrie.session.params` |
| `2026-08-01 17:20:05` | `cowrie.command.input` |
| `2026-08-01 17:20:05` | `cowrie.log.closed` |
| `2026-08-01 17:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d886142f03c9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:20 |
| **Last Seen** | 2026-08-01 17:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:20:09` | `cowrie.session.connect` |
| `2026-08-01 17:20:09` | `cowrie.client.version` |
| `2026-08-01 17:20:10` | `cowrie.client.kex` |
| `2026-08-01 17:20:10` | `cowrie.login.success` |
| `2026-08-01 17:20:11` | `cowrie.session.params` |
| `2026-08-01 17:20:11` | `cowrie.command.input` |
| `2026-08-01 17:20:11` | `cowrie.log.closed` |
| `2026-08-01 17:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cab45cb2163

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:20 |
| **Last Seen** | 2026-08-01 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:20:15` | `cowrie.session.connect` |
| `2026-08-01 17:20:16` | `cowrie.client.version` |
| `2026-08-01 17:20:16` | `cowrie.client.kex` |
| `2026-08-01 17:20:16` | `cowrie.login.success` |
| `2026-08-01 17:20:17` | `cowrie.session.params` |
| `2026-08-01 17:20:17` | `cowrie.command.input` |
| `2026-08-01 17:20:17` | `cowrie.log.closed` |
| `2026-08-01 17:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b8195a4f45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:20 |
| **Last Seen** | 2026-08-01 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:20:21` | `cowrie.session.connect` |
| `2026-08-01 17:20:22` | `cowrie.client.version` |
| `2026-08-01 17:20:22` | `cowrie.client.kex` |
| `2026-08-01 17:20:22` | `cowrie.login.success` |
| `2026-08-01 17:20:23` | `cowrie.session.params` |
| `2026-08-01 17:20:23` | `cowrie.command.input` |
| `2026-08-01 17:20:23` | `cowrie.log.closed` |
| `2026-08-01 17:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ab29f201d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:20 |
| **Last Seen** | 2026-08-01 17:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:20:27` | `cowrie.session.connect` |
| `2026-08-01 17:20:27` | `cowrie.client.version` |
| `2026-08-01 17:20:27` | `cowrie.client.kex` |
| `2026-08-01 17:20:28` | `cowrie.login.success` |
| `2026-08-01 17:20:29` | `cowrie.session.params` |
| `2026-08-01 17:20:29` | `cowrie.command.input` |
| `2026-08-01 17:20:29` | `cowrie.log.closed` |
| `2026-08-01 17:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d372e2971df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:20 |
| **Last Seen** | 2026-08-01 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:20:34` | `cowrie.session.connect` |
| `2026-08-01 17:20:34` | `cowrie.client.version` |
| `2026-08-01 17:20:34` | `cowrie.client.kex` |
| `2026-08-01 17:20:34` | `cowrie.login.success` |
| `2026-08-01 17:20:35` | `cowrie.session.params` |
| `2026-08-01 17:20:35` | `cowrie.command.input` |
| `2026-08-01 17:20:35` | `cowrie.log.closed` |
| `2026-08-01 17:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53d77c29f719

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:20 |
| **Last Seen** | 2026-08-01 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:20:40` | `cowrie.session.connect` |
| `2026-08-01 17:20:40` | `cowrie.client.version` |
| `2026-08-01 17:20:40` | `cowrie.client.kex` |
| `2026-08-01 17:20:40` | `cowrie.login.success` |
| `2026-08-01 17:20:41` | `cowrie.session.params` |
| `2026-08-01 17:20:41` | `cowrie.command.input` |
| `2026-08-01 17:20:41` | `cowrie.log.closed` |
| `2026-08-01 17:20:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07f2548dd524

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:20 |
| **Last Seen** | 2026-08-01 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:20:46` | `cowrie.session.connect` |
| `2026-08-01 17:20:46` | `cowrie.client.version` |
| `2026-08-01 17:20:46` | `cowrie.client.kex` |
| `2026-08-01 17:20:46` | `cowrie.login.success` |
| `2026-08-01 17:20:47` | `cowrie.session.params` |
| `2026-08-01 17:20:47` | `cowrie.command.input` |
| `2026-08-01 17:20:48` | `cowrie.log.closed` |
| `2026-08-01 17:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c38c1da4b05

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:20 |
| **Last Seen** | 2026-08-01 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:20:52` | `cowrie.session.connect` |
| `2026-08-01 17:20:52` | `cowrie.client.version` |
| `2026-08-01 17:20:52` | `cowrie.client.kex` |
| `2026-08-01 17:20:52` | `cowrie.login.success` |
| `2026-08-01 17:20:53` | `cowrie.session.params` |
| `2026-08-01 17:20:53` | `cowrie.command.input` |
| `2026-08-01 17:20:53` | `cowrie.log.closed` |
| `2026-08-01 17:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93014152d232

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:20 |
| **Last Seen** | 2026-08-01 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:20:58` | `cowrie.session.connect` |
| `2026-08-01 17:20:58` | `cowrie.client.version` |
| `2026-08-01 17:20:58` | `cowrie.client.kex` |
| `2026-08-01 17:20:58` | `cowrie.login.success` |
| `2026-08-01 17:20:59` | `cowrie.session.params` |
| `2026-08-01 17:20:59` | `cowrie.command.input` |
| `2026-08-01 17:20:59` | `cowrie.log.closed` |
| `2026-08-01 17:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e771edafe39a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:21 |
| **Last Seen** | 2026-08-01 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:21:04` | `cowrie.session.connect` |
| `2026-08-01 17:21:04` | `cowrie.client.version` |
| `2026-08-01 17:21:04` | `cowrie.client.kex` |
| `2026-08-01 17:21:04` | `cowrie.login.success` |
| `2026-08-01 17:21:05` | `cowrie.session.params` |
| `2026-08-01 17:21:05` | `cowrie.command.input` |
| `2026-08-01 17:21:05` | `cowrie.log.closed` |
| `2026-08-01 17:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf002448df6d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:21 |
| **Last Seen** | 2026-08-01 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:21:10` | `cowrie.session.connect` |
| `2026-08-01 17:21:10` | `cowrie.client.version` |
| `2026-08-01 17:21:10` | `cowrie.client.kex` |
| `2026-08-01 17:21:11` | `cowrie.login.success` |
| `2026-08-01 17:21:12` | `cowrie.session.params` |
| `2026-08-01 17:21:12` | `cowrie.command.input` |
| `2026-08-01 17:21:12` | `cowrie.log.closed` |
| `2026-08-01 17:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88b9d57c2c7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:21 |
| **Last Seen** | 2026-08-01 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:21:16` | `cowrie.session.connect` |
| `2026-08-01 17:21:16` | `cowrie.client.version` |
| `2026-08-01 17:21:17` | `cowrie.client.kex` |
| `2026-08-01 17:21:17` | `cowrie.login.success` |
| `2026-08-01 17:21:18` | `cowrie.session.params` |
| `2026-08-01 17:21:18` | `cowrie.command.input` |
| `2026-08-01 17:21:18` | `cowrie.log.closed` |
| `2026-08-01 17:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0eefdbccdcb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:21 |
| **Last Seen** | 2026-08-01 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:21:23` | `cowrie.session.connect` |
| `2026-08-01 17:21:23` | `cowrie.client.version` |
| `2026-08-01 17:21:23` | `cowrie.client.kex` |
| `2026-08-01 17:21:23` | `cowrie.login.success` |
| `2026-08-01 17:21:24` | `cowrie.session.params` |
| `2026-08-01 17:21:24` | `cowrie.command.input` |
| `2026-08-01 17:21:24` | `cowrie.log.closed` |
| `2026-08-01 17:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d206d30f68f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:21 |
| **Last Seen** | 2026-08-01 17:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:21:29` | `cowrie.session.connect` |
| `2026-08-01 17:21:29` | `cowrie.client.version` |
| `2026-08-01 17:21:29` | `cowrie.client.kex` |
| `2026-08-01 17:21:30` | `cowrie.login.success` |
| `2026-08-01 17:21:30` | `cowrie.session.params` |
| `2026-08-01 17:21:30` | `cowrie.command.input` |
| `2026-08-01 17:21:31` | `cowrie.log.closed` |
| `2026-08-01 17:21:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f107e437a9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:21 |
| **Last Seen** | 2026-08-01 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:21:35` | `cowrie.session.connect` |
| `2026-08-01 17:21:35` | `cowrie.client.version` |
| `2026-08-01 17:21:35` | `cowrie.client.kex` |
| `2026-08-01 17:21:35` | `cowrie.login.success` |
| `2026-08-01 17:21:36` | `cowrie.session.params` |
| `2026-08-01 17:21:36` | `cowrie.command.input` |
| `2026-08-01 17:21:37` | `cowrie.log.closed` |
| `2026-08-01 17:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db027bb3c77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:21 |
| **Last Seen** | 2026-08-01 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:21:41` | `cowrie.session.connect` |
| `2026-08-01 17:21:41` | `cowrie.client.version` |
| `2026-08-01 17:21:41` | `cowrie.client.kex` |
| `2026-08-01 17:21:42` | `cowrie.login.success` |
| `2026-08-01 17:21:43` | `cowrie.session.params` |
| `2026-08-01 17:21:43` | `cowrie.command.input` |
| `2026-08-01 17:21:43` | `cowrie.log.closed` |
| `2026-08-01 17:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9a08ebb34a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:21 |
| **Last Seen** | 2026-08-01 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:21:47` | `cowrie.session.connect` |
| `2026-08-01 17:21:47` | `cowrie.client.version` |
| `2026-08-01 17:21:47` | `cowrie.client.kex` |
| `2026-08-01 17:21:48` | `cowrie.login.success` |
| `2026-08-01 17:21:49` | `cowrie.session.params` |
| `2026-08-01 17:21:49` | `cowrie.command.input` |
| `2026-08-01 17:21:49` | `cowrie.log.closed` |
| `2026-08-01 17:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d30f716b313

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:21 |
| **Last Seen** | 2026-08-01 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:21:54` | `cowrie.session.connect` |
| `2026-08-01 17:21:54` | `cowrie.client.version` |
| `2026-08-01 17:21:54` | `cowrie.client.kex` |
| `2026-08-01 17:21:54` | `cowrie.login.success` |
| `2026-08-01 17:21:55` | `cowrie.session.params` |
| `2026-08-01 17:21:55` | `cowrie.command.input` |
| `2026-08-01 17:21:55` | `cowrie.log.closed` |
| `2026-08-01 17:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5303094a9222

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:00` | `cowrie.session.connect` |
| `2026-08-01 17:22:00` | `cowrie.client.version` |
| `2026-08-01 17:22:00` | `cowrie.client.kex` |
| `2026-08-01 17:22:01` | `cowrie.login.success` |
| `2026-08-01 17:22:02` | `cowrie.session.params` |
| `2026-08-01 17:22:02` | `cowrie.command.input` |
| `2026-08-01 17:22:02` | `cowrie.log.closed` |
| `2026-08-01 17:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32d60560ce6c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:06` | `cowrie.session.connect` |
| `2026-08-01 17:22:06` | `cowrie.client.version` |
| `2026-08-01 17:22:07` | `cowrie.client.kex` |
| `2026-08-01 17:22:07` | `cowrie.login.success` |
| `2026-08-01 17:22:08` | `cowrie.session.params` |
| `2026-08-01 17:22:08` | `cowrie.command.input` |
| `2026-08-01 17:22:08` | `cowrie.log.closed` |
| `2026-08-01 17:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b5a6e3fe28a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:13` | `cowrie.session.connect` |
| `2026-08-01 17:22:13` | `cowrie.client.version` |
| `2026-08-01 17:22:13` | `cowrie.client.kex` |
| `2026-08-01 17:22:13` | `cowrie.login.success` |
| `2026-08-01 17:22:14` | `cowrie.session.params` |
| `2026-08-01 17:22:14` | `cowrie.command.input` |
| `2026-08-01 17:22:14` | `cowrie.log.closed` |
| `2026-08-01 17:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6261931a9fea

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:14` | `cowrie.session.connect` |
| `2026-08-01 17:22:14` | `cowrie.client.version` |
| `2026-08-01 17:22:14` | `cowrie.client.kex` |
| `2026-08-01 17:22:16` | `cowrie.login.success` |
| `2026-08-01 17:22:17` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc8f24f6d6c

| Field | Detail |
|---|---|
| **Source IP** | `163.192.48[.]255` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:18` | `cowrie.session.connect` |
| `2026-08-01 17:22:18` | `cowrie.client.version` |
| `2026-08-01 17:22:18` | `cowrie.client.kex` |
| `2026-08-01 17:22:18` | `cowrie.login.success` |
| `2026-08-01 17:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.192.48[.]255` to AbuseIPDB if not already reported
- [ ] Block `163.192.48[.]255` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94fb35bea392

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:19` | `cowrie.session.connect` |
| `2026-08-01 17:22:19` | `cowrie.client.version` |
| `2026-08-01 17:22:19` | `cowrie.client.kex` |
| `2026-08-01 17:22:20` | `cowrie.login.success` |
| `2026-08-01 17:22:21` | `cowrie.session.params` |
| `2026-08-01 17:22:21` | `cowrie.command.input` |
| `2026-08-01 17:22:21` | `cowrie.log.closed` |
| `2026-08-01 17:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e79c1d6033d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:25` | `cowrie.session.connect` |
| `2026-08-01 17:22:25` | `cowrie.client.version` |
| `2026-08-01 17:22:25` | `cowrie.client.kex` |
| `2026-08-01 17:22:25` | `cowrie.login.success` |
| `2026-08-01 17:22:27` | `cowrie.session.params` |
| `2026-08-01 17:22:27` | `cowrie.command.input` |
| `2026-08-01 17:22:27` | `cowrie.log.closed` |
| `2026-08-01 17:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7ecdda1a57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:31` | `cowrie.session.connect` |
| `2026-08-01 17:22:31` | `cowrie.client.version` |
| `2026-08-01 17:22:31` | `cowrie.client.kex` |
| `2026-08-01 17:22:32` | `cowrie.login.success` |
| `2026-08-01 17:22:33` | `cowrie.session.params` |
| `2026-08-01 17:22:33` | `cowrie.command.input` |
| `2026-08-01 17:22:33` | `cowrie.log.closed` |
| `2026-08-01 17:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8ec287c772

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:31` | `cowrie.session.connect` |
| `2026-08-01 17:22:31` | `cowrie.client.version` |
| `2026-08-01 17:22:31` | `cowrie.client.kex` |
| `2026-08-01 17:22:32` | `cowrie.login.success` |
| `2026-08-01 17:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8b0cb733a37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:37` | `cowrie.session.connect` |
| `2026-08-01 17:22:37` | `cowrie.client.version` |
| `2026-08-01 17:22:37` | `cowrie.client.kex` |
| `2026-08-01 17:22:37` | `cowrie.login.success` |
| `2026-08-01 17:22:38` | `cowrie.session.params` |
| `2026-08-01 17:22:38` | `cowrie.command.input` |
| `2026-08-01 17:22:38` | `cowrie.log.closed` |
| `2026-08-01 17:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efdddd5382e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:43` | `cowrie.session.connect` |
| `2026-08-01 17:22:43` | `cowrie.client.version` |
| `2026-08-01 17:22:43` | `cowrie.client.kex` |
| `2026-08-01 17:22:44` | `cowrie.login.success` |
| `2026-08-01 17:22:45` | `cowrie.session.params` |
| `2026-08-01 17:22:45` | `cowrie.command.input` |
| `2026-08-01 17:22:45` | `cowrie.log.closed` |
| `2026-08-01 17:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04231d062431

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:50` | `cowrie.session.connect` |
| `2026-08-01 17:22:50` | `cowrie.client.version` |
| `2026-08-01 17:22:50` | `cowrie.client.kex` |
| `2026-08-01 17:22:50` | `cowrie.login.success` |
| `2026-08-01 17:22:51` | `cowrie.session.params` |
| `2026-08-01 17:22:51` | `cowrie.command.input` |
| `2026-08-01 17:22:51` | `cowrie.log.closed` |
| `2026-08-01 17:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01bde41e10cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:22 |
| **Last Seen** | 2026-08-01 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:22:56` | `cowrie.session.connect` |
| `2026-08-01 17:22:56` | `cowrie.client.version` |
| `2026-08-01 17:22:56` | `cowrie.client.kex` |
| `2026-08-01 17:22:56` | `cowrie.login.success` |
| `2026-08-01 17:22:57` | `cowrie.session.params` |
| `2026-08-01 17:22:57` | `cowrie.command.input` |
| `2026-08-01 17:22:57` | `cowrie.log.closed` |
| `2026-08-01 17:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d20bb1dd3e96

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:01` | `cowrie.session.connect` |
| `2026-08-01 17:23:02` | `cowrie.client.version` |
| `2026-08-01 17:23:02` | `cowrie.client.kex` |
| `2026-08-01 17:23:02` | `cowrie.login.success` |
| `2026-08-01 17:23:03` | `cowrie.session.params` |
| `2026-08-01 17:23:03` | `cowrie.command.input` |
| `2026-08-01 17:23:03` | `cowrie.log.closed` |
| `2026-08-01 17:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72c820b208ec

| Field | Detail |
|---|---|
| **Source IP** | `192.161.49[.]2` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0, Accept: */*, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:06` | `cowrie.session.connect` |
| `2026-08-01 17:23:06` | `cowrie.login.success` |
| `2026-08-01 17:23:06` | `cowrie.session.params` |
| `2026-08-01 17:23:06` | `cowrie.command.input` |
| `2026-08-01 17:23:06` | `cowrie.command.input` |
| `2026-08-01 17:23:06` | `cowrie.command.failed` |
| `2026-08-01 17:23:06` | `cowrie.command.input` |
| `2026-08-01 17:23:06` | `cowrie.command.failed` |
| `2026-08-01 17:23:06` | `cowrie.command.input` |
| `2026-08-01 17:23:06` | `cowrie.log.closed` |
| `2026-08-01 17:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.161.49[.]2` to AbuseIPDB if not already reported
- [ ] Block `192.161.49[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d8ac37a91ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:08` | `cowrie.session.connect` |
| `2026-08-01 17:23:08` | `cowrie.client.version` |
| `2026-08-01 17:23:08` | `cowrie.client.kex` |
| `2026-08-01 17:23:08` | `cowrie.login.success` |
| `2026-08-01 17:23:09` | `cowrie.session.params` |
| `2026-08-01 17:23:09` | `cowrie.command.input` |
| `2026-08-01 17:23:09` | `cowrie.log.closed` |
| `2026-08-01 17:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc0f3ce4843

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:13` | `cowrie.session.connect` |
| `2026-08-01 17:23:13` | `cowrie.client.version` |
| `2026-08-01 17:23:13` | `cowrie.client.kex` |
| `2026-08-01 17:23:14` | `cowrie.login.success` |
| `2026-08-01 17:23:14` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9cacada5b1a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:14` | `cowrie.session.connect` |
| `2026-08-01 17:23:14` | `cowrie.client.version` |
| `2026-08-01 17:23:14` | `cowrie.client.kex` |
| `2026-08-01 17:23:15` | `cowrie.login.success` |
| `2026-08-01 17:23:16` | `cowrie.session.params` |
| `2026-08-01 17:23:16` | `cowrie.command.input` |
| `2026-08-01 17:23:16` | `cowrie.log.closed` |
| `2026-08-01 17:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4da33c0bc3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:20` | `cowrie.session.connect` |
| `2026-08-01 17:23:20` | `cowrie.client.version` |
| `2026-08-01 17:23:20` | `cowrie.client.kex` |
| `2026-08-01 17:23:20` | `cowrie.login.success` |
| `2026-08-01 17:23:21` | `cowrie.session.params` |
| `2026-08-01 17:23:21` | `cowrie.command.input` |
| `2026-08-01 17:23:21` | `cowrie.log.closed` |
| `2026-08-01 17:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a2c0f8c09c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:26` | `cowrie.session.connect` |
| `2026-08-01 17:23:26` | `cowrie.client.version` |
| `2026-08-01 17:23:26` | `cowrie.client.kex` |
| `2026-08-01 17:23:27` | `cowrie.login.success` |
| `2026-08-01 17:23:28` | `cowrie.session.params` |
| `2026-08-01 17:23:28` | `cowrie.command.input` |
| `2026-08-01 17:23:28` | `cowrie.log.closed` |
| `2026-08-01 17:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99d9106122e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:33` | `cowrie.session.connect` |
| `2026-08-01 17:23:33` | `cowrie.client.version` |
| `2026-08-01 17:23:33` | `cowrie.client.kex` |
| `2026-08-01 17:23:34` | `cowrie.login.success` |
| `2026-08-01 17:23:35` | `cowrie.session.params` |
| `2026-08-01 17:23:35` | `cowrie.command.input` |
| `2026-08-01 17:23:35` | `cowrie.log.closed` |
| `2026-08-01 17:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95913e40e52b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:39` | `cowrie.session.connect` |
| `2026-08-01 17:23:39` | `cowrie.client.version` |
| `2026-08-01 17:23:39` | `cowrie.client.kex` |
| `2026-08-01 17:23:39` | `cowrie.login.success` |
| `2026-08-01 17:23:40` | `cowrie.session.params` |
| `2026-08-01 17:23:40` | `cowrie.command.input` |
| `2026-08-01 17:23:40` | `cowrie.log.closed` |
| `2026-08-01 17:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab85e842253

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:45` | `cowrie.session.connect` |
| `2026-08-01 17:23:45` | `cowrie.client.version` |
| `2026-08-01 17:23:45` | `cowrie.client.kex` |
| `2026-08-01 17:23:45` | `cowrie.login.success` |
| `2026-08-01 17:23:46` | `cowrie.session.params` |
| `2026-08-01 17:23:46` | `cowrie.command.input` |
| `2026-08-01 17:23:47` | `cowrie.log.closed` |
| `2026-08-01 17:23:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600dd7e4bb1f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]227` |
| **First Seen** | 2026-08-01 17:23 |
| **Last Seen** | 2026-08-01 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:23:51` | `cowrie.session.connect` |
| `2026-08-01 17:23:51` | `cowrie.client.version` |
| `2026-08-01 17:23:51` | `cowrie.client.kex` |
| `2026-08-01 17:23:51` | `cowrie.login.success` |
| `2026-08-01 17:23:52` | `cowrie.session.params` |
| `2026-08-01 17:23:52` | `cowrie.command.input` |
| `2026-08-01 17:23:52` | `cowrie.log.closed` |
| `2026-08-01 17:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5136eb956edf

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-08-01 17:31 |
| **Last Seen** | 2026-08-01 17:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:31:30` | `cowrie.session.connect` |
| `2026-08-01 17:31:30` | `cowrie.client.version` |
| `2026-08-01 17:31:30` | `cowrie.client.kex` |
| `2026-08-01 17:31:32` | `cowrie.login.success` |
| `2026-08-01 17:31:33` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b199f809c76a

| Field | Detail |
|---|---|
| **Source IP** | `68.7.114[.]69` |
| **First Seen** | 2026-08-01 17:31 |
| **Last Seen** | 2026-08-01 17:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:31:42` | `cowrie.session.connect` |
| `2026-08-01 17:31:43` | `cowrie.client.version` |
| `2026-08-01 17:31:43` | `cowrie.client.kex` |
| `2026-08-01 17:31:44` | `cowrie.login.success` |
| `2026-08-01 17:31:44` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.7.114[.]69` to AbuseIPDB if not already reported
- [ ] Block `68.7.114[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-837f77b81e2c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.132[.]8` |
| **First Seen** | 2026-08-01 17:44 |
| **Last Seen** | 2026-08-01 17:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:44:31` | `cowrie.session.connect` |
| `2026-08-01 17:44:31` | `cowrie.login.success` |
| `2026-08-01 17:44:32` | `cowrie.session.params` |
| `2026-08-01 17:44:32` | `cowrie.command.input` |
| `2026-08-01 17:44:33` | `cowrie.command.input` |
| `2026-08-01 17:44:33` | `cowrie.command.input` |
| `2026-08-01 17:44:34` | `cowrie.command.input` |
| `2026-08-01 17:44:34` | `cowrie.command.failed` |
| `2026-08-01 17:44:35` | `cowrie.log.closed` |
| `2026-08-01 17:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.132[.]8` to AbuseIPDB if not already reported
- [ ] Block `176.65.132[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20329da8fe2f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 17:45 |
| **Last Seen** | 2026-08-01 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:45:37` | `cowrie.session.connect` |
| `2026-08-01 17:45:37` | `cowrie.client.version` |
| `2026-08-01 17:45:37` | `cowrie.client.kex` |
| `2026-08-01 17:45:37` | `cowrie.login.success` |
| `2026-08-01 17:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5faa643a98d3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 17:45 |
| **Last Seen** | 2026-08-01 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:45:37` | `cowrie.session.connect` |
| `2026-08-01 17:45:37` | `cowrie.client.version` |
| `2026-08-01 17:45:37` | `cowrie.client.kex` |
| `2026-08-01 17:45:37` | `cowrie.login.success` |
| `2026-08-01 17:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29984b8271e9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 17:45 |
| **Last Seen** | 2026-08-01 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:45:46` | `cowrie.session.connect` |
| `2026-08-01 17:45:46` | `cowrie.client.version` |
| `2026-08-01 17:45:46` | `cowrie.client.kex` |
| `2026-08-01 17:45:46` | `cowrie.login.success` |
| `2026-08-01 17:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c47b374bb72e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 17:45 |
| **Last Seen** | 2026-08-01 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:45:46` | `cowrie.session.connect` |
| `2026-08-01 17:45:46` | `cowrie.client.version` |
| `2026-08-01 17:45:46` | `cowrie.client.kex` |
| `2026-08-01 17:45:46` | `cowrie.login.success` |
| `2026-08-01 17:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6666904415cc

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-08-01 17:48 |
| **Last Seen** | 2026-08-01 17:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:48:09` | `cowrie.session.connect` |
| `2026-08-01 17:48:09` | `cowrie.client.version` |
| `2026-08-01 17:48:09` | `cowrie.client.kex` |
| `2026-08-01 17:48:12` | `cowrie.login.success` |
| `2026-08-01 17:48:12` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9c263a13ab

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-08-01 17:48 |
| **Last Seen** | 2026-08-01 17:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:48:22` | `cowrie.session.connect` |
| `2026-08-01 17:48:22` | `cowrie.client.version` |
| `2026-08-01 17:48:22` | `cowrie.client.kex` |
| `2026-08-01 17:48:24` | `cowrie.login.success` |
| `2026-08-01 17:48:24` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ca11a592825

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-08-01 17:51 |
| **Last Seen** | 2026-08-01 17:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:51:48` | `cowrie.session.connect` |
| `2026-08-01 17:51:49` | `cowrie.client.version` |
| `2026-08-01 17:51:49` | `cowrie.client.kex` |
| `2026-08-01 17:51:51` | `cowrie.login.success` |
| `2026-08-01 17:51:52` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8f41ce8dc2b

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-08-01 17:52 |
| **Last Seen** | 2026-08-01 17:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:52:01` | `cowrie.session.connect` |
| `2026-08-01 17:52:02` | `cowrie.client.version` |
| `2026-08-01 17:52:02` | `cowrie.client.kex` |
| `2026-08-01 17:52:04` | `cowrie.login.success` |
| `2026-08-01 17:52:05` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cbffddd2d35

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-08-01 17:57 |
| **Last Seen** | 2026-08-01 17:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:57:54` | `cowrie.session.connect` |
| `2026-08-01 17:57:54` | `cowrie.client.version` |
| `2026-08-01 17:57:54` | `cowrie.client.kex` |
| `2026-08-01 17:57:55` | `cowrie.login.success` |
| `2026-08-01 17:57:56` | `cowrie.direct-tcpip.request` |
| `2026-08-01 17:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d0324a7bf9

| Field | Detail |
|---|---|
| **Source IP** | `45.43.37[.]254` |
| **First Seen** | 2026-08-01 17:58 |
| **Last Seen** | 2026-08-01 17:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 17:58:49` | `cowrie.session.connect` |
| `2026-08-01 17:58:49` | `cowrie.telnet.option` |
| `2026-08-01 17:58:49` | `cowrie.telnet.option` |
| `2026-08-01 17:59:51` | `cowrie.login.success` |
| `2026-08-01 17:59:51` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `45.43.37[.]254` to AbuseIPDB if not already reported
- [ ] Block `45.43.37[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198ec6e22b90

| Field | Detail |
|---|---|
| **Source IP** | `107.150.100[.]146` |
| **First Seen** | 2026-08-01 18:02 |
| **Last Seen** | 2026-08-01 18:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:02:44` | `cowrie.session.connect` |
| `2026-08-01 18:02:44` | `cowrie.client.version` |
| `2026-08-01 18:02:44` | `cowrie.client.kex` |
| `2026-08-01 18:02:45` | `cowrie.login.success` |
| `2026-08-01 18:02:45` | `cowrie.session.params` |
| `2026-08-01 18:02:45` | `cowrie.command.input` |
| `2026-08-01 18:02:45` | `cowrie.command.failed` |
| `2026-08-01 18:02:46` | `cowrie.log.closed` |
| `2026-08-01 18:02:46` | `cowrie.session.params` |
| `2026-08-01 18:02:46` | `cowrie.command.input` |
| `2026-08-01 18:02:46` | `cowrie.session.file_download` |
| `2026-08-01 18:02:46` | `cowrie.log.closed` |
| `2026-08-01 18:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.100[.]146` to AbuseIPDB if not already reported
- [ ] Block `107.150.100[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86cfce31e471

| Field | Detail |
|---|---|
| **Source IP** | `107.150.100[.]146` |
| **First Seen** | 2026-08-01 18:02 |
| **Last Seen** | 2026-08-01 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:02:46` | `cowrie.session.connect` |
| `2026-08-01 18:02:46` | `cowrie.client.version` |
| `2026-08-01 18:02:47` | `cowrie.client.kex` |
| `2026-08-01 18:02:47` | `cowrie.login.success` |
| `2026-08-01 18:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.100[.]146` to AbuseIPDB if not already reported
- [ ] Block `107.150.100[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac9f4762c7e2

| Field | Detail |
|---|---|
| **Source IP** | `107.150.100[.]146` |
| **First Seen** | 2026-08-01 18:02 |
| **Last Seen** | 2026-08-01 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:02:47` | `cowrie.session.connect` |
| `2026-08-01 18:02:47` | `cowrie.client.version` |
| `2026-08-01 18:02:47` | `cowrie.client.kex` |
| `2026-08-01 18:02:47` | `cowrie.login.success` |
| `2026-08-01 18:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.100[.]146` to AbuseIPDB if not already reported
- [ ] Block `107.150.100[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8df93e1bc57

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 18:03 |
| **Last Seen** | 2026-08-01 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:03:09` | `cowrie.session.connect` |
| `2026-08-01 18:03:09` | `cowrie.client.version` |
| `2026-08-01 18:03:10` | `cowrie.client.kex` |
| `2026-08-01 18:03:10` | `cowrie.login.success` |
| `2026-08-01 18:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87d7f2eb1c1e

| Field | Detail |
|---|---|
| **Source IP** | `138.124.30[.]187` |
| **First Seen** | 2026-08-01 18:05 |
| **Last Seen** | 2026-08-01 18:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:05:17` | `cowrie.session.connect` |
| `2026-08-01 18:05:17` | `cowrie.client.version` |
| `2026-08-01 18:05:17` | `cowrie.client.kex` |
| `2026-08-01 18:05:17` | `cowrie.login.success` |
| `2026-08-01 18:05:18` | `cowrie.session.params` |
| `2026-08-01 18:05:18` | `cowrie.command.input` |
| `2026-08-01 18:05:18` | `cowrie.command.failed` |
| `2026-08-01 18:05:18` | `cowrie.log.closed` |
| `2026-08-01 18:05:19` | `cowrie.session.params` |
| `2026-08-01 18:05:19` | `cowrie.command.input` |
| `2026-08-01 18:05:19` | `cowrie.session.file_download` |
| `2026-08-01 18:05:19` | `cowrie.log.closed` |
| `2026-08-01 18:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.30[.]187` to AbuseIPDB if not already reported
- [ ] Block `138.124.30[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59636ed8346c

| Field | Detail |
|---|---|
| **Source IP** | `138.124.30[.]187` |
| **First Seen** | 2026-08-01 18:05 |
| **Last Seen** | 2026-08-01 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:05:19` | `cowrie.session.connect` |
| `2026-08-01 18:05:19` | `cowrie.client.version` |
| `2026-08-01 18:05:19` | `cowrie.client.kex` |
| `2026-08-01 18:05:20` | `cowrie.login.success` |
| `2026-08-01 18:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.30[.]187` to AbuseIPDB if not already reported
- [ ] Block `138.124.30[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6acb2ed1bfd4

| Field | Detail |
|---|---|
| **Source IP** | `138.124.30[.]187` |
| **First Seen** | 2026-08-01 18:05 |
| **Last Seen** | 2026-08-01 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:05:20` | `cowrie.session.connect` |
| `2026-08-01 18:05:20` | `cowrie.client.version` |
| `2026-08-01 18:05:20` | `cowrie.client.kex` |
| `2026-08-01 18:05:20` | `cowrie.login.success` |
| `2026-08-01 18:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.30[.]187` to AbuseIPDB if not already reported
- [ ] Block `138.124.30[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3263d019aac4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 18:15 |
| **Last Seen** | 2026-08-01 18:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:15:54` | `cowrie.session.connect` |
| `2026-08-01 18:15:54` | `cowrie.client.version` |
| `2026-08-01 18:15:54` | `cowrie.client.kex` |
| `2026-08-01 18:15:54` | `cowrie.login.success` |
| `2026-08-01 18:15:54` | `cowrie.direct-tcpip.request` |
| `2026-08-01 18:15:54` | `cowrie.direct-tcpip.data` |
| `2026-08-01 18:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5e51756e23

| Field | Detail |
|---|---|
| **Source IP** | `60.174.35[.]18` |
| **First Seen** | 2026-08-01 18:22 |
| **Last Seen** | 2026-08-01 18:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:22:59` | `cowrie.session.connect` |
| `2026-08-01 18:23:00` | `cowrie.client.version` |
| `2026-08-01 18:23:00` | `cowrie.client.kex` |
| `2026-08-01 18:23:02` | `cowrie.login.success` |
| `2026-08-01 18:23:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 18:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.35[.]18` to AbuseIPDB if not already reported
- [ ] Block `60.174.35[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e345f66219

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-08-01 18:26 |
| **Last Seen** | 2026-08-01 18:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:26:32` | `cowrie.session.connect` |
| `2026-08-01 18:26:33` | `cowrie.client.version` |
| `2026-08-01 18:26:33` | `cowrie.client.kex` |
| `2026-08-01 18:26:35` | `cowrie.login.success` |
| `2026-08-01 18:26:35` | `cowrie.direct-tcpip.request` |
| `2026-08-01 18:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f155b914f11c

| Field | Detail |
|---|---|
| **Source IP** | `194.31.8[.]12` |
| **First Seen** | 2026-08-01 18:31 |
| **Last Seen** | 2026-08-01 18:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:31:44` | `cowrie.session.connect` |
| `2026-08-01 18:31:45` | `cowrie.client.version` |
| `2026-08-01 18:31:45` | `cowrie.client.kex` |
| `2026-08-01 18:31:46` | `cowrie.login.success` |
| `2026-08-01 18:31:46` | `cowrie.direct-tcpip.request` |
| `2026-08-01 18:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.31.8[.]12` to AbuseIPDB if not already reported
- [ ] Block `194.31.8[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc985af77490

| Field | Detail |
|---|---|
| **Source IP** | `20.227.140[.]178` |
| **First Seen** | 2026-08-01 18:45 |
| **Last Seen** | 2026-08-01 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:45:47` | `cowrie.session.connect` |
| `2026-08-01 18:45:47` | `cowrie.client.version` |
| `2026-08-01 18:45:47` | `cowrie.client.kex` |
| `2026-08-01 18:45:47` | `cowrie.login.success` |
| `2026-08-01 18:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.227.140[.]178` to AbuseIPDB if not already reported
- [ ] Block `20.227.140[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f82a14ab7b75

| Field | Detail |
|---|---|
| **Source IP** | `198.98.53[.]110` |
| **First Seen** | 2026-08-01 18:48 |
| **Last Seen** | 2026-08-01 18:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system, shell, sh` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:48:56` | `cowrie.session.connect` |
| `2026-08-01 18:48:58` | `cowrie.telnet.option` |
| `2026-08-01 18:48:59` | `cowrie.telnet.option` |
| `2026-08-01 18:48:59` | `cowrie.login.success` |
| `2026-08-01 18:49:00` | `cowrie.session.params` |
| `2026-08-01 18:49:02` | `cowrie.telnet.option` |
| `2026-08-01 18:49:02` | `cowrie.telnet.option` |
| `2026-08-01 18:49:02` | `cowrie.command.input` |
| `2026-08-01 18:49:02` | `cowrie.command.input` |
| `2026-08-01 18:49:02` | `cowrie.command.failed` |
| `2026-08-01 18:49:02` | `cowrie.command.input` |
| `2026-08-01 18:49:02` | `cowrie.command.failed` |
| `2026-08-01 18:49:02` | `cowrie.command.input` |
| `2026-08-01 18:49:02` | `cowrie.command.failed` |
| `2026-08-01 18:49:02` | `cowrie.command.input` |
| `2026-08-01 18:49:02` | `cowrie.command.input` |
| `2026-08-01 18:49:02` | `cowrie.command.input` |
| `2026-08-01 18:49:02` | `cowrie.command.input` |
| `2026-08-01 18:49:02` | `cowrie.command.input` |
| `2026-08-01 18:49:02` | `cowrie.command.input` |
| `2026-08-01 18:49:03` | `cowrie.log.closed` |
| `2026-08-01 18:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.53[.]110` to AbuseIPDB if not already reported
- [ ] Block `198.98.53[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f43b073fd0

| Field | Detail |
|---|---|
| **Source IP** | `121.40.20[.]65` |
| **First Seen** | 2026-08-01 18:49 |
| **Last Seen** | 2026-08-01 18:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:49:52` | `cowrie.session.connect` |
| `2026-08-01 18:49:52` | `cowrie.client.version` |
| `2026-08-01 18:49:52` | `cowrie.client.kex` |
| `2026-08-01 18:49:53` | `cowrie.login.success` |
| `2026-08-01 18:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.40.20[.]65` to AbuseIPDB if not already reported
- [ ] Block `121.40.20[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483510c128fd

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-01 18:49 |
| **Last Seen** | 2026-08-01 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 18:49:53` | `cowrie.session.connect` |
| `2026-08-01 18:49:53` | `cowrie.client.version` |
| `2026-08-01 18:49:53` | `cowrie.client.kex` |
| `2026-08-01 18:49:53` | `cowrie.login.success` |
| `2026-08-01 18:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.227.254[.]154` | **6** | 2026-08-01 17:05 | 2026-08-01 17:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]121` | **5** | 2026-08-01 18:48 | 2026-08-01 18:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-08-01 18:46 | 2026-08-01 18:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]213` | **3** | 2026-08-01 17:20 | 2026-08-01 17:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]104` | **3** | 2026-08-01 18:47 | 2026-08-01 18:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]73` | **3** | 2026-08-01 18:48 | 2026-08-01 18:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-01 18:18 | 2026-08-01 18:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.124[.]200` | **2** | 2026-08-01 18:12 | 2026-08-01 18:14 | 2m | 0 | `T1592` | 🟢 LOW |
| `124.89.83[.]31` | **2** | 2026-08-01 18:40 | 2026-08-01 18:42 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-01 17:15 | 2026-08-01 18:13 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.194[.]130` | **2** | 2026-08-01 18:52 | 2026-08-01 18:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | **2** | 2026-08-01 17:08 | 2026-08-01 17:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-01 17:32 | 2026-08-01 18:38 | 2m | 0 | `T1592` | 🟢 LOW |
| `104.152.58[.]233` | 1 | 2026-08-01 17:48 | 2026-08-01 17:48 | 1s | 0 | `T1592` | 🟢 LOW |
| `116.255.226[.]73` | 1 | 2026-08-01 17:41 | 2026-08-01 17:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.52.92[.]90` | 1 | 2026-08-01 18:06 | 2026-08-01 18:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-01 18:13 | 2026-08-01 18:13 | 37s | 0 | `T1592` | 🟢 LOW |
| `176.65.132[.]8` | 1 | 2026-08-01 17:44 | 2026-08-01 17:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.55.126[.]88` | 1 | 2026-08-01 17:29 | 2026-08-01 17:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `20.3.129[.]142` | 1 | 2026-08-01 17:28 | 2026-08-01 17:28 | 33s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]212` | 1 | 2026-08-01 17:20 | 2026-08-01 17:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]214` | 1 | 2026-08-01 17:20 | 2026-08-01 17:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]222` | 1 | 2026-08-01 17:20 | 2026-08-01 17:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.66.197[.]199` | 1 | 2026-08-01 17:22 | 2026-08-01 17:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-08-01 17:06 | 2026-08-01 17:07 | 32s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]209` | 1 | 2026-08-01 18:47 | 2026-08-01 18:47 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]90` | 1 | 2026-08-01 16:58 | 2026-08-01 16:58 | 16s | 0 | `T1592` | 🟢 LOW |
| `69.244.92[.]158` | 1 | 2026-08-01 16:58 | 2026-08-01 16:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `8.209.236[.]13` | 1 | 2026-08-01 17:41 | 2026-08-01 17:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.14.4[.]190` | 1 | 2026-08-01 17:24 | 2026-08-01 17:25 | 12s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]78` | 1 | 2026-08-01 17:48 | 2026-08-01 17:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `91.92.42[.]227` | 1 | 2026-08-01 17:08 | 2026-08-01 17:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

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

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
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
| `124.89.83[.]31` | CN | China Unicom Shannxi province network | **100** ⚠️ | 3 |
| `213.66.197[.]199` | SE | Telia Network services | **100** ⚠️ | 43 |
| `66.132.195[.]121` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `66.132.195[.]73` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `20.227.140[.]178` | AU | Microsoft Corporation | **100** ⚠️ | 23 |
| `204.76.203[.]222` | NL | Intelligence Hosting LLC | **100** ⚠️ | 27 |
| `163.192.48[.]255` | US | Oracle Corporation | **100** ⚠️ | 14 |
| `203.252.10[.]3` | KR | LG DACOM Corporation | **100** ⚠️ | 50 |
| `204.76.203[.]213` | NL | Intelligence Hosting LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 313 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 306 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 378 cases |
| Tool 34  | Credential Extractor        | ✅ 323 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 74 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (4.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 306 priority case(s) shown individually · 32 recon entry/entries in table (13 group(s) consolidating 38 session(s)).

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
_Report time: 2026-08-01T19:15:38Z_

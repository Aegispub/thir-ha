# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-15 |
| **Generated At** | 2026-08-15T18:34:04Z |
| **Shift Time** | 18:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **6094** |
| Confirmed Threats | **6054** |
| False Positives Filtered | **40** (0.7%) |
| Unique Attacker IPs | **97** |
| Countries of Origin | **35** |
| High Severity Cases | **336** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **5758** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **356** |
| Unique Credential Pairs | **314** |
| Unique Usernames | **127** |
| Unique Passwords | **197** |
| Successful Auth Pairs | **347** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 90 |
| `debian` | 15 |
| `user` | 14 |
| `admin` | 10 |
| `config` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 22 |
| `123` | 17 |
| `1234` | 10 |
| `1` | 8 |
| `root` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `qwerty123` | 6 |
| `config` | `6666` | 6 |
| `debian` | `1q2w3e4r` | 5 |
| `debian` | `webmaster` | 5 |
| `user` | `password321` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `airflow` | `airflow` | `77.239.124.237` | 2026-08-15T14:55:10 |
| `data` | `data` | `77.239.124.237` | 2026-08-15T14:55:19 |
| `hadoop` | `123` | `77.239.124.237` | 2026-08-15T14:55:27 |
| `tom` | `tom` | `77.239.124.237` | 2026-08-15T14:55:35 |
| `kipt` | `kipt` | `77.239.124.237` | 2026-08-15T14:55:44 |
| `administrator` | `Passw0rd` | `77.239.124.237` | 2026-08-15T14:55:53 |
| `appuser` | `appuser` | `77.239.124.237` | 2026-08-15T14:56:01 |
| `root` | `test123` | `77.239.124.237` | 2026-08-15T14:56:08 |
| `root` | `00000000` | `77.239.124.237` | 2026-08-15T14:56:16 |
| `www` | `123321` | `77.239.124.237` | 2026-08-15T14:56:24 |
| `asterisk` | `asterisk` | `77.239.124.237` | 2026-08-15T14:56:33 |
| `root` | `Aa123456` | `77.239.124.237` | 2026-08-15T14:56:40 |
| `deploy` | `root` | `77.239.124.237` | 2026-08-15T14:56:48 |
| `odoo17` | `odoo17` | `77.239.124.237` | 2026-08-15T14:56:57 |
| `openclaw` | `123456` | `77.239.124.237` | 2026-08-15T14:57:05 |
| `trade` | `123456` | `77.239.124.237` | 2026-08-15T14:57:13 |
| `root` | `!QAZ2wsx3edc` | `77.239.124.237` | 2026-08-15T14:57:22 |
| `deploy` | `!Q2w3e4r` | `77.239.124.237` | 2026-08-15T14:57:30 |
| `ubuntu` | `1234` | `77.239.124.237` | 2026-08-15T14:57:38 |
| `user3` | `12345678` | `77.239.124.237` | 2026-08-15T14:57:47 |
| `user2` | `123456` | `77.239.124.237` | 2026-08-15T14:57:56 |
| `user` | `12345` | `77.239.124.237` | 2026-08-15T14:58:04 |
| `alex` | `12345678` | `77.239.124.237` | 2026-08-15T14:58:13 |
| `labuser` | `p@ssw0rd` | `77.239.124.237` | 2026-08-15T14:58:22 |
| `debian` | `123456` | `77.239.124.237` | 2026-08-15T14:58:31 |
| `user1` | `123456789` | `77.239.124.237` | 2026-08-15T14:58:39 |
| `openvpn` | `openvpn` | `77.239.124.237` | 2026-08-15T14:58:47 |
| `root` | `Welcome123` | `77.239.124.237` | 2026-08-15T14:58:55 |
| `root` | `000000` | `77.239.124.237` | 2026-08-15T14:59:03 |
| `adminuser` | `adminuser` | `77.239.124.237` | 2026-08-15T14:59:12 |
| `root` | `Aa123456@` | `77.239.124.237` | 2026-08-15T14:59:21 |
| `dev` | `password` | `77.239.124.237` | 2026-08-15T14:59:29 |
| `openclaw` | `1234` | `77.239.124.237` | 2026-08-15T14:59:38 |
| `user` | `111111` | `77.239.124.237` | 2026-08-15T14:59:45 |
| `rdpuser` | `123` | `77.239.124.237` | 2026-08-15T14:59:54 |
| `test` | `test1234` | `77.239.124.237` | 2026-08-15T15:00:03 |
| `debian` | `debian` | `77.239.124.237` | 2026-08-15T15:00:11 |
| `admin2` | `admin2` | `77.239.124.237` | 2026-08-15T15:00:20 |
| `user` | `user` | `77.239.124.237` | 2026-08-15T15:00:28 |
| `ecommerce` | `ecommerce` | `77.239.124.237` | 2026-08-15T15:00:36 |
| `pi` | `1234` | `77.239.124.237` | 2026-08-15T15:00:45 |
| `minecraft` | `password` | `77.239.124.237` | 2026-08-15T15:00:53 |
| `admin` | `password` | `77.239.124.237` | 2026-08-15T15:01:02 |
| `appuser` | `password` | `77.239.124.237` | 2026-08-15T15:01:11 |
| `root` | `toor` | `77.239.124.237` | 2026-08-15T15:01:19 |
| `cursor` | `cursor` | `77.239.124.237` | 2026-08-15T15:01:27 |
| `root` | `Pass1234` | `77.239.124.237` | 2026-08-15T15:01:36 |
| `uftp` | `uftp` | `77.239.124.237` | 2026-08-15T15:01:44 |
| `root` | `Qwerty123` | `77.239.124.237` | 2026-08-15T15:01:52 |
| `root` | `4` | `187.49.63.51` | 2026-08-15T15:01:54 |
| `amit` | `amit` | `77.239.124.237` | 2026-08-15T15:02:01 |
| `root` | `4` | `64.72.74.162` | 2026-08-15T15:02:04 |
| `root` | `!Q2w3e4r` | `77.239.124.237` | 2026-08-15T15:02:09 |
| `dev` | `123456` | `77.239.124.237` | 2026-08-15T15:02:18 |
| `student` | `student123` | `77.239.124.237` | 2026-08-15T15:02:26 |
| `root` | `baidu@123` | `77.239.124.237` | 2026-08-15T15:02:34 |
| `ftpuser` | `123` | `77.239.124.237` | 2026-08-15T15:02:42 |
| `root` | `11` | `77.239.124.237` | 2026-08-15T15:02:50 |
| `guest` | `pi` | `77.239.124.237` | 2026-08-15T15:02:58 |
| `root` | `eve` | `77.239.124.237` | 2026-08-15T15:03:06 |
| `webuser` | `123456` | `77.239.124.237` | 2026-08-15T15:03:15 |
| `manoj` | `manoj123` | `77.239.124.237` | 2026-08-15T15:03:23 |
| `user` | `123` | `77.239.124.237` | 2026-08-15T15:03:31 |
| `debian` | `1q2w3e4r` | `10.0.0.73` | 2026-08-15T15:03:35 |
| `pi` | `root` | `77.239.124.237` | 2026-08-15T15:03:40 |
| `root` | `pass` | `77.239.124.237` | 2026-08-15T15:03:48 |
| `root` | `!Q@W3e4r` | `77.239.124.237` | 2026-08-15T15:03:57 |
| `onkar` | `onkar123` | `77.239.124.237` | 2026-08-15T15:04:05 |
| `debian` | `toor` | `77.239.124.237` | 2026-08-15T15:04:13 |
| `app` | `123` | `77.239.124.237` | 2026-08-15T15:04:22 |
| `root` | `P@ssword` | `77.239.124.237` | 2026-08-15T15:04:30 |
| `dmdba` | `dmdba123456` | `77.239.124.237` | 2026-08-15T15:04:39 |
| `testuser` | `123321` | `77.239.124.237` | 2026-08-15T15:04:47 |
| `root` | `admin123` | `77.239.124.237` | 2026-08-15T15:04:55 |
| `root` | `a1b2c3d4` | `217.165.22.192` | 2026-08-15T15:05:01 |
| `myuser` | `root` | `77.239.124.237` | 2026-08-15T15:05:04 |
| `steam` | `123` | `77.239.124.237` | 2026-08-15T15:05:12 |
| `debian` | `1q2w3e4r` | `124.239.169.52` | 2026-08-15T15:05:13 |
| `root` | `1qaz@WSX` | `77.239.124.237` | 2026-08-15T15:05:20 |
| `debian` | `1q2w3e4r` | `65.20.202.4` | 2026-08-15T15:05:27 |
| `deployer` | `user` | `77.239.124.237` | 2026-08-15T15:05:29 |
| `karel` | `karel` | `77.239.124.237` | 2026-08-15T15:05:37 |
| `niaoyun` | `123456` | `77.239.124.237` | 2026-08-15T15:05:45 |
| `nutanix` | `nutanix/4u` | `77.239.124.237` | 2026-08-15T15:05:54 |
| `dani` | `dani` | `77.239.124.237` | 2026-08-15T15:06:03 |
| `claude` | `abc123` | `77.239.124.237` | 2026-08-15T15:06:11 |
| `root` | `28011988` | `77.239.124.237` | 2026-08-15T15:06:19 |
| `alex` | `1` | `77.239.124.237` | 2026-08-15T15:06:27 |
| `kim` | `kim123` | `77.239.124.237` | 2026-08-15T15:06:36 |
| `pi` | `p@ssw0rd` | `77.239.124.237` | 2026-08-15T15:06:44 |
| `test` | `qwerty123` | `178.178.222.60` | 2026-08-15T15:06:51 |
| `admin123` | `1234` | `77.239.124.237` | 2026-08-15T15:06:52 |
| `test` | `qwerty123` | `101.13.5.26` | 2026-08-15T15:07:00 |
| `sftpuser` | `123` | `77.239.124.237` | 2026-08-15T15:07:01 |
| `frappe` | `frappe123` | `77.239.124.237` | 2026-08-15T15:07:09 |
| `guest` | `123456` | `77.239.124.237` | 2026-08-15T15:07:18 |
| `gateway` | `gateway` | `77.239.124.237` | 2026-08-15T15:07:26 |
| `home` | `home` | `77.239.124.237` | 2026-08-15T15:07:34 |
| `ubuntu` | `rootroot` | `77.239.124.237` | 2026-08-15T15:07:43 |
| `user1` | `root@123` | `77.239.124.237` | 2026-08-15T15:07:51 |
| `david` | `123456` | `77.239.124.237` | 2026-08-15T15:07:59 |
| `bernard` | `bernard` | `77.239.124.237` | 2026-08-15T15:08:06 |
| `ts` | `ts` | `77.239.124.237` | 2026-08-15T15:08:15 |
| `nexus` | `pi` | `77.239.124.237` | 2026-08-15T15:08:24 |
| `linuxuser` | `1` | `77.239.124.237` | 2026-08-15T15:08:31 |
| `root` | `abc12345` | `77.239.124.237` | 2026-08-15T15:08:40 |
| `t1` | `123` | `77.239.124.237` | 2026-08-15T15:08:49 |
| `root` | `Aa1234567890` | `77.239.124.237` | 2026-08-15T15:08:57 |
| `newuser` | `123` | `77.239.124.237` | 2026-08-15T15:09:06 |
| `root` | `19901017` | `77.239.124.237` | 2026-08-15T15:09:13 |
| `frappe` | `12345678` | `77.239.124.237` | 2026-08-15T15:09:22 |
| `support` | `techsupport` | `123.123.196.140` | 2026-08-15T15:09:26 |
| `odoo` | `123` | `77.239.124.237` | 2026-08-15T15:09:30 |
| `support` | `techsupport` | `185.40.122.250` | 2026-08-15T15:09:37 |
| `support` | `techsupport` | `125.35.109.214` | 2026-08-15T15:09:38 |
| `deployer` | `deployer123` | `77.239.124.237` | 2026-08-15T15:09:38 |
| `support` | `techsupport` | `83.166.50.15` | 2026-08-15T15:09:46 |
| `root` | `root@2026` | `77.239.124.237` | 2026-08-15T15:09:46 |
| `odoo17` | `12345` | `77.239.124.237` | 2026-08-15T15:09:55 |
| `frappe` | `frappe@123` | `77.239.124.237` | 2026-08-15T15:10:03 |
| `debian` | `qwerty` | `77.239.124.237` | 2026-08-15T15:10:11 |
| `milad` | `milad` | `77.239.124.237` | 2026-08-15T15:10:19 |
| `prem` | `12345` | `77.239.124.237` | 2026-08-15T15:10:27 |
| `neptune` | `neptune` | `77.239.124.237` | 2026-08-15T15:10:35 |
| `root` | `qq123456` | `77.239.124.237` | 2026-08-15T15:10:43 |
| `root` | `Welcome@123` | `77.239.124.237` | 2026-08-15T15:10:53 |
| `jellyfin` | `123` | `77.239.124.237` | 2026-08-15T15:11:01 |
| `user3` | `user3` | `77.239.124.237` | 2026-08-15T15:11:09 |
| `data` | `test` | `77.239.124.237` | 2026-08-15T15:11:18 |
| `ai` | `Aa123456` | `77.239.124.237` | 2026-08-15T15:11:26 |
| `admin1` | `123456` | `77.239.124.237` | 2026-08-15T15:11:35 |
| `admin` | `1234` | `77.239.124.237` | 2026-08-15T15:11:43 |
| `root` | `!qaz@WSX` | `77.239.124.237` | 2026-08-15T15:11:51 |
| `fastuser` | `1234567890` | `77.239.124.237` | 2026-08-15T15:12:00 |
| `admin` | `admin` | `157.245.213.135` | 2026-08-15T15:12:04 |
| `fivem` | `12345` | `77.239.124.237` | 2026-08-15T15:12:09 |
| `app` | `rootroot` | `77.239.124.237` | 2026-08-15T15:12:17 |
| `ranga` | `ranga` | `77.239.124.237` | 2026-08-15T15:12:25 |
| `root` | `qazwsxedc` | `77.239.124.237` | 2026-08-15T15:12:34 |
| `support` | `123` | `77.239.124.237` | 2026-08-15T15:12:43 |
| `user10` | `user10` | `77.239.124.237` | 2026-08-15T15:12:51 |
| `admin` | `P@ssw0rd` | `77.239.124.237` | 2026-08-15T15:12:59 |
| `root` | `Aa123456.` | `45.142.193.164` | 2026-08-15T15:13:00 |
| `testuser` | `test` | `77.239.124.237` | 2026-08-15T15:13:08 |
| `oracle` | `Aa123456` | `77.239.124.237` | 2026-08-15T15:13:17 |
| `debian` | `Aa123456.` | `77.239.124.237` | 2026-08-15T15:13:26 |
| `dev` | `123` | `77.239.124.237` | 2026-08-15T15:13:34 |
| `root` | `1qazxsw2` | `77.239.124.237` | 2026-08-15T15:13:42 |
| `claude` | `root` | `77.239.124.237` | 2026-08-15T15:13:50 |
| `master` | `passwd` | `77.239.124.237` | 2026-08-15T15:13:57 |
| `ec2-user` | `ec2-user` | `77.239.124.237` | 2026-08-15T15:14:06 |
| `devuser` | `devuser` | `77.239.124.237` | 2026-08-15T15:14:14 |
| `root` | `1qaz!QAZ` | `77.239.124.237` | 2026-08-15T15:14:23 |
| `cloud` | `cloud` | `77.239.124.237` | 2026-08-15T15:14:31 |
| `root` | `123abc456` | `77.239.124.237` | 2026-08-15T15:14:39 |
| `openclaw` | `123` | `77.239.124.237` | 2026-08-15T15:14:47 |
| `root` | `nPSpP4PBW0` | `77.239.124.237` | 2026-08-15T15:14:56 |
| `deployer` | `deployer` | `77.239.124.237` | 2026-08-15T15:15:05 |
| `david` | `david` | `77.239.124.237` | 2026-08-15T15:15:13 |
| `root` | `abc123` | `77.239.124.237` | 2026-08-15T15:15:21 |
| `admin` | `!QAZ2wsx` | `77.239.124.237` | 2026-08-15T15:15:30 |
| `root` | `Qq123456` | `77.239.124.237` | 2026-08-15T15:15:38 |
| `postgres` | `postgres` | `77.239.124.237` | 2026-08-15T15:15:46 |
| `testuser` | `123456` | `77.239.124.237` | 2026-08-15T15:15:54 |
| `kali` | `kali` | `77.239.124.237` | 2026-08-15T15:16:02 |
| `node` | `123456` | `77.239.124.237` | 2026-08-15T15:16:10 |
| `frappe` | `admin` | `77.239.124.237` | 2026-08-15T15:16:19 |
| `test` | `123456` | `77.239.124.237` | 2026-08-15T15:16:28 |
| `dmdba` | `123456` | `77.239.124.237` | 2026-08-15T15:16:36 |
| `root` | `welcome1` | `77.239.124.237` | 2026-08-15T15:16:45 |
| `ossuser` | `Changeme_123` | `77.239.124.237` | 2026-08-15T15:16:53 |
| `mysql` | `mysql` | `77.239.124.237` | 2026-08-15T15:17:01 |
| `root` | `Huawei@123` | `77.239.124.237` | 2026-08-15T15:17:10 |
| `minecraft` | `1234` | `77.239.124.237` | 2026-08-15T15:17:19 |
| `root` | `aA123456` | `77.239.124.237` | 2026-08-15T15:17:27 |
| `root` | `qwe123!@#` | `77.239.124.237` | 2026-08-15T15:17:35 |
| `deploy` | `qwerty123` | `77.239.124.237` | 2026-08-15T15:17:43 |
| `server` | `server` | `77.239.124.237` | 2026-08-15T15:17:51 |
| `root` | `rootrootroot` | `77.239.124.237` | 2026-08-15T15:18:00 |
| `user` | `git` | `77.239.124.237` | 2026-08-15T15:18:08 |
| `ftpuser` | `ftpuser` | `77.239.124.237` | 2026-08-15T15:18:16 |
| `root` | `12qwaszx` | `77.239.124.237` | 2026-08-15T15:18:24 |
| `test` | `qwerty123` | `10.0.0.73` | 2026-08-15T15:18:30 |
| `milad` | `milad123` | `77.239.124.237` | 2026-08-15T15:18:33 |
| `root` | `ZAQ!2wsx` | `77.239.124.237` | 2026-08-15T15:18:41 |
| `bot` | `123456` | `77.239.124.237` | 2026-08-15T15:18:50 |
| `nobody` | `1234` | `77.239.124.237` | 2026-08-15T15:18:59 |
| `test1` | `test1` | `77.239.124.237` | 2026-08-15T15:19:07 |
| `alex` | `1234` | `77.239.124.237` | 2026-08-15T15:19:14 |
| `rdpuser` | `123456` | `77.239.124.237` | 2026-08-15T15:19:22 |
| `root` | `102030` | `77.239.124.237` | 2026-08-15T15:19:31 |
| `ethan` | `ethan` | `77.239.124.237` | 2026-08-15T15:19:40 |
| `core` | `1qaz2wsx` | `77.239.124.237` | 2026-08-15T15:19:47 |
| `root` | `t0talc0ntr0l4!` | `77.239.124.237` | 2026-08-15T15:19:54 |
| `root` | `nD6ffS9msOngs` | `77.239.124.237` | 2026-08-15T15:20:01 |
| `root` | `Pass@123` | `77.239.124.237` | 2026-08-15T15:20:07 |
| `admin` | `051178` | `77.239.124.237` | 2026-08-15T15:20:13 |
| `root` | `rootroot` | `77.239.124.237` | 2026-08-15T15:20:19 |
| `jakob` | `jakob` | `77.239.124.237` | 2026-08-15T15:20:25 |
| `usuario` | `usuario` | `77.239.124.237` | 2026-08-15T15:20:31 |
| `admin` | `111111` | `77.239.124.237` | 2026-08-15T15:20:38 |
| `root` | `password` | `77.239.124.237` | 2026-08-15T15:20:44 |
| `system` | `system` | `77.239.124.237` | 2026-08-15T15:20:51 |
| `root` | `1qaz@wsx` | `77.239.124.237` | 2026-08-15T15:20:57 |
| `postgres` | `1` | `77.239.124.237` | 2026-08-15T15:21:04 |
| `term2` | `term2` | `77.239.124.237` | 2026-08-15T15:21:10 |
| `test` | `1` | `77.239.124.237` | 2026-08-15T15:21:15 |
| `debian` | `1q2w3e4r` | `188.219.104.210` | 2026-08-15T15:21:19 |
| `openclaw` | `user` | `77.239.124.237` | 2026-08-15T15:21:22 |
| `core` | `P@ssw0rd` | `77.239.124.237` | 2026-08-15T15:21:28 |
| `debian` | `1q2w3e4r` | `180.76.52.146` | 2026-08-15T15:21:32 |
| `root` | `passw0rd` | `77.239.124.237` | 2026-08-15T15:21:34 |
| `opc` | `opc` | `77.239.124.237` | 2026-08-15T15:21:41 |
| `runner` | `123` | `77.239.124.237` | 2026-08-15T15:21:47 |
| `admin` | `1qaz@WSX` | `77.239.124.237` | 2026-08-15T15:21:53 |
| `root` | `Root@123` | `77.239.124.237` | 2026-08-15T15:22:00 |
| `postgres` | `123456` | `77.239.124.237` | 2026-08-15T15:22:11 |
| `deploy` | `qwerty` | `77.239.124.237` | 2026-08-15T15:22:19 |
| `ubuntu` | `qwe123456` | `77.239.124.237` | 2026-08-15T15:22:27 |
| `claude` | `12345678` | `77.239.124.237` | 2026-08-15T15:22:34 |
| `user1` | `123456` | `77.239.124.237` | 2026-08-15T15:22:41 |
| `root` | `abcd1234` | `77.239.124.237` | 2026-08-15T15:22:47 |
| `user` | `qwe123456` | `77.239.124.237` | 2026-08-15T15:22:55 |
| `bob` | `bob` | `77.239.124.237` | 2026-08-15T15:23:02 |
| `ftp` | `ftp` | `77.239.124.237` | 2026-08-15T15:23:09 |
| `deploy` | `dev` | `77.239.124.237` | 2026-08-15T15:23:16 |
| `coder` | `123456` | `77.239.124.237` | 2026-08-15T15:23:22 |
| `newuser` | `newuser` | `77.239.124.237` | 2026-08-15T15:23:29 |
| `support` | `Passw0rd` | `77.239.124.237` | 2026-08-15T15:23:37 |
| `root` | `Huawei123` | `77.239.124.237` | 2026-08-15T15:23:45 |
| `root` | `Yun@wocloud.szkj` | `77.239.124.237` | 2026-08-15T15:23:53 |
| `student` | `redhat` | `77.239.124.237` | 2026-08-15T15:24:01 |
| `ubuntu` | `admin@123` | `77.239.124.237` | 2026-08-15T15:24:10 |
| `root` | `123.com` | `217.165.22.192` | 2026-08-15T15:24:14 |
| `tomcat` | `tomcat` | `77.239.124.237` | 2026-08-15T15:24:18 |
| `pi` | `pi` | `77.239.124.237` | 2026-08-15T15:24:26 |
| `ec2-user` | `123456` | `77.239.124.237` | 2026-08-15T15:24:34 |
| `root1` | `gg` | `77.239.124.237` | 2026-08-15T15:24:43 |
| `ark` | `ark` | `77.239.124.237` | 2026-08-15T15:24:52 |
| `root` | `Aa123321` | `77.239.124.237` | 2026-08-15T15:25:00 |
| `root` | `root111` | `10.0.0.73` | 2026-08-15T15:25:09 |
| `dev` | `abc123` | `77.239.124.237` | 2026-08-15T15:25:09 |
| `user` | `12345678` | `77.239.124.237` | 2026-08-15T15:25:18 |
| `monitor` | `monitor` | `77.239.124.237` | 2026-08-15T15:25:26 |
| `ubuntu` | `ubuntu` | `77.239.124.237` | 2026-08-15T15:25:34 |
| `root` | `aB123456` | `77.239.124.237` | 2026-08-15T15:25:42 |
| `root` | `Aa123123` | `77.239.124.237` | 2026-08-15T15:25:51 |
| `steam` | `steam` | `77.239.124.237` | 2026-08-15T15:25:59 |
| `claude` | `123` | `77.239.124.237` | 2026-08-15T15:26:08 |
| `root` | `123@@@` | `77.239.124.237` | 2026-08-15T15:26:16 |
| `www` | `12345678` | `77.239.124.237` | 2026-08-15T15:26:25 |
| `root1` | `1` | `77.239.124.237` | 2026-08-15T15:26:34 |
| `root` | `zaq12wsx` | `77.239.124.237` | 2026-08-15T15:26:41 |
| `root` | `kali` | `77.239.124.237` | 2026-08-15T15:26:50 |
| `root` | `123qwe!@` | `77.239.124.237` | 2026-08-15T15:26:58 |
| `ai` | `toor` | `77.239.124.237` | 2026-08-15T15:27:06 |
| `admin` | `111` | `77.239.124.237` | 2026-08-15T15:27:15 |
| `root` | `qwe123` | `77.239.124.237` | 2026-08-15T15:27:23 |
| `devops` | `123456789` | `77.239.124.237` | 2026-08-15T15:27:31 |
| `pi` | `123456` | `77.239.124.237` | 2026-08-15T15:27:39 |
| `john` | `john` | `77.239.124.237` | 2026-08-15T15:27:48 |
| `root` | `Admin123` | `77.239.124.237` | 2026-08-15T15:27:56 |
| `ts3` | `ts3` | `77.239.124.237` | 2026-08-15T15:28:05 |
| `home` | `root` | `77.239.124.237` | 2026-08-15T15:28:13 |
| `root1` | `root1` | `77.239.124.237` | 2026-08-15T15:28:22 |
| `sam` | `1234567890` | `77.239.124.237` | 2026-08-15T15:28:30 |
| `mcserver` | `mcserver` | `77.239.124.237` | 2026-08-15T15:28:39 |
| `vagrant` | `vagrant` | `77.239.124.237` | 2026-08-15T15:28:47 |
| `dmdba` | `dmdba` | `77.239.124.237` | 2026-08-15T15:28:55 |
| `user2` | `1` | `77.239.124.237` | 2026-08-15T15:29:04 |
| `root` | `CatCult2025!` | `77.239.124.237` | 2026-08-15T15:29:12 |
| `fivem` | `password` | `77.239.124.237` | 2026-08-15T15:29:20 |
| `www` | `user` | `77.239.124.237` | 2026-08-15T15:29:29 |
| `sam` | `abc123` | `77.239.124.237` | 2026-08-15T15:29:38 |
| `user` | `rootroot` | `77.239.124.237` | 2026-08-15T15:29:46 |
| `system` | `12345` | `77.239.124.237` | 2026-08-15T15:29:54 |
| `admin2` | `1234` | `77.239.124.237` | 2026-08-15T15:30:02 |
| `toto` | `toto` | `77.239.124.237` | 2026-08-15T15:30:10 |
| `btc` | `btc` | `77.239.124.237` | 2026-08-15T15:30:18 |
| `root` | `P@ssw0rd` | `77.239.124.237` | 2026-08-15T15:30:27 |
| `steam` | `1` | `77.239.124.237` | 2026-08-15T15:30:35 |
| `root` | `Aa111111.` | `77.239.124.237` | 2026-08-15T15:30:44 |
| `git` | `123` | `77.239.124.237` | 2026-08-15T15:30:53 |
| `guest` | `111111` | `77.239.124.237` | 2026-08-15T15:31:01 |
| `jellyfin` | `root` | `77.239.124.237` | 2026-08-15T15:31:09 |
| `labuser` | `labuser` | `77.239.124.237` | 2026-08-15T15:31:17 |
| `packer` | `packer` | `77.239.124.237` | 2026-08-15T15:31:26 |
| `git` | `dev` | `77.239.124.237` | 2026-08-15T15:31:35 |
| `claude` | `1234` | `77.239.124.237` | 2026-08-15T15:31:44 |
| `root` | `P@ssword1` | `77.239.124.237` | 2026-08-15T15:31:53 |
| `webmaster` | `webmaster` | `77.239.124.237` | 2026-08-15T15:32:01 |
| `omm` | `omm` | `77.239.124.237` | 2026-08-15T15:32:09 |
| `pi` | `raspberry` | `77.239.124.237` | 2026-08-15T15:32:18 |
| `samuel` | `a` | `77.239.124.237` | 2026-08-15T15:32:26 |
| `bot` | `abc123` | `77.239.124.237` | 2026-08-15T15:32:34 |
| `user3` | `1` | `77.239.124.237` | 2026-08-15T15:32:43 |
| `user` | `user123456` | `77.239.124.237` | 2026-08-15T15:32:52 |
| `rancher` | `rancher123` | `77.239.124.237` | 2026-08-15T15:32:59 |
| `fastuser` | `fastuser` | `77.239.124.237` | 2026-08-15T15:33:07 |
| `root` | `root@123` | `45.142.193.164` | 2026-08-15T15:35:21 |
| `test` | `qwerty123` | `156.238.86.2` | 2026-08-15T15:35:42 |
| `test` | `qwerty123` | `111.70.32.51` | 2026-08-15T15:35:56 |
| `new` | `new` | `45.154.244.193` | 2026-08-15T15:37:11 |
| `config` | `6666` | `10.0.0.73` | 2026-08-15T15:37:34 |
| `config` | `6666` | `210.177.143.61` | 2026-08-15T15:39:12 |
| `config` | `6666` | `192.34.128.202` | 2026-08-15T15:39:20 |
| `debian` | `webmaster` | `178.178.222.55` | 2026-08-15T15:41:00 |
| `debian` | `webmaster` | `117.248.201.39` | 2026-08-15T15:41:15 |
| `admin` | `Admin@1234` | `5.48.46.95` | 2026-08-15T15:41:26 |
| `root` | `1234.com` | `217.165.22.192` | 2026-08-15T15:43:24 |
| `root` | `root111` | `122.170.99.195` | 2026-08-15T15:43:52 |
| `root` | `root111` | `49.124.153.61` | 2026-08-15T15:44:02 |
| `unknown` | `unknown1234567` | `49.124.151.4` | 2026-08-15T15:46:31 |
| `unknown` | `unknown1234567` | `223.197.226.51` | 2026-08-15T15:46:44 |
| `root` | `Abcd1234` | `10.0.0.73` | 2026-08-15T15:50:53 |
| `debian` | `webmaster` | `10.0.0.73` | 2026-08-15T15:52:39 |
| `config` | `6666` | `94.228.240.2` | 2026-08-15T15:55:28 |
| `config` | `6666` | `165.227.129.203` | 2026-08-15T15:55:34 |
| `support` | `support` | `176.53.159.196` | 2026-08-15T16:06:01 |
| `debian` | `webmaster` | `223.210.27.53` | 2026-08-15T16:10:03 |
| `centos` | `qwerty` | `10.0.0.73` | 2026-08-15T16:11:48 |
| `root` | `Admin123@` | `45.142.193.164` | 2026-08-15T16:14:00 |
| `config` | `P@ssw0rd` | `85.105.2.51` | 2026-08-15T16:14:58 |
| `config` | `P@ssw0rd` | `182.151.45.136` | 2026-08-15T16:15:07 |
| `blank` | `toor` | `196.188.93.169` | 2026-08-15T16:17:36 |
| `blank` | `toor` | `61.77.220.62` | 2026-08-15T16:17:56 |
| `blank` | `toor` | `103.251.143.14` | 2026-08-15T16:18:05 |
| `new` | `new` | `10.0.0.73` | 2026-08-15T16:18:12 |
| `username` | `password` | `10.0.0.73` | 2026-08-15T16:18:17 |
| `root` | `ABCabc123` | `217.165.22.192` | 2026-08-15T16:21:40 |
| `config` | `P@ssw0rd` | `10.0.0.73` | 2026-08-15T16:26:45 |
| `centos` | `qwerty` | `211.238.237.254` | 2026-08-15T16:29:41 |
| `support` | `support` | `10.0.0.73` | 2026-08-15T16:30:51 |
| `root` | `admin` | `31.77.227.120` | 2026-08-15T16:31:28 |
| `root` | `12345678` | `31.77.227.120` | 2026-08-15T16:31:53 |
| `root` | `admin123` | `31.77.227.120` | 2026-08-15T16:32:15 |
| `root` | `1234567` | `31.77.227.120` | 2026-08-15T16:32:36 |
| `root` | `123123` | `31.77.227.120` | 2026-08-15T16:32:50 |
| `user` | `password321` | `10.0.0.73` | 2026-08-15T16:33:20 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-15T16:35:08 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-15T16:35:08 |
| `root` | `redhat123` | `217.165.22.192` | 2026-08-15T16:40:48 |
| `config` | `P@ssw0rd` | `111.39.167.59` | 2026-08-15T16:44:04 |
| `supervisor` | `12345` | `50.188.204.213` | 2026-08-15T16:49:12 |
| `user` | `password321` | `211.238.237.254` | 2026-08-15T16:51:42 |
| `user` | `password321` | `182.79.218.101` | 2026-08-15T16:51:53 |
| `user` | `password321` | `220.93.167.144` | 2026-08-15T16:51:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **6094** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 298 |
| OpenSSH | 41 |
| libssh | 10 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 280 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 39 | 37 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |
| `16443846184e...` | Generic scanner | 6 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 280 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 39 | 37 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 4 | — |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `9052c4ab4164...` | OpenSSH | 2 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **97** |
| Unique ASNs | **80** |
| High-Risk ASNs | **61** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (336)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-719820356e5b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:55 |
| **Last Seen** | 2026-08-15 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:55:10` | `cowrie.session.connect` |
| `2026-08-15 14:55:10` | `cowrie.client.version` |
| `2026-08-15 14:55:10` | `cowrie.client.kex` |
| `2026-08-15 14:55:10` | `cowrie.login.success` |
| `2026-08-15 14:55:11` | `cowrie.session.params` |
| `2026-08-15 14:55:11` | `cowrie.command.input` |
| `2026-08-15 14:55:11` | `cowrie.log.closed` |
| `2026-08-15 14:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d6abe3238fa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:55 |
| **Last Seen** | 2026-08-15 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:55:18` | `cowrie.session.connect` |
| `2026-08-15 14:55:18` | `cowrie.client.version` |
| `2026-08-15 14:55:18` | `cowrie.client.kex` |
| `2026-08-15 14:55:19` | `cowrie.login.success` |
| `2026-08-15 14:55:20` | `cowrie.session.params` |
| `2026-08-15 14:55:20` | `cowrie.command.input` |
| `2026-08-15 14:55:20` | `cowrie.log.closed` |
| `2026-08-15 14:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f8db9a20bd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:55 |
| **Last Seen** | 2026-08-15 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:55:26` | `cowrie.session.connect` |
| `2026-08-15 14:55:26` | `cowrie.client.version` |
| `2026-08-15 14:55:26` | `cowrie.client.kex` |
| `2026-08-15 14:55:27` | `cowrie.login.success` |
| `2026-08-15 14:55:28` | `cowrie.session.params` |
| `2026-08-15 14:55:28` | `cowrie.command.input` |
| `2026-08-15 14:55:28` | `cowrie.log.closed` |
| `2026-08-15 14:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f59dbb4deb6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:55 |
| **Last Seen** | 2026-08-15 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:55:35` | `cowrie.session.connect` |
| `2026-08-15 14:55:35` | `cowrie.client.version` |
| `2026-08-15 14:55:35` | `cowrie.client.kex` |
| `2026-08-15 14:55:35` | `cowrie.login.success` |
| `2026-08-15 14:55:36` | `cowrie.session.params` |
| `2026-08-15 14:55:36` | `cowrie.command.input` |
| `2026-08-15 14:55:37` | `cowrie.log.closed` |
| `2026-08-15 14:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2428639791d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:55 |
| **Last Seen** | 2026-08-15 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:55:44` | `cowrie.session.connect` |
| `2026-08-15 14:55:44` | `cowrie.client.version` |
| `2026-08-15 14:55:44` | `cowrie.client.kex` |
| `2026-08-15 14:55:44` | `cowrie.login.success` |
| `2026-08-15 14:55:45` | `cowrie.session.params` |
| `2026-08-15 14:55:45` | `cowrie.command.input` |
| `2026-08-15 14:55:45` | `cowrie.log.closed` |
| `2026-08-15 14:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5c6c25601f0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:55 |
| **Last Seen** | 2026-08-15 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:55:52` | `cowrie.session.connect` |
| `2026-08-15 14:55:52` | `cowrie.client.version` |
| `2026-08-15 14:55:52` | `cowrie.client.kex` |
| `2026-08-15 14:55:53` | `cowrie.login.success` |
| `2026-08-15 14:55:53` | `cowrie.session.params` |
| `2026-08-15 14:55:53` | `cowrie.command.input` |
| `2026-08-15 14:55:53` | `cowrie.log.closed` |
| `2026-08-15 14:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2760d71599ea

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:56 |
| **Last Seen** | 2026-08-15 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:56:00` | `cowrie.session.connect` |
| `2026-08-15 14:56:00` | `cowrie.client.version` |
| `2026-08-15 14:56:00` | `cowrie.client.kex` |
| `2026-08-15 14:56:01` | `cowrie.login.success` |
| `2026-08-15 14:56:02` | `cowrie.session.params` |
| `2026-08-15 14:56:02` | `cowrie.command.input` |
| `2026-08-15 14:56:02` | `cowrie.log.closed` |
| `2026-08-15 14:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6befdc9514e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:56 |
| **Last Seen** | 2026-08-15 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:56:08` | `cowrie.session.connect` |
| `2026-08-15 14:56:08` | `cowrie.client.version` |
| `2026-08-15 14:56:08` | `cowrie.client.kex` |
| `2026-08-15 14:56:08` | `cowrie.login.success` |
| `2026-08-15 14:56:09` | `cowrie.session.params` |
| `2026-08-15 14:56:09` | `cowrie.command.input` |
| `2026-08-15 14:56:09` | `cowrie.log.closed` |
| `2026-08-15 14:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-968e9a2b14ff

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:56 |
| **Last Seen** | 2026-08-15 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:56:15` | `cowrie.session.connect` |
| `2026-08-15 14:56:15` | `cowrie.client.version` |
| `2026-08-15 14:56:15` | `cowrie.client.kex` |
| `2026-08-15 14:56:16` | `cowrie.login.success` |
| `2026-08-15 14:56:16` | `cowrie.session.params` |
| `2026-08-15 14:56:16` | `cowrie.command.input` |
| `2026-08-15 14:56:17` | `cowrie.log.closed` |
| `2026-08-15 14:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f301c3d4920

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:56 |
| **Last Seen** | 2026-08-15 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:56:24` | `cowrie.session.connect` |
| `2026-08-15 14:56:24` | `cowrie.client.version` |
| `2026-08-15 14:56:24` | `cowrie.client.kex` |
| `2026-08-15 14:56:24` | `cowrie.login.success` |
| `2026-08-15 14:56:25` | `cowrie.session.params` |
| `2026-08-15 14:56:25` | `cowrie.command.input` |
| `2026-08-15 14:56:25` | `cowrie.log.closed` |
| `2026-08-15 14:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869696663a58

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:56 |
| **Last Seen** | 2026-08-15 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:56:32` | `cowrie.session.connect` |
| `2026-08-15 14:56:32` | `cowrie.client.version` |
| `2026-08-15 14:56:33` | `cowrie.client.kex` |
| `2026-08-15 14:56:33` | `cowrie.login.success` |
| `2026-08-15 14:56:34` | `cowrie.session.params` |
| `2026-08-15 14:56:34` | `cowrie.command.input` |
| `2026-08-15 14:56:34` | `cowrie.log.closed` |
| `2026-08-15 14:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df7a0b8a81d3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:56 |
| **Last Seen** | 2026-08-15 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:56:40` | `cowrie.session.connect` |
| `2026-08-15 14:56:40` | `cowrie.client.version` |
| `2026-08-15 14:56:40` | `cowrie.client.kex` |
| `2026-08-15 14:56:40` | `cowrie.login.success` |
| `2026-08-15 14:56:41` | `cowrie.session.params` |
| `2026-08-15 14:56:41` | `cowrie.command.input` |
| `2026-08-15 14:56:41` | `cowrie.log.closed` |
| `2026-08-15 14:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a90fc0b173

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:56 |
| **Last Seen** | 2026-08-15 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:56:48` | `cowrie.session.connect` |
| `2026-08-15 14:56:48` | `cowrie.client.version` |
| `2026-08-15 14:56:48` | `cowrie.client.kex` |
| `2026-08-15 14:56:48` | `cowrie.login.success` |
| `2026-08-15 14:56:49` | `cowrie.session.params` |
| `2026-08-15 14:56:49` | `cowrie.command.input` |
| `2026-08-15 14:56:49` | `cowrie.log.closed` |
| `2026-08-15 14:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26ef48e0a182

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:56 |
| **Last Seen** | 2026-08-15 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:56:56` | `cowrie.session.connect` |
| `2026-08-15 14:56:56` | `cowrie.client.version` |
| `2026-08-15 14:56:56` | `cowrie.client.kex` |
| `2026-08-15 14:56:57` | `cowrie.login.success` |
| `2026-08-15 14:56:57` | `cowrie.session.params` |
| `2026-08-15 14:56:57` | `cowrie.command.input` |
| `2026-08-15 14:56:58` | `cowrie.log.closed` |
| `2026-08-15 14:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c5aad1f921

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:57 |
| **Last Seen** | 2026-08-15 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:57:05` | `cowrie.session.connect` |
| `2026-08-15 14:57:05` | `cowrie.client.version` |
| `2026-08-15 14:57:05` | `cowrie.client.kex` |
| `2026-08-15 14:57:05` | `cowrie.login.success` |
| `2026-08-15 14:57:06` | `cowrie.session.params` |
| `2026-08-15 14:57:06` | `cowrie.command.input` |
| `2026-08-15 14:57:06` | `cowrie.log.closed` |
| `2026-08-15 14:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde807bc47d6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:57 |
| **Last Seen** | 2026-08-15 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:57:13` | `cowrie.session.connect` |
| `2026-08-15 14:57:13` | `cowrie.client.version` |
| `2026-08-15 14:57:13` | `cowrie.client.kex` |
| `2026-08-15 14:57:13` | `cowrie.login.success` |
| `2026-08-15 14:57:14` | `cowrie.session.params` |
| `2026-08-15 14:57:14` | `cowrie.command.input` |
| `2026-08-15 14:57:14` | `cowrie.log.closed` |
| `2026-08-15 14:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271cead5ba5c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:57 |
| **Last Seen** | 2026-08-15 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:57:21` | `cowrie.session.connect` |
| `2026-08-15 14:57:21` | `cowrie.client.version` |
| `2026-08-15 14:57:21` | `cowrie.client.kex` |
| `2026-08-15 14:57:22` | `cowrie.login.success` |
| `2026-08-15 14:57:22` | `cowrie.session.params` |
| `2026-08-15 14:57:22` | `cowrie.command.input` |
| `2026-08-15 14:57:22` | `cowrie.log.closed` |
| `2026-08-15 14:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc02cc5b994

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:57 |
| **Last Seen** | 2026-08-15 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:57:29` | `cowrie.session.connect` |
| `2026-08-15 14:57:29` | `cowrie.client.version` |
| `2026-08-15 14:57:29` | `cowrie.client.kex` |
| `2026-08-15 14:57:30` | `cowrie.login.success` |
| `2026-08-15 14:57:30` | `cowrie.session.params` |
| `2026-08-15 14:57:30` | `cowrie.command.input` |
| `2026-08-15 14:57:31` | `cowrie.log.closed` |
| `2026-08-15 14:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc2d9e7e1abf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:57 |
| **Last Seen** | 2026-08-15 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:57:38` | `cowrie.session.connect` |
| `2026-08-15 14:57:38` | `cowrie.client.version` |
| `2026-08-15 14:57:38` | `cowrie.client.kex` |
| `2026-08-15 14:57:38` | `cowrie.login.success` |
| `2026-08-15 14:57:39` | `cowrie.session.params` |
| `2026-08-15 14:57:39` | `cowrie.command.input` |
| `2026-08-15 14:57:39` | `cowrie.log.closed` |
| `2026-08-15 14:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92783505fc2b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:57 |
| **Last Seen** | 2026-08-15 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:57:46` | `cowrie.session.connect` |
| `2026-08-15 14:57:46` | `cowrie.client.version` |
| `2026-08-15 14:57:46` | `cowrie.client.kex` |
| `2026-08-15 14:57:47` | `cowrie.login.success` |
| `2026-08-15 14:57:48` | `cowrie.session.params` |
| `2026-08-15 14:57:48` | `cowrie.command.input` |
| `2026-08-15 14:57:48` | `cowrie.log.closed` |
| `2026-08-15 14:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ee015a5758d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:57 |
| **Last Seen** | 2026-08-15 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:57:55` | `cowrie.session.connect` |
| `2026-08-15 14:57:55` | `cowrie.client.version` |
| `2026-08-15 14:57:55` | `cowrie.client.kex` |
| `2026-08-15 14:57:56` | `cowrie.login.success` |
| `2026-08-15 14:57:57` | `cowrie.session.params` |
| `2026-08-15 14:57:57` | `cowrie.command.input` |
| `2026-08-15 14:57:57` | `cowrie.log.closed` |
| `2026-08-15 14:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d8d34245aaf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:58 |
| **Last Seen** | 2026-08-15 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:58:04` | `cowrie.session.connect` |
| `2026-08-15 14:58:04` | `cowrie.client.version` |
| `2026-08-15 14:58:04` | `cowrie.client.kex` |
| `2026-08-15 14:58:04` | `cowrie.login.success` |
| `2026-08-15 14:58:05` | `cowrie.session.params` |
| `2026-08-15 14:58:05` | `cowrie.command.input` |
| `2026-08-15 14:58:05` | `cowrie.log.closed` |
| `2026-08-15 14:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a342689e502

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:58 |
| **Last Seen** | 2026-08-15 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:58:13` | `cowrie.session.connect` |
| `2026-08-15 14:58:13` | `cowrie.client.version` |
| `2026-08-15 14:58:13` | `cowrie.client.kex` |
| `2026-08-15 14:58:13` | `cowrie.login.success` |
| `2026-08-15 14:58:14` | `cowrie.session.params` |
| `2026-08-15 14:58:14` | `cowrie.command.input` |
| `2026-08-15 14:58:14` | `cowrie.log.closed` |
| `2026-08-15 14:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2523ee3617b8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:58 |
| **Last Seen** | 2026-08-15 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:58:22` | `cowrie.session.connect` |
| `2026-08-15 14:58:22` | `cowrie.client.version` |
| `2026-08-15 14:58:22` | `cowrie.client.kex` |
| `2026-08-15 14:58:22` | `cowrie.login.success` |
| `2026-08-15 14:58:23` | `cowrie.session.params` |
| `2026-08-15 14:58:23` | `cowrie.command.input` |
| `2026-08-15 14:58:23` | `cowrie.log.closed` |
| `2026-08-15 14:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5323e5d7a4f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:58 |
| **Last Seen** | 2026-08-15 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:58:30` | `cowrie.session.connect` |
| `2026-08-15 14:58:30` | `cowrie.client.version` |
| `2026-08-15 14:58:30` | `cowrie.client.kex` |
| `2026-08-15 14:58:31` | `cowrie.login.success` |
| `2026-08-15 14:58:31` | `cowrie.session.params` |
| `2026-08-15 14:58:31` | `cowrie.command.input` |
| `2026-08-15 14:58:31` | `cowrie.log.closed` |
| `2026-08-15 14:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4944531f0683

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:58 |
| **Last Seen** | 2026-08-15 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:58:38` | `cowrie.session.connect` |
| `2026-08-15 14:58:38` | `cowrie.client.version` |
| `2026-08-15 14:58:38` | `cowrie.client.kex` |
| `2026-08-15 14:58:39` | `cowrie.login.success` |
| `2026-08-15 14:58:39` | `cowrie.session.params` |
| `2026-08-15 14:58:39` | `cowrie.command.input` |
| `2026-08-15 14:58:40` | `cowrie.log.closed` |
| `2026-08-15 14:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae0f170c4ae

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:58 |
| **Last Seen** | 2026-08-15 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:58:46` | `cowrie.session.connect` |
| `2026-08-15 14:58:46` | `cowrie.client.version` |
| `2026-08-15 14:58:46` | `cowrie.client.kex` |
| `2026-08-15 14:58:47` | `cowrie.login.success` |
| `2026-08-15 14:58:48` | `cowrie.session.params` |
| `2026-08-15 14:58:48` | `cowrie.command.input` |
| `2026-08-15 14:58:48` | `cowrie.log.closed` |
| `2026-08-15 14:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c191ca7a12da

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:58 |
| **Last Seen** | 2026-08-15 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:58:54` | `cowrie.session.connect` |
| `2026-08-15 14:58:54` | `cowrie.client.version` |
| `2026-08-15 14:58:54` | `cowrie.client.kex` |
| `2026-08-15 14:58:55` | `cowrie.login.success` |
| `2026-08-15 14:58:55` | `cowrie.session.params` |
| `2026-08-15 14:58:55` | `cowrie.command.input` |
| `2026-08-15 14:58:56` | `cowrie.log.closed` |
| `2026-08-15 14:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f3424bcb394

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:59 |
| **Last Seen** | 2026-08-15 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:59:03` | `cowrie.session.connect` |
| `2026-08-15 14:59:03` | `cowrie.client.version` |
| `2026-08-15 14:59:03` | `cowrie.client.kex` |
| `2026-08-15 14:59:03` | `cowrie.login.success` |
| `2026-08-15 14:59:04` | `cowrie.session.params` |
| `2026-08-15 14:59:04` | `cowrie.command.input` |
| `2026-08-15 14:59:05` | `cowrie.log.closed` |
| `2026-08-15 14:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7dbe21963ee

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:59 |
| **Last Seen** | 2026-08-15 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:59:11` | `cowrie.session.connect` |
| `2026-08-15 14:59:11` | `cowrie.client.version` |
| `2026-08-15 14:59:12` | `cowrie.client.kex` |
| `2026-08-15 14:59:12` | `cowrie.login.success` |
| `2026-08-15 14:59:13` | `cowrie.session.params` |
| `2026-08-15 14:59:13` | `cowrie.command.input` |
| `2026-08-15 14:59:13` | `cowrie.log.closed` |
| `2026-08-15 14:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd1c0439d047

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:59 |
| **Last Seen** | 2026-08-15 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:59:20` | `cowrie.session.connect` |
| `2026-08-15 14:59:20` | `cowrie.client.version` |
| `2026-08-15 14:59:20` | `cowrie.client.kex` |
| `2026-08-15 14:59:21` | `cowrie.login.success` |
| `2026-08-15 14:59:22` | `cowrie.session.params` |
| `2026-08-15 14:59:22` | `cowrie.command.input` |
| `2026-08-15 14:59:22` | `cowrie.log.closed` |
| `2026-08-15 14:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-642be47f6f47

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:59 |
| **Last Seen** | 2026-08-15 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:59:29` | `cowrie.session.connect` |
| `2026-08-15 14:59:29` | `cowrie.client.version` |
| `2026-08-15 14:59:29` | `cowrie.client.kex` |
| `2026-08-15 14:59:29` | `cowrie.login.success` |
| `2026-08-15 14:59:30` | `cowrie.session.params` |
| `2026-08-15 14:59:30` | `cowrie.command.input` |
| `2026-08-15 14:59:30` | `cowrie.log.closed` |
| `2026-08-15 14:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622345be7fdb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:59 |
| **Last Seen** | 2026-08-15 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:59:37` | `cowrie.session.connect` |
| `2026-08-15 14:59:37` | `cowrie.client.version` |
| `2026-08-15 14:59:37` | `cowrie.client.kex` |
| `2026-08-15 14:59:38` | `cowrie.login.success` |
| `2026-08-15 14:59:39` | `cowrie.session.params` |
| `2026-08-15 14:59:39` | `cowrie.command.input` |
| `2026-08-15 14:59:39` | `cowrie.log.closed` |
| `2026-08-15 14:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f884186e3e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:59 |
| **Last Seen** | 2026-08-15 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:59:45` | `cowrie.session.connect` |
| `2026-08-15 14:59:45` | `cowrie.client.version` |
| `2026-08-15 14:59:45` | `cowrie.client.kex` |
| `2026-08-15 14:59:45` | `cowrie.login.success` |
| `2026-08-15 14:59:46` | `cowrie.session.params` |
| `2026-08-15 14:59:46` | `cowrie.command.input` |
| `2026-08-15 14:59:46` | `cowrie.log.closed` |
| `2026-08-15 14:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ce121c4384

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 14:59 |
| **Last Seen** | 2026-08-15 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 14:59:54` | `cowrie.session.connect` |
| `2026-08-15 14:59:54` | `cowrie.client.version` |
| `2026-08-15 14:59:54` | `cowrie.client.kex` |
| `2026-08-15 14:59:54` | `cowrie.login.success` |
| `2026-08-15 14:59:55` | `cowrie.session.params` |
| `2026-08-15 14:59:55` | `cowrie.command.input` |
| `2026-08-15 14:59:55` | `cowrie.log.closed` |
| `2026-08-15 14:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac4b822f6921

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:00 |
| **Last Seen** | 2026-08-15 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:00:02` | `cowrie.session.connect` |
| `2026-08-15 15:00:03` | `cowrie.client.version` |
| `2026-08-15 15:00:03` | `cowrie.client.kex` |
| `2026-08-15 15:00:03` | `cowrie.login.success` |
| `2026-08-15 15:00:04` | `cowrie.session.params` |
| `2026-08-15 15:00:04` | `cowrie.command.input` |
| `2026-08-15 15:00:04` | `cowrie.log.closed` |
| `2026-08-15 15:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc91050f3b61

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:00 |
| **Last Seen** | 2026-08-15 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:00:11` | `cowrie.session.connect` |
| `2026-08-15 15:00:11` | `cowrie.client.version` |
| `2026-08-15 15:00:11` | `cowrie.client.kex` |
| `2026-08-15 15:00:11` | `cowrie.login.success` |
| `2026-08-15 15:00:12` | `cowrie.session.params` |
| `2026-08-15 15:00:12` | `cowrie.command.input` |
| `2026-08-15 15:00:12` | `cowrie.log.closed` |
| `2026-08-15 15:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8981f6db7cd1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:00 |
| **Last Seen** | 2026-08-15 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:00:20` | `cowrie.session.connect` |
| `2026-08-15 15:00:20` | `cowrie.client.version` |
| `2026-08-15 15:00:20` | `cowrie.client.kex` |
| `2026-08-15 15:00:20` | `cowrie.login.success` |
| `2026-08-15 15:00:21` | `cowrie.session.params` |
| `2026-08-15 15:00:21` | `cowrie.command.input` |
| `2026-08-15 15:00:21` | `cowrie.log.closed` |
| `2026-08-15 15:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe6438b90a5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:00 |
| **Last Seen** | 2026-08-15 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:00:28` | `cowrie.session.connect` |
| `2026-08-15 15:00:28` | `cowrie.client.version` |
| `2026-08-15 15:00:28` | `cowrie.client.kex` |
| `2026-08-15 15:00:28` | `cowrie.login.success` |
| `2026-08-15 15:00:29` | `cowrie.session.params` |
| `2026-08-15 15:00:29` | `cowrie.command.input` |
| `2026-08-15 15:00:29` | `cowrie.log.closed` |
| `2026-08-15 15:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1377ab9e2fba

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:00 |
| **Last Seen** | 2026-08-15 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:00:36` | `cowrie.session.connect` |
| `2026-08-15 15:00:36` | `cowrie.client.version` |
| `2026-08-15 15:00:36` | `cowrie.client.kex` |
| `2026-08-15 15:00:36` | `cowrie.login.success` |
| `2026-08-15 15:00:37` | `cowrie.session.params` |
| `2026-08-15 15:00:37` | `cowrie.command.input` |
| `2026-08-15 15:00:37` | `cowrie.log.closed` |
| `2026-08-15 15:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5856681cc08a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:00 |
| **Last Seen** | 2026-08-15 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:00:44` | `cowrie.session.connect` |
| `2026-08-15 15:00:44` | `cowrie.client.version` |
| `2026-08-15 15:00:44` | `cowrie.client.kex` |
| `2026-08-15 15:00:45` | `cowrie.login.success` |
| `2026-08-15 15:00:45` | `cowrie.session.params` |
| `2026-08-15 15:00:45` | `cowrie.command.input` |
| `2026-08-15 15:00:45` | `cowrie.log.closed` |
| `2026-08-15 15:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75bde26ffa40

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:00 |
| **Last Seen** | 2026-08-15 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:00:53` | `cowrie.session.connect` |
| `2026-08-15 15:00:53` | `cowrie.client.version` |
| `2026-08-15 15:00:53` | `cowrie.client.kex` |
| `2026-08-15 15:00:53` | `cowrie.login.success` |
| `2026-08-15 15:00:54` | `cowrie.session.params` |
| `2026-08-15 15:00:54` | `cowrie.command.input` |
| `2026-08-15 15:00:54` | `cowrie.log.closed` |
| `2026-08-15 15:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-052b51d16b4f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:01 |
| **Last Seen** | 2026-08-15 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:01:02` | `cowrie.session.connect` |
| `2026-08-15 15:01:02` | `cowrie.client.version` |
| `2026-08-15 15:01:02` | `cowrie.client.kex` |
| `2026-08-15 15:01:02` | `cowrie.login.success` |
| `2026-08-15 15:01:03` | `cowrie.session.params` |
| `2026-08-15 15:01:03` | `cowrie.command.input` |
| `2026-08-15 15:01:03` | `cowrie.log.closed` |
| `2026-08-15 15:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5f391bec77

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:01 |
| **Last Seen** | 2026-08-15 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:01:10` | `cowrie.session.connect` |
| `2026-08-15 15:01:10` | `cowrie.client.version` |
| `2026-08-15 15:01:11` | `cowrie.client.kex` |
| `2026-08-15 15:01:11` | `cowrie.login.success` |
| `2026-08-15 15:01:12` | `cowrie.session.params` |
| `2026-08-15 15:01:12` | `cowrie.command.input` |
| `2026-08-15 15:01:12` | `cowrie.log.closed` |
| `2026-08-15 15:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25fb052d3063

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:01 |
| **Last Seen** | 2026-08-15 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:01:19` | `cowrie.session.connect` |
| `2026-08-15 15:01:19` | `cowrie.client.version` |
| `2026-08-15 15:01:19` | `cowrie.client.kex` |
| `2026-08-15 15:01:19` | `cowrie.login.success` |
| `2026-08-15 15:01:20` | `cowrie.session.params` |
| `2026-08-15 15:01:20` | `cowrie.command.input` |
| `2026-08-15 15:01:20` | `cowrie.log.closed` |
| `2026-08-15 15:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a29bf1ce224

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:01 |
| **Last Seen** | 2026-08-15 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:01:27` | `cowrie.session.connect` |
| `2026-08-15 15:01:27` | `cowrie.client.version` |
| `2026-08-15 15:01:27` | `cowrie.client.kex` |
| `2026-08-15 15:01:27` | `cowrie.login.success` |
| `2026-08-15 15:01:28` | `cowrie.session.params` |
| `2026-08-15 15:01:28` | `cowrie.command.input` |
| `2026-08-15 15:01:28` | `cowrie.log.closed` |
| `2026-08-15 15:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2455f9eead1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:01 |
| **Last Seen** | 2026-08-15 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:01:35` | `cowrie.session.connect` |
| `2026-08-15 15:01:35` | `cowrie.client.version` |
| `2026-08-15 15:01:35` | `cowrie.client.kex` |
| `2026-08-15 15:01:36` | `cowrie.login.success` |
| `2026-08-15 15:01:36` | `cowrie.session.params` |
| `2026-08-15 15:01:36` | `cowrie.command.input` |
| `2026-08-15 15:01:37` | `cowrie.log.closed` |
| `2026-08-15 15:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c33474561cad

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]51` |
| **First Seen** | 2026-08-15 15:01 |
| **Last Seen** | 2026-08-15 15:02 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:01:43` | `cowrie.session.connect` |
| `2026-08-15 15:01:48` | `cowrie.client.version` |
| `2026-08-15 15:01:48` | `cowrie.client.kex` |
| `2026-08-15 15:01:54` | `cowrie.login.success` |
| `2026-08-15 15:01:56` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]51` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b8e47211707

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:01 |
| **Last Seen** | 2026-08-15 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:01:44` | `cowrie.session.connect` |
| `2026-08-15 15:01:44` | `cowrie.client.version` |
| `2026-08-15 15:01:44` | `cowrie.client.kex` |
| `2026-08-15 15:01:44` | `cowrie.login.success` |
| `2026-08-15 15:01:45` | `cowrie.session.params` |
| `2026-08-15 15:01:45` | `cowrie.command.input` |
| `2026-08-15 15:01:45` | `cowrie.log.closed` |
| `2026-08-15 15:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd554e4bab44

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:01 |
| **Last Seen** | 2026-08-15 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:01:52` | `cowrie.session.connect` |
| `2026-08-15 15:01:52` | `cowrie.client.version` |
| `2026-08-15 15:01:52` | `cowrie.client.kex` |
| `2026-08-15 15:01:52` | `cowrie.login.success` |
| `2026-08-15 15:01:53` | `cowrie.session.params` |
| `2026-08-15 15:01:53` | `cowrie.command.input` |
| `2026-08-15 15:01:53` | `cowrie.log.closed` |
| `2026-08-15 15:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c21d628b18

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:02 |
| **Last Seen** | 2026-08-15 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:02:01` | `cowrie.session.connect` |
| `2026-08-15 15:02:01` | `cowrie.client.version` |
| `2026-08-15 15:02:01` | `cowrie.client.kex` |
| `2026-08-15 15:02:01` | `cowrie.login.success` |
| `2026-08-15 15:02:02` | `cowrie.session.params` |
| `2026-08-15 15:02:02` | `cowrie.command.input` |
| `2026-08-15 15:02:02` | `cowrie.log.closed` |
| `2026-08-15 15:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb97f2359faf

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-08-15 15:02 |
| **Last Seen** | 2026-08-15 15:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:02:02` | `cowrie.session.connect` |
| `2026-08-15 15:02:03` | `cowrie.client.version` |
| `2026-08-15 15:02:03` | `cowrie.client.kex` |
| `2026-08-15 15:02:04` | `cowrie.login.success` |
| `2026-08-15 15:02:05` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92954e278527

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:02 |
| **Last Seen** | 2026-08-15 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:02:08` | `cowrie.session.connect` |
| `2026-08-15 15:02:08` | `cowrie.client.version` |
| `2026-08-15 15:02:08` | `cowrie.client.kex` |
| `2026-08-15 15:02:09` | `cowrie.login.success` |
| `2026-08-15 15:02:10` | `cowrie.session.params` |
| `2026-08-15 15:02:10` | `cowrie.command.input` |
| `2026-08-15 15:02:10` | `cowrie.log.closed` |
| `2026-08-15 15:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-112e21576b40

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:02 |
| **Last Seen** | 2026-08-15 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:02:17` | `cowrie.session.connect` |
| `2026-08-15 15:02:17` | `cowrie.client.version` |
| `2026-08-15 15:02:17` | `cowrie.client.kex` |
| `2026-08-15 15:02:18` | `cowrie.login.success` |
| `2026-08-15 15:02:18` | `cowrie.session.params` |
| `2026-08-15 15:02:18` | `cowrie.command.input` |
| `2026-08-15 15:02:18` | `cowrie.log.closed` |
| `2026-08-15 15:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d07bf5799c93

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:02 |
| **Last Seen** | 2026-08-15 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:02:26` | `cowrie.session.connect` |
| `2026-08-15 15:02:26` | `cowrie.client.version` |
| `2026-08-15 15:02:26` | `cowrie.client.kex` |
| `2026-08-15 15:02:26` | `cowrie.login.success` |
| `2026-08-15 15:02:27` | `cowrie.session.params` |
| `2026-08-15 15:02:27` | `cowrie.command.input` |
| `2026-08-15 15:02:27` | `cowrie.log.closed` |
| `2026-08-15 15:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-706f7dd409b4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:02 |
| **Last Seen** | 2026-08-15 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:02:33` | `cowrie.session.connect` |
| `2026-08-15 15:02:33` | `cowrie.client.version` |
| `2026-08-15 15:02:33` | `cowrie.client.kex` |
| `2026-08-15 15:02:34` | `cowrie.login.success` |
| `2026-08-15 15:02:35` | `cowrie.session.params` |
| `2026-08-15 15:02:35` | `cowrie.command.input` |
| `2026-08-15 15:02:35` | `cowrie.log.closed` |
| `2026-08-15 15:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-633882074e4f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:02 |
| **Last Seen** | 2026-08-15 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:02:41` | `cowrie.session.connect` |
| `2026-08-15 15:02:41` | `cowrie.client.version` |
| `2026-08-15 15:02:41` | `cowrie.client.kex` |
| `2026-08-15 15:02:42` | `cowrie.login.success` |
| `2026-08-15 15:02:42` | `cowrie.session.params` |
| `2026-08-15 15:02:42` | `cowrie.command.input` |
| `2026-08-15 15:02:43` | `cowrie.log.closed` |
| `2026-08-15 15:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-634b33c0df57

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:02 |
| **Last Seen** | 2026-08-15 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:02:50` | `cowrie.session.connect` |
| `2026-08-15 15:02:50` | `cowrie.client.version` |
| `2026-08-15 15:02:50` | `cowrie.client.kex` |
| `2026-08-15 15:02:50` | `cowrie.login.success` |
| `2026-08-15 15:02:51` | `cowrie.session.params` |
| `2026-08-15 15:02:51` | `cowrie.command.input` |
| `2026-08-15 15:02:51` | `cowrie.log.closed` |
| `2026-08-15 15:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92107e110f5d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:02 |
| **Last Seen** | 2026-08-15 15:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:02:57` | `cowrie.session.connect` |
| `2026-08-15 15:02:58` | `cowrie.client.version` |
| `2026-08-15 15:02:58` | `cowrie.client.kex` |
| `2026-08-15 15:02:58` | `cowrie.login.success` |
| `2026-08-15 15:02:59` | `cowrie.session.params` |
| `2026-08-15 15:02:59` | `cowrie.command.input` |
| `2026-08-15 15:02:59` | `cowrie.log.closed` |
| `2026-08-15 15:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8436a143bc80

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:03 |
| **Last Seen** | 2026-08-15 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:03:05` | `cowrie.session.connect` |
| `2026-08-15 15:03:05` | `cowrie.client.version` |
| `2026-08-15 15:03:05` | `cowrie.client.kex` |
| `2026-08-15 15:03:06` | `cowrie.login.success` |
| `2026-08-15 15:03:07` | `cowrie.session.params` |
| `2026-08-15 15:03:07` | `cowrie.command.input` |
| `2026-08-15 15:03:07` | `cowrie.log.closed` |
| `2026-08-15 15:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576435f5a249

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:03 |
| **Last Seen** | 2026-08-15 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:03:14` | `cowrie.session.connect` |
| `2026-08-15 15:03:14` | `cowrie.client.version` |
| `2026-08-15 15:03:14` | `cowrie.client.kex` |
| `2026-08-15 15:03:15` | `cowrie.login.success` |
| `2026-08-15 15:03:16` | `cowrie.session.params` |
| `2026-08-15 15:03:16` | `cowrie.command.input` |
| `2026-08-15 15:03:16` | `cowrie.log.closed` |
| `2026-08-15 15:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5190a4f74b2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:03 |
| **Last Seen** | 2026-08-15 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:03:22` | `cowrie.session.connect` |
| `2026-08-15 15:03:22` | `cowrie.client.version` |
| `2026-08-15 15:03:22` | `cowrie.client.kex` |
| `2026-08-15 15:03:23` | `cowrie.login.success` |
| `2026-08-15 15:03:24` | `cowrie.session.params` |
| `2026-08-15 15:03:24` | `cowrie.command.input` |
| `2026-08-15 15:03:24` | `cowrie.log.closed` |
| `2026-08-15 15:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71fecf48f82

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:03 |
| **Last Seen** | 2026-08-15 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:03:31` | `cowrie.session.connect` |
| `2026-08-15 15:03:31` | `cowrie.client.version` |
| `2026-08-15 15:03:31` | `cowrie.client.kex` |
| `2026-08-15 15:03:31` | `cowrie.login.success` |
| `2026-08-15 15:03:32` | `cowrie.session.params` |
| `2026-08-15 15:03:32` | `cowrie.command.input` |
| `2026-08-15 15:03:32` | `cowrie.log.closed` |
| `2026-08-15 15:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a07955349cb5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:03 |
| **Last Seen** | 2026-08-15 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:03:39` | `cowrie.session.connect` |
| `2026-08-15 15:03:39` | `cowrie.client.version` |
| `2026-08-15 15:03:39` | `cowrie.client.kex` |
| `2026-08-15 15:03:40` | `cowrie.login.success` |
| `2026-08-15 15:03:41` | `cowrie.session.params` |
| `2026-08-15 15:03:41` | `cowrie.command.input` |
| `2026-08-15 15:03:41` | `cowrie.log.closed` |
| `2026-08-15 15:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-225e24aa57a8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:03 |
| **Last Seen** | 2026-08-15 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:03:48` | `cowrie.session.connect` |
| `2026-08-15 15:03:48` | `cowrie.client.version` |
| `2026-08-15 15:03:48` | `cowrie.client.kex` |
| `2026-08-15 15:03:48` | `cowrie.login.success` |
| `2026-08-15 15:03:49` | `cowrie.session.params` |
| `2026-08-15 15:03:49` | `cowrie.command.input` |
| `2026-08-15 15:03:49` | `cowrie.log.closed` |
| `2026-08-15 15:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aec367ee8e91

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:03 |
| **Last Seen** | 2026-08-15 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:03:57` | `cowrie.session.connect` |
| `2026-08-15 15:03:57` | `cowrie.client.version` |
| `2026-08-15 15:03:57` | `cowrie.client.kex` |
| `2026-08-15 15:03:57` | `cowrie.login.success` |
| `2026-08-15 15:03:58` | `cowrie.session.params` |
| `2026-08-15 15:03:58` | `cowrie.command.input` |
| `2026-08-15 15:03:58` | `cowrie.log.closed` |
| `2026-08-15 15:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e798a94283d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:04 |
| **Last Seen** | 2026-08-15 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:04:04` | `cowrie.session.connect` |
| `2026-08-15 15:04:04` | `cowrie.client.version` |
| `2026-08-15 15:04:04` | `cowrie.client.kex` |
| `2026-08-15 15:04:05` | `cowrie.login.success` |
| `2026-08-15 15:04:06` | `cowrie.session.params` |
| `2026-08-15 15:04:06` | `cowrie.command.input` |
| `2026-08-15 15:04:06` | `cowrie.log.closed` |
| `2026-08-15 15:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c45e055951aa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:04 |
| **Last Seen** | 2026-08-15 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:04:12` | `cowrie.session.connect` |
| `2026-08-15 15:04:12` | `cowrie.client.version` |
| `2026-08-15 15:04:12` | `cowrie.client.kex` |
| `2026-08-15 15:04:13` | `cowrie.login.success` |
| `2026-08-15 15:04:14` | `cowrie.session.params` |
| `2026-08-15 15:04:14` | `cowrie.command.input` |
| `2026-08-15 15:04:14` | `cowrie.log.closed` |
| `2026-08-15 15:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b274a48f5c3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:04 |
| **Last Seen** | 2026-08-15 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:04:21` | `cowrie.session.connect` |
| `2026-08-15 15:04:21` | `cowrie.client.version` |
| `2026-08-15 15:04:21` | `cowrie.client.kex` |
| `2026-08-15 15:04:22` | `cowrie.login.success` |
| `2026-08-15 15:04:23` | `cowrie.session.params` |
| `2026-08-15 15:04:23` | `cowrie.command.input` |
| `2026-08-15 15:04:23` | `cowrie.log.closed` |
| `2026-08-15 15:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6192cd68a739

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:04 |
| **Last Seen** | 2026-08-15 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:04:30` | `cowrie.session.connect` |
| `2026-08-15 15:04:30` | `cowrie.client.version` |
| `2026-08-15 15:04:30` | `cowrie.client.kex` |
| `2026-08-15 15:04:30` | `cowrie.login.success` |
| `2026-08-15 15:04:31` | `cowrie.session.params` |
| `2026-08-15 15:04:31` | `cowrie.command.input` |
| `2026-08-15 15:04:31` | `cowrie.log.closed` |
| `2026-08-15 15:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4cbe955b5a7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:04 |
| **Last Seen** | 2026-08-15 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:04:39` | `cowrie.session.connect` |
| `2026-08-15 15:04:39` | `cowrie.client.version` |
| `2026-08-15 15:04:39` | `cowrie.client.kex` |
| `2026-08-15 15:04:39` | `cowrie.login.success` |
| `2026-08-15 15:04:40` | `cowrie.session.params` |
| `2026-08-15 15:04:40` | `cowrie.command.input` |
| `2026-08-15 15:04:40` | `cowrie.log.closed` |
| `2026-08-15 15:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e63d722a171

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:04 |
| **Last Seen** | 2026-08-15 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:04:47` | `cowrie.session.connect` |
| `2026-08-15 15:04:47` | `cowrie.client.version` |
| `2026-08-15 15:04:47` | `cowrie.client.kex` |
| `2026-08-15 15:04:47` | `cowrie.login.success` |
| `2026-08-15 15:04:48` | `cowrie.session.params` |
| `2026-08-15 15:04:48` | `cowrie.command.input` |
| `2026-08-15 15:04:48` | `cowrie.log.closed` |
| `2026-08-15 15:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a822f4d8b65

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:04 |
| **Last Seen** | 2026-08-15 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:04:55` | `cowrie.session.connect` |
| `2026-08-15 15:04:55` | `cowrie.client.version` |
| `2026-08-15 15:04:55` | `cowrie.client.kex` |
| `2026-08-15 15:04:55` | `cowrie.login.success` |
| `2026-08-15 15:04:56` | `cowrie.session.params` |
| `2026-08-15 15:04:56` | `cowrie.command.input` |
| `2026-08-15 15:04:57` | `cowrie.log.closed` |
| `2026-08-15 15:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ff22538b33

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 15:05 |
| **Last Seen** | 2026-08-15 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:05:01` | `cowrie.session.connect` |
| `2026-08-15 15:05:01` | `cowrie.client.version` |
| `2026-08-15 15:05:01` | `cowrie.client.kex` |
| `2026-08-15 15:05:01` | `cowrie.login.success` |
| `2026-08-15 15:05:02` | `cowrie.session.params` |
| `2026-08-15 15:05:02` | `cowrie.command.input` |
| `2026-08-15 15:05:03` | `cowrie.log.closed` |
| `2026-08-15 15:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71ff329230ad

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:05 |
| **Last Seen** | 2026-08-15 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:05:03` | `cowrie.session.connect` |
| `2026-08-15 15:05:03` | `cowrie.client.version` |
| `2026-08-15 15:05:03` | `cowrie.client.kex` |
| `2026-08-15 15:05:04` | `cowrie.login.success` |
| `2026-08-15 15:05:05` | `cowrie.session.params` |
| `2026-08-15 15:05:05` | `cowrie.command.input` |
| `2026-08-15 15:05:05` | `cowrie.log.closed` |
| `2026-08-15 15:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b93f7ec91f89

| Field | Detail |
|---|---|
| **Source IP** | `124.239.169[.]52` |
| **First Seen** | 2026-08-15 15:05 |
| **Last Seen** | 2026-08-15 15:05 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:05:07` | `cowrie.session.connect` |
| `2026-08-15 15:05:09` | `cowrie.client.version` |
| `2026-08-15 15:05:09` | `cowrie.client.kex` |
| `2026-08-15 15:05:13` | `cowrie.login.success` |
| `2026-08-15 15:05:14` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.169[.]52` to AbuseIPDB if not already reported
- [ ] Block `124.239.169[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4539e5bb5ea4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:05 |
| **Last Seen** | 2026-08-15 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:05:11` | `cowrie.session.connect` |
| `2026-08-15 15:05:11` | `cowrie.client.version` |
| `2026-08-15 15:05:11` | `cowrie.client.kex` |
| `2026-08-15 15:05:12` | `cowrie.login.success` |
| `2026-08-15 15:05:12` | `cowrie.session.params` |
| `2026-08-15 15:05:12` | `cowrie.command.input` |
| `2026-08-15 15:05:13` | `cowrie.log.closed` |
| `2026-08-15 15:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a901d0993689

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:05 |
| **Last Seen** | 2026-08-15 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:05:20` | `cowrie.session.connect` |
| `2026-08-15 15:05:20` | `cowrie.client.version` |
| `2026-08-15 15:05:20` | `cowrie.client.kex` |
| `2026-08-15 15:05:20` | `cowrie.login.success` |
| `2026-08-15 15:05:21` | `cowrie.session.params` |
| `2026-08-15 15:05:21` | `cowrie.command.input` |
| `2026-08-15 15:05:22` | `cowrie.log.closed` |
| `2026-08-15 15:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b1763c4b337

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-08-15 15:05 |
| **Last Seen** | 2026-08-15 15:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:05:24` | `cowrie.session.connect` |
| `2026-08-15 15:05:25` | `cowrie.client.version` |
| `2026-08-15 15:05:25` | `cowrie.client.kex` |
| `2026-08-15 15:05:27` | `cowrie.login.success` |
| `2026-08-15 15:05:28` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52f141cc4252

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:05 |
| **Last Seen** | 2026-08-15 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:05:28` | `cowrie.session.connect` |
| `2026-08-15 15:05:28` | `cowrie.client.version` |
| `2026-08-15 15:05:28` | `cowrie.client.kex` |
| `2026-08-15 15:05:29` | `cowrie.login.success` |
| `2026-08-15 15:05:30` | `cowrie.session.params` |
| `2026-08-15 15:05:30` | `cowrie.command.input` |
| `2026-08-15 15:05:30` | `cowrie.log.closed` |
| `2026-08-15 15:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab16e54ca96

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:05 |
| **Last Seen** | 2026-08-15 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:05:37` | `cowrie.session.connect` |
| `2026-08-15 15:05:37` | `cowrie.client.version` |
| `2026-08-15 15:05:37` | `cowrie.client.kex` |
| `2026-08-15 15:05:37` | `cowrie.login.success` |
| `2026-08-15 15:05:38` | `cowrie.session.params` |
| `2026-08-15 15:05:38` | `cowrie.command.input` |
| `2026-08-15 15:05:38` | `cowrie.log.closed` |
| `2026-08-15 15:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f8ae3732e94

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:05 |
| **Last Seen** | 2026-08-15 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:05:45` | `cowrie.session.connect` |
| `2026-08-15 15:05:45` | `cowrie.client.version` |
| `2026-08-15 15:05:45` | `cowrie.client.kex` |
| `2026-08-15 15:05:45` | `cowrie.login.success` |
| `2026-08-15 15:05:46` | `cowrie.session.params` |
| `2026-08-15 15:05:46` | `cowrie.command.input` |
| `2026-08-15 15:05:46` | `cowrie.log.closed` |
| `2026-08-15 15:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7788974db05c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:05 |
| **Last Seen** | 2026-08-15 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:05:54` | `cowrie.session.connect` |
| `2026-08-15 15:05:54` | `cowrie.client.version` |
| `2026-08-15 15:05:54` | `cowrie.client.kex` |
| `2026-08-15 15:05:54` | `cowrie.login.success` |
| `2026-08-15 15:05:55` | `cowrie.session.params` |
| `2026-08-15 15:05:55` | `cowrie.command.input` |
| `2026-08-15 15:05:55` | `cowrie.log.closed` |
| `2026-08-15 15:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e9dc1383a99

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:06 |
| **Last Seen** | 2026-08-15 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:06:02` | `cowrie.session.connect` |
| `2026-08-15 15:06:02` | `cowrie.client.version` |
| `2026-08-15 15:06:02` | `cowrie.client.kex` |
| `2026-08-15 15:06:03` | `cowrie.login.success` |
| `2026-08-15 15:06:04` | `cowrie.session.params` |
| `2026-08-15 15:06:04` | `cowrie.command.input` |
| `2026-08-15 15:06:04` | `cowrie.log.closed` |
| `2026-08-15 15:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac3e9411fbd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:06 |
| **Last Seen** | 2026-08-15 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:06:10` | `cowrie.session.connect` |
| `2026-08-15 15:06:10` | `cowrie.client.version` |
| `2026-08-15 15:06:10` | `cowrie.client.kex` |
| `2026-08-15 15:06:11` | `cowrie.login.success` |
| `2026-08-15 15:06:12` | `cowrie.session.params` |
| `2026-08-15 15:06:12` | `cowrie.command.input` |
| `2026-08-15 15:06:12` | `cowrie.log.closed` |
| `2026-08-15 15:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6cc88b16c6e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:06 |
| **Last Seen** | 2026-08-15 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:06:19` | `cowrie.session.connect` |
| `2026-08-15 15:06:19` | `cowrie.client.version` |
| `2026-08-15 15:06:19` | `cowrie.client.kex` |
| `2026-08-15 15:06:19` | `cowrie.login.success` |
| `2026-08-15 15:06:20` | `cowrie.session.params` |
| `2026-08-15 15:06:20` | `cowrie.command.input` |
| `2026-08-15 15:06:20` | `cowrie.log.closed` |
| `2026-08-15 15:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-326362adc47e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:06 |
| **Last Seen** | 2026-08-15 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:06:27` | `cowrie.session.connect` |
| `2026-08-15 15:06:27` | `cowrie.client.version` |
| `2026-08-15 15:06:27` | `cowrie.client.kex` |
| `2026-08-15 15:06:27` | `cowrie.login.success` |
| `2026-08-15 15:06:28` | `cowrie.session.params` |
| `2026-08-15 15:06:28` | `cowrie.command.input` |
| `2026-08-15 15:06:28` | `cowrie.log.closed` |
| `2026-08-15 15:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-457798f18220

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:06 |
| **Last Seen** | 2026-08-15 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:06:35` | `cowrie.session.connect` |
| `2026-08-15 15:06:35` | `cowrie.client.version` |
| `2026-08-15 15:06:35` | `cowrie.client.kex` |
| `2026-08-15 15:06:36` | `cowrie.login.success` |
| `2026-08-15 15:06:37` | `cowrie.session.params` |
| `2026-08-15 15:06:37` | `cowrie.command.input` |
| `2026-08-15 15:06:37` | `cowrie.log.closed` |
| `2026-08-15 15:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0adfd4e9c353

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:06 |
| **Last Seen** | 2026-08-15 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:06:43` | `cowrie.session.connect` |
| `2026-08-15 15:06:43` | `cowrie.client.version` |
| `2026-08-15 15:06:44` | `cowrie.client.kex` |
| `2026-08-15 15:06:44` | `cowrie.login.success` |
| `2026-08-15 15:06:45` | `cowrie.session.params` |
| `2026-08-15 15:06:45` | `cowrie.command.input` |
| `2026-08-15 15:06:45` | `cowrie.log.closed` |
| `2026-08-15 15:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10e907aa98d4

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-08-15 15:06 |
| **Last Seen** | 2026-08-15 15:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:06:48` | `cowrie.session.connect` |
| `2026-08-15 15:06:49` | `cowrie.client.version` |
| `2026-08-15 15:06:49` | `cowrie.client.kex` |
| `2026-08-15 15:06:51` | `cowrie.login.success` |
| `2026-08-15 15:06:51` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ae9f5f1fc1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:06 |
| **Last Seen** | 2026-08-15 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:06:52` | `cowrie.session.connect` |
| `2026-08-15 15:06:52` | `cowrie.client.version` |
| `2026-08-15 15:06:52` | `cowrie.client.kex` |
| `2026-08-15 15:06:52` | `cowrie.login.success` |
| `2026-08-15 15:06:53` | `cowrie.session.params` |
| `2026-08-15 15:06:53` | `cowrie.command.input` |
| `2026-08-15 15:06:53` | `cowrie.log.closed` |
| `2026-08-15 15:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52da7474ef87

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-08-15 15:06 |
| **Last Seen** | 2026-08-15 15:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:06:57` | `cowrie.session.connect` |
| `2026-08-15 15:06:57` | `cowrie.client.version` |
| `2026-08-15 15:06:57` | `cowrie.client.kex` |
| `2026-08-15 15:07:00` | `cowrie.login.success` |
| `2026-08-15 15:07:01` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43b054da6089

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:07 |
| **Last Seen** | 2026-08-15 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:07:01` | `cowrie.session.connect` |
| `2026-08-15 15:07:01` | `cowrie.client.version` |
| `2026-08-15 15:07:01` | `cowrie.client.kex` |
| `2026-08-15 15:07:01` | `cowrie.login.success` |
| `2026-08-15 15:07:02` | `cowrie.session.params` |
| `2026-08-15 15:07:02` | `cowrie.command.input` |
| `2026-08-15 15:07:02` | `cowrie.log.closed` |
| `2026-08-15 15:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d882be5b562

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:07 |
| **Last Seen** | 2026-08-15 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:07:09` | `cowrie.session.connect` |
| `2026-08-15 15:07:09` | `cowrie.client.version` |
| `2026-08-15 15:07:09` | `cowrie.client.kex` |
| `2026-08-15 15:07:09` | `cowrie.login.success` |
| `2026-08-15 15:07:10` | `cowrie.session.params` |
| `2026-08-15 15:07:10` | `cowrie.command.input` |
| `2026-08-15 15:07:10` | `cowrie.log.closed` |
| `2026-08-15 15:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5b50b0344bf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:07 |
| **Last Seen** | 2026-08-15 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:07:17` | `cowrie.session.connect` |
| `2026-08-15 15:07:17` | `cowrie.client.version` |
| `2026-08-15 15:07:17` | `cowrie.client.kex` |
| `2026-08-15 15:07:18` | `cowrie.login.success` |
| `2026-08-15 15:07:19` | `cowrie.session.params` |
| `2026-08-15 15:07:19` | `cowrie.command.input` |
| `2026-08-15 15:07:19` | `cowrie.log.closed` |
| `2026-08-15 15:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e043662852

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:07 |
| **Last Seen** | 2026-08-15 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:07:25` | `cowrie.session.connect` |
| `2026-08-15 15:07:25` | `cowrie.client.version` |
| `2026-08-15 15:07:25` | `cowrie.client.kex` |
| `2026-08-15 15:07:26` | `cowrie.login.success` |
| `2026-08-15 15:07:26` | `cowrie.session.params` |
| `2026-08-15 15:07:26` | `cowrie.command.input` |
| `2026-08-15 15:07:27` | `cowrie.log.closed` |
| `2026-08-15 15:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b83988a4864

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:07 |
| **Last Seen** | 2026-08-15 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:07:33` | `cowrie.session.connect` |
| `2026-08-15 15:07:33` | `cowrie.client.version` |
| `2026-08-15 15:07:34` | `cowrie.client.kex` |
| `2026-08-15 15:07:34` | `cowrie.login.success` |
| `2026-08-15 15:07:35` | `cowrie.session.params` |
| `2026-08-15 15:07:35` | `cowrie.command.input` |
| `2026-08-15 15:07:35` | `cowrie.log.closed` |
| `2026-08-15 15:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2e3359d0898

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:07 |
| **Last Seen** | 2026-08-15 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:07:42` | `cowrie.session.connect` |
| `2026-08-15 15:07:42` | `cowrie.client.version` |
| `2026-08-15 15:07:42` | `cowrie.client.kex` |
| `2026-08-15 15:07:43` | `cowrie.login.success` |
| `2026-08-15 15:07:44` | `cowrie.session.params` |
| `2026-08-15 15:07:44` | `cowrie.command.input` |
| `2026-08-15 15:07:44` | `cowrie.log.closed` |
| `2026-08-15 15:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-944e327240be

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:07 |
| **Last Seen** | 2026-08-15 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:07:51` | `cowrie.session.connect` |
| `2026-08-15 15:07:51` | `cowrie.client.version` |
| `2026-08-15 15:07:51` | `cowrie.client.kex` |
| `2026-08-15 15:07:51` | `cowrie.login.success` |
| `2026-08-15 15:07:52` | `cowrie.session.params` |
| `2026-08-15 15:07:52` | `cowrie.command.input` |
| `2026-08-15 15:07:52` | `cowrie.log.closed` |
| `2026-08-15 15:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e84dafb7e0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:07 |
| **Last Seen** | 2026-08-15 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:07:58` | `cowrie.session.connect` |
| `2026-08-15 15:07:58` | `cowrie.client.version` |
| `2026-08-15 15:07:59` | `cowrie.client.kex` |
| `2026-08-15 15:07:59` | `cowrie.login.success` |
| `2026-08-15 15:08:00` | `cowrie.session.params` |
| `2026-08-15 15:08:00` | `cowrie.command.input` |
| `2026-08-15 15:08:00` | `cowrie.log.closed` |
| `2026-08-15 15:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9cec34208e2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:08 |
| **Last Seen** | 2026-08-15 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:08:06` | `cowrie.session.connect` |
| `2026-08-15 15:08:06` | `cowrie.client.version` |
| `2026-08-15 15:08:06` | `cowrie.client.kex` |
| `2026-08-15 15:08:06` | `cowrie.login.success` |
| `2026-08-15 15:08:08` | `cowrie.session.params` |
| `2026-08-15 15:08:08` | `cowrie.command.input` |
| `2026-08-15 15:08:08` | `cowrie.log.closed` |
| `2026-08-15 15:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8cf3df28d02

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:08 |
| **Last Seen** | 2026-08-15 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:08:14` | `cowrie.session.connect` |
| `2026-08-15 15:08:14` | `cowrie.client.version` |
| `2026-08-15 15:08:14` | `cowrie.client.kex` |
| `2026-08-15 15:08:15` | `cowrie.login.success` |
| `2026-08-15 15:08:15` | `cowrie.session.params` |
| `2026-08-15 15:08:15` | `cowrie.command.input` |
| `2026-08-15 15:08:16` | `cowrie.log.closed` |
| `2026-08-15 15:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2975b8f4807

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:08 |
| **Last Seen** | 2026-08-15 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:08:23` | `cowrie.session.connect` |
| `2026-08-15 15:08:23` | `cowrie.client.version` |
| `2026-08-15 15:08:23` | `cowrie.client.kex` |
| `2026-08-15 15:08:24` | `cowrie.login.success` |
| `2026-08-15 15:08:25` | `cowrie.session.params` |
| `2026-08-15 15:08:25` | `cowrie.command.input` |
| `2026-08-15 15:08:25` | `cowrie.log.closed` |
| `2026-08-15 15:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82b24ca2c02

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:08 |
| **Last Seen** | 2026-08-15 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:08:31` | `cowrie.session.connect` |
| `2026-08-15 15:08:31` | `cowrie.client.version` |
| `2026-08-15 15:08:31` | `cowrie.client.kex` |
| `2026-08-15 15:08:31` | `cowrie.login.success` |
| `2026-08-15 15:08:32` | `cowrie.session.params` |
| `2026-08-15 15:08:32` | `cowrie.command.input` |
| `2026-08-15 15:08:32` | `cowrie.log.closed` |
| `2026-08-15 15:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d5e27cfc72

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:08 |
| **Last Seen** | 2026-08-15 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:08:40` | `cowrie.session.connect` |
| `2026-08-15 15:08:40` | `cowrie.client.version` |
| `2026-08-15 15:08:40` | `cowrie.client.kex` |
| `2026-08-15 15:08:40` | `cowrie.login.success` |
| `2026-08-15 15:08:41` | `cowrie.session.params` |
| `2026-08-15 15:08:41` | `cowrie.command.input` |
| `2026-08-15 15:08:41` | `cowrie.log.closed` |
| `2026-08-15 15:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95800f95c147

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:08 |
| **Last Seen** | 2026-08-15 15:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:08:48` | `cowrie.session.connect` |
| `2026-08-15 15:08:48` | `cowrie.client.version` |
| `2026-08-15 15:08:48` | `cowrie.client.kex` |
| `2026-08-15 15:08:49` | `cowrie.login.success` |
| `2026-08-15 15:08:50` | `cowrie.session.params` |
| `2026-08-15 15:08:50` | `cowrie.command.input` |
| `2026-08-15 15:08:50` | `cowrie.log.closed` |
| `2026-08-15 15:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df031b35207

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:08 |
| **Last Seen** | 2026-08-15 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:08:56` | `cowrie.session.connect` |
| `2026-08-15 15:08:56` | `cowrie.client.version` |
| `2026-08-15 15:08:56` | `cowrie.client.kex` |
| `2026-08-15 15:08:57` | `cowrie.login.success` |
| `2026-08-15 15:08:58` | `cowrie.session.params` |
| `2026-08-15 15:08:58` | `cowrie.command.input` |
| `2026-08-15 15:08:58` | `cowrie.log.closed` |
| `2026-08-15 15:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367a4b6dfefd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:05` | `cowrie.session.connect` |
| `2026-08-15 15:09:05` | `cowrie.client.version` |
| `2026-08-15 15:09:05` | `cowrie.client.kex` |
| `2026-08-15 15:09:06` | `cowrie.login.success` |
| `2026-08-15 15:09:06` | `cowrie.session.params` |
| `2026-08-15 15:09:06` | `cowrie.command.input` |
| `2026-08-15 15:09:06` | `cowrie.log.closed` |
| `2026-08-15 15:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4727c0154a5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:13` | `cowrie.session.connect` |
| `2026-08-15 15:09:13` | `cowrie.client.version` |
| `2026-08-15 15:09:13` | `cowrie.client.kex` |
| `2026-08-15 15:09:13` | `cowrie.login.success` |
| `2026-08-15 15:09:14` | `cowrie.session.params` |
| `2026-08-15 15:09:14` | `cowrie.command.input` |
| `2026-08-15 15:09:14` | `cowrie.log.closed` |
| `2026-08-15 15:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-714a37412157

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:21` | `cowrie.session.connect` |
| `2026-08-15 15:09:21` | `cowrie.client.version` |
| `2026-08-15 15:09:21` | `cowrie.client.kex` |
| `2026-08-15 15:09:22` | `cowrie.login.success` |
| `2026-08-15 15:09:22` | `cowrie.session.params` |
| `2026-08-15 15:09:22` | `cowrie.command.input` |
| `2026-08-15 15:09:22` | `cowrie.log.closed` |
| `2026-08-15 15:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-453bf8317816

| Field | Detail |
|---|---|
| **Source IP** | `123.123.196[.]140` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:22` | `cowrie.session.connect` |
| `2026-08-15 15:09:24` | `cowrie.client.version` |
| `2026-08-15 15:09:24` | `cowrie.client.kex` |
| `2026-08-15 15:09:26` | `cowrie.login.success` |
| `2026-08-15 15:09:27` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.123.196[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.123.196[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0761a056d60

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:30` | `cowrie.session.connect` |
| `2026-08-15 15:09:30` | `cowrie.client.version` |
| `2026-08-15 15:09:30` | `cowrie.client.kex` |
| `2026-08-15 15:09:30` | `cowrie.login.success` |
| `2026-08-15 15:09:31` | `cowrie.session.params` |
| `2026-08-15 15:09:31` | `cowrie.command.input` |
| `2026-08-15 15:09:31` | `cowrie.log.closed` |
| `2026-08-15 15:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc5a3f13429

| Field | Detail |
|---|---|
| **Source IP** | `185.40.122[.]250` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:32` | `cowrie.session.connect` |
| `2026-08-15 15:09:33` | `cowrie.client.version` |
| `2026-08-15 15:09:33` | `cowrie.client.kex` |
| `2026-08-15 15:09:37` | `cowrie.login.success` |
| `2026-08-15 15:09:38` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.40.122[.]250` to AbuseIPDB if not already reported
- [ ] Block `185.40.122[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f4120f2e2dc

| Field | Detail |
|---|---|
| **Source IP** | `125.35.109[.]214` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:35` | `cowrie.session.connect` |
| `2026-08-15 15:09:36` | `cowrie.client.version` |
| `2026-08-15 15:09:36` | `cowrie.client.kex` |
| `2026-08-15 15:09:38` | `cowrie.login.success` |
| `2026-08-15 15:09:39` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.35.109[.]214` to AbuseIPDB if not already reported
- [ ] Block `125.35.109[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f657808d15c5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:38` | `cowrie.session.connect` |
| `2026-08-15 15:09:38` | `cowrie.client.version` |
| `2026-08-15 15:09:38` | `cowrie.client.kex` |
| `2026-08-15 15:09:38` | `cowrie.login.success` |
| `2026-08-15 15:09:39` | `cowrie.session.params` |
| `2026-08-15 15:09:39` | `cowrie.command.input` |
| `2026-08-15 15:09:39` | `cowrie.log.closed` |
| `2026-08-15 15:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ae30f11f49

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:45` | `cowrie.session.connect` |
| `2026-08-15 15:09:45` | `cowrie.client.version` |
| `2026-08-15 15:09:45` | `cowrie.client.kex` |
| `2026-08-15 15:09:46` | `cowrie.login.success` |
| `2026-08-15 15:09:46` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1342aa0a88b3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:46` | `cowrie.session.connect` |
| `2026-08-15 15:09:46` | `cowrie.client.version` |
| `2026-08-15 15:09:46` | `cowrie.client.kex` |
| `2026-08-15 15:09:46` | `cowrie.login.success` |
| `2026-08-15 15:09:47` | `cowrie.session.params` |
| `2026-08-15 15:09:47` | `cowrie.command.input` |
| `2026-08-15 15:09:47` | `cowrie.log.closed` |
| `2026-08-15 15:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7500b621008c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:09 |
| **Last Seen** | 2026-08-15 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:09:54` | `cowrie.session.connect` |
| `2026-08-15 15:09:54` | `cowrie.client.version` |
| `2026-08-15 15:09:54` | `cowrie.client.kex` |
| `2026-08-15 15:09:55` | `cowrie.login.success` |
| `2026-08-15 15:09:56` | `cowrie.session.params` |
| `2026-08-15 15:09:56` | `cowrie.command.input` |
| `2026-08-15 15:09:56` | `cowrie.log.closed` |
| `2026-08-15 15:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0b04fce2027

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:10 |
| **Last Seen** | 2026-08-15 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:10:03` | `cowrie.session.connect` |
| `2026-08-15 15:10:03` | `cowrie.client.version` |
| `2026-08-15 15:10:03` | `cowrie.client.kex` |
| `2026-08-15 15:10:03` | `cowrie.login.success` |
| `2026-08-15 15:10:04` | `cowrie.session.params` |
| `2026-08-15 15:10:04` | `cowrie.command.input` |
| `2026-08-15 15:10:04` | `cowrie.log.closed` |
| `2026-08-15 15:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71f8c361620c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:10 |
| **Last Seen** | 2026-08-15 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:10:10` | `cowrie.session.connect` |
| `2026-08-15 15:10:10` | `cowrie.client.version` |
| `2026-08-15 15:10:10` | `cowrie.client.kex` |
| `2026-08-15 15:10:11` | `cowrie.login.success` |
| `2026-08-15 15:10:11` | `cowrie.session.params` |
| `2026-08-15 15:10:11` | `cowrie.command.input` |
| `2026-08-15 15:10:12` | `cowrie.log.closed` |
| `2026-08-15 15:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e29bbce1ad86

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:10 |
| **Last Seen** | 2026-08-15 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:10:18` | `cowrie.session.connect` |
| `2026-08-15 15:10:18` | `cowrie.client.version` |
| `2026-08-15 15:10:18` | `cowrie.client.kex` |
| `2026-08-15 15:10:19` | `cowrie.login.success` |
| `2026-08-15 15:10:20` | `cowrie.session.params` |
| `2026-08-15 15:10:20` | `cowrie.command.input` |
| `2026-08-15 15:10:20` | `cowrie.log.closed` |
| `2026-08-15 15:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-893eb1a5047a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:10 |
| **Last Seen** | 2026-08-15 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:10:26` | `cowrie.session.connect` |
| `2026-08-15 15:10:26` | `cowrie.client.version` |
| `2026-08-15 15:10:27` | `cowrie.client.kex` |
| `2026-08-15 15:10:27` | `cowrie.login.success` |
| `2026-08-15 15:10:28` | `cowrie.session.params` |
| `2026-08-15 15:10:28` | `cowrie.command.input` |
| `2026-08-15 15:10:28` | `cowrie.log.closed` |
| `2026-08-15 15:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-771e8514db00

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:10 |
| **Last Seen** | 2026-08-15 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:10:35` | `cowrie.session.connect` |
| `2026-08-15 15:10:35` | `cowrie.client.version` |
| `2026-08-15 15:10:35` | `cowrie.client.kex` |
| `2026-08-15 15:10:35` | `cowrie.login.success` |
| `2026-08-15 15:10:36` | `cowrie.session.params` |
| `2026-08-15 15:10:36` | `cowrie.command.input` |
| `2026-08-15 15:10:36` | `cowrie.log.closed` |
| `2026-08-15 15:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26bd7252229a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:10 |
| **Last Seen** | 2026-08-15 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:10:43` | `cowrie.session.connect` |
| `2026-08-15 15:10:43` | `cowrie.client.version` |
| `2026-08-15 15:10:43` | `cowrie.client.kex` |
| `2026-08-15 15:10:43` | `cowrie.login.success` |
| `2026-08-15 15:10:45` | `cowrie.session.params` |
| `2026-08-15 15:10:45` | `cowrie.command.input` |
| `2026-08-15 15:10:45` | `cowrie.log.closed` |
| `2026-08-15 15:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e634de1a5cac

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:10 |
| **Last Seen** | 2026-08-15 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:10:52` | `cowrie.session.connect` |
| `2026-08-15 15:10:52` | `cowrie.client.version` |
| `2026-08-15 15:10:52` | `cowrie.client.kex` |
| `2026-08-15 15:10:53` | `cowrie.login.success` |
| `2026-08-15 15:10:53` | `cowrie.session.params` |
| `2026-08-15 15:10:53` | `cowrie.command.input` |
| `2026-08-15 15:10:53` | `cowrie.log.closed` |
| `2026-08-15 15:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-817eb9908105

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:11 |
| **Last Seen** | 2026-08-15 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:11:00` | `cowrie.session.connect` |
| `2026-08-15 15:11:00` | `cowrie.client.version` |
| `2026-08-15 15:11:00` | `cowrie.client.kex` |
| `2026-08-15 15:11:01` | `cowrie.login.success` |
| `2026-08-15 15:11:02` | `cowrie.session.params` |
| `2026-08-15 15:11:02` | `cowrie.command.input` |
| `2026-08-15 15:11:02` | `cowrie.log.closed` |
| `2026-08-15 15:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada788ade2c9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:11 |
| **Last Seen** | 2026-08-15 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:11:09` | `cowrie.session.connect` |
| `2026-08-15 15:11:09` | `cowrie.client.version` |
| `2026-08-15 15:11:09` | `cowrie.client.kex` |
| `2026-08-15 15:11:09` | `cowrie.login.success` |
| `2026-08-15 15:11:10` | `cowrie.session.params` |
| `2026-08-15 15:11:10` | `cowrie.command.input` |
| `2026-08-15 15:11:10` | `cowrie.log.closed` |
| `2026-08-15 15:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7461c36a80d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:11 |
| **Last Seen** | 2026-08-15 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:11:17` | `cowrie.session.connect` |
| `2026-08-15 15:11:17` | `cowrie.client.version` |
| `2026-08-15 15:11:17` | `cowrie.client.kex` |
| `2026-08-15 15:11:18` | `cowrie.login.success` |
| `2026-08-15 15:11:18` | `cowrie.session.params` |
| `2026-08-15 15:11:18` | `cowrie.command.input` |
| `2026-08-15 15:11:18` | `cowrie.log.closed` |
| `2026-08-15 15:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96a77efa7013

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:11 |
| **Last Seen** | 2026-08-15 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:11:26` | `cowrie.session.connect` |
| `2026-08-15 15:11:26` | `cowrie.client.version` |
| `2026-08-15 15:11:26` | `cowrie.client.kex` |
| `2026-08-15 15:11:26` | `cowrie.login.success` |
| `2026-08-15 15:11:27` | `cowrie.session.params` |
| `2026-08-15 15:11:27` | `cowrie.command.input` |
| `2026-08-15 15:11:27` | `cowrie.log.closed` |
| `2026-08-15 15:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-361da6c30e77

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:11 |
| **Last Seen** | 2026-08-15 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:11:34` | `cowrie.session.connect` |
| `2026-08-15 15:11:34` | `cowrie.client.version` |
| `2026-08-15 15:11:34` | `cowrie.client.kex` |
| `2026-08-15 15:11:35` | `cowrie.login.success` |
| `2026-08-15 15:11:36` | `cowrie.session.params` |
| `2026-08-15 15:11:36` | `cowrie.command.input` |
| `2026-08-15 15:11:36` | `cowrie.log.closed` |
| `2026-08-15 15:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad270c03a3f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:11 |
| **Last Seen** | 2026-08-15 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:11:42` | `cowrie.session.connect` |
| `2026-08-15 15:11:42` | `cowrie.client.version` |
| `2026-08-15 15:11:42` | `cowrie.client.kex` |
| `2026-08-15 15:11:43` | `cowrie.login.success` |
| `2026-08-15 15:11:43` | `cowrie.session.params` |
| `2026-08-15 15:11:43` | `cowrie.command.input` |
| `2026-08-15 15:11:44` | `cowrie.log.closed` |
| `2026-08-15 15:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4c7ad040d3c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:11 |
| **Last Seen** | 2026-08-15 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:11:51` | `cowrie.session.connect` |
| `2026-08-15 15:11:51` | `cowrie.client.version` |
| `2026-08-15 15:11:51` | `cowrie.client.kex` |
| `2026-08-15 15:11:51` | `cowrie.login.success` |
| `2026-08-15 15:11:52` | `cowrie.session.params` |
| `2026-08-15 15:11:52` | `cowrie.command.input` |
| `2026-08-15 15:11:53` | `cowrie.log.closed` |
| `2026-08-15 15:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d158159de818

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:11 |
| **Last Seen** | 2026-08-15 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:11:59` | `cowrie.session.connect` |
| `2026-08-15 15:11:59` | `cowrie.client.version` |
| `2026-08-15 15:11:59` | `cowrie.client.kex` |
| `2026-08-15 15:12:00` | `cowrie.login.success` |
| `2026-08-15 15:12:00` | `cowrie.session.params` |
| `2026-08-15 15:12:00` | `cowrie.command.input` |
| `2026-08-15 15:12:01` | `cowrie.log.closed` |
| `2026-08-15 15:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72969e555e9a

| Field | Detail |
|---|---|
| **Source IP** | `157.245.213[.]135` |
| **First Seen** | 2026-08-15 15:12 |
| **Last Seen** | 2026-08-15 15:13 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:12:02` | `cowrie.session.connect` |
| `2026-08-15 15:12:03` | `cowrie.telnet.option` |
| `2026-08-15 15:12:04` | `cowrie.telnet.option` |
| `2026-08-15 15:12:04` | `cowrie.login.success` |
| `2026-08-15 15:12:04` | `cowrie.session.params` |
| `2026-08-15 15:12:05` | `cowrie.telnet.option` |
| `2026-08-15 15:12:05` | `cowrie.telnet.option` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.failed` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.failed` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.failed` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.failed` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.failed` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.failed` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.failed` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.failed` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:12:05` | `cowrie.command.input` |
| `2026-08-15 15:13:06` | `cowrie.log.closed` |
| `2026-08-15 15:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.213[.]135` to AbuseIPDB if not already reported
- [ ] Block `157.245.213[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b3607e97e69

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:12 |
| **Last Seen** | 2026-08-15 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:12:08` | `cowrie.session.connect` |
| `2026-08-15 15:12:08` | `cowrie.client.version` |
| `2026-08-15 15:12:08` | `cowrie.client.kex` |
| `2026-08-15 15:12:09` | `cowrie.login.success` |
| `2026-08-15 15:12:09` | `cowrie.session.params` |
| `2026-08-15 15:12:09` | `cowrie.command.input` |
| `2026-08-15 15:12:10` | `cowrie.log.closed` |
| `2026-08-15 15:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201e166e6836

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:12 |
| **Last Seen** | 2026-08-15 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:12:17` | `cowrie.session.connect` |
| `2026-08-15 15:12:17` | `cowrie.client.version` |
| `2026-08-15 15:12:17` | `cowrie.client.kex` |
| `2026-08-15 15:12:17` | `cowrie.login.success` |
| `2026-08-15 15:12:18` | `cowrie.session.params` |
| `2026-08-15 15:12:18` | `cowrie.command.input` |
| `2026-08-15 15:12:18` | `cowrie.log.closed` |
| `2026-08-15 15:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d313f3208a7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:12 |
| **Last Seen** | 2026-08-15 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:12:25` | `cowrie.session.connect` |
| `2026-08-15 15:12:25` | `cowrie.client.version` |
| `2026-08-15 15:12:25` | `cowrie.client.kex` |
| `2026-08-15 15:12:25` | `cowrie.login.success` |
| `2026-08-15 15:12:26` | `cowrie.session.params` |
| `2026-08-15 15:12:26` | `cowrie.command.input` |
| `2026-08-15 15:12:26` | `cowrie.log.closed` |
| `2026-08-15 15:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4f0127c37a

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 15:12 |
| **Last Seen** | 2026-08-15 15:13 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:12:33` | `cowrie.session.connect` |
| `2026-08-15 15:12:38` | `cowrie.client.version` |
| `2026-08-15 15:12:38` | `cowrie.client.kex` |
| `2026-08-15 15:13:00` | `cowrie.login.success` |
| `2026-08-15 15:13:13` | `cowrie.session.params` |
| `2026-08-15 15:13:13` | `cowrie.command.input` |
| `2026-08-15 15:13:18` | `cowrie.log.closed` |
| `2026-08-15 15:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73200130060

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:12 |
| **Last Seen** | 2026-08-15 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:12:34` | `cowrie.session.connect` |
| `2026-08-15 15:12:34` | `cowrie.client.version` |
| `2026-08-15 15:12:34` | `cowrie.client.kex` |
| `2026-08-15 15:12:34` | `cowrie.login.success` |
| `2026-08-15 15:12:35` | `cowrie.session.params` |
| `2026-08-15 15:12:35` | `cowrie.command.input` |
| `2026-08-15 15:12:36` | `cowrie.log.closed` |
| `2026-08-15 15:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f4dfe8a3d8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:12 |
| **Last Seen** | 2026-08-15 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:12:42` | `cowrie.session.connect` |
| `2026-08-15 15:12:42` | `cowrie.client.version` |
| `2026-08-15 15:12:42` | `cowrie.client.kex` |
| `2026-08-15 15:12:43` | `cowrie.login.success` |
| `2026-08-15 15:12:43` | `cowrie.session.params` |
| `2026-08-15 15:12:43` | `cowrie.command.input` |
| `2026-08-15 15:12:43` | `cowrie.log.closed` |
| `2026-08-15 15:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a9e26ff844a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:12 |
| **Last Seen** | 2026-08-15 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:12:51` | `cowrie.session.connect` |
| `2026-08-15 15:12:51` | `cowrie.client.version` |
| `2026-08-15 15:12:51` | `cowrie.client.kex` |
| `2026-08-15 15:12:51` | `cowrie.login.success` |
| `2026-08-15 15:12:52` | `cowrie.session.params` |
| `2026-08-15 15:12:52` | `cowrie.command.input` |
| `2026-08-15 15:12:52` | `cowrie.log.closed` |
| `2026-08-15 15:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eefab0afce12

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:12 |
| **Last Seen** | 2026-08-15 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:12:59` | `cowrie.session.connect` |
| `2026-08-15 15:12:59` | `cowrie.client.version` |
| `2026-08-15 15:12:59` | `cowrie.client.kex` |
| `2026-08-15 15:12:59` | `cowrie.login.success` |
| `2026-08-15 15:13:00` | `cowrie.session.params` |
| `2026-08-15 15:13:00` | `cowrie.command.input` |
| `2026-08-15 15:13:00` | `cowrie.log.closed` |
| `2026-08-15 15:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e604e8e2d92

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:13 |
| **Last Seen** | 2026-08-15 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:13:07` | `cowrie.session.connect` |
| `2026-08-15 15:13:07` | `cowrie.client.version` |
| `2026-08-15 15:13:07` | `cowrie.client.kex` |
| `2026-08-15 15:13:08` | `cowrie.login.success` |
| `2026-08-15 15:13:08` | `cowrie.session.params` |
| `2026-08-15 15:13:08` | `cowrie.command.input` |
| `2026-08-15 15:13:08` | `cowrie.log.closed` |
| `2026-08-15 15:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee7d833aa88

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:13 |
| **Last Seen** | 2026-08-15 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:13:16` | `cowrie.session.connect` |
| `2026-08-15 15:13:16` | `cowrie.client.version` |
| `2026-08-15 15:13:17` | `cowrie.client.kex` |
| `2026-08-15 15:13:17` | `cowrie.login.success` |
| `2026-08-15 15:13:18` | `cowrie.session.params` |
| `2026-08-15 15:13:18` | `cowrie.command.input` |
| `2026-08-15 15:13:18` | `cowrie.log.closed` |
| `2026-08-15 15:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33353e213d62

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:13 |
| **Last Seen** | 2026-08-15 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:13:26` | `cowrie.session.connect` |
| `2026-08-15 15:13:26` | `cowrie.client.version` |
| `2026-08-15 15:13:26` | `cowrie.client.kex` |
| `2026-08-15 15:13:26` | `cowrie.login.success` |
| `2026-08-15 15:13:27` | `cowrie.session.params` |
| `2026-08-15 15:13:27` | `cowrie.command.input` |
| `2026-08-15 15:13:27` | `cowrie.log.closed` |
| `2026-08-15 15:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e225d1923482

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:13 |
| **Last Seen** | 2026-08-15 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:13:34` | `cowrie.session.connect` |
| `2026-08-15 15:13:34` | `cowrie.client.version` |
| `2026-08-15 15:13:34` | `cowrie.client.kex` |
| `2026-08-15 15:13:34` | `cowrie.login.success` |
| `2026-08-15 15:13:35` | `cowrie.session.params` |
| `2026-08-15 15:13:35` | `cowrie.command.input` |
| `2026-08-15 15:13:36` | `cowrie.log.closed` |
| `2026-08-15 15:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d496cd7edc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:13 |
| **Last Seen** | 2026-08-15 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:13:42` | `cowrie.session.connect` |
| `2026-08-15 15:13:42` | `cowrie.client.version` |
| `2026-08-15 15:13:42` | `cowrie.client.kex` |
| `2026-08-15 15:13:42` | `cowrie.login.success` |
| `2026-08-15 15:13:43` | `cowrie.session.params` |
| `2026-08-15 15:13:43` | `cowrie.command.input` |
| `2026-08-15 15:13:43` | `cowrie.log.closed` |
| `2026-08-15 15:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370d5c6cec28

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:13 |
| **Last Seen** | 2026-08-15 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:13:50` | `cowrie.session.connect` |
| `2026-08-15 15:13:50` | `cowrie.client.version` |
| `2026-08-15 15:13:50` | `cowrie.client.kex` |
| `2026-08-15 15:13:50` | `cowrie.login.success` |
| `2026-08-15 15:13:51` | `cowrie.session.params` |
| `2026-08-15 15:13:51` | `cowrie.command.input` |
| `2026-08-15 15:13:51` | `cowrie.log.closed` |
| `2026-08-15 15:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d15e02c87ede

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:13 |
| **Last Seen** | 2026-08-15 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:13:57` | `cowrie.session.connect` |
| `2026-08-15 15:13:57` | `cowrie.client.version` |
| `2026-08-15 15:13:57` | `cowrie.client.kex` |
| `2026-08-15 15:13:57` | `cowrie.login.success` |
| `2026-08-15 15:13:58` | `cowrie.session.params` |
| `2026-08-15 15:13:58` | `cowrie.command.input` |
| `2026-08-15 15:13:58` | `cowrie.log.closed` |
| `2026-08-15 15:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e4834bc10bc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:14 |
| **Last Seen** | 2026-08-15 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:14:05` | `cowrie.session.connect` |
| `2026-08-15 15:14:05` | `cowrie.client.version` |
| `2026-08-15 15:14:05` | `cowrie.client.kex` |
| `2026-08-15 15:14:06` | `cowrie.login.success` |
| `2026-08-15 15:14:06` | `cowrie.session.params` |
| `2026-08-15 15:14:06` | `cowrie.command.input` |
| `2026-08-15 15:14:06` | `cowrie.log.closed` |
| `2026-08-15 15:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b8664ac6efc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:14 |
| **Last Seen** | 2026-08-15 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:14:13` | `cowrie.session.connect` |
| `2026-08-15 15:14:13` | `cowrie.client.version` |
| `2026-08-15 15:14:14` | `cowrie.client.kex` |
| `2026-08-15 15:14:14` | `cowrie.login.success` |
| `2026-08-15 15:14:15` | `cowrie.session.params` |
| `2026-08-15 15:14:15` | `cowrie.command.input` |
| `2026-08-15 15:14:15` | `cowrie.log.closed` |
| `2026-08-15 15:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34093fdc35a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:14 |
| **Last Seen** | 2026-08-15 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:14:22` | `cowrie.session.connect` |
| `2026-08-15 15:14:22` | `cowrie.client.version` |
| `2026-08-15 15:14:22` | `cowrie.client.kex` |
| `2026-08-15 15:14:23` | `cowrie.login.success` |
| `2026-08-15 15:14:24` | `cowrie.session.params` |
| `2026-08-15 15:14:24` | `cowrie.command.input` |
| `2026-08-15 15:14:24` | `cowrie.log.closed` |
| `2026-08-15 15:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b5e6c802d0c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:14 |
| **Last Seen** | 2026-08-15 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:14:30` | `cowrie.session.connect` |
| `2026-08-15 15:14:30` | `cowrie.client.version` |
| `2026-08-15 15:14:31` | `cowrie.client.kex` |
| `2026-08-15 15:14:31` | `cowrie.login.success` |
| `2026-08-15 15:14:32` | `cowrie.session.params` |
| `2026-08-15 15:14:32` | `cowrie.command.input` |
| `2026-08-15 15:14:32` | `cowrie.log.closed` |
| `2026-08-15 15:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ee4917ae895

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:14 |
| **Last Seen** | 2026-08-15 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:14:38` | `cowrie.session.connect` |
| `2026-08-15 15:14:38` | `cowrie.client.version` |
| `2026-08-15 15:14:38` | `cowrie.client.kex` |
| `2026-08-15 15:14:39` | `cowrie.login.success` |
| `2026-08-15 15:14:40` | `cowrie.session.params` |
| `2026-08-15 15:14:40` | `cowrie.command.input` |
| `2026-08-15 15:14:40` | `cowrie.log.closed` |
| `2026-08-15 15:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd00e6f195c5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:14 |
| **Last Seen** | 2026-08-15 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:14:47` | `cowrie.session.connect` |
| `2026-08-15 15:14:47` | `cowrie.client.version` |
| `2026-08-15 15:14:47` | `cowrie.client.kex` |
| `2026-08-15 15:14:47` | `cowrie.login.success` |
| `2026-08-15 15:14:48` | `cowrie.session.params` |
| `2026-08-15 15:14:48` | `cowrie.command.input` |
| `2026-08-15 15:14:48` | `cowrie.log.closed` |
| `2026-08-15 15:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d55916cb9d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:14 |
| **Last Seen** | 2026-08-15 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:14:55` | `cowrie.session.connect` |
| `2026-08-15 15:14:56` | `cowrie.client.version` |
| `2026-08-15 15:14:56` | `cowrie.client.kex` |
| `2026-08-15 15:14:56` | `cowrie.login.success` |
| `2026-08-15 15:14:57` | `cowrie.session.params` |
| `2026-08-15 15:14:57` | `cowrie.command.input` |
| `2026-08-15 15:14:57` | `cowrie.log.closed` |
| `2026-08-15 15:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d568eb9a7e94

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:15 |
| **Last Seen** | 2026-08-15 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:15:04` | `cowrie.session.connect` |
| `2026-08-15 15:15:04` | `cowrie.client.version` |
| `2026-08-15 15:15:04` | `cowrie.client.kex` |
| `2026-08-15 15:15:05` | `cowrie.login.success` |
| `2026-08-15 15:15:05` | `cowrie.session.params` |
| `2026-08-15 15:15:05` | `cowrie.command.input` |
| `2026-08-15 15:15:06` | `cowrie.log.closed` |
| `2026-08-15 15:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fa784548d2d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:15 |
| **Last Seen** | 2026-08-15 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:15:13` | `cowrie.session.connect` |
| `2026-08-15 15:15:13` | `cowrie.client.version` |
| `2026-08-15 15:15:13` | `cowrie.client.kex` |
| `2026-08-15 15:15:13` | `cowrie.login.success` |
| `2026-08-15 15:15:14` | `cowrie.session.params` |
| `2026-08-15 15:15:14` | `cowrie.command.input` |
| `2026-08-15 15:15:14` | `cowrie.log.closed` |
| `2026-08-15 15:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6a4ec09b1c4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:15 |
| **Last Seen** | 2026-08-15 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:15:21` | `cowrie.session.connect` |
| `2026-08-15 15:15:21` | `cowrie.client.version` |
| `2026-08-15 15:15:21` | `cowrie.client.kex` |
| `2026-08-15 15:15:21` | `cowrie.login.success` |
| `2026-08-15 15:15:22` | `cowrie.session.params` |
| `2026-08-15 15:15:22` | `cowrie.command.input` |
| `2026-08-15 15:15:22` | `cowrie.log.closed` |
| `2026-08-15 15:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e07a9a8fa8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:15 |
| **Last Seen** | 2026-08-15 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:15:29` | `cowrie.session.connect` |
| `2026-08-15 15:15:29` | `cowrie.client.version` |
| `2026-08-15 15:15:30` | `cowrie.client.kex` |
| `2026-08-15 15:15:30` | `cowrie.login.success` |
| `2026-08-15 15:15:31` | `cowrie.session.params` |
| `2026-08-15 15:15:31` | `cowrie.command.input` |
| `2026-08-15 15:15:31` | `cowrie.log.closed` |
| `2026-08-15 15:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccbacbf770a3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:15 |
| **Last Seen** | 2026-08-15 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:15:37` | `cowrie.session.connect` |
| `2026-08-15 15:15:37` | `cowrie.client.version` |
| `2026-08-15 15:15:38` | `cowrie.client.kex` |
| `2026-08-15 15:15:38` | `cowrie.login.success` |
| `2026-08-15 15:15:39` | `cowrie.session.params` |
| `2026-08-15 15:15:39` | `cowrie.command.input` |
| `2026-08-15 15:15:39` | `cowrie.log.closed` |
| `2026-08-15 15:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8027f25638a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:15 |
| **Last Seen** | 2026-08-15 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:15:46` | `cowrie.session.connect` |
| `2026-08-15 15:15:46` | `cowrie.client.version` |
| `2026-08-15 15:15:46` | `cowrie.client.kex` |
| `2026-08-15 15:15:46` | `cowrie.login.success` |
| `2026-08-15 15:15:47` | `cowrie.session.params` |
| `2026-08-15 15:15:47` | `cowrie.command.input` |
| `2026-08-15 15:15:47` | `cowrie.log.closed` |
| `2026-08-15 15:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7640a9fb4a8b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:15 |
| **Last Seen** | 2026-08-15 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:15:54` | `cowrie.session.connect` |
| `2026-08-15 15:15:54` | `cowrie.client.version` |
| `2026-08-15 15:15:54` | `cowrie.client.kex` |
| `2026-08-15 15:15:54` | `cowrie.login.success` |
| `2026-08-15 15:15:55` | `cowrie.session.params` |
| `2026-08-15 15:15:55` | `cowrie.command.input` |
| `2026-08-15 15:15:55` | `cowrie.log.closed` |
| `2026-08-15 15:15:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5737e9f14ee

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:16 |
| **Last Seen** | 2026-08-15 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:16:02` | `cowrie.session.connect` |
| `2026-08-15 15:16:02` | `cowrie.client.version` |
| `2026-08-15 15:16:02` | `cowrie.client.kex` |
| `2026-08-15 15:16:02` | `cowrie.login.success` |
| `2026-08-15 15:16:03` | `cowrie.session.params` |
| `2026-08-15 15:16:03` | `cowrie.command.input` |
| `2026-08-15 15:16:03` | `cowrie.log.closed` |
| `2026-08-15 15:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-764f97f43cd4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:16 |
| **Last Seen** | 2026-08-15 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:16:10` | `cowrie.session.connect` |
| `2026-08-15 15:16:10` | `cowrie.client.version` |
| `2026-08-15 15:16:10` | `cowrie.client.kex` |
| `2026-08-15 15:16:10` | `cowrie.login.success` |
| `2026-08-15 15:16:11` | `cowrie.session.params` |
| `2026-08-15 15:16:11` | `cowrie.command.input` |
| `2026-08-15 15:16:11` | `cowrie.log.closed` |
| `2026-08-15 15:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c8f1ed810f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:16 |
| **Last Seen** | 2026-08-15 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:16:18` | `cowrie.session.connect` |
| `2026-08-15 15:16:18` | `cowrie.client.version` |
| `2026-08-15 15:16:19` | `cowrie.client.kex` |
| `2026-08-15 15:16:19` | `cowrie.login.success` |
| `2026-08-15 15:16:20` | `cowrie.session.params` |
| `2026-08-15 15:16:20` | `cowrie.command.input` |
| `2026-08-15 15:16:20` | `cowrie.log.closed` |
| `2026-08-15 15:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1f35c12f14

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:16 |
| **Last Seen** | 2026-08-15 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:16:27` | `cowrie.session.connect` |
| `2026-08-15 15:16:27` | `cowrie.client.version` |
| `2026-08-15 15:16:28` | `cowrie.client.kex` |
| `2026-08-15 15:16:28` | `cowrie.login.success` |
| `2026-08-15 15:16:29` | `cowrie.session.params` |
| `2026-08-15 15:16:29` | `cowrie.command.input` |
| `2026-08-15 15:16:29` | `cowrie.log.closed` |
| `2026-08-15 15:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e346ed30499

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:16 |
| **Last Seen** | 2026-08-15 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:16:35` | `cowrie.session.connect` |
| `2026-08-15 15:16:35` | `cowrie.client.version` |
| `2026-08-15 15:16:35` | `cowrie.client.kex` |
| `2026-08-15 15:16:36` | `cowrie.login.success` |
| `2026-08-15 15:16:36` | `cowrie.session.params` |
| `2026-08-15 15:16:36` | `cowrie.command.input` |
| `2026-08-15 15:16:37` | `cowrie.log.closed` |
| `2026-08-15 15:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957d6c442083

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:16 |
| **Last Seen** | 2026-08-15 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:16:44` | `cowrie.session.connect` |
| `2026-08-15 15:16:44` | `cowrie.client.version` |
| `2026-08-15 15:16:44` | `cowrie.client.kex` |
| `2026-08-15 15:16:45` | `cowrie.login.success` |
| `2026-08-15 15:16:45` | `cowrie.session.params` |
| `2026-08-15 15:16:45` | `cowrie.command.input` |
| `2026-08-15 15:16:45` | `cowrie.log.closed` |
| `2026-08-15 15:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3766b5fde0fd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:16 |
| **Last Seen** | 2026-08-15 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:16:52` | `cowrie.session.connect` |
| `2026-08-15 15:16:52` | `cowrie.client.version` |
| `2026-08-15 15:16:53` | `cowrie.client.kex` |
| `2026-08-15 15:16:53` | `cowrie.login.success` |
| `2026-08-15 15:16:54` | `cowrie.session.params` |
| `2026-08-15 15:16:54` | `cowrie.command.input` |
| `2026-08-15 15:16:54` | `cowrie.log.closed` |
| `2026-08-15 15:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b78484e1bbb8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:17 |
| **Last Seen** | 2026-08-15 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:17:00` | `cowrie.session.connect` |
| `2026-08-15 15:17:00` | `cowrie.client.version` |
| `2026-08-15 15:17:01` | `cowrie.client.kex` |
| `2026-08-15 15:17:01` | `cowrie.login.success` |
| `2026-08-15 15:17:02` | `cowrie.session.params` |
| `2026-08-15 15:17:02` | `cowrie.command.input` |
| `2026-08-15 15:17:02` | `cowrie.log.closed` |
| `2026-08-15 15:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1057ee152ef7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:17 |
| **Last Seen** | 2026-08-15 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:17:10` | `cowrie.session.connect` |
| `2026-08-15 15:17:10` | `cowrie.client.version` |
| `2026-08-15 15:17:10` | `cowrie.client.kex` |
| `2026-08-15 15:17:10` | `cowrie.login.success` |
| `2026-08-15 15:17:11` | `cowrie.session.params` |
| `2026-08-15 15:17:11` | `cowrie.command.input` |
| `2026-08-15 15:17:11` | `cowrie.log.closed` |
| `2026-08-15 15:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9112fe6522e6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:17 |
| **Last Seen** | 2026-08-15 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:17:18` | `cowrie.session.connect` |
| `2026-08-15 15:17:18` | `cowrie.client.version` |
| `2026-08-15 15:17:18` | `cowrie.client.kex` |
| `2026-08-15 15:17:19` | `cowrie.login.success` |
| `2026-08-15 15:17:20` | `cowrie.session.params` |
| `2026-08-15 15:17:20` | `cowrie.command.input` |
| `2026-08-15 15:17:20` | `cowrie.log.closed` |
| `2026-08-15 15:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89fe858b384e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:17 |
| **Last Seen** | 2026-08-15 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:17:26` | `cowrie.session.connect` |
| `2026-08-15 15:17:26` | `cowrie.client.version` |
| `2026-08-15 15:17:26` | `cowrie.client.kex` |
| `2026-08-15 15:17:27` | `cowrie.login.success` |
| `2026-08-15 15:17:27` | `cowrie.session.params` |
| `2026-08-15 15:17:27` | `cowrie.command.input` |
| `2026-08-15 15:17:28` | `cowrie.log.closed` |
| `2026-08-15 15:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2f703d60e5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:17 |
| **Last Seen** | 2026-08-15 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:17:35` | `cowrie.session.connect` |
| `2026-08-15 15:17:35` | `cowrie.client.version` |
| `2026-08-15 15:17:35` | `cowrie.client.kex` |
| `2026-08-15 15:17:35` | `cowrie.login.success` |
| `2026-08-15 15:17:36` | `cowrie.session.params` |
| `2026-08-15 15:17:36` | `cowrie.command.input` |
| `2026-08-15 15:17:36` | `cowrie.log.closed` |
| `2026-08-15 15:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-143f644e8e7f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:17 |
| **Last Seen** | 2026-08-15 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:17:43` | `cowrie.session.connect` |
| `2026-08-15 15:17:43` | `cowrie.client.version` |
| `2026-08-15 15:17:43` | `cowrie.client.kex` |
| `2026-08-15 15:17:43` | `cowrie.login.success` |
| `2026-08-15 15:17:44` | `cowrie.session.params` |
| `2026-08-15 15:17:44` | `cowrie.command.input` |
| `2026-08-15 15:17:44` | `cowrie.log.closed` |
| `2026-08-15 15:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-369333e4a5fa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:17 |
| **Last Seen** | 2026-08-15 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:17:51` | `cowrie.session.connect` |
| `2026-08-15 15:17:51` | `cowrie.client.version` |
| `2026-08-15 15:17:51` | `cowrie.client.kex` |
| `2026-08-15 15:17:51` | `cowrie.login.success` |
| `2026-08-15 15:17:52` | `cowrie.session.params` |
| `2026-08-15 15:17:52` | `cowrie.command.input` |
| `2026-08-15 15:17:52` | `cowrie.log.closed` |
| `2026-08-15 15:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf7ed4d74f3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:17 |
| **Last Seen** | 2026-08-15 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:17:59` | `cowrie.session.connect` |
| `2026-08-15 15:18:00` | `cowrie.client.version` |
| `2026-08-15 15:18:00` | `cowrie.client.kex` |
| `2026-08-15 15:18:00` | `cowrie.login.success` |
| `2026-08-15 15:18:01` | `cowrie.session.params` |
| `2026-08-15 15:18:01` | `cowrie.command.input` |
| `2026-08-15 15:18:01` | `cowrie.log.closed` |
| `2026-08-15 15:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf3b6fbaf33

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:18 |
| **Last Seen** | 2026-08-15 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:18:08` | `cowrie.session.connect` |
| `2026-08-15 15:18:08` | `cowrie.client.version` |
| `2026-08-15 15:18:08` | `cowrie.client.kex` |
| `2026-08-15 15:18:08` | `cowrie.login.success` |
| `2026-08-15 15:18:09` | `cowrie.session.params` |
| `2026-08-15 15:18:09` | `cowrie.command.input` |
| `2026-08-15 15:18:09` | `cowrie.log.closed` |
| `2026-08-15 15:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec380d49a1b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:18 |
| **Last Seen** | 2026-08-15 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:18:16` | `cowrie.session.connect` |
| `2026-08-15 15:18:16` | `cowrie.client.version` |
| `2026-08-15 15:18:16` | `cowrie.client.kex` |
| `2026-08-15 15:18:16` | `cowrie.login.success` |
| `2026-08-15 15:18:17` | `cowrie.session.params` |
| `2026-08-15 15:18:17` | `cowrie.command.input` |
| `2026-08-15 15:18:17` | `cowrie.log.closed` |
| `2026-08-15 15:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb0fce93ec6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:18 |
| **Last Seen** | 2026-08-15 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:18:24` | `cowrie.session.connect` |
| `2026-08-15 15:18:24` | `cowrie.client.version` |
| `2026-08-15 15:18:24` | `cowrie.client.kex` |
| `2026-08-15 15:18:24` | `cowrie.login.success` |
| `2026-08-15 15:18:25` | `cowrie.session.params` |
| `2026-08-15 15:18:25` | `cowrie.command.input` |
| `2026-08-15 15:18:25` | `cowrie.log.closed` |
| `2026-08-15 15:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4a773131e1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:18 |
| **Last Seen** | 2026-08-15 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:18:32` | `cowrie.session.connect` |
| `2026-08-15 15:18:32` | `cowrie.client.version` |
| `2026-08-15 15:18:33` | `cowrie.client.kex` |
| `2026-08-15 15:18:33` | `cowrie.login.success` |
| `2026-08-15 15:18:34` | `cowrie.session.params` |
| `2026-08-15 15:18:34` | `cowrie.command.input` |
| `2026-08-15 15:18:34` | `cowrie.log.closed` |
| `2026-08-15 15:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5091e9f53ddb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:18 |
| **Last Seen** | 2026-08-15 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:18:41` | `cowrie.session.connect` |
| `2026-08-15 15:18:41` | `cowrie.client.version` |
| `2026-08-15 15:18:41` | `cowrie.client.kex` |
| `2026-08-15 15:18:41` | `cowrie.login.success` |
| `2026-08-15 15:18:42` | `cowrie.session.params` |
| `2026-08-15 15:18:42` | `cowrie.command.input` |
| `2026-08-15 15:18:42` | `cowrie.log.closed` |
| `2026-08-15 15:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-281d96ea9a79

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:18 |
| **Last Seen** | 2026-08-15 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:18:49` | `cowrie.session.connect` |
| `2026-08-15 15:18:49` | `cowrie.client.version` |
| `2026-08-15 15:18:49` | `cowrie.client.kex` |
| `2026-08-15 15:18:50` | `cowrie.login.success` |
| `2026-08-15 15:18:51` | `cowrie.session.params` |
| `2026-08-15 15:18:51` | `cowrie.command.input` |
| `2026-08-15 15:18:51` | `cowrie.log.closed` |
| `2026-08-15 15:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd6b33f6e616

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:18 |
| **Last Seen** | 2026-08-15 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:18:58` | `cowrie.session.connect` |
| `2026-08-15 15:18:58` | `cowrie.client.version` |
| `2026-08-15 15:18:59` | `cowrie.client.kex` |
| `2026-08-15 15:18:59` | `cowrie.login.success` |
| `2026-08-15 15:19:00` | `cowrie.session.params` |
| `2026-08-15 15:19:00` | `cowrie.command.input` |
| `2026-08-15 15:19:00` | `cowrie.log.closed` |
| `2026-08-15 15:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65253ca67ae

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:19 |
| **Last Seen** | 2026-08-15 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:19:07` | `cowrie.session.connect` |
| `2026-08-15 15:19:07` | `cowrie.client.version` |
| `2026-08-15 15:19:07` | `cowrie.client.kex` |
| `2026-08-15 15:19:07` | `cowrie.login.success` |
| `2026-08-15 15:19:08` | `cowrie.session.params` |
| `2026-08-15 15:19:08` | `cowrie.command.input` |
| `2026-08-15 15:19:08` | `cowrie.log.closed` |
| `2026-08-15 15:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72cc840a5b57

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:19 |
| **Last Seen** | 2026-08-15 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:19:14` | `cowrie.session.connect` |
| `2026-08-15 15:19:14` | `cowrie.client.version` |
| `2026-08-15 15:19:14` | `cowrie.client.kex` |
| `2026-08-15 15:19:14` | `cowrie.login.success` |
| `2026-08-15 15:19:15` | `cowrie.session.params` |
| `2026-08-15 15:19:15` | `cowrie.command.input` |
| `2026-08-15 15:19:15` | `cowrie.log.closed` |
| `2026-08-15 15:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c030e513085

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:19 |
| **Last Seen** | 2026-08-15 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:19:21` | `cowrie.session.connect` |
| `2026-08-15 15:19:22` | `cowrie.client.version` |
| `2026-08-15 15:19:22` | `cowrie.client.kex` |
| `2026-08-15 15:19:22` | `cowrie.login.success` |
| `2026-08-15 15:19:23` | `cowrie.session.params` |
| `2026-08-15 15:19:23` | `cowrie.command.input` |
| `2026-08-15 15:19:23` | `cowrie.log.closed` |
| `2026-08-15 15:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1d5f0c6037

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:19 |
| **Last Seen** | 2026-08-15 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:19:31` | `cowrie.session.connect` |
| `2026-08-15 15:19:31` | `cowrie.client.version` |
| `2026-08-15 15:19:31` | `cowrie.client.kex` |
| `2026-08-15 15:19:31` | `cowrie.login.success` |
| `2026-08-15 15:19:32` | `cowrie.session.params` |
| `2026-08-15 15:19:32` | `cowrie.command.input` |
| `2026-08-15 15:19:32` | `cowrie.log.closed` |
| `2026-08-15 15:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d47a1bda355

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:19 |
| **Last Seen** | 2026-08-15 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:19:39` | `cowrie.session.connect` |
| `2026-08-15 15:19:39` | `cowrie.client.version` |
| `2026-08-15 15:19:39` | `cowrie.client.kex` |
| `2026-08-15 15:19:40` | `cowrie.login.success` |
| `2026-08-15 15:19:40` | `cowrie.session.params` |
| `2026-08-15 15:19:40` | `cowrie.command.input` |
| `2026-08-15 15:19:41` | `cowrie.log.closed` |
| `2026-08-15 15:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d631b7d102f8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:19 |
| **Last Seen** | 2026-08-15 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:19:47` | `cowrie.session.connect` |
| `2026-08-15 15:19:47` | `cowrie.client.version` |
| `2026-08-15 15:19:47` | `cowrie.client.kex` |
| `2026-08-15 15:19:47` | `cowrie.login.success` |
| `2026-08-15 15:19:48` | `cowrie.session.params` |
| `2026-08-15 15:19:48` | `cowrie.command.input` |
| `2026-08-15 15:19:48` | `cowrie.log.closed` |
| `2026-08-15 15:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17074b80bdf7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:19 |
| **Last Seen** | 2026-08-15 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:19:54` | `cowrie.session.connect` |
| `2026-08-15 15:19:54` | `cowrie.client.version` |
| `2026-08-15 15:19:54` | `cowrie.client.kex` |
| `2026-08-15 15:19:54` | `cowrie.login.success` |
| `2026-08-15 15:19:55` | `cowrie.session.params` |
| `2026-08-15 15:19:55` | `cowrie.command.input` |
| `2026-08-15 15:19:56` | `cowrie.log.closed` |
| `2026-08-15 15:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05762635a0d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:20 |
| **Last Seen** | 2026-08-15 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:20:00` | `cowrie.session.connect` |
| `2026-08-15 15:20:00` | `cowrie.client.version` |
| `2026-08-15 15:20:00` | `cowrie.client.kex` |
| `2026-08-15 15:20:01` | `cowrie.login.success` |
| `2026-08-15 15:20:01` | `cowrie.session.params` |
| `2026-08-15 15:20:01` | `cowrie.command.input` |
| `2026-08-15 15:20:02` | `cowrie.log.closed` |
| `2026-08-15 15:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d46a9ec3ad

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:20 |
| **Last Seen** | 2026-08-15 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:20:06` | `cowrie.session.connect` |
| `2026-08-15 15:20:06` | `cowrie.client.version` |
| `2026-08-15 15:20:06` | `cowrie.client.kex` |
| `2026-08-15 15:20:07` | `cowrie.login.success` |
| `2026-08-15 15:20:07` | `cowrie.session.params` |
| `2026-08-15 15:20:07` | `cowrie.command.input` |
| `2026-08-15 15:20:07` | `cowrie.log.closed` |
| `2026-08-15 15:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b79a3e7aef8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:20 |
| **Last Seen** | 2026-08-15 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:20:12` | `cowrie.session.connect` |
| `2026-08-15 15:20:12` | `cowrie.client.version` |
| `2026-08-15 15:20:12` | `cowrie.client.kex` |
| `2026-08-15 15:20:13` | `cowrie.login.success` |
| `2026-08-15 15:20:14` | `cowrie.session.params` |
| `2026-08-15 15:20:14` | `cowrie.command.input` |
| `2026-08-15 15:20:14` | `cowrie.log.closed` |
| `2026-08-15 15:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dee1aa62d63

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:20 |
| **Last Seen** | 2026-08-15 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:20:19` | `cowrie.session.connect` |
| `2026-08-15 15:20:19` | `cowrie.client.version` |
| `2026-08-15 15:20:19` | `cowrie.client.kex` |
| `2026-08-15 15:20:19` | `cowrie.login.success` |
| `2026-08-15 15:20:20` | `cowrie.session.params` |
| `2026-08-15 15:20:20` | `cowrie.command.input` |
| `2026-08-15 15:20:20` | `cowrie.log.closed` |
| `2026-08-15 15:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-583465b8335b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:20 |
| **Last Seen** | 2026-08-15 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:20:25` | `cowrie.session.connect` |
| `2026-08-15 15:20:25` | `cowrie.client.version` |
| `2026-08-15 15:20:25` | `cowrie.client.kex` |
| `2026-08-15 15:20:25` | `cowrie.login.success` |
| `2026-08-15 15:20:26` | `cowrie.session.params` |
| `2026-08-15 15:20:26` | `cowrie.command.input` |
| `2026-08-15 15:20:26` | `cowrie.log.closed` |
| `2026-08-15 15:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a05d2869e9e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:20 |
| **Last Seen** | 2026-08-15 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:20:31` | `cowrie.session.connect` |
| `2026-08-15 15:20:31` | `cowrie.client.version` |
| `2026-08-15 15:20:31` | `cowrie.client.kex` |
| `2026-08-15 15:20:31` | `cowrie.login.success` |
| `2026-08-15 15:20:32` | `cowrie.session.params` |
| `2026-08-15 15:20:32` | `cowrie.command.input` |
| `2026-08-15 15:20:33` | `cowrie.log.closed` |
| `2026-08-15 15:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-000d4e08a65b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:20 |
| **Last Seen** | 2026-08-15 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:20:37` | `cowrie.session.connect` |
| `2026-08-15 15:20:37` | `cowrie.client.version` |
| `2026-08-15 15:20:37` | `cowrie.client.kex` |
| `2026-08-15 15:20:38` | `cowrie.login.success` |
| `2026-08-15 15:20:38` | `cowrie.session.params` |
| `2026-08-15 15:20:38` | `cowrie.command.input` |
| `2026-08-15 15:20:39` | `cowrie.log.closed` |
| `2026-08-15 15:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e4d20bed8d4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:20 |
| **Last Seen** | 2026-08-15 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:20:44` | `cowrie.session.connect` |
| `2026-08-15 15:20:44` | `cowrie.client.version` |
| `2026-08-15 15:20:44` | `cowrie.client.kex` |
| `2026-08-15 15:20:44` | `cowrie.login.success` |
| `2026-08-15 15:20:45` | `cowrie.session.params` |
| `2026-08-15 15:20:45` | `cowrie.command.input` |
| `2026-08-15 15:20:45` | `cowrie.log.closed` |
| `2026-08-15 15:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71478412f592

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:20 |
| **Last Seen** | 2026-08-15 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:20:51` | `cowrie.session.connect` |
| `2026-08-15 15:20:51` | `cowrie.client.version` |
| `2026-08-15 15:20:51` | `cowrie.client.kex` |
| `2026-08-15 15:20:51` | `cowrie.login.success` |
| `2026-08-15 15:20:52` | `cowrie.session.params` |
| `2026-08-15 15:20:52` | `cowrie.command.input` |
| `2026-08-15 15:20:52` | `cowrie.log.closed` |
| `2026-08-15 15:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9120f0f941a0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:20 |
| **Last Seen** | 2026-08-15 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:20:57` | `cowrie.session.connect` |
| `2026-08-15 15:20:57` | `cowrie.client.version` |
| `2026-08-15 15:20:57` | `cowrie.client.kex` |
| `2026-08-15 15:20:57` | `cowrie.login.success` |
| `2026-08-15 15:20:58` | `cowrie.session.params` |
| `2026-08-15 15:20:58` | `cowrie.command.input` |
| `2026-08-15 15:20:58` | `cowrie.log.closed` |
| `2026-08-15 15:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf383b03340

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:03` | `cowrie.session.connect` |
| `2026-08-15 15:21:03` | `cowrie.client.version` |
| `2026-08-15 15:21:03` | `cowrie.client.kex` |
| `2026-08-15 15:21:04` | `cowrie.login.success` |
| `2026-08-15 15:21:04` | `cowrie.session.params` |
| `2026-08-15 15:21:04` | `cowrie.command.input` |
| `2026-08-15 15:21:05` | `cowrie.log.closed` |
| `2026-08-15 15:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c55c7e189b6e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:09` | `cowrie.session.connect` |
| `2026-08-15 15:21:09` | `cowrie.client.version` |
| `2026-08-15 15:21:09` | `cowrie.client.kex` |
| `2026-08-15 15:21:10` | `cowrie.login.success` |
| `2026-08-15 15:21:10` | `cowrie.session.params` |
| `2026-08-15 15:21:10` | `cowrie.command.input` |
| `2026-08-15 15:21:11` | `cowrie.log.closed` |
| `2026-08-15 15:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e57b7cc7074

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:15` | `cowrie.session.connect` |
| `2026-08-15 15:21:15` | `cowrie.client.version` |
| `2026-08-15 15:21:15` | `cowrie.client.kex` |
| `2026-08-15 15:21:15` | `cowrie.login.success` |
| `2026-08-15 15:21:16` | `cowrie.session.params` |
| `2026-08-15 15:21:16` | `cowrie.command.input` |
| `2026-08-15 15:21:16` | `cowrie.log.closed` |
| `2026-08-15 15:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5bbfa7cd35

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:18` | `cowrie.session.connect` |
| `2026-08-15 15:21:18` | `cowrie.client.version` |
| `2026-08-15 15:21:18` | `cowrie.client.kex` |
| `2026-08-15 15:21:19` | `cowrie.login.success` |
| `2026-08-15 15:21:20` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deea6cbd4328

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:21` | `cowrie.session.connect` |
| `2026-08-15 15:21:21` | `cowrie.client.version` |
| `2026-08-15 15:21:22` | `cowrie.client.kex` |
| `2026-08-15 15:21:22` | `cowrie.login.success` |
| `2026-08-15 15:21:23` | `cowrie.session.params` |
| `2026-08-15 15:21:23` | `cowrie.command.input` |
| `2026-08-15 15:21:23` | `cowrie.log.closed` |
| `2026-08-15 15:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d021fd74226

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:27` | `cowrie.session.connect` |
| `2026-08-15 15:21:27` | `cowrie.client.version` |
| `2026-08-15 15:21:28` | `cowrie.client.kex` |
| `2026-08-15 15:21:28` | `cowrie.login.success` |
| `2026-08-15 15:21:29` | `cowrie.session.params` |
| `2026-08-15 15:21:29` | `cowrie.command.input` |
| `2026-08-15 15:21:29` | `cowrie.log.closed` |
| `2026-08-15 15:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9dcb4266677

| Field | Detail |
|---|---|
| **Source IP** | `180.76.52[.]146` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:30` | `cowrie.session.connect` |
| `2026-08-15 15:21:30` | `cowrie.client.version` |
| `2026-08-15 15:21:30` | `cowrie.client.kex` |
| `2026-08-15 15:21:32` | `cowrie.login.success` |
| `2026-08-15 15:21:33` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.52[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.76.52[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add60de21b0e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:34` | `cowrie.session.connect` |
| `2026-08-15 15:21:34` | `cowrie.client.version` |
| `2026-08-15 15:21:34` | `cowrie.client.kex` |
| `2026-08-15 15:21:34` | `cowrie.login.success` |
| `2026-08-15 15:21:35` | `cowrie.session.params` |
| `2026-08-15 15:21:35` | `cowrie.command.input` |
| `2026-08-15 15:21:35` | `cowrie.log.closed` |
| `2026-08-15 15:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c45605b64d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:40` | `cowrie.session.connect` |
| `2026-08-15 15:21:40` | `cowrie.client.version` |
| `2026-08-15 15:21:40` | `cowrie.client.kex` |
| `2026-08-15 15:21:41` | `cowrie.login.success` |
| `2026-08-15 15:21:42` | `cowrie.session.params` |
| `2026-08-15 15:21:42` | `cowrie.command.input` |
| `2026-08-15 15:21:42` | `cowrie.log.closed` |
| `2026-08-15 15:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-353fe5fd2551

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:46` | `cowrie.session.connect` |
| `2026-08-15 15:21:46` | `cowrie.client.version` |
| `2026-08-15 15:21:47` | `cowrie.client.kex` |
| `2026-08-15 15:21:47` | `cowrie.login.success` |
| `2026-08-15 15:21:48` | `cowrie.session.params` |
| `2026-08-15 15:21:48` | `cowrie.command.input` |
| `2026-08-15 15:21:48` | `cowrie.log.closed` |
| `2026-08-15 15:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4e8ee37c900

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:21 |
| **Last Seen** | 2026-08-15 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:21:53` | `cowrie.session.connect` |
| `2026-08-15 15:21:53` | `cowrie.client.version` |
| `2026-08-15 15:21:53` | `cowrie.client.kex` |
| `2026-08-15 15:21:53` | `cowrie.login.success` |
| `2026-08-15 15:21:54` | `cowrie.session.params` |
| `2026-08-15 15:21:54` | `cowrie.command.input` |
| `2026-08-15 15:21:54` | `cowrie.log.closed` |
| `2026-08-15 15:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-037e0d23b5a4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:22 |
| **Last Seen** | 2026-08-15 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:22:00` | `cowrie.session.connect` |
| `2026-08-15 15:22:00` | `cowrie.client.version` |
| `2026-08-15 15:22:00` | `cowrie.client.kex` |
| `2026-08-15 15:22:00` | `cowrie.login.success` |
| `2026-08-15 15:22:01` | `cowrie.session.params` |
| `2026-08-15 15:22:01` | `cowrie.command.input` |
| `2026-08-15 15:22:02` | `cowrie.log.closed` |
| `2026-08-15 15:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed036bc9211

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:22 |
| **Last Seen** | 2026-08-15 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:22:10` | `cowrie.session.connect` |
| `2026-08-15 15:22:10` | `cowrie.client.version` |
| `2026-08-15 15:22:10` | `cowrie.client.kex` |
| `2026-08-15 15:22:11` | `cowrie.login.success` |
| `2026-08-15 15:22:12` | `cowrie.session.params` |
| `2026-08-15 15:22:12` | `cowrie.command.input` |
| `2026-08-15 15:22:12` | `cowrie.log.closed` |
| `2026-08-15 15:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a086cb4d290

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:22 |
| **Last Seen** | 2026-08-15 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:22:19` | `cowrie.session.connect` |
| `2026-08-15 15:22:19` | `cowrie.client.version` |
| `2026-08-15 15:22:19` | `cowrie.client.kex` |
| `2026-08-15 15:22:19` | `cowrie.login.success` |
| `2026-08-15 15:22:20` | `cowrie.session.params` |
| `2026-08-15 15:22:20` | `cowrie.command.input` |
| `2026-08-15 15:22:20` | `cowrie.log.closed` |
| `2026-08-15 15:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcdb4fe2c2b3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:22 |
| **Last Seen** | 2026-08-15 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:22:26` | `cowrie.session.connect` |
| `2026-08-15 15:22:26` | `cowrie.client.version` |
| `2026-08-15 15:22:27` | `cowrie.client.kex` |
| `2026-08-15 15:22:27` | `cowrie.login.success` |
| `2026-08-15 15:22:28` | `cowrie.session.params` |
| `2026-08-15 15:22:28` | `cowrie.command.input` |
| `2026-08-15 15:22:28` | `cowrie.log.closed` |
| `2026-08-15 15:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a75a1311cce8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:22 |
| **Last Seen** | 2026-08-15 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:22:33` | `cowrie.session.connect` |
| `2026-08-15 15:22:33` | `cowrie.client.version` |
| `2026-08-15 15:22:34` | `cowrie.client.kex` |
| `2026-08-15 15:22:34` | `cowrie.login.success` |
| `2026-08-15 15:22:35` | `cowrie.session.params` |
| `2026-08-15 15:22:35` | `cowrie.command.input` |
| `2026-08-15 15:22:35` | `cowrie.log.closed` |
| `2026-08-15 15:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e2edba7f968

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:22 |
| **Last Seen** | 2026-08-15 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:22:40` | `cowrie.session.connect` |
| `2026-08-15 15:22:40` | `cowrie.client.version` |
| `2026-08-15 15:22:40` | `cowrie.client.kex` |
| `2026-08-15 15:22:41` | `cowrie.login.success` |
| `2026-08-15 15:22:42` | `cowrie.session.params` |
| `2026-08-15 15:22:42` | `cowrie.command.input` |
| `2026-08-15 15:22:42` | `cowrie.log.closed` |
| `2026-08-15 15:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68ba65140e4f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:22 |
| **Last Seen** | 2026-08-15 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:22:47` | `cowrie.session.connect` |
| `2026-08-15 15:22:47` | `cowrie.client.version` |
| `2026-08-15 15:22:47` | `cowrie.client.kex` |
| `2026-08-15 15:22:47` | `cowrie.login.success` |
| `2026-08-15 15:22:48` | `cowrie.session.params` |
| `2026-08-15 15:22:48` | `cowrie.command.input` |
| `2026-08-15 15:22:48` | `cowrie.log.closed` |
| `2026-08-15 15:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e3defcc8cf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:22 |
| **Last Seen** | 2026-08-15 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:22:55` | `cowrie.session.connect` |
| `2026-08-15 15:22:55` | `cowrie.client.version` |
| `2026-08-15 15:22:55` | `cowrie.client.kex` |
| `2026-08-15 15:22:55` | `cowrie.login.success` |
| `2026-08-15 15:22:56` | `cowrie.session.params` |
| `2026-08-15 15:22:56` | `cowrie.command.input` |
| `2026-08-15 15:22:56` | `cowrie.log.closed` |
| `2026-08-15 15:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d29115c600f6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:23 |
| **Last Seen** | 2026-08-15 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:23:02` | `cowrie.session.connect` |
| `2026-08-15 15:23:02` | `cowrie.client.version` |
| `2026-08-15 15:23:02` | `cowrie.client.kex` |
| `2026-08-15 15:23:02` | `cowrie.login.success` |
| `2026-08-15 15:23:03` | `cowrie.session.params` |
| `2026-08-15 15:23:03` | `cowrie.command.input` |
| `2026-08-15 15:23:03` | `cowrie.log.closed` |
| `2026-08-15 15:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a3188129e84

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:23 |
| **Last Seen** | 2026-08-15 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:23:09` | `cowrie.session.connect` |
| `2026-08-15 15:23:09` | `cowrie.client.version` |
| `2026-08-15 15:23:09` | `cowrie.client.kex` |
| `2026-08-15 15:23:09` | `cowrie.login.success` |
| `2026-08-15 15:23:10` | `cowrie.session.params` |
| `2026-08-15 15:23:10` | `cowrie.command.input` |
| `2026-08-15 15:23:10` | `cowrie.log.closed` |
| `2026-08-15 15:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9903c6f705

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:23 |
| **Last Seen** | 2026-08-15 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:23:16` | `cowrie.session.connect` |
| `2026-08-15 15:23:16` | `cowrie.client.version` |
| `2026-08-15 15:23:16` | `cowrie.client.kex` |
| `2026-08-15 15:23:16` | `cowrie.login.success` |
| `2026-08-15 15:23:17` | `cowrie.session.params` |
| `2026-08-15 15:23:17` | `cowrie.command.input` |
| `2026-08-15 15:23:17` | `cowrie.log.closed` |
| `2026-08-15 15:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1990c528d138

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:23 |
| **Last Seen** | 2026-08-15 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:23:21` | `cowrie.session.connect` |
| `2026-08-15 15:23:21` | `cowrie.client.version` |
| `2026-08-15 15:23:21` | `cowrie.client.kex` |
| `2026-08-15 15:23:22` | `cowrie.login.success` |
| `2026-08-15 15:23:23` | `cowrie.session.params` |
| `2026-08-15 15:23:23` | `cowrie.command.input` |
| `2026-08-15 15:23:23` | `cowrie.log.closed` |
| `2026-08-15 15:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeaa84da12f6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:23 |
| **Last Seen** | 2026-08-15 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:23:28` | `cowrie.session.connect` |
| `2026-08-15 15:23:28` | `cowrie.client.version` |
| `2026-08-15 15:23:28` | `cowrie.client.kex` |
| `2026-08-15 15:23:29` | `cowrie.login.success` |
| `2026-08-15 15:23:29` | `cowrie.session.params` |
| `2026-08-15 15:23:29` | `cowrie.command.input` |
| `2026-08-15 15:23:29` | `cowrie.log.closed` |
| `2026-08-15 15:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb76f39499c8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:23 |
| **Last Seen** | 2026-08-15 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:23:37` | `cowrie.session.connect` |
| `2026-08-15 15:23:37` | `cowrie.client.version` |
| `2026-08-15 15:23:37` | `cowrie.client.kex` |
| `2026-08-15 15:23:37` | `cowrie.login.success` |
| `2026-08-15 15:23:38` | `cowrie.session.params` |
| `2026-08-15 15:23:38` | `cowrie.command.input` |
| `2026-08-15 15:23:38` | `cowrie.log.closed` |
| `2026-08-15 15:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def1fd915dc1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:23 |
| **Last Seen** | 2026-08-15 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:23:45` | `cowrie.session.connect` |
| `2026-08-15 15:23:45` | `cowrie.client.version` |
| `2026-08-15 15:23:45` | `cowrie.client.kex` |
| `2026-08-15 15:23:45` | `cowrie.login.success` |
| `2026-08-15 15:23:46` | `cowrie.session.params` |
| `2026-08-15 15:23:46` | `cowrie.command.input` |
| `2026-08-15 15:23:46` | `cowrie.log.closed` |
| `2026-08-15 15:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0260b235b89a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:23 |
| **Last Seen** | 2026-08-15 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:23:53` | `cowrie.session.connect` |
| `2026-08-15 15:23:53` | `cowrie.client.version` |
| `2026-08-15 15:23:53` | `cowrie.client.kex` |
| `2026-08-15 15:23:53` | `cowrie.login.success` |
| `2026-08-15 15:23:54` | `cowrie.session.params` |
| `2026-08-15 15:23:54` | `cowrie.command.input` |
| `2026-08-15 15:23:54` | `cowrie.log.closed` |
| `2026-08-15 15:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660371fd58a9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:24 |
| **Last Seen** | 2026-08-15 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:24:01` | `cowrie.session.connect` |
| `2026-08-15 15:24:01` | `cowrie.client.version` |
| `2026-08-15 15:24:01` | `cowrie.client.kex` |
| `2026-08-15 15:24:01` | `cowrie.login.success` |
| `2026-08-15 15:24:02` | `cowrie.session.params` |
| `2026-08-15 15:24:02` | `cowrie.command.input` |
| `2026-08-15 15:24:03` | `cowrie.log.closed` |
| `2026-08-15 15:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddcabca85b0b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:24 |
| **Last Seen** | 2026-08-15 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:24:10` | `cowrie.session.connect` |
| `2026-08-15 15:24:10` | `cowrie.client.version` |
| `2026-08-15 15:24:10` | `cowrie.client.kex` |
| `2026-08-15 15:24:10` | `cowrie.login.success` |
| `2026-08-15 15:24:11` | `cowrie.session.params` |
| `2026-08-15 15:24:11` | `cowrie.command.input` |
| `2026-08-15 15:24:11` | `cowrie.log.closed` |
| `2026-08-15 15:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf4ea2304c2

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 15:24 |
| **Last Seen** | 2026-08-15 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:24:14` | `cowrie.session.connect` |
| `2026-08-15 15:24:14` | `cowrie.client.version` |
| `2026-08-15 15:24:14` | `cowrie.client.kex` |
| `2026-08-15 15:24:14` | `cowrie.login.success` |
| `2026-08-15 15:24:15` | `cowrie.session.params` |
| `2026-08-15 15:24:15` | `cowrie.command.input` |
| `2026-08-15 15:24:16` | `cowrie.log.closed` |
| `2026-08-15 15:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2a9ee98226

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:24 |
| **Last Seen** | 2026-08-15 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:24:18` | `cowrie.session.connect` |
| `2026-08-15 15:24:18` | `cowrie.client.version` |
| `2026-08-15 15:24:18` | `cowrie.client.kex` |
| `2026-08-15 15:24:18` | `cowrie.login.success` |
| `2026-08-15 15:24:19` | `cowrie.session.params` |
| `2026-08-15 15:24:19` | `cowrie.command.input` |
| `2026-08-15 15:24:19` | `cowrie.log.closed` |
| `2026-08-15 15:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa99924f9c26

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:24 |
| **Last Seen** | 2026-08-15 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:24:26` | `cowrie.session.connect` |
| `2026-08-15 15:24:26` | `cowrie.client.version` |
| `2026-08-15 15:24:26` | `cowrie.client.kex` |
| `2026-08-15 15:24:26` | `cowrie.login.success` |
| `2026-08-15 15:24:27` | `cowrie.session.params` |
| `2026-08-15 15:24:27` | `cowrie.command.input` |
| `2026-08-15 15:24:27` | `cowrie.log.closed` |
| `2026-08-15 15:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f58e881573

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:24 |
| **Last Seen** | 2026-08-15 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:24:34` | `cowrie.session.connect` |
| `2026-08-15 15:24:34` | `cowrie.client.version` |
| `2026-08-15 15:24:34` | `cowrie.client.kex` |
| `2026-08-15 15:24:34` | `cowrie.login.success` |
| `2026-08-15 15:24:35` | `cowrie.session.params` |
| `2026-08-15 15:24:35` | `cowrie.command.input` |
| `2026-08-15 15:24:36` | `cowrie.log.closed` |
| `2026-08-15 15:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd46e10d869

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:24 |
| **Last Seen** | 2026-08-15 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:24:43` | `cowrie.session.connect` |
| `2026-08-15 15:24:43` | `cowrie.client.version` |
| `2026-08-15 15:24:43` | `cowrie.client.kex` |
| `2026-08-15 15:24:43` | `cowrie.login.success` |
| `2026-08-15 15:24:44` | `cowrie.session.params` |
| `2026-08-15 15:24:44` | `cowrie.command.input` |
| `2026-08-15 15:24:44` | `cowrie.log.closed` |
| `2026-08-15 15:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b20cc4e8a050

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:24 |
| **Last Seen** | 2026-08-15 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:24:51` | `cowrie.session.connect` |
| `2026-08-15 15:24:51` | `cowrie.client.version` |
| `2026-08-15 15:24:51` | `cowrie.client.kex` |
| `2026-08-15 15:24:52` | `cowrie.login.success` |
| `2026-08-15 15:24:52` | `cowrie.session.params` |
| `2026-08-15 15:24:52` | `cowrie.command.input` |
| `2026-08-15 15:24:52` | `cowrie.log.closed` |
| `2026-08-15 15:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d7e53f77bf9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:25 |
| **Last Seen** | 2026-08-15 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:25:00` | `cowrie.session.connect` |
| `2026-08-15 15:25:00` | `cowrie.client.version` |
| `2026-08-15 15:25:00` | `cowrie.client.kex` |
| `2026-08-15 15:25:00` | `cowrie.login.success` |
| `2026-08-15 15:25:01` | `cowrie.session.params` |
| `2026-08-15 15:25:01` | `cowrie.command.input` |
| `2026-08-15 15:25:01` | `cowrie.log.closed` |
| `2026-08-15 15:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8543f66b15e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:25 |
| **Last Seen** | 2026-08-15 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:25:08` | `cowrie.session.connect` |
| `2026-08-15 15:25:08` | `cowrie.client.version` |
| `2026-08-15 15:25:08` | `cowrie.client.kex` |
| `2026-08-15 15:25:09` | `cowrie.login.success` |
| `2026-08-15 15:25:10` | `cowrie.session.params` |
| `2026-08-15 15:25:10` | `cowrie.command.input` |
| `2026-08-15 15:25:10` | `cowrie.log.closed` |
| `2026-08-15 15:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74176821956e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:25 |
| **Last Seen** | 2026-08-15 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:25:17` | `cowrie.session.connect` |
| `2026-08-15 15:25:17` | `cowrie.client.version` |
| `2026-08-15 15:25:17` | `cowrie.client.kex` |
| `2026-08-15 15:25:18` | `cowrie.login.success` |
| `2026-08-15 15:25:19` | `cowrie.session.params` |
| `2026-08-15 15:25:19` | `cowrie.command.input` |
| `2026-08-15 15:25:19` | `cowrie.log.closed` |
| `2026-08-15 15:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b9e794cfb9a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:25 |
| **Last Seen** | 2026-08-15 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:25:26` | `cowrie.session.connect` |
| `2026-08-15 15:25:26` | `cowrie.client.version` |
| `2026-08-15 15:25:26` | `cowrie.client.kex` |
| `2026-08-15 15:25:26` | `cowrie.login.success` |
| `2026-08-15 15:25:27` | `cowrie.session.params` |
| `2026-08-15 15:25:27` | `cowrie.command.input` |
| `2026-08-15 15:25:27` | `cowrie.log.closed` |
| `2026-08-15 15:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69f26dc813b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:25 |
| **Last Seen** | 2026-08-15 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:25:34` | `cowrie.session.connect` |
| `2026-08-15 15:25:34` | `cowrie.client.version` |
| `2026-08-15 15:25:34` | `cowrie.client.kex` |
| `2026-08-15 15:25:34` | `cowrie.login.success` |
| `2026-08-15 15:25:35` | `cowrie.session.params` |
| `2026-08-15 15:25:35` | `cowrie.command.input` |
| `2026-08-15 15:25:35` | `cowrie.log.closed` |
| `2026-08-15 15:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fcfe184c1c2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:25 |
| **Last Seen** | 2026-08-15 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:25:42` | `cowrie.session.connect` |
| `2026-08-15 15:25:42` | `cowrie.client.version` |
| `2026-08-15 15:25:42` | `cowrie.client.kex` |
| `2026-08-15 15:25:42` | `cowrie.login.success` |
| `2026-08-15 15:25:43` | `cowrie.session.params` |
| `2026-08-15 15:25:43` | `cowrie.command.input` |
| `2026-08-15 15:25:43` | `cowrie.log.closed` |
| `2026-08-15 15:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-130594e0d112

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:25 |
| **Last Seen** | 2026-08-15 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:25:51` | `cowrie.session.connect` |
| `2026-08-15 15:25:51` | `cowrie.client.version` |
| `2026-08-15 15:25:51` | `cowrie.client.kex` |
| `2026-08-15 15:25:51` | `cowrie.login.success` |
| `2026-08-15 15:25:52` | `cowrie.session.params` |
| `2026-08-15 15:25:52` | `cowrie.command.input` |
| `2026-08-15 15:25:52` | `cowrie.log.closed` |
| `2026-08-15 15:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-188639d4e45f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:25 |
| **Last Seen** | 2026-08-15 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:25:59` | `cowrie.session.connect` |
| `2026-08-15 15:25:59` | `cowrie.client.version` |
| `2026-08-15 15:25:59` | `cowrie.client.kex` |
| `2026-08-15 15:25:59` | `cowrie.login.success` |
| `2026-08-15 15:26:00` | `cowrie.session.params` |
| `2026-08-15 15:26:00` | `cowrie.command.input` |
| `2026-08-15 15:26:00` | `cowrie.log.closed` |
| `2026-08-15 15:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af909dbe2806

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:26 |
| **Last Seen** | 2026-08-15 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:26:07` | `cowrie.session.connect` |
| `2026-08-15 15:26:08` | `cowrie.client.version` |
| `2026-08-15 15:26:08` | `cowrie.client.kex` |
| `2026-08-15 15:26:08` | `cowrie.login.success` |
| `2026-08-15 15:26:09` | `cowrie.session.params` |
| `2026-08-15 15:26:09` | `cowrie.command.input` |
| `2026-08-15 15:26:09` | `cowrie.log.closed` |
| `2026-08-15 15:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02df49be0fd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:26 |
| **Last Seen** | 2026-08-15 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:26:16` | `cowrie.session.connect` |
| `2026-08-15 15:26:16` | `cowrie.client.version` |
| `2026-08-15 15:26:16` | `cowrie.client.kex` |
| `2026-08-15 15:26:16` | `cowrie.login.success` |
| `2026-08-15 15:26:17` | `cowrie.session.params` |
| `2026-08-15 15:26:17` | `cowrie.command.input` |
| `2026-08-15 15:26:17` | `cowrie.log.closed` |
| `2026-08-15 15:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34cea7172d0c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:26 |
| **Last Seen** | 2026-08-15 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:26:25` | `cowrie.session.connect` |
| `2026-08-15 15:26:25` | `cowrie.client.version` |
| `2026-08-15 15:26:25` | `cowrie.client.kex` |
| `2026-08-15 15:26:25` | `cowrie.login.success` |
| `2026-08-15 15:26:26` | `cowrie.session.params` |
| `2026-08-15 15:26:26` | `cowrie.command.input` |
| `2026-08-15 15:26:26` | `cowrie.log.closed` |
| `2026-08-15 15:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bc45c2afdb5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:26 |
| **Last Seen** | 2026-08-15 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:26:33` | `cowrie.session.connect` |
| `2026-08-15 15:26:33` | `cowrie.client.version` |
| `2026-08-15 15:26:33` | `cowrie.client.kex` |
| `2026-08-15 15:26:34` | `cowrie.login.success` |
| `2026-08-15 15:26:34` | `cowrie.session.params` |
| `2026-08-15 15:26:34` | `cowrie.command.input` |
| `2026-08-15 15:26:35` | `cowrie.log.closed` |
| `2026-08-15 15:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d9a49daf5cd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:26 |
| **Last Seen** | 2026-08-15 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:26:41` | `cowrie.session.connect` |
| `2026-08-15 15:26:41` | `cowrie.client.version` |
| `2026-08-15 15:26:41` | `cowrie.client.kex` |
| `2026-08-15 15:26:41` | `cowrie.login.success` |
| `2026-08-15 15:26:43` | `cowrie.session.params` |
| `2026-08-15 15:26:43` | `cowrie.command.input` |
| `2026-08-15 15:26:43` | `cowrie.log.closed` |
| `2026-08-15 15:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-832dc5acce4a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:26 |
| **Last Seen** | 2026-08-15 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:26:50` | `cowrie.session.connect` |
| `2026-08-15 15:26:50` | `cowrie.client.version` |
| `2026-08-15 15:26:50` | `cowrie.client.kex` |
| `2026-08-15 15:26:50` | `cowrie.login.success` |
| `2026-08-15 15:26:51` | `cowrie.session.params` |
| `2026-08-15 15:26:51` | `cowrie.command.input` |
| `2026-08-15 15:26:51` | `cowrie.log.closed` |
| `2026-08-15 15:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4965e551b08

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:26 |
| **Last Seen** | 2026-08-15 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:26:58` | `cowrie.session.connect` |
| `2026-08-15 15:26:58` | `cowrie.client.version` |
| `2026-08-15 15:26:58` | `cowrie.client.kex` |
| `2026-08-15 15:26:58` | `cowrie.login.success` |
| `2026-08-15 15:26:59` | `cowrie.session.params` |
| `2026-08-15 15:26:59` | `cowrie.command.input` |
| `2026-08-15 15:26:59` | `cowrie.log.closed` |
| `2026-08-15 15:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d7dd4931e1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:27 |
| **Last Seen** | 2026-08-15 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:27:06` | `cowrie.session.connect` |
| `2026-08-15 15:27:06` | `cowrie.client.version` |
| `2026-08-15 15:27:06` | `cowrie.client.kex` |
| `2026-08-15 15:27:06` | `cowrie.login.success` |
| `2026-08-15 15:27:07` | `cowrie.session.params` |
| `2026-08-15 15:27:07` | `cowrie.command.input` |
| `2026-08-15 15:27:07` | `cowrie.log.closed` |
| `2026-08-15 15:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2459b743ef0e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:27 |
| **Last Seen** | 2026-08-15 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:27:14` | `cowrie.session.connect` |
| `2026-08-15 15:27:14` | `cowrie.client.version` |
| `2026-08-15 15:27:15` | `cowrie.client.kex` |
| `2026-08-15 15:27:15` | `cowrie.login.success` |
| `2026-08-15 15:27:16` | `cowrie.session.params` |
| `2026-08-15 15:27:16` | `cowrie.command.input` |
| `2026-08-15 15:27:16` | `cowrie.log.closed` |
| `2026-08-15 15:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2662b0359e18

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:27 |
| **Last Seen** | 2026-08-15 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:27:23` | `cowrie.session.connect` |
| `2026-08-15 15:27:23` | `cowrie.client.version` |
| `2026-08-15 15:27:23` | `cowrie.client.kex` |
| `2026-08-15 15:27:23` | `cowrie.login.success` |
| `2026-08-15 15:27:24` | `cowrie.session.params` |
| `2026-08-15 15:27:24` | `cowrie.command.input` |
| `2026-08-15 15:27:24` | `cowrie.log.closed` |
| `2026-08-15 15:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bae436ae8efc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:27 |
| **Last Seen** | 2026-08-15 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:27:31` | `cowrie.session.connect` |
| `2026-08-15 15:27:31` | `cowrie.client.version` |
| `2026-08-15 15:27:31` | `cowrie.client.kex` |
| `2026-08-15 15:27:31` | `cowrie.login.success` |
| `2026-08-15 15:27:32` | `cowrie.session.params` |
| `2026-08-15 15:27:32` | `cowrie.command.input` |
| `2026-08-15 15:27:32` | `cowrie.log.closed` |
| `2026-08-15 15:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2f93490da3f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:27 |
| **Last Seen** | 2026-08-15 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:27:39` | `cowrie.session.connect` |
| `2026-08-15 15:27:39` | `cowrie.client.version` |
| `2026-08-15 15:27:39` | `cowrie.client.kex` |
| `2026-08-15 15:27:39` | `cowrie.login.success` |
| `2026-08-15 15:27:40` | `cowrie.session.params` |
| `2026-08-15 15:27:40` | `cowrie.command.input` |
| `2026-08-15 15:27:40` | `cowrie.log.closed` |
| `2026-08-15 15:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-706b3e01d95c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:27 |
| **Last Seen** | 2026-08-15 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:27:47` | `cowrie.session.connect` |
| `2026-08-15 15:27:47` | `cowrie.client.version` |
| `2026-08-15 15:27:47` | `cowrie.client.kex` |
| `2026-08-15 15:27:48` | `cowrie.login.success` |
| `2026-08-15 15:27:48` | `cowrie.session.params` |
| `2026-08-15 15:27:48` | `cowrie.command.input` |
| `2026-08-15 15:27:48` | `cowrie.log.closed` |
| `2026-08-15 15:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d12ae7ca03

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:27 |
| **Last Seen** | 2026-08-15 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:27:56` | `cowrie.session.connect` |
| `2026-08-15 15:27:56` | `cowrie.client.version` |
| `2026-08-15 15:27:56` | `cowrie.client.kex` |
| `2026-08-15 15:27:56` | `cowrie.login.success` |
| `2026-08-15 15:27:57` | `cowrie.session.params` |
| `2026-08-15 15:27:57` | `cowrie.command.input` |
| `2026-08-15 15:27:57` | `cowrie.log.closed` |
| `2026-08-15 15:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639fe9ae894c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:28 |
| **Last Seen** | 2026-08-15 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:28:04` | `cowrie.session.connect` |
| `2026-08-15 15:28:04` | `cowrie.client.version` |
| `2026-08-15 15:28:04` | `cowrie.client.kex` |
| `2026-08-15 15:28:05` | `cowrie.login.success` |
| `2026-08-15 15:28:05` | `cowrie.session.params` |
| `2026-08-15 15:28:05` | `cowrie.command.input` |
| `2026-08-15 15:28:06` | `cowrie.log.closed` |
| `2026-08-15 15:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c6c701bf993

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:28 |
| **Last Seen** | 2026-08-15 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:28:13` | `cowrie.session.connect` |
| `2026-08-15 15:28:13` | `cowrie.client.version` |
| `2026-08-15 15:28:13` | `cowrie.client.kex` |
| `2026-08-15 15:28:13` | `cowrie.login.success` |
| `2026-08-15 15:28:14` | `cowrie.session.params` |
| `2026-08-15 15:28:14` | `cowrie.command.input` |
| `2026-08-15 15:28:14` | `cowrie.log.closed` |
| `2026-08-15 15:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d6f68b7bbf4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:28 |
| **Last Seen** | 2026-08-15 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:28:22` | `cowrie.session.connect` |
| `2026-08-15 15:28:22` | `cowrie.client.version` |
| `2026-08-15 15:28:22` | `cowrie.client.kex` |
| `2026-08-15 15:28:22` | `cowrie.login.success` |
| `2026-08-15 15:28:23` | `cowrie.session.params` |
| `2026-08-15 15:28:23` | `cowrie.command.input` |
| `2026-08-15 15:28:23` | `cowrie.log.closed` |
| `2026-08-15 15:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885b99d3cbb4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:28 |
| **Last Seen** | 2026-08-15 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:28:30` | `cowrie.session.connect` |
| `2026-08-15 15:28:30` | `cowrie.client.version` |
| `2026-08-15 15:28:30` | `cowrie.client.kex` |
| `2026-08-15 15:28:30` | `cowrie.login.success` |
| `2026-08-15 15:28:31` | `cowrie.session.params` |
| `2026-08-15 15:28:31` | `cowrie.command.input` |
| `2026-08-15 15:28:31` | `cowrie.log.closed` |
| `2026-08-15 15:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a2ef4349f56

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:28 |
| **Last Seen** | 2026-08-15 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:28:38` | `cowrie.session.connect` |
| `2026-08-15 15:28:38` | `cowrie.client.version` |
| `2026-08-15 15:28:38` | `cowrie.client.kex` |
| `2026-08-15 15:28:39` | `cowrie.login.success` |
| `2026-08-15 15:28:40` | `cowrie.session.params` |
| `2026-08-15 15:28:40` | `cowrie.command.input` |
| `2026-08-15 15:28:40` | `cowrie.log.closed` |
| `2026-08-15 15:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e54c27bc9aee

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:28 |
| **Last Seen** | 2026-08-15 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:28:46` | `cowrie.session.connect` |
| `2026-08-15 15:28:46` | `cowrie.client.version` |
| `2026-08-15 15:28:46` | `cowrie.client.kex` |
| `2026-08-15 15:28:47` | `cowrie.login.success` |
| `2026-08-15 15:28:48` | `cowrie.session.params` |
| `2026-08-15 15:28:48` | `cowrie.command.input` |
| `2026-08-15 15:28:48` | `cowrie.log.closed` |
| `2026-08-15 15:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1971b72d4712

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:28 |
| **Last Seen** | 2026-08-15 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:28:55` | `cowrie.session.connect` |
| `2026-08-15 15:28:55` | `cowrie.client.version` |
| `2026-08-15 15:28:55` | `cowrie.client.kex` |
| `2026-08-15 15:28:55` | `cowrie.login.success` |
| `2026-08-15 15:28:56` | `cowrie.session.params` |
| `2026-08-15 15:28:56` | `cowrie.command.input` |
| `2026-08-15 15:28:56` | `cowrie.log.closed` |
| `2026-08-15 15:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f24fafa66c25

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:29 |
| **Last Seen** | 2026-08-15 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:29:03` | `cowrie.session.connect` |
| `2026-08-15 15:29:03` | `cowrie.client.version` |
| `2026-08-15 15:29:03` | `cowrie.client.kex` |
| `2026-08-15 15:29:04` | `cowrie.login.success` |
| `2026-08-15 15:29:04` | `cowrie.session.params` |
| `2026-08-15 15:29:04` | `cowrie.command.input` |
| `2026-08-15 15:29:05` | `cowrie.log.closed` |
| `2026-08-15 15:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2a264cfe9a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:29 |
| **Last Seen** | 2026-08-15 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:29:11` | `cowrie.session.connect` |
| `2026-08-15 15:29:11` | `cowrie.client.version` |
| `2026-08-15 15:29:11` | `cowrie.client.kex` |
| `2026-08-15 15:29:12` | `cowrie.login.success` |
| `2026-08-15 15:29:13` | `cowrie.session.params` |
| `2026-08-15 15:29:13` | `cowrie.command.input` |
| `2026-08-15 15:29:13` | `cowrie.log.closed` |
| `2026-08-15 15:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b280773aff89

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:29 |
| **Last Seen** | 2026-08-15 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:29:19` | `cowrie.session.connect` |
| `2026-08-15 15:29:19` | `cowrie.client.version` |
| `2026-08-15 15:29:20` | `cowrie.client.kex` |
| `2026-08-15 15:29:20` | `cowrie.login.success` |
| `2026-08-15 15:29:21` | `cowrie.session.params` |
| `2026-08-15 15:29:21` | `cowrie.command.input` |
| `2026-08-15 15:29:21` | `cowrie.log.closed` |
| `2026-08-15 15:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477116aeef3d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:29 |
| **Last Seen** | 2026-08-15 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:29:28` | `cowrie.session.connect` |
| `2026-08-15 15:29:28` | `cowrie.client.version` |
| `2026-08-15 15:29:28` | `cowrie.client.kex` |
| `2026-08-15 15:29:29` | `cowrie.login.success` |
| `2026-08-15 15:29:30` | `cowrie.session.params` |
| `2026-08-15 15:29:30` | `cowrie.command.input` |
| `2026-08-15 15:29:30` | `cowrie.log.closed` |
| `2026-08-15 15:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d32a8ebc76a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:29 |
| **Last Seen** | 2026-08-15 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:29:37` | `cowrie.session.connect` |
| `2026-08-15 15:29:37` | `cowrie.client.version` |
| `2026-08-15 15:29:37` | `cowrie.client.kex` |
| `2026-08-15 15:29:38` | `cowrie.login.success` |
| `2026-08-15 15:29:39` | `cowrie.session.params` |
| `2026-08-15 15:29:39` | `cowrie.command.input` |
| `2026-08-15 15:29:39` | `cowrie.log.closed` |
| `2026-08-15 15:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73a1cbefc04c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:29 |
| **Last Seen** | 2026-08-15 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:29:45` | `cowrie.session.connect` |
| `2026-08-15 15:29:45` | `cowrie.client.version` |
| `2026-08-15 15:29:45` | `cowrie.client.kex` |
| `2026-08-15 15:29:46` | `cowrie.login.success` |
| `2026-08-15 15:29:46` | `cowrie.session.params` |
| `2026-08-15 15:29:46` | `cowrie.command.input` |
| `2026-08-15 15:29:47` | `cowrie.log.closed` |
| `2026-08-15 15:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b561a8aeb0d1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:29 |
| **Last Seen** | 2026-08-15 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:29:53` | `cowrie.session.connect` |
| `2026-08-15 15:29:53` | `cowrie.client.version` |
| `2026-08-15 15:29:54` | `cowrie.client.kex` |
| `2026-08-15 15:29:54` | `cowrie.login.success` |
| `2026-08-15 15:29:54` | `cowrie.session.params` |
| `2026-08-15 15:29:54` | `cowrie.command.input` |
| `2026-08-15 15:29:55` | `cowrie.log.closed` |
| `2026-08-15 15:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d36043013b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:30 |
| **Last Seen** | 2026-08-15 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:30:01` | `cowrie.session.connect` |
| `2026-08-15 15:30:01` | `cowrie.client.version` |
| `2026-08-15 15:30:01` | `cowrie.client.kex` |
| `2026-08-15 15:30:02` | `cowrie.login.success` |
| `2026-08-15 15:30:03` | `cowrie.session.params` |
| `2026-08-15 15:30:03` | `cowrie.command.input` |
| `2026-08-15 15:30:03` | `cowrie.log.closed` |
| `2026-08-15 15:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a55da3b87115

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:30 |
| **Last Seen** | 2026-08-15 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:30:09` | `cowrie.session.connect` |
| `2026-08-15 15:30:09` | `cowrie.client.version` |
| `2026-08-15 15:30:09` | `cowrie.client.kex` |
| `2026-08-15 15:30:10` | `cowrie.login.success` |
| `2026-08-15 15:30:11` | `cowrie.session.params` |
| `2026-08-15 15:30:11` | `cowrie.command.input` |
| `2026-08-15 15:30:11` | `cowrie.log.closed` |
| `2026-08-15 15:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebd7466b8781

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:30 |
| **Last Seen** | 2026-08-15 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:30:18` | `cowrie.session.connect` |
| `2026-08-15 15:30:18` | `cowrie.client.version` |
| `2026-08-15 15:30:18` | `cowrie.client.kex` |
| `2026-08-15 15:30:18` | `cowrie.login.success` |
| `2026-08-15 15:30:19` | `cowrie.session.params` |
| `2026-08-15 15:30:19` | `cowrie.command.input` |
| `2026-08-15 15:30:19` | `cowrie.log.closed` |
| `2026-08-15 15:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844788eb472e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:30 |
| **Last Seen** | 2026-08-15 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:30:26` | `cowrie.session.connect` |
| `2026-08-15 15:30:26` | `cowrie.client.version` |
| `2026-08-15 15:30:26` | `cowrie.client.kex` |
| `2026-08-15 15:30:27` | `cowrie.login.success` |
| `2026-08-15 15:30:27` | `cowrie.session.params` |
| `2026-08-15 15:30:27` | `cowrie.command.input` |
| `2026-08-15 15:30:28` | `cowrie.log.closed` |
| `2026-08-15 15:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83f685e65f8b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:30 |
| **Last Seen** | 2026-08-15 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:30:35` | `cowrie.session.connect` |
| `2026-08-15 15:30:35` | `cowrie.client.version` |
| `2026-08-15 15:30:35` | `cowrie.client.kex` |
| `2026-08-15 15:30:35` | `cowrie.login.success` |
| `2026-08-15 15:30:36` | `cowrie.session.params` |
| `2026-08-15 15:30:36` | `cowrie.command.input` |
| `2026-08-15 15:30:36` | `cowrie.log.closed` |
| `2026-08-15 15:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824fe0c79910

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:30 |
| **Last Seen** | 2026-08-15 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:30:44` | `cowrie.session.connect` |
| `2026-08-15 15:30:44` | `cowrie.client.version` |
| `2026-08-15 15:30:44` | `cowrie.client.kex` |
| `2026-08-15 15:30:44` | `cowrie.login.success` |
| `2026-08-15 15:30:45` | `cowrie.session.params` |
| `2026-08-15 15:30:45` | `cowrie.command.input` |
| `2026-08-15 15:30:45` | `cowrie.log.closed` |
| `2026-08-15 15:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5497958e225

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:30 |
| **Last Seen** | 2026-08-15 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:30:52` | `cowrie.session.connect` |
| `2026-08-15 15:30:52` | `cowrie.client.version` |
| `2026-08-15 15:30:52` | `cowrie.client.kex` |
| `2026-08-15 15:30:53` | `cowrie.login.success` |
| `2026-08-15 15:30:54` | `cowrie.session.params` |
| `2026-08-15 15:30:54` | `cowrie.command.input` |
| `2026-08-15 15:30:54` | `cowrie.log.closed` |
| `2026-08-15 15:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34a867745778

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:31 |
| **Last Seen** | 2026-08-15 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:31:01` | `cowrie.session.connect` |
| `2026-08-15 15:31:01` | `cowrie.client.version` |
| `2026-08-15 15:31:01` | `cowrie.client.kex` |
| `2026-08-15 15:31:01` | `cowrie.login.success` |
| `2026-08-15 15:31:02` | `cowrie.session.params` |
| `2026-08-15 15:31:02` | `cowrie.command.input` |
| `2026-08-15 15:31:02` | `cowrie.log.closed` |
| `2026-08-15 15:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8f604239342

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:31 |
| **Last Seen** | 2026-08-15 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:31:08` | `cowrie.session.connect` |
| `2026-08-15 15:31:08` | `cowrie.client.version` |
| `2026-08-15 15:31:08` | `cowrie.client.kex` |
| `2026-08-15 15:31:09` | `cowrie.login.success` |
| `2026-08-15 15:31:10` | `cowrie.session.params` |
| `2026-08-15 15:31:10` | `cowrie.command.input` |
| `2026-08-15 15:31:10` | `cowrie.log.closed` |
| `2026-08-15 15:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c9fbae05ed

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:31 |
| **Last Seen** | 2026-08-15 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:31:17` | `cowrie.session.connect` |
| `2026-08-15 15:31:17` | `cowrie.client.version` |
| `2026-08-15 15:31:17` | `cowrie.client.kex` |
| `2026-08-15 15:31:17` | `cowrie.login.success` |
| `2026-08-15 15:31:19` | `cowrie.session.params` |
| `2026-08-15 15:31:19` | `cowrie.command.input` |
| `2026-08-15 15:31:19` | `cowrie.log.closed` |
| `2026-08-15 15:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30fb213c7ebb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:31 |
| **Last Seen** | 2026-08-15 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:31:26` | `cowrie.session.connect` |
| `2026-08-15 15:31:26` | `cowrie.client.version` |
| `2026-08-15 15:31:26` | `cowrie.client.kex` |
| `2026-08-15 15:31:26` | `cowrie.login.success` |
| `2026-08-15 15:31:27` | `cowrie.session.params` |
| `2026-08-15 15:31:27` | `cowrie.command.input` |
| `2026-08-15 15:31:27` | `cowrie.log.closed` |
| `2026-08-15 15:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0521502eb399

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:31 |
| **Last Seen** | 2026-08-15 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:31:35` | `cowrie.session.connect` |
| `2026-08-15 15:31:35` | `cowrie.client.version` |
| `2026-08-15 15:31:35` | `cowrie.client.kex` |
| `2026-08-15 15:31:35` | `cowrie.login.success` |
| `2026-08-15 15:31:36` | `cowrie.session.params` |
| `2026-08-15 15:31:36` | `cowrie.command.input` |
| `2026-08-15 15:31:36` | `cowrie.log.closed` |
| `2026-08-15 15:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91228f2be75f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:31 |
| **Last Seen** | 2026-08-15 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:31:44` | `cowrie.session.connect` |
| `2026-08-15 15:31:44` | `cowrie.client.version` |
| `2026-08-15 15:31:44` | `cowrie.client.kex` |
| `2026-08-15 15:31:44` | `cowrie.login.success` |
| `2026-08-15 15:31:45` | `cowrie.session.params` |
| `2026-08-15 15:31:45` | `cowrie.command.input` |
| `2026-08-15 15:31:45` | `cowrie.log.closed` |
| `2026-08-15 15:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0755b699c6a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:31 |
| **Last Seen** | 2026-08-15 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:31:52` | `cowrie.session.connect` |
| `2026-08-15 15:31:52` | `cowrie.client.version` |
| `2026-08-15 15:31:52` | `cowrie.client.kex` |
| `2026-08-15 15:31:53` | `cowrie.login.success` |
| `2026-08-15 15:31:53` | `cowrie.session.params` |
| `2026-08-15 15:31:53` | `cowrie.command.input` |
| `2026-08-15 15:31:53` | `cowrie.log.closed` |
| `2026-08-15 15:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8baca2c5520e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:32 |
| **Last Seen** | 2026-08-15 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:32:01` | `cowrie.session.connect` |
| `2026-08-15 15:32:01` | `cowrie.client.version` |
| `2026-08-15 15:32:01` | `cowrie.client.kex` |
| `2026-08-15 15:32:01` | `cowrie.login.success` |
| `2026-08-15 15:32:02` | `cowrie.session.params` |
| `2026-08-15 15:32:02` | `cowrie.command.input` |
| `2026-08-15 15:32:02` | `cowrie.log.closed` |
| `2026-08-15 15:32:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4729fd3dea09

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:32 |
| **Last Seen** | 2026-08-15 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:32:08` | `cowrie.session.connect` |
| `2026-08-15 15:32:08` | `cowrie.client.version` |
| `2026-08-15 15:32:09` | `cowrie.client.kex` |
| `2026-08-15 15:32:09` | `cowrie.login.success` |
| `2026-08-15 15:32:10` | `cowrie.session.params` |
| `2026-08-15 15:32:10` | `cowrie.command.input` |
| `2026-08-15 15:32:10` | `cowrie.log.closed` |
| `2026-08-15 15:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a3deb237a8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:32 |
| **Last Seen** | 2026-08-15 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:32:18` | `cowrie.session.connect` |
| `2026-08-15 15:32:18` | `cowrie.client.version` |
| `2026-08-15 15:32:18` | `cowrie.client.kex` |
| `2026-08-15 15:32:18` | `cowrie.login.success` |
| `2026-08-15 15:32:19` | `cowrie.session.params` |
| `2026-08-15 15:32:19` | `cowrie.command.input` |
| `2026-08-15 15:32:19` | `cowrie.log.closed` |
| `2026-08-15 15:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2050c0208fa4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:32 |
| **Last Seen** | 2026-08-15 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:32:25` | `cowrie.session.connect` |
| `2026-08-15 15:32:25` | `cowrie.client.version` |
| `2026-08-15 15:32:26` | `cowrie.client.kex` |
| `2026-08-15 15:32:26` | `cowrie.login.success` |
| `2026-08-15 15:32:27` | `cowrie.session.params` |
| `2026-08-15 15:32:27` | `cowrie.command.input` |
| `2026-08-15 15:32:27` | `cowrie.log.closed` |
| `2026-08-15 15:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-435ae97cb739

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:32 |
| **Last Seen** | 2026-08-15 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:32:34` | `cowrie.session.connect` |
| `2026-08-15 15:32:34` | `cowrie.client.version` |
| `2026-08-15 15:32:34` | `cowrie.client.kex` |
| `2026-08-15 15:32:34` | `cowrie.login.success` |
| `2026-08-15 15:32:35` | `cowrie.session.params` |
| `2026-08-15 15:32:35` | `cowrie.command.input` |
| `2026-08-15 15:32:35` | `cowrie.log.closed` |
| `2026-08-15 15:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4198c036ecd4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:32 |
| **Last Seen** | 2026-08-15 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:32:43` | `cowrie.session.connect` |
| `2026-08-15 15:32:43` | `cowrie.client.version` |
| `2026-08-15 15:32:43` | `cowrie.client.kex` |
| `2026-08-15 15:32:43` | `cowrie.login.success` |
| `2026-08-15 15:32:44` | `cowrie.session.params` |
| `2026-08-15 15:32:44` | `cowrie.command.input` |
| `2026-08-15 15:32:44` | `cowrie.log.closed` |
| `2026-08-15 15:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d719c66718

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:32 |
| **Last Seen** | 2026-08-15 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:32:51` | `cowrie.session.connect` |
| `2026-08-15 15:32:51` | `cowrie.client.version` |
| `2026-08-15 15:32:51` | `cowrie.client.kex` |
| `2026-08-15 15:32:52` | `cowrie.login.success` |
| `2026-08-15 15:32:53` | `cowrie.session.params` |
| `2026-08-15 15:32:53` | `cowrie.command.input` |
| `2026-08-15 15:32:53` | `cowrie.log.closed` |
| `2026-08-15 15:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046da1828716

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:32 |
| **Last Seen** | 2026-08-15 15:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:32:59` | `cowrie.session.connect` |
| `2026-08-15 15:32:59` | `cowrie.client.version` |
| `2026-08-15 15:32:59` | `cowrie.client.kex` |
| `2026-08-15 15:32:59` | `cowrie.login.success` |
| `2026-08-15 15:33:00` | `cowrie.session.params` |
| `2026-08-15 15:33:00` | `cowrie.command.input` |
| `2026-08-15 15:33:00` | `cowrie.log.closed` |
| `2026-08-15 15:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e6267e80236

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]237` |
| **First Seen** | 2026-08-15 15:33 |
| **Last Seen** | 2026-08-15 15:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:33:07` | `cowrie.session.connect` |
| `2026-08-15 15:33:07` | `cowrie.client.version` |
| `2026-08-15 15:33:07` | `cowrie.client.kex` |
| `2026-08-15 15:33:07` | `cowrie.login.success` |
| `2026-08-15 15:33:08` | `cowrie.session.params` |
| `2026-08-15 15:33:08` | `cowrie.command.input` |
| `2026-08-15 15:33:08` | `cowrie.log.closed` |
| `2026-08-15 15:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]237` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24e39fc98e0a

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 15:34 |
| **Last Seen** | 2026-08-15 15:35 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:34:54` | `cowrie.session.connect` |
| `2026-08-15 15:34:59` | `cowrie.client.version` |
| `2026-08-15 15:34:59` | `cowrie.client.kex` |
| `2026-08-15 15:35:21` | `cowrie.login.success` |
| `2026-08-15 15:35:33` | `cowrie.session.params` |
| `2026-08-15 15:35:33` | `cowrie.command.input` |
| `2026-08-15 15:35:38` | `cowrie.log.closed` |
| `2026-08-15 15:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f703fbf2e77

| Field | Detail |
|---|---|
| **Source IP** | `156.238.86[.]2` |
| **First Seen** | 2026-08-15 15:35 |
| **Last Seen** | 2026-08-15 15:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:35:40` | `cowrie.session.connect` |
| `2026-08-15 15:35:40` | `cowrie.client.version` |
| `2026-08-15 15:35:40` | `cowrie.client.kex` |
| `2026-08-15 15:35:42` | `cowrie.login.success` |
| `2026-08-15 15:35:42` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.238.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `156.238.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d68005350f

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]51` |
| **First Seen** | 2026-08-15 15:35 |
| **Last Seen** | 2026-08-15 15:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:35:53` | `cowrie.session.connect` |
| `2026-08-15 15:35:54` | `cowrie.client.version` |
| `2026-08-15 15:35:54` | `cowrie.client.kex` |
| `2026-08-15 15:35:56` | `cowrie.login.success` |
| `2026-08-15 15:35:57` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]51` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8544bee99693

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-15 15:37 |
| **Last Seen** | 2026-08-15 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:37:10` | `cowrie.session.connect` |
| `2026-08-15 15:37:10` | `cowrie.client.version` |
| `2026-08-15 15:37:10` | `cowrie.client.kex` |
| `2026-08-15 15:37:11` | `cowrie.login.success` |
| `2026-08-15 15:37:11` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:37:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-15 15:37:11` | `cowrie.direct-tcpip.data` |
| `2026-08-15 15:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a1942149a2

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-08-15 15:39 |
| **Last Seen** | 2026-08-15 15:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:39:08` | `cowrie.session.connect` |
| `2026-08-15 15:39:09` | `cowrie.client.version` |
| `2026-08-15 15:39:09` | `cowrie.client.kex` |
| `2026-08-15 15:39:12` | `cowrie.login.success` |
| `2026-08-15 15:39:13` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-928eeed4b8df

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-08-15 15:39 |
| **Last Seen** | 2026-08-15 15:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:39:18` | `cowrie.session.connect` |
| `2026-08-15 15:39:19` | `cowrie.client.version` |
| `2026-08-15 15:39:19` | `cowrie.client.kex` |
| `2026-08-15 15:39:20` | `cowrie.login.success` |
| `2026-08-15 15:39:20` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47d68964360a

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-08-15 15:40 |
| **Last Seen** | 2026-08-15 15:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:40:57` | `cowrie.session.connect` |
| `2026-08-15 15:40:57` | `cowrie.client.version` |
| `2026-08-15 15:40:57` | `cowrie.client.kex` |
| `2026-08-15 15:41:00` | `cowrie.login.success` |
| `2026-08-15 15:41:01` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87dbbce71bf9

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-15 15:41 |
| **Last Seen** | 2026-08-15 15:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:41:09` | `cowrie.session.connect` |
| `2026-08-15 15:41:12` | `cowrie.client.version` |
| `2026-08-15 15:41:12` | `cowrie.client.kex` |
| `2026-08-15 15:41:15` | `cowrie.login.success` |
| `2026-08-15 15:41:16` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b4ed3cd69c

| Field | Detail |
|---|---|
| **Source IP** | `5.48.46[.]95` |
| **First Seen** | 2026-08-15 15:41 |
| **Last Seen** | 2026-08-15 15:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:41:25` | `cowrie.session.connect` |
| `2026-08-15 15:41:26` | `cowrie.client.version` |
| `2026-08-15 15:41:26` | `cowrie.client.kex` |
| `2026-08-15 15:41:26` | `cowrie.login.success` |
| `2026-08-15 15:41:27` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.48.46[.]95` to AbuseIPDB if not already reported
- [ ] Block `5.48.46[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc6fc011a09

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 15:43 |
| **Last Seen** | 2026-08-15 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:43:23` | `cowrie.session.connect` |
| `2026-08-15 15:43:23` | `cowrie.client.version` |
| `2026-08-15 15:43:23` | `cowrie.client.kex` |
| `2026-08-15 15:43:24` | `cowrie.login.success` |
| `2026-08-15 15:43:25` | `cowrie.session.params` |
| `2026-08-15 15:43:25` | `cowrie.command.input` |
| `2026-08-15 15:43:25` | `cowrie.log.closed` |
| `2026-08-15 15:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90317d9a5cf0

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-15 15:43 |
| **Last Seen** | 2026-08-15 15:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:43:50` | `cowrie.session.connect` |
| `2026-08-15 15:43:51` | `cowrie.client.version` |
| `2026-08-15 15:43:51` | `cowrie.client.kex` |
| `2026-08-15 15:43:52` | `cowrie.login.success` |
| `2026-08-15 15:43:53` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f2b86a1963

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]61` |
| **First Seen** | 2026-08-15 15:43 |
| **Last Seen** | 2026-08-15 15:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:43:59` | `cowrie.session.connect` |
| `2026-08-15 15:44:00` | `cowrie.client.version` |
| `2026-08-15 15:44:00` | `cowrie.client.kex` |
| `2026-08-15 15:44:02` | `cowrie.login.success` |
| `2026-08-15 15:44:03` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]61` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71c2b3a42a5

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]4` |
| **First Seen** | 2026-08-15 15:46 |
| **Last Seen** | 2026-08-15 15:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:46:29` | `cowrie.session.connect` |
| `2026-08-15 15:46:29` | `cowrie.client.version` |
| `2026-08-15 15:46:29` | `cowrie.client.kex` |
| `2026-08-15 15:46:31` | `cowrie.login.success` |
| `2026-08-15 15:46:32` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]4` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2163bb4cb24d

| Field | Detail |
|---|---|
| **Source IP** | `223.197.226[.]51` |
| **First Seen** | 2026-08-15 15:46 |
| **Last Seen** | 2026-08-15 15:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:46:42` | `cowrie.session.connect` |
| `2026-08-15 15:46:42` | `cowrie.client.version` |
| `2026-08-15 15:46:42` | `cowrie.client.kex` |
| `2026-08-15 15:46:44` | `cowrie.login.success` |
| `2026-08-15 15:46:45` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.226[.]51` to AbuseIPDB if not already reported
- [ ] Block `223.197.226[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59ee7e092e71

| Field | Detail |
|---|---|
| **Source IP** | `94.228.240[.]2` |
| **First Seen** | 2026-08-15 15:55 |
| **Last Seen** | 2026-08-15 15:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:55:26` | `cowrie.session.connect` |
| `2026-08-15 15:55:26` | `cowrie.client.version` |
| `2026-08-15 15:55:26` | `cowrie.client.kex` |
| `2026-08-15 15:55:28` | `cowrie.login.success` |
| `2026-08-15 15:55:28` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.228.240[.]2` to AbuseIPDB if not already reported
- [ ] Block `94.228.240[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3178eff7f4ae

| Field | Detail |
|---|---|
| **Source IP** | `165.227.129[.]203` |
| **First Seen** | 2026-08-15 15:55 |
| **Last Seen** | 2026-08-15 15:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 15:55:33` | `cowrie.session.connect` |
| `2026-08-15 15:55:33` | `cowrie.client.version` |
| `2026-08-15 15:55:33` | `cowrie.client.kex` |
| `2026-08-15 15:55:34` | `cowrie.login.success` |
| `2026-08-15 15:55:35` | `cowrie.direct-tcpip.request` |
| `2026-08-15 15:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.129[.]203` to AbuseIPDB if not already reported
- [ ] Block `165.227.129[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e651324859fe

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 16:06 |
| **Last Seen** | 2026-08-15 16:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:06:01` | `cowrie.session.connect` |
| `2026-08-15 16:06:01` | `cowrie.client.version` |
| `2026-08-15 16:06:01` | `cowrie.client.kex` |
| `2026-08-15 16:06:01` | `cowrie.login.success` |
| `2026-08-15 16:06:01` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:06:02` | `cowrie.direct-tcpip.data` |
| `2026-08-15 16:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-671dd2842ca2

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-08-15 16:09 |
| **Last Seen** | 2026-08-15 16:10 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:09:59` | `cowrie.session.connect` |
| `2026-08-15 16:10:01` | `cowrie.client.version` |
| `2026-08-15 16:10:01` | `cowrie.client.kex` |
| `2026-08-15 16:10:03` | `cowrie.login.success` |
| `2026-08-15 16:10:04` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f843492e906

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 16:13 |
| **Last Seen** | 2026-08-15 16:14 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:13:27` | `cowrie.session.connect` |
| `2026-08-15 16:13:33` | `cowrie.client.version` |
| `2026-08-15 16:13:33` | `cowrie.client.kex` |
| `2026-08-15 16:14:00` | `cowrie.login.success` |
| `2026-08-15 16:14:11` | `cowrie.session.params` |
| `2026-08-15 16:14:11` | `cowrie.command.input` |
| `2026-08-15 16:14:19` | `cowrie.log.closed` |
| `2026-08-15 16:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-141abbb22b03

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-08-15 16:14 |
| **Last Seen** | 2026-08-15 16:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:14:56` | `cowrie.session.connect` |
| `2026-08-15 16:14:57` | `cowrie.client.version` |
| `2026-08-15 16:14:57` | `cowrie.client.kex` |
| `2026-08-15 16:14:58` | `cowrie.login.success` |
| `2026-08-15 16:14:58` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cddb7a9718a4

| Field | Detail |
|---|---|
| **Source IP** | `182.151.45[.]136` |
| **First Seen** | 2026-08-15 16:15 |
| **Last Seen** | 2026-08-15 16:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:15:03` | `cowrie.session.connect` |
| `2026-08-15 16:15:05` | `cowrie.client.version` |
| `2026-08-15 16:15:05` | `cowrie.client.kex` |
| `2026-08-15 16:15:07` | `cowrie.login.success` |
| `2026-08-15 16:15:07` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.151.45[.]136` to AbuseIPDB if not already reported
- [ ] Block `182.151.45[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a198adb7eb

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-15 16:17 |
| **Last Seen** | 2026-08-15 16:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:17:34` | `cowrie.session.connect` |
| `2026-08-15 16:17:35` | `cowrie.client.version` |
| `2026-08-15 16:17:35` | `cowrie.client.kex` |
| `2026-08-15 16:17:36` | `cowrie.login.success` |
| `2026-08-15 16:17:36` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0300c7dc101

| Field | Detail |
|---|---|
| **Source IP** | `61.77.220[.]62` |
| **First Seen** | 2026-08-15 16:17 |
| **Last Seen** | 2026-08-15 16:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:17:53` | `cowrie.session.connect` |
| `2026-08-15 16:17:53` | `cowrie.client.version` |
| `2026-08-15 16:17:53` | `cowrie.client.kex` |
| `2026-08-15 16:17:56` | `cowrie.login.success` |
| `2026-08-15 16:17:57` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.77.220[.]62` to AbuseIPDB if not already reported
- [ ] Block `61.77.220[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6af96d2dd087

| Field | Detail |
|---|---|
| **Source IP** | `103.251.143[.]14` |
| **First Seen** | 2026-08-15 16:18 |
| **Last Seen** | 2026-08-15 16:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:18:02` | `cowrie.session.connect` |
| `2026-08-15 16:18:03` | `cowrie.client.version` |
| `2026-08-15 16:18:03` | `cowrie.client.kex` |
| `2026-08-15 16:18:05` | `cowrie.login.success` |
| `2026-08-15 16:18:06` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:18:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.251.143[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.251.143[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-081e44bd1081

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 16:21 |
| **Last Seen** | 2026-08-15 16:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:21:39` | `cowrie.session.connect` |
| `2026-08-15 16:21:39` | `cowrie.client.version` |
| `2026-08-15 16:21:40` | `cowrie.client.kex` |
| `2026-08-15 16:21:40` | `cowrie.login.success` |
| `2026-08-15 16:21:41` | `cowrie.session.params` |
| `2026-08-15 16:21:41` | `cowrie.command.input` |
| `2026-08-15 16:21:42` | `cowrie.log.closed` |
| `2026-08-15 16:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-836a71c6824a

| Field | Detail |
|---|---|
| **Source IP** | `211.238.237[.]254` |
| **First Seen** | 2026-08-15 16:29 |
| **Last Seen** | 2026-08-15 16:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:29:38` | `cowrie.session.connect` |
| `2026-08-15 16:29:39` | `cowrie.client.version` |
| `2026-08-15 16:29:39` | `cowrie.client.kex` |
| `2026-08-15 16:29:41` | `cowrie.login.success` |
| `2026-08-15 16:29:42` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.238.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `211.238.237[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2adafd0040b

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-15 16:31 |
| **Last Seen** | 2026-08-15 16:31 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:31:15` | `cowrie.session.connect` |
| `2026-08-15 16:31:17` | `cowrie.client.version` |
| `2026-08-15 16:31:17` | `cowrie.client.kex` |
| `2026-08-15 16:31:28` | `cowrie.login.success` |
| `2026-08-15 16:31:32` | `cowrie.session.params` |
| `2026-08-15 16:31:32` | `cowrie.command.input` |
| `2026-08-15 16:31:35` | `cowrie.log.closed` |
| `2026-08-15 16:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314775303e85

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-15 16:31 |
| **Last Seen** | 2026-08-15 16:32 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:31:36` | `cowrie.session.connect` |
| `2026-08-15 16:31:38` | `cowrie.client.version` |
| `2026-08-15 16:31:38` | `cowrie.client.kex` |
| `2026-08-15 16:31:53` | `cowrie.login.success` |
| `2026-08-15 16:31:58` | `cowrie.session.params` |
| `2026-08-15 16:31:58` | `cowrie.command.input` |
| `2026-08-15 16:32:01` | `cowrie.log.closed` |
| `2026-08-15 16:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaa5ef25a86e

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-15 16:32 |
| **Last Seen** | 2026-08-15 16:32 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:32:01` | `cowrie.session.connect` |
| `2026-08-15 16:32:03` | `cowrie.client.version` |
| `2026-08-15 16:32:03` | `cowrie.client.kex` |
| `2026-08-15 16:32:15` | `cowrie.login.success` |
| `2026-08-15 16:32:22` | `cowrie.session.params` |
| `2026-08-15 16:32:22` | `cowrie.command.input` |
| `2026-08-15 16:32:24` | `cowrie.log.closed` |
| `2026-08-15 16:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d29e2179964d

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-15 16:32 |
| **Last Seen** | 2026-08-15 16:32 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:32:25` | `cowrie.session.connect` |
| `2026-08-15 16:32:27` | `cowrie.client.version` |
| `2026-08-15 16:32:27` | `cowrie.client.kex` |
| `2026-08-15 16:32:36` | `cowrie.login.success` |
| `2026-08-15 16:32:42` | `cowrie.session.params` |
| `2026-08-15 16:32:42` | `cowrie.command.input` |
| `2026-08-15 16:32:44` | `cowrie.log.closed` |
| `2026-08-15 16:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770dc9607758

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-15 16:32 |
| **Last Seen** | 2026-08-15 16:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:32:45` | `cowrie.session.connect` |
| `2026-08-15 16:32:46` | `cowrie.client.version` |
| `2026-08-15 16:32:46` | `cowrie.client.kex` |
| `2026-08-15 16:32:50` | `cowrie.login.success` |
| `2026-08-15 16:32:51` | `cowrie.session.params` |
| `2026-08-15 16:32:51` | `cowrie.command.input` |
| `2026-08-15 16:32:51` | `cowrie.log.closed` |
| `2026-08-15 16:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c96c2eba10d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-15 16:35 |
| **Last Seen** | 2026-08-15 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:35:07` | `cowrie.session.connect` |
| `2026-08-15 16:35:07` | `cowrie.client.version` |
| `2026-08-15 16:35:07` | `cowrie.client.kex` |
| `2026-08-15 16:35:08` | `cowrie.login.success` |
| `2026-08-15 16:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91844b19dfaa

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-15 16:35 |
| **Last Seen** | 2026-08-15 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:35:07` | `cowrie.session.connect` |
| `2026-08-15 16:35:07` | `cowrie.client.version` |
| `2026-08-15 16:35:07` | `cowrie.client.kex` |
| `2026-08-15 16:35:08` | `cowrie.login.success` |
| `2026-08-15 16:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ab6e78dd65

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 16:40 |
| **Last Seen** | 2026-08-15 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:40:47` | `cowrie.session.connect` |
| `2026-08-15 16:40:47` | `cowrie.client.version` |
| `2026-08-15 16:40:48` | `cowrie.client.kex` |
| `2026-08-15 16:40:48` | `cowrie.login.success` |
| `2026-08-15 16:40:49` | `cowrie.session.params` |
| `2026-08-15 16:40:49` | `cowrie.command.input` |
| `2026-08-15 16:40:49` | `cowrie.log.closed` |
| `2026-08-15 16:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2981efd3d115

| Field | Detail |
|---|---|
| **Source IP** | `111.39.167[.]59` |
| **First Seen** | 2026-08-15 16:43 |
| **Last Seen** | 2026-08-15 16:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:43:58` | `cowrie.session.connect` |
| `2026-08-15 16:43:59` | `cowrie.client.version` |
| `2026-08-15 16:43:59` | `cowrie.client.kex` |
| `2026-08-15 16:44:04` | `cowrie.login.success` |
| `2026-08-15 16:44:06` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.167[.]59` to AbuseIPDB if not already reported
- [ ] Block `111.39.167[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49bd98e25379

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-08-15 16:49 |
| **Last Seen** | 2026-08-15 16:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:49:08` | `cowrie.session.connect` |
| `2026-08-15 16:49:09` | `cowrie.client.version` |
| `2026-08-15 16:49:09` | `cowrie.client.kex` |
| `2026-08-15 16:49:12` | `cowrie.login.success` |
| `2026-08-15 16:49:13` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1033869235e

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-08-15 16:49 |
| **Last Seen** | 2026-08-15 16:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:49:18` | `cowrie.session.connect` |
| `2026-08-15 16:49:19` | `cowrie.client.version` |
| `2026-08-15 16:49:19` | `cowrie.client.kex` |
| `2026-08-15 16:49:21` | `cowrie.login.success` |
| `2026-08-15 16:49:22` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-117266149a64

| Field | Detail |
|---|---|
| **Source IP** | `211.238.237[.]254` |
| **First Seen** | 2026-08-15 16:51 |
| **Last Seen** | 2026-08-15 16:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:51:39` | `cowrie.session.connect` |
| `2026-08-15 16:51:40` | `cowrie.client.version` |
| `2026-08-15 16:51:40` | `cowrie.client.kex` |
| `2026-08-15 16:51:42` | `cowrie.login.success` |
| `2026-08-15 16:51:43` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.238.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `211.238.237[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dabcef3a4798

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]101` |
| **First Seen** | 2026-08-15 16:51 |
| **Last Seen** | 2026-08-15 16:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:51:50` | `cowrie.session.connect` |
| `2026-08-15 16:51:51` | `cowrie.client.version` |
| `2026-08-15 16:51:51` | `cowrie.client.kex` |
| `2026-08-15 16:51:53` | `cowrie.login.success` |
| `2026-08-15 16:51:54` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]101` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f7bcc057725

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-08-15 16:51 |
| **Last Seen** | 2026-08-15 16:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 16:51:52` | `cowrie.session.connect` |
| `2026-08-15 16:51:53` | `cowrie.client.version` |
| `2026-08-15 16:51:53` | `cowrie.client.kex` |
| `2026-08-15 16:51:56` | `cowrie.login.success` |
| `2026-08-15 16:51:58` | `cowrie.direct-tcpip.request` |
| `2026-08-15 16:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **5660** | 2026-08-15 14:55 | 2026-08-15 16:55 | 6668m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-15 15:02 | 2026-08-15 16:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-15 16:39 | 2026-08-15 16:44 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.142.193[.]164` | **3** | 2026-08-15 15:55 | 2026-08-15 16:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-08-15 16:21 | 2026-08-15 16:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]42` | **3** | 2026-08-15 15:56 | 2026-08-15 15:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]194` | **3** | 2026-08-15 15:51 | 2026-08-15 15:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]86` | **3** | 2026-08-15 15:56 | 2026-08-15 15:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-15 16:43 | 2026-08-15 16:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-15 15:25 | 2026-08-15 15:32 | 1m | 0 | `T1592` | 🟢 LOW |
| `111.10.169[.]205` | **2** | 2026-08-15 15:06 | 2026-08-15 15:09 | 2m | 0 | `T1592` | 🟢 LOW |
| `156.225.1[.]105` | **2** | 2026-08-15 16:30 | 2026-08-15 16:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `31.77.227[.]120` | **2** | 2026-08-15 16:30 | 2026-08-15 16:31 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.76.250[.]51` | **2** | 2026-08-15 16:06 | 2026-08-15 16:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.180.8[.]116` | 1 | 2026-08-15 16:35 | 2026-08-15 16:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]215` | 1 | 2026-08-15 15:16 | 2026-08-15 15:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.208.236[.]223` | 1 | 2026-08-15 16:30 | 2026-08-15 16:30 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.27.129[.]78` | 1 | 2026-08-15 16:13 | 2026-08-15 16:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-08-15 15:43 | 2026-08-15 15:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.197[.]168` | 1 | 2026-08-15 16:17 | 2026-08-15 16:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-08-15 16:14 | 2026-08-15 16:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.19.55[.]153` | 1 | 2026-08-15 15:09 | 2026-08-15 15:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.123.219[.]34` | 1 | 2026-08-15 16:32 | 2026-08-15 16:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.211.96[.]85` | 1 | 2026-08-15 15:58 | 2026-08-15 15:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-15 16:17 | 2026-08-15 16:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.86.140[.]39` | 1 | 2026-08-15 16:06 | 2026-08-15 16:06 | 10s | 0 | `T1592` | 🟢 LOW |
| `217.165.22[.]192` | 1 | 2026-08-15 16:02 | 2026-08-15 16:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.159.21[.]170` | 1 | 2026-08-15 16:29 | 2026-08-15 16:29 | 10s | 0 | `T1592` | 🟢 LOW |
| `39.105.212[.]205` | 1 | 2026-08-15 16:54 | 2026-08-15 16:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-15 16:02 | 2026-08-15 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.183.190[.]246` | 1 | 2026-08-15 14:59 | 2026-08-15 15:00 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-08-15 15:35 | 2026-08-15 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-08-15 15:35 | 2026-08-15 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.172.1[.]210` | 1 | 2026-08-15 16:19 | 2026-08-15 16:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.226.56[.]106` | 1 | 2026-08-15 16:09 | 2026-08-15 16:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.239.84[.]130` | 1 | 2026-08-15 16:43 | 2026-08-15 16:45 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

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
| `156.238.86[.]2` | PK | SB Link Network Private Limited | **100** ⚠️ | 50 |
| `61.77.220[.]62` | KR | Korea Telecom | **100** ⚠️ | 34 |
| `187.49.63[.]51` | BR | SCM EVOLUTT CONNECT LTDA | **100** ⚠️ | 11 |
| `192.34.128[.]202` | US | Zito Media | **100** ⚠️ | 50 |
| `122.170.99[.]195` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `182.151.45[.]136` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `200.86.140[.]39` | CL | VTR BANDA ANCHA S.A. | **100** ⚠️ | 3 |
| `104.152.52[.]215` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |
| `50.188.204[.]213` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 353 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 336 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1003.008](https://attack.mitre.org/techniques/T1003/008) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 6094 cases |
| Tool 34  | Credential Extractor        | ✅ 356 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 97 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (0.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 80 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 336 priority case(s) shown individually · 36 recon entry/entries in table (14 group(s) consolidating 5696 session(s)).

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
_Report time: 2026-08-15T18:34:04Z_

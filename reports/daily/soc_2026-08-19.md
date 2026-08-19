# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-19 |
| **Generated At** | 2026-08-19T03:01:31Z |
| **Shift Time** | 03:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1228** |
| Confirmed Threats | **1211** |
| False Positives Filtered | **17** (1.4%) |
| Unique Attacker IPs | **79** |
| Countries of Origin | **29** |
| High Severity Cases | **248** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **980** |
| Malware Samples Analyzed | **3** HIGH · **21** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **269** |
| Unique Credential Pairs | **225** |
| Unique Usernames | **104** |
| Unique Passwords | **160** |
| Successful Auth Pairs | **256** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 69 |
| `debian` | 13 |
| `default` | 12 |
| `support` | 11 |
| `centos` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 15 |
| `1` | 9 |
| `default2023` | 6 |
| `1234` | 6 |
| `debian2016` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `default` | `default2023` | 6 |
| `debian` | `debian2016` | 6 |
| `default` | `default2013` | 6 |
| `support` | `support2012` | 4 |
| `pi` | `abcd1234` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwerty12345` | `85.158.145.129` | 2026-08-19T00:55:51 |
| `test` | `test2016` | `61.2.44.54` | 2026-08-19T00:56:20 |
| `default` | `default2023` | `196.188.93.169` | 2026-08-19T00:57:24 |
| `default` | `default2023` | `192.72.56.178` | 2026-08-19T00:57:31 |
| `support` | `support2012` | `124.239.129.2` | 2026-08-19T01:01:00 |
| `support` | `support2012` | `93.241.232.14` | 2026-08-19T01:01:07 |
| `support` | `support2012` | `35.130.111.98` | 2026-08-19T01:01:08 |
| `support` | `support2012` | `36.154.134.146` | 2026-08-19T01:01:16 |
| `root` | `qwerty123456` | `85.158.145.129` | 2026-08-19T01:01:45 |
| `root` | `qwerty1234567` | `85.158.145.129` | 2026-08-19T01:07:39 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-19T01:07:59 |
| `default` | `default2023` | `10.0.0.73` | 2026-08-19T01:08:39 |
| `test` | `test2016` | `65.20.138.46` | 2026-08-19T01:12:05 |
| `test` | `test2016` | `31.173.66.222` | 2026-08-19T01:12:13 |
| `root` | `qwerty12345678` | `85.158.145.129` | 2026-08-19T01:13:34 |
| `centos` | `centos2016` | `10.0.0.73` | 2026-08-19T01:16:13 |
| `root` | `qwerty123456789` | `85.158.145.129` | 2026-08-19T01:19:28 |
| `support` | `support` | `176.53.159.196` | 2026-08-19T01:20:01 |
| `default` | `default2023` | `112.27.38.203` | 2026-08-19T01:25:23 |
| `root` | `qwerty1234567890` | `85.158.145.129` | 2026-08-19T01:25:23 |
| `default` | `default2023` | `186.215.107.189` | 2026-08-19T01:25:38 |
| `centos` | `centos2019` | `24.97.253.246` | 2026-08-19T01:29:42 |
| `centos` | `centos2019` | `78.197.6.173` | 2026-08-19T01:29:49 |
| `debian` | `debian2007` | `122.166.253.226` | 2026-08-19T01:30:30 |
| `debian` | `debian2007` | `122.187.229.201` | 2026-08-19T01:30:41 |
| `root` | `qwerty6` | `85.158.145.129` | 2026-08-19T01:31:18 |
| `centos` | `centos2016` | `81.237.155.113` | 2026-08-19T01:34:05 |
| `centos` | `centos2016` | `182.75.197.174` | 2026-08-19T01:34:13 |
| `root` | `qwerty7` | `85.158.145.129` | 2026-08-19T01:37:12 |
| `debian` | `debian2007` | `10.0.0.73` | 2026-08-19T01:41:54 |
| `oracle` | `P@ssword123` | `103.59.163.134` | 2026-08-19T01:41:54 |
| `345gs5662d34` | `345gs5662d34` | `103.59.163.134` | 2026-08-19T01:41:59 |
| `oracle` | `3245gs5662d34` | `103.59.163.134` | 2026-08-19T01:42:01 |
| `root` | `qwerty77` | `85.158.145.129` | 2026-08-19T01:43:07 |
| `nia` | `1234` | `119.96.173.169` | 2026-08-19T01:47:56 |
| `nia` | `3245gs5662d34` | `119.96.173.169` | 2026-08-19T01:48:08 |
| `root` | `qwerty777` | `85.158.145.129` | 2026-08-19T01:49:02 |
| `support` | `support2003` | `10.0.0.73` | 2026-08-19T01:49:09 |
| `root` | `passwd@123!` | `221.162.218.85` | 2026-08-19T01:51:57 |
| `345gs5662d34` | `345gs5662d34` | `221.162.218.85` | 2026-08-19T01:52:00 |
| `root` | `3245gs5662d34` | `221.162.218.85` | 2026-08-19T01:52:02 |
| `root` | `qwertys` | `85.158.145.129` | 2026-08-19T01:54:57 |
| `hammad` | `hammad` | `50.6.228.111` | 2026-08-19T01:56:24 |
| `345gs5662d34` | `345gs5662d34` | `50.6.228.111` | 2026-08-19T01:56:25 |
| `hammad` | `3245gs5662d34` | `50.6.228.111` | 2026-08-19T01:56:25 |
| `root` | `qwertyui` | `85.158.145.129` | 2026-08-19T02:00:52 |
| `centos` | `centos2022` | `10.0.0.73` | 2026-08-19T02:01:13 |
| `debian` | `debian2016` | `62.91.108.146` | 2026-08-19T02:03:38 |
| `debian` | `debian2016` | `178.178.222.50` | 2026-08-19T02:03:50 |
| `support` | `support` | `10.0.0.73` | 2026-08-19T02:04:02 |
| `root` | `qwertyuiop` | `85.158.145.129` | 2026-08-19T02:06:47 |
| `support` | `support2003` | `196.203.231.220` | 2026-08-19T02:07:11 |
| `root` | `qwertz123` | `85.158.145.129` | 2026-08-19T02:12:42 |
| `debian` | `debian2016` | `10.0.0.73` | 2026-08-19T02:14:43 |
| `root` | `qwertz12` | `85.158.145.129` | 2026-08-19T02:18:38 |
| `centos` | `centos2022` | `125.72.150.250` | 2026-08-19T02:18:49 |
| `centos` | `centos2022` | `182.75.197.174` | 2026-08-19T02:19:00 |
| `default` | `default2013` | `10.0.0.73` | 2026-08-19T02:22:13 |
| `root` | `qwertz1` | `85.158.145.129` | 2026-08-19T02:24:33 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.90` | 2026-08-19T02:27:42 |
| `root` | `admin` | `108.46.229.102` | 2026-08-19T02:29:33 |
| `root` | `qwertz1234` | `85.158.145.129` | 2026-08-19T02:30:29 |
| `debian` | `debian2016` | `60.249.252.94` | 2026-08-19T02:31:42 |
| `debian` | `debian2016` | `185.112.148.66` | 2026-08-19T02:31:52 |
| `cw` | `cw` | `77.239.124.242` | 2026-08-19T02:36:13 |
| `admin` | `admin2002` | `65.20.175.6` | 2026-08-19T02:36:18 |
| `root` | `123abc456` | `77.239.124.242` | 2026-08-19T02:36:20 |
| `root` | `qwertz12345` | `85.158.145.129` | 2026-08-19T02:36:24 |
| `appuser` | `password` | `77.239.124.242` | 2026-08-19T02:36:26 |
| `admin` | `admin2002` | `177.174.89.99` | 2026-08-19T02:36:27 |
| `support` | `Passw0rd` | `77.239.124.242` | 2026-08-19T02:36:34 |
| `root` | `Password` | `77.239.124.242` | 2026-08-19T02:36:39 |
| `root` | `Aa111111.` | `77.239.124.242` | 2026-08-19T02:36:45 |
| `operator` | `operator1234` | `117.253.130.123` | 2026-08-19T02:36:46 |
| `root` | `Abc12345` | `77.239.124.242` | 2026-08-19T02:36:52 |
| `tactical` | `123456` | `77.239.124.242` | 2026-08-19T02:36:57 |
| `labuser` | `p@ssw0rd` | `77.239.124.242` | 2026-08-19T02:37:04 |
| `john` | `123456` | `77.239.124.242` | 2026-08-19T02:37:12 |
| `odoo16` | `odoo16` | `77.239.124.242` | 2026-08-19T02:37:18 |
| `vm` | `vm` | `77.239.124.242` | 2026-08-19T02:37:26 |
| `root` | `19901017` | `77.239.124.242` | 2026-08-19T02:37:32 |
| `openvpn` | `openvpn` | `77.239.124.242` | 2026-08-19T02:37:39 |
| `ubuntu` | `1234` | `77.239.124.242` | 2026-08-19T02:37:46 |
| `administrator` | `administrator` | `77.239.124.242` | 2026-08-19T02:37:53 |
| `btc` | `btc` | `77.239.124.242` | 2026-08-19T02:38:00 |
| `martin` | `martin` | `77.239.124.242` | 2026-08-19T02:38:06 |
| `sysupdate` | `123456` | `77.239.124.242` | 2026-08-19T02:38:13 |
| `tester` | `12345` | `77.239.124.242` | 2026-08-19T02:38:19 |
| `cloud` | `cloud123!` | `77.239.124.242` | 2026-08-19T02:38:26 |
| `odoo` | `123` | `77.239.124.242` | 2026-08-19T02:38:33 |
| `root1` | `1` | `77.239.124.242` | 2026-08-19T02:38:39 |
| `root` | `qwe123!@` | `77.239.124.242` | 2026-08-19T02:38:46 |
| `cloud` | `Wangsu@2017` | `77.239.124.242` | 2026-08-19T02:38:53 |
| `root` | `aB123456` | `77.239.124.242` | 2026-08-19T02:39:00 |
| `ossuser` | `Changeme_123` | `77.239.124.242` | 2026-08-19T02:39:05 |
| `deployer` | `user` | `77.239.124.242` | 2026-08-19T02:39:12 |
| `oracle` | `oracle123` | `77.239.124.242` | 2026-08-19T02:39:18 |
| `web` | `web123` | `77.239.124.242` | 2026-08-19T02:39:25 |
| `root` | `root@1234` | `77.239.124.242` | 2026-08-19T02:39:32 |
| `x` | `1` | `77.239.124.242` | 2026-08-19T02:39:39 |
| `odoo14` | `odoo` | `77.239.124.242` | 2026-08-19T02:39:47 |
| `root` | `12345678` | `77.239.124.242` | 2026-08-19T02:39:53 |
| `user1` | `modzmodz` | `77.239.124.242` | 2026-08-19T02:40:01 |
| `test` | `1234qwer` | `77.239.124.242` | 2026-08-19T02:40:07 |
| `default` | `default2013` | `34.41.211.48` | 2026-08-19T02:40:08 |
| `dev` | `abc123` | `77.239.124.242` | 2026-08-19T02:40:14 |
| `default` | `default2013` | `174.94.236.211` | 2026-08-19T02:40:16 |
| `www` | `12345678` | `77.239.124.242` | 2026-08-19T02:40:21 |
| `default` | `default2013` | `65.20.204.41` | 2026-08-19T02:40:21 |
| `root` | `p@ssword` | `77.239.124.242` | 2026-08-19T02:40:27 |
| `default` | `default2013` | `103.121.27.218` | 2026-08-19T02:40:30 |
| `user` | `111` | `77.239.124.242` | 2026-08-19T02:40:33 |
| `main` | `12345` | `77.239.124.242` | 2026-08-19T02:40:39 |
| `root` | `toor` | `77.239.124.242` | 2026-08-19T02:40:45 |
| `zabbix` | `zabbix` | `77.239.124.242` | 2026-08-19T02:40:51 |
| `liyang` | `123456` | `77.239.124.242` | 2026-08-19T02:40:58 |
| `user1` | `123` | `77.239.124.242` | 2026-08-19T02:41:03 |
| `root` | `test@123` | `77.239.124.242` | 2026-08-19T02:41:10 |
| `vncuser` | `123456` | `77.239.124.242` | 2026-08-19T02:41:15 |
| `user2` | `1` | `77.239.124.242` | 2026-08-19T02:41:21 |
| `nexus` | `pi` | `77.239.124.242` | 2026-08-19T02:41:29 |
| `ubuntu` | `12345678` | `77.239.124.242` | 2026-08-19T02:41:35 |
| `openclaw` | `123456` | `77.239.124.242` | 2026-08-19T02:41:42 |
| `ali` | `ali` | `77.239.124.242` | 2026-08-19T02:41:50 |
| `alex` | `1` | `77.239.124.242` | 2026-08-19T02:41:57 |
| `root` | `Abcd1234` | `77.239.124.242` | 2026-08-19T02:42:03 |
| `postgres` | `123456` | `77.239.124.242` | 2026-08-19T02:42:09 |
| `deploy` | `1234` | `77.239.124.242` | 2026-08-19T02:42:17 |
| `root` | `qwertz123456` | `85.158.145.129` | 2026-08-19T02:42:19 |
| `root` | `qazwsxedc` | `77.239.124.242` | 2026-08-19T02:42:23 |
| `ansible` | `passwd` | `77.239.124.242` | 2026-08-19T02:42:29 |
| `rancher` | `rancher` | `77.239.124.242` | 2026-08-19T02:42:36 |
| `debian` | `123456789` | `77.239.124.242` | 2026-08-19T02:42:43 |
| `claude` | `claude` | `77.239.124.242` | 2026-08-19T02:42:50 |
| `root` | `qazwsx123` | `77.239.124.242` | 2026-08-19T02:42:57 |
| `admin` | `1` | `77.239.124.242` | 2026-08-19T02:43:04 |
| `ethan` | `ethan` | `77.239.124.242` | 2026-08-19T02:43:11 |
| `app` | `root` | `77.239.124.242` | 2026-08-19T02:43:17 |
| `bitrix` | `bitrix` | `77.239.124.242` | 2026-08-19T02:43:23 |
| `appuser` | `appuser` | `77.239.124.242` | 2026-08-19T02:43:35 |
| `kim` | `kim123` | `77.239.124.242` | 2026-08-19T02:43:41 |
| `david` | `david` | `77.239.124.242` | 2026-08-19T02:43:48 |
| `admin` | `111` | `77.239.124.242` | 2026-08-19T02:43:56 |
| `root` | `test123` | `77.239.124.242` | 2026-08-19T02:44:01 |
| `user1` | `12345` | `77.239.124.242` | 2026-08-19T02:44:08 |
| `user` | `git` | `77.239.124.242` | 2026-08-19T02:44:14 |
| `ec2-user` | `ec2-user` | `77.239.124.242` | 2026-08-19T02:44:19 |
| `root` | `Aa@123456` | `77.239.124.242` | 2026-08-19T02:44:24 |
| `admin` | `1234` | `77.239.124.242` | 2026-08-19T02:44:31 |
| `z` | `qwe123` | `77.239.124.242` | 2026-08-19T02:44:37 |
| `airflow` | `airflow` | `77.239.124.242` | 2026-08-19T02:44:42 |
| `root` | `A123456a` | `77.239.124.242` | 2026-08-19T02:44:49 |
| `gitlab-runner` | `passwd` | `77.239.124.242` | 2026-08-19T02:44:55 |
| `user` | `12345678` | `77.239.124.242` | 2026-08-19T02:45:01 |
| `root` | `linux` | `77.239.124.242` | 2026-08-19T02:45:06 |
| `john` | `john` | `77.239.124.242` | 2026-08-19T02:45:11 |
| `tom` | `tom` | `77.239.124.242` | 2026-08-19T02:45:18 |
| `chris` | `123456` | `77.239.124.242` | 2026-08-19T02:45:25 |
| `username` | `password` | `77.239.124.242` | 2026-08-19T02:45:31 |
| `minecraft` | `1234567890` | `77.239.124.242` | 2026-08-19T02:45:37 |
| `openclaw` | `1` | `77.239.124.242` | 2026-08-19T02:45:43 |
| `rdpuser` | `rdpuser` | `77.239.124.242` | 2026-08-19T02:45:49 |
| `gitlab` | `git` | `77.239.124.242` | 2026-08-19T02:45:54 |
| `root` | `Admin123!` | `77.239.124.242` | 2026-08-19T02:46:00 |
| `root` | `zaq12wsx` | `77.239.124.242` | 2026-08-19T02:46:05 |
| `root` | `qwerty123` | `77.239.124.242` | 2026-08-19T02:46:11 |
| `adminuser` | `123456` | `77.239.124.242` | 2026-08-19T02:46:17 |
| `pi` | `toor` | `77.239.124.242` | 2026-08-19T02:46:22 |
| `teamspeak` | `teamspeak` | `77.239.124.242` | 2026-08-19T02:46:27 |
| `systemd` | `1q2w3e4r` | `77.239.124.242` | 2026-08-19T02:46:32 |
| `admin123` | `admin123` | `77.239.124.242` | 2026-08-19T02:46:39 |
| `root` | `qwe123456` | `77.239.124.242` | 2026-08-19T02:46:44 |
| `devuser` | `devuser` | `77.239.124.242` | 2026-08-19T02:46:51 |
| `runner` | `1234` | `77.239.124.242` | 2026-08-19T02:46:56 |
| `fivem` | `12345` | `77.239.124.242` | 2026-08-19T02:47:01 |
| `sam` | `1234` | `77.239.124.242` | 2026-08-19T02:47:06 |
| `bob` | `root` | `77.239.124.242` | 2026-08-19T02:47:12 |
| `test` | `1` | `77.239.124.242` | 2026-08-19T02:47:17 |
| `root` | `Aa123456` | `77.239.124.242` | 2026-08-19T02:47:23 |
| `hadoop` | `hadoop123` | `77.239.124.242` | 2026-08-19T02:47:31 |
| `docker` | `docker123` | `77.239.124.242` | 2026-08-19T02:47:37 |
| `test2` | `test2` | `77.239.124.242` | 2026-08-19T02:47:44 |
| `user` | `123` | `77.239.124.242` | 2026-08-19T02:47:50 |
| `devops` | `123456` | `77.239.124.242` | 2026-08-19T02:47:56 |
| `operator` | `operator1234` | `10.0.0.73` | 2026-08-19T02:48:02 |
| `gary` | `gary` | `77.239.124.242` | 2026-08-19T02:48:02 |
| `root` | `passw0rd` | `77.239.124.242` | 2026-08-19T02:48:08 |
| `root` | `qwezxc` | `85.158.145.129` | 2026-08-19T02:48:14 |
| `root` | `Welcome@123` | `77.239.124.242` | 2026-08-19T02:48:15 |
| `yogesh` | `yogesh` | `34.88.29.206` | 2026-08-19T02:48:19 |
| `rdpuser` | `123456` | `77.239.124.242` | 2026-08-19T02:48:20 |
| `345gs5662d34` | `345gs5662d34` | `34.88.29.206` | 2026-08-19T02:48:23 |
| `yogesh` | `3245gs5662d34` | `34.88.29.206` | 2026-08-19T02:48:25 |
| `system` | `12345` | `77.239.124.242` | 2026-08-19T02:48:27 |
| `deployer` | `123456` | `77.239.124.242` | 2026-08-19T02:48:32 |
| `test1` | `test123` | `77.239.124.242` | 2026-08-19T02:48:38 |
| `debian` | `toor` | `77.239.124.242` | 2026-08-19T02:48:46 |
| `server` | `12345` | `77.239.124.242` | 2026-08-19T02:48:53 |
| `sam` | `1234567890` | `77.239.124.242` | 2026-08-19T02:49:00 |
| `root` | `Huawei123` | `77.239.124.242` | 2026-08-19T02:49:07 |
| `www` | `123321` | `77.239.124.242` | 2026-08-19T02:49:13 |
| `root` | `Passw0rd` | `77.239.124.242` | 2026-08-19T02:49:20 |
| `root` | `123` | `77.239.124.242` | 2026-08-19T02:49:26 |
| `www` | `user` | `77.239.124.242` | 2026-08-19T02:49:32 |
| `postgres` | `postgres` | `77.239.124.242` | 2026-08-19T02:49:39 |
| `root` | `1qaz@WSX` | `77.239.124.242` | 2026-08-19T02:49:46 |
| `ai` | `Aa123456` | `77.239.124.242` | 2026-08-19T02:49:53 |
| `root` | `ZAQ!2wsx` | `77.239.124.242` | 2026-08-19T02:49:59 |
| `root` | `Aaaa1111` | `77.239.124.242` | 2026-08-19T02:50:05 |
| `root` | `0000` | `77.239.124.242` | 2026-08-19T02:50:11 |
| `root` | `******` | `77.239.124.242` | 2026-08-19T02:50:18 |
| `customer` | `customer` | `77.239.124.242` | 2026-08-19T02:50:25 |
| `ubuntu` | `Ubuntu123!` | `77.239.124.242` | 2026-08-19T02:50:31 |
| `root` | `Qwerty123` | `77.239.124.242` | 2026-08-19T02:50:37 |
| `user` | `passw0rd` | `77.239.124.242` | 2026-08-19T02:50:44 |
| `root` | `1qaz!QAZ` | `77.239.124.242` | 2026-08-19T02:50:49 |
| `root` | `admin1234` | `77.239.124.242` | 2026-08-19T02:50:56 |
| `developer` | `root` | `77.239.124.242` | 2026-08-19T02:51:02 |
| `oracle` | `oracle` | `77.239.124.242` | 2026-08-19T02:51:09 |
| `ubuntu` | `qwer1234` | `77.239.124.242` | 2026-08-19T02:51:16 |
| `root` | `1qazXSW@` | `77.239.124.242` | 2026-08-19T02:51:22 |
| `test_user` | `1` | `77.239.124.242` | 2026-08-19T02:51:29 |
| `lin` | `123456` | `77.239.124.242` | 2026-08-19T02:51:35 |
| `odoo14` | `odoo14` | `77.239.124.242` | 2026-08-19T02:51:41 |
| `user1` | `user1` | `77.239.124.242` | 2026-08-19T02:51:49 |
| `teamspeak` | `1` | `77.239.124.242` | 2026-08-19T02:51:54 |
| `amin` | `amin` | `77.239.124.242` | 2026-08-19T02:52:00 |
| `admin` | `admin2002` | `218.59.235.170` | 2026-08-19T02:52:05 |
| `ai` | `ai` | `77.239.124.242` | 2026-08-19T02:52:06 |
| `grok` | `12345678` | `77.239.124.242` | 2026-08-19T02:52:11 |
| `git` | `123` | `77.239.124.242` | 2026-08-19T02:52:18 |
| `dev` | `dev` | `77.239.124.242` | 2026-08-19T02:52:25 |
| `node` | `1qaz2wsx` | `77.239.124.242` | 2026-08-19T02:52:31 |
| `ec2-user` | `123456` | `77.239.124.242` | 2026-08-19T02:52:38 |
| `root` | `q1w2e3r4` | `77.239.124.242` | 2026-08-19T02:52:44 |
| `student` | `redhat` | `77.239.124.242` | 2026-08-19T02:52:51 |
| `ubuntu` | `qwe123` | `77.239.124.242` | 2026-08-19T02:52:56 |
| `trade` | `123456` | `77.239.124.242` | 2026-08-19T02:53:03 |
| `root` | `12345qwe` | `77.239.124.242` | 2026-08-19T02:53:10 |
| `user` | `user` | `77.239.124.242` | 2026-08-19T02:53:17 |
| `nginx` | `toor` | `77.239.124.242` | 2026-08-19T02:53:25 |
| `alex` | `Ab123456` | `77.239.124.242` | 2026-08-19T02:53:31 |
| `deploy` | `deploy` | `77.239.124.242` | 2026-08-19T02:53:38 |
| `ftpuser` | `p@ssw0rd` | `77.239.124.242` | 2026-08-19T02:53:45 |
| `ubuntu` | `1qaz@WSX` | `77.239.124.242` | 2026-08-19T02:53:52 |
| `root` | `0` | `77.239.124.242` | 2026-08-19T02:53:58 |
| `root` | `Aa123123` | `77.239.124.242` | 2026-08-19T02:54:05 |
| `root` | `test` | `85.158.145.129` | 2026-08-19T02:54:09 |
| `frappe` | `frappe@123` | `77.239.124.242` | 2026-08-19T02:54:10 |
| `ivan` | `ivan` | `77.239.124.242` | 2026-08-19T02:54:18 |
| `dolphinscheduler` | `dolphinscheduler` | `77.239.124.242` | 2026-08-19T02:54:24 |
| `plex` | `plex` | `77.239.124.242` | 2026-08-19T02:54:30 |
| `ubuntu` | `123456789` | `77.239.124.242` | 2026-08-19T02:54:37 |
| `debian` | `qwerty` | `77.239.124.242` | 2026-08-19T02:54:44 |
| `sysupdate` | `Password1` | `77.239.124.242` | 2026-08-19T02:54:51 |
| `root` | `11111111` | `77.239.124.242` | 2026-08-19T02:54:57 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1228** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 211 |
| OpenSSH | 32 |
| libssh | 20 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 177 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 32 | 31 |
| `98f63c4d9c87...` | Generic scanner | 21 | 1 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 177 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 32 | 31 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 21 | 1 | Generic scanner |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `119.96.173.169`, `221.162.218.85`, `34.88.29.206`, `103.59.163.134`, `50.6.228.111`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **79** |
| Unique ASNs | **63** |
| High-Risk ASNs | **53** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS27747` | Telecentro S.A. | 2 | LOW |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (247)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a6e7d335ad61

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 00:55 |
| **Last Seen** | 2026-08-19 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 00:55:50` | `cowrie.session.connect` |
| `2026-08-19 00:55:50` | `cowrie.client.version` |
| `2026-08-19 00:55:50` | `cowrie.client.kex` |
| `2026-08-19 00:55:51` | `cowrie.login.success` |
| `2026-08-19 00:55:51` | `cowrie.session.params` |
| `2026-08-19 00:55:51` | `cowrie.command.input` |
| `2026-08-19 00:55:52` | `cowrie.log.closed` |
| `2026-08-19 00:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e89ee0bd464

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-08-19 00:56 |
| **Last Seen** | 2026-08-19 00:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 00:56:17` | `cowrie.session.connect` |
| `2026-08-19 00:56:18` | `cowrie.client.version` |
| `2026-08-19 00:56:18` | `cowrie.client.kex` |
| `2026-08-19 00:56:20` | `cowrie.login.success` |
| `2026-08-19 00:56:21` | `cowrie.direct-tcpip.request` |
| `2026-08-19 00:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1805de74dcf0

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-19 00:57 |
| **Last Seen** | 2026-08-19 00:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 00:57:22` | `cowrie.session.connect` |
| `2026-08-19 00:57:22` | `cowrie.client.version` |
| `2026-08-19 00:57:22` | `cowrie.client.kex` |
| `2026-08-19 00:57:24` | `cowrie.login.success` |
| `2026-08-19 00:57:24` | `cowrie.direct-tcpip.request` |
| `2026-08-19 00:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9497c2c8f46f

| Field | Detail |
|---|---|
| **Source IP** | `192.72.56[.]178` |
| **First Seen** | 2026-08-19 00:57 |
| **Last Seen** | 2026-08-19 00:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 00:57:29` | `cowrie.session.connect` |
| `2026-08-19 00:57:30` | `cowrie.client.version` |
| `2026-08-19 00:57:30` | `cowrie.client.kex` |
| `2026-08-19 00:57:31` | `cowrie.login.success` |
| `2026-08-19 00:57:32` | `cowrie.direct-tcpip.request` |
| `2026-08-19 00:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.72.56[.]178` to AbuseIPDB if not already reported
- [ ] Block `192.72.56[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd0fe144a598

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-08-19 01:00 |
| **Last Seen** | 2026-08-19 01:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:00:57` | `cowrie.session.connect` |
| `2026-08-19 01:00:58` | `cowrie.client.version` |
| `2026-08-19 01:00:58` | `cowrie.client.kex` |
| `2026-08-19 01:01:00` | `cowrie.login.success` |
| `2026-08-19 01:01:01` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29a0e4f78ef7

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-08-19 01:01 |
| **Last Seen** | 2026-08-19 01:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:01:05` | `cowrie.session.connect` |
| `2026-08-19 01:01:06` | `cowrie.client.version` |
| `2026-08-19 01:01:06` | `cowrie.client.kex` |
| `2026-08-19 01:01:07` | `cowrie.login.success` |
| `2026-08-19 01:01:07` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c80b8784654

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]98` |
| **First Seen** | 2026-08-19 01:01 |
| **Last Seen** | 2026-08-19 01:01 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:01:06` | `cowrie.session.connect` |
| `2026-08-19 01:01:06` | `cowrie.client.version` |
| `2026-08-19 01:01:06` | `cowrie.client.kex` |
| `2026-08-19 01:01:08` | `cowrie.login.success` |
| `2026-08-19 01:01:08` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]98` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c550f3c3401

| Field | Detail |
|---|---|
| **Source IP** | `36.154.134[.]146` |
| **First Seen** | 2026-08-19 01:01 |
| **Last Seen** | 2026-08-19 01:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:01:13` | `cowrie.session.connect` |
| `2026-08-19 01:01:13` | `cowrie.client.version` |
| `2026-08-19 01:01:14` | `cowrie.client.kex` |
| `2026-08-19 01:01:16` | `cowrie.login.success` |
| `2026-08-19 01:01:16` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.154.134[.]146` to AbuseIPDB if not already reported
- [ ] Block `36.154.134[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea53023b40eb

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 01:01 |
| **Last Seen** | 2026-08-19 01:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:01:45` | `cowrie.session.connect` |
| `2026-08-19 01:01:45` | `cowrie.client.version` |
| `2026-08-19 01:01:45` | `cowrie.client.kex` |
| `2026-08-19 01:01:45` | `cowrie.login.success` |
| `2026-08-19 01:01:46` | `cowrie.session.params` |
| `2026-08-19 01:01:46` | `cowrie.command.input` |
| `2026-08-19 01:01:46` | `cowrie.log.closed` |
| `2026-08-19 01:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a32b150eb9

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 01:07 |
| **Last Seen** | 2026-08-19 01:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:07:39` | `cowrie.session.connect` |
| `2026-08-19 01:07:39` | `cowrie.client.version` |
| `2026-08-19 01:07:39` | `cowrie.client.kex` |
| `2026-08-19 01:07:39` | `cowrie.login.success` |
| `2026-08-19 01:07:40` | `cowrie.session.params` |
| `2026-08-19 01:07:40` | `cowrie.command.input` |
| `2026-08-19 01:07:40` | `cowrie.log.closed` |
| `2026-08-19 01:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e93ce0967fd

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]46` |
| **First Seen** | 2026-08-19 01:12 |
| **Last Seen** | 2026-08-19 01:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:12:02` | `cowrie.session.connect` |
| `2026-08-19 01:12:03` | `cowrie.client.version` |
| `2026-08-19 01:12:03` | `cowrie.client.kex` |
| `2026-08-19 01:12:05` | `cowrie.login.success` |
| `2026-08-19 01:12:05` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]46` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b673642ab8cc

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-08-19 01:12 |
| **Last Seen** | 2026-08-19 01:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:12:11` | `cowrie.session.connect` |
| `2026-08-19 01:12:11` | `cowrie.client.version` |
| `2026-08-19 01:12:11` | `cowrie.client.kex` |
| `2026-08-19 01:12:13` | `cowrie.login.success` |
| `2026-08-19 01:12:14` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-310c8619cc34

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 01:13 |
| **Last Seen** | 2026-08-19 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:13:33` | `cowrie.session.connect` |
| `2026-08-19 01:13:33` | `cowrie.client.version` |
| `2026-08-19 01:13:34` | `cowrie.client.kex` |
| `2026-08-19 01:13:34` | `cowrie.login.success` |
| `2026-08-19 01:13:35` | `cowrie.session.params` |
| `2026-08-19 01:13:35` | `cowrie.command.input` |
| `2026-08-19 01:13:35` | `cowrie.log.closed` |
| `2026-08-19 01:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18252baee56f

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 01:19 |
| **Last Seen** | 2026-08-19 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:19:28` | `cowrie.session.connect` |
| `2026-08-19 01:19:28` | `cowrie.client.version` |
| `2026-08-19 01:19:28` | `cowrie.client.kex` |
| `2026-08-19 01:19:28` | `cowrie.login.success` |
| `2026-08-19 01:19:29` | `cowrie.session.params` |
| `2026-08-19 01:19:29` | `cowrie.command.input` |
| `2026-08-19 01:19:29` | `cowrie.log.closed` |
| `2026-08-19 01:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f10becfbf63

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 01:20 |
| **Last Seen** | 2026-08-19 01:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:20:01` | `cowrie.session.connect` |
| `2026-08-19 01:20:01` | `cowrie.client.version` |
| `2026-08-19 01:20:01` | `cowrie.client.kex` |
| `2026-08-19 01:20:01` | `cowrie.login.success` |
| `2026-08-19 01:20:02` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:20:02` | `cowrie.direct-tcpip.data` |
| `2026-08-19 01:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a6666b843c

| Field | Detail |
|---|---|
| **Source IP** | `112.27.38[.]203` |
| **First Seen** | 2026-08-19 01:25 |
| **Last Seen** | 2026-08-19 01:25 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:25:16` | `cowrie.session.connect` |
| `2026-08-19 01:25:18` | `cowrie.client.version` |
| `2026-08-19 01:25:18` | `cowrie.client.kex` |
| `2026-08-19 01:25:23` | `cowrie.login.success` |
| `2026-08-19 01:25:25` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.27.38[.]203` to AbuseIPDB if not already reported
- [ ] Block `112.27.38[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7903172ac1

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 01:25 |
| **Last Seen** | 2026-08-19 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:25:23` | `cowrie.session.connect` |
| `2026-08-19 01:25:23` | `cowrie.client.version` |
| `2026-08-19 01:25:23` | `cowrie.client.kex` |
| `2026-08-19 01:25:23` | `cowrie.login.success` |
| `2026-08-19 01:25:24` | `cowrie.session.params` |
| `2026-08-19 01:25:24` | `cowrie.command.input` |
| `2026-08-19 01:25:24` | `cowrie.log.closed` |
| `2026-08-19 01:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0bd74297d9a

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-19 01:25 |
| **Last Seen** | 2026-08-19 01:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:25:36` | `cowrie.session.connect` |
| `2026-08-19 01:25:36` | `cowrie.client.version` |
| `2026-08-19 01:25:36` | `cowrie.client.kex` |
| `2026-08-19 01:25:38` | `cowrie.login.success` |
| `2026-08-19 01:25:39` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e08292d6a581

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-08-19 01:29 |
| **Last Seen** | 2026-08-19 01:34 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:29:39` | `cowrie.session.connect` |
| `2026-08-19 01:29:40` | `cowrie.client.version` |
| `2026-08-19 01:29:40` | `cowrie.client.kex` |
| `2026-08-19 01:29:42` | `cowrie.login.success` |
| `2026-08-19 01:29:42` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fdffc0eb555

| Field | Detail |
|---|---|
| **Source IP** | `78.197.6[.]173` |
| **First Seen** | 2026-08-19 01:29 |
| **Last Seen** | 2026-08-19 01:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:29:47` | `cowrie.session.connect` |
| `2026-08-19 01:29:48` | `cowrie.client.version` |
| `2026-08-19 01:29:48` | `cowrie.client.kex` |
| `2026-08-19 01:29:49` | `cowrie.login.success` |
| `2026-08-19 01:29:49` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.197.6[.]173` to AbuseIPDB if not already reported
- [ ] Block `78.197.6[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e84cce04894

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-08-19 01:30 |
| **Last Seen** | 2026-08-19 01:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:30:26` | `cowrie.session.connect` |
| `2026-08-19 01:30:27` | `cowrie.client.version` |
| `2026-08-19 01:30:27` | `cowrie.client.kex` |
| `2026-08-19 01:30:30` | `cowrie.login.success` |
| `2026-08-19 01:30:31` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f95d59ef74

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]201` |
| **First Seen** | 2026-08-19 01:30 |
| **Last Seen** | 2026-08-19 01:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:30:37` | `cowrie.session.connect` |
| `2026-08-19 01:30:38` | `cowrie.client.version` |
| `2026-08-19 01:30:38` | `cowrie.client.kex` |
| `2026-08-19 01:30:41` | `cowrie.login.success` |
| `2026-08-19 01:30:42` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]201` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9bffcef50f9

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 01:31 |
| **Last Seen** | 2026-08-19 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:31:17` | `cowrie.session.connect` |
| `2026-08-19 01:31:17` | `cowrie.client.version` |
| `2026-08-19 01:31:18` | `cowrie.client.kex` |
| `2026-08-19 01:31:18` | `cowrie.login.success` |
| `2026-08-19 01:31:19` | `cowrie.session.params` |
| `2026-08-19 01:31:19` | `cowrie.command.input` |
| `2026-08-19 01:31:19` | `cowrie.log.closed` |
| `2026-08-19 01:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28336aec0199

| Field | Detail |
|---|---|
| **Source IP** | `81.237.155[.]113` |
| **First Seen** | 2026-08-19 01:34 |
| **Last Seen** | 2026-08-19 01:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:34:04` | `cowrie.session.connect` |
| `2026-08-19 01:34:04` | `cowrie.client.version` |
| `2026-08-19 01:34:04` | `cowrie.client.kex` |
| `2026-08-19 01:34:05` | `cowrie.login.success` |
| `2026-08-19 01:34:05` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.237.155[.]113` to AbuseIPDB if not already reported
- [ ] Block `81.237.155[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8fbe7e74f90

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-19 01:34 |
| **Last Seen** | 2026-08-19 01:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:34:11` | `cowrie.session.connect` |
| `2026-08-19 01:34:11` | `cowrie.client.version` |
| `2026-08-19 01:34:11` | `cowrie.client.kex` |
| `2026-08-19 01:34:13` | `cowrie.login.success` |
| `2026-08-19 01:34:14` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b74b27d5d2

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 01:37 |
| **Last Seen** | 2026-08-19 01:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:37:12` | `cowrie.session.connect` |
| `2026-08-19 01:37:12` | `cowrie.client.version` |
| `2026-08-19 01:37:12` | `cowrie.client.kex` |
| `2026-08-19 01:37:12` | `cowrie.login.success` |
| `2026-08-19 01:37:13` | `cowrie.session.params` |
| `2026-08-19 01:37:13` | `cowrie.command.input` |
| `2026-08-19 01:37:13` | `cowrie.log.closed` |
| `2026-08-19 01:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eac81f5bd01

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 01:40 |
| **Last Seen** | 2026-08-19 01:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:40:25` | `cowrie.session.connect` |
| `2026-08-19 01:40:25` | `cowrie.client.version` |
| `2026-08-19 01:40:25` | `cowrie.client.kex` |
| `2026-08-19 01:40:25` | `cowrie.login.success` |
| `2026-08-19 01:40:25` | `cowrie.direct-tcpip.request` |
| `2026-08-19 01:40:26` | `cowrie.direct-tcpip.data` |
| `2026-08-19 01:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61e441febc66

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]134` |
| **First Seen** | 2026-08-19 01:41 |
| **Last Seen** | 2026-08-19 01:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:41:53` | `cowrie.session.connect` |
| `2026-08-19 01:41:53` | `cowrie.client.version` |
| `2026-08-19 01:41:53` | `cowrie.client.kex` |
| `2026-08-19 01:41:54` | `cowrie.login.success` |
| `2026-08-19 01:41:55` | `cowrie.session.params` |
| `2026-08-19 01:41:55` | `cowrie.command.input` |
| `2026-08-19 01:41:55` | `cowrie.command.failed` |
| `2026-08-19 01:41:56` | `cowrie.log.closed` |
| `2026-08-19 01:41:57` | `cowrie.session.params` |
| `2026-08-19 01:41:57` | `cowrie.command.input` |
| `2026-08-19 01:41:57` | `cowrie.session.file_download` |
| `2026-08-19 01:41:57` | `cowrie.log.closed` |
| `2026-08-19 01:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]134` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d219a54503c9

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]134` |
| **First Seen** | 2026-08-19 01:41 |
| **Last Seen** | 2026-08-19 01:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:41:58` | `cowrie.session.connect` |
| `2026-08-19 01:41:58` | `cowrie.client.version` |
| `2026-08-19 01:41:58` | `cowrie.client.kex` |
| `2026-08-19 01:41:59` | `cowrie.login.success` |
| `2026-08-19 01:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]134` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a379e2910ea1

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]134` |
| **First Seen** | 2026-08-19 01:41 |
| **Last Seen** | 2026-08-19 01:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:41:59` | `cowrie.session.connect` |
| `2026-08-19 01:41:59` | `cowrie.client.version` |
| `2026-08-19 01:42:00` | `cowrie.client.kex` |
| `2026-08-19 01:42:01` | `cowrie.login.success` |
| `2026-08-19 01:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]134` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9a141008949

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 01:43 |
| **Last Seen** | 2026-08-19 01:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:43:07` | `cowrie.session.connect` |
| `2026-08-19 01:43:07` | `cowrie.client.version` |
| `2026-08-19 01:43:07` | `cowrie.client.kex` |
| `2026-08-19 01:43:07` | `cowrie.login.success` |
| `2026-08-19 01:43:08` | `cowrie.session.params` |
| `2026-08-19 01:43:08` | `cowrie.command.input` |
| `2026-08-19 01:43:08` | `cowrie.log.closed` |
| `2026-08-19 01:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bbf6fb52bcb

| Field | Detail |
|---|---|
| **Source IP** | `119.96.173[.]169` |
| **First Seen** | 2026-08-19 01:47 |
| **Last Seen** | 2026-08-19 01:48 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:47:55` | `cowrie.session.connect` |
| `2026-08-19 01:47:55` | `cowrie.client.version` |
| `2026-08-19 01:47:56` | `cowrie.client.kex` |
| `2026-08-19 01:47:56` | `cowrie.login.success` |
| `2026-08-19 01:47:57` | `cowrie.session.params` |
| `2026-08-19 01:47:57` | `cowrie.command.input` |
| `2026-08-19 01:47:57` | `cowrie.command.failed` |
| `2026-08-19 01:47:58` | `cowrie.log.closed` |
| `2026-08-19 01:47:59` | `cowrie.session.params` |
| `2026-08-19 01:47:59` | `cowrie.command.input` |
| `2026-08-19 01:47:59` | `cowrie.session.file_download` |
| `2026-08-19 01:47:59` | `cowrie.log.closed` |
| `2026-08-19 01:48:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.173[.]169` to AbuseIPDB if not already reported
- [ ] Block `119.96.173[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4625960de80

| Field | Detail |
|---|---|
| **Source IP** | `119.96.173[.]169` |
| **First Seen** | 2026-08-19 01:48 |
| **Last Seen** | 2026-08-19 01:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:48:07` | `cowrie.session.connect` |
| `2026-08-19 01:48:07` | `cowrie.client.version` |
| `2026-08-19 01:48:07` | `cowrie.client.kex` |
| `2026-08-19 01:48:08` | `cowrie.login.success` |
| `2026-08-19 01:48:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.173[.]169` to AbuseIPDB if not already reported
- [ ] Block `119.96.173[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef0c461ff52

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 01:49 |
| **Last Seen** | 2026-08-19 01:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:49:02` | `cowrie.session.connect` |
| `2026-08-19 01:49:02` | `cowrie.client.version` |
| `2026-08-19 01:49:02` | `cowrie.client.kex` |
| `2026-08-19 01:49:02` | `cowrie.login.success` |
| `2026-08-19 01:49:03` | `cowrie.session.params` |
| `2026-08-19 01:49:03` | `cowrie.command.input` |
| `2026-08-19 01:49:03` | `cowrie.log.closed` |
| `2026-08-19 01:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b92d9cf6920

| Field | Detail |
|---|---|
| **Source IP** | `221.162.218[.]85` |
| **First Seen** | 2026-08-19 01:51 |
| **Last Seen** | 2026-08-19 01:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:51:56` | `cowrie.session.connect` |
| `2026-08-19 01:51:56` | `cowrie.client.version` |
| `2026-08-19 01:51:56` | `cowrie.client.kex` |
| `2026-08-19 01:51:57` | `cowrie.login.success` |
| `2026-08-19 01:51:58` | `cowrie.session.params` |
| `2026-08-19 01:51:58` | `cowrie.command.input` |
| `2026-08-19 01:51:58` | `cowrie.command.failed` |
| `2026-08-19 01:51:58` | `cowrie.log.closed` |
| `2026-08-19 01:51:59` | `cowrie.session.params` |
| `2026-08-19 01:51:59` | `cowrie.command.input` |
| `2026-08-19 01:51:59` | `cowrie.session.file_download` |
| `2026-08-19 01:51:59` | `cowrie.log.closed` |
| `2026-08-19 01:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.162.218[.]85` to AbuseIPDB if not already reported
- [ ] Block `221.162.218[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7950d5b249a

| Field | Detail |
|---|---|
| **Source IP** | `221.162.218[.]85` |
| **First Seen** | 2026-08-19 01:51 |
| **Last Seen** | 2026-08-19 01:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:51:59` | `cowrie.session.connect` |
| `2026-08-19 01:51:59` | `cowrie.client.version` |
| `2026-08-19 01:52:00` | `cowrie.client.kex` |
| `2026-08-19 01:52:00` | `cowrie.login.success` |
| `2026-08-19 01:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.162.218[.]85` to AbuseIPDB if not already reported
- [ ] Block `221.162.218[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab51be13a89

| Field | Detail |
|---|---|
| **Source IP** | `221.162.218[.]85` |
| **First Seen** | 2026-08-19 01:52 |
| **Last Seen** | 2026-08-19 01:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:52:01` | `cowrie.session.connect` |
| `2026-08-19 01:52:01` | `cowrie.client.version` |
| `2026-08-19 01:52:01` | `cowrie.client.kex` |
| `2026-08-19 01:52:02` | `cowrie.login.success` |
| `2026-08-19 01:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.162.218[.]85` to AbuseIPDB if not already reported
- [ ] Block `221.162.218[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b1c7449fa2

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 01:54 |
| **Last Seen** | 2026-08-19 01:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:54:57` | `cowrie.session.connect` |
| `2026-08-19 01:54:57` | `cowrie.client.version` |
| `2026-08-19 01:54:57` | `cowrie.client.kex` |
| `2026-08-19 01:54:57` | `cowrie.login.success` |
| `2026-08-19 01:54:58` | `cowrie.session.params` |
| `2026-08-19 01:54:58` | `cowrie.command.input` |
| `2026-08-19 01:54:58` | `cowrie.log.closed` |
| `2026-08-19 01:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-680f3603fa07

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-08-19 01:56 |
| **Last Seen** | 2026-08-19 01:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:56:24` | `cowrie.session.connect` |
| `2026-08-19 01:56:24` | `cowrie.client.version` |
| `2026-08-19 01:56:24` | `cowrie.client.kex` |
| `2026-08-19 01:56:24` | `cowrie.login.success` |
| `2026-08-19 01:56:24` | `cowrie.session.params` |
| `2026-08-19 01:56:24` | `cowrie.command.input` |
| `2026-08-19 01:56:24` | `cowrie.command.failed` |
| `2026-08-19 01:56:24` | `cowrie.log.closed` |
| `2026-08-19 01:56:25` | `cowrie.session.params` |
| `2026-08-19 01:56:25` | `cowrie.command.input` |
| `2026-08-19 01:56:25` | `cowrie.session.file_download` |
| `2026-08-19 01:56:25` | `cowrie.log.closed` |
| `2026-08-19 01:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab0d83b89d3e

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-08-19 01:56 |
| **Last Seen** | 2026-08-19 01:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:56:25` | `cowrie.session.connect` |
| `2026-08-19 01:56:25` | `cowrie.client.version` |
| `2026-08-19 01:56:25` | `cowrie.client.kex` |
| `2026-08-19 01:56:25` | `cowrie.login.success` |
| `2026-08-19 01:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-002bf99d50ac

| Field | Detail |
|---|---|
| **Source IP** | `50.6.228[.]111` |
| **First Seen** | 2026-08-19 01:56 |
| **Last Seen** | 2026-08-19 01:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 01:56:25` | `cowrie.session.connect` |
| `2026-08-19 01:56:25` | `cowrie.client.version` |
| `2026-08-19 01:56:25` | `cowrie.client.kex` |
| `2026-08-19 01:56:25` | `cowrie.login.success` |
| `2026-08-19 01:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.228[.]111` to AbuseIPDB if not already reported
- [ ] Block `50.6.228[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e07483766d

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 02:00 |
| **Last Seen** | 2026-08-19 02:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:00:52` | `cowrie.session.connect` |
| `2026-08-19 02:00:52` | `cowrie.client.version` |
| `2026-08-19 02:00:52` | `cowrie.client.kex` |
| `2026-08-19 02:00:52` | `cowrie.login.success` |
| `2026-08-19 02:00:53` | `cowrie.session.params` |
| `2026-08-19 02:00:53` | `cowrie.command.input` |
| `2026-08-19 02:00:53` | `cowrie.log.closed` |
| `2026-08-19 02:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-780e8d9002da

| Field | Detail |
|---|---|
| **Source IP** | `62.91.108[.]146` |
| **First Seen** | 2026-08-19 02:03 |
| **Last Seen** | 2026-08-19 02:03 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:03:26` | `cowrie.session.connect` |
| `2026-08-19 02:03:29` | `cowrie.client.version` |
| `2026-08-19 02:03:29` | `cowrie.client.kex` |
| `2026-08-19 02:03:38` | `cowrie.login.success` |
| `2026-08-19 02:03:42` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.91.108[.]146` to AbuseIPDB if not already reported
- [ ] Block `62.91.108[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58fc6ce9434a

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]50` |
| **First Seen** | 2026-08-19 02:03 |
| **Last Seen** | 2026-08-19 02:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:03:49` | `cowrie.session.connect` |
| `2026-08-19 02:03:49` | `cowrie.client.version` |
| `2026-08-19 02:03:49` | `cowrie.client.kex` |
| `2026-08-19 02:03:50` | `cowrie.login.success` |
| `2026-08-19 02:03:51` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]50` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b2026ab24ba

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 02:06 |
| **Last Seen** | 2026-08-19 02:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:06:47` | `cowrie.session.connect` |
| `2026-08-19 02:06:47` | `cowrie.client.version` |
| `2026-08-19 02:06:47` | `cowrie.client.kex` |
| `2026-08-19 02:06:47` | `cowrie.login.success` |
| `2026-08-19 02:06:48` | `cowrie.session.params` |
| `2026-08-19 02:06:48` | `cowrie.command.input` |
| `2026-08-19 02:06:48` | `cowrie.log.closed` |
| `2026-08-19 02:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24d4246d44c5

| Field | Detail |
|---|---|
| **Source IP** | `196.203.231[.]220` |
| **First Seen** | 2026-08-19 02:07 |
| **Last Seen** | 2026-08-19 02:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:07:09` | `cowrie.session.connect` |
| `2026-08-19 02:07:09` | `cowrie.client.version` |
| `2026-08-19 02:07:09` | `cowrie.client.kex` |
| `2026-08-19 02:07:11` | `cowrie.login.success` |
| `2026-08-19 02:07:11` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.203.231[.]220` to AbuseIPDB if not already reported
- [ ] Block `196.203.231[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcb1acf39c34

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 02:12 |
| **Last Seen** | 2026-08-19 02:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:12:42` | `cowrie.session.connect` |
| `2026-08-19 02:12:42` | `cowrie.client.version` |
| `2026-08-19 02:12:42` | `cowrie.client.kex` |
| `2026-08-19 02:12:42` | `cowrie.login.success` |
| `2026-08-19 02:12:43` | `cowrie.session.params` |
| `2026-08-19 02:12:43` | `cowrie.command.input` |
| `2026-08-19 02:12:43` | `cowrie.log.closed` |
| `2026-08-19 02:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6db29575d5

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 02:18 |
| **Last Seen** | 2026-08-19 02:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:18:37` | `cowrie.session.connect` |
| `2026-08-19 02:18:37` | `cowrie.client.version` |
| `2026-08-19 02:18:38` | `cowrie.client.kex` |
| `2026-08-19 02:18:38` | `cowrie.login.success` |
| `2026-08-19 02:18:38` | `cowrie.session.params` |
| `2026-08-19 02:18:38` | `cowrie.command.input` |
| `2026-08-19 02:18:39` | `cowrie.log.closed` |
| `2026-08-19 02:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97650e03f5dc

| Field | Detail |
|---|---|
| **Source IP** | `125.72.150[.]250` |
| **First Seen** | 2026-08-19 02:18 |
| **Last Seen** | 2026-08-19 02:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:18:46` | `cowrie.session.connect` |
| `2026-08-19 02:18:47` | `cowrie.client.version` |
| `2026-08-19 02:18:47` | `cowrie.client.kex` |
| `2026-08-19 02:18:49` | `cowrie.login.success` |
| `2026-08-19 02:18:50` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.72.150[.]250` to AbuseIPDB if not already reported
- [ ] Block `125.72.150[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6726aa202d83

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-19 02:18 |
| **Last Seen** | 2026-08-19 02:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:18:56` | `cowrie.session.connect` |
| `2026-08-19 02:18:57` | `cowrie.client.version` |
| `2026-08-19 02:18:57` | `cowrie.client.kex` |
| `2026-08-19 02:19:00` | `cowrie.login.success` |
| `2026-08-19 02:19:01` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc577cbe060

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 02:24 |
| **Last Seen** | 2026-08-19 02:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:24:33` | `cowrie.session.connect` |
| `2026-08-19 02:24:33` | `cowrie.client.version` |
| `2026-08-19 02:24:33` | `cowrie.client.kex` |
| `2026-08-19 02:24:33` | `cowrie.login.success` |
| `2026-08-19 02:24:34` | `cowrie.session.params` |
| `2026-08-19 02:24:34` | `cowrie.command.input` |
| `2026-08-19 02:24:34` | `cowrie.log.closed` |
| `2026-08-19 02:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d90a2da96011

| Field | Detail |
|---|---|
| **Source IP** | `108.46.229[.]102` |
| **First Seen** | 2026-08-19 02:29 |
| **Last Seen** | 2026-08-19 02:30 |
| **Session Duration** | 71s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:29:27` | `cowrie.session.connect` |
| `2026-08-19 02:29:27` | `cowrie.client.version` |
| `2026-08-19 02:29:28` | `cowrie.client.kex` |
| `2026-08-19 02:29:32` | `cowrie.login.failed` |
| `2026-08-19 02:29:33` | `cowrie.login.success` |
| `2026-08-19 02:29:34` | `cowrie.session.params` |
| `2026-08-19 02:29:34` | `cowrie.command.input` |
| `2026-08-19 02:29:34` | `cowrie.command.failed` |
| `2026-08-19 02:29:34` | `cowrie.log.closed` |
| `2026-08-19 02:29:34` | `cowrie.session.params` |
| `2026-08-19 02:29:34` | `cowrie.command.input` |
| `2026-08-19 02:29:34` | `cowrie.log.closed` |
| `2026-08-19 02:29:35` | `cowrie.session.params` |
| `2026-08-19 02:29:35` | `cowrie.command.input` |
| `2026-08-19 02:29:35` | `cowrie.log.closed` |
| `2026-08-19 02:29:36` | `cowrie.session.params` |
| `2026-08-19 02:29:36` | `cowrie.command.input` |
| `2026-08-19 02:29:36` | `cowrie.log.closed` |
| `2026-08-19 02:29:36` | `cowrie.session.params` |
| `2026-08-19 02:29:36` | `cowrie.command.input` |
| `2026-08-19 02:29:36` | `cowrie.log.closed` |
| `2026-08-19 02:29:37` | `cowrie.session.params` |
| `2026-08-19 02:29:37` | `cowrie.command.input` |
| `2026-08-19 02:29:37` | `cowrie.log.closed` |
| `2026-08-19 02:29:38` | `cowrie.session.params` |
| `2026-08-19 02:29:38` | `cowrie.command.input` |
| `2026-08-19 02:29:38` | `cowrie.log.closed` |
| `2026-08-19 02:29:38` | `cowrie.session.params` |
| `2026-08-19 02:29:38` | `cowrie.command.input` |
| `2026-08-19 02:29:39` | `cowrie.log.closed` |
| `2026-08-19 02:29:39` | `cowrie.session.params` |
| `2026-08-19 02:29:39` | `cowrie.command.input` |
| `2026-08-19 02:29:39` | `cowrie.log.closed` |
| `2026-08-19 02:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.46.229[.]102` to AbuseIPDB if not already reported
- [ ] Block `108.46.229[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cb546a10c27

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 02:30 |
| **Last Seen** | 2026-08-19 02:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:30:28` | `cowrie.session.connect` |
| `2026-08-19 02:30:28` | `cowrie.client.version` |
| `2026-08-19 02:30:28` | `cowrie.client.kex` |
| `2026-08-19 02:30:29` | `cowrie.login.success` |
| `2026-08-19 02:30:29` | `cowrie.session.params` |
| `2026-08-19 02:30:29` | `cowrie.command.input` |
| `2026-08-19 02:30:29` | `cowrie.log.closed` |
| `2026-08-19 02:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-856757d6ebe5

| Field | Detail |
|---|---|
| **Source IP** | `60.249.252[.]94` |
| **First Seen** | 2026-08-19 02:31 |
| **Last Seen** | 2026-08-19 02:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:31:39` | `cowrie.session.connect` |
| `2026-08-19 02:31:40` | `cowrie.client.version` |
| `2026-08-19 02:31:40` | `cowrie.client.kex` |
| `2026-08-19 02:31:42` | `cowrie.login.success` |
| `2026-08-19 02:31:43` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.252[.]94` to AbuseIPDB if not already reported
- [ ] Block `60.249.252[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59aea064e0bd

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-08-19 02:31 |
| **Last Seen** | 2026-08-19 02:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:31:50` | `cowrie.session.connect` |
| `2026-08-19 02:31:51` | `cowrie.client.version` |
| `2026-08-19 02:31:51` | `cowrie.client.kex` |
| `2026-08-19 02:31:52` | `cowrie.login.success` |
| `2026-08-19 02:31:53` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea06e91fdc2d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:13` | `cowrie.session.connect` |
| `2026-08-19 02:36:13` | `cowrie.client.version` |
| `2026-08-19 02:36:13` | `cowrie.client.kex` |
| `2026-08-19 02:36:13` | `cowrie.login.success` |
| `2026-08-19 02:36:14` | `cowrie.session.params` |
| `2026-08-19 02:36:14` | `cowrie.command.input` |
| `2026-08-19 02:36:15` | `cowrie.log.closed` |
| `2026-08-19 02:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c7bfd7e719

| Field | Detail |
|---|---|
| **Source IP** | `65.20.175[.]6` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:16` | `cowrie.session.connect` |
| `2026-08-19 02:36:16` | `cowrie.client.version` |
| `2026-08-19 02:36:16` | `cowrie.client.kex` |
| `2026-08-19 02:36:18` | `cowrie.login.success` |
| `2026-08-19 02:36:18` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.175[.]6` to AbuseIPDB if not already reported
- [ ] Block `65.20.175[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a45a4cbbc9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:20` | `cowrie.session.connect` |
| `2026-08-19 02:36:20` | `cowrie.client.version` |
| `2026-08-19 02:36:20` | `cowrie.client.kex` |
| `2026-08-19 02:36:20` | `cowrie.login.success` |
| `2026-08-19 02:36:21` | `cowrie.session.params` |
| `2026-08-19 02:36:21` | `cowrie.command.input` |
| `2026-08-19 02:36:21` | `cowrie.log.closed` |
| `2026-08-19 02:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827aca7027d9

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:23` | `cowrie.session.connect` |
| `2026-08-19 02:36:23` | `cowrie.client.version` |
| `2026-08-19 02:36:24` | `cowrie.client.kex` |
| `2026-08-19 02:36:24` | `cowrie.login.success` |
| `2026-08-19 02:36:25` | `cowrie.session.params` |
| `2026-08-19 02:36:25` | `cowrie.command.input` |
| `2026-08-19 02:36:25` | `cowrie.log.closed` |
| `2026-08-19 02:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94df19b61c96

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:23` | `cowrie.session.connect` |
| `2026-08-19 02:36:25` | `cowrie.client.version` |
| `2026-08-19 02:36:25` | `cowrie.client.kex` |
| `2026-08-19 02:36:27` | `cowrie.login.success` |
| `2026-08-19 02:36:28` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c08c3f3afb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:26` | `cowrie.session.connect` |
| `2026-08-19 02:36:26` | `cowrie.client.version` |
| `2026-08-19 02:36:26` | `cowrie.client.kex` |
| `2026-08-19 02:36:26` | `cowrie.login.success` |
| `2026-08-19 02:36:27` | `cowrie.session.params` |
| `2026-08-19 02:36:27` | `cowrie.command.input` |
| `2026-08-19 02:36:27` | `cowrie.log.closed` |
| `2026-08-19 02:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47cbd3475463

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:33` | `cowrie.session.connect` |
| `2026-08-19 02:36:33` | `cowrie.client.version` |
| `2026-08-19 02:36:33` | `cowrie.client.kex` |
| `2026-08-19 02:36:34` | `cowrie.login.success` |
| `2026-08-19 02:36:35` | `cowrie.session.params` |
| `2026-08-19 02:36:35` | `cowrie.command.input` |
| `2026-08-19 02:36:35` | `cowrie.log.closed` |
| `2026-08-19 02:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a016d0316997

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:38` | `cowrie.session.connect` |
| `2026-08-19 02:36:38` | `cowrie.client.version` |
| `2026-08-19 02:36:38` | `cowrie.client.kex` |
| `2026-08-19 02:36:39` | `cowrie.login.success` |
| `2026-08-19 02:36:40` | `cowrie.session.params` |
| `2026-08-19 02:36:40` | `cowrie.command.input` |
| `2026-08-19 02:36:40` | `cowrie.log.closed` |
| `2026-08-19 02:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e867a7e5135e

| Field | Detail |
|---|---|
| **Source IP** | `117.253.130[.]123` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:42` | `cowrie.session.connect` |
| `2026-08-19 02:36:43` | `cowrie.client.version` |
| `2026-08-19 02:36:43` | `cowrie.client.kex` |
| `2026-08-19 02:36:46` | `cowrie.login.success` |
| `2026-08-19 02:36:47` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.253.130[.]123` to AbuseIPDB if not already reported
- [ ] Block `117.253.130[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-065c138475f8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:44` | `cowrie.session.connect` |
| `2026-08-19 02:36:44` | `cowrie.client.version` |
| `2026-08-19 02:36:44` | `cowrie.client.kex` |
| `2026-08-19 02:36:45` | `cowrie.login.success` |
| `2026-08-19 02:36:45` | `cowrie.session.params` |
| `2026-08-19 02:36:45` | `cowrie.command.input` |
| `2026-08-19 02:36:45` | `cowrie.log.closed` |
| `2026-08-19 02:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eecab9a4fd40

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:51` | `cowrie.session.connect` |
| `2026-08-19 02:36:51` | `cowrie.client.version` |
| `2026-08-19 02:36:52` | `cowrie.client.kex` |
| `2026-08-19 02:36:52` | `cowrie.login.success` |
| `2026-08-19 02:36:53` | `cowrie.session.params` |
| `2026-08-19 02:36:53` | `cowrie.command.input` |
| `2026-08-19 02:36:53` | `cowrie.log.closed` |
| `2026-08-19 02:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d856a281d714

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:36 |
| **Last Seen** | 2026-08-19 02:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:36:57` | `cowrie.session.connect` |
| `2026-08-19 02:36:57` | `cowrie.client.version` |
| `2026-08-19 02:36:57` | `cowrie.client.kex` |
| `2026-08-19 02:36:57` | `cowrie.login.success` |
| `2026-08-19 02:36:58` | `cowrie.session.params` |
| `2026-08-19 02:36:58` | `cowrie.command.input` |
| `2026-08-19 02:36:58` | `cowrie.log.closed` |
| `2026-08-19 02:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caeed4aaf110

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:37 |
| **Last Seen** | 2026-08-19 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:37:03` | `cowrie.session.connect` |
| `2026-08-19 02:37:03` | `cowrie.client.version` |
| `2026-08-19 02:37:03` | `cowrie.client.kex` |
| `2026-08-19 02:37:04` | `cowrie.login.success` |
| `2026-08-19 02:37:04` | `cowrie.session.params` |
| `2026-08-19 02:37:04` | `cowrie.command.input` |
| `2026-08-19 02:37:04` | `cowrie.log.closed` |
| `2026-08-19 02:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b41fbc91367d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:37 |
| **Last Seen** | 2026-08-19 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:37:11` | `cowrie.session.connect` |
| `2026-08-19 02:37:11` | `cowrie.client.version` |
| `2026-08-19 02:37:11` | `cowrie.client.kex` |
| `2026-08-19 02:37:12` | `cowrie.login.success` |
| `2026-08-19 02:37:12` | `cowrie.session.params` |
| `2026-08-19 02:37:12` | `cowrie.command.input` |
| `2026-08-19 02:37:13` | `cowrie.log.closed` |
| `2026-08-19 02:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a72f85c3f7ed

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:37 |
| **Last Seen** | 2026-08-19 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:37:17` | `cowrie.session.connect` |
| `2026-08-19 02:37:17` | `cowrie.client.version` |
| `2026-08-19 02:37:17` | `cowrie.client.kex` |
| `2026-08-19 02:37:18` | `cowrie.login.success` |
| `2026-08-19 02:37:18` | `cowrie.session.params` |
| `2026-08-19 02:37:18` | `cowrie.command.input` |
| `2026-08-19 02:37:19` | `cowrie.log.closed` |
| `2026-08-19 02:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe0fd83135e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:37 |
| **Last Seen** | 2026-08-19 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:37:25` | `cowrie.session.connect` |
| `2026-08-19 02:37:25` | `cowrie.client.version` |
| `2026-08-19 02:37:25` | `cowrie.client.kex` |
| `2026-08-19 02:37:26` | `cowrie.login.success` |
| `2026-08-19 02:37:27` | `cowrie.session.params` |
| `2026-08-19 02:37:27` | `cowrie.command.input` |
| `2026-08-19 02:37:27` | `cowrie.log.closed` |
| `2026-08-19 02:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-225e41db1b8d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:37 |
| **Last Seen** | 2026-08-19 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:37:31` | `cowrie.session.connect` |
| `2026-08-19 02:37:31` | `cowrie.client.version` |
| `2026-08-19 02:37:31` | `cowrie.client.kex` |
| `2026-08-19 02:37:32` | `cowrie.login.success` |
| `2026-08-19 02:37:32` | `cowrie.session.params` |
| `2026-08-19 02:37:32` | `cowrie.command.input` |
| `2026-08-19 02:37:32` | `cowrie.log.closed` |
| `2026-08-19 02:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa6d08c17d31

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:37 |
| **Last Seen** | 2026-08-19 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:37:39` | `cowrie.session.connect` |
| `2026-08-19 02:37:39` | `cowrie.client.version` |
| `2026-08-19 02:37:39` | `cowrie.client.kex` |
| `2026-08-19 02:37:39` | `cowrie.login.success` |
| `2026-08-19 02:37:40` | `cowrie.session.params` |
| `2026-08-19 02:37:40` | `cowrie.command.input` |
| `2026-08-19 02:37:40` | `cowrie.log.closed` |
| `2026-08-19 02:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f22cbe3ba56

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:37 |
| **Last Seen** | 2026-08-19 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:37:45` | `cowrie.session.connect` |
| `2026-08-19 02:37:46` | `cowrie.client.version` |
| `2026-08-19 02:37:46` | `cowrie.client.kex` |
| `2026-08-19 02:37:46` | `cowrie.login.success` |
| `2026-08-19 02:37:47` | `cowrie.session.params` |
| `2026-08-19 02:37:47` | `cowrie.command.input` |
| `2026-08-19 02:37:47` | `cowrie.log.closed` |
| `2026-08-19 02:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a04019a21f4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:37 |
| **Last Seen** | 2026-08-19 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:37:53` | `cowrie.session.connect` |
| `2026-08-19 02:37:53` | `cowrie.client.version` |
| `2026-08-19 02:37:53` | `cowrie.client.kex` |
| `2026-08-19 02:37:53` | `cowrie.login.success` |
| `2026-08-19 02:37:54` | `cowrie.session.params` |
| `2026-08-19 02:37:54` | `cowrie.command.input` |
| `2026-08-19 02:37:54` | `cowrie.log.closed` |
| `2026-08-19 02:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6148538b308e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:37 |
| **Last Seen** | 2026-08-19 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:37:59` | `cowrie.session.connect` |
| `2026-08-19 02:37:59` | `cowrie.client.version` |
| `2026-08-19 02:37:59` | `cowrie.client.kex` |
| `2026-08-19 02:38:00` | `cowrie.login.success` |
| `2026-08-19 02:38:01` | `cowrie.session.params` |
| `2026-08-19 02:38:01` | `cowrie.command.input` |
| `2026-08-19 02:38:01` | `cowrie.log.closed` |
| `2026-08-19 02:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43463176afcd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:38 |
| **Last Seen** | 2026-08-19 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:38:06` | `cowrie.session.connect` |
| `2026-08-19 02:38:06` | `cowrie.client.version` |
| `2026-08-19 02:38:06` | `cowrie.client.kex` |
| `2026-08-19 02:38:06` | `cowrie.login.success` |
| `2026-08-19 02:38:07` | `cowrie.session.params` |
| `2026-08-19 02:38:07` | `cowrie.command.input` |
| `2026-08-19 02:38:07` | `cowrie.log.closed` |
| `2026-08-19 02:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f1c2f1d7a6d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:38 |
| **Last Seen** | 2026-08-19 02:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:38:12` | `cowrie.session.connect` |
| `2026-08-19 02:38:12` | `cowrie.client.version` |
| `2026-08-19 02:38:12` | `cowrie.client.kex` |
| `2026-08-19 02:38:13` | `cowrie.login.success` |
| `2026-08-19 02:38:14` | `cowrie.session.params` |
| `2026-08-19 02:38:14` | `cowrie.command.input` |
| `2026-08-19 02:38:14` | `cowrie.log.closed` |
| `2026-08-19 02:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1202d09c3fa3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:38 |
| **Last Seen** | 2026-08-19 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:38:19` | `cowrie.session.connect` |
| `2026-08-19 02:38:19` | `cowrie.client.version` |
| `2026-08-19 02:38:19` | `cowrie.client.kex` |
| `2026-08-19 02:38:19` | `cowrie.login.success` |
| `2026-08-19 02:38:20` | `cowrie.session.params` |
| `2026-08-19 02:38:20` | `cowrie.command.input` |
| `2026-08-19 02:38:20` | `cowrie.log.closed` |
| `2026-08-19 02:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f33e737e03

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:38 |
| **Last Seen** | 2026-08-19 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:38:26` | `cowrie.session.connect` |
| `2026-08-19 02:38:26` | `cowrie.client.version` |
| `2026-08-19 02:38:26` | `cowrie.client.kex` |
| `2026-08-19 02:38:26` | `cowrie.login.success` |
| `2026-08-19 02:38:27` | `cowrie.session.params` |
| `2026-08-19 02:38:27` | `cowrie.command.input` |
| `2026-08-19 02:38:27` | `cowrie.log.closed` |
| `2026-08-19 02:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a41e3d078d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:38 |
| **Last Seen** | 2026-08-19 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:38:32` | `cowrie.session.connect` |
| `2026-08-19 02:38:33` | `cowrie.client.version` |
| `2026-08-19 02:38:33` | `cowrie.client.kex` |
| `2026-08-19 02:38:33` | `cowrie.login.success` |
| `2026-08-19 02:38:34` | `cowrie.session.params` |
| `2026-08-19 02:38:34` | `cowrie.command.input` |
| `2026-08-19 02:38:34` | `cowrie.log.closed` |
| `2026-08-19 02:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91e8d9aa8d0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:38 |
| **Last Seen** | 2026-08-19 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:38:39` | `cowrie.session.connect` |
| `2026-08-19 02:38:39` | `cowrie.client.version` |
| `2026-08-19 02:38:39` | `cowrie.client.kex` |
| `2026-08-19 02:38:39` | `cowrie.login.success` |
| `2026-08-19 02:38:40` | `cowrie.session.params` |
| `2026-08-19 02:38:40` | `cowrie.command.input` |
| `2026-08-19 02:38:40` | `cowrie.log.closed` |
| `2026-08-19 02:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2b1cc8295a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:38 |
| **Last Seen** | 2026-08-19 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:38:46` | `cowrie.session.connect` |
| `2026-08-19 02:38:46` | `cowrie.client.version` |
| `2026-08-19 02:38:46` | `cowrie.client.kex` |
| `2026-08-19 02:38:46` | `cowrie.login.success` |
| `2026-08-19 02:38:47` | `cowrie.session.params` |
| `2026-08-19 02:38:47` | `cowrie.command.input` |
| `2026-08-19 02:38:47` | `cowrie.log.closed` |
| `2026-08-19 02:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a89c984847a6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:38 |
| **Last Seen** | 2026-08-19 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:38:52` | `cowrie.session.connect` |
| `2026-08-19 02:38:52` | `cowrie.client.version` |
| `2026-08-19 02:38:52` | `cowrie.client.kex` |
| `2026-08-19 02:38:53` | `cowrie.login.success` |
| `2026-08-19 02:38:54` | `cowrie.session.params` |
| `2026-08-19 02:38:54` | `cowrie.command.input` |
| `2026-08-19 02:38:54` | `cowrie.log.closed` |
| `2026-08-19 02:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c04a1062f5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:38 |
| **Last Seen** | 2026-08-19 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:38:59` | `cowrie.session.connect` |
| `2026-08-19 02:38:59` | `cowrie.client.version` |
| `2026-08-19 02:38:59` | `cowrie.client.kex` |
| `2026-08-19 02:39:00` | `cowrie.login.success` |
| `2026-08-19 02:39:00` | `cowrie.session.params` |
| `2026-08-19 02:39:00` | `cowrie.command.input` |
| `2026-08-19 02:39:00` | `cowrie.log.closed` |
| `2026-08-19 02:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82b7a2aceeeb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:39 |
| **Last Seen** | 2026-08-19 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:39:05` | `cowrie.session.connect` |
| `2026-08-19 02:39:05` | `cowrie.client.version` |
| `2026-08-19 02:39:05` | `cowrie.client.kex` |
| `2026-08-19 02:39:05` | `cowrie.login.success` |
| `2026-08-19 02:39:06` | `cowrie.session.params` |
| `2026-08-19 02:39:06` | `cowrie.command.input` |
| `2026-08-19 02:39:06` | `cowrie.log.closed` |
| `2026-08-19 02:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f104fe781e23

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:39 |
| **Last Seen** | 2026-08-19 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:39:12` | `cowrie.session.connect` |
| `2026-08-19 02:39:12` | `cowrie.client.version` |
| `2026-08-19 02:39:12` | `cowrie.client.kex` |
| `2026-08-19 02:39:12` | `cowrie.login.success` |
| `2026-08-19 02:39:13` | `cowrie.session.params` |
| `2026-08-19 02:39:13` | `cowrie.command.input` |
| `2026-08-19 02:39:13` | `cowrie.log.closed` |
| `2026-08-19 02:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d25b96ac7bf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:39 |
| **Last Seen** | 2026-08-19 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:39:17` | `cowrie.session.connect` |
| `2026-08-19 02:39:17` | `cowrie.client.version` |
| `2026-08-19 02:39:17` | `cowrie.client.kex` |
| `2026-08-19 02:39:18` | `cowrie.login.success` |
| `2026-08-19 02:39:18` | `cowrie.session.params` |
| `2026-08-19 02:39:18` | `cowrie.command.input` |
| `2026-08-19 02:39:19` | `cowrie.log.closed` |
| `2026-08-19 02:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d1d390c96e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:39 |
| **Last Seen** | 2026-08-19 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:39:24` | `cowrie.session.connect` |
| `2026-08-19 02:39:24` | `cowrie.client.version` |
| `2026-08-19 02:39:24` | `cowrie.client.kex` |
| `2026-08-19 02:39:25` | `cowrie.login.success` |
| `2026-08-19 02:39:26` | `cowrie.session.params` |
| `2026-08-19 02:39:26` | `cowrie.command.input` |
| `2026-08-19 02:39:26` | `cowrie.log.closed` |
| `2026-08-19 02:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faeb36f0cfb0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:39 |
| **Last Seen** | 2026-08-19 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:39:31` | `cowrie.session.connect` |
| `2026-08-19 02:39:31` | `cowrie.client.version` |
| `2026-08-19 02:39:31` | `cowrie.client.kex` |
| `2026-08-19 02:39:32` | `cowrie.login.success` |
| `2026-08-19 02:39:33` | `cowrie.session.params` |
| `2026-08-19 02:39:33` | `cowrie.command.input` |
| `2026-08-19 02:39:33` | `cowrie.log.closed` |
| `2026-08-19 02:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93094ba74ebb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:39 |
| **Last Seen** | 2026-08-19 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:39:39` | `cowrie.session.connect` |
| `2026-08-19 02:39:39` | `cowrie.client.version` |
| `2026-08-19 02:39:39` | `cowrie.client.kex` |
| `2026-08-19 02:39:39` | `cowrie.login.success` |
| `2026-08-19 02:39:40` | `cowrie.session.params` |
| `2026-08-19 02:39:40` | `cowrie.command.input` |
| `2026-08-19 02:39:40` | `cowrie.log.closed` |
| `2026-08-19 02:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-597460f080c8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:39 |
| **Last Seen** | 2026-08-19 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:39:47` | `cowrie.session.connect` |
| `2026-08-19 02:39:47` | `cowrie.client.version` |
| `2026-08-19 02:39:47` | `cowrie.client.kex` |
| `2026-08-19 02:39:47` | `cowrie.login.success` |
| `2026-08-19 02:39:48` | `cowrie.session.params` |
| `2026-08-19 02:39:48` | `cowrie.command.input` |
| `2026-08-19 02:39:48` | `cowrie.log.closed` |
| `2026-08-19 02:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd04ccdfcb9a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:39 |
| **Last Seen** | 2026-08-19 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:39:53` | `cowrie.session.connect` |
| `2026-08-19 02:39:53` | `cowrie.client.version` |
| `2026-08-19 02:39:53` | `cowrie.client.kex` |
| `2026-08-19 02:39:53` | `cowrie.login.success` |
| `2026-08-19 02:39:54` | `cowrie.session.params` |
| `2026-08-19 02:39:54` | `cowrie.command.input` |
| `2026-08-19 02:39:55` | `cowrie.log.closed` |
| `2026-08-19 02:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64efbe70bbd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:00` | `cowrie.session.connect` |
| `2026-08-19 02:40:00` | `cowrie.client.version` |
| `2026-08-19 02:40:00` | `cowrie.client.kex` |
| `2026-08-19 02:40:01` | `cowrie.login.success` |
| `2026-08-19 02:40:01` | `cowrie.session.params` |
| `2026-08-19 02:40:01` | `cowrie.command.input` |
| `2026-08-19 02:40:01` | `cowrie.log.closed` |
| `2026-08-19 02:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ea51431ee8

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:06` | `cowrie.session.connect` |
| `2026-08-19 02:40:07` | `cowrie.client.version` |
| `2026-08-19 02:40:07` | `cowrie.client.kex` |
| `2026-08-19 02:40:08` | `cowrie.login.success` |
| `2026-08-19 02:40:08` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12cf7887a2d0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:07` | `cowrie.session.connect` |
| `2026-08-19 02:40:07` | `cowrie.client.version` |
| `2026-08-19 02:40:07` | `cowrie.client.kex` |
| `2026-08-19 02:40:07` | `cowrie.login.success` |
| `2026-08-19 02:40:08` | `cowrie.session.params` |
| `2026-08-19 02:40:08` | `cowrie.command.input` |
| `2026-08-19 02:40:08` | `cowrie.log.closed` |
| `2026-08-19 02:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eea9a0e26f90

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:13` | `cowrie.session.connect` |
| `2026-08-19 02:40:13` | `cowrie.client.version` |
| `2026-08-19 02:40:13` | `cowrie.client.kex` |
| `2026-08-19 02:40:14` | `cowrie.login.success` |
| `2026-08-19 02:40:15` | `cowrie.session.params` |
| `2026-08-19 02:40:15` | `cowrie.command.input` |
| `2026-08-19 02:40:15` | `cowrie.log.closed` |
| `2026-08-19 02:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31f47d9a8c3

| Field | Detail |
|---|---|
| **Source IP** | `174.94.236[.]211` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:14` | `cowrie.session.connect` |
| `2026-08-19 02:40:15` | `cowrie.client.version` |
| `2026-08-19 02:40:15` | `cowrie.client.kex` |
| `2026-08-19 02:40:16` | `cowrie.login.success` |
| `2026-08-19 02:40:16` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.94.236[.]211` to AbuseIPDB if not already reported
- [ ] Block `174.94.236[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-953740970990

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:19` | `cowrie.session.connect` |
| `2026-08-19 02:40:20` | `cowrie.client.version` |
| `2026-08-19 02:40:20` | `cowrie.client.kex` |
| `2026-08-19 02:40:21` | `cowrie.login.success` |
| `2026-08-19 02:40:22` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da7201b07c7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:20` | `cowrie.session.connect` |
| `2026-08-19 02:40:20` | `cowrie.client.version` |
| `2026-08-19 02:40:20` | `cowrie.client.kex` |
| `2026-08-19 02:40:21` | `cowrie.login.success` |
| `2026-08-19 02:40:21` | `cowrie.session.params` |
| `2026-08-19 02:40:21` | `cowrie.command.input` |
| `2026-08-19 02:40:21` | `cowrie.log.closed` |
| `2026-08-19 02:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a06959f1e1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:26` | `cowrie.session.connect` |
| `2026-08-19 02:40:26` | `cowrie.client.version` |
| `2026-08-19 02:40:26` | `cowrie.client.kex` |
| `2026-08-19 02:40:27` | `cowrie.login.success` |
| `2026-08-19 02:40:27` | `cowrie.session.params` |
| `2026-08-19 02:40:27` | `cowrie.command.input` |
| `2026-08-19 02:40:28` | `cowrie.log.closed` |
| `2026-08-19 02:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77d65471c3f

| Field | Detail |
|---|---|
| **Source IP** | `103.121.27[.]218` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:27` | `cowrie.session.connect` |
| `2026-08-19 02:40:28` | `cowrie.client.version` |
| `2026-08-19 02:40:28` | `cowrie.client.kex` |
| `2026-08-19 02:40:30` | `cowrie.login.success` |
| `2026-08-19 02:40:31` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.121.27[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cfa586654e9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:32` | `cowrie.session.connect` |
| `2026-08-19 02:40:32` | `cowrie.client.version` |
| `2026-08-19 02:40:33` | `cowrie.client.kex` |
| `2026-08-19 02:40:33` | `cowrie.login.success` |
| `2026-08-19 02:40:34` | `cowrie.session.params` |
| `2026-08-19 02:40:34` | `cowrie.command.input` |
| `2026-08-19 02:40:34` | `cowrie.log.closed` |
| `2026-08-19 02:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8804585637e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:39` | `cowrie.session.connect` |
| `2026-08-19 02:40:39` | `cowrie.client.version` |
| `2026-08-19 02:40:39` | `cowrie.client.kex` |
| `2026-08-19 02:40:39` | `cowrie.login.success` |
| `2026-08-19 02:40:40` | `cowrie.session.params` |
| `2026-08-19 02:40:40` | `cowrie.command.input` |
| `2026-08-19 02:40:40` | `cowrie.log.closed` |
| `2026-08-19 02:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2948a4943127

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:44` | `cowrie.session.connect` |
| `2026-08-19 02:40:44` | `cowrie.client.version` |
| `2026-08-19 02:40:44` | `cowrie.client.kex` |
| `2026-08-19 02:40:45` | `cowrie.login.success` |
| `2026-08-19 02:40:46` | `cowrie.session.params` |
| `2026-08-19 02:40:46` | `cowrie.command.input` |
| `2026-08-19 02:40:46` | `cowrie.log.closed` |
| `2026-08-19 02:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd671df57f2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:51` | `cowrie.session.connect` |
| `2026-08-19 02:40:51` | `cowrie.client.version` |
| `2026-08-19 02:40:51` | `cowrie.client.kex` |
| `2026-08-19 02:40:51` | `cowrie.login.success` |
| `2026-08-19 02:40:52` | `cowrie.session.params` |
| `2026-08-19 02:40:52` | `cowrie.command.input` |
| `2026-08-19 02:40:52` | `cowrie.log.closed` |
| `2026-08-19 02:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f09a35853130

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:40 |
| **Last Seen** | 2026-08-19 02:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:40:57` | `cowrie.session.connect` |
| `2026-08-19 02:40:57` | `cowrie.client.version` |
| `2026-08-19 02:40:57` | `cowrie.client.kex` |
| `2026-08-19 02:40:58` | `cowrie.login.success` |
| `2026-08-19 02:40:58` | `cowrie.session.params` |
| `2026-08-19 02:40:58` | `cowrie.command.input` |
| `2026-08-19 02:40:59` | `cowrie.log.closed` |
| `2026-08-19 02:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c7dc5f8849

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:41 |
| **Last Seen** | 2026-08-19 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:41:03` | `cowrie.session.connect` |
| `2026-08-19 02:41:03` | `cowrie.client.version` |
| `2026-08-19 02:41:03` | `cowrie.client.kex` |
| `2026-08-19 02:41:03` | `cowrie.login.success` |
| `2026-08-19 02:41:04` | `cowrie.session.params` |
| `2026-08-19 02:41:04` | `cowrie.command.input` |
| `2026-08-19 02:41:04` | `cowrie.log.closed` |
| `2026-08-19 02:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaa703d5a0d9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:41 |
| **Last Seen** | 2026-08-19 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:41:09` | `cowrie.session.connect` |
| `2026-08-19 02:41:09` | `cowrie.client.version` |
| `2026-08-19 02:41:09` | `cowrie.client.kex` |
| `2026-08-19 02:41:10` | `cowrie.login.success` |
| `2026-08-19 02:41:11` | `cowrie.session.params` |
| `2026-08-19 02:41:11` | `cowrie.command.input` |
| `2026-08-19 02:41:11` | `cowrie.log.closed` |
| `2026-08-19 02:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8f096e29330

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:41 |
| **Last Seen** | 2026-08-19 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:41:14` | `cowrie.session.connect` |
| `2026-08-19 02:41:14` | `cowrie.client.version` |
| `2026-08-19 02:41:15` | `cowrie.client.kex` |
| `2026-08-19 02:41:15` | `cowrie.login.success` |
| `2026-08-19 02:41:16` | `cowrie.session.params` |
| `2026-08-19 02:41:16` | `cowrie.command.input` |
| `2026-08-19 02:41:16` | `cowrie.log.closed` |
| `2026-08-19 02:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568011296f45

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:41 |
| **Last Seen** | 2026-08-19 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:41:21` | `cowrie.session.connect` |
| `2026-08-19 02:41:21` | `cowrie.client.version` |
| `2026-08-19 02:41:21` | `cowrie.client.kex` |
| `2026-08-19 02:41:21` | `cowrie.login.success` |
| `2026-08-19 02:41:22` | `cowrie.session.params` |
| `2026-08-19 02:41:22` | `cowrie.command.input` |
| `2026-08-19 02:41:22` | `cowrie.log.closed` |
| `2026-08-19 02:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d3bf6761ff1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:41 |
| **Last Seen** | 2026-08-19 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:41:28` | `cowrie.session.connect` |
| `2026-08-19 02:41:28` | `cowrie.client.version` |
| `2026-08-19 02:41:28` | `cowrie.client.kex` |
| `2026-08-19 02:41:29` | `cowrie.login.success` |
| `2026-08-19 02:41:29` | `cowrie.session.params` |
| `2026-08-19 02:41:29` | `cowrie.command.input` |
| `2026-08-19 02:41:29` | `cowrie.log.closed` |
| `2026-08-19 02:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0233ec3b5954

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:41 |
| **Last Seen** | 2026-08-19 02:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:41:34` | `cowrie.session.connect` |
| `2026-08-19 02:41:35` | `cowrie.client.version` |
| `2026-08-19 02:41:35` | `cowrie.client.kex` |
| `2026-08-19 02:41:35` | `cowrie.login.success` |
| `2026-08-19 02:41:36` | `cowrie.session.params` |
| `2026-08-19 02:41:36` | `cowrie.command.input` |
| `2026-08-19 02:41:36` | `cowrie.log.closed` |
| `2026-08-19 02:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ecaf987cbd7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:41 |
| **Last Seen** | 2026-08-19 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:41:42` | `cowrie.session.connect` |
| `2026-08-19 02:41:42` | `cowrie.client.version` |
| `2026-08-19 02:41:42` | `cowrie.client.kex` |
| `2026-08-19 02:41:42` | `cowrie.login.success` |
| `2026-08-19 02:41:43` | `cowrie.session.params` |
| `2026-08-19 02:41:43` | `cowrie.command.input` |
| `2026-08-19 02:41:43` | `cowrie.log.closed` |
| `2026-08-19 02:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4eb24690807

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:41 |
| **Last Seen** | 2026-08-19 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:41:49` | `cowrie.session.connect` |
| `2026-08-19 02:41:49` | `cowrie.client.version` |
| `2026-08-19 02:41:50` | `cowrie.client.kex` |
| `2026-08-19 02:41:50` | `cowrie.login.success` |
| `2026-08-19 02:41:51` | `cowrie.session.params` |
| `2026-08-19 02:41:51` | `cowrie.command.input` |
| `2026-08-19 02:41:51` | `cowrie.log.closed` |
| `2026-08-19 02:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428f7a2f3854

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:41 |
| **Last Seen** | 2026-08-19 02:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:41:56` | `cowrie.session.connect` |
| `2026-08-19 02:41:56` | `cowrie.client.version` |
| `2026-08-19 02:41:57` | `cowrie.client.kex` |
| `2026-08-19 02:41:57` | `cowrie.login.success` |
| `2026-08-19 02:41:58` | `cowrie.session.params` |
| `2026-08-19 02:41:58` | `cowrie.command.input` |
| `2026-08-19 02:41:58` | `cowrie.log.closed` |
| `2026-08-19 02:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9377c21d6bf2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:42 |
| **Last Seen** | 2026-08-19 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:42:03` | `cowrie.session.connect` |
| `2026-08-19 02:42:03` | `cowrie.client.version` |
| `2026-08-19 02:42:03` | `cowrie.client.kex` |
| `2026-08-19 02:42:03` | `cowrie.login.success` |
| `2026-08-19 02:42:04` | `cowrie.session.params` |
| `2026-08-19 02:42:04` | `cowrie.command.input` |
| `2026-08-19 02:42:04` | `cowrie.log.closed` |
| `2026-08-19 02:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17eed70edb8b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:42 |
| **Last Seen** | 2026-08-19 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:42:09` | `cowrie.session.connect` |
| `2026-08-19 02:42:09` | `cowrie.client.version` |
| `2026-08-19 02:42:09` | `cowrie.client.kex` |
| `2026-08-19 02:42:09` | `cowrie.login.success` |
| `2026-08-19 02:42:10` | `cowrie.session.params` |
| `2026-08-19 02:42:10` | `cowrie.command.input` |
| `2026-08-19 02:42:10` | `cowrie.log.closed` |
| `2026-08-19 02:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1168bb6bca8e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:42 |
| **Last Seen** | 2026-08-19 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:42:16` | `cowrie.session.connect` |
| `2026-08-19 02:42:16` | `cowrie.client.version` |
| `2026-08-19 02:42:16` | `cowrie.client.kex` |
| `2026-08-19 02:42:17` | `cowrie.login.success` |
| `2026-08-19 02:42:17` | `cowrie.session.params` |
| `2026-08-19 02:42:17` | `cowrie.command.input` |
| `2026-08-19 02:42:17` | `cowrie.log.closed` |
| `2026-08-19 02:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2d2c78a5da

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 02:42 |
| **Last Seen** | 2026-08-19 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:42:18` | `cowrie.session.connect` |
| `2026-08-19 02:42:18` | `cowrie.client.version` |
| `2026-08-19 02:42:18` | `cowrie.client.kex` |
| `2026-08-19 02:42:19` | `cowrie.login.success` |
| `2026-08-19 02:42:19` | `cowrie.session.params` |
| `2026-08-19 02:42:19` | `cowrie.command.input` |
| `2026-08-19 02:42:20` | `cowrie.log.closed` |
| `2026-08-19 02:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc36d9bba65b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:42 |
| **Last Seen** | 2026-08-19 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:42:23` | `cowrie.session.connect` |
| `2026-08-19 02:42:23` | `cowrie.client.version` |
| `2026-08-19 02:42:23` | `cowrie.client.kex` |
| `2026-08-19 02:42:23` | `cowrie.login.success` |
| `2026-08-19 02:42:24` | `cowrie.session.params` |
| `2026-08-19 02:42:24` | `cowrie.command.input` |
| `2026-08-19 02:42:24` | `cowrie.log.closed` |
| `2026-08-19 02:42:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de792e350a26

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:42 |
| **Last Seen** | 2026-08-19 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:42:29` | `cowrie.session.connect` |
| `2026-08-19 02:42:29` | `cowrie.client.version` |
| `2026-08-19 02:42:29` | `cowrie.client.kex` |
| `2026-08-19 02:42:29` | `cowrie.login.success` |
| `2026-08-19 02:42:30` | `cowrie.session.params` |
| `2026-08-19 02:42:30` | `cowrie.command.input` |
| `2026-08-19 02:42:30` | `cowrie.log.closed` |
| `2026-08-19 02:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30e8c34c1683

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:42 |
| **Last Seen** | 2026-08-19 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:42:36` | `cowrie.session.connect` |
| `2026-08-19 02:42:36` | `cowrie.client.version` |
| `2026-08-19 02:42:36` | `cowrie.client.kex` |
| `2026-08-19 02:42:36` | `cowrie.login.success` |
| `2026-08-19 02:42:37` | `cowrie.session.params` |
| `2026-08-19 02:42:37` | `cowrie.command.input` |
| `2026-08-19 02:42:37` | `cowrie.log.closed` |
| `2026-08-19 02:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06f9d5a6bb3f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:42 |
| **Last Seen** | 2026-08-19 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:42:43` | `cowrie.session.connect` |
| `2026-08-19 02:42:43` | `cowrie.client.version` |
| `2026-08-19 02:42:43` | `cowrie.client.kex` |
| `2026-08-19 02:42:43` | `cowrie.login.success` |
| `2026-08-19 02:42:44` | `cowrie.session.params` |
| `2026-08-19 02:42:44` | `cowrie.command.input` |
| `2026-08-19 02:42:44` | `cowrie.log.closed` |
| `2026-08-19 02:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b799bd9288a2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:42 |
| **Last Seen** | 2026-08-19 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:42:49` | `cowrie.session.connect` |
| `2026-08-19 02:42:50` | `cowrie.client.version` |
| `2026-08-19 02:42:50` | `cowrie.client.kex` |
| `2026-08-19 02:42:50` | `cowrie.login.success` |
| `2026-08-19 02:42:51` | `cowrie.session.params` |
| `2026-08-19 02:42:51` | `cowrie.command.input` |
| `2026-08-19 02:42:51` | `cowrie.log.closed` |
| `2026-08-19 02:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73ff8c8ddc8a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:42 |
| **Last Seen** | 2026-08-19 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:42:57` | `cowrie.session.connect` |
| `2026-08-19 02:42:57` | `cowrie.client.version` |
| `2026-08-19 02:42:57` | `cowrie.client.kex` |
| `2026-08-19 02:42:57` | `cowrie.login.success` |
| `2026-08-19 02:42:58` | `cowrie.session.params` |
| `2026-08-19 02:42:58` | `cowrie.command.input` |
| `2026-08-19 02:42:58` | `cowrie.log.closed` |
| `2026-08-19 02:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-650e3153f204

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:43 |
| **Last Seen** | 2026-08-19 02:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:43:03` | `cowrie.session.connect` |
| `2026-08-19 02:43:03` | `cowrie.client.version` |
| `2026-08-19 02:43:03` | `cowrie.client.kex` |
| `2026-08-19 02:43:04` | `cowrie.login.success` |
| `2026-08-19 02:43:05` | `cowrie.session.params` |
| `2026-08-19 02:43:05` | `cowrie.command.input` |
| `2026-08-19 02:43:05` | `cowrie.log.closed` |
| `2026-08-19 02:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24dba504159b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:43 |
| **Last Seen** | 2026-08-19 02:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:43:10` | `cowrie.session.connect` |
| `2026-08-19 02:43:10` | `cowrie.client.version` |
| `2026-08-19 02:43:10` | `cowrie.client.kex` |
| `2026-08-19 02:43:11` | `cowrie.login.success` |
| `2026-08-19 02:43:11` | `cowrie.session.params` |
| `2026-08-19 02:43:11` | `cowrie.command.input` |
| `2026-08-19 02:43:11` | `cowrie.log.closed` |
| `2026-08-19 02:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccafe076a177

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:43 |
| **Last Seen** | 2026-08-19 02:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:43:16` | `cowrie.session.connect` |
| `2026-08-19 02:43:17` | `cowrie.client.version` |
| `2026-08-19 02:43:17` | `cowrie.client.kex` |
| `2026-08-19 02:43:17` | `cowrie.login.success` |
| `2026-08-19 02:43:18` | `cowrie.session.params` |
| `2026-08-19 02:43:18` | `cowrie.command.input` |
| `2026-08-19 02:43:18` | `cowrie.log.closed` |
| `2026-08-19 02:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-614f5dee8bcf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:43 |
| **Last Seen** | 2026-08-19 02:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:43:22` | `cowrie.session.connect` |
| `2026-08-19 02:43:22` | `cowrie.client.version` |
| `2026-08-19 02:43:22` | `cowrie.client.kex` |
| `2026-08-19 02:43:23` | `cowrie.login.success` |
| `2026-08-19 02:43:24` | `cowrie.session.params` |
| `2026-08-19 02:43:24` | `cowrie.command.input` |
| `2026-08-19 02:43:24` | `cowrie.log.closed` |
| `2026-08-19 02:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f61390ad26

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:43 |
| **Last Seen** | 2026-08-19 02:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:43:34` | `cowrie.session.connect` |
| `2026-08-19 02:43:34` | `cowrie.client.version` |
| `2026-08-19 02:43:34` | `cowrie.client.kex` |
| `2026-08-19 02:43:35` | `cowrie.login.success` |
| `2026-08-19 02:43:36` | `cowrie.session.params` |
| `2026-08-19 02:43:36` | `cowrie.command.input` |
| `2026-08-19 02:43:36` | `cowrie.log.closed` |
| `2026-08-19 02:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38c7f2e3ace

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:43 |
| **Last Seen** | 2026-08-19 02:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:43:41` | `cowrie.session.connect` |
| `2026-08-19 02:43:41` | `cowrie.client.version` |
| `2026-08-19 02:43:41` | `cowrie.client.kex` |
| `2026-08-19 02:43:41` | `cowrie.login.success` |
| `2026-08-19 02:43:42` | `cowrie.session.params` |
| `2026-08-19 02:43:42` | `cowrie.command.input` |
| `2026-08-19 02:43:42` | `cowrie.log.closed` |
| `2026-08-19 02:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a081061ad0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:43 |
| **Last Seen** | 2026-08-19 02:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:43:47` | `cowrie.session.connect` |
| `2026-08-19 02:43:47` | `cowrie.client.version` |
| `2026-08-19 02:43:47` | `cowrie.client.kex` |
| `2026-08-19 02:43:48` | `cowrie.login.success` |
| `2026-08-19 02:43:49` | `cowrie.session.params` |
| `2026-08-19 02:43:49` | `cowrie.command.input` |
| `2026-08-19 02:43:49` | `cowrie.log.closed` |
| `2026-08-19 02:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5cbe7c43cb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:43 |
| **Last Seen** | 2026-08-19 02:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:43:55` | `cowrie.session.connect` |
| `2026-08-19 02:43:55` | `cowrie.client.version` |
| `2026-08-19 02:43:55` | `cowrie.client.kex` |
| `2026-08-19 02:43:56` | `cowrie.login.success` |
| `2026-08-19 02:43:56` | `cowrie.session.params` |
| `2026-08-19 02:43:56` | `cowrie.command.input` |
| `2026-08-19 02:43:57` | `cowrie.log.closed` |
| `2026-08-19 02:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-462b14b0ef12

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:01` | `cowrie.session.connect` |
| `2026-08-19 02:44:01` | `cowrie.client.version` |
| `2026-08-19 02:44:01` | `cowrie.client.kex` |
| `2026-08-19 02:44:01` | `cowrie.login.success` |
| `2026-08-19 02:44:02` | `cowrie.session.params` |
| `2026-08-19 02:44:02` | `cowrie.command.input` |
| `2026-08-19 02:44:02` | `cowrie.log.closed` |
| `2026-08-19 02:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f7ade65e9ac

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:07` | `cowrie.session.connect` |
| `2026-08-19 02:44:08` | `cowrie.client.version` |
| `2026-08-19 02:44:08` | `cowrie.client.kex` |
| `2026-08-19 02:44:08` | `cowrie.login.success` |
| `2026-08-19 02:44:09` | `cowrie.session.params` |
| `2026-08-19 02:44:09` | `cowrie.command.input` |
| `2026-08-19 02:44:09` | `cowrie.log.closed` |
| `2026-08-19 02:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718d9c1e30fc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:13` | `cowrie.session.connect` |
| `2026-08-19 02:44:13` | `cowrie.client.version` |
| `2026-08-19 02:44:13` | `cowrie.client.kex` |
| `2026-08-19 02:44:14` | `cowrie.login.success` |
| `2026-08-19 02:44:15` | `cowrie.session.params` |
| `2026-08-19 02:44:15` | `cowrie.command.input` |
| `2026-08-19 02:44:15` | `cowrie.log.closed` |
| `2026-08-19 02:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f851bf6a7322

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:19` | `cowrie.session.connect` |
| `2026-08-19 02:44:19` | `cowrie.client.version` |
| `2026-08-19 02:44:19` | `cowrie.client.kex` |
| `2026-08-19 02:44:19` | `cowrie.login.success` |
| `2026-08-19 02:44:20` | `cowrie.session.params` |
| `2026-08-19 02:44:20` | `cowrie.command.input` |
| `2026-08-19 02:44:20` | `cowrie.log.closed` |
| `2026-08-19 02:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39d0816d85a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:24` | `cowrie.session.connect` |
| `2026-08-19 02:44:24` | `cowrie.client.version` |
| `2026-08-19 02:44:24` | `cowrie.client.kex` |
| `2026-08-19 02:44:24` | `cowrie.login.success` |
| `2026-08-19 02:44:25` | `cowrie.session.params` |
| `2026-08-19 02:44:25` | `cowrie.command.input` |
| `2026-08-19 02:44:25` | `cowrie.log.closed` |
| `2026-08-19 02:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b53a3635db

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:30` | `cowrie.session.connect` |
| `2026-08-19 02:44:30` | `cowrie.client.version` |
| `2026-08-19 02:44:30` | `cowrie.client.kex` |
| `2026-08-19 02:44:31` | `cowrie.login.success` |
| `2026-08-19 02:44:32` | `cowrie.session.params` |
| `2026-08-19 02:44:32` | `cowrie.command.input` |
| `2026-08-19 02:44:32` | `cowrie.log.closed` |
| `2026-08-19 02:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9cc0a5ea21

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:36` | `cowrie.session.connect` |
| `2026-08-19 02:44:36` | `cowrie.client.version` |
| `2026-08-19 02:44:36` | `cowrie.client.kex` |
| `2026-08-19 02:44:37` | `cowrie.login.success` |
| `2026-08-19 02:44:37` | `cowrie.session.params` |
| `2026-08-19 02:44:37` | `cowrie.command.input` |
| `2026-08-19 02:44:38` | `cowrie.log.closed` |
| `2026-08-19 02:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd832b7f6ed

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:42` | `cowrie.session.connect` |
| `2026-08-19 02:44:42` | `cowrie.client.version` |
| `2026-08-19 02:44:42` | `cowrie.client.kex` |
| `2026-08-19 02:44:42` | `cowrie.login.success` |
| `2026-08-19 02:44:43` | `cowrie.session.params` |
| `2026-08-19 02:44:43` | `cowrie.command.input` |
| `2026-08-19 02:44:43` | `cowrie.log.closed` |
| `2026-08-19 02:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a66cd4cfba

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:49` | `cowrie.session.connect` |
| `2026-08-19 02:44:49` | `cowrie.client.version` |
| `2026-08-19 02:44:49` | `cowrie.client.kex` |
| `2026-08-19 02:44:49` | `cowrie.login.success` |
| `2026-08-19 02:44:50` | `cowrie.session.params` |
| `2026-08-19 02:44:50` | `cowrie.command.input` |
| `2026-08-19 02:44:50` | `cowrie.log.closed` |
| `2026-08-19 02:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0064f01ed492

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:51` | `cowrie.session.connect` |
| `2026-08-19 02:44:51` | `cowrie.client.version` |
| `2026-08-19 02:44:51` | `cowrie.client.kex` |
| `2026-08-19 02:44:51` | `cowrie.login.success` |
| `2026-08-19 02:44:51` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:44:52` | `cowrie.direct-tcpip.data` |
| `2026-08-19 02:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25c28b9f50d7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:44 |
| **Last Seen** | 2026-08-19 02:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:44:55` | `cowrie.session.connect` |
| `2026-08-19 02:44:55` | `cowrie.client.version` |
| `2026-08-19 02:44:55` | `cowrie.client.kex` |
| `2026-08-19 02:44:55` | `cowrie.login.success` |
| `2026-08-19 02:44:56` | `cowrie.session.params` |
| `2026-08-19 02:44:56` | `cowrie.command.input` |
| `2026-08-19 02:44:56` | `cowrie.log.closed` |
| `2026-08-19 02:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a044bfc1f14d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:01` | `cowrie.session.connect` |
| `2026-08-19 02:45:01` | `cowrie.client.version` |
| `2026-08-19 02:45:01` | `cowrie.client.kex` |
| `2026-08-19 02:45:01` | `cowrie.login.success` |
| `2026-08-19 02:45:02` | `cowrie.session.params` |
| `2026-08-19 02:45:02` | `cowrie.command.input` |
| `2026-08-19 02:45:02` | `cowrie.log.closed` |
| `2026-08-19 02:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b4904133fa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:05` | `cowrie.session.connect` |
| `2026-08-19 02:45:05` | `cowrie.client.version` |
| `2026-08-19 02:45:05` | `cowrie.client.kex` |
| `2026-08-19 02:45:06` | `cowrie.login.success` |
| `2026-08-19 02:45:07` | `cowrie.session.params` |
| `2026-08-19 02:45:07` | `cowrie.command.input` |
| `2026-08-19 02:45:07` | `cowrie.log.closed` |
| `2026-08-19 02:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf9835fc0d4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:11` | `cowrie.session.connect` |
| `2026-08-19 02:45:11` | `cowrie.client.version` |
| `2026-08-19 02:45:11` | `cowrie.client.kex` |
| `2026-08-19 02:45:11` | `cowrie.login.success` |
| `2026-08-19 02:45:12` | `cowrie.session.params` |
| `2026-08-19 02:45:12` | `cowrie.command.input` |
| `2026-08-19 02:45:12` | `cowrie.log.closed` |
| `2026-08-19 02:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa30b574a18a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:18` | `cowrie.session.connect` |
| `2026-08-19 02:45:18` | `cowrie.client.version` |
| `2026-08-19 02:45:18` | `cowrie.client.kex` |
| `2026-08-19 02:45:18` | `cowrie.login.success` |
| `2026-08-19 02:45:19` | `cowrie.session.params` |
| `2026-08-19 02:45:19` | `cowrie.command.input` |
| `2026-08-19 02:45:19` | `cowrie.log.closed` |
| `2026-08-19 02:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-188855537b29

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:24` | `cowrie.session.connect` |
| `2026-08-19 02:45:24` | `cowrie.client.version` |
| `2026-08-19 02:45:24` | `cowrie.client.kex` |
| `2026-08-19 02:45:25` | `cowrie.login.success` |
| `2026-08-19 02:45:25` | `cowrie.session.params` |
| `2026-08-19 02:45:25` | `cowrie.command.input` |
| `2026-08-19 02:45:26` | `cowrie.log.closed` |
| `2026-08-19 02:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67721e4e0d9d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:31` | `cowrie.session.connect` |
| `2026-08-19 02:45:31` | `cowrie.client.version` |
| `2026-08-19 02:45:31` | `cowrie.client.kex` |
| `2026-08-19 02:45:31` | `cowrie.login.success` |
| `2026-08-19 02:45:32` | `cowrie.session.params` |
| `2026-08-19 02:45:32` | `cowrie.command.input` |
| `2026-08-19 02:45:32` | `cowrie.log.closed` |
| `2026-08-19 02:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b46529458b0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:36` | `cowrie.session.connect` |
| `2026-08-19 02:45:36` | `cowrie.client.version` |
| `2026-08-19 02:45:36` | `cowrie.client.kex` |
| `2026-08-19 02:45:37` | `cowrie.login.success` |
| `2026-08-19 02:45:37` | `cowrie.session.params` |
| `2026-08-19 02:45:37` | `cowrie.command.input` |
| `2026-08-19 02:45:37` | `cowrie.log.closed` |
| `2026-08-19 02:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214ebf562e06

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:42` | `cowrie.session.connect` |
| `2026-08-19 02:45:42` | `cowrie.client.version` |
| `2026-08-19 02:45:42` | `cowrie.client.kex` |
| `2026-08-19 02:45:43` | `cowrie.login.success` |
| `2026-08-19 02:45:43` | `cowrie.session.params` |
| `2026-08-19 02:45:44` | `cowrie.command.input` |
| `2026-08-19 02:45:44` | `cowrie.log.closed` |
| `2026-08-19 02:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74e9af9b1f27

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:48` | `cowrie.session.connect` |
| `2026-08-19 02:45:48` | `cowrie.client.version` |
| `2026-08-19 02:45:48` | `cowrie.client.kex` |
| `2026-08-19 02:45:49` | `cowrie.login.success` |
| `2026-08-19 02:45:49` | `cowrie.session.params` |
| `2026-08-19 02:45:49` | `cowrie.command.input` |
| `2026-08-19 02:45:50` | `cowrie.log.closed` |
| `2026-08-19 02:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f5e3cb969d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:54` | `cowrie.session.connect` |
| `2026-08-19 02:45:54` | `cowrie.client.version` |
| `2026-08-19 02:45:54` | `cowrie.client.kex` |
| `2026-08-19 02:45:54` | `cowrie.login.success` |
| `2026-08-19 02:45:55` | `cowrie.session.params` |
| `2026-08-19 02:45:55` | `cowrie.command.input` |
| `2026-08-19 02:45:55` | `cowrie.log.closed` |
| `2026-08-19 02:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da2922c1190

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:45 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:45:59` | `cowrie.session.connect` |
| `2026-08-19 02:45:59` | `cowrie.client.version` |
| `2026-08-19 02:46:00` | `cowrie.client.kex` |
| `2026-08-19 02:46:00` | `cowrie.login.success` |
| `2026-08-19 02:46:01` | `cowrie.session.params` |
| `2026-08-19 02:46:01` | `cowrie.command.input` |
| `2026-08-19 02:46:01` | `cowrie.log.closed` |
| `2026-08-19 02:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e43118adf388

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:46 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:46:05` | `cowrie.session.connect` |
| `2026-08-19 02:46:05` | `cowrie.client.version` |
| `2026-08-19 02:46:05` | `cowrie.client.kex` |
| `2026-08-19 02:46:05` | `cowrie.login.success` |
| `2026-08-19 02:46:06` | `cowrie.session.params` |
| `2026-08-19 02:46:06` | `cowrie.command.input` |
| `2026-08-19 02:46:06` | `cowrie.log.closed` |
| `2026-08-19 02:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b68c48da176

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:46 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:46:10` | `cowrie.session.connect` |
| `2026-08-19 02:46:11` | `cowrie.client.version` |
| `2026-08-19 02:46:11` | `cowrie.client.kex` |
| `2026-08-19 02:46:11` | `cowrie.login.success` |
| `2026-08-19 02:46:12` | `cowrie.session.params` |
| `2026-08-19 02:46:12` | `cowrie.command.input` |
| `2026-08-19 02:46:12` | `cowrie.log.closed` |
| `2026-08-19 02:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03fafb1e35ad

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:46 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:46:16` | `cowrie.session.connect` |
| `2026-08-19 02:46:16` | `cowrie.client.version` |
| `2026-08-19 02:46:16` | `cowrie.client.kex` |
| `2026-08-19 02:46:17` | `cowrie.login.success` |
| `2026-08-19 02:46:18` | `cowrie.session.params` |
| `2026-08-19 02:46:18` | `cowrie.command.input` |
| `2026-08-19 02:46:18` | `cowrie.log.closed` |
| `2026-08-19 02:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d1bab9dcf67

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:46 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:46:21` | `cowrie.session.connect` |
| `2026-08-19 02:46:21` | `cowrie.client.version` |
| `2026-08-19 02:46:21` | `cowrie.client.kex` |
| `2026-08-19 02:46:22` | `cowrie.login.success` |
| `2026-08-19 02:46:23` | `cowrie.session.params` |
| `2026-08-19 02:46:23` | `cowrie.command.input` |
| `2026-08-19 02:46:23` | `cowrie.log.closed` |
| `2026-08-19 02:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9bb3e4f0a6a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:46 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:46:26` | `cowrie.session.connect` |
| `2026-08-19 02:46:26` | `cowrie.client.version` |
| `2026-08-19 02:46:26` | `cowrie.client.kex` |
| `2026-08-19 02:46:27` | `cowrie.login.success` |
| `2026-08-19 02:46:27` | `cowrie.session.params` |
| `2026-08-19 02:46:27` | `cowrie.command.input` |
| `2026-08-19 02:46:27` | `cowrie.log.closed` |
| `2026-08-19 02:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9c14f636cb0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:46 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:46:32` | `cowrie.session.connect` |
| `2026-08-19 02:46:32` | `cowrie.client.version` |
| `2026-08-19 02:46:32` | `cowrie.client.kex` |
| `2026-08-19 02:46:32` | `cowrie.login.success` |
| `2026-08-19 02:46:33` | `cowrie.session.params` |
| `2026-08-19 02:46:33` | `cowrie.command.input` |
| `2026-08-19 02:46:34` | `cowrie.log.closed` |
| `2026-08-19 02:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fd21ab9becb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:46 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:46:38` | `cowrie.session.connect` |
| `2026-08-19 02:46:38` | `cowrie.client.version` |
| `2026-08-19 02:46:38` | `cowrie.client.kex` |
| `2026-08-19 02:46:39` | `cowrie.login.success` |
| `2026-08-19 02:46:40` | `cowrie.session.params` |
| `2026-08-19 02:46:40` | `cowrie.command.input` |
| `2026-08-19 02:46:40` | `cowrie.log.closed` |
| `2026-08-19 02:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa9ff6dea83

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:46 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:46:44` | `cowrie.session.connect` |
| `2026-08-19 02:46:44` | `cowrie.client.version` |
| `2026-08-19 02:46:44` | `cowrie.client.kex` |
| `2026-08-19 02:46:44` | `cowrie.login.success` |
| `2026-08-19 02:46:45` | `cowrie.session.params` |
| `2026-08-19 02:46:45` | `cowrie.command.input` |
| `2026-08-19 02:46:45` | `cowrie.log.closed` |
| `2026-08-19 02:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-091001e75909

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:46 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:46:50` | `cowrie.session.connect` |
| `2026-08-19 02:46:51` | `cowrie.client.version` |
| `2026-08-19 02:46:51` | `cowrie.client.kex` |
| `2026-08-19 02:46:51` | `cowrie.login.success` |
| `2026-08-19 02:46:52` | `cowrie.session.params` |
| `2026-08-19 02:46:52` | `cowrie.command.input` |
| `2026-08-19 02:46:52` | `cowrie.log.closed` |
| `2026-08-19 02:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05e45ebfe515

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:46 |
| **Last Seen** | 2026-08-19 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:46:55` | `cowrie.session.connect` |
| `2026-08-19 02:46:55` | `cowrie.client.version` |
| `2026-08-19 02:46:55` | `cowrie.client.kex` |
| `2026-08-19 02:46:56` | `cowrie.login.success` |
| `2026-08-19 02:46:57` | `cowrie.session.params` |
| `2026-08-19 02:46:57` | `cowrie.command.input` |
| `2026-08-19 02:46:57` | `cowrie.log.closed` |
| `2026-08-19 02:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-592ced60cddb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:47 |
| **Last Seen** | 2026-08-19 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:47:01` | `cowrie.session.connect` |
| `2026-08-19 02:47:01` | `cowrie.client.version` |
| `2026-08-19 02:47:01` | `cowrie.client.kex` |
| `2026-08-19 02:47:01` | `cowrie.login.success` |
| `2026-08-19 02:47:02` | `cowrie.session.params` |
| `2026-08-19 02:47:02` | `cowrie.command.input` |
| `2026-08-19 02:47:02` | `cowrie.log.closed` |
| `2026-08-19 02:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f294531e905

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:47 |
| **Last Seen** | 2026-08-19 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:47:06` | `cowrie.session.connect` |
| `2026-08-19 02:47:06` | `cowrie.client.version` |
| `2026-08-19 02:47:06` | `cowrie.client.kex` |
| `2026-08-19 02:47:06` | `cowrie.login.success` |
| `2026-08-19 02:47:07` | `cowrie.session.params` |
| `2026-08-19 02:47:07` | `cowrie.command.input` |
| `2026-08-19 02:47:07` | `cowrie.log.closed` |
| `2026-08-19 02:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a229848233f3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:47 |
| **Last Seen** | 2026-08-19 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:47:11` | `cowrie.session.connect` |
| `2026-08-19 02:47:11` | `cowrie.client.version` |
| `2026-08-19 02:47:11` | `cowrie.client.kex` |
| `2026-08-19 02:47:12` | `cowrie.login.success` |
| `2026-08-19 02:47:12` | `cowrie.session.params` |
| `2026-08-19 02:47:12` | `cowrie.command.input` |
| `2026-08-19 02:47:12` | `cowrie.log.closed` |
| `2026-08-19 02:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0eb8ff50a3e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:47 |
| **Last Seen** | 2026-08-19 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:47:17` | `cowrie.session.connect` |
| `2026-08-19 02:47:17` | `cowrie.client.version` |
| `2026-08-19 02:47:17` | `cowrie.client.kex` |
| `2026-08-19 02:47:17` | `cowrie.login.success` |
| `2026-08-19 02:47:18` | `cowrie.session.params` |
| `2026-08-19 02:47:18` | `cowrie.command.input` |
| `2026-08-19 02:47:18` | `cowrie.log.closed` |
| `2026-08-19 02:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-940bcbe533dd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:47 |
| **Last Seen** | 2026-08-19 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:47:23` | `cowrie.session.connect` |
| `2026-08-19 02:47:23` | `cowrie.client.version` |
| `2026-08-19 02:47:23` | `cowrie.client.kex` |
| `2026-08-19 02:47:23` | `cowrie.login.success` |
| `2026-08-19 02:47:24` | `cowrie.session.params` |
| `2026-08-19 02:47:24` | `cowrie.command.input` |
| `2026-08-19 02:47:24` | `cowrie.log.closed` |
| `2026-08-19 02:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbe79b28ae4f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:47 |
| **Last Seen** | 2026-08-19 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:47:31` | `cowrie.session.connect` |
| `2026-08-19 02:47:31` | `cowrie.client.version` |
| `2026-08-19 02:47:31` | `cowrie.client.kex` |
| `2026-08-19 02:47:31` | `cowrie.login.success` |
| `2026-08-19 02:47:32` | `cowrie.session.params` |
| `2026-08-19 02:47:32` | `cowrie.command.input` |
| `2026-08-19 02:47:32` | `cowrie.log.closed` |
| `2026-08-19 02:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d8be22e57e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:47 |
| **Last Seen** | 2026-08-19 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:47:36` | `cowrie.session.connect` |
| `2026-08-19 02:47:36` | `cowrie.client.version` |
| `2026-08-19 02:47:36` | `cowrie.client.kex` |
| `2026-08-19 02:47:37` | `cowrie.login.success` |
| `2026-08-19 02:47:38` | `cowrie.session.params` |
| `2026-08-19 02:47:38` | `cowrie.command.input` |
| `2026-08-19 02:47:38` | `cowrie.log.closed` |
| `2026-08-19 02:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3821d4e09f2d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:47 |
| **Last Seen** | 2026-08-19 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:47:43` | `cowrie.session.connect` |
| `2026-08-19 02:47:43` | `cowrie.client.version` |
| `2026-08-19 02:47:43` | `cowrie.client.kex` |
| `2026-08-19 02:47:44` | `cowrie.login.success` |
| `2026-08-19 02:47:45` | `cowrie.session.params` |
| `2026-08-19 02:47:45` | `cowrie.command.input` |
| `2026-08-19 02:47:45` | `cowrie.log.closed` |
| `2026-08-19 02:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bd6159820c3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:47 |
| **Last Seen** | 2026-08-19 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:47:49` | `cowrie.session.connect` |
| `2026-08-19 02:47:49` | `cowrie.client.version` |
| `2026-08-19 02:47:49` | `cowrie.client.kex` |
| `2026-08-19 02:47:50` | `cowrie.login.success` |
| `2026-08-19 02:47:50` | `cowrie.session.params` |
| `2026-08-19 02:47:51` | `cowrie.command.input` |
| `2026-08-19 02:47:51` | `cowrie.log.closed` |
| `2026-08-19 02:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3856ed74f186

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:47 |
| **Last Seen** | 2026-08-19 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:47:56` | `cowrie.session.connect` |
| `2026-08-19 02:47:56` | `cowrie.client.version` |
| `2026-08-19 02:47:56` | `cowrie.client.kex` |
| `2026-08-19 02:47:56` | `cowrie.login.success` |
| `2026-08-19 02:47:57` | `cowrie.session.params` |
| `2026-08-19 02:47:57` | `cowrie.command.input` |
| `2026-08-19 02:47:57` | `cowrie.log.closed` |
| `2026-08-19 02:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1410fb54e7c7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:01` | `cowrie.session.connect` |
| `2026-08-19 02:48:01` | `cowrie.client.version` |
| `2026-08-19 02:48:02` | `cowrie.client.kex` |
| `2026-08-19 02:48:02` | `cowrie.login.success` |
| `2026-08-19 02:48:03` | `cowrie.session.params` |
| `2026-08-19 02:48:03` | `cowrie.command.input` |
| `2026-08-19 02:48:03` | `cowrie.log.closed` |
| `2026-08-19 02:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-596ab082ef7b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:07` | `cowrie.session.connect` |
| `2026-08-19 02:48:07` | `cowrie.client.version` |
| `2026-08-19 02:48:07` | `cowrie.client.kex` |
| `2026-08-19 02:48:08` | `cowrie.login.success` |
| `2026-08-19 02:48:09` | `cowrie.session.params` |
| `2026-08-19 02:48:09` | `cowrie.command.input` |
| `2026-08-19 02:48:09` | `cowrie.log.closed` |
| `2026-08-19 02:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6efb873f1e0

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:14` | `cowrie.session.connect` |
| `2026-08-19 02:48:14` | `cowrie.client.version` |
| `2026-08-19 02:48:14` | `cowrie.client.kex` |
| `2026-08-19 02:48:14` | `cowrie.login.success` |
| `2026-08-19 02:48:15` | `cowrie.session.params` |
| `2026-08-19 02:48:15` | `cowrie.command.input` |
| `2026-08-19 02:48:15` | `cowrie.log.closed` |
| `2026-08-19 02:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0a9f36ff5d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:14` | `cowrie.session.connect` |
| `2026-08-19 02:48:14` | `cowrie.client.version` |
| `2026-08-19 02:48:14` | `cowrie.client.kex` |
| `2026-08-19 02:48:15` | `cowrie.login.success` |
| `2026-08-19 02:48:16` | `cowrie.session.params` |
| `2026-08-19 02:48:16` | `cowrie.command.input` |
| `2026-08-19 02:48:16` | `cowrie.log.closed` |
| `2026-08-19 02:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68d29930a216

| Field | Detail |
|---|---|
| **Source IP** | `34.88.29[.]206` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:17` | `cowrie.session.connect` |
| `2026-08-19 02:48:17` | `cowrie.client.version` |
| `2026-08-19 02:48:18` | `cowrie.client.kex` |
| `2026-08-19 02:48:19` | `cowrie.login.success` |
| `2026-08-19 02:48:20` | `cowrie.session.params` |
| `2026-08-19 02:48:20` | `cowrie.command.input` |
| `2026-08-19 02:48:20` | `cowrie.command.failed` |
| `2026-08-19 02:48:20` | `cowrie.log.closed` |
| `2026-08-19 02:48:22` | `cowrie.session.params` |
| `2026-08-19 02:48:22` | `cowrie.command.input` |
| `2026-08-19 02:48:22` | `cowrie.session.file_download` |
| `2026-08-19 02:48:22` | `cowrie.log.closed` |
| `2026-08-19 02:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.88.29[.]206` to AbuseIPDB if not already reported
- [ ] Block `34.88.29[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b4dc35d6f5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:20` | `cowrie.session.connect` |
| `2026-08-19 02:48:20` | `cowrie.client.version` |
| `2026-08-19 02:48:20` | `cowrie.client.kex` |
| `2026-08-19 02:48:20` | `cowrie.login.success` |
| `2026-08-19 02:48:21` | `cowrie.session.params` |
| `2026-08-19 02:48:21` | `cowrie.command.input` |
| `2026-08-19 02:48:22` | `cowrie.log.closed` |
| `2026-08-19 02:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b197056e876

| Field | Detail |
|---|---|
| **Source IP** | `34.88.29[.]206` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:22` | `cowrie.session.connect` |
| `2026-08-19 02:48:22` | `cowrie.client.version` |
| `2026-08-19 02:48:22` | `cowrie.client.kex` |
| `2026-08-19 02:48:23` | `cowrie.login.success` |
| `2026-08-19 02:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.88.29[.]206` to AbuseIPDB if not already reported
- [ ] Block `34.88.29[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba345c82593

| Field | Detail |
|---|---|
| **Source IP** | `34.88.29[.]206` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:24` | `cowrie.session.connect` |
| `2026-08-19 02:48:24` | `cowrie.client.version` |
| `2026-08-19 02:48:24` | `cowrie.client.kex` |
| `2026-08-19 02:48:25` | `cowrie.login.success` |
| `2026-08-19 02:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.88.29[.]206` to AbuseIPDB if not already reported
- [ ] Block `34.88.29[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b382edc1c091

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:26` | `cowrie.session.connect` |
| `2026-08-19 02:48:26` | `cowrie.client.version` |
| `2026-08-19 02:48:26` | `cowrie.client.kex` |
| `2026-08-19 02:48:27` | `cowrie.login.success` |
| `2026-08-19 02:48:27` | `cowrie.session.params` |
| `2026-08-19 02:48:27` | `cowrie.command.input` |
| `2026-08-19 02:48:28` | `cowrie.log.closed` |
| `2026-08-19 02:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8f9fd80263c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:31` | `cowrie.session.connect` |
| `2026-08-19 02:48:31` | `cowrie.client.version` |
| `2026-08-19 02:48:31` | `cowrie.client.kex` |
| `2026-08-19 02:48:32` | `cowrie.login.success` |
| `2026-08-19 02:48:32` | `cowrie.session.params` |
| `2026-08-19 02:48:32` | `cowrie.command.input` |
| `2026-08-19 02:48:32` | `cowrie.log.closed` |
| `2026-08-19 02:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-713264ed578b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:38` | `cowrie.session.connect` |
| `2026-08-19 02:48:38` | `cowrie.client.version` |
| `2026-08-19 02:48:38` | `cowrie.client.kex` |
| `2026-08-19 02:48:38` | `cowrie.login.success` |
| `2026-08-19 02:48:39` | `cowrie.session.params` |
| `2026-08-19 02:48:39` | `cowrie.command.input` |
| `2026-08-19 02:48:39` | `cowrie.log.closed` |
| `2026-08-19 02:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20bb5e28648c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:46` | `cowrie.session.connect` |
| `2026-08-19 02:48:46` | `cowrie.client.version` |
| `2026-08-19 02:48:46` | `cowrie.client.kex` |
| `2026-08-19 02:48:46` | `cowrie.login.success` |
| `2026-08-19 02:48:47` | `cowrie.session.params` |
| `2026-08-19 02:48:47` | `cowrie.command.input` |
| `2026-08-19 02:48:47` | `cowrie.log.closed` |
| `2026-08-19 02:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5156632f7b8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:52` | `cowrie.session.connect` |
| `2026-08-19 02:48:52` | `cowrie.client.version` |
| `2026-08-19 02:48:53` | `cowrie.client.kex` |
| `2026-08-19 02:48:53` | `cowrie.login.success` |
| `2026-08-19 02:48:54` | `cowrie.session.params` |
| `2026-08-19 02:48:54` | `cowrie.command.input` |
| `2026-08-19 02:48:54` | `cowrie.log.closed` |
| `2026-08-19 02:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5a691a0b04

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:48 |
| **Last Seen** | 2026-08-19 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:48:59` | `cowrie.session.connect` |
| `2026-08-19 02:48:59` | `cowrie.client.version` |
| `2026-08-19 02:49:00` | `cowrie.client.kex` |
| `2026-08-19 02:49:00` | `cowrie.login.success` |
| `2026-08-19 02:49:01` | `cowrie.session.params` |
| `2026-08-19 02:49:01` | `cowrie.command.input` |
| `2026-08-19 02:49:01` | `cowrie.log.closed` |
| `2026-08-19 02:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd4534998fe9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:49 |
| **Last Seen** | 2026-08-19 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:49:07` | `cowrie.session.connect` |
| `2026-08-19 02:49:07` | `cowrie.client.version` |
| `2026-08-19 02:49:07` | `cowrie.client.kex` |
| `2026-08-19 02:49:07` | `cowrie.login.success` |
| `2026-08-19 02:49:08` | `cowrie.session.params` |
| `2026-08-19 02:49:08` | `cowrie.command.input` |
| `2026-08-19 02:49:08` | `cowrie.log.closed` |
| `2026-08-19 02:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c4db38c811

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:49 |
| **Last Seen** | 2026-08-19 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:49:12` | `cowrie.session.connect` |
| `2026-08-19 02:49:12` | `cowrie.client.version` |
| `2026-08-19 02:49:12` | `cowrie.client.kex` |
| `2026-08-19 02:49:13` | `cowrie.login.success` |
| `2026-08-19 02:49:13` | `cowrie.session.params` |
| `2026-08-19 02:49:13` | `cowrie.command.input` |
| `2026-08-19 02:49:14` | `cowrie.log.closed` |
| `2026-08-19 02:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dca77113849c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:49 |
| **Last Seen** | 2026-08-19 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:49:20` | `cowrie.session.connect` |
| `2026-08-19 02:49:20` | `cowrie.client.version` |
| `2026-08-19 02:49:20` | `cowrie.client.kex` |
| `2026-08-19 02:49:20` | `cowrie.login.success` |
| `2026-08-19 02:49:21` | `cowrie.session.params` |
| `2026-08-19 02:49:21` | `cowrie.command.input` |
| `2026-08-19 02:49:21` | `cowrie.log.closed` |
| `2026-08-19 02:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-345fee161600

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:49 |
| **Last Seen** | 2026-08-19 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:49:26` | `cowrie.session.connect` |
| `2026-08-19 02:49:26` | `cowrie.client.version` |
| `2026-08-19 02:49:26` | `cowrie.client.kex` |
| `2026-08-19 02:49:26` | `cowrie.login.success` |
| `2026-08-19 02:49:27` | `cowrie.session.params` |
| `2026-08-19 02:49:27` | `cowrie.command.input` |
| `2026-08-19 02:49:27` | `cowrie.log.closed` |
| `2026-08-19 02:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e0b144f83bc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:49 |
| **Last Seen** | 2026-08-19 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:49:31` | `cowrie.session.connect` |
| `2026-08-19 02:49:31` | `cowrie.client.version` |
| `2026-08-19 02:49:31` | `cowrie.client.kex` |
| `2026-08-19 02:49:32` | `cowrie.login.success` |
| `2026-08-19 02:49:33` | `cowrie.session.params` |
| `2026-08-19 02:49:33` | `cowrie.command.input` |
| `2026-08-19 02:49:33` | `cowrie.log.closed` |
| `2026-08-19 02:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-913fc36e54a9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:49 |
| **Last Seen** | 2026-08-19 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:49:39` | `cowrie.session.connect` |
| `2026-08-19 02:49:39` | `cowrie.client.version` |
| `2026-08-19 02:49:39` | `cowrie.client.kex` |
| `2026-08-19 02:49:39` | `cowrie.login.success` |
| `2026-08-19 02:49:40` | `cowrie.session.params` |
| `2026-08-19 02:49:40` | `cowrie.command.input` |
| `2026-08-19 02:49:40` | `cowrie.log.closed` |
| `2026-08-19 02:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a8b56bb819c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:49 |
| **Last Seen** | 2026-08-19 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:49:45` | `cowrie.session.connect` |
| `2026-08-19 02:49:45` | `cowrie.client.version` |
| `2026-08-19 02:49:45` | `cowrie.client.kex` |
| `2026-08-19 02:49:46` | `cowrie.login.success` |
| `2026-08-19 02:49:46` | `cowrie.session.params` |
| `2026-08-19 02:49:46` | `cowrie.command.input` |
| `2026-08-19 02:49:47` | `cowrie.log.closed` |
| `2026-08-19 02:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62bfc64a1323

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:49 |
| **Last Seen** | 2026-08-19 02:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:49:52` | `cowrie.session.connect` |
| `2026-08-19 02:49:52` | `cowrie.client.version` |
| `2026-08-19 02:49:52` | `cowrie.client.kex` |
| `2026-08-19 02:49:53` | `cowrie.login.success` |
| `2026-08-19 02:49:54` | `cowrie.session.params` |
| `2026-08-19 02:49:54` | `cowrie.command.input` |
| `2026-08-19 02:49:54` | `cowrie.log.closed` |
| `2026-08-19 02:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffb07f114fe8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:49 |
| **Last Seen** | 2026-08-19 02:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:49:58` | `cowrie.session.connect` |
| `2026-08-19 02:49:58` | `cowrie.client.version` |
| `2026-08-19 02:49:58` | `cowrie.client.kex` |
| `2026-08-19 02:49:59` | `cowrie.login.success` |
| `2026-08-19 02:50:00` | `cowrie.session.params` |
| `2026-08-19 02:50:00` | `cowrie.command.input` |
| `2026-08-19 02:50:00` | `cowrie.log.closed` |
| `2026-08-19 02:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ac4acda1675

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:50 |
| **Last Seen** | 2026-08-19 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:50:04` | `cowrie.session.connect` |
| `2026-08-19 02:50:04` | `cowrie.client.version` |
| `2026-08-19 02:50:04` | `cowrie.client.kex` |
| `2026-08-19 02:50:05` | `cowrie.login.success` |
| `2026-08-19 02:50:06` | `cowrie.session.params` |
| `2026-08-19 02:50:06` | `cowrie.command.input` |
| `2026-08-19 02:50:06` | `cowrie.log.closed` |
| `2026-08-19 02:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b211524567f9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:50 |
| **Last Seen** | 2026-08-19 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:50:11` | `cowrie.session.connect` |
| `2026-08-19 02:50:11` | `cowrie.client.version` |
| `2026-08-19 02:50:11` | `cowrie.client.kex` |
| `2026-08-19 02:50:11` | `cowrie.login.success` |
| `2026-08-19 02:50:12` | `cowrie.session.params` |
| `2026-08-19 02:50:12` | `cowrie.command.input` |
| `2026-08-19 02:50:12` | `cowrie.log.closed` |
| `2026-08-19 02:50:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e40c6e2940

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:50 |
| **Last Seen** | 2026-08-19 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:50:18` | `cowrie.session.connect` |
| `2026-08-19 02:50:18` | `cowrie.client.version` |
| `2026-08-19 02:50:18` | `cowrie.client.kex` |
| `2026-08-19 02:50:18` | `cowrie.login.success` |
| `2026-08-19 02:50:19` | `cowrie.session.params` |
| `2026-08-19 02:50:19` | `cowrie.command.input` |
| `2026-08-19 02:50:19` | `cowrie.log.closed` |
| `2026-08-19 02:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d73a4505fe26

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:50 |
| **Last Seen** | 2026-08-19 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:50:24` | `cowrie.session.connect` |
| `2026-08-19 02:50:24` | `cowrie.client.version` |
| `2026-08-19 02:50:24` | `cowrie.client.kex` |
| `2026-08-19 02:50:25` | `cowrie.login.success` |
| `2026-08-19 02:50:25` | `cowrie.session.params` |
| `2026-08-19 02:50:25` | `cowrie.command.input` |
| `2026-08-19 02:50:25` | `cowrie.log.closed` |
| `2026-08-19 02:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e00ab254fb8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:50 |
| **Last Seen** | 2026-08-19 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:50:31` | `cowrie.session.connect` |
| `2026-08-19 02:50:31` | `cowrie.client.version` |
| `2026-08-19 02:50:31` | `cowrie.client.kex` |
| `2026-08-19 02:50:31` | `cowrie.login.success` |
| `2026-08-19 02:50:32` | `cowrie.session.params` |
| `2026-08-19 02:50:32` | `cowrie.command.input` |
| `2026-08-19 02:50:32` | `cowrie.log.closed` |
| `2026-08-19 02:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeed7e570eab

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:50 |
| **Last Seen** | 2026-08-19 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:50:37` | `cowrie.session.connect` |
| `2026-08-19 02:50:37` | `cowrie.client.version` |
| `2026-08-19 02:50:37` | `cowrie.client.kex` |
| `2026-08-19 02:50:37` | `cowrie.login.success` |
| `2026-08-19 02:50:38` | `cowrie.session.params` |
| `2026-08-19 02:50:38` | `cowrie.command.input` |
| `2026-08-19 02:50:38` | `cowrie.log.closed` |
| `2026-08-19 02:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb788793d2ff

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:50 |
| **Last Seen** | 2026-08-19 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:50:43` | `cowrie.session.connect` |
| `2026-08-19 02:50:43` | `cowrie.client.version` |
| `2026-08-19 02:50:43` | `cowrie.client.kex` |
| `2026-08-19 02:50:44` | `cowrie.login.success` |
| `2026-08-19 02:50:45` | `cowrie.session.params` |
| `2026-08-19 02:50:45` | `cowrie.command.input` |
| `2026-08-19 02:50:45` | `cowrie.log.closed` |
| `2026-08-19 02:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c73cb8ddb686

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:50 |
| **Last Seen** | 2026-08-19 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:50:49` | `cowrie.session.connect` |
| `2026-08-19 02:50:49` | `cowrie.client.version` |
| `2026-08-19 02:50:49` | `cowrie.client.kex` |
| `2026-08-19 02:50:49` | `cowrie.login.success` |
| `2026-08-19 02:50:50` | `cowrie.session.params` |
| `2026-08-19 02:50:50` | `cowrie.command.input` |
| `2026-08-19 02:50:50` | `cowrie.log.closed` |
| `2026-08-19 02:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade99eab5cc2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:50 |
| **Last Seen** | 2026-08-19 02:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:50:55` | `cowrie.session.connect` |
| `2026-08-19 02:50:55` | `cowrie.client.version` |
| `2026-08-19 02:50:55` | `cowrie.client.kex` |
| `2026-08-19 02:50:56` | `cowrie.login.success` |
| `2026-08-19 02:50:56` | `cowrie.session.params` |
| `2026-08-19 02:50:56` | `cowrie.command.input` |
| `2026-08-19 02:50:57` | `cowrie.log.closed` |
| `2026-08-19 02:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac2031321f6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:51 |
| **Last Seen** | 2026-08-19 02:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:51:02` | `cowrie.session.connect` |
| `2026-08-19 02:51:02` | `cowrie.client.version` |
| `2026-08-19 02:51:02` | `cowrie.client.kex` |
| `2026-08-19 02:51:02` | `cowrie.login.success` |
| `2026-08-19 02:51:03` | `cowrie.session.params` |
| `2026-08-19 02:51:03` | `cowrie.command.input` |
| `2026-08-19 02:51:03` | `cowrie.log.closed` |
| `2026-08-19 02:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-646cd380d863

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:51 |
| **Last Seen** | 2026-08-19 02:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:51:08` | `cowrie.session.connect` |
| `2026-08-19 02:51:08` | `cowrie.client.version` |
| `2026-08-19 02:51:08` | `cowrie.client.kex` |
| `2026-08-19 02:51:09` | `cowrie.login.success` |
| `2026-08-19 02:51:10` | `cowrie.session.params` |
| `2026-08-19 02:51:10` | `cowrie.command.input` |
| `2026-08-19 02:51:10` | `cowrie.log.closed` |
| `2026-08-19 02:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9950a6415c48

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:51 |
| **Last Seen** | 2026-08-19 02:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:51:15` | `cowrie.session.connect` |
| `2026-08-19 02:51:15` | `cowrie.client.version` |
| `2026-08-19 02:51:15` | `cowrie.client.kex` |
| `2026-08-19 02:51:16` | `cowrie.login.success` |
| `2026-08-19 02:51:16` | `cowrie.session.params` |
| `2026-08-19 02:51:16` | `cowrie.command.input` |
| `2026-08-19 02:51:17` | `cowrie.log.closed` |
| `2026-08-19 02:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60a8c60d929

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:51 |
| **Last Seen** | 2026-08-19 02:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:51:22` | `cowrie.session.connect` |
| `2026-08-19 02:51:22` | `cowrie.client.version` |
| `2026-08-19 02:51:22` | `cowrie.client.kex` |
| `2026-08-19 02:51:22` | `cowrie.login.success` |
| `2026-08-19 02:51:23` | `cowrie.session.params` |
| `2026-08-19 02:51:23` | `cowrie.command.input` |
| `2026-08-19 02:51:23` | `cowrie.log.closed` |
| `2026-08-19 02:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-114cd8798d86

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:51 |
| **Last Seen** | 2026-08-19 02:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:51:28` | `cowrie.session.connect` |
| `2026-08-19 02:51:28` | `cowrie.client.version` |
| `2026-08-19 02:51:29` | `cowrie.client.kex` |
| `2026-08-19 02:51:29` | `cowrie.login.success` |
| `2026-08-19 02:51:30` | `cowrie.session.params` |
| `2026-08-19 02:51:30` | `cowrie.command.input` |
| `2026-08-19 02:51:30` | `cowrie.log.closed` |
| `2026-08-19 02:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfc51d6950f1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:51 |
| **Last Seen** | 2026-08-19 02:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:51:34` | `cowrie.session.connect` |
| `2026-08-19 02:51:34` | `cowrie.client.version` |
| `2026-08-19 02:51:34` | `cowrie.client.kex` |
| `2026-08-19 02:51:35` | `cowrie.login.success` |
| `2026-08-19 02:51:35` | `cowrie.session.params` |
| `2026-08-19 02:51:35` | `cowrie.command.input` |
| `2026-08-19 02:51:36` | `cowrie.log.closed` |
| `2026-08-19 02:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8014b45f8d72

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:51 |
| **Last Seen** | 2026-08-19 02:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:51:41` | `cowrie.session.connect` |
| `2026-08-19 02:51:41` | `cowrie.client.version` |
| `2026-08-19 02:51:41` | `cowrie.client.kex` |
| `2026-08-19 02:51:41` | `cowrie.login.success` |
| `2026-08-19 02:51:43` | `cowrie.session.params` |
| `2026-08-19 02:51:43` | `cowrie.command.input` |
| `2026-08-19 02:51:43` | `cowrie.log.closed` |
| `2026-08-19 02:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a82875e969

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:51 |
| **Last Seen** | 2026-08-19 02:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:51:48` | `cowrie.session.connect` |
| `2026-08-19 02:51:48` | `cowrie.client.version` |
| `2026-08-19 02:51:48` | `cowrie.client.kex` |
| `2026-08-19 02:51:49` | `cowrie.login.success` |
| `2026-08-19 02:51:49` | `cowrie.session.params` |
| `2026-08-19 02:51:49` | `cowrie.command.input` |
| `2026-08-19 02:51:49` | `cowrie.log.closed` |
| `2026-08-19 02:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a16d1526284d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:51 |
| **Last Seen** | 2026-08-19 02:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:51:54` | `cowrie.session.connect` |
| `2026-08-19 02:51:54` | `cowrie.client.version` |
| `2026-08-19 02:51:54` | `cowrie.client.kex` |
| `2026-08-19 02:51:54` | `cowrie.login.success` |
| `2026-08-19 02:51:55` | `cowrie.session.params` |
| `2026-08-19 02:51:55` | `cowrie.command.input` |
| `2026-08-19 02:51:55` | `cowrie.log.closed` |
| `2026-08-19 02:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-345c85819361

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:51 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:51:59` | `cowrie.session.connect` |
| `2026-08-19 02:51:59` | `cowrie.client.version` |
| `2026-08-19 02:51:59` | `cowrie.client.kex` |
| `2026-08-19 02:52:00` | `cowrie.login.success` |
| `2026-08-19 02:52:01` | `cowrie.session.params` |
| `2026-08-19 02:52:01` | `cowrie.command.input` |
| `2026-08-19 02:52:01` | `cowrie.log.closed` |
| `2026-08-19 02:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266d2a6f1510

| Field | Detail |
|---|---|
| **Source IP** | `218.59.235[.]170` |
| **First Seen** | 2026-08-19 02:52 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:52:02` | `cowrie.session.connect` |
| `2026-08-19 02:52:02` | `cowrie.client.version` |
| `2026-08-19 02:52:02` | `cowrie.client.kex` |
| `2026-08-19 02:52:05` | `cowrie.login.success` |
| `2026-08-19 02:52:06` | `cowrie.direct-tcpip.request` |
| `2026-08-19 02:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.59.235[.]170` to AbuseIPDB if not already reported
- [ ] Block `218.59.235[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58328fdc31a1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:52 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:52:05` | `cowrie.session.connect` |
| `2026-08-19 02:52:05` | `cowrie.client.version` |
| `2026-08-19 02:52:05` | `cowrie.client.kex` |
| `2026-08-19 02:52:06` | `cowrie.login.success` |
| `2026-08-19 02:52:06` | `cowrie.session.params` |
| `2026-08-19 02:52:06` | `cowrie.command.input` |
| `2026-08-19 02:52:06` | `cowrie.log.closed` |
| `2026-08-19 02:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e2df0ac7e79

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:52 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:52:10` | `cowrie.session.connect` |
| `2026-08-19 02:52:10` | `cowrie.client.version` |
| `2026-08-19 02:52:10` | `cowrie.client.kex` |
| `2026-08-19 02:52:11` | `cowrie.login.success` |
| `2026-08-19 02:52:12` | `cowrie.session.params` |
| `2026-08-19 02:52:12` | `cowrie.command.input` |
| `2026-08-19 02:52:12` | `cowrie.log.closed` |
| `2026-08-19 02:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354e42b9bd3a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:52 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:52:18` | `cowrie.session.connect` |
| `2026-08-19 02:52:18` | `cowrie.client.version` |
| `2026-08-19 02:52:18` | `cowrie.client.kex` |
| `2026-08-19 02:52:18` | `cowrie.login.success` |
| `2026-08-19 02:52:19` | `cowrie.session.params` |
| `2026-08-19 02:52:19` | `cowrie.command.input` |
| `2026-08-19 02:52:19` | `cowrie.log.closed` |
| `2026-08-19 02:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d79dd13c2435

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:52 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:52:25` | `cowrie.session.connect` |
| `2026-08-19 02:52:25` | `cowrie.client.version` |
| `2026-08-19 02:52:25` | `cowrie.client.kex` |
| `2026-08-19 02:52:25` | `cowrie.login.success` |
| `2026-08-19 02:52:26` | `cowrie.session.params` |
| `2026-08-19 02:52:26` | `cowrie.command.input` |
| `2026-08-19 02:52:26` | `cowrie.log.closed` |
| `2026-08-19 02:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49cfdd22936a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:52 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:52:31` | `cowrie.session.connect` |
| `2026-08-19 02:52:31` | `cowrie.client.version` |
| `2026-08-19 02:52:31` | `cowrie.client.kex` |
| `2026-08-19 02:52:31` | `cowrie.login.success` |
| `2026-08-19 02:52:33` | `cowrie.session.params` |
| `2026-08-19 02:52:33` | `cowrie.command.input` |
| `2026-08-19 02:52:33` | `cowrie.log.closed` |
| `2026-08-19 02:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d63b4c2950

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:52 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:52:38` | `cowrie.session.connect` |
| `2026-08-19 02:52:38` | `cowrie.client.version` |
| `2026-08-19 02:52:38` | `cowrie.client.kex` |
| `2026-08-19 02:52:38` | `cowrie.login.success` |
| `2026-08-19 02:52:39` | `cowrie.session.params` |
| `2026-08-19 02:52:39` | `cowrie.command.input` |
| `2026-08-19 02:52:39` | `cowrie.log.closed` |
| `2026-08-19 02:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ad99293930

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:52 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:52:43` | `cowrie.session.connect` |
| `2026-08-19 02:52:43` | `cowrie.client.version` |
| `2026-08-19 02:52:43` | `cowrie.client.kex` |
| `2026-08-19 02:52:44` | `cowrie.login.success` |
| `2026-08-19 02:52:45` | `cowrie.session.params` |
| `2026-08-19 02:52:45` | `cowrie.command.input` |
| `2026-08-19 02:52:45` | `cowrie.log.closed` |
| `2026-08-19 02:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99899b18f00

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:52 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:52:50` | `cowrie.session.connect` |
| `2026-08-19 02:52:50` | `cowrie.client.version` |
| `2026-08-19 02:52:50` | `cowrie.client.kex` |
| `2026-08-19 02:52:51` | `cowrie.login.success` |
| `2026-08-19 02:52:51` | `cowrie.session.params` |
| `2026-08-19 02:52:51` | `cowrie.command.input` |
| `2026-08-19 02:52:52` | `cowrie.log.closed` |
| `2026-08-19 02:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e57843c8b626

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:52 |
| **Last Seen** | 2026-08-19 02:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:52:56` | `cowrie.session.connect` |
| `2026-08-19 02:52:56` | `cowrie.client.version` |
| `2026-08-19 02:52:56` | `cowrie.client.kex` |
| `2026-08-19 02:52:56` | `cowrie.login.success` |
| `2026-08-19 02:52:57` | `cowrie.session.params` |
| `2026-08-19 02:52:57` | `cowrie.command.input` |
| `2026-08-19 02:52:57` | `cowrie.log.closed` |
| `2026-08-19 02:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e5c4241870

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:53 |
| **Last Seen** | 2026-08-19 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:53:02` | `cowrie.session.connect` |
| `2026-08-19 02:53:02` | `cowrie.client.version` |
| `2026-08-19 02:53:02` | `cowrie.client.kex` |
| `2026-08-19 02:53:03` | `cowrie.login.success` |
| `2026-08-19 02:53:03` | `cowrie.session.params` |
| `2026-08-19 02:53:03` | `cowrie.command.input` |
| `2026-08-19 02:53:04` | `cowrie.log.closed` |
| `2026-08-19 02:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70f678c9a739

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:53 |
| **Last Seen** | 2026-08-19 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:53:09` | `cowrie.session.connect` |
| `2026-08-19 02:53:09` | `cowrie.client.version` |
| `2026-08-19 02:53:09` | `cowrie.client.kex` |
| `2026-08-19 02:53:10` | `cowrie.login.success` |
| `2026-08-19 02:53:10` | `cowrie.session.params` |
| `2026-08-19 02:53:10` | `cowrie.command.input` |
| `2026-08-19 02:53:11` | `cowrie.log.closed` |
| `2026-08-19 02:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8a28d21898

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:53 |
| **Last Seen** | 2026-08-19 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:53:16` | `cowrie.session.connect` |
| `2026-08-19 02:53:16` | `cowrie.client.version` |
| `2026-08-19 02:53:16` | `cowrie.client.kex` |
| `2026-08-19 02:53:17` | `cowrie.login.success` |
| `2026-08-19 02:53:17` | `cowrie.session.params` |
| `2026-08-19 02:53:17` | `cowrie.command.input` |
| `2026-08-19 02:53:18` | `cowrie.log.closed` |
| `2026-08-19 02:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15175bb70d31

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:53 |
| **Last Seen** | 2026-08-19 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:53:24` | `cowrie.session.connect` |
| `2026-08-19 02:53:24` | `cowrie.client.version` |
| `2026-08-19 02:53:24` | `cowrie.client.kex` |
| `2026-08-19 02:53:25` | `cowrie.login.success` |
| `2026-08-19 02:53:25` | `cowrie.session.params` |
| `2026-08-19 02:53:25` | `cowrie.command.input` |
| `2026-08-19 02:53:26` | `cowrie.log.closed` |
| `2026-08-19 02:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a8a666200f0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:53 |
| **Last Seen** | 2026-08-19 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:53:31` | `cowrie.session.connect` |
| `2026-08-19 02:53:31` | `cowrie.client.version` |
| `2026-08-19 02:53:31` | `cowrie.client.kex` |
| `2026-08-19 02:53:31` | `cowrie.login.success` |
| `2026-08-19 02:53:32` | `cowrie.session.params` |
| `2026-08-19 02:53:32` | `cowrie.command.input` |
| `2026-08-19 02:53:32` | `cowrie.log.closed` |
| `2026-08-19 02:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-942923fb332e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:53 |
| **Last Seen** | 2026-08-19 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:53:38` | `cowrie.session.connect` |
| `2026-08-19 02:53:38` | `cowrie.client.version` |
| `2026-08-19 02:53:38` | `cowrie.client.kex` |
| `2026-08-19 02:53:38` | `cowrie.login.success` |
| `2026-08-19 02:53:39` | `cowrie.session.params` |
| `2026-08-19 02:53:39` | `cowrie.command.input` |
| `2026-08-19 02:53:39` | `cowrie.log.closed` |
| `2026-08-19 02:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29c888afb158

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:53 |
| **Last Seen** | 2026-08-19 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:53:44` | `cowrie.session.connect` |
| `2026-08-19 02:53:44` | `cowrie.client.version` |
| `2026-08-19 02:53:44` | `cowrie.client.kex` |
| `2026-08-19 02:53:45` | `cowrie.login.success` |
| `2026-08-19 02:53:46` | `cowrie.session.params` |
| `2026-08-19 02:53:46` | `cowrie.command.input` |
| `2026-08-19 02:53:46` | `cowrie.log.closed` |
| `2026-08-19 02:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee5f4ad06814

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:53 |
| **Last Seen** | 2026-08-19 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:53:51` | `cowrie.session.connect` |
| `2026-08-19 02:53:51` | `cowrie.client.version` |
| `2026-08-19 02:53:51` | `cowrie.client.kex` |
| `2026-08-19 02:53:52` | `cowrie.login.success` |
| `2026-08-19 02:53:53` | `cowrie.session.params` |
| `2026-08-19 02:53:53` | `cowrie.command.input` |
| `2026-08-19 02:53:53` | `cowrie.log.closed` |
| `2026-08-19 02:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1f768bf788

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:53 |
| **Last Seen** | 2026-08-19 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:53:58` | `cowrie.session.connect` |
| `2026-08-19 02:53:58` | `cowrie.client.version` |
| `2026-08-19 02:53:58` | `cowrie.client.kex` |
| `2026-08-19 02:53:58` | `cowrie.login.success` |
| `2026-08-19 02:53:59` | `cowrie.session.params` |
| `2026-08-19 02:53:59` | `cowrie.command.input` |
| `2026-08-19 02:53:59` | `cowrie.log.closed` |
| `2026-08-19 02:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af53c3b903bb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:54 |
| **Last Seen** | 2026-08-19 02:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:54:04` | `cowrie.session.connect` |
| `2026-08-19 02:54:04` | `cowrie.client.version` |
| `2026-08-19 02:54:05` | `cowrie.client.kex` |
| `2026-08-19 02:54:05` | `cowrie.login.success` |
| `2026-08-19 02:54:06` | `cowrie.session.params` |
| `2026-08-19 02:54:06` | `cowrie.command.input` |
| `2026-08-19 02:54:06` | `cowrie.log.closed` |
| `2026-08-19 02:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c587ab16659

| Field | Detail |
|---|---|
| **Source IP** | `85.158.145[.]129` |
| **First Seen** | 2026-08-19 02:54 |
| **Last Seen** | 2026-08-19 02:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:54:09` | `cowrie.session.connect` |
| `2026-08-19 02:54:09` | `cowrie.client.version` |
| `2026-08-19 02:54:09` | `cowrie.client.kex` |
| `2026-08-19 02:54:09` | `cowrie.login.success` |
| `2026-08-19 02:54:10` | `cowrie.session.params` |
| `2026-08-19 02:54:10` | `cowrie.command.input` |
| `2026-08-19 02:54:10` | `cowrie.log.closed` |
| `2026-08-19 02:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.158.145[.]129` to AbuseIPDB if not already reported
- [ ] Block `85.158.145[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7bd9a51eedd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:54 |
| **Last Seen** | 2026-08-19 02:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:54:10` | `cowrie.session.connect` |
| `2026-08-19 02:54:10` | `cowrie.client.version` |
| `2026-08-19 02:54:10` | `cowrie.client.kex` |
| `2026-08-19 02:54:10` | `cowrie.login.success` |
| `2026-08-19 02:54:11` | `cowrie.session.params` |
| `2026-08-19 02:54:11` | `cowrie.command.input` |
| `2026-08-19 02:54:12` | `cowrie.log.closed` |
| `2026-08-19 02:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd03dc985330

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:54 |
| **Last Seen** | 2026-08-19 02:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:54:17` | `cowrie.session.connect` |
| `2026-08-19 02:54:17` | `cowrie.client.version` |
| `2026-08-19 02:54:17` | `cowrie.client.kex` |
| `2026-08-19 02:54:18` | `cowrie.login.success` |
| `2026-08-19 02:54:19` | `cowrie.session.params` |
| `2026-08-19 02:54:19` | `cowrie.command.input` |
| `2026-08-19 02:54:19` | `cowrie.log.closed` |
| `2026-08-19 02:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-550ce9b25fd6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:54 |
| **Last Seen** | 2026-08-19 02:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:54:24` | `cowrie.session.connect` |
| `2026-08-19 02:54:24` | `cowrie.client.version` |
| `2026-08-19 02:54:24` | `cowrie.client.kex` |
| `2026-08-19 02:54:24` | `cowrie.login.success` |
| `2026-08-19 02:54:25` | `cowrie.session.params` |
| `2026-08-19 02:54:25` | `cowrie.command.input` |
| `2026-08-19 02:54:25` | `cowrie.log.closed` |
| `2026-08-19 02:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e947f15f40e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:54 |
| **Last Seen** | 2026-08-19 02:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:54:30` | `cowrie.session.connect` |
| `2026-08-19 02:54:30` | `cowrie.client.version` |
| `2026-08-19 02:54:30` | `cowrie.client.kex` |
| `2026-08-19 02:54:30` | `cowrie.login.success` |
| `2026-08-19 02:54:31` | `cowrie.session.params` |
| `2026-08-19 02:54:31` | `cowrie.command.input` |
| `2026-08-19 02:54:32` | `cowrie.log.closed` |
| `2026-08-19 02:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894612a6a67d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:54 |
| **Last Seen** | 2026-08-19 02:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:54:37` | `cowrie.session.connect` |
| `2026-08-19 02:54:37` | `cowrie.client.version` |
| `2026-08-19 02:54:37` | `cowrie.client.kex` |
| `2026-08-19 02:54:37` | `cowrie.login.success` |
| `2026-08-19 02:54:38` | `cowrie.session.params` |
| `2026-08-19 02:54:38` | `cowrie.command.input` |
| `2026-08-19 02:54:38` | `cowrie.log.closed` |
| `2026-08-19 02:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9f317a79058

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:54 |
| **Last Seen** | 2026-08-19 02:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:54:43` | `cowrie.session.connect` |
| `2026-08-19 02:54:43` | `cowrie.client.version` |
| `2026-08-19 02:54:43` | `cowrie.client.kex` |
| `2026-08-19 02:54:44` | `cowrie.login.success` |
| `2026-08-19 02:54:45` | `cowrie.session.params` |
| `2026-08-19 02:54:45` | `cowrie.command.input` |
| `2026-08-19 02:54:45` | `cowrie.log.closed` |
| `2026-08-19 02:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeed943b9170

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:54 |
| **Last Seen** | 2026-08-19 02:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:54:50` | `cowrie.session.connect` |
| `2026-08-19 02:54:50` | `cowrie.client.version` |
| `2026-08-19 02:54:50` | `cowrie.client.kex` |
| `2026-08-19 02:54:51` | `cowrie.login.success` |
| `2026-08-19 02:54:51` | `cowrie.session.params` |
| `2026-08-19 02:54:51` | `cowrie.command.input` |
| `2026-08-19 02:54:52` | `cowrie.log.closed` |
| `2026-08-19 02:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d505ab17d75

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]242` |
| **First Seen** | 2026-08-19 02:54 |
| **Last Seen** | 2026-08-19 02:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-19 02:54:57` | `cowrie.session.connect` |
| `2026-08-19 02:54:57` | `cowrie.client.version` |
| `2026-08-19 02:54:57` | `cowrie.client.kex` |
| `2026-08-19 02:54:57` | `cowrie.login.success` |
| `2026-08-19 02:54:58` | `cowrie.session.params` |
| `2026-08-19 02:54:58` | `cowrie.command.input` |
| `2026-08-19 02:54:58` | `cowrie.log.closed` |
| `2026-08-19 02:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]242` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **927** | 2026-08-19 00:55 | 2026-08-19 02:55 | 1091m | 0 | `T1592` | 🟠 MEDIUM |
| `172.236.228[.]227` | **3** | 2026-08-19 01:45 | 2026-08-19 01:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-19 01:37 | 2026-08-19 02:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.55.2[.]194` | **2** | 2026-08-19 01:45 | 2026-08-19 01:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-08-19 02:54 | 2026-08-19 02:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | **2** | 2026-08-19 01:08 | 2026-08-19 01:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]186` | **2** | 2026-08-19 02:26 | 2026-08-19 02:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]242` | **2** | 2026-08-19 02:35 | 2026-08-19 02:43 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.31.210[.]125` | 1 | 2026-08-19 02:45 | 2026-08-19 02:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]88` | 1 | 2026-08-19 01:53 | 2026-08-19 01:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.72.87[.]7` | 1 | 2026-08-19 02:07 | 2026-08-19 02:07 | 4s | 0 | `T1592` | 🟢 LOW |
| `183.208.49[.]88` | 1 | 2026-08-19 02:49 | 2026-08-19 02:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `200.59.88[.]198` | 1 | 2026-08-19 01:26 | 2026-08-19 01:26 | 10s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-08-19 02:24 | 2026-08-19 02:25 | 41s | 0 | `T1592` | 🟢 LOW |
| `220.132.170[.]64` | 1 | 2026-08-19 02:02 | 2026-08-19 02:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.248.213[.]232` | 1 | 2026-08-19 02:03 | 2026-08-19 02:03 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-08-19 01:44 | 2026-08-19 01:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-08-19 02:41 | 2026-08-19 02:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.210.94[.]61` | 1 | 2026-08-19 02:12 | 2026-08-19 02:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]205` | 1 | 2026-08-19 02:07 | 2026-08-19 02:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.175.149[.]14` | 1 | 2026-08-19 01:19 | 2026-08-19 01:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `61.149.183[.]194` | 1 | 2026-08-19 02:18 | 2026-08-19 02:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]152` | 1 | 2026-08-19 01:34 | 2026-08-19 01:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]174` | 1 | 2026-08-19 01:55 | 2026-08-19 01:55 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-19 01:31 | 2026-08-19 01:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]177` | 1 | 2026-08-19 01:58 | 2026-08-19 01:58 | 17s | 0 | `T1592` | 🟢 LOW |
| `73.166.138[.]164` | 1 | 2026-08-19 01:54 | 2026-08-19 01:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-08-19 02:51 | 2026-08-19 02:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]34` | 1 | 2026-08-19 01:47 | 2026-08-19 01:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-08-19 02:53 | 2026-08-19 02:53 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |

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
| `124.239.129[.]2` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `93.241.232[.]14` | DE | Deutsche Telekom AG | **100** ⚠️ | 50 |
| `54.175.149[.]14` | US | Amazon Technologies Inc. | **100** ⚠️ | 10 |
| `192.72.56[.]178` | TW | Seednet-TaipeiDP-S | **100** ⚠️ | 29 |
| `49.124.149[.]205` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 50 |
| `77.239.124[.]242` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 17 |
| `43.248.213[.]232` | ID | PT. MATRIXNET GLOBAL INDONESIA | **100** ⚠️ | 5 |
| `81.237.155[.]113` | SE | Telia Network Services | **100** ⚠️ | 46 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `220.132.170[.]64` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 266 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 248 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 11 below threshold 25 | 3 |
| AbuseIPDB score 2 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1228 cases |
| Tool 34  | Credential Extractor        | ✅ 269 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 79 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (1.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 63 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 247 priority case(s) shown individually · 30 recon entry/entries in table (8 group(s) consolidating 942 session(s)).

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
_Report time: 2026-08-19T03:01:31Z_

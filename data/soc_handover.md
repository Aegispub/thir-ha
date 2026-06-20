# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-20 |
| **Generated At** | 2026-06-20T12:00:06Z |
| **Shift Time** | 12:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **652** |
| Confirmed Threats | **634** |
| False Positives Filtered | **18** (2.8%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **15** |
| High Severity Cases | **245** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **407** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **246** |
| Unique Credential Pairs | **236** |
| Unique Usernames | **103** |
| Unique Passwords | **157** |
| Successful Auth Pairs | **242** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 66 |
| `admin` | 14 |
| `ubuntu` | 9 |
| `user` | 7 |
| `deploy` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 11 |
| `admin` | 9 |
| `12345` | 9 |
| `1` | 8 |
| `root` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 8 |
| `root` | `123@@@` | 2 |
| `root` | `LeitboGi0ro` | 2 |
| `root` | `smo@@kkklss` | 2 |
| `root` | `54321` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `54321` | `45.198.224.120` | 2026-06-20T08:55:31 |
| `admin` | `admin` | `68.183.234.194` | 2026-06-20T09:01:48 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-20T09:01:49 |
| `root` | `qwert12` | `45.198.224.120` | 2026-06-20T09:03:43 |
| `jenkins` | `jenkins` | `45.198.224.120` | 2026-06-20T09:11:39 |
| `admin` | `admin` | `27.79.7.135` | 2026-06-20T09:19:15 |
| `root` | `admin` | `27.79.7.135` | 2026-06-20T09:24:22 |
| `installer` | `installer` | `27.79.7.135` | 2026-06-20T09:28:15 |
| `admin` | `admin` | `45.184.226.43` | 2026-06-20T09:34:03 |
| `test3` | `test3` | `45.198.224.120` | 2026-06-20T09:36:02 |
| `squid` | `squid` | `27.79.7.135` | 2026-06-20T09:42:49 |
| `support` | `support` | `27.79.7.135` | 2026-06-20T09:51:46 |
| `ubuntu` | `a` | `45.198.224.120` | 2026-06-20T09:51:58 |
| `root` | `@` | `27.79.7.135` | 2026-06-20T09:55:40 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-20T10:08:53 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-20T10:08:53 |
| `solana` | `solana` | `80.94.92.186` | 2026-06-20T10:09:38 |
| `sol` | `123` | `80.94.92.186` | 2026-06-20T10:14:13 |
| `root` | `P@ssw0rd!@#123` | `45.198.224.120` | 2026-06-20T10:16:31 |
| `sol` | `1234` | `80.94.92.186` | 2026-06-20T10:18:25 |
| `solv` | `solv` | `80.94.92.186` | 2026-06-20T10:22:23 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-20T10:22:47 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-20T10:22:47 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-20T10:22:53 |
| `solv` | `123456` | `80.94.92.186` | 2026-06-20T10:26:24 |
| `a` | `a` | `101.206.107.245` | 2026-06-20T10:27:32 |
| `ubuntu` | `ubuntu` | `80.94.92.186` | 2026-06-20T10:30:35 |
| `root` | `Primo2` | `45.198.224.120` | 2026-06-20T10:33:02 |
| `admin1` | `modzmodz` | `91.92.40.124` | 2026-06-20T10:33:33 |
| `amine` | `amine` | `91.92.40.124` | 2026-06-20T10:33:43 |
| `appuser` | `test` | `91.92.40.124` | 2026-06-20T10:33:51 |
| `sdadmin` | `51nGleD` | `91.92.40.124` | 2026-06-20T10:33:58 |
| `node` | `node` | `91.92.40.124` | 2026-06-20T10:34:05 |
| `nutanix` | `nutanix/4u` | `91.92.40.124` | 2026-06-20T10:34:12 |
| `deploy` | `1` | `91.92.40.124` | 2026-06-20T10:34:20 |
| `tactical` | `tactical` | `91.92.40.124` | 2026-06-20T10:34:27 |
| `myuser` | `myuser` | `91.92.40.124` | 2026-06-20T10:34:33 |
| `newuser` | `qwerty` | `91.92.40.124` | 2026-06-20T10:34:42 |
| `sam` | `1234567890` | `91.92.40.124` | 2026-06-20T10:34:47 |
| `root` | `Pass@123` | `91.92.40.124` | 2026-06-20T10:34:55 |
| `odoo17` | `odoo17` | `91.92.40.124` | 2026-06-20T10:35:02 |
| `root` | `Admin123!@#` | `91.92.40.124` | 2026-06-20T10:35:09 |
| `app` | `root` | `91.92.40.124` | 2026-06-20T10:35:17 |
| `claude` | `abc123` | `91.92.40.124` | 2026-06-20T10:35:25 |
| `ubuntu` | `123456` | `80.94.92.186` | 2026-06-20T10:35:26 |
| `bernard` | `bernard` | `91.92.40.124` | 2026-06-20T10:35:31 |
| `test` | `1234qwer` | `91.92.40.124` | 2026-06-20T10:35:35 |
| `gitlab-runner` | `passwd` | `91.92.40.124` | 2026-06-20T10:35:41 |
| `root` | `Aa1234567890` | `91.92.40.124` | 2026-06-20T10:35:45 |
| `ubuntu` | `qwe123456` | `91.92.40.124` | 2026-06-20T10:35:50 |
| `erpnext` | `erpnext` | `91.92.40.124` | 2026-06-20T10:35:57 |
| `root` | `Welcome123` | `91.92.40.124` | 2026-06-20T10:36:04 |
| `user1` | `user1` | `91.92.40.124` | 2026-06-20T10:36:11 |
| `system` | `1qaz2wsx` | `91.92.40.124` | 2026-06-20T10:36:16 |
| `root` | `1q2w3e4r5t6y` | `91.92.40.124` | 2026-06-20T10:36:24 |
| `deployer` | `user` | `91.92.40.124` | 2026-06-20T10:36:29 |
| `user2` | `123456` | `91.92.40.124` | 2026-06-20T10:36:37 |
| `ftpuser1` | `123456` | `91.92.40.124` | 2026-06-20T10:36:43 |
| `x` | `1` | `91.92.40.124` | 2026-06-20T10:36:47 |
| `user` | `user123456` | `91.92.40.124` | 2026-06-20T10:36:54 |
| `rock` | `rock` | `91.92.40.124` | 2026-06-20T10:37:00 |
| `root` | `root123` | `91.92.40.124` | 2026-06-20T10:37:06 |
| `mysql` | `mysql` | `91.92.40.124` | 2026-06-20T10:37:10 |
| `root` | `admin1` | `91.92.40.124` | 2026-06-20T10:37:17 |
| `appuser` | `12345` | `91.92.40.124` | 2026-06-20T10:37:23 |
| `docker` | `docker123` | `91.92.40.124` | 2026-06-20T10:37:28 |
| `dev` | `password` | `91.92.40.124` | 2026-06-20T10:37:35 |
| `root` | `Huawei@123` | `91.92.40.124` | 2026-06-20T10:37:42 |
| `test1` | `123456789` | `91.92.40.124` | 2026-06-20T10:37:48 |
| `root` | `!qaz@WSX` | `91.92.40.124` | 2026-06-20T10:37:54 |
| `minecraft` | `123` | `91.92.40.124` | 2026-06-20T10:38:00 |
| `test` | `passwd` | `91.92.40.124` | 2026-06-20T10:38:07 |
| `frappe` | `123` | `91.92.40.124` | 2026-06-20T10:38:13 |
| `root` | `ubuntu` | `91.92.40.124` | 2026-06-20T10:38:19 |
| `root` | `root1234` | `91.92.40.124` | 2026-06-20T10:38:26 |
| `deploy` | `deploy` | `91.92.40.124` | 2026-06-20T10:38:32 |
| `root` | `abcd@1234` | `91.92.40.124` | 2026-06-20T10:38:38 |
| `admin` | `admin` | `212.227.235.203` | 2026-06-20T10:38:39 |
| `system` | `system` | `91.92.40.124` | 2026-06-20T10:38:45 |
| `root` | `pass` | `91.92.40.124` | 2026-06-20T10:38:51 |
| `user` | `qwe123456` | `91.92.40.124` | 2026-06-20T10:38:58 |
| `deploy` | `123123` | `91.92.40.124` | 2026-06-20T10:39:03 |
| `pi` | `123456` | `91.92.40.124` | 2026-06-20T10:39:09 |
| `erp` | `erp` | `91.92.40.124` | 2026-06-20T10:39:15 |
| `azureuser` | `12345` | `91.92.40.124` | 2026-06-20T10:39:21 |
| `admin` | `111` | `91.92.40.124` | 2026-06-20T10:39:27 |
| `work` | `work` | `91.92.40.124` | 2026-06-20T10:39:34 |
| `admin` | `abc123` | `91.92.40.124` | 2026-06-20T10:39:40 |
| `systemd` | `1q2w3e4r` | `91.92.40.124` | 2026-06-20T10:39:45 |
| `root` | `12345qwert` | `91.92.40.124` | 2026-06-20T10:39:51 |
| `administrator` | `administrator` | `91.92.40.124` | 2026-06-20T10:39:58 |
| `root` | `qwertyuiop` | `91.92.40.124` | 2026-06-20T10:40:03 |
| `pi` | `toor` | `91.92.40.124` | 2026-06-20T10:40:11 |
| `ubuntu` | `1qaz@WSX` | `91.92.40.124` | 2026-06-20T10:40:17 |
| `developer` | `developer` | `91.92.40.124` | 2026-06-20T10:40:22 |
| `ubuntu` | `12345678` | `80.94.92.186` | 2026-06-20T10:40:27 |
| `web` | `web123` | `91.92.40.124` | 2026-06-20T10:40:29 |
| `test` | `1` | `91.92.40.124` | 2026-06-20T10:40:35 |
| `teamspeak` | `raspberry` | `91.92.40.124` | 2026-06-20T10:40:41 |
| `user` | `1qaz@WSX` | `91.92.40.124` | 2026-06-20T10:40:48 |
| `ubuntu` | `qwerty12345678` | `45.198.224.120` | 2026-06-20T10:40:49 |
| `john` | `123456` | `91.92.40.124` | 2026-06-20T10:40:53 |
| `deploy` | `qwerty123` | `91.92.40.124` | 2026-06-20T10:40:59 |
| `minecraft` | `1` | `91.92.40.124` | 2026-06-20T10:41:06 |
| `root` | `qwe@123` | `91.92.40.124` | 2026-06-20T10:41:11 |
| `ansible` | `passwd` | `91.92.40.124` | 2026-06-20T10:41:17 |
| `user2` | `user2` | `91.92.40.124` | 2026-06-20T10:41:24 |
| `user` | `111111` | `91.92.40.124` | 2026-06-20T10:41:30 |
| `root` | `Qwerty123` | `91.92.40.124` | 2026-06-20T10:41:36 |
| `ubuntu` | `Aa123456` | `91.92.40.124` | 2026-06-20T10:41:42 |
| `test` | `test123` | `91.92.40.124` | 2026-06-20T10:41:48 |
| `root` | `admin123` | `91.92.40.124` | 2026-06-20T10:41:54 |
| `ai` | `ai` | `91.92.40.124` | 2026-06-20T10:42:00 |
| `deployer` | `deployer123` | `91.92.40.124` | 2026-06-20T10:42:06 |
| `root` | `aa123456` | `91.92.40.124` | 2026-06-20T10:42:12 |
| `minecraft` | `password` | `91.92.40.124` | 2026-06-20T10:42:18 |
| `root` | `qwe123456` | `91.92.40.124` | 2026-06-20T10:42:24 |
| `xiao` | `xiao` | `91.92.40.124` | 2026-06-20T10:42:30 |
| `user2` | `1` | `91.92.40.124` | 2026-06-20T10:42:36 |
| `root` | `1Q2w3e4r` | `91.92.40.124` | 2026-06-20T10:42:43 |
| `test` | `123456` | `91.92.40.124` | 2026-06-20T10:42:49 |
| `admin` | `root` | `91.92.40.124` | 2026-06-20T10:42:55 |
| `server` | `12345` | `91.92.40.124` | 2026-06-20T10:43:00 |
| `root` | `password` | `91.92.40.124` | 2026-06-20T10:43:07 |
| `jack` | `jack` | `91.92.40.124` | 2026-06-20T10:43:13 |
| `adminuser` | `adminuser` | `91.92.40.124` | 2026-06-20T10:43:20 |
| `kingbase` | `kingbase` | `91.92.40.124` | 2026-06-20T10:43:26 |
| `tester` | `12345` | `91.92.40.124` | 2026-06-20T10:43:31 |
| `debian` | `toor` | `91.92.40.124` | 2026-06-20T10:43:37 |
| `root` | `12qwaszx` | `91.92.40.124` | 2026-06-20T10:43:44 |
| `rdpuser` | `123456` | `91.92.40.124` | 2026-06-20T10:43:51 |
| `user1` | `123456789` | `91.92.40.124` | 2026-06-20T10:43:56 |
| `root` | `Password` | `91.92.40.124` | 2026-06-20T10:44:04 |
| `root` | `root@123` | `91.92.40.124` | 2026-06-20T10:44:08 |
| `david` | `david` | `91.92.40.124` | 2026-06-20T10:44:16 |
| `bitrix` | `bitrix` | `91.92.40.124` | 2026-06-20T10:44:21 |
| `root` | `aA123456` | `91.92.40.124` | 2026-06-20T10:44:26 |
| `ec2-user` | `12345678` | `91.92.40.124` | 2026-06-20T10:44:33 |
| `git` | `1234` | `91.92.40.124` | 2026-06-20T10:44:39 |
| `root` | `P@ssword` | `91.92.40.124` | 2026-06-20T10:44:45 |
| `test1` | `test123` | `91.92.40.124` | 2026-06-20T10:44:51 |
| `user2` | `123` | `91.92.40.124` | 2026-06-20T10:44:58 |
| `ghost` | `ghost` | `91.92.40.124` | 2026-06-20T10:45:03 |
| `gary` | `gary` | `91.92.40.124` | 2026-06-20T10:45:10 |
| `demo` | `demo` | `91.92.40.124` | 2026-06-20T10:45:15 |
| `root` | `1qazxsw2` | `91.92.40.124` | 2026-06-20T10:45:22 |
| `root` | `1qaz@WSX` | `91.92.40.124` | 2026-06-20T10:45:28 |
| `sol` | `12345678` | `80.94.92.186` | 2026-06-20T10:45:29 |
| `runner` | `test` | `91.92.40.124` | 2026-06-20T10:45:33 |
| `root` | `Welcome@123` | `91.92.40.124` | 2026-06-20T10:45:40 |
| `admin` | `admin` | `91.92.40.124` | 2026-06-20T10:45:46 |
| `admin` | `!QAZ2wsx` | `91.92.40.124` | 2026-06-20T10:45:52 |
| `master` | `qwerty` | `91.92.40.124` | 2026-06-20T10:45:59 |
| `root` | `passwd` | `91.92.40.124` | 2026-06-20T10:46:06 |
| `dev` | `dev` | `91.92.40.124` | 2026-06-20T10:46:11 |
| `media` | `media` | `91.92.40.124` | 2026-06-20T10:46:17 |
| `root` | `qwe123` | `91.92.40.124` | 2026-06-20T10:46:23 |
| `appuser` | `root` | `91.92.40.124` | 2026-06-20T10:46:29 |
| `root` | `ZAQ!2wsx` | `91.92.40.124` | 2026-06-20T10:46:34 |
| `www` | `user` | `91.92.40.124` | 2026-06-20T10:46:41 |
| `csgo` | `csgo` | `91.92.40.124` | 2026-06-20T10:46:47 |
| `tester` | `test` | `91.92.40.124` | 2026-06-20T10:46:53 |
| `root` | `modzmodz` | `91.92.40.124` | 2026-06-20T10:46:59 |
| `user1` | `12345` | `91.92.40.124` | 2026-06-20T10:47:04 |
| `ivan` | `ivan` | `91.92.40.124` | 2026-06-20T10:47:11 |
| `es` | `123456` | `91.92.40.124` | 2026-06-20T10:47:17 |
| `user` | `user` | `91.92.40.124` | 2026-06-20T10:47:24 |
| `airflow` | `airflow` | `91.92.40.124` | 2026-06-20T10:47:30 |
| `amir` | `amir` | `91.92.40.124` | 2026-06-20T10:47:35 |
| `ethan` | `ethan` | `91.92.40.124` | 2026-06-20T10:47:41 |
| `azureuser` | `root` | `91.92.40.124` | 2026-06-20T10:47:48 |
| `root` | `Huawei123` | `91.92.40.124` | 2026-06-20T10:47:53 |
| `admin` | `E4IuG88G` | `91.92.40.124` | 2026-06-20T10:48:00 |
| `trader` | `trader` | `91.92.40.124` | 2026-06-20T10:48:05 |
| `claude` | `1234` | `91.92.40.124` | 2026-06-20T10:48:12 |
| `webuser` | `123456` | `91.92.40.124` | 2026-06-20T10:48:18 |
| `ubuntu` | `1` | `91.92.40.124` | 2026-06-20T10:48:24 |
| `prem` | `12345` | `91.92.40.124` | 2026-06-20T10:48:30 |
| `root` | `q1w2e3r4` | `91.92.40.124` | 2026-06-20T10:48:35 |
| `debian` | `Aa123456.` | `91.92.40.124` | 2026-06-20T10:48:42 |
| `root` | `Aa123456` | `91.92.40.124` | 2026-06-20T10:48:48 |
| `root` | `123123123` | `91.92.40.124` | 2026-06-20T10:48:55 |
| `ark` | `ark` | `91.92.40.124` | 2026-06-20T10:49:01 |
| `support` | `123` | `91.92.40.124` | 2026-06-20T10:49:07 |
| `guest` | `pi` | `91.92.40.124` | 2026-06-20T10:49:13 |
| `root` | `00000000` | `91.92.40.124` | 2026-06-20T10:49:19 |
| `root` | `admin@123` | `91.92.40.124` | 2026-06-20T10:49:26 |
| `root` | `CatCult2025!` | `91.92.40.124` | 2026-06-20T10:49:30 |
| `root` | `aB123456` | `91.92.40.124` | 2026-06-20T10:49:36 |
| `installer` | `12345` | `91.92.40.124` | 2026-06-20T10:49:43 |
| `user` | `111` | `91.92.40.124` | 2026-06-20T10:49:49 |
| `student` | `password` | `91.92.40.124` | 2026-06-20T10:49:55 |
| `root` | `1qazXSW@` | `91.92.40.124` | 2026-06-20T10:50:02 |
| `dolphinscheduler` | `dolphinscheduler` | `91.92.40.124` | 2026-06-20T10:50:08 |
| `john` | `john` | `91.92.40.124` | 2026-06-20T10:50:15 |
| `openvpn` | `12345678` | `91.92.40.124` | 2026-06-20T10:50:21 |
| `data` | `test` | `91.92.40.124` | 2026-06-20T10:50:27 |
| `sol` | `jito` | `80.94.92.186` | 2026-06-20T10:50:30 |
| `user` | `password` | `91.92.40.124` | 2026-06-20T10:50:33 |
| `server` | `root` | `91.92.40.124` | 2026-06-20T10:50:40 |
| `steam` | `1` | `91.92.40.124` | 2026-06-20T10:50:47 |
| `claude` | `root` | `91.92.40.124` | 2026-06-20T10:50:53 |
| `user1` | `root@123` | `91.92.40.124` | 2026-06-20T10:51:00 |
| `hadoop` | `hadoop123` | `91.92.40.124` | 2026-06-20T10:51:05 |
| `sysupdate` | `Password1` | `91.92.40.124` | 2026-06-20T10:51:11 |
| `root` | `123123` | `91.92.40.124` | 2026-06-20T10:51:18 |
| `admin` | `password` | `91.92.40.124` | 2026-06-20T10:51:23 |
| `root` | `changeme` | `91.92.40.124` | 2026-06-20T10:51:30 |
| `root` | `Ab123456` | `91.92.40.124` | 2026-06-20T10:51:35 |
| `bot` | `bot` | `91.92.40.124` | 2026-06-20T10:51:42 |
| `root` | `P@ssw0rd` | `91.92.40.124` | 2026-06-20T10:51:47 |
| `root` | `123qwe!@` | `91.92.40.124` | 2026-06-20T10:51:54 |
| `crafty` | `12345678` | `91.92.40.124` | 2026-06-20T10:52:00 |
| `openclaw` | `openclaw` | `91.92.40.124` | 2026-06-20T10:52:06 |
| `student` | `redhat` | `91.92.40.124` | 2026-06-20T10:52:12 |
| `system` | `12345` | `91.92.40.124` | 2026-06-20T10:52:17 |
| `newuser` | `123456` | `91.92.40.124` | 2026-06-20T10:52:24 |
| `app` | `app` | `91.92.40.124` | 2026-06-20T10:52:29 |
| `jellyfin` | `password` | `91.92.40.124` | 2026-06-20T10:52:35 |
| `runner` | `runner` | `91.92.40.124` | 2026-06-20T10:52:41 |
| `admin2` | `admin2` | `91.92.40.124` | 2026-06-20T10:52:49 |
| `root` | `111111` | `91.92.40.124` | 2026-06-20T10:52:53 |
| `crafty` | `1234` | `91.92.40.124` | 2026-06-20T10:53:00 |
| `dev` | `123` | `91.92.40.124` | 2026-06-20T10:53:06 |
| `splunk` | `splunk` | `91.92.40.124` | 2026-06-20T10:53:12 |
| `openclaw` | `12345` | `91.92.40.124` | 2026-06-20T10:53:18 |
| `root` | `Admin123` | `91.92.40.124` | 2026-06-20T10:53:25 |
| `server` | `1234` | `91.92.40.124` | 2026-06-20T10:53:31 |
| `debian` | `debian` | `91.92.40.124` | 2026-06-20T10:53:37 |
| `root` | `Ac123456` | `91.92.40.124` | 2026-06-20T10:53:44 |
| `openclaw` | `1234` | `91.92.40.124` | 2026-06-20T10:53:49 |
| `deploy` | `rootroot` | `91.92.40.124` | 2026-06-20T10:53:56 |
| `omm` | `omm` | `91.92.40.124` | 2026-06-20T10:54:02 |
| `newuser` | `newuser` | `91.92.40.124` | 2026-06-20T10:54:08 |
| `guest` | `guest123` | `91.92.40.124` | 2026-06-20T10:54:15 |
| `devuser` | `devuser` | `91.92.40.124` | 2026-06-20T10:54:22 |
| `pi` | `1` | `91.92.40.124` | 2026-06-20T10:54:29 |
| `root` | `nD6ffS9msOngs` | `91.92.40.124` | 2026-06-20T10:54:34 |
| `hduser` | `hduser` | `91.92.40.124` | 2026-06-20T10:54:40 |
| `root` | `123456789` | `91.92.40.124` | 2026-06-20T10:54:47 |
| `portal` | `portal` | `91.92.40.124` | 2026-06-20T10:54:53 |
| `openclaw` | `user` | `91.92.40.124` | 2026-06-20T10:54:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **652** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 235 |
| libssh | 14 |
| AsyncSSH (Python) | 9 |
| Paramiko (Python) | 6 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 209 | 1 |
| `16443846184e...` | Generic scanner | 19 | 2 |
| `fda360b1b4f4...` | Mirai/variant | 9 | 1 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `19532158b559...` | Mirai/variant | 3 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 209 | 1 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 19 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 10 | 4 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 9 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 3 | 3 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **24** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS398705` | Censys, Inc. | 1 | LOW |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS45903` | CMC Telecom Infrastructure Company | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (245)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-298dfb002425

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 08:55 |
| **Last Seen** | 2026-06-20 08:55 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 08:55:10` | `cowrie.session.connect` |
| `2026-06-20 08:55:12` | `cowrie.client.version` |
| `2026-06-20 08:55:12` | `cowrie.client.kex` |
| `2026-06-20 08:55:31` | `cowrie.login.success` |
| `2026-06-20 08:55:41` | `cowrie.session.params` |
| `2026-06-20 08:55:41` | `cowrie.command.input` |
| `2026-06-20 08:55:45` | `cowrie.log.closed` |
| `2026-06-20 08:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc7aa01d5ee4

| Field | Detail |
|---|---|
| **Source IP** | `68.183.234[.]194` |
| **First Seen** | 2026-06-20 09:01 |
| **Last Seen** | 2026-06-20 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:01:47` | `cowrie.session.connect` |
| `2026-06-20 09:01:47` | `cowrie.client.version` |
| `2026-06-20 09:01:47` | `cowrie.client.kex` |
| `2026-06-20 09:01:48` | `cowrie.login.success` |
| `2026-06-20 09:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.234[.]194` to AbuseIPDB if not already reported
- [ ] Block `68.183.234[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61d21100c2d0

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-20 09:01 |
| **Last Seen** | 2026-06-20 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:01:48` | `cowrie.session.connect` |
| `2026-06-20 09:01:48` | `cowrie.client.version` |
| `2026-06-20 09:01:48` | `cowrie.client.kex` |
| `2026-06-20 09:01:49` | `cowrie.login.success` |
| `2026-06-20 09:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e8deb09c122

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 09:03 |
| **Last Seen** | 2026-06-20 09:03 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:03:21` | `cowrie.session.connect` |
| `2026-06-20 09:03:25` | `cowrie.client.version` |
| `2026-06-20 09:03:25` | `cowrie.client.kex` |
| `2026-06-20 09:03:43` | `cowrie.login.success` |
| `2026-06-20 09:03:52` | `cowrie.session.params` |
| `2026-06-20 09:03:52` | `cowrie.command.input` |
| `2026-06-20 09:03:57` | `cowrie.log.closed` |
| `2026-06-20 09:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7dd1a4cef6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 09:11 |
| **Last Seen** | 2026-06-20 09:11 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:11:18` | `cowrie.session.connect` |
| `2026-06-20 09:11:21` | `cowrie.client.version` |
| `2026-06-20 09:11:21` | `cowrie.client.kex` |
| `2026-06-20 09:11:39` | `cowrie.login.success` |
| `2026-06-20 09:11:47` | `cowrie.session.params` |
| `2026-06-20 09:11:47` | `cowrie.command.input` |
| `2026-06-20 09:11:52` | `cowrie.log.closed` |
| `2026-06-20 09:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3deae7cd5ee7

| Field | Detail |
|---|---|
| **Source IP** | `27.79.7[.]135` |
| **First Seen** | 2026-06-20 09:19 |
| **Last Seen** | 2026-06-20 09:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:19:14` | `cowrie.session.connect` |
| `2026-06-20 09:19:14` | `cowrie.client.version` |
| `2026-06-20 09:19:14` | `cowrie.client.kex` |
| `2026-06-20 09:19:15` | `cowrie.login.success` |
| `2026-06-20 09:19:15` | `cowrie.direct-tcpip.request` |
| `2026-06-20 09:19:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-20 09:19:15` | `cowrie.direct-tcpip.data` |
| `2026-06-20 09:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.7[.]135` to AbuseIPDB if not already reported
- [ ] Block `27.79.7[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24d8248813fb

| Field | Detail |
|---|---|
| **Source IP** | `27.79.7[.]135` |
| **First Seen** | 2026-06-20 09:24 |
| **Last Seen** | 2026-06-20 09:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:24:11` | `cowrie.session.connect` |
| `2026-06-20 09:24:11` | `cowrie.client.version` |
| `2026-06-20 09:24:15` | `cowrie.client.kex` |
| `2026-06-20 09:24:22` | `cowrie.login.success` |
| `2026-06-20 09:24:23` | `cowrie.direct-tcpip.request` |
| `2026-06-20 09:24:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.7[.]135` to AbuseIPDB if not already reported
- [ ] Block `27.79.7[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d8eb6297d5f

| Field | Detail |
|---|---|
| **Source IP** | `27.79.7[.]135` |
| **First Seen** | 2026-06-20 09:28 |
| **Last Seen** | 2026-06-20 09:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:28:07` | `cowrie.session.connect` |
| `2026-06-20 09:28:08` | `cowrie.client.version` |
| `2026-06-20 09:28:08` | `cowrie.client.kex` |
| `2026-06-20 09:28:15` | `cowrie.login.success` |
| `2026-06-20 09:28:15` | `cowrie.direct-tcpip.request` |
| `2026-06-20 09:28:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-20 09:28:15` | `cowrie.direct-tcpip.data` |
| `2026-06-20 09:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.7[.]135` to AbuseIPDB if not already reported
- [ ] Block `27.79.7[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b28cdf487d33

| Field | Detail |
|---|---|
| **Source IP** | `45.184.226[.]43` |
| **First Seen** | 2026-06-20 09:34 |
| **Last Seen** | 2026-06-20 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:34:02` | `cowrie.session.connect` |
| `2026-06-20 09:34:02` | `cowrie.client.version` |
| `2026-06-20 09:34:02` | `cowrie.client.kex` |
| `2026-06-20 09:34:03` | `cowrie.login.success` |
| `2026-06-20 09:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.184.226[.]43` to AbuseIPDB if not already reported
- [ ] Block `45.184.226[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f58eeec252

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-20 09:34 |
| **Last Seen** | 2026-06-20 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:34:05` | `cowrie.session.connect` |
| `2026-06-20 09:34:05` | `cowrie.client.version` |
| `2026-06-20 09:34:05` | `cowrie.client.kex` |
| `2026-06-20 09:34:06` | `cowrie.login.success` |
| `2026-06-20 09:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3236cb5315

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 09:35 |
| **Last Seen** | 2026-06-20 09:36 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:35:36` | `cowrie.session.connect` |
| `2026-06-20 09:35:39` | `cowrie.client.version` |
| `2026-06-20 09:35:39` | `cowrie.client.kex` |
| `2026-06-20 09:36:02` | `cowrie.login.success` |
| `2026-06-20 09:36:09` | `cowrie.session.params` |
| `2026-06-20 09:36:09` | `cowrie.command.input` |
| `2026-06-20 09:36:14` | `cowrie.log.closed` |
| `2026-06-20 09:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5301c5abbac

| Field | Detail |
|---|---|
| **Source IP** | `27.79.7[.]135` |
| **First Seen** | 2026-06-20 09:42 |
| **Last Seen** | 2026-06-20 09:43 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:42:32` | `cowrie.session.connect` |
| `2026-06-20 09:42:32` | `cowrie.client.version` |
| `2026-06-20 09:42:37` | `cowrie.client.kex` |
| `2026-06-20 09:42:49` | `cowrie.login.success` |
| `2026-06-20 09:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.7[.]135` to AbuseIPDB if not already reported
- [ ] Block `27.79.7[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc461cf8851

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 09:51 |
| **Last Seen** | 2026-06-20 09:52 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:51:37` | `cowrie.session.connect` |
| `2026-06-20 09:51:40` | `cowrie.client.version` |
| `2026-06-20 09:51:40` | `cowrie.client.kex` |
| `2026-06-20 09:51:58` | `cowrie.login.success` |
| `2026-06-20 09:52:07` | `cowrie.session.params` |
| `2026-06-20 09:52:07` | `cowrie.command.input` |
| `2026-06-20 09:52:12` | `cowrie.log.closed` |
| `2026-06-20 09:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50e014b58b9

| Field | Detail |
|---|---|
| **Source IP** | `27.79.7[.]135` |
| **First Seen** | 2026-06-20 09:51 |
| **Last Seen** | 2026-06-20 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:51:44` | `cowrie.session.connect` |
| `2026-06-20 09:51:44` | `cowrie.client.version` |
| `2026-06-20 09:51:46` | `cowrie.client.kex` |
| `2026-06-20 09:51:46` | `cowrie.login.success` |
| `2026-06-20 09:51:47` | `cowrie.direct-tcpip.request` |
| `2026-06-20 09:51:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-20 09:51:47` | `cowrie.direct-tcpip.data` |
| `2026-06-20 09:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.7[.]135` to AbuseIPDB if not already reported
- [ ] Block `27.79.7[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33722db6ea4e

| Field | Detail |
|---|---|
| **Source IP** | `27.79.7[.]135` |
| **First Seen** | 2026-06-20 09:55 |
| **Last Seen** | 2026-06-20 09:56 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 09:55:10` | `cowrie.session.connect` |
| `2026-06-20 09:55:10` | `cowrie.client.version` |
| `2026-06-20 09:55:12` | `cowrie.client.kex` |
| `2026-06-20 09:55:40` | `cowrie.login.success` |
| `2026-06-20 09:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.7[.]135` to AbuseIPDB if not already reported
- [ ] Block `27.79.7[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0daf2bed1d7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-20 10:08 |
| **Last Seen** | 2026-06-20 10:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:08:51` | `cowrie.session.connect` |
| `2026-06-20 10:08:51` | `cowrie.client.version` |
| `2026-06-20 10:08:52` | `cowrie.client.kex` |
| `2026-06-20 10:08:53` | `cowrie.login.success` |
| `2026-06-20 10:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a0e6ce8afa

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-20 10:08 |
| **Last Seen** | 2026-06-20 10:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:08:52` | `cowrie.session.connect` |
| `2026-06-20 10:08:52` | `cowrie.client.version` |
| `2026-06-20 10:08:52` | `cowrie.client.kex` |
| `2026-06-20 10:08:53` | `cowrie.login.success` |
| `2026-06-20 10:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db34f0819c2e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]186` |
| **First Seen** | 2026-06-20 10:09 |
| **Last Seen** | 2026-06-20 10:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:09:37` | `cowrie.session.connect` |
| `2026-06-20 10:09:37` | `cowrie.client.version` |
| `2026-06-20 10:09:37` | `cowrie.client.kex` |
| `2026-06-20 10:09:38` | `cowrie.login.success` |
| `2026-06-20 10:09:40` | `cowrie.session.params` |
| `2026-06-20 10:09:40` | `cowrie.command.input` |
| `2026-06-20 10:09:40` | `cowrie.log.closed` |
| `2026-06-20 10:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]186` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37f59c2c1ccb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]186` |
| **First Seen** | 2026-06-20 10:14 |
| **Last Seen** | 2026-06-20 10:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:14:09` | `cowrie.session.connect` |
| `2026-06-20 10:14:10` | `cowrie.client.version` |
| `2026-06-20 10:14:10` | `cowrie.client.kex` |
| `2026-06-20 10:14:13` | `cowrie.login.success` |
| `2026-06-20 10:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]186` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d220f44eb5c6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 10:16 |
| **Last Seen** | 2026-06-20 10:16 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:16:12` | `cowrie.session.connect` |
| `2026-06-20 10:16:15` | `cowrie.client.version` |
| `2026-06-20 10:16:15` | `cowrie.client.kex` |
| `2026-06-20 10:16:31` | `cowrie.login.success` |
| `2026-06-20 10:16:41` | `cowrie.session.params` |
| `2026-06-20 10:16:41` | `cowrie.command.input` |
| `2026-06-20 10:16:44` | `cowrie.log.closed` |
| `2026-06-20 10:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2efcd337d90d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]186` |
| **First Seen** | 2026-06-20 10:18 |
| **Last Seen** | 2026-06-20 10:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:18:23` | `cowrie.session.connect` |
| `2026-06-20 10:18:23` | `cowrie.client.version` |
| `2026-06-20 10:18:23` | `cowrie.client.kex` |
| `2026-06-20 10:18:25` | `cowrie.login.success` |
| `2026-06-20 10:18:26` | `cowrie.session.params` |
| `2026-06-20 10:18:26` | `cowrie.command.input` |
| `2026-06-20 10:18:27` | `cowrie.log.closed` |
| `2026-06-20 10:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]186` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e96c711eb6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]186` |
| **First Seen** | 2026-06-20 10:22 |
| **Last Seen** | 2026-06-20 10:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:22:18` | `cowrie.session.connect` |
| `2026-06-20 10:22:18` | `cowrie.client.version` |
| `2026-06-20 10:22:18` | `cowrie.client.kex` |
| `2026-06-20 10:22:23` | `cowrie.login.success` |
| `2026-06-20 10:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]186` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe246b46c0d0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 10:22 |
| **Last Seen** | 2026-06-20 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:22:46` | `cowrie.session.connect` |
| `2026-06-20 10:22:46` | `cowrie.client.version` |
| `2026-06-20 10:22:46` | `cowrie.client.kex` |
| `2026-06-20 10:22:47` | `cowrie.login.success` |
| `2026-06-20 10:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fef9eae54b1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 10:22 |
| **Last Seen** | 2026-06-20 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:22:46` | `cowrie.session.connect` |
| `2026-06-20 10:22:46` | `cowrie.client.version` |
| `2026-06-20 10:22:46` | `cowrie.client.kex` |
| `2026-06-20 10:22:47` | `cowrie.login.success` |
| `2026-06-20 10:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cac65040b4f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 10:22 |
| **Last Seen** | 2026-06-20 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:22:52` | `cowrie.session.connect` |
| `2026-06-20 10:22:52` | `cowrie.client.version` |
| `2026-06-20 10:22:52` | `cowrie.client.kex` |
| `2026-06-20 10:22:53` | `cowrie.login.success` |
| `2026-06-20 10:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f134dc8b4a0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 10:22 |
| **Last Seen** | 2026-06-20 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:22:53` | `cowrie.session.connect` |
| `2026-06-20 10:22:53` | `cowrie.client.version` |
| `2026-06-20 10:22:53` | `cowrie.client.kex` |
| `2026-06-20 10:22:54` | `cowrie.login.success` |
| `2026-06-20 10:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfefb5bbd78e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]186` |
| **First Seen** | 2026-06-20 10:26 |
| **Last Seen** | 2026-06-20 10:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:26:22` | `cowrie.session.connect` |
| `2026-06-20 10:26:22` | `cowrie.client.version` |
| `2026-06-20 10:26:22` | `cowrie.client.kex` |
| `2026-06-20 10:26:24` | `cowrie.login.success` |
| `2026-06-20 10:26:26` | `cowrie.session.params` |
| `2026-06-20 10:26:26` | `cowrie.command.input` |
| `2026-06-20 10:26:26` | `cowrie.log.closed` |
| `2026-06-20 10:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]186` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-343401c469e4

| Field | Detail |
|---|---|
| **Source IP** | `101.206.107[.]245` |
| **First Seen** | 2026-06-20 10:27 |
| **Last Seen** | 2026-06-20 10:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:27:26` | `cowrie.session.connect` |
| `2026-06-20 10:27:26` | `cowrie.client.version` |
| `2026-06-20 10:27:26` | `cowrie.client.kex` |
| `2026-06-20 10:27:32` | `cowrie.login.success` |
| `2026-06-20 10:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.206.107[.]245` to AbuseIPDB if not already reported
- [ ] Block `101.206.107[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d94d06c3689

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]186` |
| **First Seen** | 2026-06-20 10:30 |
| **Last Seen** | 2026-06-20 10:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:30:34` | `cowrie.session.connect` |
| `2026-06-20 10:30:34` | `cowrie.client.version` |
| `2026-06-20 10:30:34` | `cowrie.client.kex` |
| `2026-06-20 10:30:35` | `cowrie.login.success` |
| `2026-06-20 10:30:37` | `cowrie.session.params` |
| `2026-06-20 10:30:37` | `cowrie.command.input` |
| `2026-06-20 10:30:37` | `cowrie.log.closed` |
| `2026-06-20 10:30:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]186` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-131181288c92

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 10:32 |
| **Last Seen** | 2026-06-20 10:33 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:32:43` | `cowrie.session.connect` |
| `2026-06-20 10:32:46` | `cowrie.client.version` |
| `2026-06-20 10:32:46` | `cowrie.client.kex` |
| `2026-06-20 10:33:02` | `cowrie.login.success` |
| `2026-06-20 10:33:10` | `cowrie.session.params` |
| `2026-06-20 10:33:10` | `cowrie.command.input` |
| `2026-06-20 10:33:19` | `cowrie.log.closed` |
| `2026-06-20 10:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e61b224eff1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:33 |
| **Last Seen** | 2026-06-20 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:33:32` | `cowrie.session.connect` |
| `2026-06-20 10:33:32` | `cowrie.client.version` |
| `2026-06-20 10:33:33` | `cowrie.client.kex` |
| `2026-06-20 10:33:33` | `cowrie.login.success` |
| `2026-06-20 10:33:34` | `cowrie.session.params` |
| `2026-06-20 10:33:34` | `cowrie.command.input` |
| `2026-06-20 10:33:34` | `cowrie.log.closed` |
| `2026-06-20 10:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e66b6739b4ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:33 |
| **Last Seen** | 2026-06-20 10:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:33:39` | `cowrie.session.connect` |
| `2026-06-20 10:33:40` | `cowrie.client.version` |
| `2026-06-20 10:33:40` | `cowrie.client.kex` |
| `2026-06-20 10:33:43` | `cowrie.login.success` |
| `2026-06-20 10:33:44` | `cowrie.session.params` |
| `2026-06-20 10:33:44` | `cowrie.command.input` |
| `2026-06-20 10:33:45` | `cowrie.log.closed` |
| `2026-06-20 10:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-490224158c53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:33 |
| **Last Seen** | 2026-06-20 10:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:33:47` | `cowrie.session.connect` |
| `2026-06-20 10:33:48` | `cowrie.client.version` |
| `2026-06-20 10:33:48` | `cowrie.client.kex` |
| `2026-06-20 10:33:51` | `cowrie.login.success` |
| `2026-06-20 10:33:53` | `cowrie.session.params` |
| `2026-06-20 10:33:53` | `cowrie.command.input` |
| `2026-06-20 10:33:53` | `cowrie.log.closed` |
| `2026-06-20 10:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df94e6da07e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:33 |
| **Last Seen** | 2026-06-20 10:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:33:53` | `cowrie.session.connect` |
| `2026-06-20 10:33:54` | `cowrie.client.version` |
| `2026-06-20 10:33:54` | `cowrie.client.kex` |
| `2026-06-20 10:33:58` | `cowrie.login.success` |
| `2026-06-20 10:34:00` | `cowrie.session.params` |
| `2026-06-20 10:34:00` | `cowrie.command.input` |
| `2026-06-20 10:34:01` | `cowrie.log.closed` |
| `2026-06-20 10:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a17b2d6f33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:34 |
| **Last Seen** | 2026-06-20 10:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:34:00` | `cowrie.session.connect` |
| `2026-06-20 10:34:01` | `cowrie.client.version` |
| `2026-06-20 10:34:01` | `cowrie.client.kex` |
| `2026-06-20 10:34:05` | `cowrie.login.success` |
| `2026-06-20 10:34:08` | `cowrie.session.params` |
| `2026-06-20 10:34:08` | `cowrie.command.input` |
| `2026-06-20 10:34:09` | `cowrie.log.closed` |
| `2026-06-20 10:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a89609fa2b8f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:34 |
| **Last Seen** | 2026-06-20 10:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:34:06` | `cowrie.session.connect` |
| `2026-06-20 10:34:07` | `cowrie.client.version` |
| `2026-06-20 10:34:07` | `cowrie.client.kex` |
| `2026-06-20 10:34:12` | `cowrie.login.success` |
| `2026-06-20 10:34:16` | `cowrie.session.params` |
| `2026-06-20 10:34:16` | `cowrie.command.input` |
| `2026-06-20 10:34:18` | `cowrie.log.closed` |
| `2026-06-20 10:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9db7266a21c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:34 |
| **Last Seen** | 2026-06-20 10:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:34:12` | `cowrie.session.connect` |
| `2026-06-20 10:34:13` | `cowrie.client.version` |
| `2026-06-20 10:34:13` | `cowrie.client.kex` |
| `2026-06-20 10:34:20` | `cowrie.login.success` |
| `2026-06-20 10:34:23` | `cowrie.session.params` |
| `2026-06-20 10:34:23` | `cowrie.command.input` |
| `2026-06-20 10:34:25` | `cowrie.log.closed` |
| `2026-06-20 10:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4910e34a38ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:34 |
| **Last Seen** | 2026-06-20 10:34 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:34:19` | `cowrie.session.connect` |
| `2026-06-20 10:34:20` | `cowrie.client.version` |
| `2026-06-20 10:34:20` | `cowrie.client.kex` |
| `2026-06-20 10:34:27` | `cowrie.login.success` |
| `2026-06-20 10:34:31` | `cowrie.session.params` |
| `2026-06-20 10:34:31` | `cowrie.command.input` |
| `2026-06-20 10:34:33` | `cowrie.log.closed` |
| `2026-06-20 10:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fad997018d39

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:34 |
| **Last Seen** | 2026-06-20 10:34 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:34:24` | `cowrie.session.connect` |
| `2026-06-20 10:34:26` | `cowrie.client.version` |
| `2026-06-20 10:34:26` | `cowrie.client.kex` |
| `2026-06-20 10:34:33` | `cowrie.login.success` |
| `2026-06-20 10:34:38` | `cowrie.session.params` |
| `2026-06-20 10:34:38` | `cowrie.command.input` |
| `2026-06-20 10:34:40` | `cowrie.log.closed` |
| `2026-06-20 10:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adc732396aad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:34 |
| **Last Seen** | 2026-06-20 10:34 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:34:31` | `cowrie.session.connect` |
| `2026-06-20 10:34:33` | `cowrie.client.version` |
| `2026-06-20 10:34:33` | `cowrie.client.kex` |
| `2026-06-20 10:34:42` | `cowrie.login.success` |
| `2026-06-20 10:34:46` | `cowrie.session.params` |
| `2026-06-20 10:34:46` | `cowrie.command.input` |
| `2026-06-20 10:34:48` | `cowrie.log.closed` |
| `2026-06-20 10:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32451c263bdb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:34 |
| **Last Seen** | 2026-06-20 10:34 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:34:37` | `cowrie.session.connect` |
| `2026-06-20 10:34:39` | `cowrie.client.version` |
| `2026-06-20 10:34:39` | `cowrie.client.kex` |
| `2026-06-20 10:34:47` | `cowrie.login.success` |
| `2026-06-20 10:34:53` | `cowrie.session.params` |
| `2026-06-20 10:34:53` | `cowrie.command.input` |
| `2026-06-20 10:34:55` | `cowrie.log.closed` |
| `2026-06-20 10:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200e82f244eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:34 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:34:44` | `cowrie.session.connect` |
| `2026-06-20 10:34:46` | `cowrie.client.version` |
| `2026-06-20 10:34:46` | `cowrie.client.kex` |
| `2026-06-20 10:34:55` | `cowrie.login.success` |
| `2026-06-20 10:35:01` | `cowrie.session.params` |
| `2026-06-20 10:35:01` | `cowrie.command.input` |
| `2026-06-20 10:35:04` | `cowrie.log.closed` |
| `2026-06-20 10:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-713a55bf9375

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:34 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:34:49` | `cowrie.session.connect` |
| `2026-06-20 10:34:52` | `cowrie.client.version` |
| `2026-06-20 10:34:52` | `cowrie.client.kex` |
| `2026-06-20 10:35:02` | `cowrie.login.success` |
| `2026-06-20 10:35:08` | `cowrie.session.params` |
| `2026-06-20 10:35:08` | `cowrie.command.input` |
| `2026-06-20 10:35:11` | `cowrie.log.closed` |
| `2026-06-20 10:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8dc82b5e10c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:34 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:34:56` | `cowrie.session.connect` |
| `2026-06-20 10:34:58` | `cowrie.client.version` |
| `2026-06-20 10:34:58` | `cowrie.client.kex` |
| `2026-06-20 10:35:09` | `cowrie.login.success` |
| `2026-06-20 10:35:17` | `cowrie.session.params` |
| `2026-06-20 10:35:17` | `cowrie.command.input` |
| `2026-06-20 10:35:20` | `cowrie.log.closed` |
| `2026-06-20 10:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e32879e9feb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:35 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:35:02` | `cowrie.session.connect` |
| `2026-06-20 10:35:04` | `cowrie.client.version` |
| `2026-06-20 10:35:04` | `cowrie.client.kex` |
| `2026-06-20 10:35:17` | `cowrie.login.success` |
| `2026-06-20 10:35:26` | `cowrie.session.params` |
| `2026-06-20 10:35:26` | `cowrie.command.input` |
| `2026-06-20 10:35:29` | `cowrie.log.closed` |
| `2026-06-20 10:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35a70f5305c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:35 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:35:08` | `cowrie.session.connect` |
| `2026-06-20 10:35:11` | `cowrie.client.version` |
| `2026-06-20 10:35:11` | `cowrie.client.kex` |
| `2026-06-20 10:35:25` | `cowrie.login.success` |
| `2026-06-20 10:35:32` | `cowrie.session.params` |
| `2026-06-20 10:35:32` | `cowrie.command.input` |
| `2026-06-20 10:35:34` | `cowrie.log.closed` |
| `2026-06-20 10:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8729cfd173a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:35 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:35:14` | `cowrie.session.connect` |
| `2026-06-20 10:35:17` | `cowrie.client.version` |
| `2026-06-20 10:35:17` | `cowrie.client.kex` |
| `2026-06-20 10:35:31` | `cowrie.login.success` |
| `2026-06-20 10:35:36` | `cowrie.session.params` |
| `2026-06-20 10:35:36` | `cowrie.command.input` |
| `2026-06-20 10:35:39` | `cowrie.log.closed` |
| `2026-06-20 10:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-061f8ba4eeaf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:35 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:35:19` | `cowrie.session.connect` |
| `2026-06-20 10:35:23` | `cowrie.client.version` |
| `2026-06-20 10:35:23` | `cowrie.client.kex` |
| `2026-06-20 10:35:35` | `cowrie.login.success` |
| `2026-06-20 10:35:41` | `cowrie.session.params` |
| `2026-06-20 10:35:41` | `cowrie.command.input` |
| `2026-06-20 10:35:43` | `cowrie.log.closed` |
| `2026-06-20 10:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fff2c6608e6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]186` |
| **First Seen** | 2026-06-20 10:35 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:35:24` | `cowrie.session.connect` |
| `2026-06-20 10:35:24` | `cowrie.client.version` |
| `2026-06-20 10:35:25` | `cowrie.client.kex` |
| `2026-06-20 10:35:26` | `cowrie.login.success` |
| `2026-06-20 10:35:28` | `cowrie.session.params` |
| `2026-06-20 10:35:28` | `cowrie.command.input` |
| `2026-06-20 10:35:28` | `cowrie.log.closed` |
| `2026-06-20 10:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]186` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e965c215a45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:35 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:35:28` | `cowrie.session.connect` |
| `2026-06-20 10:35:30` | `cowrie.client.version` |
| `2026-06-20 10:35:30` | `cowrie.client.kex` |
| `2026-06-20 10:35:41` | `cowrie.login.success` |
| `2026-06-20 10:35:45` | `cowrie.session.params` |
| `2026-06-20 10:35:45` | `cowrie.command.input` |
| `2026-06-20 10:35:46` | `cowrie.log.closed` |
| `2026-06-20 10:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effb8385f030

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:35 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:35:35` | `cowrie.session.connect` |
| `2026-06-20 10:35:38` | `cowrie.client.version` |
| `2026-06-20 10:35:38` | `cowrie.client.kex` |
| `2026-06-20 10:35:45` | `cowrie.login.success` |
| `2026-06-20 10:35:48` | `cowrie.session.params` |
| `2026-06-20 10:35:48` | `cowrie.command.input` |
| `2026-06-20 10:35:49` | `cowrie.log.closed` |
| `2026-06-20 10:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9846698bace7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:35 |
| **Last Seen** | 2026-06-20 10:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:35:45` | `cowrie.session.connect` |
| `2026-06-20 10:35:46` | `cowrie.client.version` |
| `2026-06-20 10:35:46` | `cowrie.client.kex` |
| `2026-06-20 10:35:50` | `cowrie.login.success` |
| `2026-06-20 10:35:53` | `cowrie.session.params` |
| `2026-06-20 10:35:53` | `cowrie.command.input` |
| `2026-06-20 10:35:54` | `cowrie.log.closed` |
| `2026-06-20 10:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a020b0ea41

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:35 |
| **Last Seen** | 2026-06-20 10:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:35:52` | `cowrie.session.connect` |
| `2026-06-20 10:35:53` | `cowrie.client.version` |
| `2026-06-20 10:35:53` | `cowrie.client.kex` |
| `2026-06-20 10:35:57` | `cowrie.login.success` |
| `2026-06-20 10:36:00` | `cowrie.session.params` |
| `2026-06-20 10:36:00` | `cowrie.command.input` |
| `2026-06-20 10:36:01` | `cowrie.log.closed` |
| `2026-06-20 10:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d44a23f4de6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:35 |
| **Last Seen** | 2026-06-20 10:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:35:58` | `cowrie.session.connect` |
| `2026-06-20 10:35:59` | `cowrie.client.version` |
| `2026-06-20 10:35:59` | `cowrie.client.kex` |
| `2026-06-20 10:36:04` | `cowrie.login.success` |
| `2026-06-20 10:36:07` | `cowrie.session.params` |
| `2026-06-20 10:36:07` | `cowrie.command.input` |
| `2026-06-20 10:36:08` | `cowrie.log.closed` |
| `2026-06-20 10:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6325aa716acc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:36 |
| **Last Seen** | 2026-06-20 10:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:36:05` | `cowrie.session.connect` |
| `2026-06-20 10:36:06` | `cowrie.client.version` |
| `2026-06-20 10:36:06` | `cowrie.client.kex` |
| `2026-06-20 10:36:11` | `cowrie.login.success` |
| `2026-06-20 10:36:14` | `cowrie.session.params` |
| `2026-06-20 10:36:14` | `cowrie.command.input` |
| `2026-06-20 10:36:15` | `cowrie.log.closed` |
| `2026-06-20 10:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb74d0db98e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:36 |
| **Last Seen** | 2026-06-20 10:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:36:11` | `cowrie.session.connect` |
| `2026-06-20 10:36:12` | `cowrie.client.version` |
| `2026-06-20 10:36:12` | `cowrie.client.kex` |
| `2026-06-20 10:36:16` | `cowrie.login.success` |
| `2026-06-20 10:36:20` | `cowrie.session.params` |
| `2026-06-20 10:36:20` | `cowrie.command.input` |
| `2026-06-20 10:36:21` | `cowrie.log.closed` |
| `2026-06-20 10:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-670f52ff19a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:36 |
| **Last Seen** | 2026-06-20 10:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:36:17` | `cowrie.session.connect` |
| `2026-06-20 10:36:18` | `cowrie.client.version` |
| `2026-06-20 10:36:18` | `cowrie.client.kex` |
| `2026-06-20 10:36:24` | `cowrie.login.success` |
| `2026-06-20 10:36:27` | `cowrie.session.params` |
| `2026-06-20 10:36:27` | `cowrie.command.input` |
| `2026-06-20 10:36:28` | `cowrie.log.closed` |
| `2026-06-20 10:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c19215df0e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:36 |
| **Last Seen** | 2026-06-20 10:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:36:23` | `cowrie.session.connect` |
| `2026-06-20 10:36:25` | `cowrie.client.version` |
| `2026-06-20 10:36:25` | `cowrie.client.kex` |
| `2026-06-20 10:36:29` | `cowrie.login.success` |
| `2026-06-20 10:36:32` | `cowrie.session.params` |
| `2026-06-20 10:36:32` | `cowrie.command.input` |
| `2026-06-20 10:36:34` | `cowrie.log.closed` |
| `2026-06-20 10:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d50789374e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:36 |
| **Last Seen** | 2026-06-20 10:36 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:36:29` | `cowrie.session.connect` |
| `2026-06-20 10:36:31` | `cowrie.client.version` |
| `2026-06-20 10:36:31` | `cowrie.client.kex` |
| `2026-06-20 10:36:37` | `cowrie.login.success` |
| `2026-06-20 10:36:40` | `cowrie.session.params` |
| `2026-06-20 10:36:40` | `cowrie.command.input` |
| `2026-06-20 10:36:41` | `cowrie.log.closed` |
| `2026-06-20 10:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db62c70f544

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:36 |
| **Last Seen** | 2026-06-20 10:36 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:36:35` | `cowrie.session.connect` |
| `2026-06-20 10:36:37` | `cowrie.client.version` |
| `2026-06-20 10:36:37` | `cowrie.client.kex` |
| `2026-06-20 10:36:43` | `cowrie.login.success` |
| `2026-06-20 10:36:46` | `cowrie.session.params` |
| `2026-06-20 10:36:46` | `cowrie.command.input` |
| `2026-06-20 10:36:47` | `cowrie.log.closed` |
| `2026-06-20 10:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71cd2368a7cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:36 |
| **Last Seen** | 2026-06-20 10:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:36:41` | `cowrie.session.connect` |
| `2026-06-20 10:36:43` | `cowrie.client.version` |
| `2026-06-20 10:36:43` | `cowrie.client.kex` |
| `2026-06-20 10:36:47` | `cowrie.login.success` |
| `2026-06-20 10:36:49` | `cowrie.session.params` |
| `2026-06-20 10:36:49` | `cowrie.command.input` |
| `2026-06-20 10:36:50` | `cowrie.log.closed` |
| `2026-06-20 10:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1427d6da7048

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:36 |
| **Last Seen** | 2026-06-20 10:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:36:49` | `cowrie.session.connect` |
| `2026-06-20 10:36:50` | `cowrie.client.version` |
| `2026-06-20 10:36:50` | `cowrie.client.kex` |
| `2026-06-20 10:36:54` | `cowrie.login.success` |
| `2026-06-20 10:36:56` | `cowrie.session.params` |
| `2026-06-20 10:36:56` | `cowrie.command.input` |
| `2026-06-20 10:36:58` | `cowrie.log.closed` |
| `2026-06-20 10:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b186afd2438d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:36 |
| **Last Seen** | 2026-06-20 10:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:36:54` | `cowrie.session.connect` |
| `2026-06-20 10:36:55` | `cowrie.client.version` |
| `2026-06-20 10:36:55` | `cowrie.client.kex` |
| `2026-06-20 10:37:00` | `cowrie.login.success` |
| `2026-06-20 10:37:03` | `cowrie.session.params` |
| `2026-06-20 10:37:03` | `cowrie.command.input` |
| `2026-06-20 10:37:04` | `cowrie.log.closed` |
| `2026-06-20 10:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccd814f4390f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:37 |
| **Last Seen** | 2026-06-20 10:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:37:00` | `cowrie.session.connect` |
| `2026-06-20 10:37:01` | `cowrie.client.version` |
| `2026-06-20 10:37:01` | `cowrie.client.kex` |
| `2026-06-20 10:37:06` | `cowrie.login.success` |
| `2026-06-20 10:37:07` | `cowrie.session.params` |
| `2026-06-20 10:37:07` | `cowrie.command.input` |
| `2026-06-20 10:37:08` | `cowrie.log.closed` |
| `2026-06-20 10:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b51525d3bc83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:37 |
| **Last Seen** | 2026-06-20 10:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:37:08` | `cowrie.session.connect` |
| `2026-06-20 10:37:08` | `cowrie.client.version` |
| `2026-06-20 10:37:08` | `cowrie.client.kex` |
| `2026-06-20 10:37:10` | `cowrie.login.success` |
| `2026-06-20 10:37:11` | `cowrie.session.params` |
| `2026-06-20 10:37:11` | `cowrie.command.input` |
| `2026-06-20 10:37:12` | `cowrie.log.closed` |
| `2026-06-20 10:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d3ac9ac13a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:37 |
| **Last Seen** | 2026-06-20 10:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:37:15` | `cowrie.session.connect` |
| `2026-06-20 10:37:15` | `cowrie.client.version` |
| `2026-06-20 10:37:15` | `cowrie.client.kex` |
| `2026-06-20 10:37:17` | `cowrie.login.success` |
| `2026-06-20 10:37:18` | `cowrie.session.params` |
| `2026-06-20 10:37:18` | `cowrie.command.input` |
| `2026-06-20 10:37:18` | `cowrie.log.closed` |
| `2026-06-20 10:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc4d231852a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:37 |
| **Last Seen** | 2026-06-20 10:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:37:21` | `cowrie.session.connect` |
| `2026-06-20 10:37:21` | `cowrie.client.version` |
| `2026-06-20 10:37:21` | `cowrie.client.kex` |
| `2026-06-20 10:37:23` | `cowrie.login.success` |
| `2026-06-20 10:37:25` | `cowrie.session.params` |
| `2026-06-20 10:37:25` | `cowrie.command.input` |
| `2026-06-20 10:37:25` | `cowrie.log.closed` |
| `2026-06-20 10:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed95a5df487c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:37 |
| **Last Seen** | 2026-06-20 10:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:37:28` | `cowrie.session.connect` |
| `2026-06-20 10:37:28` | `cowrie.client.version` |
| `2026-06-20 10:37:28` | `cowrie.client.kex` |
| `2026-06-20 10:37:28` | `cowrie.login.success` |
| `2026-06-20 10:37:30` | `cowrie.session.params` |
| `2026-06-20 10:37:30` | `cowrie.command.input` |
| `2026-06-20 10:37:30` | `cowrie.log.closed` |
| `2026-06-20 10:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-028a3b166f6c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:37 |
| **Last Seen** | 2026-06-20 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:37:34` | `cowrie.session.connect` |
| `2026-06-20 10:37:34` | `cowrie.client.version` |
| `2026-06-20 10:37:34` | `cowrie.client.kex` |
| `2026-06-20 10:37:35` | `cowrie.login.success` |
| `2026-06-20 10:37:35` | `cowrie.session.params` |
| `2026-06-20 10:37:35` | `cowrie.command.input` |
| `2026-06-20 10:37:36` | `cowrie.log.closed` |
| `2026-06-20 10:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7ac53327a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:37 |
| **Last Seen** | 2026-06-20 10:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:37:40` | `cowrie.session.connect` |
| `2026-06-20 10:37:40` | `cowrie.client.version` |
| `2026-06-20 10:37:41` | `cowrie.client.kex` |
| `2026-06-20 10:37:42` | `cowrie.login.success` |
| `2026-06-20 10:37:43` | `cowrie.session.params` |
| `2026-06-20 10:37:43` | `cowrie.command.input` |
| `2026-06-20 10:37:44` | `cowrie.log.closed` |
| `2026-06-20 10:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f715d23e189c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:37 |
| **Last Seen** | 2026-06-20 10:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:37:46` | `cowrie.session.connect` |
| `2026-06-20 10:37:47` | `cowrie.client.version` |
| `2026-06-20 10:37:47` | `cowrie.client.kex` |
| `2026-06-20 10:37:48` | `cowrie.login.success` |
| `2026-06-20 10:37:49` | `cowrie.session.params` |
| `2026-06-20 10:37:49` | `cowrie.command.input` |
| `2026-06-20 10:37:50` | `cowrie.log.closed` |
| `2026-06-20 10:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3d34adc098

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:37 |
| **Last Seen** | 2026-06-20 10:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:37:52` | `cowrie.session.connect` |
| `2026-06-20 10:37:53` | `cowrie.client.version` |
| `2026-06-20 10:37:53` | `cowrie.client.kex` |
| `2026-06-20 10:37:54` | `cowrie.login.success` |
| `2026-06-20 10:37:55` | `cowrie.session.params` |
| `2026-06-20 10:37:55` | `cowrie.command.input` |
| `2026-06-20 10:37:56` | `cowrie.log.closed` |
| `2026-06-20 10:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9c11416bdc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:37 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:37:59` | `cowrie.session.connect` |
| `2026-06-20 10:37:59` | `cowrie.client.version` |
| `2026-06-20 10:37:59` | `cowrie.client.kex` |
| `2026-06-20 10:38:00` | `cowrie.login.success` |
| `2026-06-20 10:38:01` | `cowrie.session.params` |
| `2026-06-20 10:38:01` | `cowrie.command.input` |
| `2026-06-20 10:38:02` | `cowrie.log.closed` |
| `2026-06-20 10:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93447c35f971

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:06` | `cowrie.session.connect` |
| `2026-06-20 10:38:06` | `cowrie.client.version` |
| `2026-06-20 10:38:06` | `cowrie.client.kex` |
| `2026-06-20 10:38:07` | `cowrie.login.success` |
| `2026-06-20 10:38:08` | `cowrie.session.params` |
| `2026-06-20 10:38:08` | `cowrie.command.input` |
| `2026-06-20 10:38:08` | `cowrie.log.closed` |
| `2026-06-20 10:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a56381cd3aba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:12` | `cowrie.session.connect` |
| `2026-06-20 10:38:12` | `cowrie.client.version` |
| `2026-06-20 10:38:12` | `cowrie.client.kex` |
| `2026-06-20 10:38:13` | `cowrie.login.success` |
| `2026-06-20 10:38:14` | `cowrie.session.params` |
| `2026-06-20 10:38:14` | `cowrie.command.input` |
| `2026-06-20 10:38:14` | `cowrie.log.closed` |
| `2026-06-20 10:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0cbe2e08aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:18` | `cowrie.session.connect` |
| `2026-06-20 10:38:18` | `cowrie.client.version` |
| `2026-06-20 10:38:18` | `cowrie.client.kex` |
| `2026-06-20 10:38:19` | `cowrie.login.success` |
| `2026-06-20 10:38:21` | `cowrie.session.params` |
| `2026-06-20 10:38:21` | `cowrie.command.input` |
| `2026-06-20 10:38:21` | `cowrie.log.closed` |
| `2026-06-20 10:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-501fdf02275d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:24` | `cowrie.session.connect` |
| `2026-06-20 10:38:25` | `cowrie.client.version` |
| `2026-06-20 10:38:25` | `cowrie.client.kex` |
| `2026-06-20 10:38:26` | `cowrie.login.success` |
| `2026-06-20 10:38:27` | `cowrie.session.params` |
| `2026-06-20 10:38:27` | `cowrie.command.input` |
| `2026-06-20 10:38:28` | `cowrie.log.closed` |
| `2026-06-20 10:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41dab5700d9f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:30` | `cowrie.session.connect` |
| `2026-06-20 10:38:30` | `cowrie.client.version` |
| `2026-06-20 10:38:31` | `cowrie.client.kex` |
| `2026-06-20 10:38:32` | `cowrie.login.success` |
| `2026-06-20 10:38:34` | `cowrie.session.params` |
| `2026-06-20 10:38:34` | `cowrie.command.input` |
| `2026-06-20 10:38:34` | `cowrie.log.closed` |
| `2026-06-20 10:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15c729443f95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:36` | `cowrie.session.connect` |
| `2026-06-20 10:38:37` | `cowrie.client.version` |
| `2026-06-20 10:38:37` | `cowrie.client.kex` |
| `2026-06-20 10:38:38` | `cowrie.login.success` |
| `2026-06-20 10:38:40` | `cowrie.session.params` |
| `2026-06-20 10:38:40` | `cowrie.command.input` |
| `2026-06-20 10:38:41` | `cowrie.log.closed` |
| `2026-06-20 10:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f9be63d2af

| Field | Detail |
|---|---|
| **Source IP** | `212.227.235[.]203` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:38` | `cowrie.session.connect` |
| `2026-06-20 10:38:38` | `cowrie.client.version` |
| `2026-06-20 10:38:39` | `cowrie.client.kex` |
| `2026-06-20 10:38:39` | `cowrie.login.success` |
| `2026-06-20 10:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.227.235[.]203` to AbuseIPDB if not already reported
- [ ] Block `212.227.235[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14240357e423

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:39` | `cowrie.session.connect` |
| `2026-06-20 10:38:39` | `cowrie.client.version` |
| `2026-06-20 10:38:39` | `cowrie.client.kex` |
| `2026-06-20 10:38:39` | `cowrie.login.success` |
| `2026-06-20 10:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79872f7c07ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:42` | `cowrie.session.connect` |
| `2026-06-20 10:38:43` | `cowrie.client.version` |
| `2026-06-20 10:38:43` | `cowrie.client.kex` |
| `2026-06-20 10:38:45` | `cowrie.login.success` |
| `2026-06-20 10:38:47` | `cowrie.session.params` |
| `2026-06-20 10:38:47` | `cowrie.command.input` |
| `2026-06-20 10:38:48` | `cowrie.log.closed` |
| `2026-06-20 10:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd15f33f3ba7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:48` | `cowrie.session.connect` |
| `2026-06-20 10:38:49` | `cowrie.client.version` |
| `2026-06-20 10:38:49` | `cowrie.client.kex` |
| `2026-06-20 10:38:51` | `cowrie.login.success` |
| `2026-06-20 10:38:53` | `cowrie.session.params` |
| `2026-06-20 10:38:53` | `cowrie.command.input` |
| `2026-06-20 10:38:54` | `cowrie.log.closed` |
| `2026-06-20 10:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d8fe686f6d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:38 |
| **Last Seen** | 2026-06-20 10:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:38:54` | `cowrie.session.connect` |
| `2026-06-20 10:38:55` | `cowrie.client.version` |
| `2026-06-20 10:38:55` | `cowrie.client.kex` |
| `2026-06-20 10:38:58` | `cowrie.login.success` |
| `2026-06-20 10:38:59` | `cowrie.session.params` |
| `2026-06-20 10:38:59` | `cowrie.command.input` |
| `2026-06-20 10:39:00` | `cowrie.log.closed` |
| `2026-06-20 10:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8b4225a1bb9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:39 |
| **Last Seen** | 2026-06-20 10:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:39:00` | `cowrie.session.connect` |
| `2026-06-20 10:39:01` | `cowrie.client.version` |
| `2026-06-20 10:39:01` | `cowrie.client.kex` |
| `2026-06-20 10:39:03` | `cowrie.login.success` |
| `2026-06-20 10:39:05` | `cowrie.session.params` |
| `2026-06-20 10:39:05` | `cowrie.command.input` |
| `2026-06-20 10:39:05` | `cowrie.log.closed` |
| `2026-06-20 10:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef86cd9e3d83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:39 |
| **Last Seen** | 2026-06-20 10:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:39:07` | `cowrie.session.connect` |
| `2026-06-20 10:39:08` | `cowrie.client.version` |
| `2026-06-20 10:39:08` | `cowrie.client.kex` |
| `2026-06-20 10:39:09` | `cowrie.login.success` |
| `2026-06-20 10:39:10` | `cowrie.session.params` |
| `2026-06-20 10:39:10` | `cowrie.command.input` |
| `2026-06-20 10:39:11` | `cowrie.log.closed` |
| `2026-06-20 10:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e76e814539

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:39 |
| **Last Seen** | 2026-06-20 10:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:39:13` | `cowrie.session.connect` |
| `2026-06-20 10:39:13` | `cowrie.client.version` |
| `2026-06-20 10:39:13` | `cowrie.client.kex` |
| `2026-06-20 10:39:15` | `cowrie.login.success` |
| `2026-06-20 10:39:17` | `cowrie.session.params` |
| `2026-06-20 10:39:17` | `cowrie.command.input` |
| `2026-06-20 10:39:17` | `cowrie.log.closed` |
| `2026-06-20 10:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-285d2e3dd1b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:39 |
| **Last Seen** | 2026-06-20 10:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:39:20` | `cowrie.session.connect` |
| `2026-06-20 10:39:20` | `cowrie.client.version` |
| `2026-06-20 10:39:20` | `cowrie.client.kex` |
| `2026-06-20 10:39:21` | `cowrie.login.success` |
| `2026-06-20 10:39:22` | `cowrie.session.params` |
| `2026-06-20 10:39:22` | `cowrie.command.input` |
| `2026-06-20 10:39:23` | `cowrie.log.closed` |
| `2026-06-20 10:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f343939131c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:39 |
| **Last Seen** | 2026-06-20 10:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:39:26` | `cowrie.session.connect` |
| `2026-06-20 10:39:26` | `cowrie.client.version` |
| `2026-06-20 10:39:26` | `cowrie.client.kex` |
| `2026-06-20 10:39:27` | `cowrie.login.success` |
| `2026-06-20 10:39:28` | `cowrie.session.params` |
| `2026-06-20 10:39:28` | `cowrie.command.input` |
| `2026-06-20 10:39:29` | `cowrie.log.closed` |
| `2026-06-20 10:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2da488f9286

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:39 |
| **Last Seen** | 2026-06-20 10:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:39:31` | `cowrie.session.connect` |
| `2026-06-20 10:39:31` | `cowrie.client.version` |
| `2026-06-20 10:39:31` | `cowrie.client.kex` |
| `2026-06-20 10:39:34` | `cowrie.login.success` |
| `2026-06-20 10:39:35` | `cowrie.session.params` |
| `2026-06-20 10:39:35` | `cowrie.command.input` |
| `2026-06-20 10:39:36` | `cowrie.log.closed` |
| `2026-06-20 10:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a96cca7dbe5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:39 |
| **Last Seen** | 2026-06-20 10:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:39:37` | `cowrie.session.connect` |
| `2026-06-20 10:39:38` | `cowrie.client.version` |
| `2026-06-20 10:39:38` | `cowrie.client.kex` |
| `2026-06-20 10:39:40` | `cowrie.login.success` |
| `2026-06-20 10:39:42` | `cowrie.session.params` |
| `2026-06-20 10:39:42` | `cowrie.command.input` |
| `2026-06-20 10:39:43` | `cowrie.log.closed` |
| `2026-06-20 10:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a0b887a02b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:39 |
| **Last Seen** | 2026-06-20 10:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:39:43` | `cowrie.session.connect` |
| `2026-06-20 10:39:44` | `cowrie.client.version` |
| `2026-06-20 10:39:44` | `cowrie.client.kex` |
| `2026-06-20 10:39:45` | `cowrie.login.success` |
| `2026-06-20 10:39:46` | `cowrie.session.params` |
| `2026-06-20 10:39:46` | `cowrie.command.input` |
| `2026-06-20 10:39:47` | `cowrie.log.closed` |
| `2026-06-20 10:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45a05d52e97

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:39 |
| **Last Seen** | 2026-06-20 10:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:39:50` | `cowrie.session.connect` |
| `2026-06-20 10:39:50` | `cowrie.client.version` |
| `2026-06-20 10:39:50` | `cowrie.client.kex` |
| `2026-06-20 10:39:51` | `cowrie.login.success` |
| `2026-06-20 10:39:53` | `cowrie.session.params` |
| `2026-06-20 10:39:53` | `cowrie.command.input` |
| `2026-06-20 10:39:53` | `cowrie.log.closed` |
| `2026-06-20 10:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa58554c45f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:39 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:39:56` | `cowrie.session.connect` |
| `2026-06-20 10:39:56` | `cowrie.client.version` |
| `2026-06-20 10:39:56` | `cowrie.client.kex` |
| `2026-06-20 10:39:58` | `cowrie.login.success` |
| `2026-06-20 10:39:59` | `cowrie.session.params` |
| `2026-06-20 10:39:59` | `cowrie.command.input` |
| `2026-06-20 10:40:00` | `cowrie.log.closed` |
| `2026-06-20 10:40:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e432942d2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:03` | `cowrie.session.connect` |
| `2026-06-20 10:40:03` | `cowrie.client.version` |
| `2026-06-20 10:40:03` | `cowrie.client.kex` |
| `2026-06-20 10:40:03` | `cowrie.login.success` |
| `2026-06-20 10:40:04` | `cowrie.session.params` |
| `2026-06-20 10:40:04` | `cowrie.command.input` |
| `2026-06-20 10:40:05` | `cowrie.log.closed` |
| `2026-06-20 10:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553c5ab714ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:09` | `cowrie.session.connect` |
| `2026-06-20 10:40:09` | `cowrie.client.version` |
| `2026-06-20 10:40:09` | `cowrie.client.kex` |
| `2026-06-20 10:40:11` | `cowrie.login.success` |
| `2026-06-20 10:40:12` | `cowrie.session.params` |
| `2026-06-20 10:40:12` | `cowrie.command.input` |
| `2026-06-20 10:40:13` | `cowrie.log.closed` |
| `2026-06-20 10:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95c7c2d5e246

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:15` | `cowrie.session.connect` |
| `2026-06-20 10:40:15` | `cowrie.client.version` |
| `2026-06-20 10:40:15` | `cowrie.client.kex` |
| `2026-06-20 10:40:17` | `cowrie.login.success` |
| `2026-06-20 10:40:18` | `cowrie.session.params` |
| `2026-06-20 10:40:18` | `cowrie.command.input` |
| `2026-06-20 10:40:19` | `cowrie.log.closed` |
| `2026-06-20 10:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ef4b9b995c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:22` | `cowrie.session.connect` |
| `2026-06-20 10:40:22` | `cowrie.client.version` |
| `2026-06-20 10:40:22` | `cowrie.client.kex` |
| `2026-06-20 10:40:22` | `cowrie.login.success` |
| `2026-06-20 10:40:23` | `cowrie.session.params` |
| `2026-06-20 10:40:23` | `cowrie.command.input` |
| `2026-06-20 10:40:23` | `cowrie.log.closed` |
| `2026-06-20 10:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9321a1091eb1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]186` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:24` | `cowrie.session.connect` |
| `2026-06-20 10:40:24` | `cowrie.client.version` |
| `2026-06-20 10:40:24` | `cowrie.client.kex` |
| `2026-06-20 10:40:27` | `cowrie.login.success` |
| `2026-06-20 10:40:28` | `cowrie.session.params` |
| `2026-06-20 10:40:28` | `cowrie.command.input` |
| `2026-06-20 10:40:29` | `cowrie.log.closed` |
| `2026-06-20 10:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]186` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad99695f82a9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:27` | `cowrie.session.connect` |
| `2026-06-20 10:40:28` | `cowrie.client.version` |
| `2026-06-20 10:40:28` | `cowrie.client.kex` |
| `2026-06-20 10:40:29` | `cowrie.login.success` |
| `2026-06-20 10:40:30` | `cowrie.session.params` |
| `2026-06-20 10:40:30` | `cowrie.command.input` |
| `2026-06-20 10:40:30` | `cowrie.log.closed` |
| `2026-06-20 10:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db80aaf171f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:34` | `cowrie.session.connect` |
| `2026-06-20 10:40:37` | `cowrie.client.version` |
| `2026-06-20 10:40:37` | `cowrie.client.kex` |
| `2026-06-20 10:40:49` | `cowrie.login.success` |
| `2026-06-20 10:40:57` | `cowrie.session.params` |
| `2026-06-20 10:40:57` | `cowrie.command.input` |
| `2026-06-20 10:41:00` | `cowrie.log.closed` |
| `2026-06-20 10:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a4362f0c19

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:34` | `cowrie.session.connect` |
| `2026-06-20 10:40:34` | `cowrie.client.version` |
| `2026-06-20 10:40:34` | `cowrie.client.kex` |
| `2026-06-20 10:40:35` | `cowrie.login.success` |
| `2026-06-20 10:40:37` | `cowrie.session.params` |
| `2026-06-20 10:40:37` | `cowrie.command.input` |
| `2026-06-20 10:40:37` | `cowrie.log.closed` |
| `2026-06-20 10:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f534f7ff543

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:40` | `cowrie.session.connect` |
| `2026-06-20 10:40:40` | `cowrie.client.version` |
| `2026-06-20 10:40:40` | `cowrie.client.kex` |
| `2026-06-20 10:40:41` | `cowrie.login.success` |
| `2026-06-20 10:40:42` | `cowrie.session.params` |
| `2026-06-20 10:40:42` | `cowrie.command.input` |
| `2026-06-20 10:40:42` | `cowrie.log.closed` |
| `2026-06-20 10:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0d93fb91b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:46` | `cowrie.session.connect` |
| `2026-06-20 10:40:46` | `cowrie.client.version` |
| `2026-06-20 10:40:46` | `cowrie.client.kex` |
| `2026-06-20 10:40:48` | `cowrie.login.success` |
| `2026-06-20 10:40:49` | `cowrie.session.params` |
| `2026-06-20 10:40:49` | `cowrie.command.input` |
| `2026-06-20 10:40:49` | `cowrie.log.closed` |
| `2026-06-20 10:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb10c896c6a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:52` | `cowrie.session.connect` |
| `2026-06-20 10:40:53` | `cowrie.client.version` |
| `2026-06-20 10:40:53` | `cowrie.client.kex` |
| `2026-06-20 10:40:53` | `cowrie.login.success` |
| `2026-06-20 10:40:55` | `cowrie.session.params` |
| `2026-06-20 10:40:55` | `cowrie.command.input` |
| `2026-06-20 10:40:55` | `cowrie.log.closed` |
| `2026-06-20 10:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d4a776cee9e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:40 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:40:58` | `cowrie.session.connect` |
| `2026-06-20 10:40:59` | `cowrie.client.version` |
| `2026-06-20 10:40:59` | `cowrie.client.kex` |
| `2026-06-20 10:40:59` | `cowrie.login.success` |
| `2026-06-20 10:41:01` | `cowrie.session.params` |
| `2026-06-20 10:41:01` | `cowrie.command.input` |
| `2026-06-20 10:41:01` | `cowrie.log.closed` |
| `2026-06-20 10:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bcce563f33e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:41 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:41:04` | `cowrie.session.connect` |
| `2026-06-20 10:41:04` | `cowrie.client.version` |
| `2026-06-20 10:41:04` | `cowrie.client.kex` |
| `2026-06-20 10:41:06` | `cowrie.login.success` |
| `2026-06-20 10:41:07` | `cowrie.session.params` |
| `2026-06-20 10:41:07` | `cowrie.command.input` |
| `2026-06-20 10:41:07` | `cowrie.log.closed` |
| `2026-06-20 10:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0109b480e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:41 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:41:11` | `cowrie.session.connect` |
| `2026-06-20 10:41:11` | `cowrie.client.version` |
| `2026-06-20 10:41:11` | `cowrie.client.kex` |
| `2026-06-20 10:41:11` | `cowrie.login.success` |
| `2026-06-20 10:41:12` | `cowrie.session.params` |
| `2026-06-20 10:41:12` | `cowrie.command.input` |
| `2026-06-20 10:41:12` | `cowrie.log.closed` |
| `2026-06-20 10:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869658ce0213

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:41 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:41:17` | `cowrie.session.connect` |
| `2026-06-20 10:41:17` | `cowrie.client.version` |
| `2026-06-20 10:41:17` | `cowrie.client.kex` |
| `2026-06-20 10:41:17` | `cowrie.login.success` |
| `2026-06-20 10:41:18` | `cowrie.session.params` |
| `2026-06-20 10:41:18` | `cowrie.command.input` |
| `2026-06-20 10:41:19` | `cowrie.log.closed` |
| `2026-06-20 10:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3962c5f393

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:41 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:41:22` | `cowrie.session.connect` |
| `2026-06-20 10:41:22` | `cowrie.client.version` |
| `2026-06-20 10:41:22` | `cowrie.client.kex` |
| `2026-06-20 10:41:24` | `cowrie.login.success` |
| `2026-06-20 10:41:25` | `cowrie.session.params` |
| `2026-06-20 10:41:25` | `cowrie.command.input` |
| `2026-06-20 10:41:25` | `cowrie.log.closed` |
| `2026-06-20 10:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7461dd01128

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:41 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:41:28` | `cowrie.session.connect` |
| `2026-06-20 10:41:28` | `cowrie.client.version` |
| `2026-06-20 10:41:28` | `cowrie.client.kex` |
| `2026-06-20 10:41:30` | `cowrie.login.success` |
| `2026-06-20 10:41:32` | `cowrie.session.params` |
| `2026-06-20 10:41:32` | `cowrie.command.input` |
| `2026-06-20 10:41:33` | `cowrie.log.closed` |
| `2026-06-20 10:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7099aac0aab9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:41 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:41:34` | `cowrie.session.connect` |
| `2026-06-20 10:41:34` | `cowrie.client.version` |
| `2026-06-20 10:41:34` | `cowrie.client.kex` |
| `2026-06-20 10:41:36` | `cowrie.login.success` |
| `2026-06-20 10:41:38` | `cowrie.session.params` |
| `2026-06-20 10:41:38` | `cowrie.command.input` |
| `2026-06-20 10:41:38` | `cowrie.log.closed` |
| `2026-06-20 10:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3679c294a8ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:41 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:41:41` | `cowrie.session.connect` |
| `2026-06-20 10:41:41` | `cowrie.client.version` |
| `2026-06-20 10:41:41` | `cowrie.client.kex` |
| `2026-06-20 10:41:42` | `cowrie.login.success` |
| `2026-06-20 10:41:43` | `cowrie.session.params` |
| `2026-06-20 10:41:43` | `cowrie.command.input` |
| `2026-06-20 10:41:43` | `cowrie.log.closed` |
| `2026-06-20 10:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24d9ccde934d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:41 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:41:47` | `cowrie.session.connect` |
| `2026-06-20 10:41:47` | `cowrie.client.version` |
| `2026-06-20 10:41:47` | `cowrie.client.kex` |
| `2026-06-20 10:41:48` | `cowrie.login.success` |
| `2026-06-20 10:41:49` | `cowrie.session.params` |
| `2026-06-20 10:41:49` | `cowrie.command.input` |
| `2026-06-20 10:41:50` | `cowrie.log.closed` |
| `2026-06-20 10:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50b9c8cf05b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:41 |
| **Last Seen** | 2026-06-20 10:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:41:52` | `cowrie.session.connect` |
| `2026-06-20 10:41:52` | `cowrie.client.version` |
| `2026-06-20 10:41:52` | `cowrie.client.kex` |
| `2026-06-20 10:41:54` | `cowrie.login.success` |
| `2026-06-20 10:41:56` | `cowrie.session.params` |
| `2026-06-20 10:41:56` | `cowrie.command.input` |
| `2026-06-20 10:41:56` | `cowrie.log.closed` |
| `2026-06-20 10:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89d370ebce40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:41 |
| **Last Seen** | 2026-06-20 10:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:41:58` | `cowrie.session.connect` |
| `2026-06-20 10:41:59` | `cowrie.client.version` |
| `2026-06-20 10:41:59` | `cowrie.client.kex` |
| `2026-06-20 10:42:00` | `cowrie.login.success` |
| `2026-06-20 10:42:01` | `cowrie.session.params` |
| `2026-06-20 10:42:01` | `cowrie.command.input` |
| `2026-06-20 10:42:02` | `cowrie.log.closed` |
| `2026-06-20 10:42:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91fb8bfee478

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:42 |
| **Last Seen** | 2026-06-20 10:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:42:05` | `cowrie.session.connect` |
| `2026-06-20 10:42:05` | `cowrie.client.version` |
| `2026-06-20 10:42:05` | `cowrie.client.kex` |
| `2026-06-20 10:42:06` | `cowrie.login.success` |
| `2026-06-20 10:42:08` | `cowrie.session.params` |
| `2026-06-20 10:42:08` | `cowrie.command.input` |
| `2026-06-20 10:42:08` | `cowrie.log.closed` |
| `2026-06-20 10:42:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-609078c389da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:42 |
| **Last Seen** | 2026-06-20 10:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:42:10` | `cowrie.session.connect` |
| `2026-06-20 10:42:11` | `cowrie.client.version` |
| `2026-06-20 10:42:11` | `cowrie.client.kex` |
| `2026-06-20 10:42:12` | `cowrie.login.success` |
| `2026-06-20 10:42:13` | `cowrie.session.params` |
| `2026-06-20 10:42:13` | `cowrie.command.input` |
| `2026-06-20 10:42:14` | `cowrie.log.closed` |
| `2026-06-20 10:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88fbb62d6089

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:42 |
| **Last Seen** | 2026-06-20 10:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:42:16` | `cowrie.session.connect` |
| `2026-06-20 10:42:17` | `cowrie.client.version` |
| `2026-06-20 10:42:17` | `cowrie.client.kex` |
| `2026-06-20 10:42:18` | `cowrie.login.success` |
| `2026-06-20 10:42:19` | `cowrie.session.params` |
| `2026-06-20 10:42:19` | `cowrie.command.input` |
| `2026-06-20 10:42:20` | `cowrie.log.closed` |
| `2026-06-20 10:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40ac7b5d8f43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:42 |
| **Last Seen** | 2026-06-20 10:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:42:22` | `cowrie.session.connect` |
| `2026-06-20 10:42:23` | `cowrie.client.version` |
| `2026-06-20 10:42:23` | `cowrie.client.kex` |
| `2026-06-20 10:42:24` | `cowrie.login.success` |
| `2026-06-20 10:42:25` | `cowrie.session.params` |
| `2026-06-20 10:42:25` | `cowrie.command.input` |
| `2026-06-20 10:42:25` | `cowrie.log.closed` |
| `2026-06-20 10:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee9be80682b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:42 |
| **Last Seen** | 2026-06-20 10:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:42:29` | `cowrie.session.connect` |
| `2026-06-20 10:42:29` | `cowrie.client.version` |
| `2026-06-20 10:42:29` | `cowrie.client.kex` |
| `2026-06-20 10:42:30` | `cowrie.login.success` |
| `2026-06-20 10:42:31` | `cowrie.session.params` |
| `2026-06-20 10:42:31` | `cowrie.command.input` |
| `2026-06-20 10:42:31` | `cowrie.log.closed` |
| `2026-06-20 10:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98211eead0d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:42 |
| **Last Seen** | 2026-06-20 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:42:35` | `cowrie.session.connect` |
| `2026-06-20 10:42:35` | `cowrie.client.version` |
| `2026-06-20 10:42:35` | `cowrie.client.kex` |
| `2026-06-20 10:42:36` | `cowrie.login.success` |
| `2026-06-20 10:42:36` | `cowrie.session.params` |
| `2026-06-20 10:42:36` | `cowrie.command.input` |
| `2026-06-20 10:42:37` | `cowrie.log.closed` |
| `2026-06-20 10:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5715ab47777

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:42 |
| **Last Seen** | 2026-06-20 10:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:42:41` | `cowrie.session.connect` |
| `2026-06-20 10:42:41` | `cowrie.client.version` |
| `2026-06-20 10:42:41` | `cowrie.client.kex` |
| `2026-06-20 10:42:43` | `cowrie.login.success` |
| `2026-06-20 10:42:44` | `cowrie.session.params` |
| `2026-06-20 10:42:44` | `cowrie.command.input` |
| `2026-06-20 10:42:44` | `cowrie.log.closed` |
| `2026-06-20 10:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d47e99deec0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:42 |
| **Last Seen** | 2026-06-20 10:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:42:47` | `cowrie.session.connect` |
| `2026-06-20 10:42:47` | `cowrie.client.version` |
| `2026-06-20 10:42:47` | `cowrie.client.kex` |
| `2026-06-20 10:42:49` | `cowrie.login.success` |
| `2026-06-20 10:42:50` | `cowrie.session.params` |
| `2026-06-20 10:42:50` | `cowrie.command.input` |
| `2026-06-20 10:42:51` | `cowrie.log.closed` |
| `2026-06-20 10:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a8ac39ed8ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:42 |
| **Last Seen** | 2026-06-20 10:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:42:52` | `cowrie.session.connect` |
| `2026-06-20 10:42:53` | `cowrie.client.version` |
| `2026-06-20 10:42:53` | `cowrie.client.kex` |
| `2026-06-20 10:42:55` | `cowrie.login.success` |
| `2026-06-20 10:42:56` | `cowrie.session.params` |
| `2026-06-20 10:42:56` | `cowrie.command.input` |
| `2026-06-20 10:42:56` | `cowrie.log.closed` |
| `2026-06-20 10:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05777d9213a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:42 |
| **Last Seen** | 2026-06-20 10:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:42:59` | `cowrie.session.connect` |
| `2026-06-20 10:42:59` | `cowrie.client.version` |
| `2026-06-20 10:42:59` | `cowrie.client.kex` |
| `2026-06-20 10:43:00` | `cowrie.login.success` |
| `2026-06-20 10:43:01` | `cowrie.session.params` |
| `2026-06-20 10:43:01` | `cowrie.command.input` |
| `2026-06-20 10:43:02` | `cowrie.log.closed` |
| `2026-06-20 10:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27ea9fc86e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:43 |
| **Last Seen** | 2026-06-20 10:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:43:05` | `cowrie.session.connect` |
| `2026-06-20 10:43:05` | `cowrie.client.version` |
| `2026-06-20 10:43:05` | `cowrie.client.kex` |
| `2026-06-20 10:43:07` | `cowrie.login.success` |
| `2026-06-20 10:43:08` | `cowrie.session.params` |
| `2026-06-20 10:43:08` | `cowrie.command.input` |
| `2026-06-20 10:43:08` | `cowrie.log.closed` |
| `2026-06-20 10:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb50e44ab13

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:43 |
| **Last Seen** | 2026-06-20 10:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:43:11` | `cowrie.session.connect` |
| `2026-06-20 10:43:11` | `cowrie.client.version` |
| `2026-06-20 10:43:11` | `cowrie.client.kex` |
| `2026-06-20 10:43:13` | `cowrie.login.success` |
| `2026-06-20 10:43:14` | `cowrie.session.params` |
| `2026-06-20 10:43:14` | `cowrie.command.input` |
| `2026-06-20 10:43:15` | `cowrie.log.closed` |
| `2026-06-20 10:43:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7a6eb793e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:43 |
| **Last Seen** | 2026-06-20 10:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:43:17` | `cowrie.session.connect` |
| `2026-06-20 10:43:17` | `cowrie.client.version` |
| `2026-06-20 10:43:17` | `cowrie.client.kex` |
| `2026-06-20 10:43:20` | `cowrie.login.success` |
| `2026-06-20 10:43:22` | `cowrie.session.params` |
| `2026-06-20 10:43:22` | `cowrie.command.input` |
| `2026-06-20 10:43:22` | `cowrie.log.closed` |
| `2026-06-20 10:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3a7208cd59

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:43 |
| **Last Seen** | 2026-06-20 10:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:43:22` | `cowrie.session.connect` |
| `2026-06-20 10:43:23` | `cowrie.client.version` |
| `2026-06-20 10:43:23` | `cowrie.client.kex` |
| `2026-06-20 10:43:26` | `cowrie.login.success` |
| `2026-06-20 10:43:28` | `cowrie.session.params` |
| `2026-06-20 10:43:28` | `cowrie.command.input` |
| `2026-06-20 10:43:28` | `cowrie.log.closed` |
| `2026-06-20 10:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15d17f5a0401

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:43 |
| **Last Seen** | 2026-06-20 10:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:43:29` | `cowrie.session.connect` |
| `2026-06-20 10:43:29` | `cowrie.client.version` |
| `2026-06-20 10:43:29` | `cowrie.client.kex` |
| `2026-06-20 10:43:31` | `cowrie.login.success` |
| `2026-06-20 10:43:32` | `cowrie.session.params` |
| `2026-06-20 10:43:32` | `cowrie.command.input` |
| `2026-06-20 10:43:32` | `cowrie.log.closed` |
| `2026-06-20 10:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6658c90cff4c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:43 |
| **Last Seen** | 2026-06-20 10:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:43:36` | `cowrie.session.connect` |
| `2026-06-20 10:43:36` | `cowrie.client.version` |
| `2026-06-20 10:43:36` | `cowrie.client.kex` |
| `2026-06-20 10:43:37` | `cowrie.login.success` |
| `2026-06-20 10:43:38` | `cowrie.session.params` |
| `2026-06-20 10:43:38` | `cowrie.command.input` |
| `2026-06-20 10:43:39` | `cowrie.log.closed` |
| `2026-06-20 10:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f18431b250a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:43 |
| **Last Seen** | 2026-06-20 10:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:43:41` | `cowrie.session.connect` |
| `2026-06-20 10:43:42` | `cowrie.client.version` |
| `2026-06-20 10:43:42` | `cowrie.client.kex` |
| `2026-06-20 10:43:44` | `cowrie.login.success` |
| `2026-06-20 10:43:46` | `cowrie.session.params` |
| `2026-06-20 10:43:46` | `cowrie.command.input` |
| `2026-06-20 10:43:46` | `cowrie.log.closed` |
| `2026-06-20 10:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-254fb20adccf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:43 |
| **Last Seen** | 2026-06-20 10:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:43:47` | `cowrie.session.connect` |
| `2026-06-20 10:43:47` | `cowrie.client.version` |
| `2026-06-20 10:43:47` | `cowrie.client.kex` |
| `2026-06-20 10:43:51` | `cowrie.login.success` |
| `2026-06-20 10:43:53` | `cowrie.session.params` |
| `2026-06-20 10:43:53` | `cowrie.command.input` |
| `2026-06-20 10:43:53` | `cowrie.log.closed` |
| `2026-06-20 10:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b852a54567a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:43 |
| **Last Seen** | 2026-06-20 10:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:43:54` | `cowrie.session.connect` |
| `2026-06-20 10:43:54` | `cowrie.client.version` |
| `2026-06-20 10:43:54` | `cowrie.client.kex` |
| `2026-06-20 10:43:56` | `cowrie.login.success` |
| `2026-06-20 10:43:57` | `cowrie.session.params` |
| `2026-06-20 10:43:57` | `cowrie.command.input` |
| `2026-06-20 10:43:58` | `cowrie.log.closed` |
| `2026-06-20 10:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba8987871d02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:44 |
| **Last Seen** | 2026-06-20 10:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:44:00` | `cowrie.session.connect` |
| `2026-06-20 10:44:00` | `cowrie.client.version` |
| `2026-06-20 10:44:00` | `cowrie.client.kex` |
| `2026-06-20 10:44:04` | `cowrie.login.success` |
| `2026-06-20 10:44:05` | `cowrie.session.params` |
| `2026-06-20 10:44:05` | `cowrie.command.input` |
| `2026-06-20 10:44:06` | `cowrie.log.closed` |
| `2026-06-20 10:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0958aa35baf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:44 |
| **Last Seen** | 2026-06-20 10:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:44:07` | `cowrie.session.connect` |
| `2026-06-20 10:44:07` | `cowrie.client.version` |
| `2026-06-20 10:44:07` | `cowrie.client.kex` |
| `2026-06-20 10:44:08` | `cowrie.login.success` |
| `2026-06-20 10:44:09` | `cowrie.session.params` |
| `2026-06-20 10:44:09` | `cowrie.command.input` |
| `2026-06-20 10:44:09` | `cowrie.log.closed` |
| `2026-06-20 10:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccb68dfd37bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:44 |
| **Last Seen** | 2026-06-20 10:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:44:13` | `cowrie.session.connect` |
| `2026-06-20 10:44:13` | `cowrie.client.version` |
| `2026-06-20 10:44:13` | `cowrie.client.kex` |
| `2026-06-20 10:44:16` | `cowrie.login.success` |
| `2026-06-20 10:44:17` | `cowrie.session.params` |
| `2026-06-20 10:44:17` | `cowrie.command.input` |
| `2026-06-20 10:44:18` | `cowrie.log.closed` |
| `2026-06-20 10:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2046984f7f3d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:44 |
| **Last Seen** | 2026-06-20 10:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:44:19` | `cowrie.session.connect` |
| `2026-06-20 10:44:19` | `cowrie.client.version` |
| `2026-06-20 10:44:19` | `cowrie.client.kex` |
| `2026-06-20 10:44:21` | `cowrie.login.success` |
| `2026-06-20 10:44:22` | `cowrie.session.params` |
| `2026-06-20 10:44:22` | `cowrie.command.input` |
| `2026-06-20 10:44:22` | `cowrie.log.closed` |
| `2026-06-20 10:44:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b9a41eb9760

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:44 |
| **Last Seen** | 2026-06-20 10:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:44:26` | `cowrie.session.connect` |
| `2026-06-20 10:44:26` | `cowrie.client.version` |
| `2026-06-20 10:44:26` | `cowrie.client.kex` |
| `2026-06-20 10:44:26` | `cowrie.login.success` |
| `2026-06-20 10:44:28` | `cowrie.session.params` |
| `2026-06-20 10:44:28` | `cowrie.command.input` |
| `2026-06-20 10:44:28` | `cowrie.log.closed` |
| `2026-06-20 10:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb63c359d378

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:44 |
| **Last Seen** | 2026-06-20 10:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:44:32` | `cowrie.session.connect` |
| `2026-06-20 10:44:32` | `cowrie.client.version` |
| `2026-06-20 10:44:32` | `cowrie.client.kex` |
| `2026-06-20 10:44:33` | `cowrie.login.success` |
| `2026-06-20 10:44:34` | `cowrie.session.params` |
| `2026-06-20 10:44:34` | `cowrie.command.input` |
| `2026-06-20 10:44:34` | `cowrie.log.closed` |
| `2026-06-20 10:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-287aa833dcd6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:44 |
| **Last Seen** | 2026-06-20 10:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:44:37` | `cowrie.session.connect` |
| `2026-06-20 10:44:37` | `cowrie.client.version` |
| `2026-06-20 10:44:37` | `cowrie.client.kex` |
| `2026-06-20 10:44:39` | `cowrie.login.success` |
| `2026-06-20 10:44:41` | `cowrie.session.params` |
| `2026-06-20 10:44:41` | `cowrie.command.input` |
| `2026-06-20 10:44:41` | `cowrie.log.closed` |
| `2026-06-20 10:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4bba00f8b48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:44 |
| **Last Seen** | 2026-06-20 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:44:44` | `cowrie.session.connect` |
| `2026-06-20 10:44:44` | `cowrie.client.version` |
| `2026-06-20 10:44:44` | `cowrie.client.kex` |
| `2026-06-20 10:44:45` | `cowrie.login.success` |
| `2026-06-20 10:44:46` | `cowrie.session.params` |
| `2026-06-20 10:44:46` | `cowrie.command.input` |
| `2026-06-20 10:44:46` | `cowrie.log.closed` |
| `2026-06-20 10:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e47f1c40fcc8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:44 |
| **Last Seen** | 2026-06-20 10:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:44:50` | `cowrie.session.connect` |
| `2026-06-20 10:44:50` | `cowrie.client.version` |
| `2026-06-20 10:44:50` | `cowrie.client.kex` |
| `2026-06-20 10:44:51` | `cowrie.login.success` |
| `2026-06-20 10:44:52` | `cowrie.session.params` |
| `2026-06-20 10:44:52` | `cowrie.command.input` |
| `2026-06-20 10:44:52` | `cowrie.log.closed` |
| `2026-06-20 10:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ae20ecf9e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:44 |
| **Last Seen** | 2026-06-20 10:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:44:56` | `cowrie.session.connect` |
| `2026-06-20 10:44:56` | `cowrie.client.version` |
| `2026-06-20 10:44:56` | `cowrie.client.kex` |
| `2026-06-20 10:44:58` | `cowrie.login.success` |
| `2026-06-20 10:44:59` | `cowrie.session.params` |
| `2026-06-20 10:44:59` | `cowrie.command.input` |
| `2026-06-20 10:44:59` | `cowrie.log.closed` |
| `2026-06-20 10:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a30ec9b16ed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:02` | `cowrie.session.connect` |
| `2026-06-20 10:45:02` | `cowrie.client.version` |
| `2026-06-20 10:45:03` | `cowrie.client.kex` |
| `2026-06-20 10:45:03` | `cowrie.login.success` |
| `2026-06-20 10:45:04` | `cowrie.session.params` |
| `2026-06-20 10:45:04` | `cowrie.command.input` |
| `2026-06-20 10:45:04` | `cowrie.log.closed` |
| `2026-06-20 10:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8a46166f4d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:08` | `cowrie.session.connect` |
| `2026-06-20 10:45:08` | `cowrie.client.version` |
| `2026-06-20 10:45:08` | `cowrie.client.kex` |
| `2026-06-20 10:45:10` | `cowrie.login.success` |
| `2026-06-20 10:45:11` | `cowrie.session.params` |
| `2026-06-20 10:45:11` | `cowrie.command.input` |
| `2026-06-20 10:45:11` | `cowrie.log.closed` |
| `2026-06-20 10:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6521c95669

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:14` | `cowrie.session.connect` |
| `2026-06-20 10:45:14` | `cowrie.client.version` |
| `2026-06-20 10:45:14` | `cowrie.client.kex` |
| `2026-06-20 10:45:15` | `cowrie.login.success` |
| `2026-06-20 10:45:17` | `cowrie.session.params` |
| `2026-06-20 10:45:17` | `cowrie.command.input` |
| `2026-06-20 10:45:17` | `cowrie.log.closed` |
| `2026-06-20 10:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb39f75e2e57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:20` | `cowrie.session.connect` |
| `2026-06-20 10:45:20` | `cowrie.client.version` |
| `2026-06-20 10:45:20` | `cowrie.client.kex` |
| `2026-06-20 10:45:22` | `cowrie.login.success` |
| `2026-06-20 10:45:23` | `cowrie.session.params` |
| `2026-06-20 10:45:23` | `cowrie.command.input` |
| `2026-06-20 10:45:23` | `cowrie.log.closed` |
| `2026-06-20 10:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae0c2f5ed4a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:27` | `cowrie.session.connect` |
| `2026-06-20 10:45:27` | `cowrie.client.version` |
| `2026-06-20 10:45:27` | `cowrie.client.kex` |
| `2026-06-20 10:45:28` | `cowrie.login.success` |
| `2026-06-20 10:45:29` | `cowrie.session.params` |
| `2026-06-20 10:45:29` | `cowrie.command.input` |
| `2026-06-20 10:45:29` | `cowrie.log.closed` |
| `2026-06-20 10:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-520ee02fc7e8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]186` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:27` | `cowrie.session.connect` |
| `2026-06-20 10:45:27` | `cowrie.client.version` |
| `2026-06-20 10:45:27` | `cowrie.client.kex` |
| `2026-06-20 10:45:29` | `cowrie.login.success` |
| `2026-06-20 10:45:30` | `cowrie.session.params` |
| `2026-06-20 10:45:30` | `cowrie.command.input` |
| `2026-06-20 10:45:30` | `cowrie.log.closed` |
| `2026-06-20 10:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]186` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d27034f662

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:33` | `cowrie.session.connect` |
| `2026-06-20 10:45:33` | `cowrie.client.version` |
| `2026-06-20 10:45:33` | `cowrie.client.kex` |
| `2026-06-20 10:45:33` | `cowrie.login.success` |
| `2026-06-20 10:45:35` | `cowrie.session.params` |
| `2026-06-20 10:45:35` | `cowrie.command.input` |
| `2026-06-20 10:45:35` | `cowrie.log.closed` |
| `2026-06-20 10:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-295f6f238af5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:38` | `cowrie.session.connect` |
| `2026-06-20 10:45:39` | `cowrie.client.version` |
| `2026-06-20 10:45:39` | `cowrie.client.kex` |
| `2026-06-20 10:45:40` | `cowrie.login.success` |
| `2026-06-20 10:45:42` | `cowrie.session.params` |
| `2026-06-20 10:45:42` | `cowrie.command.input` |
| `2026-06-20 10:45:42` | `cowrie.log.closed` |
| `2026-06-20 10:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1451f2e8c995

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:44` | `cowrie.session.connect` |
| `2026-06-20 10:45:45` | `cowrie.client.version` |
| `2026-06-20 10:45:45` | `cowrie.client.kex` |
| `2026-06-20 10:45:46` | `cowrie.login.success` |
| `2026-06-20 10:45:47` | `cowrie.session.params` |
| `2026-06-20 10:45:47` | `cowrie.command.input` |
| `2026-06-20 10:45:48` | `cowrie.log.closed` |
| `2026-06-20 10:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-455c1de672d6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:51` | `cowrie.session.connect` |
| `2026-06-20 10:45:51` | `cowrie.client.version` |
| `2026-06-20 10:45:51` | `cowrie.client.kex` |
| `2026-06-20 10:45:52` | `cowrie.login.success` |
| `2026-06-20 10:45:54` | `cowrie.session.params` |
| `2026-06-20 10:45:54` | `cowrie.command.input` |
| `2026-06-20 10:45:55` | `cowrie.log.closed` |
| `2026-06-20 10:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f82f20c4e61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:45 |
| **Last Seen** | 2026-06-20 10:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:45:56` | `cowrie.session.connect` |
| `2026-06-20 10:45:57` | `cowrie.client.version` |
| `2026-06-20 10:45:57` | `cowrie.client.kex` |
| `2026-06-20 10:45:59` | `cowrie.login.success` |
| `2026-06-20 10:46:01` | `cowrie.session.params` |
| `2026-06-20 10:46:01` | `cowrie.command.input` |
| `2026-06-20 10:46:02` | `cowrie.log.closed` |
| `2026-06-20 10:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d4ab819910

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:46 |
| **Last Seen** | 2026-06-20 10:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:46:02` | `cowrie.session.connect` |
| `2026-06-20 10:46:03` | `cowrie.client.version` |
| `2026-06-20 10:46:03` | `cowrie.client.kex` |
| `2026-06-20 10:46:06` | `cowrie.login.success` |
| `2026-06-20 10:46:07` | `cowrie.session.params` |
| `2026-06-20 10:46:07` | `cowrie.command.input` |
| `2026-06-20 10:46:08` | `cowrie.log.closed` |
| `2026-06-20 10:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3cf4a3b9224

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:46 |
| **Last Seen** | 2026-06-20 10:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:46:09` | `cowrie.session.connect` |
| `2026-06-20 10:46:09` | `cowrie.client.version` |
| `2026-06-20 10:46:09` | `cowrie.client.kex` |
| `2026-06-20 10:46:11` | `cowrie.login.success` |
| `2026-06-20 10:46:12` | `cowrie.session.params` |
| `2026-06-20 10:46:12` | `cowrie.command.input` |
| `2026-06-20 10:46:13` | `cowrie.log.closed` |
| `2026-06-20 10:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d920b45e42e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:46 |
| **Last Seen** | 2026-06-20 10:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:46:15` | `cowrie.session.connect` |
| `2026-06-20 10:46:15` | `cowrie.client.version` |
| `2026-06-20 10:46:15` | `cowrie.client.kex` |
| `2026-06-20 10:46:17` | `cowrie.login.success` |
| `2026-06-20 10:46:18` | `cowrie.session.params` |
| `2026-06-20 10:46:18` | `cowrie.command.input` |
| `2026-06-20 10:46:18` | `cowrie.log.closed` |
| `2026-06-20 10:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a9a3413ec4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:46 |
| **Last Seen** | 2026-06-20 10:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:46:21` | `cowrie.session.connect` |
| `2026-06-20 10:46:21` | `cowrie.client.version` |
| `2026-06-20 10:46:21` | `cowrie.client.kex` |
| `2026-06-20 10:46:23` | `cowrie.login.success` |
| `2026-06-20 10:46:24` | `cowrie.session.params` |
| `2026-06-20 10:46:24` | `cowrie.command.input` |
| `2026-06-20 10:46:24` | `cowrie.log.closed` |
| `2026-06-20 10:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7402c8e7f72

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:46 |
| **Last Seen** | 2026-06-20 10:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:46:27` | `cowrie.session.connect` |
| `2026-06-20 10:46:28` | `cowrie.client.version` |
| `2026-06-20 10:46:28` | `cowrie.client.kex` |
| `2026-06-20 10:46:29` | `cowrie.login.success` |
| `2026-06-20 10:46:30` | `cowrie.session.params` |
| `2026-06-20 10:46:30` | `cowrie.command.input` |
| `2026-06-20 10:46:31` | `cowrie.log.closed` |
| `2026-06-20 10:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14d00c79473d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:46 |
| **Last Seen** | 2026-06-20 10:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:46:33` | `cowrie.session.connect` |
| `2026-06-20 10:46:34` | `cowrie.client.version` |
| `2026-06-20 10:46:34` | `cowrie.client.kex` |
| `2026-06-20 10:46:34` | `cowrie.login.success` |
| `2026-06-20 10:46:35` | `cowrie.session.params` |
| `2026-06-20 10:46:35` | `cowrie.command.input` |
| `2026-06-20 10:46:35` | `cowrie.log.closed` |
| `2026-06-20 10:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7a4fa999de1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:46 |
| **Last Seen** | 2026-06-20 10:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:46:39` | `cowrie.session.connect` |
| `2026-06-20 10:46:39` | `cowrie.client.version` |
| `2026-06-20 10:46:39` | `cowrie.client.kex` |
| `2026-06-20 10:46:41` | `cowrie.login.success` |
| `2026-06-20 10:46:42` | `cowrie.session.params` |
| `2026-06-20 10:46:42` | `cowrie.command.input` |
| `2026-06-20 10:46:42` | `cowrie.log.closed` |
| `2026-06-20 10:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89cae09c75e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:46 |
| **Last Seen** | 2026-06-20 10:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:46:45` | `cowrie.session.connect` |
| `2026-06-20 10:46:46` | `cowrie.client.version` |
| `2026-06-20 10:46:46` | `cowrie.client.kex` |
| `2026-06-20 10:46:47` | `cowrie.login.success` |
| `2026-06-20 10:46:48` | `cowrie.session.params` |
| `2026-06-20 10:46:48` | `cowrie.command.input` |
| `2026-06-20 10:46:49` | `cowrie.log.closed` |
| `2026-06-20 10:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed8c1577d68

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:46 |
| **Last Seen** | 2026-06-20 10:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:46:51` | `cowrie.session.connect` |
| `2026-06-20 10:46:52` | `cowrie.client.version` |
| `2026-06-20 10:46:52` | `cowrie.client.kex` |
| `2026-06-20 10:46:53` | `cowrie.login.success` |
| `2026-06-20 10:46:54` | `cowrie.session.params` |
| `2026-06-20 10:46:54` | `cowrie.command.input` |
| `2026-06-20 10:46:54` | `cowrie.log.closed` |
| `2026-06-20 10:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa0de0b9d16

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:46 |
| **Last Seen** | 2026-06-20 10:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:46:57` | `cowrie.session.connect` |
| `2026-06-20 10:46:57` | `cowrie.client.version` |
| `2026-06-20 10:46:57` | `cowrie.client.kex` |
| `2026-06-20 10:46:59` | `cowrie.login.success` |
| `2026-06-20 10:47:01` | `cowrie.session.params` |
| `2026-06-20 10:47:01` | `cowrie.command.input` |
| `2026-06-20 10:47:01` | `cowrie.log.closed` |
| `2026-06-20 10:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76be2e5adc6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:47 |
| **Last Seen** | 2026-06-20 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:47:04` | `cowrie.session.connect` |
| `2026-06-20 10:47:04` | `cowrie.client.version` |
| `2026-06-20 10:47:04` | `cowrie.client.kex` |
| `2026-06-20 10:47:04` | `cowrie.login.success` |
| `2026-06-20 10:47:05` | `cowrie.session.params` |
| `2026-06-20 10:47:05` | `cowrie.command.input` |
| `2026-06-20 10:47:05` | `cowrie.log.closed` |
| `2026-06-20 10:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a7d27a7731

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:47 |
| **Last Seen** | 2026-06-20 10:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:47:09` | `cowrie.session.connect` |
| `2026-06-20 10:47:09` | `cowrie.client.version` |
| `2026-06-20 10:47:09` | `cowrie.client.kex` |
| `2026-06-20 10:47:11` | `cowrie.login.success` |
| `2026-06-20 10:47:12` | `cowrie.session.params` |
| `2026-06-20 10:47:12` | `cowrie.command.input` |
| `2026-06-20 10:47:13` | `cowrie.log.closed` |
| `2026-06-20 10:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9310161b9910

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:47 |
| **Last Seen** | 2026-06-20 10:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:47:15` | `cowrie.session.connect` |
| `2026-06-20 10:47:15` | `cowrie.client.version` |
| `2026-06-20 10:47:15` | `cowrie.client.kex` |
| `2026-06-20 10:47:17` | `cowrie.login.success` |
| `2026-06-20 10:47:18` | `cowrie.session.params` |
| `2026-06-20 10:47:18` | `cowrie.command.input` |
| `2026-06-20 10:47:19` | `cowrie.log.closed` |
| `2026-06-20 10:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df500ef12987

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:47 |
| **Last Seen** | 2026-06-20 10:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:47:21` | `cowrie.session.connect` |
| `2026-06-20 10:47:21` | `cowrie.client.version` |
| `2026-06-20 10:47:21` | `cowrie.client.kex` |
| `2026-06-20 10:47:24` | `cowrie.login.success` |
| `2026-06-20 10:47:25` | `cowrie.session.params` |
| `2026-06-20 10:47:25` | `cowrie.command.input` |
| `2026-06-20 10:47:26` | `cowrie.log.closed` |
| `2026-06-20 10:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7881e477c2d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:47 |
| **Last Seen** | 2026-06-20 10:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:47:27` | `cowrie.session.connect` |
| `2026-06-20 10:47:27` | `cowrie.client.version` |
| `2026-06-20 10:47:27` | `cowrie.client.kex` |
| `2026-06-20 10:47:30` | `cowrie.login.success` |
| `2026-06-20 10:47:31` | `cowrie.session.params` |
| `2026-06-20 10:47:31` | `cowrie.command.input` |
| `2026-06-20 10:47:32` | `cowrie.log.closed` |
| `2026-06-20 10:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8403cef3c085

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:47 |
| **Last Seen** | 2026-06-20 10:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:47:34` | `cowrie.session.connect` |
| `2026-06-20 10:47:34` | `cowrie.client.version` |
| `2026-06-20 10:47:34` | `cowrie.client.kex` |
| `2026-06-20 10:47:35` | `cowrie.login.success` |
| `2026-06-20 10:47:36` | `cowrie.session.params` |
| `2026-06-20 10:47:36` | `cowrie.command.input` |
| `2026-06-20 10:47:36` | `cowrie.log.closed` |
| `2026-06-20 10:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73ed09ea8941

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:47 |
| **Last Seen** | 2026-06-20 10:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:47:40` | `cowrie.session.connect` |
| `2026-06-20 10:47:40` | `cowrie.client.version` |
| `2026-06-20 10:47:40` | `cowrie.client.kex` |
| `2026-06-20 10:47:41` | `cowrie.login.success` |
| `2026-06-20 10:47:41` | `cowrie.session.params` |
| `2026-06-20 10:47:41` | `cowrie.command.input` |
| `2026-06-20 10:47:42` | `cowrie.log.closed` |
| `2026-06-20 10:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c68d5ce9632

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:47 |
| **Last Seen** | 2026-06-20 10:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:47:46` | `cowrie.session.connect` |
| `2026-06-20 10:47:46` | `cowrie.client.version` |
| `2026-06-20 10:47:46` | `cowrie.client.kex` |
| `2026-06-20 10:47:48` | `cowrie.login.success` |
| `2026-06-20 10:47:49` | `cowrie.session.params` |
| `2026-06-20 10:47:49` | `cowrie.command.input` |
| `2026-06-20 10:47:50` | `cowrie.log.closed` |
| `2026-06-20 10:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cbaabadbd96

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:47 |
| **Last Seen** | 2026-06-20 10:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:47:51` | `cowrie.session.connect` |
| `2026-06-20 10:47:52` | `cowrie.client.version` |
| `2026-06-20 10:47:52` | `cowrie.client.kex` |
| `2026-06-20 10:47:53` | `cowrie.login.success` |
| `2026-06-20 10:47:55` | `cowrie.session.params` |
| `2026-06-20 10:47:55` | `cowrie.command.input` |
| `2026-06-20 10:47:55` | `cowrie.log.closed` |
| `2026-06-20 10:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee790b34ad78

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:47 |
| **Last Seen** | 2026-06-20 10:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:47:57` | `cowrie.session.connect` |
| `2026-06-20 10:47:58` | `cowrie.client.version` |
| `2026-06-20 10:47:58` | `cowrie.client.kex` |
| `2026-06-20 10:48:00` | `cowrie.login.success` |
| `2026-06-20 10:48:02` | `cowrie.session.params` |
| `2026-06-20 10:48:02` | `cowrie.command.input` |
| `2026-06-20 10:48:03` | `cowrie.log.closed` |
| `2026-06-20 10:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c451b0072ec5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:48 |
| **Last Seen** | 2026-06-20 10:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:48:03` | `cowrie.session.connect` |
| `2026-06-20 10:48:04` | `cowrie.client.version` |
| `2026-06-20 10:48:04` | `cowrie.client.kex` |
| `2026-06-20 10:48:05` | `cowrie.login.success` |
| `2026-06-20 10:48:07` | `cowrie.session.params` |
| `2026-06-20 10:48:07` | `cowrie.command.input` |
| `2026-06-20 10:48:07` | `cowrie.log.closed` |
| `2026-06-20 10:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa26036a182

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:48 |
| **Last Seen** | 2026-06-20 10:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:48:10` | `cowrie.session.connect` |
| `2026-06-20 10:48:10` | `cowrie.client.version` |
| `2026-06-20 10:48:10` | `cowrie.client.kex` |
| `2026-06-20 10:48:12` | `cowrie.login.success` |
| `2026-06-20 10:48:13` | `cowrie.session.params` |
| `2026-06-20 10:48:13` | `cowrie.command.input` |
| `2026-06-20 10:48:13` | `cowrie.log.closed` |
| `2026-06-20 10:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61ef96b5bfde

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:48 |
| **Last Seen** | 2026-06-20 10:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:48:16` | `cowrie.session.connect` |
| `2026-06-20 10:48:16` | `cowrie.client.version` |
| `2026-06-20 10:48:16` | `cowrie.client.kex` |
| `2026-06-20 10:48:18` | `cowrie.login.success` |
| `2026-06-20 10:48:20` | `cowrie.session.params` |
| `2026-06-20 10:48:20` | `cowrie.command.input` |
| `2026-06-20 10:48:20` | `cowrie.log.closed` |
| `2026-06-20 10:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ec892888b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:48 |
| **Last Seen** | 2026-06-20 10:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:48:22` | `cowrie.session.connect` |
| `2026-06-20 10:48:22` | `cowrie.client.version` |
| `2026-06-20 10:48:22` | `cowrie.client.kex` |
| `2026-06-20 10:48:24` | `cowrie.login.success` |
| `2026-06-20 10:48:26` | `cowrie.session.params` |
| `2026-06-20 10:48:26` | `cowrie.command.input` |
| `2026-06-20 10:48:26` | `cowrie.log.closed` |
| `2026-06-20 10:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd58a4d5687

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:48 |
| **Last Seen** | 2026-06-20 10:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:48:28` | `cowrie.session.connect` |
| `2026-06-20 10:48:28` | `cowrie.client.version` |
| `2026-06-20 10:48:29` | `cowrie.client.kex` |
| `2026-06-20 10:48:30` | `cowrie.login.success` |
| `2026-06-20 10:48:31` | `cowrie.session.params` |
| `2026-06-20 10:48:31` | `cowrie.command.input` |
| `2026-06-20 10:48:31` | `cowrie.log.closed` |
| `2026-06-20 10:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75527d2b8d0b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:48 |
| **Last Seen** | 2026-06-20 10:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:48:35` | `cowrie.session.connect` |
| `2026-06-20 10:48:35` | `cowrie.client.version` |
| `2026-06-20 10:48:35` | `cowrie.client.kex` |
| `2026-06-20 10:48:35` | `cowrie.login.success` |
| `2026-06-20 10:48:36` | `cowrie.session.params` |
| `2026-06-20 10:48:36` | `cowrie.command.input` |
| `2026-06-20 10:48:36` | `cowrie.log.closed` |
| `2026-06-20 10:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c7c1c9ce92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:48 |
| **Last Seen** | 2026-06-20 10:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:48:40` | `cowrie.session.connect` |
| `2026-06-20 10:48:41` | `cowrie.client.version` |
| `2026-06-20 10:48:41` | `cowrie.client.kex` |
| `2026-06-20 10:48:42` | `cowrie.login.success` |
| `2026-06-20 10:48:43` | `cowrie.session.params` |
| `2026-06-20 10:48:43` | `cowrie.command.input` |
| `2026-06-20 10:48:43` | `cowrie.log.closed` |
| `2026-06-20 10:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f3949d4ccc2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:48 |
| **Last Seen** | 2026-06-20 10:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:48:46` | `cowrie.session.connect` |
| `2026-06-20 10:48:46` | `cowrie.client.version` |
| `2026-06-20 10:48:46` | `cowrie.client.kex` |
| `2026-06-20 10:48:48` | `cowrie.login.success` |
| `2026-06-20 10:48:50` | `cowrie.session.params` |
| `2026-06-20 10:48:50` | `cowrie.command.input` |
| `2026-06-20 10:48:50` | `cowrie.log.closed` |
| `2026-06-20 10:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4187657d213

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:48 |
| **Last Seen** | 2026-06-20 10:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:48:52` | `cowrie.session.connect` |
| `2026-06-20 10:48:52` | `cowrie.client.version` |
| `2026-06-20 10:48:52` | `cowrie.client.kex` |
| `2026-06-20 10:48:55` | `cowrie.login.success` |
| `2026-06-20 10:48:56` | `cowrie.session.params` |
| `2026-06-20 10:48:56` | `cowrie.command.input` |
| `2026-06-20 10:48:56` | `cowrie.log.closed` |
| `2026-06-20 10:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e333639930c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:48 |
| **Last Seen** | 2026-06-20 10:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:48:58` | `cowrie.session.connect` |
| `2026-06-20 10:48:59` | `cowrie.client.version` |
| `2026-06-20 10:48:59` | `cowrie.client.kex` |
| `2026-06-20 10:49:01` | `cowrie.login.success` |
| `2026-06-20 10:49:02` | `cowrie.session.params` |
| `2026-06-20 10:49:02` | `cowrie.command.input` |
| `2026-06-20 10:49:03` | `cowrie.log.closed` |
| `2026-06-20 10:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46f643b058b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:49 |
| **Last Seen** | 2026-06-20 10:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:49:04` | `cowrie.session.connect` |
| `2026-06-20 10:49:05` | `cowrie.client.version` |
| `2026-06-20 10:49:05` | `cowrie.client.kex` |
| `2026-06-20 10:49:07` | `cowrie.login.success` |
| `2026-06-20 10:49:09` | `cowrie.session.params` |
| `2026-06-20 10:49:09` | `cowrie.command.input` |
| `2026-06-20 10:49:09` | `cowrie.log.closed` |
| `2026-06-20 10:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-111c3722ca9f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:49 |
| **Last Seen** | 2026-06-20 10:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:49:10` | `cowrie.session.connect` |
| `2026-06-20 10:49:11` | `cowrie.client.version` |
| `2026-06-20 10:49:11` | `cowrie.client.kex` |
| `2026-06-20 10:49:13` | `cowrie.login.success` |
| `2026-06-20 10:49:15` | `cowrie.session.params` |
| `2026-06-20 10:49:15` | `cowrie.command.input` |
| `2026-06-20 10:49:16` | `cowrie.log.closed` |
| `2026-06-20 10:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdf1e455106e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:49 |
| **Last Seen** | 2026-06-20 10:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:49:16` | `cowrie.session.connect` |
| `2026-06-20 10:49:17` | `cowrie.client.version` |
| `2026-06-20 10:49:17` | `cowrie.client.kex` |
| `2026-06-20 10:49:19` | `cowrie.login.success` |
| `2026-06-20 10:49:21` | `cowrie.session.params` |
| `2026-06-20 10:49:21` | `cowrie.command.input` |
| `2026-06-20 10:49:22` | `cowrie.log.closed` |
| `2026-06-20 10:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c7c24d5f62d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:49 |
| **Last Seen** | 2026-06-20 10:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:49:22` | `cowrie.session.connect` |
| `2026-06-20 10:49:22` | `cowrie.client.version` |
| `2026-06-20 10:49:22` | `cowrie.client.kex` |
| `2026-06-20 10:49:26` | `cowrie.login.success` |
| `2026-06-20 10:49:27` | `cowrie.session.params` |
| `2026-06-20 10:49:27` | `cowrie.command.input` |
| `2026-06-20 10:49:28` | `cowrie.log.closed` |
| `2026-06-20 10:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bf5ee7c0b17

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:49 |
| **Last Seen** | 2026-06-20 10:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:49:29` | `cowrie.session.connect` |
| `2026-06-20 10:49:29` | `cowrie.client.version` |
| `2026-06-20 10:49:29` | `cowrie.client.kex` |
| `2026-06-20 10:49:30` | `cowrie.login.success` |
| `2026-06-20 10:49:31` | `cowrie.session.params` |
| `2026-06-20 10:49:31` | `cowrie.command.input` |
| `2026-06-20 10:49:32` | `cowrie.log.closed` |
| `2026-06-20 10:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7a1179c366

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:49 |
| **Last Seen** | 2026-06-20 10:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:49:36` | `cowrie.session.connect` |
| `2026-06-20 10:49:36` | `cowrie.client.version` |
| `2026-06-20 10:49:36` | `cowrie.client.kex` |
| `2026-06-20 10:49:36` | `cowrie.login.success` |
| `2026-06-20 10:49:37` | `cowrie.session.params` |
| `2026-06-20 10:49:37` | `cowrie.command.input` |
| `2026-06-20 10:49:38` | `cowrie.log.closed` |
| `2026-06-20 10:49:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8faf3f774b02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:49 |
| **Last Seen** | 2026-06-20 10:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:49:42` | `cowrie.session.connect` |
| `2026-06-20 10:49:42` | `cowrie.client.version` |
| `2026-06-20 10:49:42` | `cowrie.client.kex` |
| `2026-06-20 10:49:43` | `cowrie.login.success` |
| `2026-06-20 10:49:44` | `cowrie.session.params` |
| `2026-06-20 10:49:44` | `cowrie.command.input` |
| `2026-06-20 10:49:44` | `cowrie.log.closed` |
| `2026-06-20 10:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6da853c07cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:49 |
| **Last Seen** | 2026-06-20 10:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:49:48` | `cowrie.session.connect` |
| `2026-06-20 10:49:48` | `cowrie.client.version` |
| `2026-06-20 10:49:48` | `cowrie.client.kex` |
| `2026-06-20 10:49:49` | `cowrie.login.success` |
| `2026-06-20 10:49:50` | `cowrie.session.params` |
| `2026-06-20 10:49:50` | `cowrie.command.input` |
| `2026-06-20 10:49:50` | `cowrie.log.closed` |
| `2026-06-20 10:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3593888e2b50

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:49 |
| **Last Seen** | 2026-06-20 10:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:49:54` | `cowrie.session.connect` |
| `2026-06-20 10:49:54` | `cowrie.client.version` |
| `2026-06-20 10:49:54` | `cowrie.client.kex` |
| `2026-06-20 10:49:55` | `cowrie.login.success` |
| `2026-06-20 10:49:57` | `cowrie.session.params` |
| `2026-06-20 10:49:57` | `cowrie.command.input` |
| `2026-06-20 10:49:57` | `cowrie.log.closed` |
| `2026-06-20 10:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b07833902f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:01` | `cowrie.session.connect` |
| `2026-06-20 10:50:01` | `cowrie.client.version` |
| `2026-06-20 10:50:01` | `cowrie.client.kex` |
| `2026-06-20 10:50:02` | `cowrie.login.success` |
| `2026-06-20 10:50:03` | `cowrie.session.params` |
| `2026-06-20 10:50:03` | `cowrie.command.input` |
| `2026-06-20 10:50:03` | `cowrie.log.closed` |
| `2026-06-20 10:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-309bf80bad46

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:07` | `cowrie.session.connect` |
| `2026-06-20 10:50:07` | `cowrie.client.version` |
| `2026-06-20 10:50:07` | `cowrie.client.kex` |
| `2026-06-20 10:50:08` | `cowrie.login.success` |
| `2026-06-20 10:50:09` | `cowrie.session.params` |
| `2026-06-20 10:50:09` | `cowrie.command.input` |
| `2026-06-20 10:50:09` | `cowrie.log.closed` |
| `2026-06-20 10:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-691369802277

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:14` | `cowrie.session.connect` |
| `2026-06-20 10:50:14` | `cowrie.client.version` |
| `2026-06-20 10:50:14` | `cowrie.client.kex` |
| `2026-06-20 10:50:15` | `cowrie.login.success` |
| `2026-06-20 10:50:15` | `cowrie.session.params` |
| `2026-06-20 10:50:15` | `cowrie.command.input` |
| `2026-06-20 10:50:16` | `cowrie.log.closed` |
| `2026-06-20 10:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dabbfec0d6f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:20` | `cowrie.session.connect` |
| `2026-06-20 10:50:20` | `cowrie.client.version` |
| `2026-06-20 10:50:20` | `cowrie.client.kex` |
| `2026-06-20 10:50:21` | `cowrie.login.success` |
| `2026-06-20 10:50:22` | `cowrie.session.params` |
| `2026-06-20 10:50:22` | `cowrie.command.input` |
| `2026-06-20 10:50:22` | `cowrie.log.closed` |
| `2026-06-20 10:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de3823124885

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:26` | `cowrie.session.connect` |
| `2026-06-20 10:50:26` | `cowrie.client.version` |
| `2026-06-20 10:50:26` | `cowrie.client.kex` |
| `2026-06-20 10:50:27` | `cowrie.login.success` |
| `2026-06-20 10:50:28` | `cowrie.session.params` |
| `2026-06-20 10:50:28` | `cowrie.command.input` |
| `2026-06-20 10:50:28` | `cowrie.log.closed` |
| `2026-06-20 10:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9264b32b127

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]186` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:27` | `cowrie.session.connect` |
| `2026-06-20 10:50:28` | `cowrie.client.version` |
| `2026-06-20 10:50:28` | `cowrie.client.kex` |
| `2026-06-20 10:50:30` | `cowrie.login.success` |
| `2026-06-20 10:50:32` | `cowrie.session.params` |
| `2026-06-20 10:50:32` | `cowrie.command.input` |
| `2026-06-20 10:50:33` | `cowrie.log.closed` |
| `2026-06-20 10:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]186` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21551edf3f4d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:32` | `cowrie.session.connect` |
| `2026-06-20 10:50:33` | `cowrie.client.version` |
| `2026-06-20 10:50:33` | `cowrie.client.kex` |
| `2026-06-20 10:50:33` | `cowrie.login.success` |
| `2026-06-20 10:50:34` | `cowrie.session.params` |
| `2026-06-20 10:50:34` | `cowrie.command.input` |
| `2026-06-20 10:50:34` | `cowrie.log.closed` |
| `2026-06-20 10:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af18b0c9d20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:39` | `cowrie.session.connect` |
| `2026-06-20 10:50:39` | `cowrie.client.version` |
| `2026-06-20 10:50:39` | `cowrie.client.kex` |
| `2026-06-20 10:50:40` | `cowrie.login.success` |
| `2026-06-20 10:50:41` | `cowrie.session.params` |
| `2026-06-20 10:50:41` | `cowrie.command.input` |
| `2026-06-20 10:50:42` | `cowrie.log.closed` |
| `2026-06-20 10:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbeded764427

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:45` | `cowrie.session.connect` |
| `2026-06-20 10:50:45` | `cowrie.client.version` |
| `2026-06-20 10:50:45` | `cowrie.client.kex` |
| `2026-06-20 10:50:47` | `cowrie.login.success` |
| `2026-06-20 10:50:48` | `cowrie.session.params` |
| `2026-06-20 10:50:48` | `cowrie.command.input` |
| `2026-06-20 10:50:49` | `cowrie.log.closed` |
| `2026-06-20 10:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c5194b6291

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:51` | `cowrie.session.connect` |
| `2026-06-20 10:50:51` | `cowrie.client.version` |
| `2026-06-20 10:50:51` | `cowrie.client.kex` |
| `2026-06-20 10:50:53` | `cowrie.login.success` |
| `2026-06-20 10:50:55` | `cowrie.session.params` |
| `2026-06-20 10:50:55` | `cowrie.command.input` |
| `2026-06-20 10:50:56` | `cowrie.log.closed` |
| `2026-06-20 10:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7461047585c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:50 |
| **Last Seen** | 2026-06-20 10:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:50:57` | `cowrie.session.connect` |
| `2026-06-20 10:50:57` | `cowrie.client.version` |
| `2026-06-20 10:50:57` | `cowrie.client.kex` |
| `2026-06-20 10:51:00` | `cowrie.login.success` |
| `2026-06-20 10:51:01` | `cowrie.session.params` |
| `2026-06-20 10:51:01` | `cowrie.command.input` |
| `2026-06-20 10:51:01` | `cowrie.log.closed` |
| `2026-06-20 10:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b318bc068bfb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:51 |
| **Last Seen** | 2026-06-20 10:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:51:04` | `cowrie.session.connect` |
| `2026-06-20 10:51:04` | `cowrie.client.version` |
| `2026-06-20 10:51:04` | `cowrie.client.kex` |
| `2026-06-20 10:51:05` | `cowrie.login.success` |
| `2026-06-20 10:51:05` | `cowrie.session.params` |
| `2026-06-20 10:51:05` | `cowrie.command.input` |
| `2026-06-20 10:51:06` | `cowrie.log.closed` |
| `2026-06-20 10:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e6f8c52bf8c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:51 |
| **Last Seen** | 2026-06-20 10:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:51:10` | `cowrie.session.connect` |
| `2026-06-20 10:51:10` | `cowrie.client.version` |
| `2026-06-20 10:51:10` | `cowrie.client.kex` |
| `2026-06-20 10:51:11` | `cowrie.login.success` |
| `2026-06-20 10:51:12` | `cowrie.session.params` |
| `2026-06-20 10:51:12` | `cowrie.command.input` |
| `2026-06-20 10:51:12` | `cowrie.log.closed` |
| `2026-06-20 10:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7afba07fbaa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:51 |
| **Last Seen** | 2026-06-20 10:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:51:16` | `cowrie.session.connect` |
| `2026-06-20 10:51:16` | `cowrie.client.version` |
| `2026-06-20 10:51:16` | `cowrie.client.kex` |
| `2026-06-20 10:51:18` | `cowrie.login.success` |
| `2026-06-20 10:51:19` | `cowrie.session.params` |
| `2026-06-20 10:51:19` | `cowrie.command.input` |
| `2026-06-20 10:51:19` | `cowrie.log.closed` |
| `2026-06-20 10:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3f746e268b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:51 |
| **Last Seen** | 2026-06-20 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:51:22` | `cowrie.session.connect` |
| `2026-06-20 10:51:22` | `cowrie.client.version` |
| `2026-06-20 10:51:23` | `cowrie.client.kex` |
| `2026-06-20 10:51:23` | `cowrie.login.success` |
| `2026-06-20 10:51:24` | `cowrie.session.params` |
| `2026-06-20 10:51:24` | `cowrie.command.input` |
| `2026-06-20 10:51:24` | `cowrie.log.closed` |
| `2026-06-20 10:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c31a4d1351

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:51 |
| **Last Seen** | 2026-06-20 10:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:51:28` | `cowrie.session.connect` |
| `2026-06-20 10:51:29` | `cowrie.client.version` |
| `2026-06-20 10:51:29` | `cowrie.client.kex` |
| `2026-06-20 10:51:30` | `cowrie.login.success` |
| `2026-06-20 10:51:31` | `cowrie.session.params` |
| `2026-06-20 10:51:31` | `cowrie.command.input` |
| `2026-06-20 10:51:31` | `cowrie.log.closed` |
| `2026-06-20 10:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d418d4374bb0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:51 |
| **Last Seen** | 2026-06-20 10:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:51:35` | `cowrie.session.connect` |
| `2026-06-20 10:51:35` | `cowrie.client.version` |
| `2026-06-20 10:51:35` | `cowrie.client.kex` |
| `2026-06-20 10:51:35` | `cowrie.login.success` |
| `2026-06-20 10:51:36` | `cowrie.session.params` |
| `2026-06-20 10:51:36` | `cowrie.command.input` |
| `2026-06-20 10:51:37` | `cowrie.log.closed` |
| `2026-06-20 10:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57789e520824

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:51 |
| **Last Seen** | 2026-06-20 10:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:51:40` | `cowrie.session.connect` |
| `2026-06-20 10:51:41` | `cowrie.client.version` |
| `2026-06-20 10:51:41` | `cowrie.client.kex` |
| `2026-06-20 10:51:42` | `cowrie.login.success` |
| `2026-06-20 10:51:43` | `cowrie.session.params` |
| `2026-06-20 10:51:43` | `cowrie.command.input` |
| `2026-06-20 10:51:43` | `cowrie.log.closed` |
| `2026-06-20 10:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9dd49ecee21

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:51 |
| **Last Seen** | 2026-06-20 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:51:46` | `cowrie.session.connect` |
| `2026-06-20 10:51:47` | `cowrie.client.version` |
| `2026-06-20 10:51:47` | `cowrie.client.kex` |
| `2026-06-20 10:51:47` | `cowrie.login.success` |
| `2026-06-20 10:51:48` | `cowrie.session.params` |
| `2026-06-20 10:51:48` | `cowrie.command.input` |
| `2026-06-20 10:51:48` | `cowrie.log.closed` |
| `2026-06-20 10:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e0a4dad0911

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:51 |
| **Last Seen** | 2026-06-20 10:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:51:52` | `cowrie.session.connect` |
| `2026-06-20 10:51:52` | `cowrie.client.version` |
| `2026-06-20 10:51:52` | `cowrie.client.kex` |
| `2026-06-20 10:51:54` | `cowrie.login.success` |
| `2026-06-20 10:51:55` | `cowrie.session.params` |
| `2026-06-20 10:51:55` | `cowrie.command.input` |
| `2026-06-20 10:51:55` | `cowrie.log.closed` |
| `2026-06-20 10:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885e5f85ef71

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:51 |
| **Last Seen** | 2026-06-20 10:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:51:58` | `cowrie.session.connect` |
| `2026-06-20 10:51:58` | `cowrie.client.version` |
| `2026-06-20 10:51:58` | `cowrie.client.kex` |
| `2026-06-20 10:52:00` | `cowrie.login.success` |
| `2026-06-20 10:52:01` | `cowrie.session.params` |
| `2026-06-20 10:52:01` | `cowrie.command.input` |
| `2026-06-20 10:52:02` | `cowrie.log.closed` |
| `2026-06-20 10:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b75bb33cdc16

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:52 |
| **Last Seen** | 2026-06-20 10:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:52:04` | `cowrie.session.connect` |
| `2026-06-20 10:52:04` | `cowrie.client.version` |
| `2026-06-20 10:52:04` | `cowrie.client.kex` |
| `2026-06-20 10:52:06` | `cowrie.login.success` |
| `2026-06-20 10:52:08` | `cowrie.session.params` |
| `2026-06-20 10:52:08` | `cowrie.command.input` |
| `2026-06-20 10:52:08` | `cowrie.log.closed` |
| `2026-06-20 10:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844c102ce4a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:52 |
| **Last Seen** | 2026-06-20 10:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:52:10` | `cowrie.session.connect` |
| `2026-06-20 10:52:10` | `cowrie.client.version` |
| `2026-06-20 10:52:10` | `cowrie.client.kex` |
| `2026-06-20 10:52:12` | `cowrie.login.success` |
| `2026-06-20 10:52:13` | `cowrie.session.params` |
| `2026-06-20 10:52:13` | `cowrie.command.input` |
| `2026-06-20 10:52:14` | `cowrie.log.closed` |
| `2026-06-20 10:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf51a7bd109

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:52 |
| **Last Seen** | 2026-06-20 10:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:52:16` | `cowrie.session.connect` |
| `2026-06-20 10:52:16` | `cowrie.client.version` |
| `2026-06-20 10:52:16` | `cowrie.client.kex` |
| `2026-06-20 10:52:17` | `cowrie.login.success` |
| `2026-06-20 10:52:18` | `cowrie.session.params` |
| `2026-06-20 10:52:18` | `cowrie.command.input` |
| `2026-06-20 10:52:19` | `cowrie.log.closed` |
| `2026-06-20 10:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e082313856aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:52 |
| **Last Seen** | 2026-06-20 10:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:52:22` | `cowrie.session.connect` |
| `2026-06-20 10:52:22` | `cowrie.client.version` |
| `2026-06-20 10:52:22` | `cowrie.client.kex` |
| `2026-06-20 10:52:24` | `cowrie.login.success` |
| `2026-06-20 10:52:25` | `cowrie.session.params` |
| `2026-06-20 10:52:25` | `cowrie.command.input` |
| `2026-06-20 10:52:25` | `cowrie.log.closed` |
| `2026-06-20 10:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3042e558b708

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:52 |
| **Last Seen** | 2026-06-20 10:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:52:28` | `cowrie.session.connect` |
| `2026-06-20 10:52:28` | `cowrie.client.version` |
| `2026-06-20 10:52:28` | `cowrie.client.kex` |
| `2026-06-20 10:52:29` | `cowrie.login.success` |
| `2026-06-20 10:52:30` | `cowrie.session.params` |
| `2026-06-20 10:52:30` | `cowrie.command.input` |
| `2026-06-20 10:52:31` | `cowrie.log.closed` |
| `2026-06-20 10:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0bfc9029fc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:52 |
| **Last Seen** | 2026-06-20 10:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:52:34` | `cowrie.session.connect` |
| `2026-06-20 10:52:34` | `cowrie.client.version` |
| `2026-06-20 10:52:34` | `cowrie.client.kex` |
| `2026-06-20 10:52:35` | `cowrie.login.success` |
| `2026-06-20 10:52:36` | `cowrie.session.params` |
| `2026-06-20 10:52:36` | `cowrie.command.input` |
| `2026-06-20 10:52:37` | `cowrie.log.closed` |
| `2026-06-20 10:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-110d5f88dd38

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:52 |
| **Last Seen** | 2026-06-20 10:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:52:40` | `cowrie.session.connect` |
| `2026-06-20 10:52:41` | `cowrie.client.version` |
| `2026-06-20 10:52:41` | `cowrie.client.kex` |
| `2026-06-20 10:52:41` | `cowrie.login.success` |
| `2026-06-20 10:52:42` | `cowrie.session.params` |
| `2026-06-20 10:52:42` | `cowrie.command.input` |
| `2026-06-20 10:52:43` | `cowrie.log.closed` |
| `2026-06-20 10:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55afa1d60e76

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:52 |
| **Last Seen** | 2026-06-20 10:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:52:47` | `cowrie.session.connect` |
| `2026-06-20 10:52:48` | `cowrie.client.version` |
| `2026-06-20 10:52:48` | `cowrie.client.kex` |
| `2026-06-20 10:52:49` | `cowrie.login.success` |
| `2026-06-20 10:52:50` | `cowrie.session.params` |
| `2026-06-20 10:52:50` | `cowrie.command.input` |
| `2026-06-20 10:52:50` | `cowrie.log.closed` |
| `2026-06-20 10:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-094f897b17a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:52 |
| **Last Seen** | 2026-06-20 10:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:52:53` | `cowrie.session.connect` |
| `2026-06-20 10:52:53` | `cowrie.client.version` |
| `2026-06-20 10:52:53` | `cowrie.client.kex` |
| `2026-06-20 10:52:53` | `cowrie.login.success` |
| `2026-06-20 10:52:55` | `cowrie.session.params` |
| `2026-06-20 10:52:55` | `cowrie.command.input` |
| `2026-06-20 10:52:55` | `cowrie.log.closed` |
| `2026-06-20 10:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c393e42071

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:52 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:52:58` | `cowrie.session.connect` |
| `2026-06-20 10:52:59` | `cowrie.client.version` |
| `2026-06-20 10:52:59` | `cowrie.client.kex` |
| `2026-06-20 10:53:00` | `cowrie.login.success` |
| `2026-06-20 10:53:01` | `cowrie.session.params` |
| `2026-06-20 10:53:01` | `cowrie.command.input` |
| `2026-06-20 10:53:01` | `cowrie.log.closed` |
| `2026-06-20 10:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbe2718edb29

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:05` | `cowrie.session.connect` |
| `2026-06-20 10:53:05` | `cowrie.client.version` |
| `2026-06-20 10:53:05` | `cowrie.client.kex` |
| `2026-06-20 10:53:06` | `cowrie.login.success` |
| `2026-06-20 10:53:08` | `cowrie.session.params` |
| `2026-06-20 10:53:08` | `cowrie.command.input` |
| `2026-06-20 10:53:08` | `cowrie.log.closed` |
| `2026-06-20 10:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d68de56b0c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:11` | `cowrie.session.connect` |
| `2026-06-20 10:53:11` | `cowrie.client.version` |
| `2026-06-20 10:53:11` | `cowrie.client.kex` |
| `2026-06-20 10:53:12` | `cowrie.login.success` |
| `2026-06-20 10:53:13` | `cowrie.session.params` |
| `2026-06-20 10:53:13` | `cowrie.command.input` |
| `2026-06-20 10:53:13` | `cowrie.log.closed` |
| `2026-06-20 10:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8915203d215f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:17` | `cowrie.session.connect` |
| `2026-06-20 10:53:17` | `cowrie.client.version` |
| `2026-06-20 10:53:17` | `cowrie.client.kex` |
| `2026-06-20 10:53:18` | `cowrie.login.success` |
| `2026-06-20 10:53:18` | `cowrie.session.params` |
| `2026-06-20 10:53:18` | `cowrie.command.input` |
| `2026-06-20 10:53:19` | `cowrie.log.closed` |
| `2026-06-20 10:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42eef575d6f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:23` | `cowrie.session.connect` |
| `2026-06-20 10:53:24` | `cowrie.client.version` |
| `2026-06-20 10:53:24` | `cowrie.client.kex` |
| `2026-06-20 10:53:25` | `cowrie.login.success` |
| `2026-06-20 10:53:27` | `cowrie.session.params` |
| `2026-06-20 10:53:27` | `cowrie.command.input` |
| `2026-06-20 10:53:27` | `cowrie.log.closed` |
| `2026-06-20 10:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4715ef053d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:29` | `cowrie.session.connect` |
| `2026-06-20 10:53:29` | `cowrie.client.version` |
| `2026-06-20 10:53:29` | `cowrie.client.kex` |
| `2026-06-20 10:53:31` | `cowrie.login.success` |
| `2026-06-20 10:53:33` | `cowrie.session.params` |
| `2026-06-20 10:53:33` | `cowrie.command.input` |
| `2026-06-20 10:53:34` | `cowrie.log.closed` |
| `2026-06-20 10:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98fceae1a488

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:35` | `cowrie.session.connect` |
| `2026-06-20 10:53:35` | `cowrie.client.version` |
| `2026-06-20 10:53:35` | `cowrie.client.kex` |
| `2026-06-20 10:53:37` | `cowrie.login.success` |
| `2026-06-20 10:53:39` | `cowrie.session.params` |
| `2026-06-20 10:53:39` | `cowrie.command.input` |
| `2026-06-20 10:53:40` | `cowrie.log.closed` |
| `2026-06-20 10:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72f11f1b1f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:41` | `cowrie.session.connect` |
| `2026-06-20 10:53:41` | `cowrie.client.version` |
| `2026-06-20 10:53:41` | `cowrie.client.kex` |
| `2026-06-20 10:53:44` | `cowrie.login.success` |
| `2026-06-20 10:53:46` | `cowrie.session.params` |
| `2026-06-20 10:53:46` | `cowrie.command.input` |
| `2026-06-20 10:53:46` | `cowrie.log.closed` |
| `2026-06-20 10:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa31f7c7335

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:47` | `cowrie.session.connect` |
| `2026-06-20 10:53:47` | `cowrie.client.version` |
| `2026-06-20 10:53:47` | `cowrie.client.kex` |
| `2026-06-20 10:53:49` | `cowrie.login.success` |
| `2026-06-20 10:53:51` | `cowrie.session.params` |
| `2026-06-20 10:53:51` | `cowrie.command.input` |
| `2026-06-20 10:53:52` | `cowrie.log.closed` |
| `2026-06-20 10:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb7241f7012

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:53` | `cowrie.session.connect` |
| `2026-06-20 10:53:53` | `cowrie.client.version` |
| `2026-06-20 10:53:53` | `cowrie.client.kex` |
| `2026-06-20 10:53:56` | `cowrie.login.success` |
| `2026-06-20 10:53:58` | `cowrie.session.params` |
| `2026-06-20 10:53:58` | `cowrie.command.input` |
| `2026-06-20 10:53:58` | `cowrie.log.closed` |
| `2026-06-20 10:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1355fd47b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:59` | `cowrie.session.connect` |
| `2026-06-20 10:54:00` | `cowrie.client.version` |
| `2026-06-20 10:54:00` | `cowrie.client.kex` |
| `2026-06-20 10:54:02` | `cowrie.login.success` |
| `2026-06-20 10:54:05` | `cowrie.session.params` |
| `2026-06-20 10:54:05` | `cowrie.command.input` |
| `2026-06-20 10:54:06` | `cowrie.log.closed` |
| `2026-06-20 10:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39ee4fccd28b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:54 |
| **Last Seen** | 2026-06-20 10:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:54:05` | `cowrie.session.connect` |
| `2026-06-20 10:54:05` | `cowrie.client.version` |
| `2026-06-20 10:54:05` | `cowrie.client.kex` |
| `2026-06-20 10:54:08` | `cowrie.login.success` |
| `2026-06-20 10:54:11` | `cowrie.session.params` |
| `2026-06-20 10:54:11` | `cowrie.command.input` |
| `2026-06-20 10:54:12` | `cowrie.log.closed` |
| `2026-06-20 10:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c851f5a81daa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:54 |
| **Last Seen** | 2026-06-20 10:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:54:11` | `cowrie.session.connect` |
| `2026-06-20 10:54:11` | `cowrie.client.version` |
| `2026-06-20 10:54:11` | `cowrie.client.kex` |
| `2026-06-20 10:54:15` | `cowrie.login.success` |
| `2026-06-20 10:54:18` | `cowrie.session.params` |
| `2026-06-20 10:54:18` | `cowrie.command.input` |
| `2026-06-20 10:54:19` | `cowrie.log.closed` |
| `2026-06-20 10:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-404fd1a45db2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:54 |
| **Last Seen** | 2026-06-20 10:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:54:17` | `cowrie.session.connect` |
| `2026-06-20 10:54:18` | `cowrie.client.version` |
| `2026-06-20 10:54:18` | `cowrie.client.kex` |
| `2026-06-20 10:54:22` | `cowrie.login.success` |
| `2026-06-20 10:54:25` | `cowrie.session.params` |
| `2026-06-20 10:54:25` | `cowrie.command.input` |
| `2026-06-20 10:54:26` | `cowrie.log.closed` |
| `2026-06-20 10:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87516de208e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:54 |
| **Last Seen** | 2026-06-20 10:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:54:23` | `cowrie.session.connect` |
| `2026-06-20 10:54:24` | `cowrie.client.version` |
| `2026-06-20 10:54:24` | `cowrie.client.kex` |
| `2026-06-20 10:54:29` | `cowrie.login.success` |
| `2026-06-20 10:54:32` | `cowrie.session.params` |
| `2026-06-20 10:54:32` | `cowrie.command.input` |
| `2026-06-20 10:54:33` | `cowrie.log.closed` |
| `2026-06-20 10:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f4ddfd937d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:54 |
| **Last Seen** | 2026-06-20 10:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:54:29` | `cowrie.session.connect` |
| `2026-06-20 10:54:30` | `cowrie.client.version` |
| `2026-06-20 10:54:30` | `cowrie.client.kex` |
| `2026-06-20 10:54:34` | `cowrie.login.success` |
| `2026-06-20 10:54:35` | `cowrie.session.params` |
| `2026-06-20 10:54:35` | `cowrie.command.input` |
| `2026-06-20 10:54:36` | `cowrie.log.closed` |
| `2026-06-20 10:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a4765e55259

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:54 |
| **Last Seen** | 2026-06-20 10:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:54:36` | `cowrie.session.connect` |
| `2026-06-20 10:54:37` | `cowrie.client.version` |
| `2026-06-20 10:54:37` | `cowrie.client.kex` |
| `2026-06-20 10:54:40` | `cowrie.login.success` |
| `2026-06-20 10:54:43` | `cowrie.session.params` |
| `2026-06-20 10:54:43` | `cowrie.command.input` |
| `2026-06-20 10:54:44` | `cowrie.log.closed` |
| `2026-06-20 10:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1cf9d48137

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:54 |
| **Last Seen** | 2026-06-20 10:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:54:42` | `cowrie.session.connect` |
| `2026-06-20 10:54:43` | `cowrie.client.version` |
| `2026-06-20 10:54:43` | `cowrie.client.kex` |
| `2026-06-20 10:54:47` | `cowrie.login.success` |
| `2026-06-20 10:54:50` | `cowrie.session.params` |
| `2026-06-20 10:54:50` | `cowrie.command.input` |
| `2026-06-20 10:54:51` | `cowrie.log.closed` |
| `2026-06-20 10:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-833fe593aa5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:54 |
| **Last Seen** | 2026-06-20 10:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:54:47` | `cowrie.session.connect` |
| `2026-06-20 10:54:49` | `cowrie.client.version` |
| `2026-06-20 10:54:49` | `cowrie.client.kex` |
| `2026-06-20 10:54:53` | `cowrie.login.success` |
| `2026-06-20 10:54:56` | `cowrie.session.params` |
| `2026-06-20 10:54:56` | `cowrie.command.input` |
| `2026-06-20 10:54:57` | `cowrie.log.closed` |
| `2026-06-20 10:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5f4d7e0826

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]124` |
| **First Seen** | 2026-06-20 10:54 |
| **Last Seen** | 2026-06-20 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:54:54` | `cowrie.session.connect` |
| `2026-06-20 10:54:55` | `cowrie.client.version` |
| `2026-06-20 10:54:55` | `cowrie.client.kex` |
| `2026-06-20 10:54:59` | `cowrie.login.success` |
| `2026-06-20 10:55:04` | `cowrie.session.params` |
| `2026-06-20 10:55:04` | `cowrie.command.input` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]124` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `138.68.100[.]228` | **356** | 2026-06-20 08:55 | 2026-06-20 10:54 | 381m | 0 | `T1592` | 🟠 MEDIUM |
| `45.198.224[.]120` | **7** | 2026-06-20 09:19 | 2026-06-20 10:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.91.11[.]226` | **4** | 2026-06-20 09:13 | 2026-06-20 10:39 | 1m | 0 | `T1592` | 🟢 LOW |
| `27.79.7[.]135` | **4** | 2026-06-20 09:37 | 2026-06-20 10:05 | 3m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.206.107[.]245` | **3** | 2026-06-20 10:06 | 2026-06-20 10:41 | 2m | 0 | `T1592` | 🟢 LOW |
| `106.12.148[.]154` | **2** | 2026-06-20 09:44 | 2026-06-20 09:46 | 2m | 0 | `T1592` | 🟢 LOW |
| `36.41.186[.]9` | **2** | 2026-06-20 09:36 | 2026-06-20 09:38 | 2m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]186` | **2** | 2026-06-20 09:58 | 2026-06-20 10:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]124` | **2** | 2026-06-20 10:32 | 2026-06-20 10:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `134.122.78[.]248` | 1 | 2026-06-20 09:50 | 2026-06-20 09:51 | 30s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]129` | 1 | 2026-06-20 09:11 | 2026-06-20 09:11 | 2s | 0 | `T1592` | 🟢 LOW |
| `2.180.242[.]118` | 1 | 2026-06-20 10:48 | 2026-06-20 10:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-06-20 10:34 | 2026-06-20 10:34 | 10s | 0 | `T1592` | 🟢 LOW |
| `222.97.3[.]135` | 1 | 2026-06-20 10:19 | 2026-06-20 10:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-06-20 10:04 | 2026-06-20 10:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-20 10:25 | 2026-06-20 10:27 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (17 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **13/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `195.96.139[.]129` | GB | Driftnet Ltd | **100** ⚠️ | 7 |
| `106.12.148[.]154` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 27 |
| `183.91.11[.]226` | VN | CMC Telecom Infrastructure Company | **100** ⚠️ | 4 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `91.92.40[.]124` | NL | TechTies Inc. | **100** ⚠️ | 5 |
| `101.206.107[.]245` | CN | UNICOM Sichuan province network | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `36.41.186[.]9` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 43 |
| `212.227.235[.]203` | ES | IONOS SE | **100** ⚠️ | 3 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 269 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 245 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 652 cases |
| Tool 34  | Credential Extractor        | ✅ 246 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (2.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 245 priority case(s) shown individually · 16 recon entry/entries in table (9 group(s) consolidating 382 session(s)).

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
| CIS-1 | Asset Inventory | ACTIVE | assets.json updated every pipeline run by Tool 05 |
| CIS-2 | Software Inventory | MONITORING | tool_manifest.yaml tracks pipeline tools |
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
_Report time: 2026-06-20T12:00:06Z_

